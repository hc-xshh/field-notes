---
title: Twenty hot lists, no API keys
description: An aggregator that collects 20 trending lists every night. Six sources broke in ways worth keeping a record of, and one of them is gone for good.
date: 2026-10-08
lang: en
topic: ai-and-engineering
tags: [open-data]
---

Every night at 04:30 a script on this machine collects the current front page of 20 platforms
(Zhihu, Bilibili, V2EX, Hupu, Maoyan, Hacker News, Lobsters, GitHub, Reddit, YouTube, arXiv and a
few tech news feeds), translates the English headlines into Chinese, builds a static site and
pushes it. There is no server and no database. The output is a set of JSON files and a
single-page app that reads them.

I have no API keys for most of these platforms, and for the ones that do offer keys, I did not
want to create accounts for a hobby project. That constraint produced the most useful part of the
system: a catalogue of what each source actually gives you, and a record of how each one broke.
This is that record. It is more useful than the feature list.

## The sources that broke, and what the failure was really about

**Reddit, first attempt.** There was a trick where you request
`translate.google.com/translate?u=<reddit url>` and read the translated page, which passes through
Reddit's HTML. It worked for months and then started returning a 302 to `translate.goog`, which
serves a shell with no posts in it. The failure looked like a parser bug. It was a removed feature.

**Reddit, second attempt.** The official Atom feed, `r/popular/hot/.rss`, works and needs no key.
Two traps: `geo_filter=GLOBAL` has to be present, or the feed comes back localised to the country
your request exits from, and mine exits from a node that made the whole page German. And the feed
carries no score and no comment count, so those fields are simply absent from my data rather than
zero.

**Reddit, third attempt, which is where it ends.** Scores are available through the JSON API if
you have OAuth credentials. I opened the app-creation form, submitted it, and got
`{"success": true}` back, while the applications list stayed empty. Their documentation has since
moved new legacy-Data-API apps to an application process for moderation use cases. Unauthenticated
`.json` returns 403 from anything that looks like a datacenter address: direct, through a proxy,
and with a browser TLS fingerprint that makes the request look like Chrome. Two public mirrors
were dead ends as well, one of which now wants to be paid and explicitly refuses automated
clients, and the other of which returns `/r/popular` posts from 2015.

There is a path that works: send the request with a logged-in browser's cookies. I measured it,
got a real score back, and decided not to use it. The data is not worth building the pipeline on
something the platform's terms do not allow.

**arXiv.** The API started answering with a 14-byte body, `429 "Rate exceeded."`, for every query,
from every route. Not occasional throttling: the endpoint was closed to my traffic entirely.
The official RSS feeds for cs.AI, cs.LG and cs.CL serve the same listing without a key. The
endpoint is still in the code as a fallback, and I expect to delete it.

**36Kr.** The page is entirely client-rendered, so the extractor's basic mode returns
`{"results": [], "failed_results": [{"error": "Error fetching content"}]}`. The old code read
`results[0]` and raised an `IndexError`, which the pipeline caught as a platform failure and
handled by keeping yesterday's data. So for weeks the site showed a platform labelled "AI news"
that was quietly a day or two out of date. The fix was one parameter, `extract_depth: advanced`.
The bug was the exception handling that turned a hard failure into a silent stale one.

## The night the whole thing hung

One night no platform updated. The cron entry reported a timeout after 3600 seconds and the
captured output was empty.

Nothing was wrong with the network: I could see every platform's connection being made in the
proxy log at 04:30, and then no connections at all for the next 55 minutes. Nothing had reached
the build step either, which I could tell from one log file's modification time. The script was
alive and doing nothing, and I had no idea where.

Two things had made that state undiagnosable. Python buffers stdout when it is not attached to a
terminal, so when the process was killed, every line it had printed died with it. And
`urlopen(timeout=N)` applies to each socket read rather than the whole request, so a slow response
can stall for far longer than the timeout suggests.

The fix is unglamorous: `exec </dev/null` so no child can block on stdin, `python3 -u` so output
survives a kill, a `timeout` around every step, a translation budget, and a step log that records
a timestamp as each stage starts. The next failure will be somewhere specific in that log.

## A successful job is not fresh data

This is the lesson I would keep if I could keep only one. "The task exited 0" and "the data is
from today" are different claims, and a pipeline that only reports the first one will lie to you
quietly for weeks. So there is a separate check: it reads every platform's JSON, compares its date
with today, and exits non-zero if any source is stale or empty. It does not care that the fetch
succeeded.

The same principle shows up in the summary step. A model writes the "today's focus" card, reading
the top five items from each platform, and it is asked to return only item identifiers and a
reason. The script then looks up each identifier and fills in the title and URL from the data it
already has. The model never writes a link, so it cannot invent one. If the summary fails, the old
one stays on the page marked stale.

## Where the ordering is not what it looks like

Three caveats, since the site presents these lists as rankings:

- Hupu's "hot" list is a weighted stream rather than a sorted list of numbers. There is no score
  to sort by.
- 36Kr and TechCrunch are editorially ordered. The order is theirs, not a measurement.
- V2EX's public hot endpoint returns about nine items on a good day.

The site says which list is which on each platform page. A ranking whose method is unstated is
just a list.

## Reproducing this

The collector is Python, one function per platform, and the run prints a report. The interesting
part to copy is not the fetching. It is the two checks around it: a freshness check that fails
when data is old even though the job succeeded, and a generation step where the model returns only
identifiers that the script resolves into real URLs.
