---
title: China's parcel count and the world's, side by side
description: China's official express volume and the world's e-commerce parcel totals are different measurements. Here is the year-by-year table, with a source and a date on every number.
date: 2026-10-09
lang: en
topic: data-and-the-world
tags: [open-data, rails-and-infrastructure]
refresh: annual
data_checked: 2026-10-09
---

Two numbers get quoted at each other in writing about parcel logistics: China's express delivery volume from the State Post Bureau, and the world's e-commerce parcel count from a market research firm. They get put in one sentence, divided, and turned into a percentage.

The division is not valid. This page shows why, and it is built to be updated once a year.

The numbers I was handed were 198.95 billion parcels for China in 2025, an estimated 121 billion e-commerce parcels worldwide, and a claim that China is about 60 percent of that. Both volumes trace to a source. The percentage does not.

## The two anchor numbers, checked

**China, 2025: 198.95 billion parcels** (1,989.5亿件), up 13.6 percent on 2024 ([State Post Bureau, 2026-01-22](https://www.spb.gov.cn/gjyzj/c100015/c100016/202601/e6e402458627430daca67f9354c179ed.shtml)). It splits into 15.79 billion same-city, 178.94 billion inter-city, and 4.22 billion international plus Hong Kong, Macau and Taiwan ([same release](https://www.spb.gov.cn/gjyzj/c100015/c100016/202601/e6e402458627430daca67f9354c179ed.shtml)); only the last crosses a border.

**World, 2025: 121 billion business-to-consumer e-commerce parcels**, up 10 percent ([ECDB, 2025-12-15](https://ecdb.com/blog/global-parcel-market-2025-growth-at-scale-power-in-few-hands/5168)). The release is written as an expectation, published two weeks before the year it describes had ended, so it is a forecast rather than a count. The same article puts e-commerce at 63 percent of the total parcel market in 2025, which implies about 192 billion parcels of all kinds. The 192 is my division, not their number.

ECDB's page says around 60 percent of global B2C e-commerce parcels originate in China, without printing a Chinese total. The 81 billion in circulation comes from a trade write-up of the same data ([E-Commerce Germany News, 2026-01-09](https://ecommercegermany.com/blog/the-global-e-commerce-parcel-market-121-billion-in-volume-and-one-clear-country-leader/)). 81 ÷ 121 = 67 percent. Same figures, same release cycle, two answers.

## The two series do not count the same thing

**The Chinese number counts items at acceptance, not on delivery.** It covers enterprises holding an express business licence and their filed branches ([State Post Bureau statistical survey system published by the National Bureau of Statistics, 2024-04-23](https://www.stats.gov.cn/fw/bmdcxmsp/bmzd/202404/t20240423_1948654.html)), and excludes China Post's own parcel business, stated beside the indicator name ([State Post Bureau, 2024-01-22](https://www.spb.gov.cn/gjyzj/c100015/c100016/202401/59eeb6e8b0e7404f8127aa2c7aebded6.shtml)). The bureau defines handling volume (处理量) as business volume (业务量) plus delivery volume (投递量) ([State Post Bureau, 2026-01-22](https://www.spb.gov.cn/gjyzj/c100015/c100016/202601/e6e402458627430daca67f9354c179ed.shtml)), which puts the headline in the acceptance term. Business shipments, documents, samples and returns sit in the same count, with no weight ceiling. The 2024 bulletin records that some enterprises adjusted their reporting scope, and gives growth on a comparable basis ([State Post Bureau, 2025-05-22](https://www.spb.gov.cn/gjyzj/c100276/202505/1cc8240e52ee42079d362416fccec8b4.shtml)).

**The nearest thing to a world total used China's number as its China column.** The Pitney Bowes index measured business-to-business, business-to-consumer, consumer-to-business and consumer-consigned shipments up to 31.5 kg across thirteen markets ([Pitney Bowes, 2023-08-09](https://www.investorrelations.pitneybowes.com/news-releases/news-release-details/pitney-bowes-parcel-shipping-index-confirms-extended-effects)). For 2022 it put the world at 161 billion parcels and China at 110.6 billion in its report, rounded to 111 billion in the release. The State Post Bureau's own figure for 2022 was 110.58 billion ([State Post Bureau, 2023-01-18](https://www.spb.gov.cn/gjyzj/c100015/c100016/202301/c910dd57e739490ea60bda58174ef826.shtml)). The world total was partly assembled by inserting China's administrative count, which is why China looks like a majority of "the world".

**ECDB counts one slice only.** Business-to-consumer, and only where an online order is behind it. Its 81 billion for China therefore sits far below the bureau's 198.95 billion.

**The UPU counts postal operators only.** Its State of the Postal Sector 2024 puts domestic parcel post above 40 billion items in 2024 ([UPU, 2024-12-17](https://www.upu.int/en/publications/2ipd/the-state-of-the-postal-sector-2024)). That is about a fifth of ECDB's implied 192 billion, or a third of its 121 billion. Post offices and every licensed carrier are different populations.

The four global baselines are not from the same year: 40.2 billion (2024, postal operators), 121 billion (2025, e-commerce), 161 billion (2022, all parcels, thirteen markets), about 192 billion (my arithmetic, 2025).

## Year by year: China

Every figure is the State Post Bureau's express business volume (快递业务量), in billions of parcels.

| Year | Parcels (bn) | Change | Source, date |
| --- | --- | --- | --- |
| 2019 | 635.2 | +25.3% | [State Post Bureau statistical bulletin](https://www.spb.gov.cn/gjyzj/c100015/c100016/202005/3b737880d332463bb63e027d70fd4476.shtml), 2020-05-19 |
| 2020 | 833.6 | +31.2% | [annual release](https://www.spb.gov.cn/gjyzj/c100015/c100016/202101/2ef764639616407d82cba2aa6f4ae74d.shtml), 2021-01-14 |
| 2021 | 1,083.0 | +29.9% | [annual release](https://www.spb.gov.cn/gjyzj/c100276/202201/74c80cf2fd7b44c3aa5d6facb464bcb8.shtml), 2022-01-14 |
| 2022 | 1,105.8 | +2.1% | [annual release](https://www.spb.gov.cn/gjyzj/c100015/c100016/202301/c910dd57e739490ea60bda58174ef826.shtml), 2023-01-18 |
| 2023 | 1,320.7 | +19.4% | [statistical bulletin](https://www.spb.gov.cn/gjyzj/c100276/202405/ff1ab12da9d74425b7ddef9e38de8916.shtml), 2024-05-10 |
| 2024 | 1,750.8 | +21.5% | [annual release](https://www.spb.gov.cn/gjyzj/c100276/202501/460d02f2e54c4d0ebbba3a4f431d0042.shtml), 2025-01-20 |
| 2025 | 1,989.5 | +13.6% | [annual release](https://www.spb.gov.cn/gjyzj/c100015/c100016/202601/e6e402458627430daca67f9354c179ed.shtml), 2026-01-22 |

One trap. On 2025-01-08 the national postal work conference put 2024 at 174.5 billion ([State Post Bureau, 2025-01-08](https://www.spb.gov.cn/gjyzj/c100015/c100016/202501/57c75991afd94345ad26d47ebd762a63.shtml)); twelve days later the bureau's own release said 175.08 billion ([State Post Bureau, 2025-01-20](https://www.spb.gov.cn/gjyzj/c100276/202501/460d02f2e54c4d0ebbba3a4f431d0042.shtml)). The conference number comes from a speech; the release revises it.

## Year by year: the world

The global column has two bases and neither covers every row.

| Year | World, B2C e-commerce parcels (bn) | Source, date |
| --- | --- | --- |
| 2023 | ~100, my reconstruction | [ECDB, 2025-12-15](https://ecdb.com/blog/global-parcel-market-2025-growth-at-scale-power-in-few-hands/5168) plus arithmetic |
| 2024 | ~110, my reconstruction | [ECDB, 2025-12-15](https://ecdb.com/blog/global-parcel-market-2025-growth-at-scale-power-in-few-hands/5168) plus arithmetic |
| 2025 | 121 | [ECDB, 2025-12-15](https://ecdb.com/blog/global-parcel-market-2025-growth-at-scale-power-in-few-hands/5168), single source |

The reconstructions: ECDB states 121 billion for 2025 at 10 percent growth, and the write-up of the same data says 2024 grew at the same rate ([E-Commerce Germany News, 2026-01-09](https://ecommercegermany.com/blog/the-global-e-commerce-parcel-market-121-billion-in-volume-and-one-clear-country-leader/)). So 121 ÷ 1.1 = 110 and 110 ÷ 1.1 = 100, my divisions of stated growth rates; the 2024 rate rests on one second-hand sentence. Treat both rows as placeholders. The December 2025 article is the only parcel-market release from the firm I could reach, so I have nothing for 2019 through 2022.

For those years the only global series I could reach is the all-parcel one:

| Year | World, all parcels (bn) | Source, date |
| --- | --- | --- |
| 2016 | 64 | [Pitney Bowes](https://www.investorrelations.pitneybowes.com/news-releases/news-release-details/pitney-bowes-parcel-shipping-index-confirms-extended-effects), 2023-08-09 |
| 2019 | 103.2 | [Pitney Bowes](https://www.investorrelations.pitneybowes.com/news-releases/news-release-details/pitney-bowes-parcel-shipping-index-reports-continued-growth-0), 2020-10-12 |
| 2020 | 131.2 | [Pitney Bowes](https://investorrelations.pitneybowes.com/news-events/press-releases/detail/254/global-parcel-volume-exceeds-131-billion-in-2020-up-27-percent-year-over-year-finds-pitney-bowes-parcel-shipping-index), 2021-09-28 |
| 2021 | 159 | [Pitney Bowes](https://pitneybowes2023tf.q4web.com/news/news-details/2022/Pitney-Bowes-Parcel-Shipping-Index-Reveals-China-Is-First-Country-to-Ship-100-Billion-Parcels-as-Global-Parcel-Volume-Reaches-159-Billion-In-2021-09-22-2022/default.aspx), 2022-09-22 |
| 2022 | 161 | [Pitney Bowes](https://www.investorrelations.pitneybowes.com/news-releases/news-release-details/pitney-bowes-parcel-shipping-index-confirms-extended-effects), 2023-08-09 |

That series stops at 2022 data. The editions since are United States only: the current one leads with 23.1 billion US parcels in 2025 ([Pitney Bowes U.S. index, 2026 report, page read 2026-10-09](https://www.pitneybowes.com/us/shipping-index.html)). The past-reports list still names a 2024 global edition ([Pitney Bowes past reports, page read 2026-10-09](https://www.pitneybowes.com/us/shipping-index/past-shipping-index-reports.html)), but every release from 2024 onward that I could find describes US data. I cannot tell whether the global index was discontinued or paused.

## Parcels per person, and the arithmetic

I divided the bureau's volume by the National Bureau of Statistics' year-end population for the same year.

- **2025: 198.95bn ÷ 1.40489bn = 141.6 parcels per person.** Population 1,404.89 million at the end of 2025 ([National Bureau of Statistics communiqué, 2026-02-28](https://www.stats.gov.cn/sj/zxfbhjd/202602/t20260228_1962662.html)). The bureau publishes 141.6 for the same year ([State Post Bureau, 2026-05-22](https://www.spb.gov.cn/gjyzj/c100276/202605/ee4b41eb6db14e2ca8b5950626585fe0.shtml)), and its own note says the population denominator comes from that communiqué.
- **2024: 175.08bn ÷ 1.40828bn = 124.3 parcels per person.** Population 1,408.28 million at the end of 2024 ([National Bureau of Statistics communiqué, 2025-02-28](https://www.stats.gov.cn/sj/zxfb/202502/t20250228_1958817.html)). The bureau publishes 124.3 for that year ([State Post Bureau, 2025-05-22](https://www.spb.gov.cn/gjyzj/c100276/202505/1cc8240e52ee42079d362416fccec8b4.shtml)).

Two caveats. The denominator includes infants, so this measures volume per head rather than what one person receives. The numerator is counted at acceptance, so a parcel is booked where it was posted.

From the e-commerce side it does not reconcile. The ECDB data puts China at 81 billion parcels for 2025 and says the average Chinese consumer receives around 120 a year ([E-Commerce Germany News, 2026-01-09](https://ecommercegermany.com/blog/the-global-e-commerce-parcel-market-121-billion-in-volume-and-one-clear-country-leader/)). 81 billion divided by 1.40489 billion people is 57.7. I cannot make 120 and 81 fit without knowing their population base and whether "consumer" is narrower than "person".

## China's share, and which denominator

Four honest versions of the claim:

1. **E-commerce only: 81 ÷ 121 = 67 percent.** ECDB's own text says "around 60 percent" ([ECDB, 2025-12-15](https://ecdb.com/blog/global-parcel-market-2025-growth-at-scale-power-in-few-hands/5168)), so even this is not clean, and the 81 comes from a write-up of the same data rather than from the release itself.
2. **Share of growth, not of level.** "More than 60 percent of global courier parcel growth in 2021–2025" — the official Chinese framing, carried in English by Xinhua on 2026-01-07 ([Xinhua](https://english.news.cn/20260107/c9d9223a545d4d93998740d2aa8f04a6/c.html)). It is about the five-year increase, not the level in any one year. Some of the 60 percent claims in circulation are this one quoted out of context.
3. **Share of a Chinese official estimate of the world.** The State Post Bureau's development research centre put world volume in 2022 at about 189.2 billion items and forecast more than 200 billion for 2023, against China's own count of 132 billion that year ([Global Express Development Report 2023, released 2023-11-22, reported by the China Express Association on 2023-11-27](http://www.cea.org.cn/content/details_10_24586.html)). On its 2022 numbers China was 58 percent of the world. The report is not published online, so this reaches me through press coverage.
4. **China's express volume against ECDB's world e-commerce volume: 198.95 ÷ 121 = 164 percent.** Nonsense, and a useful test for whether a claim was built by dividing two unrelated columns.

The only defensible sentences name both sides of the ratio.

## How I checked these numbers

Every number here is the publisher's own, with a link and a date. Where a figure is not published — the 2023 and 2024 world rows, the 192 billion — I show the division behind it and say so. Where no first-hand source exists, the entry is marked single source or listed at the end.

## How I will update this page

- **Third week of January.** The year's 邮政行业运行情况 goes up on spb.gov.cn between the 14th and the 22nd of the following month. Take the number, but expect it to move.
- **May.** The full annual statistical bulletin. Quote that one once it exists, because January gets revised.
- **Late February.** The year-end population in the National Bureau of Statistics communiqué. Use the same year's figure for the per-person row.
- **Mid-December.** ECDB's parcel-market article, still labelled "expected to reach".
- **June or July, and December.** Pitney Bowes' index: current editions are US only. The UPU's Postal Statistics yearbook and State of the Postal Sector report are the postal-only series, useful as a floor.

## What I could not check

- **ECDB's own China total.** Both figures sit in a trade write-up of ECDB data, not on the ECDB article I could read. Treated here as a single source.
- **The State Post Bureau's indicator definition.** I could not fetch a document defining 快递业务量 at indicator level. "Counted at acceptance" is inferred from the 业务量 + 投递量 = 处理量 identity and from the survey system's description of who reports, which is weaker than reading the rule.
- **Any global e-commerce parcel series before 2023.** The 2023 and 2024 e-commerce values here are reconstructions, and the growth rate behind them comes from a second-hand sentence.
- **The 60 versus 67 percent discrepancy inside ECDB**, and the 120 versus 57.7 parcels-per-person discrepancy in the same data set. No methodology note found.
- **Whether Pitney Bowes' global index is discontinued or paused.** The site lists a 2024 global edition; every release I could find from 2024 onward is US-scope. Nothing states the change, so I am reading a gap.
- **The text of the Global Express Development Report 2023.** It is not published online; the 189.2 billion figure reaches me through press coverage of the launch.
- **What share of China's cross-border e-commerce volume sits outside the express count.** The 4.22 billion international figure covers parcels accepted in the mainland by licensed express enterprises. Goods leaving as freight, via overseas warehouses, or as postal items outside that population are somewhere else, and nothing I found quantifies the gap.
- **The UPU's 40 billion figure.** It comes from a modelling exercise, not a summed country table, and I could not reach the underlying data.
- **A world per-person figure.** It needs a world population denominator I have not verified, so I left it out.
