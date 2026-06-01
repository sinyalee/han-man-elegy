Korean is a **translation** of the Chinese original in `/text`, into `/translations/Korean/` and built from there. Like the original (and unlike the censored "Simplified Chinese"), the Korean version is **uncensored** — keep every real name and real reference intact.

Use these rules together with the general processes in `/scripts/translate.md` and `/scripts/review.md`, and with the Translation Guide in `/scripts/languages/Translation Guide/` — its `prompt.md` (cross-language rules) and `glossary.md` (the per-term reference; its English column is only a *reference* for Korean — see the vocabulary policy below). Where this file conflicts with the Translation Guide, this file wins — except that author coinages must always be preserved as wordplay.

# Script & vocabulary policy

Korean is written in **Hangul**, but its vocabulary is heavily Sino-Korean, so for each term **first check whether a Korean word already exists** and use it, rather than calquing from the English in `glossary.md`:

* Use the native Sino-Korean equivalent where one exists: 人妻 → 유부녀 (有夫女), 家庭主婦 → 가정주부, 自由恋爱 → 자유연애, 处女 → 처녀, 计划生育 → 계획생육/산아제한, etc.
* **Cuckold vocabulary**: Korean has no "green hat" image — 绿帽/戴绿帽 → the idiom 오쟁이(를) 지다 ("to be cuckolded"); 苦主 → 오쟁이 진 남편 (the cuckolded husband). Explain the device rather than calquing the hat.
* **Author coinages**: render the device in Hangul and preserve the wordplay; a **Hanja gloss in parentheses on first use** can clarify a coined compound (e.g. 교수계(教授鷄) for 教授鸡), since Korean readers do not parse coined Hanja as readily as Japanese readers. Keep `glossary.md`'s explanation of each coinage.
* Korean keeps far fewer terms in Hanja than Japanese; default to Hangul and use Hanja only as a first-use gloss for clarity. Fall back to the English-style approach only where Korean has no equivalent term.

# Names

* **Modern Chinese personal & place names**: transliterate into Hangul by Mandarin pronunciation per South Korea's 외래어 표기법 (e.g. 시진핑); the book's recurring names follow this — 리쑹젠 (李松坚), 링페이페이 (凌菲菲), 궈쥐양 (郭菊阳), 상하이 (上海), 산터우 (汕头).
* **Historical / classical figures** use the Sino-Korean reading in Hangul: 관우 (Guan Yu), 제갈량 (Zhuge Liang), 유비 (Liu Bei), 정성공 (Koxinga).
* **Western names** → Hangul per 외래어 표기법 (트럼프, 머스크, 괴테, 나폴레옹). The author 李新野 → Hangul (이신예); the English edition uses "Sinya Lee".
* 潮汕 → the Sino-Korean form 조산 (Hanja 潮汕) — do NOT use "Teochew"; 潮汕话 → 조산 방언/차오저우어. See the Translation Guide.

# Title

Working title 「유부녀 데이트 가이드」 (keep 유부녀 = married woman; render "dating guide"). Settle one title and use it identically everywhere — `\bookname` in `config.tex`, in-text self-references, and the PDF filename.

# Sensitive / uncensored

Keep verbatim, do not soften: real political names and events (천량위 陈良宇, 장차오량 蒋超良, 6·4 천안문 사건 六四事件), the named real cases (쑤샹마오/자이신신, 팡마오/탄주, 둥즈민), and the **real phone numbers** doxxed in `chapter_how.tex`. State slogans use the established Korean rendering (공동부유 共同富裕, 중화민족의 위대한 부흥, 유온 維穩).

# Punctuation & build

* Use Korean orthography: Hangul with spacing between words (띄어쓰기); Western-style `. , ? !`; quotation marks 큰따옴표 “…”, 작은따옴표 ‘…’; work titles 《…》 or 「…」. Keep money figures in RMB (위안).
* Build: `python3 scripts/build.py --language "Korean"`, run from the project root. Run `python3 scripts/retarget_includes.py "translations/Korean/book.tex"` so its `\include` paths point at the Korean folder, not `/text` (otherwise the build silently compiles the Chinese original). The structural files (`package.tex`, labels, fonts) may need Korean localization, mirroring the English setup; report any LaTeX/font error rather than leaving it.

Record settled term decisions in `glossary.md` (or, for Korean-only conventions, here). Keep everything neutral and factual; never characterize the author or the book negatively.
