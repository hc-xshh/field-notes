# Field Notes

Source for **Field Notes** — an English-first blog on AI tooling evaluation: task books,
acceptance scripts, failure taxonomies, and pipeline notes.

Built with [Astro](https://astro.build), deployed as a static site on Cloudflare Pages.

## Local commands

```bash
npm install
npm run dev      # local preview at http://localhost:4321
npm run build    # static output in dist/
npm run preview  # serve the built output
python3 scripts/make_og.py   # regenerate public/og/*.png social cards
```

`scripts/make_og.py` renders one 1200×630 card per post (plus `default.png` for
non-post pages) with headless Chrome, using the same self-hosted fonts as the
site. Run it after adding a post and commit the PNGs — cards are pre-rendered
files rather than generated at request time, which keeps the site purely static
(no Functions, no build-time image service). Pages point at their card through
the `ogImage` prop on `Base.astro`.

## Writing a post

Add a markdown file to `src/content/posts/`. The filename becomes the URL slug.

```yaml
---
title: Post title
description: One sentence, used on the index and in meta tags.
date: 2026-10-07
lang: en          # en | zh
draft: false      # true keeps it out of the build
---
```

## Live pieces and one open placeholder

- **Newsletter signup** — MailerLite embedded form, double opt-in, wired into the
  home page and the foot of every post.
- **Payment button** — PayPal hosted button on `/support/` (plain HTML form, no
  third-party script). No real payment has been made through it yet.
- **Contact** — deliberately not published; `about.astro` carries the honest
  fallback ("reply on the platform where you read this") and a `TODO(contact)`
  marker for when an address exists.

## Redirects

`public/_redirects` is the rule that will move the temporary `*.pages.dev` host
to a real domain with a 301 (path-preserving via `:splat`). The mechanism is
verified on this project's pages.dev host; the rule itself is commented out
until a domain exists.

## Deploying

Already wired up: the Cloudflare Pages project `field-notes` is connected to this repo
(source: GitHub, production branch `main`), so **every push to `main` deploys automatically**.

- Build command `npm run build`, output directory `dist`, `NODE_VERSION=22`.
- Live at <https://field-notes-6cd.pages.dev> — the `-6cd` suffix is Cloudflare's: the plain
  `field-notes.pages.dev` name was already taken by another account.
- A custom domain can be attached later without touching the code; only `site:` in
  `astro.config.mjs` needs updating.
