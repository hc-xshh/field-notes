---
title: Measuring error in support AI, and what accuracy hides
description: Five kinds of error, three ways one accuracy figure misleads, and what a routing test on 3,894 public complaints actually returned.
date: 2026-10-09
lang: en
topic: ai-and-engineering
tags: [ai-evaluation]
---

The way I test a support or ticketing system is against a task book, not a demo. The number people
ask for afterwards is accuracy, and I have stopped handing that over on its own: on every realistic
test set I have built, the average was the least informative thing in the results file.

What follows is the method I use now, plus a run on public data so the numbers can be checked.

## Five failure modes, five different bills

A support model fails in at least five ways, and they do not cost the same.

**Fabrication.** The reply asserts something absent from the policy or the record: a fee that does
not exist, a wrong refund window, an invented delivery date. This is what people call
hallucination. The taxonomy I lean on, OlaBench, splits it into four sub-types — factual
hallucination, misuse of retrieved results, relevance hallucination, and logical inconsistency
([OlaBench, arXiv:2510.22143v3](https://arxiv.org/abs/2510.22143v3), §3.1; v1 25 Oct 2025, v3 25
May 2026, retrieved 9 Oct 2026). A sentence that reads well and is false costs money, and the cost
usually arrives months later.

**Missed detection.** The ticket contains a legal threat, a regulator's name, a safety issue or a
fraud signal, and the system files it as routine. Nothing false was said. The failure is that no
human ever reads it. On a scoring sheet this often counts as a correct classification, because the
model did pick a queue that exists.

**Misrouting.** The reply is reasonable and the queue is wrong, so a differently-skilled team
applies its own policy. The measurable cost is time to resolution and repeat contact.

**Out-of-scope answers.** The system answers a question it was never built for — tax, legal
advice, another provider's product. The content may be accurate. The exposure is regulatory.

**Refusal.** The system declines, loops, or hands off. There is no answer, so there is no error to
score. This one gets tracked as a transfer or containment rate and drops out of the error count
entirely.

| Failure | What is wrong | Where the cost lands | Commonly reported as |
|---|---|---|---|
| Fabrication | the content | refunds, goodwill, disputes | hallucination rate |
| Missed detection | nothing | escalation, legal, safety | almost nothing |
| Misrouting | the destination | time to resolution, repeats | accuracy |
| Out of scope | the remit | compliance | rarely measured |
| Refusal | nothing | churn, containment | transfer rate |

One accuracy figure blends these five at whatever ratio the sample happens to contain, and that
ratio is set by whoever picked the sample.

## What I ran

I needed a routing task with a ground-truth label and text a model would really see. Public
complaint data has both.

The US CFPB publishes its Consumer Complaint Database under CC0 ([CFPB Consumer Complaint
Database](https://www.consumerfinance.gov/data-research/consumer-complaints/), retrieved 9 Oct
2026); the search API's own metadata reports 18,274,023 records, license CC0, last updated
2026-10-08 ([API metadata](https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/?size=0&no_aggs=true),
retrieved 9 Oct 2026).

The JSON search endpoint returns 15 fields and no narrative ([field
reference](https://cfpb.github.io/api/ccdb/fields.html), retrieved 9 Oct 2026). That is new: the
September 2026 release removed complaint narratives from the database ([CFPB release
notes](https://cfpb.github.io/api/ccdb/release-notes.html), Release 24, September 2026). So I took
the text from a Hugging Face mirror instead, `BEE-spoke-data/consumer-finance-complaints` ([dataset
card](https://huggingface.co/datasets/BEE-spoke-data/consumer-finance-complaints), CC0, mirror last
modified 29 Dec 2025); its `has-text` config holds 1,689,573 rows ([split
sizes](https://datasets-server.huggingface.co/size?dataset=BEE-spoke-data%2Fconsumer-finance-complaints),
retrieved 9 Oct 2026).

Task: read the narrative only, predict the product queue. Ground truth: the product label the CFPB
publishes. I drew 3,894 complaints from it. The oldest is dated 2015-03-20, the newest
2024-01-04.

## The label set changed under the data

The raw product field holds 17 distinct strings in this sample, and they are not 17 products. The
date ranges are what give it away.

| Product string as published | Rows | Received, first → last in this sample |
|---|---|---|
| Credit reporting, credit repair services, or other personal consumer reports | 1,892 | 2017-04-24 → 2023-08-24 |
| Debt collection | 547 | 2015-03-20 → 2023-12-18 |
| Credit card or prepaid card | 267 | 2017-04-24 → 2023-08-21 |
| Mortgage | 248 | 2015-04-21 → 2023-11-02 |
| Credit reporting or other personal consumer reports | 245 | 2023-08-26 → 2024-01-04 |
| Checking or savings account | 195 | 2017-04-24 → 2023-11-21 |
| Credit reporting | 92 | 2015-04-17 → 2017-04-09 |
| Student loan | 85 | 2015-10-06 → 2023-11-13 |
| Money transfer, virtual currency, or money service | 79 | 2017-08-08 → 2023-11-13 |
| Vehicle loan or lease | 75 | 2017-04-24 → 2023-11-01 |
| Credit card | 68 | 2015-04-06 → 2023-12-22 |
| Payday loan, title loan, or personal loan | 41 | 2017-04-24 → 2023-06-20 |
| Bank account or service | 34 | 2015-04-04 → 2017-01-31 |
| Consumer Loan | 19 | 2015-03-25 → 2017-02-03 |
| Payday loan | 3 | 2015-10-08 → 2017-02-24 |
| Money transfers | 2 | 2015-07-17 → 2015-12-05 |
| Payday loan, title loan, personal loan, or advance loan | 2 | 2023-09-20 → 2023-10-06 |

Read the dates down the table. `Bank account or service` last appears here on 2017-01-31, and
`Checking or savings account` first appears on 2017-04-24. Three more strings end in 2017 and their
successors start the same year. The three credit-reporting strings sit end to end: 2015 to 2017,
2017 to 2023, 2023 into 2024. Same category, renamed.

I collapsed the 17 strings into 9 categories before scoring anything. The mapping is in the script,
applied in one place rather than inferred per row. Without that step an accuracy compares a 2016
row and a 2023 row whose label sets do not line up, and the model gets credit or blame for the
taxonomy.

The live database disagrees with the mirror about which names are current. Aggregated over
complaints received in 2026, the CFPB API returns 11 product strings, with `Credit card` and
`Prepaid card` listed separately and no `Credit card or prepaid card` at all ([product aggregation,
complaints received 2026-01-01
onward](https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/?size=0&aggs=product&date_received_min=2026-01-01),
retrieved 9 Oct 2026). I did not reconcile the two taxonomies.

## Three ways one accuracy figure misleads

**Imbalance.** After collapsing, the sample looks like this:

| Collapsed category | Rows | Share |
|---|---|---|
| Credit reporting | 2,229 | 57.2% |
| Debt collection | 547 | 14.0% |
| Credit card or prepaid card | 335 | 8.6% |
| Mortgage | 248 | 6.4% |
| Checking or savings account | 229 | 5.9% |
| Student loan | 85 | 2.2% |
| Money transfer or virtual currency | 81 | 2.1% |
| Vehicle loan or lease | 75 | 1.9% |
| Personal / payday / title loan | 65 | 1.7% |

A predictor that answers "credit reporting" for every ticket scores 0.572 here. That is a
constant, and it sits close enough to a real model's score to be mistaken for one.

**Sample selection.** Same data, same model, two splits:

| Split | Test n | Accuracy | Macro F1 | Credit-reporting share of test set |
|---|---|---|---|---|
| Random 60/40 | 1,558 | 0.756 | 0.428 | 57.1% |
| Chronological, split at 2022-04-21 | 1,560 | 0.832 | 0.377 | 74.0% |

The chronological run scores 7.6 points higher while getting worse on most categories. The test
set became more concentrated in the biggest class, and the dominant-class predictor rides that
concentration up. Anyone reporting the 0.832 as an improvement after retraining would be reading
their own sampling as progress.

**Coverage.** Sort the test set by the model's confidence and score only the top slice:

| Coverage | Tickets scored | Accuracy on that slice |
|---|---|---|
| 100% | 1,558 | 0.756 |
| 75% | 1,168 | 0.854 |
| 50% | 779 | 0.904 |
| 25% | 389 | 0.900 |
| 10% | 155 | 0.897 |

The 0.904 at half coverage is a real number computed on held-out data, and published alone it
misdescribes the system by 15 points. Note where it stops moving: from 50% coverage down to 10%,
accuracy drifts from 0.904 to 0.897, so the model's confidence and its correctness come apart on
the tail. That tail is where the misroutes are.

Underneath the average, the per-category picture on the random split:

| Category | Test n | Recall | Precision |
|---|---|---|---|
| Credit reporting | 889 | 0.879 | 0.886 |
| Debt collection | 225 | 0.631 | 0.637 |
| Credit card or prepaid card | 129 | 0.760 | 0.430 |
| Mortgage | 114 | 0.860 | 0.737 |
| Checking or savings account | 93 | 0.548 | 0.607 |
| Money transfer or virtual currency | 32 | 0.000 | 0.000 |
| Student loan | 29 | 0.276 | 0.889 |
| Vehicle loan or lease | 29 | 0.000 | 0.000 |
| Personal / payday / title loan | 18 | 0.000 | 0.000 |

Three categories are never once predicted correctly. Accuracy is 0.756. Macro F1 is 0.428. The
distance between those two is the honest headline for this model.

## Pulling the high-risk errors out of the average

The useful published idea here is OlaBench's risk axis, Critical Business Risk Rate. It counts only
responses that inappropriately assert one of four things, each a high-stakes failure that may
trigger compliance exposure, user disputes or reputational damage: admitting platform liability
(618 test cases), misidentifying the ICS role (228), overcommitting (138), and disparaging
individuals or merchants (16) ([OlaBench,
arXiv:2510.22143v3](https://arxiv.org/abs/2510.22143v3), §3.1 and Table 1; 25 May 2026, retrieved 9
Oct 2026). It is reported as its own number, beside the hallucination rate.

The shape of that is what to copy: choose failures whose consequences differ in kind, count them
separately, publish both, and never average them.

For the routing test I defined three tiers, and I chose them:

- **critical** — a complaint about funds or account access (checking or savings, money transfer)
  lands in the reporting queue
- **material** — a credit or loan dispute lands in a different loan or reporting family
- **routine** — a misroute inside the same family

| Tier | Random split | Chronological split |
|---|---|---|
| Critical | 7 / 1,558 = 0.4% | 11 / 1,560 = 0.7% |
| Material | 43 / 1,558 = 2.8% | 28 / 1,560 = 1.8% |
| Routine | 330 / 1,558 = 21.2% | 223 / 1,560 = 14.3% |

The two splits swap places depending on which tier you read: the one with the prettier accuracy
hides a critical error rate almost twice as high.

Published work also shows how far the same named metric can move when the population changes. The
OlaBench paper reports a critical business risk rate of 8.7% for its OlaMind-Stage-2 model on the
benchmark, and a critical business risk rate below 0.05% in daily manual annotation of live
dialogues after launch ([OlaBench, arXiv:2510.22143v3](https://arxiv.org/abs/2510.22143v3), §5.2 and
Table 3; 25 May 2026, retrieved 9 Oct 2026). Both are the same metric, measured on different
populations with different annotators. Quoting one without the other is a choice.

## How these numbers were produced

- **Data.** 3,894 complaints from a CC0 mirror of the CFPB Consumer Complaint Database (config
  `has-text`, 1,689,573 rows). The draw is 40 pages of 100 consecutive rows at random offsets in
  the split, deduplicated by complaint ID, seed 20261009. Rows with a narrative under 80 characters
  were dropped. It is a clustered draw, not an independent one.
- **Label hygiene.** 17 published product strings collapsed to 9 categories using the date ranges
  in the table above. The mapping is written out in the script, not inferred per row.
- **Model.** Multinomial naive Bayes over word unigrams and bigrams, Laplace smoothing α = 1,
  features seen at least twice in training. Python standard library only.
- **Splits.** Random 60/40 with seed 7; chronological split at the 60th percentile of the
  received-date order, which lands on 2022-04-21.
- **Selective accuracy.** Test rows sorted by the model's maximum posterior probability, top k
  scored.
- Every number in the tables above is printed by that one script over that sample.
- **Deliberate choice.** No language model appears in this pipeline, including the scoring. A
  measurement instrument that is itself a model carries its own error, and OlaBench publishes the
  size of its own: its judge agrees with human annotators at 91.7% on risk identification and 82.6%
  on hallucination detection, over 5,000 human-annotated instances ([OlaBench,
  arXiv:2510.22143v3](https://arxiv.org/abs/2510.22143v3), §3.3 and Table 2; 25 May 2026, retrieved
  9 Oct 2026). A judge that disagrees with people 8% of the time on the risk axis puts a floor under
  everything else you can measure with it.

## What I could not check

- Whether the mirror's product strings match the live database's current taxonomy. The mirror's
  rows use names the live API no longer returns for complaints received in 2026. I collapsed by date
  range and did not reconcile the two.
- Whether the mirror is complete. Its files are timestamped December 2025 and the newest complaint
  in my 3,894-row sample is dated 2024-01-04. I did not verify whether later records exist in it.
- Whether complaints published with a narrative are representative of all complaints. Narratives
  appeared only with consent, so every number above sits on that consenting subset.
- Whether this sample's class mix reflects the population. Credit reporting is 57.2% of the sample
  and about 82% of the live database: 14,978,722 of 18,274,023 records carry one of the three
  credit-reporting strings ([product
  aggregation](https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/?size=0&aggs=product),
  retrieved 9 Oct 2026). Most of the gap is the mirror's date cap.
- How noisy the product label is. It is chosen by the consumer at submission, not assigned by an
  expert, and I treated it as ground truth because companies route on it. If it is noisy, my error
  rates are a floor, not a ceiling.
- Whether a published tiering exists for complaint-routing consequences. I could not find one, so
  the three tiers are mine. The OlaBench categories are a different kind of thing: they score what
  a reply asserts about liability and commitment, and they do not classify misroutes.
- Whether error rates vary with company size, state, or complaint age. A stratified rate is the
  next thing to compute.
- The naive Bayes model is a floor. A trained transformer would score higher on the same task. The
  run was to see the shape of the error distribution, and a better model changes the level without
  changing the shape.
