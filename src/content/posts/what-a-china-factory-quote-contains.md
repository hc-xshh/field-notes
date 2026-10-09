---
title: What a China factory quote actually contains
description: A field-by-field pass over a quotation for a custom part — what is on the page, which lines carry the money, and which numbers nobody publishes.
date: 2026-10-09
lang: en
topic: supply-chain
tags: [trade-and-logistics, sources-and-method]
---

I buy small runs of custom parts from factories in China. At that size there is no portal. The
quote arrives as a PDF: a summary row on top, a pile of line items underneath. Buyers read the
summary row. The lines are where the money is, and most of them sit on a rate card that somebody
else already publishes.

## The fields on the page

A quote is a filled-in version of the buyer's enquiry sheet. The closest thing to a canonical copy I
have found is a mould enquiry form (模具询价单) in a course reader hosted by a Chinese university's
IT centre ([course reader PDF, no publication date](https://it.szu.edu.cn/__local/4/F3/5E/AD2CE36A4AAF675B88DB47851F8_B5A80496_47A88E.pdf?e=.pdf), fetched 9 Oct 2026). It
asks for part name, cavity count, part drawing number, **quotation version** and **quotation
deadline**, resin and shrinkage, and then a yes/no block covering ejection type, runner and gate
type, hot runner, slides, cooling, core and cavity steel, finish, and vent depth. The version number
is the point: two quotes are comparable only if both share it.

| Field | Why it gets skipped | Range, with source | What I ask for |
|---|---|---|---|
| Sample fee | one number quoted; freight often excluded | courier only, China→US zone 6: **CNY 446**/0.5 kg document, **CNY 505**/0.5 kg non-document, **CNY 1,959**/5 kg non-document ([DHL Express Service & Rate Guide 2026: China](https://mydhlplus.dhl.com/content/dam/downloads/cn/en/rate-guide/service_and_rate_guide_cn_en_2026.pdf.coredownload.pdf), 2026 edition, fetched 9 Oct 2026) | whether it covers freight and clearance; whose courier account |
| Tooling / mould fee | never itemised | total only; no public per-item card (see below) | its own invoice line, never in the unit price |
| MOQ | one number quoted; two exist | private-mould injection parts run to MOQ ≥1,000 pieces while common-mould work takes 50 ([1688 Wiki, undated, fetched 9 Oct 2026](https://wiki.1688.com/zh/WKfw66ruc97i0w)) | manufacturing MOQ and packaging MOQ as separate numbers |
| Payment terms | the split hides where risk sits | 30% deposit, 70% before shipment: **industry-common figure, unverified** | the instrument (T/T or L/C); who pays intermediary deductions |
| Bank and FX charges | never on the factory's paper | **0.1%** of amount, min **USD 50**, max **USD 300**, plus **USD 30** cable; correspondent charges "according to actual amount deducted"; inward payment max **USD 50** ([Credit Agricole CIB China standard tariff, effective 10 April 2026](https://www.ca-cib.com/sites/default/files/2026-01/China%20tariff%20change%20notification%2010%20April%202026_EN.pdf)) | OUR / BEN / SHA stated in the contract |
| Quote validity | reads as a formality | USD/CNY central parity **7.0187** on 7 Jan 2026 → **6.7330** on 9 Oct 2026, a 4.07% renminbi appreciation ([PBOC announcement, 7 Jan 2026](https://www.pbc.gov.cn/zhengcehuobisi/125207/125217/125925/2026010708585639138/index.html); [9 Oct 2026](https://www.pbc.gov.cn/zhengcehuobisi/125207/125217/125925/2026100909035869734/index.html)) | a named fixing date, not a day count |
| Inspection / QC | filed under "buyer's account" | **0.7%** of declared value, min **CNY 5,000**, or **CNY 2,500 per man-day** ([CCIC provincial company fee notice, 11 April 2024](https://hb.ccic.com/xxgk/sfgs/art/2024/art_0ae8729fc7b14ad0aaad6d08b8003fd2.html)) | the man-day rate *and* man-day count |
| Packaging and marks | looks like logistics; priced as material and freight | non-conveyable **CNY 155**, oversize **CNY 155**, non-stackable pallet **CNY 2,340** ([DHL guide 2026: China](https://mydhlplus.dhl.com/content/dam/downloads/cn/en/rate-guide/service_and_rate_guide_cn_en_2026.pdf.coredownload.pdf), same edition) | carton spec, stack height and pallet footprint before tooling |

## The tooling line is one number with a known shape

Mould makers do not itemise a mould. "Mould: USD X." The structure of X is documented: a paper in
*Die & Mould Industry* (《模具工业》, 2005, No. 2, article 1001-2168(2005)02-0054-04) describes a
mould centre's own quotation system and gives the trade's model — **materials** (mould base, plates,
slides, hardware) + **machining** (design, CNC milling, wire cutting, EDM, machining, fitting, heat
treatment, surface treatment, trial moulding) + **overhead** (the paper's worked example: 10% of the
first two) + **profit** ([paper text, course reader copy of the 2005 journal article](http://m.download.cucdc.com/wenku/b9ae6e95c08f404684847d86979cd4f0.html), fetched 9 Oct 2026). The sentence that matters: part of the profit sits in a
profit line and part is *hidden inside the material and machining detail lines*. "Show me the
breakdown" is not a request for transparency; it is an opening bid.

| Tooling sub-item | Costed as (same paper) | Public per-item rate? |
|---|---|---|
| Mould base | catalogue size series; custom bases quoted after a stock and machining assessment | **sizes** public, prices not ([LKM standard mould bases, side-gate system](https://www.lkm.com.cn/mould_base_side_gate_system.php), undated, fetched 9 Oct 2026: 150 × 150 mm to 1000 × 1300 mm, twelve model variants) |
| Cavity / core steel | L × W × H × density × unit-weight cost | no |
| CNC milling | hours × average hourly rate | no |
| Wire-cut EDM | length of cut | no |
| Sinker EDM | hours × average hourly rate (listed as a trade, like the rest) | no |
| Surface treatment / finish | its own trade in the same list | no |
| T1 trial shot | its own trade line (试模, trial moulding) | no |

The tooling line is quotable **only as a total**; read a five-line breakdown as an aid to judgement,
not as cost data.

## Sample fee

The sample itself is labour plus a little resin; moving it is what costs. DHL's 2026 China guide
puts the United States in zone 6 for export, and its rates "exclude customs duties, taxes,
clearance-related charges, VAT and all surcharges" ([DHL 2026: China, rate tables and surcharge
pages](https://mydhlplus.dhl.com/content/dam/downloads/cn/en/rate-guide/service_and_rate_guide_cn_en_2026.pdf.coredownload.pdf), fetched 9 Oct 2026). The surcharges then arrive from the same document:
fuel, a percentage of transport and applicable services reset from a U.S. Gulf Coast kerosene-type
jet-fuel index; remote-area delivery at CNY 4/kg, minimum CNY 200; shipment insurance at CNY 100 or
1% of stated value; address correction at CNY 87. On a T1 sample the freight is routinely the
largest item, and if it ships collect it never reaches the factory's paper at all.

## MOQ is two numbers wearing one label

Manufacturing MOQ (mould, machine setup, resin minimum purchase) and packaging MOQ (plates or
die-cut tooling for carton and label) diverge, and usually only one is quoted. 1688's own wiki puts
private-mould injection parts at MOQ ≥1,000, common-mould or standard-structure goods at 50, and
attribute-level customisation at 50–200 ([1688 Wiki, undated, fetched 9 Oct 2026](https://wiki.1688.com/zh/WKfw66ruc97i0w)); a
second page from the same source says deep customisation on structure, material or size "usually
jumps to 50–500 pieces", and that suppliers who list "property customisation" options often set a
separate MOQ per option — 100 pieces for a packaging change, 300 for a size change
([1688 Wiki, undated, fetched 9 Oct 2026](https://wiki.1688.com/zh/WKfvdmrn9t59fk)). Ask for both MOQs separately, and ask which
option you are actually selecting.

## Payment terms

The 30%/70% split is repeated everywhere and traced to nothing: **industry-common figure,
unverified**. What is documented is the machinery around it — ICC's UCP 600 for documentary credits
([ICC, UCP 600 text](https://library.iccwbo.org/content/tfb/RULES/tfb-ucp600-rules.htm)), and Incoterms 2020 for where
cost and risk transfer ([ICC, Incoterms 2020](https://iccwbo.org/business-solutions/incoterms-rules/incoterms-2020/)).

## Bank and FX charges

Worked example on a USD 20,000 balance: 0.1% is USD 20, so the **USD 50 floor** applies, plus
**USD 30** cable — USD 80 before any intermediary. The line that matters is the bank's own note that
correspondent charges are deducted "according to actual amount"
([Credit Agricole CIB China standard tariff, effective 10 April 2026](https://www.ca-cib.com/sites/default/files/2026-01/China%20tariff%20change%20notification%2010%20April%202026_EN.pdf)).
If the factory's receivable lands short, that is the mechanism, and it is in the bank's document, not
the factory's. Put OUR / BEN / SHA in the contract.

## Quote validity is a currency position

| Date | USD/CNY central parity | Source |
|---|---|---|
| 2026-01-07 | 7.0187 | [PBOC](https://www.pbc.gov.cn/zhengcehuobisi/125207/125217/125925/2026010708585639138/index.html) |
| 2026-01-30 | 6.9678 | [PBOC](https://www.pbc.gov.cn/zhengcehuobisi/125207/125217/125925/2026013008522463964/index.html) |
| 2026-10-08 | 6.7367 | [PBOC](https://www.pbc.gov.cn/zhengcehuobisi/125207/125217/125925/2026100809004488108/index.html) |
| 2026-10-09 | 6.7330 | [PBOC](https://www.pbc.gov.cn/zhengcehuobisi/125207/125217/125925/2026100909035869734/index.html) |

The PBOC authorises CFETS to publish that fixing each business day. Four percent over nine months,
between the first and last rows. If the quote is in USD and the factory converts to CNY to pay wages,
that 4% is the factory's problem and returns as an email about "recent exchange rate movements". If
the quote is in CNY and you pay in USD, it is yours. Name the fixing in the contract, not a day
count.

## Quote validity is also a steel position

Baosteel reprices monthly. Its 10 July 2026 notice raised August prices by RMB 50 per tonne across
hot-rolled, heavy plate, pickled, cold-rolled, hot-dip galvanised, colour-coated and silicon steel
([notice text via Shanghai Metals Market, 10 July 2026](https://news.metal.com/newscontent/103999608-announcement-on-baosteels-adjustment-of-china-futures-selling-prices-for-sheets-plates-in-august-2026)). Its 10 September 2026 notice raised October
prices by RMB 200 per tonne on hot-rolled, pickled and cold-rolled, RMB 200 on galvanised and
colour-coated, and RMB 100 on heavy plate ([notice text via Mysteel, 10 September 2026](https://m.mysteel.com/a/26091017/010D6559C239A922_abc.html)). Two months apart, and the second quarterly step
was four times the first.

Non-ferrous inputs move daily. The 8 October 2026 schedule from China Nonferrous Metals News
(中国有色网, published by 中国有色金属报社; the table is the Changjiang spot quote republished from
长江有色金属网, 13% tax included) lists A00 aluminium ingot at ¥23,760/tonne, 1# copper at
¥112,700/tonne, ADC12 die-casting alloy at ¥24,300/tonne and ZAMAK-3 zinc alloy at ¥27,050/tonne
([China Nonferrous Metals News, 8 October 2026](https://www.cnmn.com.cn/ShowNews1.aspx?id=474429)). A 90-day validity is three mill repricings
and some sixty non-ferrous fixings.

## Inspection and QC

CCIC's provincial company files a public fee notice (11 April 2024): inspection and appraisal at
0.7% of declared value, minimum CNY 5,000, or **CNY 2,500 per man-day**; container tallying at
CNY 750 small and CNY 875 large; Africa-bound pre-shipment inspection at CNY 800 valuation per order
plus CNY 500 loading supervision per container ([CCIC fee notice, 11 April 2024](https://hb.ccic.com/xxgk/sfgs/art/2024/art_0ae8729fc7b14ad0aaad6d08b8003fd2.html)). TÜV Rheinland's Greater China
ISO 9001 price page gives a formula, not a number — (total man-days × man-day rate + certificate
fee) × VAT + travel, VAT at 6% ([TÜV Rheinland, Greater China, undated, fetched 9 Oct 2026](https://www.tuv.com/content-media-files/greater-china/pdfs/0414-quality-management-system-according-to-iso-9001/tuv-rheinland-iso-9001-price-sc-cn.pdf)). Pin down the
rate and the count. For an out-of-market comparison, SGS publishes ₹15,000 per man-day for its NPOP
scheme in India ([SGS India tariff in APEDA format, 27 August 2025](https://npop.apeda.gov.in/sites/default/files/2025-08/SGS_India_Tariff_27082025.pdf))
— same industry, not a China rate.

## Packaging and marks

Packing gets priced twice. DHL bills a piece as *non-conveyable* (CNY 155 international) if it weighs
25–70 kg, is not fully enclosed, or is packaged in metal, wood, leather, hard or soft plastic, or
expanded polystyrene foam rather than corrugated cardboard. *Oversize* (CNY 155) is a longest side
over 100 cm or a second-longest side over 80 cm. A non-stackable pallet is CNY 2,340, and does not
apply to pallets below 25 kg ([DHL 2026: China, surcharge definitions](https://mydhlplus.dhl.com/content/dam/downloads/cn/en/rate-guide/service_and_rate_guide_cn_en_2026.pdf.coredownload.pdf)).
The packing spec is a price line decided in the same meeting as the unit price. Shipping marks — what
goes on the carton, and whether they match the packing list — have no primary rule I could find;
they are agreed per order, so agree them in writing.

## How these numbers were collected

Fetched in one sitting on 9 October 2026: operator rate cards (DHL Express China 2026, Credit
Agricole CIB China effective 10 April 2026, TÜV Rheinland Greater China, CCIC's provincial fee
notice, SGS India); state-published rates (PBOC currency fixings, China Nonferrous Metals News spot
schedule); one mill's sales-price notices (Baosteel, as reprinted by SMM and Mysteel); a mould-base
maker's public catalogue sizes (LKM); platform documentation (1688 Wiki); and two teaching documents
on mould quotes. Where a figure rests on a marketplace or editorial page rather than a rate card,
the sentence says so, and undated pages carry their fetch date instead.

## What I could not check

- **Per-item tooling prices.** CNC hours, wire-cut length, EDM, surface treatment and T1 come from
  shop-internal hour rates. No published card found; I will not copy sourcing blogs that show none.
- **The 30%/70% split.** Untraceable to a primary publisher. Industry-common, unverified.
- **"In the thousands" as a headline MOQ quote.** The phrasing circulates, but I could only verify
  the platform's own numbers — ≥1,000 for private moulds, 50 for common moulds. Neither 1688 Wiki
  page I used carries a publication date.
- **Packaging and carton MOQ norms.** No primary publisher; the only figures are platform editorial
  pages, and the tiered-price examples on them are illustrative, not data.
- **Commercial China inspection rates from SGS, Bureau Veritas and Intertek.** None publish a
  per-man-day card for consumer-goods work, and the CCIC figure is one provincial notice, so I cannot
  claim it is nationally uniform.
- **Whether Baosteel's adjustment reaches any specific part.** Flat steel, not ingot — the cadence,
  not a part price.
- **Mould steel spot prices.** No mill or index card I would cite. The tooling cost model paper is
  from 2005: method, not 2026 prices.
- **My own quotes.** Not published, and none appear above.
