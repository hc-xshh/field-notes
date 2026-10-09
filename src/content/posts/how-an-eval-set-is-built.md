---
title: How an eval set is built, and why it rots
description: An eval set is an instrument with a purpose, a scoring rule, a calibration record and an expiry date. Where the samples come from, what counts as correct, and what makes the set expire.
date: 2026-10-09
lang: en
topic: ai-and-engineering
---

An eval set is an instrument. It has a purpose, a scoring rule, a calibration record and an expiry date. Treating it as a file you download is where the trouble starts: the file already made those decisions without writing them down.

What follows is the build document I would want for a set I have to defend six months from now. Each rule is traceable to a public source or marked as my practice.

## Where the samples come from

Four sources, each importing a different bias.

| Source | What you get | The bias it imports | Documented where |
| --- | --- | --- | --- |
| A public benchmark, reused | Comparability with published numbers | Contamination; a task choice someone else made | [Sainz et al., 2023-10-27](https://arxiv.org/abs/2310.18018) |
| Public administrative data | A real distribution, a public licence, dated updates | A sample of who reports, not of who is affected | [CFPB, read 2026-10-09](https://cfpb.github.io/api/ccdb/index.html) |
| Synthetic generation | Volume you can afford, labels you control | Generator artifacts in the surface form | [Gururangan et al., ACL 2018](https://aclanthology.org/N18-2017.pdf) |
| Your own production traffic | Items that match what you ship | A convenience sample that drifts with the product | [Lipton et al., ICML 2018](https://arxiv.org/abs/1802.03916) |

**Reuse.** LiveBench's authors state the problem in one sentence: test set contamination "can quickly render benchmarks obsolete" ([LiveBench, v2 2025-04-18](https://arxiv.org/abs/2406.19314)). Their answer was questions from recent competitions, arXiv papers and news, added monthly. LiveCodeBench did the same for code: 400 problems published between May 2023 and February 2024 ([LiveCodeBench, arXiv v1 2024-03-12](https://arxiv.org/abs/2403.07974)). A static benchmark decays without anyone editing it.

**Administrative data.** The CFPB complaint database is the best example I know. Its search API reported 18,274,023 records under a CC0 licence on 2026-10-09, with a `last_updated` of 2026-10-08 ([CFPB complaint search API, read 2026-10-09](https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/?size=0&no_aggs=true)). Complaints are published only after the company responds or after 15 days, whichever comes first, and complaints referred to other regulators, including depository institutions with less than $10 billion in assets, are not published ([CFPB API docs, read 2026-10-09](https://cfpb.github.io/api/ccdb/index.html)). The agency states that the database "is not a statistical sample of consumers' experiences in the marketplace" ([CFPB database page, read 2026-10-09](https://www.consumerfinance.gov/data-research/consumer-complaints/)). A random draw samples the people who complained and whose complaints survived publication, not the people who were harmed.

**Synthetic.** Gururangan et al. showed that a text classifier reading only the hypothesis, with the premise deleted, reached about 67% on SNLI and 53% on MultiNLI ([Annotation Artifacts in NLI Data, ACL 2018](https://aclanthology.org/N18-2017.pdf)). The label was recoverable from phrasing because the crowd workers followed a template. Every generator has one. My test: delete the part of the input meant to carry the answer, score again, and compare with the majority-class rate. If accuracy stays well above it, the set is partly measuring its own generator. *(my practice)*

**Production sampling.** This is the source I trust least and use most. It produces items that match what the system sees, and its composition changes when the product does. Label shift is the named version of that failure: the marginal `p(y)` moves while `p(x|y)` does not, measurable without test labels using Black Box Shift Estimation ([Lipton et al., ICML 2018](https://arxiv.org/abs/1802.03916)).

## What counts as correct

The match rule is a parameter, and the same predictions score differently under each choice. Four conventions:

| Convention | The rule, as the source writes it | Source |
| --- | --- | --- |
| Exact match against any reference | Counts predictions that match any one ground truth answer exactly; punctuation and articles ignored | [SQuAD, arXiv v3 2016-10-11](https://arxiv.org/abs/1606.05250) |
| Partial credit against the best reference | F1 over bags of tokens, "the maximum F1 over all of the ground truth answers", then averaged | [SQuAD, arXiv v3 2016-10-11](https://arxiv.org/abs/1606.05250) |
| A threshold on localisation | IoU thresholds `[.5:.05:.95]`, 10 of them; 101 recall thresholds; `maxDets` of 1, 10 and 100 | [cocoapi `cocoeval.py`, read 2026-10-09](https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocotools/cocoeval.py) |
| A graded rubric with an exclusion flag | 0–3 for how well specified the issue is; 0–3 for whether the tests are scoped to it; a separate 0/1 question for any other reason the sample should not be used; a 1–5 confidence rating | [SWE-bench annotation instructions, undated](https://cdn.openai.com/introducing-swe-bench-verified/swe-b-annotation-instructions.pdf) |

Three things this table taught me.

**Say who the ceiling belongs to.** In SQuAD the human number comes from the data: the second annotator's answer is treated as the prediction, the rest as ground truth, and humans score 77.0 exact match and 86.8 F1 on the test set ([SQuAD, arXiv v3 2016-10-11](https://arxiv.org/abs/1606.05250)). A ceiling quoted without its rule says as much about the rule as about the task.

**One published number can hide ten thresholds.** COCO's headline detection score averages over ten IoU thresholds, three detection budgets and a recall grid. A single figure without a named threshold is a claim nobody can re-check. Pick the threshold, publish it, keep it fixed across versions.

**The exclusion question is the part people skip.** SWE-bench Verified is 500 samples "verified to be non-problematic by our human annotators", drawn from 1,699 randomly sampled items that 93 Python developers annotated, with the full annotation set and the rubric released alongside ([OpenAI, updated 2025-02-24](https://openai.com/index/introducing-swe-bench-verified/)). The rubric's last section asks, 0/1, whether there is any other reason not to use the sample. My handling of it, *(my practice)*:

- A closed list of exclusion reason codes, decided before annotation starts.
- Two raters must agree before an item is dropped; one rater's "unclear" is not an exemption.
- The dropped item stays in the file with its reason code, so the exemption stays auditable.
- The exemption rate is reported next to every result; if it moves between releases, the set changed even when the questions did not.

**Ground truth built by pooling is biased by construction.** Test collections are built by judging only a sample of documents. When the pool is small relative to the collection, the judgment set "can be biased in that they favor relevant documents that contain topic title words", a bias that depends on collection size and not on the number of relevant documents ([Buckley et al., NIST, 2007-07-17](https://www.nist.gov/publications/bias-and-limits-pooling-large-collections)). In a modern eval, if your labels come from checking only what your current systems returned, the label set favours items phrased the way those systems phrase things. My rule: draw a random slice from outside the candidate pool. *(my practice)*

## Whether the raters agree

Agreement is a property of the pair and the setup.

Krippendorff's alpha is `1 − Do/De`, and it accepts any number of coders and missing entries ([Krippendorff, 2011-01-25](https://www.asc.upenn.edu/sites/default/files/2021-03/Computing%20Krippendorff%27s%20Alpha-Reliability.pdf)). For two raters, Cohen's kappa, with Landis and Koch's 1977 bands ([reproduced in an AHRQ report, 2010](https://www.ncbi.nlm.nih.gov/books/NBK52665/table/ch3.t5)).

Here is why the setup has to travel with the number. First-turn results on MT-bench, in the paper's two setups: S1 counts ties and inconsistent votes, S2 excludes ties ([MT-Bench, v4 2023-12-24](https://arxiv.org/abs/2306.05685)):

| Pair (first turn) | S1, R = 33% | S2, R = 50% | Source |
| --- | --- | --- | --- |
| GPT-4 pairwise vs human expert | 66% (n = 1,343) | 85% (n = 859) | [MT-Bench, v4 2023-12-24](https://arxiv.org/abs/2306.05685) |
| GPT-4 single-answer vs human expert | 60% (n = 1,280) | 85% (n = 739) | [MT-Bench, v4 2023-12-24](https://arxiv.org/abs/2306.05685) |
| Human vs human | 63% (n = 721) | 81% (n = 479) | [MT-Bench, v4 2023-12-24](https://arxiv.org/abs/2306.05685) |

The headline everyone quotes is 85% against 81% for human agreement ([MT-Bench, v4 2023-12-24](https://arxiv.org/abs/2306.05685)). The same table holds 66% for the same judge under the other tie rule. An agreement figure quoted without its setup is not comparable to anything.

**Measure agreement per stratum, not pooled.** ChaosNLI collected 464,500 annotations, 100 per example, over 3,113 SNLI and MNLI examples and 1,532 ANLI examples ([Nie et al., 2020-10-08](https://arxiv.org/abs/2010.03532)). Models are near-perfect where humans agree and "can barely beat a random guess" where they do not, and those low-agreement items are most of the errors. A pooled score mixes two measurement regimes whose mixing ratio changes as models improve.

**Sizing.** For an agreement study, start from the kappa minimum-sample-size tables ([Bujang and Baharum, EBPH 14(2), 2017](https://riviste.unimi.it/index.php/ebph/article/view/17614)). For comparing two systems, use a power analysis: Miller gives the MDE formula and shows that raising answers per question from 1 to 10 moved the MDE from 13.2% to 7.5%; in his illustrative table, HumanEval's 164 questions at a fictional 83.6% carry a standard error of 3.2% ([Miller, 2024-11-01](https://arxiv.org/abs/2411.00640)). If items arrive in groups, such as the same document or template, compute clustered standard errors ([Miller, 2024-11-01](https://arxiv.org/abs/2411.00640), Table 4); on DROP they were 1.34 against 0.44 naive.

My rule: size the calibration slice for the agreement interval I need, the scoring slice for the effect I want to detect, and refuse to report a gap below the MDE. *(my practice)*

## Why the set rots

| Decay | Symptom | What I do |
| --- | --- | --- |
| Contamination | One set improves while unrelated sets do not | Keep item dates and prompt hashes; treat a stale set as historical |
| Label shift | Scores move while the system did not | Estimate the label mix and re-weight or re-cut the slice |
| Taxonomy and rubric drift | The same question means something different | Version the labels; freeze the rubric text per set version |
| Saturation | Every system sits near the ceiling | Retire the set and say when |

Contamination's extent "is unknown, as it is not straightforward to measure", and where it exists it overestimates performance ([Sainz et al., 2023-10-27](https://arxiv.org/abs/2310.18018)). I cannot audit training corpora, so I keep the dates and admit the exposure window.

Saturation is not a failure of the set: GLUE's performance passed the level of non-expert humans, which is what prompted SuperGLUE ([Wang et al., 2019-05-02](https://arxiv.org/abs/1905.00537)). Benchmark choice is fragile on its own: swapping tasks can reorder methods even when the methods do not change ([Dehghani et al., 2021-07-14](https://arxiv.org/abs/2107.07002)). Both are reasons to keep more than one set.

Taxonomy drift has a public paper trail. The CFPB's September 2026 release notes record that "consumers' complaint narratives ... have been removed from the database"; the June 2026 release removed "Consumer disputed" and "Consumer consent provided" from exports, long after those filters went away; the May 2023 release re-based the ZIP code field on 2019 census estimates ([CFPB release notes, read 2026-10-09](https://cfpb.github.io/api/ccdb/release-notes.html)). A set built on those narratives became unmaintainable one month ago. The same page explains the general rule: the database shows "the consumer's original products, sub-products, issues, and sub-issues selections consistent with the options available on the form at the time the consumer submitted the complaint" ([CFPB database page, read 2026-10-09](https://www.consumerfinance.gov/data-research/consumer-complaints/)). Labels frozen at submission, against a taxonomy that keeps moving.

## Keeping it maintainable

*(my practice, with borrowed pieces named)*

1. **Version the set.** Additions and exclusions get a version bump and a changelog line; never edit an item silently.
2. **Two slices.** A frozen slice for comparability, a rolling window for freshness. LiveCodeBench and LiveBench are public versions of the same idea.
3. **Write the metadata down.** A datasheet ([Gebru et al., 2018, CACM 2021](https://arxiv.org/abs/1803.09010)) or a Croissant record ([2024-03-28](https://arxiv.org/abs/2403.19546)), so the next person need not infer the collection process.
4. **A desensitisation rule that is checkable.** The CFPB's ZIP rule is a good template: publish the 5-digit ZIP unless the census area has under 20,000 people, then 3 digits only if the wider area has more than 20,000, otherwise nothing ([CFPB field reference, read 2026-10-09](https://cfpb.github.io/api/ccdb/fields.html)). A rule stated as a threshold can be re-run; "we removed personal information" cannot.
5. **Watch the exemption rate.** It is the leading indicator that the rubric stopped fitting the data.
6. **State the blind spot in one line.** SQuAD's metrics ignore punctuation and articles; COCO's headline averages ten thresholds. Both are fine as long as the limitation is on the label.
7. **Plan the retirement.** When a set saturates or its taxonomy moves, freeze it, date it, and build the next one from the same seed items.

## What I could not check

- **How many SWE-bench samples were dropped to leave 500.** The announcement gives the annotated total (1,699) and the rubric, not the drop count ([OpenAI, updated 2025-02-24](https://openai.com/index/introducing-swe-bench-verified/)).
- **Whether any specific model saw any specific benchmark item.** Sainz et al. state the extent is unknown; I have no method that resolves this, so I do not claim cleanliness.
- **The CFPB's narrative scrubbing standard.** The field is gone and the current field reference no longer documents it; I could not reach a dated scrubbing specification.
- **The CFPB's historical `consumer_consent_provided` semantics.** The export field and its filter are gone; I found the removal dates, not the values.
- **Krippendorff's own minimum sample size for alpha.** I have the kappa tables from Bujang and Baharum; I found no equivalent table for alpha.
- **The Landis and Koch bands at first hand.** I read a reproduction of the 1977 table in a 2010 AHRQ report, not the original.
- **LiveCodeBench's current item count.** The 400 figure comes from the March 2024 paper; the platform's live count may differ.
- **The OpenAI SWE-bench Verified page at first hand.** The live page served an automated-client challenge when I read it; the same version is readable in an [Internet Archive copy](https://web.archive.org/web/20260101233457/https://openai.com/index/introducing-swe-bench-verified/), and the annotation instruction PDF is undated.
- **The CFPB record count above is a live API value** and changes daily. It was 18,274,023 when I read it on 2026-10-09.