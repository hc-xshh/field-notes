#!/usr/bin/env python3
"""Which living pages need a re-read?

Every post that declares `refresh:` in its frontmatter is a page whose numbers move.
This script asks each page's source whether anything newer than the page's own
`data_checked` exists, and prints what to do about it.

Pages whose source answers without an API key are checked live (UN Comtrade,
World Bank, Hugging Face). The rest print a short checklist: the URL to open and
what to compare, because their numbers live behind a rendered page or a bulletin
that has to be read, not parsed.

    python3 scripts/refresh_pages.py            # the whole list
    python3 scripts/refresh_pages.py --verbose  # sources even for pages that are current

Exit code is 1 when at least one page has new data waiting, so it can gate a release.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS = os.path.join(ROOT, "src", "content", "posts")
UA = "field-notes-refresh-check/1.0 (+https://field-notes-6cd.pages.dev/)"
CADENCE_DAYS = {"weekly": 7, "monthly": 31, "quarterly": 92, "annual": 365}

# What each living page is checked against. `data_year` is the newest year the page
# currently carries: when the source has that year + 1, the page needs a new row.
CONFIG: dict[str, dict] = {
    "one-commodity-through-un-comtrade": {
        "kind": "comtrade",
        "data_year": 2025,
        "reporter": 156,  # China
        "partner": 842,  # United States
        "cmd": "850760",  # lithium-ion accumulators
        "note": "annual mirror statistics, China exports to the US",
    },
    "urbanisation-rate-versus-one-county": {
        "kind": "worldbank",
        "country": "CHN",
        "indicator": "SP.URB.TOTL.IN.ZS",
        "data_year": 2025,
        "note": "World Bank urban share (the UN series, not the NBS count)",
    },
    "chinese-open-weights-timeline": {
        "kind": "huggingface",
        "note": "newest weights on the Hugging Face orgs this page already links to",
    },
}

# Pages whose numbers cannot be fetched safely: open the URL, compare by eye.
MANUAL: dict[str, list[tuple[str, str]]] = {
    "llm-api-pricing-per-task": [
        (
            "OpenAI / Google / DeepSeek / Anthropic price pages",
            "https://platform.openai.com/docs/pricing  ·  https://ai.google.dev/gemini-api/docs/pricing  ·  https://api-docs.deepseek.com/quick_start/pricing",
        ),
        ("what to compare", "the per-million input/output prices behind each job's total; the Gemini page renders client-side, so open it in a browser"),
    ],
    "container-freight-rates-by-route": [
        ("Freightos route terminals", "https://www.freightos.com/enterprise/terminal/fbx-01-china-to-north-america-west-coast/ and the other FBX pages"),
        ("what to compare", "each lane's headline number and the week it carries; the pages do not update on the same day"),
        ("second index", "Drewry WCI and the SCFI commentary, to keep the 'indices disagree' section honest"),
    ],
    "grocery-cost-by-channel": [
        ("municipal price bulletin", "https://fgw.beijing.gov.cn/gzdt/fgzs/gzdt/  (the monthly 价格监测 bulletin)"),
        ("what to compare", "wholesale / farm-market / supermarket columns for the categories in the table, and the month the bulletin covers"),
    ],
    "cost-of-living-by-city-for-chinese-abroad": [
        ("Numbeo city pages or official statistics", "https://www.numbeo.com/cost-of-living/"),
        ("what to compare", "rent, transport pass and the monthly total for each of the eight cities; note which month each figure is from"),
    ],
    "china-price-versus-overseas-price": [
        ("both sides of each comparison", "the Chinese price page and the overseas retailer page for the same item"),
        ("what to compare", "unit price, size, and whether tax is included — the whole point of the page is that the two sides are not quoted the same way"),
    ],
    "parcels-china-and-the-world": [
        ("State Post Bureau monthly release", "https://www.spb.gov.cn/"),
        ("what to compare", "the annual or year-to-date parcel count and the growth rate against the table's last row"),
    ],
    "leaving-and-returning-checklist": [
        ("exit/entry and household-registration pages", "https://www.nia.gov.cn/  ·  https://www.mps.gov.cn/"),
        ("what to compare", "whether any listed step, fee or waiting time changed; this page is re-checked when the rule changes, not on a date"),
    ],
}


def get_json(url: str, tries: int = 3, timeout: int = 30):
    last = None
    for _ in range(tries):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8", "replace"))
        except Exception as exc:  # noqa: BLE001 - reported, not raised
            last = exc
    raise RuntimeError(f"{url} -> {last}")


def read_front(slug: str) -> dict:
    text = open(os.path.join(POSTS, slug + ".md"), encoding="utf-8").read()
    fm = text.split("---\n")[1]
    out = {}
    for key in ("refresh", "data_checked", "title"):
        m = re.search(rf"^{key}: *(.+)$", fm, re.M)
        if m:
            out[key] = m.group(1).strip()
    return out


def living_pages() -> list[str]:
    slugs = []
    for name in sorted(os.listdir(POSTS)):
        if not name.endswith(".md"):
            continue
        slug = name[:-3]
        if read_front(slug).get("refresh"):
            slugs.append(slug)
    return slugs


def next_due(checked: dt.date, cadence: str) -> str:
    days = CADENCE_DAYS.get(cadence)
    return (checked + dt.timedelta(days=days)).isoformat() if days else "—"


# --------------------------------------------------------------------------
# Checks. Each returns (verdict, detail) with verdict in NEW / CURRENT / UNREACHABLE.
# --------------------------------------------------------------------------
def check_comtrade(slug: str, cfg: dict, checked: dt.date) -> tuple[str, str]:
    year = cfg["data_year"]
    base = "https://comtradeapi.un.org/public/v1/preview/C/A/HS"
    found = {}
    for probe in (year, year + 1):
        url = (
            f"{base}?reporterCode={cfg['reporter']}&period={probe}"
            f"&cmdCode={cfg['cmd']}&flowCode=X&partnerCode={cfg['partner']}"
        )
        try:
            data = get_json(url)
        except RuntimeError as exc:
            return "UNREACHABLE", str(exc)[:160]
        found[probe] = int(data.get("count") or 0) if isinstance(data, dict) else 0
    if found.get(year + 1):
        return "NEW", f"the source now has {year + 1} annual data ({found[year + 1]} record(s)) — add the row"
    if not found.get(year):
        return "UNREACHABLE", f"no {year} records either (counts {found}) — check the query before trusting this"
    return "CURRENT", f"still {year}; {year + 1} not published yet ({found[year]} record(s) for {year})"


def check_worldbank(slug: str, cfg: dict, checked: dt.date) -> tuple[str, str]:
    url = (
        f"https://api.worldbank.org/v2/country/{cfg['country']}/indicator/{cfg['indicator']}"
        "?format=json&per_page=100&date=2015:2035"
    )
    try:
        data = get_json(url)
    except RuntimeError as exc:
        return "UNREACHABLE", str(exc)[:160]
    rows = [(int(r["date"]), r["value"]) for r in (data[1] or []) if r.get("value") is not None]
    if not rows:
        return "UNREACHABLE", "no values returned"
    year, value = max(rows)
    if year > cfg["data_year"]:
        return "NEW", f"the series now runs to {year}: {value:.2f}% — add the year"
    return "CURRENT", f"latest available year is still {year} ({value:.2f}%)"


def check_huggingface(slug: str, cfg: dict, checked: dt.date) -> tuple[str, str]:
    text = open(os.path.join(POSTS, slug + ".md"), encoding="utf-8").read()
    orgs = sorted({m.group(1) for m in re.finditer(r"huggingface\.co/([A-Za-z0-9_.-]+)/", text)})
    if not orgs:
        return "UNREACHABLE", "no Hugging Face orgs found in the page"
    newest, unreachable = [], []
    for org in orgs:
        url = f"https://huggingface.co/api/models?author={org}&sort=createdAt&direction=-1&limit=1"
        try:
            data = get_json(url)
        except RuntimeError:
            unreachable.append(org)
            continue
        if isinstance(data, list) and data:
            entry = data[0]
            newest.append((entry.get("createdAt", "")[:10], org, entry.get("modelId") or entry.get("id")))
    if not newest:
        return "UNREACHABLE", f"no org answered ({len(unreachable)} tried)"
    date, org, model = max(newest)
    tail = f"; {len(unreachable)} org(s) unreachable" if unreachable else ""
    if date > checked.isoformat():
        return "NEW", f"{org}/{model} landed {date}, after this page's {checked} — add it{tail}"
    return "CURRENT", f"newest across {len(newest)} orgs is {org}/{model} at {date}{tail}"


CHECKS = {
    "comtrade": check_comtrade,
    "worldbank": check_worldbank,
    "huggingface": check_huggingface,
}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--verbose", action="store_true", help="print the checklist for current pages too")
    args = ap.parse_args()

    pages = living_pages()
    if not pages:
        print("No page declares `refresh:` — nothing to check.")
        return 0

    today = dt.date.today()
    rows, new_pages, unreachable = [], [], []
    for slug in pages:
        front = read_front(slug)
        cadence = front.get("refresh", "?")
        checked = dt.date.fromisoformat(front.get("data_checked", front.get("date", "1970-01-01")))
        cfg = CONFIG.get(slug)
        if cfg:
            verdict, detail = CHECKS[cfg["kind"]](slug, cfg, checked)
        else:
            verdict, detail = "MANUAL", "open the sources below and compare by eye"
        if verdict == "NEW":
            new_pages.append(slug)
        if verdict == "UNREACHABLE":
            unreachable.append(slug)
        rows.append((slug, cadence, checked.isoformat(), next_due(checked, cadence), verdict, detail))

    width = max(len(r[0]) for r in rows)
    print(f"Living pages · checked {today.isoformat()}\n")
    for slug, cadence, checked, due, verdict, detail in rows:
        print(f"{slug:<{width}}  {cadence:<9} read {checked}  due {due}  {verdict}")
        print(f"{'':<{width}}  {detail}")
        if verdict == "MANUAL" or args.verbose:
            for label, what in MANUAL.get(slug, []):
                print(f"{'':<{width}}    · {label}: {what}")
        print()

    print(f"{len(rows)} living page(s); {len(new_pages)} with new data; {len(unreachable)} unreachable.")
    if new_pages:
        print("Needs a re-read: " + ", ".join(new_pages))
        print(
            "To refresh one: edit the table, set `data_checked:` to today, keep the source link "
            "and its retrieval date in the text, rebuild, push."
        )
    return 1 if new_pages else 0


if __name__ == "__main__":
    sys.exit(main())
