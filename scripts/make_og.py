#!/usr/bin/env python3
"""Generate the 1200x630 social cards (og:image) for the site and every post.

Cards are rendered by headless Chrome from a small HTML template that uses the
same self-hosted fonts as the site, so a card and the page it previews look
like the same object. Output goes to public/og/<id>.png (one per post) plus
public/og/default.png for non-post pages.

Run it after adding a post, then commit the PNGs:

    python3 scripts/make_og.py

Why pre-rendered files instead of a build-time image service: the site is
purely static with no Functions and no extra build dependencies. The trade-off
is one manual command when a post is added — documented here and in README.md.
"""
import http.server, json, os, pathlib, re, shutil, socketserver, subprocess, sys, threading, time

ROOT = pathlib.Path(__file__).resolve().parent.parent
PUBLIC = ROOT / 'public'
POSTS = ROOT / 'src/content/posts'
OUT = PUBLIC / 'og'
TMP = PUBLIC / '.og-tmp'
PORT = 8099
SITE = 'field-notes-6cd.pages.dev'

CARD = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<style>
  @font-face { font-family: 'Inter'; src: url('/fonts/inter-var.woff2') format('woff2');
    font-weight: 400 900; font-style: normal; font-display: block; }
  @font-face { font-family: 'Newsreader'; src: url('/fonts/newsreader-var.woff2') format('woff2');
    font-weight: 200 800; font-style: normal; font-display: block; }
  * { box-sizing: border-box; margin: 0; }
  html, body { width: 1200px; height: 630px; }
  body {
    background: #fbfaf7; color: #17171b; font-family: 'Inter', 'PingFang SC', 'Noto Sans CJK SC', 'Microsoft YaHei', sans-serif;
    padding: 64px 72px 56px; display: flex; flex-direction: column;
    border: 1px solid #e7e3db;
  }
  .brand { font-size: 20px; font-weight: 600; letter-spacing: .16em;
    text-transform: uppercase; color: #a4401a; }
  .brand span { color: #6d6d78; letter-spacing: .1em; font-weight: 500; }
  .body { flex: 1; display: flex; align-items: center; }
  h1 { font-family: 'Newsreader', 'Songti SC', 'Noto Serif CJK SC', 'SimSun', serif; font-weight: 600; line-height: 1.12;
    letter-spacing: -.01em; font-size: __SIZE__px; }
  .foot { border-top: 1px solid #d5cfc4; padding-top: 22px; display: flex;
    justify-content: space-between; align-items: baseline;
    font-family: ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
    font-size: 19px; color: #6d6d78; }
  .foot .dot { color: #a4401a; }
</style></head>
<body>
  <div class="brand">Field Notes &nbsp;<span>__BRANDSMALL__</span></div>
  <div class="body"><h1>__TITLE__</h1></div>
  <div class="foot"><span>__META__</span><span class="dot">__RIGHT__</span></div>
</body></html>
'''


def esc(s: str) -> str:
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))


def title_size(title: str) -> int:
    n = len(title)
    if n <= 34:
        return 92
    if n <= 55:
        return 76
    if n <= 80:
        return 62
    if n <= 108:
        return 52
    return 44


def card_html(title, meta, right, brand_small='AI tooling, tested'):
    return (CARD.replace('__SIZE__', str(title_size(title)))
                .replace('__BRANDSMALL__', esc(brand_small))
                .replace('__TITLE__', esc(title))
                .replace('__META__', esc(meta))
                .replace('__RIGHT__', esc(right)))


def parse_post(path: pathlib.Path):
    raw = path.read_text()
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', raw, re.S)
    if not m:
        raise SystemExit(f'{path.name}: no frontmatter')
    fm, body = m.group(1), m.group(2)
    data = {}
    for line in fm.splitlines():
        mm = re.match(r'^(\w+):\s*(.*)$', line.strip())
        if mm:
            data[mm.group(1)] = mm.group(2).strip().strip('"\'')
    if str(data.get('draft', 'false')).lower() == 'true':
        return None
    cjk = len(re.findall(r'[\u4e00-\u9fff]', body))
    words = len(body.split())
    minutes = max(1, round(max(0, words - cjk) / 220 + cjk / 400))
    return {
        'id': path.stem,
        'title': data.get('title', path.stem),
        'date': (data.get('date') or '')[:10],
        'meta': f"{data.get('date', '')[:10]}  ·  {minutes} min read",
    }


def serve(directory: pathlib.Path, port: int):
    handler = lambda *a, **k: http.server.SimpleHTTPRequestHandler(*a, directory=str(directory), **k)
    httpd = socketserver.TCPServer(('127.0.0.1', port), handler)
    httpd.allow_reuse_address = True
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def shoot(url: str, out: pathlib.Path):
    out.parent.mkdir(parents=True, exist_ok=True)
    cmd = ['google-chrome', '--headless=new', '--disable-gpu', '--no-sandbox',
           '--hide-scrollbars', '--force-device-scale-factor=1',
           '--window-size=1200,630', '--virtual-time-budget=3000',
           f'--screenshot={out}', url]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if not out.exists():
        raise SystemExit(f'chrome failed for {url}\n{r.stderr[-800:]}')


def dims(png: pathlib.Path):
    b = png.read_bytes()[:33]
    if b[:8] != b'\x89PNG\r\n\x1a\n':
        return None
    return int.from_bytes(b[16:20], 'big'), int.from_bytes(b[20:24], 'big')


def main():
    shutil.rmtree(TMP, ignore_errors=True)
    TMP.mkdir(parents=True)
    OUT.mkdir(parents=True, exist_ok=True)

    cards = [('default', card_html('Field Notes',
                                   'Notes on building, testing and shipping AI tooling.',
                                   SITE, brand_small='no ads, no tracking'))]
    for p in sorted(POSTS.glob('*.md')):
        post = parse_post(p)
        if post:
            cards.append((post['id'],
                          card_html(post['title'], post['meta'], SITE)))

    for slug, html in cards:
        (TMP / f'{slug}.html').write_text(html)
    print(f'{len(cards)} cards written to {TMP}')

    httpd = serve(PUBLIC, PORT)
    time.sleep(0.4)
    rows = []
    try:
        for slug, _ in cards:
            out = OUT / f'{slug}.png'
            shoot(f'http://127.0.0.1:{PORT}/.og-tmp/{slug}.html', out)
            d = dims(out)
            rows.append((slug, out.stat().st_size, d))
    finally:
        httpd.shutdown()

    print(f"\n{'card':<38} {'bytes':>8}  size")
    bad = 0
    for slug, size, d in rows:
        ok = d == (1200, 630)
        bad += 0 if ok else 1
        print(f"{slug:<38} {size:>8}  {d}{'' if ok else '   <-- WRONG SIZE'}")
    shutil.rmtree(TMP, ignore_errors=True)
    print('\nVERDICT:', 'all cards 1200x630' if not bad else f'{bad} bad card(s)')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
