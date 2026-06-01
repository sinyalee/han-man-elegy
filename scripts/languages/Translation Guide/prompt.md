# Translation Guide (applies to all translations)

Language-INDEPENDENT background and rules for translating the Chinese original in `/text`. Per `scripts/translate.md` and `scripts/review.md`, every translation reads this file. It is neutral and factual; it does not judge the author or the book.

The per-term reference — every figure, character, place, organization, work, author-coinage, and recurring word, with its meaning, etymology/wordplay, and a recommended rendering — lives in the consolidated **`glossary.md`** in this folder. This `prompt.md` holds the rules and conventions; `glossary.md` holds the terms. Per-language deviations and extra rules live in each `scripts/languages/<language>/prompt.md`; where a target-language instruction conflicts with this guide, the target-language instruction wins — except that author coinages must always be preserved as wordplay (below).

## The glossary is in English — using it by language family

`glossary.md`'s middle column is **English**: it is both the recommended English rendering and the settled choice for the English edition. How a translation should use it depends on the target language:

* **Non-East-Asian languages (European, etc.).** Follow the **English** standard. The English column already carries the meaning and preserves the wordplay without Chinese characters, so translate from that model — a fully-natural rendering in your language, no calques — using the Notes for nuance and each figure's established name.
* **Japanese.** Japanese readers parse Sino-Japanese compounds and coined kanji, so **keep the Chinese-character (kanji) form wherever it stays intelligible** instead of routing through the English. Many of the source's terms and the author's coined compounds carry straight over (converted to Japanese shinjitai, with furigana or a short gloss where helpful); some terms are already Japanese (e.g. 人妻 *hitozuma*, and the cuckold premise maps onto Japanese 寝取られ/NTR vocabulary). Fall back to the English-style approach only when the kanji would not read naturally. See `scripts/languages/Japanese/prompt.md`.
* **Korean.** Modern Korean is written in Hangul but its vocabulary is heavily Sino-Korean, so for each term **first check whether a Korean word already exists** (the native Sino-Korean equivalent, e.g. 人妻 → 유부녀) and use it; a Hanja gloss in parentheses can clarify a coinage on first use. Use the English-style approach only where Korean has no equivalent. Korean keeps far fewer terms in Hanja than Japanese. See `scripts/languages/Korean/prompt.md`.
* **Chinese derivatives (Traditional / Simplified Chinese).** Keep the Chinese as Chinese; see their own `prompt.md` files.

This is why the glossary's Notes give established East-Asian names/readings (e.g. 关羽 = Japanese 関羽, Korean 관우; 郑成功 = Koxinga): each per-language `prompt.md` records the settled choice for that language.

## Rendering conventions

* **Uncensored.** This is the uncensored book — keep every real name and real reference intact (real officials like 陈良宇 / 蒋超良, 六四事件, etc.). The censored "Simplified Chinese" derivative applies its own stand-ins via `scripts/languages/Simplified Chinese/prompt.md`; do not import those here.
* **Names of people.** Use each figure's established (non-pinyin) name where one exists — Taiwan/HK/overseas figures and anyone with a well-known foreign-language name (e.g. Koxinga, Kris Wu, Andrew Yao, Kelly Zong, Vincent Chiao); otherwise romanize per the target language's convention. The author's own name is **Sinya Lee** (not pinyin "Li Xinye"). See `glossary.md` for each name.
* **Parenthetical glosses — original characters, not pinyin.** When the translated text glosses a source title, coinage, or culture-bound term in parentheses, show the original Chinese characters — e.g. *Tales of Communist Officials* (《有官在身》), *Memorial on the Expedition* (《出师表》) — not a pinyin transliteration. Characters are precise and searchable; pinyin of a phrase is opaque to Chinese and non-Chinese readers alike. Keep romanization only where it is itself the established name/title (people's names; "Huangdi Neijing") or where the gloss exists to convey pronunciation (a loanword like *shikumen*).
* **潮汕 → "Teochew".** Render 潮汕 (region, people, and dialect alike) as "Teochew", NOT "Chaoshan", in every language **not** written with Chinese characters. The East-Asian exception: Chinese and Japanese keep 潮汕 in characters, and Korean uses its Sino-Korean form (조산 / Hanja 潮汕) — none of these use "Teochew". The sub-districts 潮阳 (Chaoyang) / 潮南 (Chaonan) and the cities 潮州 (Chaozhou) / 汕头 (Shantou) keep their own romanized names.
* **Author coinages — preserve the wordplay.** Do not normalize or "correct" deliberate coinages (e.g. 保进步守, 铁绿帽法, 奋斗鸡 / 奋斗嫖客, 教授鸡, 猪精 / 狐狸精, 女拳头子, 感觉人). `glossary.md` gives each coinage's construction and a suggested rendering.
* **Explicit, legal, and political content — render directly.** Frank sex and legal/political discussion are in-scope and expected; do not soften, euphemize, or editorialize. `glossary.md` has a dedicated "Explicit / sexual vocabulary" section.
* **Units & money.** Convert or gloss traditional units where helpful (斤 = 0.5 kg; 虚岁 = nominal age counting birth as 1); label money figures consistently as RMB.

## Recording decisions

When a review or translation settles a durable term rendering, record it in `glossary.md` (term-level); when it settles a cross-language convention, record it here. Keep every entry neutral and factual — describe what a term means and how to render it, never characterizing the author or the book negatively (no "crude", "misogynist", "provocative", "defamatory", "villain", "rant", etc.). If you find such negative narrative in an existing artifact, remove it.
