---
title: "From token prices to task prices: three jobs, seven APIs"
description: I priced three concrete jobs on seven model APIs using each vendor's own pricing page, and wrote down every assumption the conversion rests on.
date: 2026-10-09
lang: en
topic: ai-and-engineering
tags: [ai-evaluation, prices]
refresh: monthly
data_checked: 2026-10-09
---

Every vendor publishes a price per million tokens. Almost none publishes what a job costs; the number that decides whether a feature ships is left as arithmetic homework.

I did that arithmetic for three jobs, from first-party price lists read on 2026-10-09. The token counts are assumptions, not measurements, and they are written out below. The money is the vendor's standard-tier list price, in USD.

## The three jobs

**Job 1, label 1,000 support messages.** Each call sends a 400-token instruction block and a 120-token message, and asks for a 15-token answer. Billed per run: 520,000 input tokens, of which 400,000 are the instruction block sent 1,000 times, plus 15,000 output tokens.

**Job 2, turn a 100,000-word draft into a structured summary.** Google's token guide says a token is about 4 characters and 100 tokens about 60-80 English words, putting 100,000 words at 125,000-167,000 tokens ([Google token counting guide](https://ai.google.dev/gemini-api/docs/tokens), read 2026-10-09). I used 140,000:

- **One shot:** 140,000 tokens in, a 3,000-token structured summary out.
- **Map-reduce:** 14 chunk calls of about 10,000 tokens each, 700 tokens of notes per chunk, then a 9,800-token reduce call. Totals: 149,800 in, 12,800 out.

**Job 3, one round of tool-assisted bug fixing.** Eight turns against a 20,000-token repository: system prompt, tool schemas, three files. The prompt grows about 2,500 tokens per turn as tool results come back, from 20,000 to 37,500. Cumulative billed input is 230,000 tokens, of which 192,500 are a re-sent prefix a cache can serve; output is 6,000 tokens including reasoning.

## How I read the price lists

Five first-party pages, all read on 2026-10-09; the Gemini API page builds its tables client-side, so I read it in a browser.

- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing) — standard tier
- [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing) — paid tier, introductory rates through 2026-12-31
- [DeepSeek Models & Pricing](https://api-docs.deepseek.com/quick_start/pricing) — off-peak column
- [xAI pricing](https://docs.x.ai/developers/pricing)

The rules I applied:

- **Standard tier only**, unless a row says batch: the real-time tier.
- **Cache reads are billed at the published cached-input rate. Cache writes are billed where a vendor publishes a write price.** OpenAI and Anthropic do: $2.50 per million tokens for the two frontier models here, $0.125 for the two small ones, on Anthropic's 5-minute cache. Google, DeepSeek and xAI publish no write price, so I charged zero, which flatters those three in every cached row.
- **In the cached rows I charge a write for every input token that is not a cache read:** 400 tokens in Job 1, 37,500 in Job 3.
- **Reasoning tokens are output tokens.** OpenAI states they are billed as output tokens ([OpenAI reasoning guide](https://developers.openai.com/api/docs/guides/reasoning), read 2026-10-09). Gemini's output price is quoted "including thinking tokens" and DeepSeek's V4.1-Flash runs in thinking mode by default.
- **Tool and search fees sit outside the main table.**
- **No prompt hits a long-context threshold**; the prompt-length step that does apply, Anthropic's 100,000-token rule, is below.
- **No aggregator site was used** for any price.

## What each job costs

| Task | Model | Estimated cost | Assumptions | Price source (read 2026-10-09) |
| --- | --- | --- | --- | --- |
| Job 1, no cache | gpt-6.1-sol | $1.19 | standard tier; 520k in / 15k out | [OpenAI](https://developers.openai.com/api/docs/pricing) |
| Job 1, no cache | gpt-6-luna | $0.060 | standard tier; 520k in / 15k out | [OpenAI](https://developers.openai.com/api/docs/pricing) |
| Job 1, no cache | Claude Sonnet 5.5 | $1.19 | standard tier; 520k in / 15k out | [Anthropic](https://platform.claude.com/docs/en/about-claude/pricing) |
| Job 1, no cache | Claude Haiku 5.5 | $0.060 | standard tier; 520k in / 15k out | [Anthropic](https://platform.claude.com/docs/en/about-claude/pricing) |
| Job 1, no cache | Gemini 3.8 Flash | $0.45 | standard tier, introductory rate; 520k in / 15k out | [Google](https://ai.google.dev/gemini-api/docs/pricing) |
| Job 1, no cache | DeepSeek V4.1-Flash | $0.087 | off-peak window; 520k in / 15k out | [DeepSeek](https://api-docs.deepseek.com/quick_start/pricing) |
| Job 1, no cache | Grok 4.7 | $1.13 | standard tier; 520k in / 15k out | [xAI](https://docs.x.ai/developers/pricing) |
| Job 1, instructions cached | gpt-6.1-sol | $0.43 | 400k of input served from cache; one 400-token write | [OpenAI](https://developers.openai.com/api/docs/pricing) |
| Job 1, instructions cached | gpt-6-luna | $0.024 | 400k of input served from cache; one 400-token write | [OpenAI](https://developers.openai.com/api/docs/pricing) |
| Job 1, instructions cached | Claude Sonnet 5.5 | $0.43 | 400k cached, 5-minute TTL and write | [Anthropic](https://platform.claude.com/docs/en/about-claude/pricing) |
| Job 1, instructions cached | Claude Haiku 5.5 | $0.024 | 400k cached, prompts under 100k, 5-minute TTL | [Anthropic](https://platform.claude.com/docs/en/about-claude/pricing) |
| Job 1, instructions cached | Gemini 3.8 Flash | $0.18 | 400k of input served from cache, storage excluded | [Google](https://ai.google.dev/gemini-api/docs/pricing) |
| Job 1, instructions cached | DeepSeek V4.1-Flash | $0.028 | off-peak; cache hits free of a write fee | [DeepSeek](https://api-docs.deepseek.com/quick_start/pricing) |
| Job 1, instructions cached | Grok 4.7 | $0.53 | 400k of input served from cache | [xAI](https://docs.x.ai/developers/pricing) |
| Job 2, one shot | gpt-6.1-sol | $0.31 | 140k in / 3k out, one call | [OpenAI](https://developers.openai.com/api/docs/pricing) |
| Job 2, one shot | gpt-6-luna | $0.016 | 140k in / 3k out, one call | [OpenAI](https://developers.openai.com/api/docs/pricing) |
| Job 2, one shot | Claude Sonnet 5.5 | $0.31 | 140k in / 3k out, one call | [Anthropic](https://platform.claude.com/docs/en/about-claude/pricing) |
| Job 2, one shot | Claude Haiku 5.5 | $0.078 | 140k in / 3k out, above the 100k step | [Anthropic](https://platform.claude.com/docs/en/about-claude/pricing) |
| Job 2, one shot | Gemini 3.8 Flash | $0.12 | 140k in / 3k out, one call | [Google](https://ai.google.dev/gemini-api/docs/pricing) |
| Job 2, one shot | DeepSeek V4.1-Flash | $0.023 | off-peak; 140k in / 3k out | [DeepSeek](https://api-docs.deepseek.com/quick_start/pricing) |
| Job 2, one shot | Grok 4.7 | $0.30 | 140k in / 3k out, under the 200k threshold | [xAI](https://docs.x.ai/developers/pricing) |
| Job 2, map-reduce | gpt-6.1-sol | $0.43 | 14 chunk calls + 1 reduce call; 149.8k in / 12.8k out | [OpenAI](https://developers.openai.com/api/docs/pricing) |
| Job 2, map-reduce | gpt-6-luna | $0.021 | 14 chunk calls + 1 reduce call | [OpenAI](https://developers.openai.com/api/docs/pricing) |
| Job 2, map-reduce | Claude Sonnet 5.5 | $0.43 | 14 chunk calls + 1 reduce call | [Anthropic](https://platform.claude.com/docs/en/about-claude/pricing) |
| Job 2, map-reduce | Claude Haiku 5.5 | $0.11 | 15 calls, each prompt under 100k | [Anthropic](https://platform.claude.com/docs/en/about-claude/pricing) |
| Job 2, map-reduce | Gemini 3.8 Flash | $0.16 | 14 chunk calls + 1 reduce call | [Google](https://ai.google.dev/gemini-api/docs/pricing) |
| Job 2, map-reduce | DeepSeek V4.1-Flash | $0.030 | off-peak window, 15 calls | [DeepSeek](https://api-docs.deepseek.com/quick_start/pricing) |
| Job 2, map-reduce | Grok 4.7 | $0.38 | 14 chunk calls + 1 reduce call | [xAI](https://docs.x.ai/developers/pricing) |
| Job 3, agent loop | gpt-6.1-sol | $0.25 | 8 turns; 230k in (192.5k read, 37.5k written) / 6k out | [OpenAI](https://developers.openai.com/api/docs/pricing) |
| Job 3, agent loop | gpt-6-luna | $0.013 | 8 turns; 230k in (192.5k read, 37.5k written) / 6k out | [OpenAI](https://developers.openai.com/api/docs/pricing) |
| Job 3, agent loop | Claude Sonnet 5.5 | $0.25 | 8 turns; 192.5k reads and 37.5k 5-minute writes / 6k out | [Anthropic](https://platform.claude.com/docs/en/about-claude/pricing) |
| Job 3, agent loop | Claude Haiku 5.5 | $0.013 | 8 turns, every prompt under 100k | [Anthropic](https://platform.claude.com/docs/en/about-claude/pricing) |
| Job 3, agent loop | Gemini 3.8 Flash | $0.065 | 8 turns; 230k in (192.5k cached) / 6k out, storage excluded | [Google](https://ai.google.dev/gemini-api/docs/pricing) |
| Job 3, agent loop | DeepSeek V4.1-Flash | $0.0098 | off-peak window; 8 turns | [DeepSeek](https://api-docs.deepseek.com/quick_start/pricing) |
| Job 3, agent loop | Grok 4.7 | $0.21 | 8 turns; 230k in (192.5k cached) / 6k out | [xAI](https://docs.x.ai/developers/pricing) |

Two pairs of rows are identical on purpose. gpt-6.1-sol and Claude Sonnet 5.5 both list $2.00 per million input tokens, $10.00 output, $0.10 cached input and a $2.50 cache write ([OpenAI pricing](https://developers.openai.com/api/docs/pricing) and [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing), read 2026-10-09); gpt-6-luna and Claude Haiku 5.5 both list $0.10, $0.50, $0.01 and $0.125.

## The same jobs with each vendor's biggest discount

Batch is the biggest published discount: 50% on OpenAI ([pricing page](https://developers.openai.com/api/docs/pricing), read 2026-10-09), on Anthropic ("a 50% discount on both input and output tokens", [pricing page](https://platform.claude.com/docs/en/about-claude/pricing), read 2026-10-09) and on Google's paid tier ("Batch API (50% cost reduction)", [pricing page](https://ai.google.dev/gemini-api/docs/pricing), read 2026-10-09), where the Batch column halves the cached-input rate too. Not everywhere: xAI's batch section gives 20% to grok-4.3 and the grok-4.20 variants and says unlisted models have no batch discount, which leaves Grok 4.7 at full price ([xAI pricing](https://docs.x.ai/developers/pricing), read 2026-10-09). DeepSeek publishes no batch tier.

| Model | Job 1, cached | Job 2, one shot | Job 3, loop | Batch discount | Price source (read 2026-10-09) |
| --- | --- | --- | --- | --- | --- |
| gpt-6.1-sol | $0.22 | $0.16 | $0.12 | 50% | [OpenAI](https://developers.openai.com/api/docs/pricing) |
| gpt-6-luna | $0.012 | $0.0078 | $0.0067 | 50% | [OpenAI](https://developers.openai.com/api/docs/pricing) |
| Claude Sonnet 5.5 | $0.22 | $0.16 | $0.12 | 50% | [Anthropic](https://platform.claude.com/docs/en/about-claude/pricing) |
| Claude Haiku 5.5 | $0.012 | $0.039 | $0.0067 | 50% | [Anthropic](https://platform.claude.com/docs/en/about-claude/pricing) |
| Gemini 3.8 Flash | $0.088 | $0.058 | $0.033 | 50% | [Google](https://ai.google.dev/gemini-api/docs/pricing) |
| DeepSeek V4.1-Flash | $0.028 | $0.023 | $0.0098 | none published | [DeepSeek](https://api-docs.deepseek.com/quick_start/pricing) |
| Grok 4.7 | $0.53 | $0.30 | $0.21 | none | [xAI](https://docs.x.ai/developers/pricing) |

Claude Haiku 5.5's one-shot cell is the outlier: batch brings it to $0.039, still three times its cached Job 1 of $0.012, because a 140,000-token prompt sits above the 100,000-token step ([Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing), read 2026-10-09).

## What the numbers say

Every figure here is arithmetic on the rows above, whose rates are linked ([OpenAI](https://developers.openai.com/api/docs/pricing), [Anthropic](https://platform.claude.com/docs/en/about-claude/pricing), [Google](https://ai.google.dev/gemini-api/docs/pricing), [DeepSeek](https://api-docs.deepseek.com/quick_start/pricing), [xAI](https://docs.x.ai/developers/pricing), read 2026-10-09).

**Output tokens decide the bill at the frontier tier.** In cached Job 1 on gpt-6.1-sol, $0.15 of the $0.43 is output (35%) and $0.04 is cached instruction tokens (9%).

**The spread inside one vendor is bigger than the spread between vendors.** Cached Job 1 is $0.024 on gpt-6-luna and Haiku 5.5, $0.43 on gpt-6.1-sol and Sonnet 5.5, $0.53 on Grok 4.7: 22x from dearest to cheapest, 18x between the cheap pair and the frontier pair. At the same tier, the vendor changes nothing.

**The agent loop is the cheapest job here.** Job 3 is $0.25 on gpt-6.1-sol against $0.31 for the one-shot summary and $1.19 for Job 1. On the small models the order flips: Haiku 5.5 pays $0.078 for the one-shot summary against $0.013 for the loop, because 140,000 tokens crosses its threshold and 230,000 over eight turns does not.

**Map-reduce costs more than one shot.** On the two $2/$10 models it is $0.43 against $0.31, and the gap is all output tokens, 12,800 against 3,000. Chunking buys reliability and pays for it in output.

**The absolute numbers are small.** The main table spans $0.0098 to $1.19; batch pulls the floor to $0.0067. At this scale, a cost problem is usually a volume problem.

## The variables that break the conversion

**Thresholds re-price the whole request.** Claude Haiku 5.5 charges $0.10 and $0.50 per million input and output tokens up to 100,000 prompt tokens, and $0.50 and $2.50 above it; the length counts cache reads and writes, and each request is priced on its own ([Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing), read 2026-10-09). Job 2's 140,000-token prompt pays the higher rate on everything: $0.078, against $0.016 under the cap. xAI applies long-context rates to all tokens in a request once the prompt passes 200,000, where Grok 4.7 costs $4.00 input, $1.00 cached input and $12.00 output instead of $2.00, $0.50 and $6.00 ([xAI pricing](https://docs.x.ai/developers/pricing), read 2026-10-09). Gemini 3.1 Pro Preview steps from $2.00 to $4.00 input per million above 200,000 tokens ([Gemini Enterprise Agent Platform pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing), read 2026-10-09). OpenAI's line is 272,000 input tokens, published in a column tooltip; above it gpt-6.1-sol's input doubles to $4.00 and its output to $15.00 ([OpenAI pricing](https://developers.openai.com/api/docs/pricing), read 2026-10-09). All three jobs stay under every line; Job 2 is halfway to OpenAI's.

**Tokenizer differences.** Anthropic notes that Claude 4.7 and later use a tokenizer that "produces approximately 30% more tokens for the same text" ([Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing), read 2026-10-09). A comparison built on one words-per-token ratio, as mine is, is off by that much for Anthropic.

**Time of day.** DeepSeek's peak hours are 01:00-04:00 and 06:00-10:00 UTC, Monday to Friday, excluding Chinese public holidays; every other hour is off-peak at half price ([DeepSeek Models & Pricing](https://api-docs.deepseek.com/quick_start/pricing), read 2026-10-09). Job 1 uncached is $0.087 off-peak and $0.174 at peak. Off-peak is 133 of the week's 168 hours.

**Cache economics differ in shape as well as in rate.** Anthropic's cache hit is 10% of the input price on most models, 5% on Opus 5.5 and Sonnet 5.5, 2.5% on Fable 5.1 and Mythos 5.1; writes cost 1.25x for five minutes and 2x for an hour, so a 5-minute cache pays for itself after one read ([Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing), read 2026-10-09). DeepSeek's hit price is $0.003 per million against $0.15 for a miss ([DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing), read 2026-10-09). Google charges no write fee but charges storage, $0.50 per million tokens per hour on Gemini 3.8 Flash through 2026-12-31 and $4.50 on Gemini 3.1 Pro ([Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing) and [Gemini Enterprise Agent Platform pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing), read 2026-10-09); a cached 140,000-token document runs $0.07 an hour on Flash and $0.63 on Pro.

**Platform fees sit outside the token meter.** OpenAI bills $2.50 per 1,000 tool calls and $10 per 1,000 web searches, so Job 3's eight calls cost $0.02, and Anthropic's tool-use prompt adds 286 to 675 tokens ([OpenAI pricing](https://developers.openai.com/api/docs/pricing) and [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing), read 2026-10-09). xAI bills X search per item fetched: $5 per 1,000 posts, $10 per 1,000 profiles ([xAI pricing](https://docs.x.ai/developers/pricing), read 2026-10-09).

**Latency and geography carry multipliers.** OpenAI's Fast mode, renamed from Priority on 2026-07-30, is 2x, and data-residency endpoints add 10%; Gemini 3.8 Flash's Priority tier is $1.35 input against $0.75 standard ([OpenAI pricing](https://developers.openai.com/api/docs/pricing) and [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing), read 2026-10-09). xAI's priority tier is 2x and its US regional endpoint 1.1x; Anthropic charges 1.1x for US-only inference; regional Bedrock and Google Cloud endpoints carry a 10% premium ([xAI pricing](https://docs.x.ai/developers/pricing) and [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing), read 2026-10-09).

**The list price itself moves.** Google quotes its Flash prices "through December 31, 2026" and doubles them on 2027-01-01: $0.75 to $1.50 input, $3.75 to $7.50 output, $0.075 to $0.15 cached input, $0.50 to $1.00 per million tokens per hour of cache storage ([Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing), read 2026-10-09). Anthropic's $2/$10 for Claude Sonnet 5 was launched as introductory pricing through 2026-08-31 and is now standard, with the rise to $3/$15 cancelled ([Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing), read 2026-10-09). OpenAI's promotional pricing for GPT-5.6 Sol runs at least through 2026-11-21, on a model not in this table ([OpenAI pricing](https://developers.openai.com/api/docs/pricing), read 2026-10-09). Any per-task table is a snapshot with an expiry date.

## What I could not check

- **I ran none of these three jobs.** The token counts are stated assumptions, and a measured run would move every number here.
- **Cache-write pricing for Google, DeepSeek and xAI.** I found no published write price for any of the three, so I charged zero. xAI's prompt-caching page lists a billing rate per token type with no write line; Google's context-caching price is a read rate plus hourly storage; DeepSeek's table has only a hit price and a miss price. If any of them does charge for writes, its cached rows are too low.
- **Whether the Haiku 5.5 threshold behaves as written at the boundary.** The page counts cache reads and writes in a prompt's length, which would mean a cached 140,000-token document pays the higher rate. I did not test it.
- **Real token counts.** I used Google's words-per-token ratio across every vendor; Anthropic's own note about a 30% tokenizer difference is a warning that this is approximate.
- **Volume, committed-use and negotiated enterprise pricing, free tiers and trial credits** are outside this table. The price on the page is the list price.
- **Resale through cloud platforms.** Anthropic bills Bedrock and Google Cloud in consumption units, and Gemini Enterprise Agent Platform prices are not the Gemini API prices: on 2026-10-09 the two pages disagreed on cache storage, $0.50 per million tokens per hour ([Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing)) against $1.00 for one model ([Gemini Enterprise Agent Platform pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)). The route you buy through can change the number.
