---
title: What this site actually ships, and the widget I can't remove
description: 2,130 bytes of HTML, 1 KB of my own JavaScript, no framework. Then the newsletter form loads jQuery, and the number stops being funny.
date: 2026-10-08
lang: en
---

The front page of this site is a 2,130-byte HTML document containing 91 elements. I wrote 1,022
bytes of JavaScript for it, in two inline blocks, and I have no build step that could hide
anything else. That is the whole page: text, a stylesheet, two typefaces.

Then you scroll to the signup form, and jQuery 3.7.1 arrives.

## How I measured it

Not from the build output. Build output tells you what you shipped, not what a browser fetched.
I opened the live site in headless Chrome, attached to it over the DevTools protocol, and read
`performance.getEntriesByType('resource')` plus the navigation timing entry.

The page, from my line:

- document: 2,130 bytes encoded, 91 elements in the DOM
- same-origin requests: 4. Stylesheet 3,498 B, Inter 48,556 B, Newsreader 132,300 B, favicon 469 B
- JavaScript I wrote: 1,022 B, in two inline `<script>` blocks (255 B to set the theme before
  first paint, 767 B for the toggle)
- there is also a 309-byte inline `<script type="application/ld+json">`, which is data for
  search engines rather than code

And the signup widget, which is a third-party embed:

- 9 requests to MailerLite's CDN
- 225,273 bytes downloaded, of which 223,312 bytes is JavaScript: jQuery 87,532 B, the widget's
  own loader 52,683 B, an input-mask bundle 70,970 B, a form renderer 12,127 B
- the remaining ~2 KB is two small stylesheets

So the form costs about 100 times my own HTML in JavaScript, on every page that shows it.

Two honest caveats on those numbers. Cross-origin responses report `transferSize: 0` unless the
server sends `Timing-Allow-Origin`, so the widget's bytes came from `curl` against the six asset
URLs, not from the browser's own accounting. And the timings came from my machine, over a tunnel:
document response started at 1,593 ms, DOM ready at 2,151 ms, and the `load` event at 9,526 ms.
That last number is the widget too. None of these three timings are what you would see.

## Why the typefaces are mine to serve

The two font files are the heaviest thing I send you, and they are the part I am most confident
about. They are subsets: Inter at 48 KB, Newsreader at 132 KB, latin ranges only, no third-party
request, no DNS lookup to someone else's CDN, and a 6-month `Cache-Control` from my own host.

I could have linked to a font CDN instead. I decided not to, for a reason I can state precisely:
I cannot verify that CDN from where my readers are. I also cannot verify it from where I am. When
I benchmarked a list of hosts from this machine, Google Fonts answered in about a second, which
looks like proof that nothing is blocked, except that my machine routes everything through a
tunnel: a request to a foreign host leaves from a Tokyo exit node, and only requests to Chinese
hosts leave from my actual ISP address. Two different addresses are answering me depending on
which host I ask, and both of them are reported as "direct".

That is the useful lesson here, and it cost me a wrong sentence earlier in this project. A test
that does not tell you which way the packets left is not a reachability test. So the font files
ship with the site, where the only network path involved is the one that already delivered the
page.

## The failure worth writing down

I styled the widget to match the site and pushed it. The button stayed black. In dark mode the
email field stayed white.

MailerLite's stylesheet writes its rules with the form's container id and `!important`:
`#mlb2-46888919.ml-form-embedContainer ... .ml-form-embedSubmit button { background-color: #000
!important }`. My override was `.newsletter .ml-form-embedSubmit button`, which has two classes.
An id plus four classes beats two classes no matter how many `!important` flags I add, because
`!important` only settles ties inside the same specificity tier.

The fix is boring: repeat the same id in my selector and add one more class, so my rule wins on
specificity and then on `!important`. The interesting part is that the screenshot looked fine. A
black button on a light page looks like a design choice. I only caught it because I stopped
looking at pixels and asked the browser for computed values:

```js
getComputedStyle(document.querySelector('.ml-embedded button[type=submit]')).backgroundColor
// "rgb(0, 0, 0)"  -> my stylesheet was not applying at all
```

Both rounds after that, light and dark, I asserted on computed colours, and kept the screenshots
for layout only. Pixels are for judging whether something looks right. They are a bad instrument
for finding out whether your CSS is in the cascade.

## What I would do about the 220 KB

Defer it. The widget only has to exist when a reader scrolls to it or clicks it, and the page can
load the embed then instead of in the `<head>`. That is the next change I want to make here, and
when it is done I will re-run the same measurement and put both numbers in this post, including
the case where it does not help.

Until then the honest statement is: this site has no framework, no bundler, no client-side router,
no analytics, and about a kilobyte of JavaScript that I wrote. The one third-party script on it is
a newsletter form, and it is heavier than everything else on the page put together.

## Reproducing this

The measurement is a CDP script: open the page in headless Chrome, enable the Network domain, read
`performance.getEntriesByType('resource')`, then `curl -o /dev/null -w '%{size_download}'` the
asset URLs to get the cross-origin bytes the Resource Timing API refuses to report. If you want
to compare your own site, the part that matters is the last step. Browser-side byte counts for
third-party assets are usually 0, and it is easy to read that as "the widget is free".
