---
title: How the money actually moves in live commerce
description: The split chain behind a livestream sale — platform fee, promotion fee, slot fee, agency cut — and when the money actually lands. Every figure carries a source and a date.
date: 2026-10-09
lang: en
topic: supply-chain
tags: [trade-and-logistics, rails-and-infrastructure]
---

Plenty of English writing explains what a livestream checkout looks like. Almost none explains the middle: who takes what out of a completed order, out of which number, and how long the seller waits before the money is theirs.

I read platform rulebooks rather than marketing decks. They are dull, and they are the only place the arithmetic is written down.

## What counts as a source here

Ranked: (1) rules published by the platform, with a date, because those move money; (2) help centres and developer docs restating them; (3) reported figures — press interviews, industry reports — fine for ranges, weak on precision; (4) "industry-common figure, unverified."

Every number below carries a link and the date of the page I read it on. Where a page renders in a browser but not in a reader, I say so.

One structural problem runs through the chain. On the Chinese platforms the headline rate is often not in the rule text: the rule gives the formula, and the category rate sits in a separate annex or an in-product lookup.

## The chain, in one pass

- the buyer pays the platform;
- the platform takes an order-level technical service fee;
- the merchant pays a promotion fee (commission) to whoever drove the sale;
- the platform takes a cut **of that promotion fee** too — a second fee, on the creator side;
- the remainder goes to the agency, which splits it with the host by private contract;
- separately, the merchant may have paid a slot fee up front, kept regardless of sales.

Two fees, two bases. Collapsing them is where most confusion starts.

## Layer one: the platform's cut

| Platform | Charge | Rate | Base |
|---|---|---|---|
| Taobao | Seller base software service fee | **0.6%**, capped at ¥60 per sub-order ([help centre](https://helpcenter.taobao.com/servicehall/content_layout?pointId=399385564309116268), 2 June 2026) | Confirmed-receipt amount incl. shipping and platform subsidies |
| Taobao Live | Live software service fee | **Receipts × category rate**; rate in a separate annex ([rule](https://terms.alicdn.com/legal-agreement/terms/b_platform_service_agreement/20240311160205306/20240311160205306.html), eff. 31 Mar 2024) | Actual receipts, excl. shipping, coupons, refunds |
| Douyin | Merchant technical service fee | Settlement base × category rate ([rule](https://school.jinritemai.com/doudian/web/article/106833), eff. 30 Sept 2026) | Payment incl. shipping + host and platform coupons + payment subsidy |
| Douyin | Creator technical service fee | **10% of the promotion fee**; 20% at C grade, 40% at D, from 8 July 2026 ([公示 notice](https://school.jinritemai.com/doudian/web/article/aJr9UHPCrEHH), 2026) | The promotion fee itself |
| Kuaishou | Merchant technical service fee | Category rate, **+0.4 points** on credit or pay-later orders ([资费一览表](https://edu.kwaixiaodian.com/rule/web/detail?id=MTyo1cSYcX), 2 Sept 2026) | Payment incl. shipping + host and platform coupons |
| Kuaishou | Platform promotion service fee | **10% of the host's commission**, currently waived ([rule](https://edu.kwaixiaodian.com/rule/web/detail?id=mB1L9k7Oza)) | The commission |

Dates matter as much as the numbers. Taobao's fee applies to orders placed from 1 Sept 2024, annual confirmed sales up to ¥120,000 are refunded in full, and the ¥60 cap runs to 30 Nov 2026. The live fee rule was published 24 Mar 2024 ([agreement](https://terms.alicdn.com/legal-agreement/terms/b_platform_service_agreement/20240311160205306/20240311160205306.html), 11 Mar 2024).

The creator-side fee is a fee on a fee. The merchant pays, say, ¥20 of promotion fee, and the platform takes part of that ¥20 before host or agency sees anything. Douyin's revised rule is explicit: the promotion fee is the base, and the band rate is 10% at grades A, B+ and B, 20% at C, 40% at D ([Douyin 公示 notice on the 精选联盟 promotion-fee rule](https://school.jinritemai.com/doudian/web/article/aJr9UHPCrEHH), 2026). Kuaishou publishes the same 10% on the host's commission, and says it is currently waived (rule cited above).

The second feature is re-rating. Douyin ran a flat 10% for years, then replaced it in July 2026 with five grades, re-assessed every month from the previous month's performance and applied to orders paid from the 9th to the 8th ([公示 notice](https://school.jinritemai.com/doudian/web/article/aJr9UHPCrEHH), 2026). The top grades get a rebate rather than a discount: A and B+ keep the 10% headline rate and receive a separate incentive payment, so their effective rate falls below 10%. That spread is wider than any merchant-side rate change I found.

Kuaishou shows how much these models differ historically. From 20 July 2019 it took 50% of the promoter's actual commission on commission-bearing listings, and 5% of order value where none was attached ([Beijing News](https://m.bjnews.com.cn/detail/156198829414583.html), 1 July 2019).

## Layer two: the fixed fee, then the commission

A 2020 reporting package put slot fees at tens of thousands to hundreds of thousands of yuan, varying with host size, and commission at 20–30% of transaction value ([Xinhua / Banyuetan](http://www.xinhuanet.com/politics/2020-07/10/c_1126218817.htm), 10 July 2020). Press figures, no methodology — historical and single-source.

The commission rate is merchant-set inside platform limits. Taobao Live's fee rule puts the ceiling at 80% with no published minimum ([热浪引擎平台资费规则](https://www.maijiaw.com/article/511372), effective 25 Feb 2022; reproduced in trade press only). Kuaishou allows 0%–90% ([快分销结算规则](https://edu.kwaixiaodian.com/rule/web/detail?id=mB1L9k7Oza)). The plausible band is far narrower than either ceiling, but no rulebook says so.

Taobao Live also rebated the live fee in full for orders placed between 1 Sept 2024 and 31 Aug 2025 ([report of the platform's 2 Sept 2024 announcement](https://finance.sina.com.cn/tech/digi/2024-09-03/doc-incmvuvt7197228.shtml), 3 Sept 2024), which is why the charge looks new and old at once.

## Layer three: the agency and the host

The private contract is where sourcing runs out, but the platform-side splits are published.

- Taobao Live takes 30% of the promotion fee from an agency-affiliated host and 40% from an individual one, so a signed host's cut is already 70% or 60% before an agency acts ([热浪引擎平台资费规则](https://www.maijiaw.com/article/511372), effective 25 Feb 2022).
- Douyin's MCN rule states the same 10% platform cut, then divides the remainder into an agency share and a host share at whatever ratio the two agreed ([Douyin 巨量百应 MCN 机构管理规范](https://school.jinritemai.com/doudian/web/article/114051), undated page).
- For scale: an industry association report counts 29,000 agencies in China as of May 2025 and puts the sector's revenue at ¥63.6 billion, expected to pass ¥70 billion in 2025 ([Economic Information Daily on the report](http://jjckb.xinhuanet.com/20250630/ee0522fc62c3416fb6bbf2c4a4d8b713/c.html), 30 June 2025).

Every "the agency takes 70%" claim I saw traces to a single undated explainer or a contract template. **Industry-common figure, unverified.**

## When the money actually lands

**Unsettled** means paid but not yet matured; a refund can still reduce it. **Settled** means receipt is confirmed, the waiting period has run, fees are deducted, and the remainder sits in a balance ([Kuaishou settlement rule](https://edu.kwaixiaodian.com/rule/web/detail?id=I9qYRHe9M6), revision notice dated 7 Aug 2023).

| Platform | Waiting period, from confirmation of receipt |
|---|---|
| Kuaishou | **7 days** at the top service-score tier, 15 days in the middle band, 20 days at the bottom |
| Douyin | **3 days** for categories with an after-sales window of 30 days or less; **10 days** for longer windows; **21 days** for shops on the zero-deposit programme |
| Taobao | Fee deducted in real time at confirmation of receipt |

Kuaishou's 7 days is what its distribution rule states, but the settlement rule underneath is tiered by the host's service score ([cycles](https://edu.kwaixiaodian.com/rule/web/detail?id=xg9G803Ru5)). Douyin's spread replaced an older model keyed to probation status and experience score, and is now tied to the category's after-sales window ([细则](https://school.jinritemai.com/doudian/web/article/111412), 7 Sept 2026). Creator commission rides on the merchant's clock throughout. That spread is the point of a settlement period as a risk instrument.

## The same chain on TikTok Shop

TikTok publishes this more cleanly, which makes it a useful yardstick.

| | United States | United Kingdom | Singapore |
|---|---|---|---|
| Seller commission | **6%** referral fee from 1 Apr 2024; five jewellery sub-categories 5% from 31 Oct 2024 | **9% incl. VAT**; electronics and selected beauty 5% | — |
| Settlement | **31 / 8 / 5 / 1 days after delivery** by tier; a 3.5+ or 4.0+ shop score unlocks the faster tiers | 3 or 15 days after delivery for creator commission | **1 / 3 / 8 / 15 days** (express, accelerated, standard, extended); express needs a 4.5+ shop rating |
| Held back | Reserve on each delivered order for **30 days** | — | — |
| Alternative | Daily Advance, up to **80%** of shipped net sales the day after shipment, from a third-party financier | — | — |
| Refunds | Referral fee refunded minus a **20% admin fee**, capped at **$5 per SKU** from 15 May 2025 | Full return → full seller commission refunded | — |

US: TikTok's own [referral fee](https://seller-us.tiktok.com/university/essay?knowledge_id=5982454398175018&lang=en), [category rate](https://seller-us.tiktok.com/university/essay?knowledge_id=5988482086864682&lang=en), [settlement tier](https://seller-us.tiktok.com/university/essay?knowledge_id=1167036928444174&lang=en), [reserve](https://seller-us.tiktok.com/university/essay?knowledge_id=3995852763531009&lang=en) and [Daily Advance](https://seller-us.tiktok.com/university/essay?knowledge_id=6571979961239339&lang=en) pages. UK: its [commission fee policy](https://seller-uk.tiktok.com/university/essay?knowledge_id=3337893683398432) and [creator payout rules](https://seller-uk.tiktok.com/university/essay?knowledge_id=7753767378814721). Singapore: its [settlement page](https://seller-sg.tiktok.com/university/essay?knowledge_id=8150481751656193&lang=en).

TikTok's creator-side formula is (product price excluding tax − seller discount) × commission rate, a narrower base than the merchant side: shipping and platform-funded discounts sit inside the seller's referral base but not the creator's ([UK guidebook on financial statements](https://seller-uk.tiktok.com/university/essay?knowledge_id=5556009217296150)). A refund reverses the creator's commission before it pays, not after. That is one reason a host's number and the platform's settled number drift apart.

## Returns: who eats the refund

- **Taobao.** Refund after receipt: the fee does not come back. Before receipt: no fee. The help page's own worked example is a ¥100 order settling at ¥99.40 ([Taobao help centre](https://helpcenter.taobao.com/servicehall/content_layout?pointId=399385564309116268), 2 June 2026).
- **Taobao Live.** A partial refund recalculates the fee on the reduced amount. A full refund with no merchant fault returns the fee, unless the merchant was on a discount scheme. Offline refunds get nothing ([Live software service fee agreement](https://terms.alicdn.com/legal-agreement/terms/b_platform_service_agreement/20240311160205306/20240311160205306.html), 11 Mar 2024).
- **Douyin.** A refund inside the after-sales window, after settlement, returns the fee proportionally. Outside the window, nothing ([Douyin merchant technical service fee rule](https://school.jinritemai.com/doudian/web/article/106833), 29 Sept 2026).
- **Kuaishou.** The commission base is recomputed as the original amount minus what was refunded; if that goes negative, the base is zero ([Kuaishou settlement rule](https://edu.kwaixiaodian.com/rule/web/detail?id=I9qYRHe9M6)).
- **TikTok.** The seller's commission returns minus the administration fee. The creator's pays only after disputes, refunds or returns resolve, and its base already excludes them.
- **Host wages.** A 2022 court report describes a company deducting refunds from a host's pay after a livestream underperformed; without an agreement on that point, the court held the wages payable and ordered the ¥6,612 owed ([People's Daily legal report](http://society.people.com.cn/n1/2022/1124/c1008-32573354.html), 24 Nov 2022). Clawback from pay is a contract term, not a platform rule.

Commission on a refunded order is usually clawed back in a *later* period than the order itself, so month-by-month comparisons never tie out. Douyin's mechanic is explicit: a 5% reserve is held back from the last 15 days of settled commission, and late refunds are drawn from it ([公示 notice](https://school.jinritemai.com/doudian/web/article/aJr9UHPCrEHH), 2026).

## The waterfall, on one hypothetical ¥100 order

The ¥100 is arithmetic, not a published rate card. Only the percentages marked as sourced are sourced.

```
Buyer pays                                              ¥100.00
  − platform order-level fee    Douyin formula; rate table not opened
  − merchant-set promotion fee  20%  [2020 press: 20–30%]    ¥ 20.00
      − platform cut of the fee 10%  [Douyin; Kuaishou]      ¥  2.00
    = agency, then host                                      ¥ 18.00
        agency/host split       private contract, ratio not published
  + slot fee, up front          tens of thousands to hundreds of thousands
  − returns                     any refund inside the window rewrites the base
  = settled                     3–21 days after receipt (Douyin); 7+ (Kuaishou)
```

If the order comes back, the promotion-fee base drops and the platform's cut with it. Whether the merchant-side fee returns depends on the platform and the refund window.

## How I would check any of this

Open the rule, not the blog post. Rules carry an effective date and a revision history, and a rate quoted without one is a rumour with a number attached. When the rule says the rate is in an annex, the annex is the rate. When a rule page renders in a browser but returns nothing to a reader, say so.

## What I could not check

- **The Taobao Live category rate table.** The rule gives the formula and points to a separate annex, which would not open. The only rate I could tie to a source is the 3% charged on the pilot categories — one bags category and one jewellery sub-category — when the rule started. Wider ranges for the annex circulate in trade press; I could not trace one to a rule, so the pilot rate is all I state.
- **Douyin's and Kuaishou's merchant-side category rates.** Both publish the formula, base and refund logic; both rate tables are in-product lookups. Kuaishou's fee schedule page documents the +0.4-point adjustment but did not render its table.
- **The live 热浪引擎 fee rule page.** The 80% ceiling and the 30%/40% platform cut come from rule text reproduced in trade press. The page on Taobao's rule centre returned no rule text to me.
- **The Kuaishou distribution rule's revision date.** The page carries no visible date, so I cannot say when the 10% or the 0%–90% range last changed.
- **Any agency–host split percentage.** No platform publishes one. Douyin's MCN rule states the platform's cut and leaves the split to agreement, which is the honest answer.
- **The 20–30% commission range and all slot-fee figures.** Press reporting, 2020, historically specific, no methodology.
- **Platform GMV figures.** One industry data service puts 2024 live-commerce transaction volume at ¥5.3256 trillion, up 8.31% ([网经社](https://www.100ec.cn/detail--6649899.html), 9 June 2025). A report published the same period cites about ¥5.8 trillion for 2024 on a different definition ([直播电商高质量发展报告](https://ciecc.ec.com.cn/upload/article/20250508/20250508102036216.pdf), 2025). Industry estimates, not audited filings, and what counts as a livestream sale varies.
- **Return and refund rates.** The commonly cited pair — women's clothing at 50–60%, livestream women's clothing above 80% — comes from a research unit and a research centre, reported by a national newspaper, not from platform disclosure ([People's Daily Overseas Edition](https://paper.people.com.cn/rmrbhwb/pc/content/202507/17/content_30088387.html), 17 July 2025).
- **Whether the ¥60 cap is still running when you read this.** The help page says orders placed and confirmed up to 30 Nov 2026, and the page itself is dated 2 June 2026.
