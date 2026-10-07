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
```

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

## Open placeholders

Two things on the site are honest placeholders, marked with `TODO` in the source:

- **Newsletter signup** (`src/pages/index.astro`) — form lands once the mailing list account exists.
- **Payment button** (`src/pages/support.astro`) — PayPal individual-seller account is under review.

## Deploying

Already wired up: the Cloudflare Pages project `field-notes` is connected to this repo
(source: GitHub, production branch `main`), so **every push to `main` deploys automatically**.

- Build command `npm run build`, output directory `dist`, `NODE_VERSION=22`.
- Live at <https://field-notes-6cd.pages.dev> — the `-6cd` suffix is Cloudflare's: the plain
  `field-notes.pages.dev` name was already taken by another account.
- A custom domain can be attached later without touching the code; only `site:` in
  `astro.config.mjs` needs updating.
