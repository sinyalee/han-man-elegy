Japanese is a **translation** of the Chinese original in `/text`, into `/translations/Japanese/` and built from there. Like the original (and unlike the censored "Simplified Chinese"), the Japanese version is **uncensored** — keep every real name and real reference intact.

Use these rules together with the general processes in `/scripts/translate.md` and `/scripts/review.md`, and with the Translation Guide in `/scripts/languages/Translation Guide/` — its `prompt.md` (cross-language rules) and `glossary.md` (the per-term reference; its English column is only a *reference* for Japanese — see the kanji policy below). Where this file conflicts with the Translation Guide, this file wins — except that author coinages must always be preserved as wordplay.

# Script & kanji policy

Japanese readers parse Sino-Japanese compounds and coined kanji, so **keep the Chinese-character (kanji) form wherever it stays intelligible** instead of routing through the English rendering in `glossary.md`. Add furigana or a short parenthetical gloss on first use where a compound is unfamiliar.

* **Convert simplified characters to Japanese shinjitai**: 绿→緑, 战→戦, 龟→亀, 权→権, 奋斗→奮闘, 鸡→鶏, 龙→龍, 师→師, 团→団, 复→復/複, etc. Use the Japanese kanji form throughout.
* **Many terms are already Japanese** — use the native word directly: 人妻 (ひとづま hitozuma), 家庭主婦/専業主婦, 自由恋愛, 処女, etc.
* **Cuckold vocabulary maps onto Japanese NTR culture** — use the established Japanese terms: 绿帽/戴绿帽 → 寝取られ (netorare / NTR); 苦主 → 寝取られた夫 (the cuckolded husband); 黄毛 → 寝取り男 / 間男. This is the genre the book's premise borrows from.
* **Author coinages — keep the kanji device** and preserve the wordplay (gloss on first use): 铁绿帽法 → 鉄緑帽法, 教授鸡 → 教授鶏, 奋斗鸡 → 奮闘鶏, 奋斗嫖客 → 奮闘嫖客, 猪精 → 猪精, 狐狸精 → 狐狸精 — **keep the 精 suffix**: it is the author's parallel animal-demon coinage, and Japanese readers parse 〜精 as a Chinese-style animal 妖怪 (cf. 猪八戒, the 妖怪 of 西遊記). Gloss the demonic sense (妖怪・物の怪) on first use, and **avoid 妖精** (which means "fairy" in Japanese — a false friend). 妖狐 (yōko) is a natural alternative for 狐狸精 alone, but it has no parallel for the pig (no 妖豚) and breaks the 猪精/狐狸精 pairing, so prefer keeping 精. Keep `glossary.md`'s explanation of each coinage's construction.
* Fall back to the English-style rendering only when the kanji would not read naturally in Japanese.

# Names

* **Chinese personal & place names**: write in kanji (shinjitai) with the Japanese on'yomi reading (furigana on first use), per standard Japanese convention — 李松堅, 凌菲菲, 郭菊陽, 上海, 汕頭. Historical figures use their established Japanese forms: 関羽 (関帝), 諸葛亮, 劉備, 鄭成功 (ていせいこう Tei Seikō — use this for the book's plain tactical reference; the "Koxinga" epithet itself is Japanese 国姓爺 こくせんや Kokusen'ya, famous from Chikamatsu's play 『国性爺合戦』, but that carries a legendary/theatrical register). The author 李新野 stays in kanji (the English edition uses "Sinya Lee").
* **Japanese figures/terms** keep their Japanese forms; **Western names** → katakana (トランプ, マスク, ゲーテ, ナポレオン).
* 潮汕 stays in kanji 潮汕 (do NOT use "Teochew"); 潮汕话 → 潮州語/潮汕語. See the Translation Guide.

# Title

Working title 「人妻デートガイド」 (keep 人妻; render "dating guide"). Settle one title and use it identically everywhere — `\bookname` in `config.tex`, in-text self-references, and the PDF filename.

# Sensitive / uncensored

Keep verbatim, do not soften: real political names and events (陳良宇, 蒋超良, 六四事件), the named real cases (蘇享茂/翟欣欣, 胖猫/譚竹, 董志民), and the **real phone numbers** doxxed in `chapter_how.tex`. State slogans use the established Japanese rendering (共同富裕, 中華民族の偉大なる復興, 維穏).

# Punctuation & build

* Use Japanese punctuation: 。、「…」『…』; full-width as normal for Japanese typesetting. Keep money figures in RMB (人民元).
* Build: `python3 scripts/build.py --language "Japanese"`, run from the project root. Run `python3 scripts/retarget_includes.py "translations/Japanese/book.tex"` so its `\include` paths point at the Japanese folder, not `/text` (otherwise the build silently compiles the Chinese original). The structural files (`package.tex`, labels, fonts) may need Japanese localization, mirroring the English setup; report any LaTeX/font error rather than leaving it.

Record settled term decisions in `glossary.md` (or, for Japanese-only conventions, here). Keep everything neutral and factual; never characterize the author or the book negatively.
