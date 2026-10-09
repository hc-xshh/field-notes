---
title: One commodity, two customs records
description: The same lithium-ion battery shipments counted by the exporter and by the importer. The money nearly matches. The kilograms do not.
date: 2026-10-09
lang: en
topic: data-and-the-world
tags: [sources-and-method, open-data]
refresh: annual
data_checked: 2026-10-09
---

Every trade flow of any size is counted twice: the exporting country files an export, the importing country files an import. Both are official, both are published, and they rarely agree. The gap is called mirror statistics.

I spent a day on one flow: lithium-ion accumulators, HS 8507.60, from China to the United States, 2021 to 2025, annual. In 2025 the two dollar values differ by 0.2%. The two weight figures differ by 378%.

## The flow I picked

HS 8507.60 is lithium-ion accumulators. The EU's equivalent line is CN 8507 60 00. China's customs administration and the US Census Bureau each submit annual figures to UN Comtrade, which republishes them, so both sides of one flow can be pulled from a single free interface with no key. It caps you near one request per second, which I hit repeatedly. The annual path refuses monthly periods; monthly figures exist on a separate path.

## The two records

Values in US dollars.

| Year | US reports: imports from China | China reports: exports to the US | China minus US |
|---|---|---|---|
| 2021 | 4,472,880,904 | 4,942,067,377 | +10.5% |
| 2022 | 9,295,203,389 | 10,140,436,891 | +9.1% |
| 2023 | 13,217,304,176 | 13,569,075,977 | +2.7% |
| 2024 | 16,457,945,481 | 15,336,139,169 | −6.8% |
| 2025 | 11,905,965,916 | 11,933,360,986 | +0.2% |

US figures from the [UN Comtrade public preview, reporter 842](https://comtradeapi.un.org/public/v1/preview/C/A/HS?reporterCode=842&period=2023&cmdCode=850760&flowCode=M&partnerCode=156), retrieved 2026-10-09. China figures from the [same API, reporter 156](https://comtradeapi.un.org/public/v1/preview/C/A/HS?reporterCode=156&period=2023&cmdCode=850760&flowCode=X&partnerCode=842), retrieved 2026-10-09.

Units are each reporter's own count of items; weight is what each labels net weight, in kilograms.

| Year | US units | China units | China minus US | US kg | China kg | China minus US |
|---|---|---|---|---|---|---|
| 2021 | 270,958,533 | 335,557,842 | +23.8% | 200,042,198 | 193,291,709 | −3% |
| 2022 | 221,625,197 | 254,795,655 | +15.0% | 445,006,157 | 452,496,225 | +2% |
| 2023 | 169,387,306 | 224,161,539 | +32.3% | 927,840,085 | 654,443,183 | −29% |
| 2024 | 170,358,802 | 189,108,696 | +11.0% | 325,967,208 | 924,296,775 | +184% |
| 2025 | 172,030,704 | 210,204,008 | +22.2% | 196,843,537 | 940,998,916 | +378% |

Same two queries, retrieved 2026-10-09. The unit column is Comtrade's quantity field, unit code 5, which its own reference file defines as `u`, number of items ([reference file](https://comtradeapi.un.org/files/v1/app/reference/QuantityUnits.json)).

## Three metrics, three verdicts

Money. The two published values sit within 11% of each other in every year, and the sign flips: China's number is higher in 2021, 2022, 2023 and 2025, lower in 2024. For a flow this size, that is agreement on either value basis.

Item counts. China reports more units in all five years, by 11% to 32%. The direction never flips, which makes it a different signal from the value gap: a persistent offset rather than noise. Both sides report the same unit, items, so the likely reading is that the two customs services are not counting the same object — a cell, a module, a pack, a battery with its housing. I cannot test that here.

Weight. Divide weight by units and the problem is plain. In 2025 China's figures imply 4.48 kg per item; the US figures imply 1.14 kg per item. Both cannot describe the same shipment. The US weight series also contradicts itself: 445 million kg in 2022, 928 million kg in 2023, 326 million kg in 2024, 197 million kg in 2025 — 2.0, 5.5, 1.9 and 1.1 kg per item — while the unit count stays between 169 and 222 million. Comtrade marks the 2022 Chinese net weight and the 2024 US net weight as estimated, not reported.

There is a plausible mechanical reason I cannot prove from the data file. The Census Bureau's guide says the only weight it publishes is shipping weight: gross weight including wrappings, crates and containers, and only for vessel and air shipments ([Census guide, section 9](https://www.census.gov/foreign-trade/guide/sec2.html), accessed 2026-10-09). That is my reading of the document, not something the trade record states.

## Does the valuation rule explain it?

The standard first answer to a mirror gap is valuation. Exporters report FOB; importers usually report CIF, which adds freight and insurance to the destination port, so imports should exceed exports by a few percent.

The United States is an exception, and that is why I chose it as the mirror. US import value is customs value: the price actually paid or payable for the goods when sold for export to the United States, excluding US import duties, freight, insurance and other charges incurred in bringing them in ([Census guide, section 6](https://www.census.gov/foreign-trade/guide/sec2.html), accessed 2026-10-09). On paper that is the same basis as China's FOB export value. The table above uses Comtrade's published import value, though, which for the US is the CIF figure, so those charges are inside it. The same US record carries a second, FOB value, 1.2% to 2.0% lower in 2022–2025 and absent for 2021. On that customs basis the gap runs from −5.6% in 2024 to +11.3% in 2022.

The EU supplies the other case. Eurostat states that extra-EU imports are valued CIF and exports FOB, and that for imports the partner is the country of origin while for exports it is the country of final destination ([Eurostat, International trade in goods](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=International_trade_in_goods_-_selected_topics), accessed 2026-10-09). The same batteries entering the EU should be recorded higher on the EU side.

| Year | EU reports (CIF, EUR) | converted to USD | China reports (FOB, USD) | EU minus China | EU kg (net mass) | China kg | EU minus China |
|---|---|---|---|---|---|---|---|
| 2021 | 6,488,838,350 | 7,674,349,117 | 8,917,616,897 | −13.9% | 218,033,088 | 310,006,083 | −29.7% |
| 2022 | 17,598,463,117 | 18,531,181,662 | 19,535,561,563 | −5.1% | 579,522,501 | 660,409,908 | −12.2% |
| 2023 | 23,259,741,834 | 25,150,758,845 | 23,354,336,657 | +7.7% | 813,302,239 | 791,298,476 | +2.8% |
| 2024 | 19,619,572,289 | 21,236,225,046 | 20,513,992,883 | +3.5% | 935,001,880 | 938,836,360 | −0.4% |
| 2025 | 25,650,086,052 | 28,984,597,239 | 29,272,424,192 | −1.0% | 1,522,030,924 | 1,655,915,264 | −8.1% |

EU values and net mass from the [Eurostat Comext API, dataset DS-045409](https://ec.europa.eu/eurostat/api/comext/dissemination/statistics/1.0/data/DS-045409?format=JSON&reporter=EU27_2020&partner=CN&product=850760&flow=1&time=2025), data vintage 2026-09-15, retrieved 2026-10-09. China's exports to the 27 member states from the [UN Comtrade public preview, reporter 156](https://comtradeapi.un.org/public/v1/preview/C/A/HS?reporterCode=156&period=2025&cmdCode=850760&flowCode=X&partnerCode=40,56,100,196,203,276,208,233,724,246,251,300,191,348,372,380,440,442,428,470,528,616,620,642,752,705,703), retrieved 2026-10-09; Comtrade's preview returned nothing for its EU aggregate partner code, so I summed the 27 members. Currency conversion at the Eurostat annual average EUR/USD rate, [dataset ert_bil_eur_a](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/ert_bil_eur_a?format=JSON&currency=USD&statinfo=AVG&time=2025), retrieved 2026-10-09: 1.1827 for 2021, 1.0530 for 2022, 1.0813 for 2023, 1.0824 for 2024, 1.13 for 2025.

The CIF rule is real and points one way every year, but the gap does not follow it: after conversion the EU's CIF figure sits below China's FOB figure in three of the five years. The wedge is in the definitions, not in the numbers. My conversion is blunt too: an annual average over trade invoiced in several currencies, where a small freight margin can hide.

The weight columns here behave far better. In each of the last three years the EU's net mass and China's net weight agree within 8.1%, and in two of those within 3% — two customs systems, one net weight each, landing on nearly the same tonnage. That contrast is the strongest evidence in this piece that the US weight column is the odd one out. It is not evidence that anyone is cheating.

## Two more explanations, one with a paper trail

Origin versus destination. China records an export against the destination the exporter declares. The United States records an import against the country of origin. A battery made in China, sold to a buyer in Singapore and forwarded to Texas, is a Chinese export to Singapore and later a US import from China. That mechanism pushes US imports above China's exports. In my data the gap runs the other way in four years out of five, so at this level it is not the dominant term. Sizing it needs shipment-level data I do not have.

Classification. A Congressional Research Service report updated in November 2025 records that US exports of non-lead-acid battery parts to Mexico rose from $43 million in 2023 to $1.9 billion in 2024 while "Mexico's import data do not show increases in battery part imports from the United States". The report's reading is "some HTS classification differences between the United States and Mexico" ([CRS report R48538, version 8](https://www.congress.gov/crs_external_products/R/PDF/R48538/R48538.8.pdf), updated 26 November 2025, accessed 2026-10-09). Two neighbours, one commodity, records that do not match, and the explanation offered is tariff lines.

The US tariff schedule now splits HS 8507.60 into statistical lines for batteries used as the primary power source in electric vehicles, for fully encased battery energy storage systems, and for everything else, with quantity reported in numbers and kilograms ([USITC Harmonized Tariff Schedule, ch. 85, Revision 20 (2026)](https://hts.usitc.gov/search?query=8507600), 8507.60, accessed 2026-10-09). HS6 8507.60 is a single number internationally, so a shift in the mix between those lines moves the weight per unit, the value per unit and the tariff treatment while leaving the HS6 comparison intact. The same report notes the code itself moved: US lithium-ion imports sat under HTS 8507.80.8010 from 2009 to 2011 and under 8507.60 from 2012.

## The incentive I went looking for

A large tariff gives an importer a reason to declare less at the border than the goods are worth. If that were happening at scale, US import values would sit well below China's export values, and the gap would widen after each tariff step. The steps are documented: lithium-ion batteries for electric vehicles went to 25% for entries on or after 27 September 2024, and lithium-ion batteries for everything else go to 25% on 1 January 2026 ([Federal Register 2024-21217](https://www.federalregister.gov/documents/2024/09/18/2024-21217/notice-of-modification-of-section-301-actions-four-year-review), published 18 September 2024, accessed 2026-10-09).

In 2025, the first full year of the EV rate, US reported imports from China fell 27.7% to $11.91bn and China's reported exports to the US fell 22.2% to $11.93bn. The records ended the year 0.2% apart, closer than any earlier year in the table. Both services agree on the direction and the rough size of the decline. I did not find a smuggling signature in the annual aggregates. That is not proof there is none: under-invoicing at both ends would cancel out, and I have no firm-level data.

## Method

- Commodity: HS 8507.60, lithium-ion accumulators excluding spent; CN 8507 60 00 in the EU nomenclature. Comtrade returns 2021 under classification code H5 and 2022–2025 under H6.
- Reporters: China (Comtrade code 156) and the United States (842) for the China-to-US flow; China (156) and the 27 EU member states summed for the China-to-EU flow. Both flows 2021–2025, annual.
- Fields: `primaryValue` in US dollars, `qty` with `qtyUnitCode` 5, `netWgt` in kilograms. Flow `X` for exports, `M` for imports. Partner 842 or 156, or the 27 member codes.
- EU figures: Comext dataset DS-045409, reporter EU27_2020, partner CN, product 850760, flow 1 (imports), indicators VALUE_IN_EUROS and QUANTITY_IN_100KG, converted from hundreds of kilograms.
- Currency: Eurostat annual average EUR/USD, dataset ert_bil_eur_a.
- Retrieval 2026-10-09, China Standard Time. Comext vintage 2026-09-15; the exchange-rate table last updated 2026-07-08. Both APIs are free, keyless and rate-limited. 2025 is the most recent complete year and remains subject to revision.

## What I could not check

- China's own portal, stats.customs.gov.cn, answers requests with HTTP 412. The Chinese figures here are what China submitted to UN Comtrade, not what its domestic tool shows today.
- The Census Bureau's trade API refuses requests without a key, so the US figures are Comtrade's republication of the US submission, not the primary. USA Trade Online needs an account I do not have.
- The US net weight for 2023, 927,840,085 kg, is inconsistent with the US's own 2022 and 2024 values and with China's 2023 value. I cannot tell which of those numbers is wrong.
- Whether the US weight column is Census shipping weight. That is my inference from the definition, not a statement in the trade record.
- Monthly timing. Monthly figures exist, but for this flow China's monthly series stops at December 2024 in the preview, so the two records can be compared month by month only through 2024.
- Whether the EU's CIF figures would still sit below China's FOB under a conversion matched to invoice currencies rather than an annual average.
- Domestic production and consumption. Both records count only what crosses a border: a battery assembled in China for a Chinese factory appears in neither.
