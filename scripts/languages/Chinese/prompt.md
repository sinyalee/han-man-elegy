This is the original, uncensored "Chinese" version, kept in /text. It is the source for all translations and for the censored "Simplified Chinese" derivative. The censorship transforms live ONLY in /scripts/languages/Simplified Chinese — do NOT apply them here. In the Chinese version, keep the real names and real references:

* Real names: "陈良宇", "蒋超良" (not the censored "陈ら宇" / "蒋超ら").
* Real references to sensitive events, e.g. "六四事件" (not the censored stand-in "几十年前").

# Review rules specific to Chinese

Use these together with the general process in /scripts/review.md.

## 的 / 地 / 得 — distinguish correctly throughout

* 的 = attributive, before a noun (美丽的花)
* 地 = adverbial, before a verb/adjective (狠狠地打、认真地回答)
* 得 = complement, after a verb/adjective (跑得快、搜集得差不多)

Fix 状语+的→地 and 动词+的+补语→得. Leave genuinely attributive 的 alone. This is a mechanical, unambiguous class — apply it as one global pass throughout, then sweep for missed cases (especially reduplicated adverb + 的: 狠狠的 / 慢慢的 / 认真的 / 仔仔细细的 + 动词).

## 权力 vs 权利

* 权利 = a right / entitlement someone holds (正当防卫权利、追求幸福的权利、没有权利干预)
* 权力 = authority or force to compel; institutional power, OR coercive leverage over a person (权力斗争、权力和资本勾结、获取诬告权力)

Decide once and apply consistently. In legal / rights passages it is almost always 权利. But coercive leverage is 权力, not 权利 — settled case: `获取诬告权力的控制行为` in chapter_sex is correct as 权力 (the power to control a man via the threat of a false accusation that can jail him, i.e. a force to compel). Do NOT "fix" it to 权利.

## 写到 / 写道 — by register (formal vs casual)

The author distinguishes the two by the register of what is being quoted:

* 写到 — for casual / personal writing being quoted (微信签名, blog posts, personal recollection). E.g. `微信签名写到：…`, `博客文章里面写到，…`, `我当时写到：…`.
* 写道 — for formal quotations (declarations, formal documents). E.g. `法国大革命的人权宣言写道``人生而自由''`.

Apply this distinction; do NOT blindly normalize one form to the other. Only flag a 写到/写道 if it is on the wrong side of this casual/formal line.

## Emphatic 是 + verb phrase — leave as-is

The author uses an affirmative/emphatic 是 before a verb phrase to assert a state, often with the trailing 的 dropped (e.g. `无论是撤退还是战斗，你都是做好准备`; cf. the parallel `都是非常有利的` in the same paragraph). Do NOT treat 是 + verb phrase as a 病句 (missing 了 / missing 的) and do NOT remove the 是 — keep it.

## Author-coined terms — leave intact (and flag for translators)

The author deliberately coins terms; do NOT "correct" them as 错别字 or 病句. Known coinages:

* `保进步守` — a deliberate wordplay splitting 保守 around 进步, contrasting 进步 (progress) with 保守 (retreating to tradition). Appears in chapter_how (`美国，基本没有保进步守的人`). Leave it untouched. Translators must render the wordplay (the 进步/保守 contrast), not normalize it to plain 保守.

When a review confirms a new author coinage, add it here so future reviews don't re-flag it and translators know to preserve the wordplay.

## 标点 conventions

* Chinese 破折号 is exactly two characters: —— (not ————).
* In-line lists use 顿号「、」between items, not commas.
* Quotation marks must pair correctly; the book body uses LaTeX ``…'' style — keep it consistent and never open with a closing mark (”…”). This is a settled, project-wide convention: convert any full-width curly quotes “…” to ``…'' as one mechanical global pass (glyph swap only — `“`→` `` `, `”`→`''`), preserving each quote's existing terminal-punctuation placement.
* A closing 句号 for a complete quoted sentence goes inside the closing quote; do not trap a 句号 inside 书名号《》 or inside a \hyperref link.
* Watch 全角/半角 mixing (e.g. a stray half-width space after 数字\%).

## Common 错别字 patterns

Homophone / near-form slips seen in this text: 做为→作为、活得→获得、防治→防止（非"防治疾病"语境）、即使→及时、抗→扛、帐户→账户、千万记→千万计、称为→成为、掌拓→掌跖、雄峰→雄蜂, and 他/她 指代错误. Duplicated particles: 的的、是是.

## Sensitive content

Frank sex and legal discussion are in-scope and fine. As the uncensored original, restore any garbled / censored sensitive terms to their true forms (see top). Still verify intent for anything that looks like a deliberate stand-in before changing it.
