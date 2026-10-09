---
title: Fifty Chinese radicals, ranked by frequency
description: I counted how many of the 1,000 and 3,000 most common Chinese characters sit under each of the 214 Kangxi radicals, and wrote down every rule the count depends on.
date: 2026-10-09
lang: en
topic: life-in-china
tags: [everyday-china, reference-pages]
---

Search for "most common Chinese radicals" and you get the same page over and over: a list of ten, fifty or a hundred radicals, a meaning next to each, sometimes a mnemonic, occasionally a colour-coded poster. What you never get is a number. The order is asserted, not shown, so you cannot tell whether the third radical on the list is third because someone counted or because it looked tidy there.

This is that count. For each of the 214 Kangxi radicals I asked a machine-readable question: how many of the 1,000 most frequent Chinese characters are indexed under this radical, and how many of the 3,000. Then I did it a second way, against a different character list, to see whether the ranking survives.

It mostly does. The exceptions are the part worth reading.

## What I counted

| Piece | Source | Date on the source |
|---|---|---|
| Radical for each character | Unihan 18.0.0, `kRSUnicode` field in `Unihan_IRGSources.txt` ([Unihan.zip](https://www.unicode.org/Public/UCD/latest/ucd/Unihan.zip)) | files dated 2026-07-31 |
| Character frequency order | Jun Da, *Modern Chinese character frequency list* ([list](https://lingua.mtsu.edu/chinese-computing/statistics/char/list.php?Which=MO), [tab-delimited download](https://lingua.mtsu.edu/chinese-computing/statistics/char/download.php?Which=MO)) | data updated 2004-03-30 |
| Second opinion character list | 《现代汉语常用字表》 frequencies, 3,500 characters ([Jun Da's copy](https://lingua.mtsu.edu/chinese-computing/statistics/char/listchangyong.php)) | updated 2004-05-25 |
| Radical stroke counts and names | Kangxi Radicals block, U+2F00–U+2FD5 ([code chart](https://www.unicode.org/Public/18.0.0/charts/PDF/U2F00.pdf)); `kTotalStrokes` and `kMandarin` from the same Unihan release | 2026-07-31 |

Short version of the method: read each character's `kRSUnicode` value, take the integer before the decimal point, strip any apostrophe, and count the character under every radical it lists. The raw frequencies in Jun Da's file sum to 193,504,018 character tokens, and the first 1,000 entries account for 89.14% of them.

## The fifty, ranked

`in 1,000` and `in 3,000` are counts of characters, not tokens. The table is ranked by the 3,000 column, ties broken by the count in the second list and then by radical number. The examples column gives three characters under that radical, with their Jun Da rank.

| # | Radical | Unicode name | Pinyin | Strokes | in 1,000 | in 3,000 | Examples (frequency rank) |
|---|---|---|---|---|---|---|---|
| 1 | 口 | Mouth | kǒu | 3 | 50 | 160 | 和 (19), 可 (30), 后 (48) |
| 2 | 手 | Hand | shǒu | 4 | 38 | 158 | 把 (110), 手 (143), 提 (196) |
| 3 | 水 | Water | shuǐ | 4 | 37 | 153 | 法 (65), 没 (72), 海 (189) |
| 4 | 人 | Man | rén | 2 | 55 | 131 | 人 (7), 他 (10), 们 (13) |
| 5 | 木 | Tree | mù | 4 | 39 | 120 | 来 (15), 样 (88), 本 (92) |
| 6 | 心 | Heart | xīn | 4 | 29 | 99 | 心 (90), 想 (99), 意 (104) |
| 7 | 艸 | Grass | cǎo | 6 | 18 | 92 | 英 (371), 花 (410), 落 (496) |
| 8 | 言 | Speech | yán | 7 | 33 | 76 | 说 (24), 话 (170), 论 (205) |
| 9 | 糸 | Silk | mì | 6 | 23 | 70 | 经 (62), 给 (180), 系 (216) |
| 10 | 辵 | Walk | chuò | 7 | 25 | 64 | 这 (11), 过 (46), 道 (52) |
| 11 | 肉 | Meat | ròu | 6 | 11 | 62 | 能 (35), 育 (609), 脸 (615) |
| 12 | 土 | Earth | tǔ | 3 | 17 | 61 | 在 (6), 地 (21), 场 (249) |
| 13 | 女 | Woman | nǚ | 3 | 13 | 58 | 如 (67), 好 (82), 她 (91) |
| 14 | 火 | Fire | huǒ | 4 | 11 | 52 | 然 (55), 点 (128), 火 (433) |
| 15 | 日 | Sun | rì | 4 | 15 | 49 | 是 (3), 时 (25), 日 (101) |
| 16 | 宀 | Roof | mián | 3 | 21 | 46 | 家 (56), 定 (77), 实 (100) |
| 17 | 金 | Gold | jīn | 8 | 7 | 41 | 金 (260), 钱 (603), 错 (638) |
| 18 | 貝 | Shell | bèi | 7 | 9 | 41 | 资 (257), 质 (404), 费 (486) |
| 19 | 刀 | Knife | dāo | 2 | 19 | 39 | 到 (22), 分 (79), 前 (93) |
| 20 | 阜 | Mound | fù | 8 | 17 | 34 | 队 (268), 院 (338), 际 (423) |
| 21 | 目 | Eye | mù | 5 | 11 | 32 | 着 (41), 看 (76), 相 (152) |
| 22 | 玉 | Jade | yù | 5 | 6 | 32 | 现 (70), 理 (89), 王 (299) |
| 23 | 石 | Stone | shí | 5 | 4 | 31 | 确 (331), 石 (414), 研 (447) |
| 24 | 一 | One | yī | 1 | 20 | 30 | 一 (2), 不 (4), 来 (15) |
| 25 | 衣 | Clothes | yī | 6 | 6 | 29 | 被 (154), 表 (177), 装 (467) |
| 26 | 竹 | Bamboo | zhú | 6 | 9 | 28 | 第 (114), 等 (158), 管 (252) |
| 27 | 禾 | Grain | hé | 5 | 8 | 27 | 种 (57), 科 (277), 程 (314) |
| 28 | 大 | Big | dà | 3 | 11 | 27 | 大 (17), 天 (78), 关 (127) |
| 29 | 頁 | Leaf | yè | 9 | 10 | 27 | 题 (218), 领 (329), 须 (444) |
| 30 | 犬 | Dog | quǎn | 4 | 3 | 25 | 状 (624), 独 (627), 犯 (767) |
| 31 | 力 | Power | lì | 2 | 11 | 25 | 动 (73), 力 (106), 加 (166) |
| 32 | 虫 | Insect | chóng | 6 | 1 | 24 | 虽 (504), 融 (1225), 虫 (1287) |
| 33 | 广 | Dotted Cliff | guǎng | 3 | 9 | 24 | 应 (144), 度 (184), 府 (417) |
| 34 | 足 | Foot | zú | 7 | 5 | 22 | 路 (305), 足 (527), 跟 (541) |
| 35 | 巾 | Turban | jīn | 3 | 9 | 22 | 常 (187), 市 (254), 师 (333) |
| 36 | 尸 | Corpse | shī | 3 | 8 | 22 | 展 (275), 局 (483), 尽 (488) |
| 37 | 山 | Mountain | shān | 3 | 4 | 21 | 山 (259), 岁 (772), 岛 (798) |
| 38 | 車 | Cart | chē | 7 | 6 | 21 | 车 (361), 转 (376), 轻 (460) |
| 39 | 攴 | Rap | pū | 4 | 14 | 21 | 政 (150), 教 (191), 数 (231) |
| 40 | 又 | Again | yòu | 2 | 13 | 20 | 对 (33), 发 (47), 又 (126) |
| 41 | 馬 | Horse | mǎ | 10 | 2 | 19 | 马 (276), 验 (534), 驻 (1288) |
| 42 | 示 | Spirit | shì | 5 | 8 | 19 | 神 (227), 社 (270), 示 (425) |
| 43 | 八 | Eight | bā | 2 | 12 | 19 | 其 (85), 公 (115), 关 (127) |
| 44 | 彳 | Step | chì | 3 | 8 | 18 | 得 (39), 很 (138), 德 (256) |
| 45 | 田 | Field | tián | 5 | 8 | 18 | 由 (136), 电 (230), 界 (288) |
| 46 | 冫 | Ice | bīng | 2 | 7 | 18 | 决 (273), 准 (379), 况 (419) |
| 47 | 邑 | City | yì | 7 | 3 | 18 | 那 (38), 都 (68), 部 (84) |
| 48 | 疒 | Sickness | nè | 5 | 3 | 17 | 病 (427), 痛 (730), 疗 (949) |
| 49 | 門 | Gate | mén | 8 | 4 | 16 | 间 (135), 问 (137), 门 (185) |
| 50 | 穴 | Cave | xué | 5 | 4 | 16 | 空 (272), 究 (429), 突 (484) |

## What the ranking actually says

The top five radicals account for 24.1% of the 3,000 entries, counting a character under every radical Unihan lists it under. The top twenty account for 53.5%. The top fifty for 76.5%. Beyond that the curve flattens hard: you need eighty radicals to reach 88.3%.

Nine of the 214 have no characters in the top 3,000 at all. They are 韭 leek, 髟 hair, 鬥 fight, 鬯 sacrificial wine, 鬲 cauldron, 鹵 salt, 黹 embroidery, 黽 frog and 龠 flute. Three are easy to explain. 鬯 is sacrificial wine and 黹 is embroidery, and neither topic turns up in a modern corpus often enough to register. 鬥 is the case where simplified writing stopped using the radical at all: the word for "fight" is now written 斗, and 斗 is indexed under radical 68, not 191.

Two entries in the table are worth pointing at because their numbers look wrong until you check the rule. 糸 silk, ninth largest grouping in the 3,000, is almost entirely there because of a simplification: 纟 is what the radical looks like in simplified characters like 经, 给, 结, 红 and 级, and Unihan marks it with an apostrophe on the radical number. Sixty-three of the seventy characters under 糸 carry that apostrophe. 攴 rap is the same story from the other direction. The form it takes on the right-hand side of a character is 攵, which CC-CEDICT records as a variant of 攴, and the fourteen characters it covers in the top 1,000 are 政, 教, 数, 放, 改, 收, 整, 敌, 效, 故, 攻, 敢, 散 and 救 — all of them far more common than the character 攴 itself, which is not in the top 3,000 at all.

## The two lists disagree, and that is the interesting part

Ranking radicals by "how many of the 3,000 most frequent running-text characters" answers one question. Ranking by "how many of the 3,500 characters the Chinese education system says a literate adult needs" answers a different one, and I ran both.

The overall shape holds. Across the 205 radicals that occur in both lists, rank correlation is 0.98. Eighteen of the top twenty are the same twenty, and forty-seven of the top fifty.

The ones that move are the useful ones:

| Radical | in 3,000 (Jun Da) | in 3,499 (常用字表) | What it means |
|---|---|---|---|
| 虫 insect | 24 | 61 | Productive in the character list, rare character by character |
| 竹 bamboo | 28 | 46 | Objects named in writing that rarely come up in it |
| 刀 knife / 阜 mound | 39 / 34 | 44 / 36 | Fall out of the top twenty when the second list decides |
| 米 rice / 鳥 bird / 食 eat | 15 / 12 / 13 | 24 / 21 / 20 | Enter the top fifty on the second list |
| 示 spirit / 八 eight / 邑 city | 19 / 19 / 18 | 18 / 17 / 16 | Fall out of the top fifty as those three come in |

虫 is the clearest case in the whole dataset. Sixty-one of the 3,499 official characters sit under it — dragonflies, shrimps, snails, moths, a long list of creatures most people recognise and rarely write. Only twenty-four of those sixty-one clear the top 3,000 by frequency. If you are building a memory deck from a list of radicals, 虫 looks important; if you are building one from a corpus, it is a rounding error. Both numbers are correct.

## How the numbers were produced

The whole thing is one Python script over a handful of files, and the files are the part you have to pin down, because a radical count is only as stable as the radical assignment behind it.

**Radical assignment.** Unihan's `kRSUnicode` gives, per character, a value like `85.5` — radical 85, five residual strokes. Some values carry apostrophes (`120'.3`), which per [UAX #38 revision 40](https://www.unicode.org/reports/tr38/tr38-40.html), dated 2026-04-23, mark a simplified form of the radical. Some characters have more than one value, space-separated; UAX #38 says this is deliberate, and exists "where there is sufficient ambiguity that a reasonable person might look for an ideograph in multiple places". I counted such a character under every radical it lists.

**The character universe.** Jun Da's list is ordered by frequency; I took the first 1,000 and the first 3,000 entries. Its raw-frequency column sums to 193,504,018, which I recomputed from the file rather than reading off the page. All 3,000 characters have a `kRSUnicode` value; nothing had to be dropped. The second list is Jun Da's copy of 《现代汉语常用字表》, which parses to 3,499 characters rather than 3,500 — his own note on the page says the segmentation step failed on one character, 啰 — so the column headed "in 3,499" is a count against 3,499, not a typo.

**Stroke counts.** I took them from `kTotalStrokes` on the unified ideograph that each Kangxi radical character is equivalent to — U+2F27 KANGXI RADICAL ROOF is equivalent to U+5B80. UAX #38 says this equivalence is intended specifically so that `kRSUnicode` and `kTotalStrokes` can be derived for the radical characters, which is what I did.

**Names and readings.** From the Unicode character names (KANGXI RADICAL MOUTH, KANGXI RADICAL DOTTED CLIFF) and from `kMandarin`. I started with [CC-CEDICT](https://www.mdbg.net/chinese/export/cedict/cedict_1_0_ts_utf-8_mdbg.txt.gz) — the snapshot I pulled is dated 2026-10-08T08:19:21Z and holds 125,218 entries — and dropped it, because its first entry for 水 is "surname Shuǐ" and its first entry for 足 is jù, "excessive". Both are real readings. Neither is the radical's reading.

## Where these numbers are soft

**Multi-radical characters get counted twice.** 38 of the top 1,000 and 77 of the top 3,000 have more than one `kRSUnicode` value, so the counts add up to slightly more than the number of characters in the list. The tie-break only matters at the boundary: four radicals sit at sixteen characters, so the last two places in the table above are a convention rather than a measurement. I checked the other rule as well: if each character is assigned only to its first-listed radical, the top twenty does not change at all, and the top fifty changes by one radical under the same tie-break — 又 drops out and 米 comes in.

**Simplified and traditional characters are different data.** 346 of the top 3,000 characters carry an apostrophe on their radical number, marking a simplified radical shape. Separately, 267 of the top 3,000 have a traditional variant indexed under a different radical. 来 is `75.3` (木) but 來 is `9.6` (人). 关 is `12.4` (八) but 關 is `169.11` (門). 业 is `1.4` (一) but 業 is `75.9` (木). 头 is `37.2` (大) but 頭 is `181.7` (頁). A frequency list of simplified text and a radical index built for the Kangxi dictionary will not agree, and the disagreement is systematic rather than random. Only 13 characters are in both groups, so the two effects stack rather than overlap. That 267 is an upper bound, not a count of errors: for some of those pairs the traditional character is a different word, so the radical change reflects a different word rather than a different indexing decision.

**A radical is an index position, not a meaning.** The three examples I show for 木 include 来, whose traditional form is indexed under 人. 关 is counted under 八. 虽 is counted under 虫, and it means "although". 特 is counted under 牛, and it means "special" — the bull it once referred to is gone. 我, "I", is indexed under 戈, a dagger-axe. 前 is indexed under 刀. Anyone who tells you the radical tells you the meaning is telling you something true often enough to be useful and false often enough to be dangerous. This dataset counts index positions.

**One reading per radical.** `kMandarin` gives a single customary reading. 广 is guǎng here; CC-CEDICT's own entry for the character is yǎn, from "house on a cliff", and I did not settle which reading a radical table should show.

## What I could not check

- Whether the Ministry of Education's own radical standard would change the ranking. 《汉字部首表》 is published on [moe.gov.cn](https://www.moe.gov.cn/jyb_sjzl/ziliao/A19/201001/t20100115_75694.html) (page dated 2005-06-28) as a scanned PDF, and I did not OCR it, so I cannot say how its radical list differs from the Kangxi 214 or whether it would move anything in the table above. I used the Kangxi set because Unihan encodes it. Not checked.
- How the ranking behaves on traditional-character text. Jun Da's list is the modern (simplified) one; his [Classical Chinese list](https://lingua.mtsu.edu/chinese-computing/statistics/char/list.php?Which=CL) exists but I did not run it against the same pipeline. Unverified.
- Whether the 2004 corpus behind the frequency order still represents written Chinese in 2026. I have no second modern corpus to compare against, and the 0.98 rank correlation above is between two different character sets drawn from the same corpus, so it is a check on the character list, not on the corpus. Single source.
- Individual `kRSUnicode` assignments against any printed dictionary. I verified a handful by hand (来, 关, 虽, 业, 头, 特, 我) and left the rest as Unihan has them.

The script and the input files are small enough to rerun; the only thing that makes this table different from the other tables out there is that all of it is written down.
