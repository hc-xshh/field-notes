---
title: The Chinese open-weights release timeline, dated
description: Sixty-seven open-weight releases from Chinese labs, each with a date I could trace to a primary source — plus the eleven candidates I dropped, and why.
date: 2026-10-09
lang: en
topic: ai-and-engineering
tags: [open-data]
refresh: quarterly
data_checked: 2026-10-09
---

This is a list of dates, not an argument. Every row is a model whose weights were
published for anyone to download, with a date I could trace back to the organization that
published it, a parameter count as stated by that organization, and a link.

Most timelines of this kind are written from memory or from coverage, which is why they drift.
I built this one from vendor pages, papers and Hugging Face's API. This revision leaves the table
at 67 rows: seven are new, one of them because an entry I dropped in the first pass turns out to
be open-weights after all. The dropped list at the end has eleven entries, each with a reason.

## How to read this timeline

**Open weights only.** A release is in the table only if the organization published
downloadable weights. API-only and hosted-only models are out, including flagship ones:
Qwen3-Max, the served ERNIE models, Kimi's hosted variants, DeepSeek's API-only models.

**A date I could trace.** The Date column has two kinds of value. A plain date is the date on
the organization's own dated page — a research blog post, a news post, a release page, an
accepted paper. A date marked `†` is the Hugging Face repository creation timestamp in UTC,
read from the Hugging Face API on 2026-10-09, used when the vendor had no dated page I could
read. The two can differ by a few days, and that is usually preparation rather than a
different release: DeepSeek-V3's weights repository was created 2024-12-25 12:52 UTC and the
announcement is dated 2024-12-26.

**Parameter counts come from the vendor, or they are blank.** Total parameters with activated
parameters for mixture-of-experts models, as stated on the announcement, the model card, or
the repository holding the same weights. A family that ships many sizes gets a range. Where
none of the vendor's pages for that release states a count, the cell is `—` rather than a
number carried over from a sibling model, even when the lineage makes the number obvious.

**One link per row, to the vendor or the weight repository.** No aggregator links, no
news coverage. That makes most rows single-source by construction: each cites the vendor's own
statement about its own release, and every `†` row is single-source by definition.

**Scope.** Language models and the flagship multimodal lines that carry the same brand and
weights: Qwen3-VL, Qwen3-Omni, MiniMax-M3. Pure image, video and speech models are out of scope.

## When the vendor's page is client-rendered

Two of the labs whose releases I date most often publish announcements as a page that ships no
text to a plain HTTP request. z.ai's blog returns a 598-byte HTML shell that loads a JavaScript
bundle; qwen.ai's blog returns a shell that fetches its content after load. Both render fine in
a browser, which is what a reader clicking the link sees.

For z.ai I did read something: the date string sits inside the page's own bundle, so the bundle
is where I checked [GLM-4.5](https://z.ai/blog/glm-4.5) (2025-07-28),
[GLM-4.6](https://z.ai/blog/glm-4.6) (2025-09-30), [GLM-4.7](https://z.ai/blog/glm-4.7)
(2025-12-22) and [GLM-5](https://z.ai/blog/glm-5) (2026-02-12). That is weaker evidence than a
rendered page, and it is why [GLM-5.2](https://z.ai/blog/glm-5.2) stays out: its bundle contains
2026-06-16 and no other date, and a date visible only inside a build artifact is not one I will
print as sourced.

Qwen's older blog carries the full text and a date; the newer qwen.ai copies do not. So the
three Qwen3-* rows dated from qwen.ai in the first pass now cite the weight repository and
carry a `†`.

## 2023

### Q1–Q2

| Model | Date | Parameters | Source |
|---|---|---|---|
| ChatGLM-6B | 2023-03-13 `†` | 6.2B | [THUDM/chatglm-6b](https://huggingface.co/THUDM/chatglm-6b) |
| Baichuan-7B | 2023-06-13 `†` | 7B | [baichuan-inc/Baichuan-7B](https://huggingface.co/baichuan-inc/Baichuan-7B) |
| ChatGLM2-6B | 2023-06-24 `†` | `—` | [THUDM/chatglm2-6b](https://huggingface.co/THUDM/chatglm2-6b) |

### Q3–Q4

| Model | Date | Parameters | Source |
|---|---|---|---|
| Qwen-7B | 2023-08-03 `†` | 7B | [Qwen/Qwen-7B-Chat](https://huggingface.co/Qwen/Qwen-7B-Chat) |
| Baichuan 2 | 2023-09-19 | 7B, 13B | [arXiv:2309.10305](https://arxiv.org/abs/2309.10305) |
| ChatGLM3-6B | 2023-10-25 `†` | `—` | [THUDM/chatglm3-6b](https://huggingface.co/THUDM/chatglm3-6b) |
| Yi-34B | 2023-11-01 `†` | 34B | [01-ai/Yi-34B](https://huggingface.co/01-ai/Yi-34B) |
| DeepSeek Coder | 2023-11-01 `†` | 1.3B–33B | [deepseek-ai/deepseek-coder-33b-instruct](https://huggingface.co/deepseek-ai/deepseek-coder-33b-instruct) |
| DeepSeek LLM | 2023-11-29 `†` | 7B, 67B | [deepseek-ai/DeepSeek-LLM-67B-Chat](https://huggingface.co/deepseek-ai/DeepSeek-LLM-67B-Chat) |

Baichuan 2 is the only 2023 row dated by a paper: `arXiv:2309.10305` is dated 2023-09-19,
while its weight repositories appear earlier, on 2023-08-30 `†`, so the paper is the single
source for that date. The two ChatGLM cells are blank because their cards do not state a count:
6.2 billion is on the ChatGLM-6B card and not on the cards of its two successors, and copying
it across is the habit that makes timelines of this kind drift.

## 2024

### Q1

| Model | Date | Parameters | Source |
|---|---|---|---|
| Qwen1.5 | 2024-02-04 | 0.5B–110B | [Qwen blog](https://qwenlm.github.io/blog/qwen1.5/) |

Qwen1.5 was in the dropped list in the first pass, because I looked for it on the new blog and
found nothing readable. The old blog still carries the post, dated 2024-02-04, listing six
sizes plus 110B.

### Q2–Q3

| Model | Date | Parameters | Source |
|---|---|---|---|
| DeepSeek-V2 | 2024-05-07 | 236B total, 21B active | [arXiv:2405.04434](https://arxiv.org/abs/2405.04434) |
| GLM-4-9B | 2024-06-04 `†` | 9B | [zai-org/GLM-4-9B-Chat](https://huggingface.co/zai-org/GLM-4-9B-Chat) |
| Qwen2 | 2024-06-07 | 0.5B–72B | [Qwen blog](https://qwenlm.github.io/blog/qwen2/) |
| Qwen2-VL | 2024-08-29 | 2B, 7B, 72B | [Qwen blog](https://qwenlm.github.io/blog/qwen2-vl/) |
| DeepSeek-V2.5 | 2024-09-05 `†` | `—` | [deepseek-ai/DeepSeek-V2.5](https://huggingface.co/deepseek-ai/DeepSeek-V2.5) |
| Qwen2.5 | 2024-09-19 | 0.5B–72B | [Qwen blog](https://qwenlm.github.io/blog/qwen2.5/) |

### Q4

| Model | Date | Parameters | Source |
|---|---|---|---|
| Hunyuan-Large | 2024-10-22 `†` | 389B total, 52B active | [tencent/Hunyuan-Large](https://huggingface.co/tencent/Hunyuan-Large) |
| Qwen2.5-Coder | 2024-11-06 `†` | 0.5B–32B | [Qwen/Qwen2.5-Coder-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct) |
| DeepSeek-V2.5-1210 | 2024-12-10 | `—` | [DeepSeek changelog](https://api-docs.deepseek.com/news/news1210) |
| DeepSeek-V3 | 2024-12-26 | 671B total, 37B active | [DeepSeek news](https://www.deepseek.com/en/news/deepseek-v3/) |

The DeepSeek point releases inside a model line are dated on DeepSeek's own changelog, one page
per release. Hunyuan-Large's 389B/52B comes from
[arXiv:2411.02265](https://arxiv.org/abs/2411.02265), submitted 2024-11-04, three weeks after
the weights appeared.

## 2025

### Q1

| Model | Date | Parameters | Source |
|---|---|---|---|
| MiniMax-Text-01 | 2025-01-14 | 456B total, 45.9B active | [arXiv:2501.08313](https://arxiv.org/abs/2501.08313) |
| DeepSeek-R1 | 2025-01-20 | 671B total, 37B active | [DeepSeek news](https://www.deepseek.com/en/news/deepseek-r1/) |
| Qwen2.5-VL | 2025-01-27 `†` | 3B, 7B, 72B | [Qwen/Qwen2.5-VL-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-72B-Instruct) |
| QwQ-32B | 2025-03-06 | 32B | [Qwen blog](https://qwenlm.github.io/blog/qwq-32b/) |
| DeepSeek-V3-0324 | 2025-03-25 | 671B total, 37B active | [DeepSeek changelog](https://api-docs.deepseek.com/news/news250325) |

The two DeepSeek updates here do not restate a parameter count on their own changelog pages;
the cells carry the count from the repositories that hold those weights, which are the V3 and
R1 repositories listed above.

### Q2

| Model | Date | Parameters | Source |
|---|---|---|---|
| Qwen3 | 2025-04-29 | 0.6B–235B | [Qwen blog](https://qwenlm.github.io/blog/qwen3/) |
| DeepSeek-R1-0528 | 2025-05-28 | 671B total, 37B active | [DeepSeek changelog](https://api-docs.deepseek.com/news/news250528) |
| MiniCPM4-8B | 2025-06-05 `†` | 8B | [openbmb/MiniCPM4-8B](https://huggingface.co/openbmb/MiniCPM4-8B) |
| MiniMax-M1 | 2025-06-16 | 456B total, 45.9B active | [arXiv:2506.13585](https://arxiv.org/abs/2506.13585) |
| Hunyuan-A13B | 2025-06-27 | 80B total, 13B active | [Tencent-Hunyuan/Hunyuan-A13B](https://github.com/Tencent-Hunyuan/Hunyuan-A13B) |
| ERNIE 4.5 | 2025-06-30 | 0.3B–300B; flagship 300B/47B | [ERNIE blog](https://ernie.baidu.com/blog/posts/ernie4.5/) |

### Q3

| Model | Date | Parameters | Source |
|---|---|---|---|
| Kimi K2 | 2025-07-11 `†` | 1T total, 32B active | [moonshotai/Kimi-K2-Instruct](https://huggingface.co/moonshotai/Kimi-K2-Instruct) |
| Qwen3-Coder | 2025-07-22 | 480B total, 35B active | [Qwen blog](https://qwenlm.github.io/blog/qwen3-coder/) |
| GLM-4.5 | 2025-07-28 | 355B total, 32B active | [z.ai blog](https://z.ai/blog/glm-4.5) |
| Step-3 | 2025-07-31 | 321B total, 38B active | [StepFun research](https://chat.stepfun.com/research/zh/step3) |
| Seed-OSS-36B | 2025-08-21 | 36B | [ByteDance Seed blog](https://seed.bytedance.com/en/blog/seed-oss-open-source-models-release) |
| DeepSeek-V3.1 | 2025-08-21 `†` | `—` | [deepseek-ai/DeepSeek-V3.1](https://huggingface.co/deepseek-ai/DeepSeek-V3.1) |
| LongCat-Flash-Chat | 2025-08-29 `†` | 560B total, 18.6B–31.3B active | [meituan-longcat/LongCat-Flash-Chat](https://huggingface.co/meituan-longcat/LongCat-Flash-Chat) |
| Qwen3-Next-80B-A3B | 2025-09-09 `†` | 80B total, 3B active | [Qwen/Qwen3-Next-80B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct) |
| Ling-flash-2.0 | 2025-09-17 `†` | 100B total, 6.1B active | [inclusionAI/Ling-flash-2.0](https://huggingface.co/inclusionAI/Ling-flash-2.0) |
| Qwen3-Omni-30B-A3B | 2025-09-20 `†` | 30B total, 3B active | [Qwen/Qwen3-Omni-30B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct) |
| Qwen3-VL | 2025-09-22 `†` | 235B total, 22B active | [Qwen/Qwen3-VL-235B-A22B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-235B-A22B-Instruct) |
| DeepSeek-V3.2-Exp | 2025-09-29 | `—` | [DeepSeek news](https://www.deepseek.com/en/news/v3-2-exp/) |
| GLM-4.6 | 2025-09-30 | `—` | [z.ai blog](https://z.ai/blog/glm-4.6) |

### Q4

| Model | Date | Parameters | Source |
|---|---|---|---|
| Ling-1T | 2025-10-02 `†` | 1T total, 50B active | [inclusionAI/Ling-1T](https://huggingface.co/inclusionAI/Ling-1T) |
| DeepSeek-OCR | 2025-10-17 `†` | `—` | [deepseek-ai/DeepSeek-OCR](https://huggingface.co/deepseek-ai/DeepSeek-OCR) |
| LongCat-Flash-Omni | 2025-10-23 `†` | 560B total, 27B active | [meituan-longcat/LongCat-Flash-Omni](https://huggingface.co/meituan-longcat/LongCat-Flash-Omni) |
| MiniMax-M2 | 2025-10-27 | 230B total, 10B active | [MiniMax blog](https://www.minimax.io/blog/minimax-m2-en-1748600000) |
| Kimi K2 Thinking | 2025-11-04 `†` | `—` | [moonshotai/Kimi-K2-Thinking](https://huggingface.co/moonshotai/Kimi-K2-Thinking) |
| DeepSeek-V3.2 | 2025-12-01 | `—` | [DeepSeek news](https://www.deepseek.com/en/news/deepseek-v3-2/) |
| GLM-4.7 | 2025-12-22 | `—` | [z.ai blog](https://z.ai/blog/glm-4.7) |

## 2026

### Q1

| Model | Date | Parameters | Source |
|---|---|---|---|
| GLM-4.7-Flash | 2026-01-19 `†` | 30B total, 3B active | [zai-org/GLM-4.7-Flash](https://huggingface.co/zai-org/GLM-4.7-Flash) |
| Step-3.5-Flash | 2026-02-01 `†` | 196B total, 11B active | [stepfun-ai/Step-3.5-Flash](https://huggingface.co/stepfun-ai/Step-3.5-Flash) |
| MiniMax-M2.5 | 2026-02-12 | `—` | [MiniMax news](https://www.minimax.io/news/minimax-m25) |
| GLM-5 | 2026-02-12 | 744B total, 40B active | [z.ai blog](https://z.ai/blog/glm-5) |
| Qwen3.5-397B-A17B | 2026-02-16 | 397B total, 17B active | [Alibaba press release](https://home.alibabagroup.com/en-US/document-1960233590314762240) |

### Q2

| Model | Date | Parameters | Source |
|---|---|---|---|
| MiniMax-M2.7 | 2026-04-09 `†` | `—` | [MiniMaxAI/MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7) |
| Kimi K2.6 | 2026-04-14 `†` | 1T total, 32B active | [moonshotai/Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6) |
| DeepSeek-V4 (Pro and Flash) | 2026-04-24 | Pro 1.6T total / 49B active; Flash 284B total / 13B active | [DeepSeek news](https://www.deepseek.com/en/news/v4-preview) |
| Step 3.7 Flash | 2026-05-23 `†` | 198B total, 11B active | [stepfun-ai/Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash) |
| MiniMax-M3 | 2026-06-01 | ~428B total, ~23B active | [MiniMax blog](https://www.minimax.io/blog/minimax-m3) |

The DeepSeek-V4 row now carries both counts; the Flash model's 284B total is stated on the same
announcement page as the Pro figures. Step 3.7 Flash moved to a `†` date: its GitHub repository
has no releases, and the page I first cited carries a creation timestamp rather than a release
date.

### Q3

| Model | Date | Parameters | Source |
|---|---|---|---|
| LongCat-2.0 | 2026-07-05 `†` | 1.6T total, ~48B active | [meituan-longcat/LongCat-2.0](https://huggingface.co/meituan-longcat/LongCat-2.0) |
| Hunyuan Hy3 | 2026-07-06 | 295B total, 21B active | [Tencent newsroom](https://www.tencent.com/tencent-hunyuan-officially-releases-hy3-advancing-agent-capabilities-and-deeper-product-integration/) |
| Qwen3.8 | 2026-08-05 `†` | 27B; 2.4T total / 95B active | [Qwen/Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) |
| DeepSeek-V4-Pro GA | 2026-08-13 | 1.6T total, 49B active | [DeepSeek changelog](https://api-docs.deepseek.com/news/news260813) |
| DeepSeek-V4-Flash-Vision-Exp | 2026-08-21 | `—` | [DeepSeek changelog](https://api-docs.deepseek.com/news/news260821) |
| DeepSeek-V4.1-Flash | 2026-09-10 | 552B total; 8B active for input, 16B for output | [DeepSeek changelog](https://api-docs.deepseek.com/news/news260910) |

Hy3 is the entry whose status changed in this revision. In the first pass I dropped it because
the page I found did not say whether weights were published. It does: Hy3 is open-sourced under
Apache 2.0 with weights on Hugging Face, and Tencent's newsroom names the parameter counts. The
V4-Pro GA row repeats the count from the April preview announcement, because the GA page does
not restate it. The Qwen3.8 row is dated by the repository of the 27B model, the first of the
line to appear; the flagship 2.4T-A95B repository was created three days later, and Qwen's own
announcement page is one of the client-rendered ones described above.

Two rows elsewhere disagree with third-party timelines for the same reason: LongCat-2.0's
repository was created 2026-07-05 while secondary coverage puts its launch at the end of June,
and DeepSeek-V4-Flash's repository was created 2026-04-22, two days before the announcement
page.

## What changed in this revision

Seven rows were added and three cells changed, listed because the edit history is the point of
a table like this:

1. **Qwen1.5 promoted into 2024 Q1** (2024-02-04), after finding the dated post on the old
   Qwen blog.
2. **Hunyuan Hy3 promoted into 2026 Q3** (2026-07-06). It was dropped in error.
3. **Four DeepSeek point releases added**: V2.5-1210 (2024-12-10), V3-0324 (2025-03-25),
   R1-0528 (2025-05-28) and V4-Pro GA (2026-08-13). All four are dated on DeepSeek's own
   changelog, the same source as V3.2 and V3.2-Exp.
4. **Qwen3.8 added** (2026-08-05 `†`), which the first pass omitted entirely.
5. **Two ChatGLM parameter cells blanked.** The ChatGLM2-6B and ChatGLM3-6B cards do not state
   a count, so the cells are now `—`.
6. **DeepSeek-V4-Flash gained its total.** The row said "Flash 13B active" and dropped the
   284B total, which the same page states.

Three rows changed source or date type for the same structural reason: the Qwen3-Next,
Qwen3-Omni and Step 3.7 Flash rows now cite a weight repository with a `†`, because the pages
cited in the first pass were either unreadable to a plain request or carried no release date.

## How this table gets updated

The table is edited in place. Every quarter I re-read the vendor pages for the labs already
listed, then check Hugging Face for new repositories under those organizations. A release
enters the table when it has a date and a link; until then it sits in the dropped list, with
the reason.

Two rules keep it stable: I do not replace a `†` date with a later one unless the vendor
publishes its own dated page, and I do not remove a superseded row.

The current table has 67 entries. Twenty-three of them fall in the twelve months from October
2025 to October 2026. That is a count of this table and nothing more; it is not a claim about
the field, because the table only holds releases I could date.

## What I could not check

**Eleven candidates were dropped**, for these reasons:

1. **Yi-1.5** (May 2024) — the weight repository
   ([01-ai/Yi-1.5-34B](https://huggingface.co/01-ai/Yi-1.5-34B)) was created 2024-05-11 `†`, and
   I could not date the announcement itself.
2. **InternLM2 and InternLM2.5** — the weight repositories
   ([internlm/internlm2-7b](https://huggingface.co/internlm/internlm2-7b),
   [internlm/internlm2_5-7b-chat](https://huggingface.co/internlm/internlm2_5-7b-chat)) look
   like renamed predecessors, so the creation timestamp does not mark the release.
3. **MiniCPM 1 and 2** — same problem; the repository
   ([openbmb/MiniCPM-2B-sft-bf16](https://huggingface.co/openbmb/MiniCPM-2B-sft-bf16)) is now a
   monorepo for a whole series.
4. **Baichuan 3 and 4** — I could not find weight artifacts at all.
5. **ERNIE 5.0** and **ERNIE 5.1** — Baidu's blog dates them 2026-02-06 and 2026-05-09
   ([ERNIE 5.0](https://ernie.baidu.com/blog/posts/ernie5.0/),
   [ERNIE 5.1](https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/)) and describes
   ERNIE 5.0 as a 2.4-trillion-parameter model, but I found no open-weight repository for
   either.
6. **Kimi K3** — the model card ([moonshotai/Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3))
   carries the full architecture table (2.8T total, 104B activated) and a license, but no
   release date. The repository timestamp is 2026-06-13 and secondary coverage says mid-July. I
   could not reconcile that.
7. **Kimi K2.5** — same shape of problem: the weight repository timestamp
   ([moonshotai/Kimi-K2.5](https://huggingface.co/moonshotai/Kimi-K2.5)) is 2026-01-01 while the
   launch is reported at the end of January.
8. **GLM-5.2** — the post is client-rendered and the only date string in its bundle is
   2026-06-16. I am not willing to print that as the release date.
9. **DeepSeek-V3.1-Terminus** — a mid-cycle rename with a 2025-09-22 `†` repository
   ([deepseek-ai/DeepSeek-V3.1-Terminus](https://huggingface.co/deepseek-ai/DeepSeek-V3.1-Terminus));
   including it would have double-counted the V3.1 line.
10. **Qwen-Image-2.1** — a dated weight repository
    ([Qwen/Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1), 2026-09-14 `†`) but an
    image model, outside this table's scope by the rule stated at the top.
11. **The Step-Audio line** — the same, for speech. The repositories exist
    ([stepfun-ai/Step-Audio-R1.1](https://huggingface.co/stepfun-ai/Step-Audio-R1.1)) and I did
    not date them, because they would need their own table with its own scope.

Three other limits on this table:

- **The `†` timestamps are preparation times, not launch times.** A repository can be created
  days before the announcement, and from outside I cannot see whether weights were uploaded
  at once or in pieces. Where the gap is large I noted it above the table.
- **The dates are the vendor's own.** No release date here has been confirmed by a second
  source, and one link per release is deliberate: a vendor correcting itself is the signal
  worth keeping, and coverage repeating the vendor is not a second source.
- **License differences are not reflected.** Apache-2.0, MIT and the vendor-specific
  licenses Kimi, MiniMax and LongCat ship under are not the same permission. Each row links to
  the page that states its license, and for Hy3 that page states Apache 2.0.
