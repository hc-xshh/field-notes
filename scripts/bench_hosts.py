#!/usr/bin/env python3
"""Reachability + latency of the hosts a static site depends on, from this
machine, direct connection (no proxy). Each host is tried twice; the faster
attempt is reported. Writes a TSV next to itself.

Usage: python3 bench_hosts.py [--proxy]
"""
import json, os, subprocess, sys, time

HOSTS = [
    ("Google Fonts CSS", "https://fonts.googleapis.com/css2?family=Inter:wght@400..700&display=swap"),
    ("Google Fonts files", "https://fonts.gstatic.com/s/inter/v13/UcCO3FwrK3iLTeHuS_fvQtMwCp50KnMw2boKoduKmMEVuLyfAZ9hiJ-Ek-_EeA.woff2"),
    ("fonts.bunny.net", "https://fonts.bunny.net/css?family=inter:400,700"),
    ("jsDelivr", "https://cdn.jsdelivr.net/npm/astro/package.json"),
    ("unpkg", "https://unpkg.com/astro/package.json"),
    ("npm registry", "https://registry.npmjs.org/astro"),
    ("npmmirror", "https://registry.npmmirror.com/astro"),
    ("cdnjs", "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js"),
    ("Tailwind CDN", "https://cdn.tailwindcss.com/"),
    ("MailerLite widget JS", "https://assets.mailerlite.com/js/universal.js"),
    ("MailerLite API", "https://api.mailerlite.com/api/v2/"),
    ("github.com", "https://github.com/withastro/astro"),
    ("raw.githubusercontent", "https://raw.githubusercontent.com/withastro/astro/main/README.md"),
    ("Cloudflare API", "https://api.cloudflare.com/client/v4/"),
    ("Cloudflare Pages (Field Notes)", "https://field-notes-6cd.pages.dev/"),
    ("Cloudflare Pages (daily-hub)", "https://daily-hub-xshh.pages.dev/"),
    ("Google (baseline)", "https://www.google.com/"),
    ("r.jina.ai", "https://r.jina.ai/https://example.com"),
]

USE_PROXY = "--proxy" in sys.argv
env = dict(os.environ)
for k in ("HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy", "ALL_PROXY", "all_proxy"):
    env.pop(k, None)
env["NO_PROXY"] = "*"
if USE_PROXY:
    env["HTTPS_PROXY"] = env["HTTP_PROXY"] = "http://127.0.0.1:7890"
    env["NO_PROXY"] = "127.0.0.1,localhost"

rows = []
print(f"{'host':<34}{'code':>6}{'t_total':>9}{'t_connect':>11}{'tls':>8}{'bytes':>10}  attempts")
print("-" * 92)
for label, url in HOSTS:
    best = None
    codes = []
    for attempt in range(2):
        cmd = ["curl", "-sS", "-o", "/dev/null", "--max-time", "8",
               "-w", "%{http_code}\t%{time_total}\t%{time_connect}\t%{time_appconnect}\t%{size_download}",
               "-L", url]
        try:
            out = subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=20).stdout.strip()
            code, t, tc, tls, size = out.split("\t")
            codes.append(code)
            if code != "000":
                rec = (float(t), float(tc), float(tls), int(size), code)
                if best is None or rec[0] < best[0]:
                    best = rec
        except Exception as e:
            codes.append(f"err:{type(e).__name__}")
        time.sleep(0.3)
    if best:
        t, tc, tls, size, code = best
        print(f"{label:<34}{code:>6}{t:>9.2f}{tc:>11.2f}{tls:>8.2f}{size:>10}  {','.join(codes)}")
        rows.append((label, url, code, t, tc, tls, size))
    else:
        print(f"{label:<34}{'---':>6}{'-':>9}{'-':>11}{'-':>8}{'-':>10}  {','.join(codes)}  UNREACHABLE")
        rows.append((label, url, "000", None, None, None, None))

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "bench_proxy.tsv" if USE_PROXY else "bench_direct.tsv")
with open(out_path, "w") as f:
    f.write("host\turl\tcode\ttotal_s\tconnect_s\ttls_s\tbytes\n")
    for r in rows:
        f.write("\t".join("" if v is None else str(v) for v in r) + "\n")
print("\nwrote", out_path, "|", time.strftime("%Y-%m-%d %H:%M:%S %Z"))
