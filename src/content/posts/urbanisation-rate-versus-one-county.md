---
title: Two urbanisation rates for one country
description: China's statistics office says 67.89 per cent of the country lives in a town or city. The World Bank says 66.34. Both have a source, and neither answers the question I had about one county.
date: 2026-10-09
lang: en
topic: data-and-the-world
tags: [open-data, sources-and-method]
refresh: annual
data_checked: 2026-10-09
---

Ask what share of China is urban and two official sources answer differently. The National Bureau of Statistics (NBS) puts the end of 2025 at 67.89 per cent ([2025 statistical communiqué](https://www.stats.gov.cn/sj/zxfb/202602/t20260228_1962662.html), 2026-02-28). The World Bank's World Development Indicators put the same year at 66.34 per cent ([WDI, indicator SP.URB.TOTL.IN.ZS](https://api.worldbank.org/v2/country/CHN/indicator/SP.URB.TOTL.IN.ZS?format=json), retrieved 2026-10-09, series last updated 2026-10-08).

That is not rounding. The gap is about 20.6 million people: 953.80 million urban residents counted by NBS, against 933.17 million in the World Bank series ([WDI, SP.URB.TOTL](https://api.worldbank.org/v2/country/CHN/indicator/SP.URB.TOTL?format=json), retrieved 2026-10-09). The denominators differ too — 1,404.89 million year-end residents ([NBS, 2026-02-28](https://www.stats.gov.cn/sj/zxfb/202602/t20260228_1962662.html)) against 1,406.59 million, and the World Bank's population series is a midyear estimate rather than a year-end count ([WDI, SP.POP.TOTL metadata](https://api.worldbank.org/v2/indicator/SP.POP.TOTL?format=json), retrieved 2026-10-09). This post is about what each figure counts, a year-by-year table, and then the part I cared about: what a single county in northern China can and cannot show with the same statistics.

## What each publisher is counting

**NBS counts resident population on urban territory.** The indicator is 常住人口城镇化率: the resident population of an area's urban territory as a share of that area's total resident population ([NBS statistics explainer](https://www.stats.gov.cn/zs/tjws/tjzb/202301/t20230101_1903783.html), page updated 2025-02-28). Two definitions sit underneath it.

- **Where urban begins.** The 城镇/乡村 line follows the rule the State Council approved as 国函[2008]60号, which makes the residents' or villagers' committee the unit of classification and actual construction the test ([rule text](https://www.stats.gov.cn/sj/tjbz/gjtjbz/202302/t20230213_1902742.html), approved 2008-07-12, in force 2008-08-01). Urban territory is 城区 plus 镇区: 城区 is the area connected to a district or city government seat, 镇区 the area connected to a county government seat or another town seat. A village whose houses merge into a town's built-up area is urban by that test, without anyone moving.
- **Who is resident.** A person counts as resident after living in the same township or subdistrict for six months or more ([7th census bulletin no. 3](https://www.stats.gov.cn/sj/zxfb/202302/t20230203_1901083.html), 2021-05-11), hukou or no hukou.

In census years the rate is computed from the census. In other years NBS splits the annual change into expansion of urban territory, natural growth inside urban areas, and rural-to-urban migration ([explainer above](https://www.stats.gov.cn/zs/tjws/tjzb/202301/t20230101_1903783.html)). The first of those three has nothing to do with people moving.

**The World Bank publishes the United Nations' number, not China's.** The WDI series is sourced to the UN Population Division's World Urbanization Prospects and carries the note that the data "are collected and smoothed by United Nations Population Division", with source organisation "World Urbanization Prospects, United Nations (UN) … National definitions" ([indicator metadata](https://api.worldbank.org/v2/indicator/SP.URB.TOTL.IN.ZS?format=json), retrieved 2026-10-09). It is a modelled series built on national definitions, not the Chinese administrative count.

Two sentences from that programme are worth keeping. Definitions "vary from country to country and may not be consistent, even between different data sources within a given country" ([WUP 2025 Methodology Report](https://population.un.org/wup/assets/Publications/undesa_pd_2025_wup2025_methodological_report.pdf), December 2025). And when the UN applied its harmonised Degree of Urbanization grid to the same planet, 58 per cent of the world was urban in 2025 by aggregated national definitions against 81 per cent living in cities and towns by the grid method ([WUP 2025 key messages](https://population.un.org/wup/assets/Publications/undesa_pd_2024_key_messages_wup_2025.pdf), November 2025). "Urban" is not one measurement anywhere, including here.

## Seven years, a source on every row

Rates in per cent; urban population in millions. The gap is NBS minus World Bank. World Bank values from [WDI SP.URB.TOTL.IN.ZS](https://api.worldbank.org/v2/country/CHN/indicator/SP.URB.TOTL.IN.ZS?format=json), retrieved 2026-10-09.

| Year | NBS rate | NBS urban population | World Bank rate | Gap (pp) | Sources and dates |
| --- | --- | --- | --- | --- | --- |
| 2019 | 60.60 | 848.43 | 62.71 | −2.11 | [NBS communiqué](https://www.stats.gov.cn/sj/zxfb/202302/t20230203_1900640.html), 2020-02-28; WDI |
| 2020 | 63.89 | 901.99 | 63.52 | +0.37 | [7th census bulletin no. 7](https://www.stats.gov.cn/sj/tjgb/rkpcgb/qgrkpcgb/202302/t20230206_1902007.html), 2021-05-11; WDI |
| 2021 | 64.72 | 914.25 | 64.72 | 0.00 | [NBS communiqué](https://www.stats.gov.cn/xxgk/sjfb/tjgb2020/202202/t20220228_1827971.html), 2022-02-28; WDI |
| 2022 | 65.22 | 920.71 | 65.22 | 0.00 | [NBS communiqué](https://www.stats.gov.cn/sj/zxfb/202302/t20230228_1919011.html), 2023-02-28; WDI |
| 2023 | 66.16 | 932.67 | 65.53 | +0.63 | [NBS communiqué](https://www.stats.gov.cn/sj/zxfb/202402/t20240228_1947915.html), 2024-02-29; WDI |
| 2024 | 67.00 | 943.50 | 65.89 | +1.11 | [NBS communiqué](https://www.stats.gov.cn/sj/zxfb/202502/t20250228_1958817.html), 2025-02-28; WDI |
| 2025 | 67.89 | 953.80 | 66.34 | +1.55 | [NBS communiqué](https://www.stats.gov.cn/sj/zxfb/202602/t20260228_1962662.html), 2026-02-28; WDI |

The 2020 row comes from the census bulletin, which is where the census-year figure is published.

Three things the table does not say by itself.

**Part of the NBS series has been rewritten.** Footnote 21 of the 2021 communiqué records that the year-end urbanisation rates for 2017 to 2019 were revised after the census ([NBS, 2022-02-28](https://www.stats.gov.cn/xxgk/sjfb/tjgb2020/202202/t20220228_1827971.html)). The 2019 row above is the figure as published at the time. The revised values live in the statistical yearbook, and the tables I could reach there are published as images, so I could not read them.

**There is a second Chinese rate, and it moves differently.** NBS also publishes 户籍人口城镇化率, the urban share by household registration. The 2019 communiqué put it at 44.38 per cent against 60.60 per cent for residence, and credits the figure to the Ministry of Public Security ([NBS, 2020-02-28](https://www.stats.gov.cn/sj/zxfb/202302/t20230203_1900640.html)); the 2020 census published 45.4 per cent against 63.89 ([bulletin no. 7](https://www.stats.gov.cn/sj/tjgb/rkpcgb/qgrkpcgb/202302/t20230206_1902007.html), 2021-05-11); at the end of 2023 the ministry put it at 48.3 per cent ([Ministry of Public Security briefing, reported by Xinhua](http://www.news.cn/20240527/121f429b1e8f4f3eb4907a874dfbef11/c.html), 2024-05-27). I found no official figure for 2024 or 2025. The two rates sat 16.2 points apart in 2019, 18.5 in 2020 and 17.9 in 2023 (my subtraction, from the figures linked above), which is the phenomenon NBS describes in its explainer: people move to towns faster than hukou moves.

**A related series steps, and the step is method.** 人户分离人口, people whose residence and hukou sit in different townships, was 280 million in the 2019 communiqué ([NBS, 2020-02-28](https://www.stats.gov.cn/sj/zxfb/202302/t20230203_1900640.html)) and 504 million in the 2021 one ([NBS, 2022-02-28](https://www.stats.gov.cn/xxgk/sjfb/tjgb2020/202202/t20220228_1827971.html)). The 2020 census counted 492.76 million, of whom 375.82 million were classified as 流动人口 ([bulletin no. 7](https://www.stats.gov.cn/sj/tjgb/rkpcgb/qgrkpcgb/202302/t20230206_1902007.html), 2021-05-11). A jump from 280 million to 504 million between two annual publications, 80 per cent in two years (my arithmetic from the two linked bulletins), is a change of counting basis. The item is not annual either: I searched the 2022, 2023, 2024 and 2025 communiqués and the term appears in none of them.

## The county I have data for

For the rest of this post I use a rural county in northern China. It is one county-level unit among the more than 2,000 the county yearbook covers, and I am not printing its name or its figures.

I started from impressions that anyone who visits such a place would form. Then I went looking for the columns.

**What the statistics can answer:**

- **Has the resident population fallen?** Computable, but only across censuses. County totals for 2010 and 2020 are published, and the 2020 county volume, 中国人口普查分县资料—2020 (510 yuan, published 2022-07), adds population structure and household living conditions ([NBS book page](https://www.stats.gov.cn/zs/tjwh/tjkw/tjzl/202302/t20230220_1913738.html)).
- **Hukou population, output, public finance, school enrolment.** Published by county in 中国县域统计年鉴 (县市卷), covering more than 2,000 county-level units ([NBS book page, 2019-07-08](https://www.stats.gov.cn/zs/tjwh/tjkw/tjzl/202302/t20230215_1907923.html)), at a lag of a year or two. The publisher's page describes the volume in general terms, so the column names I use come from third-party extracts rather than the book itself.
- **Was the county's urban area redefined?** NBS maintains the statistical division codes and urban/rural classification codes every year and publishes them ([NBS reply](https://www.stats.gov.cn/hd/lyzx/zxgk/202312/t20231206_1945208.html), 2023-11-13), so a change in urban territory is visible even when the population is not.

**What the statistics cannot answer:**

- **How many homes stand empty.** I could not find a housing-vacancy series published by any statistical system. The number in circulation is a survey estimate: an urban housing vacancy rate of 21.4 per cent in 2017, about 65 million dwellings ([China Household Finance Survey, 2017 urban housing vacancy report](https://chfs.swufe.edu.cn/__local/D/65/2B/57D2F2A832F77C8F3C1DDC4926E_ADF9EA0C_121D6C.pdf), 2018-12-21). That is a national sample, not a county count.
- **Who left, and where they went.** No annual county-level migration series exists in the sources I searched. The census gives one snapshot per decade, and the hukou-versus-residence difference at county level mixes departures with arrivals.
- **Unemployment.** The annual communiqué carries one national rate, 5.2 per cent on average in 2025 ([NBS, 2026-02-28](https://www.stats.gov.cn/sj/zxfb/202602/t20260228_1962662.html)). It is not broken down to province, let alone county.
- **House prices.** The monthly index quoted in the communiqué covers 70 large and medium-sized cities ([NBS, 2026-02-28](https://www.stats.gov.cn/sj/zxfb/202602/t20260228_1962662.html)). A county is not in it.

So the three claims that come up most often divide cleanly. "Nobody lives in the new blocks by the county town" has no indicator behind it anywhere. "All the young people have gone" has no indicator either, only a decennial census snapshot and a hukou-versus-residence difference. "The county's economy is shrinking" is checkable in the yearbook, at a two-year lag. Only one of the three can be checked, and it is not the one people say first.

## Why one county is not China

The county is in the tables above because its row exists in each of them. I did not pick it for being typical, and it is not.

- It is one county among more than 2,000 county-level units in the yearbook's coverage.
- The national rate is a weighted average in which large cities and their suburbs dominate, so a shrinking agricultural county and the country can move in opposite directions, both reported with equal confidence.
- A county's own urbanisation rate depends on where its 镇区 boundaries sit, which depends on the annual updating of classification codes. Two neighbouring counties with similar human geography can print different rates.

**How to run the same check on a county you know:**

1. Find its resident population in the 2010 and 2020 census county tables. That gives one real change over a long interval, with no annual noise.
2. Read its row in 中国县域统计年鉴 (县市卷) and note which columns exist. Hukou population and school enrolment are there in third-party extracts; housing stock and unemployment are not.
3. Check the county's urban/rural classification codes for the two years you are comparing. If the urban territory grew, part of any rate change is reclassification.
4. Write the claim you want to make, then find the column that would settle it. If the column does not exist, you are not making a statistical claim, whatever it feels like.
5. For housing, expect nothing. The nearest official material is unsold floor space held by developers: 766.32 million square metres of newly built commodity housing at the end of 2025, of which 402.36 million was residential ([NBS, 2026-02-28](https://www.stats.gov.cn/sj/zxfb/202602/t20260228_1962662.html)). That is developer inventory, not homes without occupants, and it is national.

## What I could not check

- **The revised NBS rates for 2017–2019.** The revision is documented in a footnote; the revised annual values are in yearbook tables published as images on the NBS site, which I could not read.
- **Which WUP vintage produced the World Bank's values for 2023–2025.** The indicator metadata names the programme and "national definitions" but not the revision year.
- **Whether the World Bank's China value equals the WUP 2025 published figure under national definitions.** The UN Data Portal lists an indicator, "Percentage of population by national urban definition", but its data endpoint returned 401 without an API key (retrieved 2026-10-09), and the download centre's national-definitions table sits behind a client-side tab whose files I could not address directly.
- **An official vacancy rate at any level.** My finding is negative: I could not find one. That is a search result, not a sourced fact.
- **Vacancy figures from CHFS rounds after 2017.** Later rounds ran — the 2025 round covered 23,277 households, mainly across 243 district- and county-level units ([survey description](https://chfs.swufe.edu.cn/dczx/dczx.htm), retrieved 2026-10-09) — and I found no published vacancy update.
- **The exact column list of 中国县域统计年鉴.** The publisher's page describes the volume in general terms; the column names I used come from third-party extracts, not from the book itself.
- **Whether this county publishes its own annual statistical communiqué with a resident-population figure.** Some counties do; I did not verify this one.
- **Any 户籍人口城镇化率 figure after 2023**, and how many provinces publish annual county-level resident population. I did not survey provincial yearbooks.
