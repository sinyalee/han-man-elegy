English is a **translation** of the Chinese original in `/text`, built from `/translations/English/`. Like the Chinese original (and unlike the censored "Simplified Chinese"), the English version is **uncensored** — keep every real name and real reference intact. Use these rules together with the general processes in `/scripts/translate.md` and `/scripts/review.md`, and with the term reference in `/scripts/languages/English/glossary.md`. You MUST also respect the source-side decisions in `/scripts/languages/Chinese/prompt.md` (author-coined terms, intentional stand-ins). Where this file conflicts with the Chinese instruction, this file wins — except that author coinages must always be preserved as wordplay (see below).

# Settled conventions

## Title and names

* **Book title** `人妻约会指南` → **"The Married Woman Dating Guide"**. Use this exact title everywhere: `\bookname` in `config.tex`, the running self-references in the text, and the PDF filename. The author's name `李新野` → **"Sinya Lee"** (his established English name; not "Li Xinye").
* **Romanization**: pinyin without tone marks for mainland names/places that have no established English form (郭菊阳 → Guo Juyang, 李松坚 → Li Songjian, 张桂梅 → Zhang Guimei). Defer to `glossary.md` for the per-term decision and keep every recurring name/place/term rendered **identically** throughout — this is the #1 risk when files are translated in parallel.
* **Established names override pinyin.** For Taiwan / Hong Kong / overseas figures, and for anyone — or any institution or development — with a widely-used English or official name, use that form, never mainland pinyin: 焦恩俊 → Vincent Chiao, 吴亦凡 → Kris Wu, 刘强东 → Richard Liu, 宗馥莉 → Kelly Zong, 姚期智 → Andrew Yao (Andrew Chi-Chih Yao); 清华大学 → Tsinghua University, 中山大学 → Sun Yat-sen University, 香港科大 → HKUST; 星河湾 → Star River, 波托菲诺纯水岸 → OCT Portofino (檀宫 has no confident official English name — romanize as "Tan Gong", do not guess a brand). When unsure, verify the established name rather than defaulting to pinyin.

## Voice and register — fully natural English

Render the book in **idiomatic, direct English with no calques**. It is a frank, irreverent first-person memoir-and-manual; match that voice exactly. Do **not** soften, sanitize, euphemize, or censor — frank sexual, legal, and political content is in-scope and expected.

* The signature NTR/cuckold vocabulary is rendered in plain English, **not** literal calques:
    - `人妻` → "married woman" (never a loanword).
    - `黄毛` → "the other man" / "the young lover" (not "yellow-hair").
    - `苦主` → "the cuckolded husband" / "the husband" (the wronged party).
    - `绿帽` / `戴绿帽` → "cuckoldry" / "to be cuckolded" — **drop the "green hat" image.** e.g. the recurring slogan `住明园楼盘，享绿帽人生` → "Live in a Mingyuan property, live a cuckold's life." (translate it **identically** in `dedication.tex` and `appendix_mingyuan.tex` — it's a running gag); `绿帽楼盘` → "a cuckold property"; `明园元祖绿帽房` → "the original Mingyuan cuckold flat."
* Explicit sexual terms get equally direct English (操/干 → "fuck", 鸡 → "whore", 二手货 → "used goods", 内射/无套 → "come inside"/"bareback", etc.). See `glossary.md` → "Explicit / sexual vocabulary." Do not tone these down.

## Author-coined wordplay — preserve as English coinages

The author invents terms; render the **device**, do not normalize to plain language (this overrides the "natural English" rule, which governs only the standard vocabulary above). Settled renderings:

* `铁绿帽法` → **"the Iron Cuckold Law"**; keep the `\footnote` that explains the 满清铁帽子王 ("iron-cap prince") allusion (a title that can never be removed) so the pun survives.
* `保进步守` → a portmanteau of *progressive* + *conservative*, e.g. **"progresservatism" / "progresservatives"**, with a brief inline gloss on first use ("extreme conservatism dressed up as century-old progressivism"). Mirrors the author jamming 进步 into 保守.
* Epithets stay vivid: `猪精` → "the pig-demon", `狐狸精` → "the fox-spirit/vixen", `教授鸡` → "the professor-whore", `奋斗鸡` → "hustle-whore", `奋斗嫖客` → "hustle-john", `女拳头子` → "feminist ringleader" (note the 权/拳 "rights"/"fist" pun). Keep the extended animal-spirit metaphor in `appendix_articles.tex` (`给鸡当狗`, `畜生的畜生`, 鸡/鸭/牛马/猪精/狐狸精) coherent across the whole essay.

When a review settles a new coinage rendering, record it here and in `glossary.md`.

## Uncensored / sensitive content

This is the uncensored version. **Keep verbatim**, do not redact or soften:

* Real political names and events: `陈良宇` → Chen Liangyu, `蒋超良` → Jiang Chaoliang, `六四事件` → "the June Fourth Incident", `张桂梅` → Zhang Guimei, `杨笠` → Yang Li, and the named real cases (苏享茂/翟欣欣, 胖猫/谭竹, 董志民, 重庆姐弟坠亡案). Use official English for state slogans (`共同富裕` → "common prosperity", `中华民族的伟大复兴` → "the Great Rejuvenation of the Chinese Nation").
* Real-name accusations against `李松坚` / `凌菲菲` / `许洁` and the **real phone numbers** doxxed in `chapter_how.tex` — keep the digit strings exactly as printed. (Removing any of this would be censorship; that belongs only to derived censored versions, which English is not.)

## Coy redaction blanks — never fill them

The author uses `\_` / `\_\_` (escaped underscores) as deliberate self-censoring blanks for vulgar words (legal cover), e.g. `求我\_在她里面` (preface), `我和郭菊阳\_\_的时候` / `狠狠地打她的\_\_` (chapter_sex), `不能\_\_` (appendix_articles). **Preserve them as blanks** in the English — keep the same `\_` count, placed where the omitted word would sit in the English sentence. Do NOT guess the word.

# LaTeX integrity (translate text, preserve structure)

* Preserve every command, environment, and option: `\chapter`/`\section`/`\subsection` (incl. starred `\chapter*{作者简介}`), `\textbf`/`\textit` (keep emphasis on thesis sentences and the italic essay postscripts), `\footnote{...}` (translate the contents — many carry load-bearing definitions), `\begin{figure}[H]…\includegraphics…\caption{…}` (translate **only** `\caption`; leave `[H]`, `\centering`, width, and image paths untouched), `\begin{enumerate}`/`\item`.
* **Cross-reference labels are keys — never translate them.** Keep `\label{3faces}`, `\label{sister}`, and the `axiom`/`theorem`/`corollary` labels `a1`–`a4`, `t1`–`t2`, `c1`–`c2`, plus every `\ref{…}` / `\hyperref[…]{…}` that points at them. In `\hyperref[…]{…}` translate the **visible link text** but keep hardcoded refs like "附录A.3" → "Appendix A.3" (translate 附录, keep A.3/A.4).
* **Math is verbatim.** Leave `$…$` and `$$…$$` (e.g. `$$\int_{t}^{t+\delta}p_x\,dx$$`, `$\sum_{i=1}^n p_i$`, `$p_i$/$v_i$/$c_i$`) exactly; translate only the surrounding prose that names the variables.
* **`\begin{verbatim}` in `closing.tex`** (Project: Sirius / Author: Sinya / Date: 2023-02-21): keep byte-for-byte; do not translate or reflow.
* **Escapes:** keep `\%` on every percentage; watch for `&`, `#`, `_` (only the intentional `\_` blanks should appear). Balanced braces/environments.
* **Quotes:** the source uses the LaTeX `` ``…'' `` convention, which renders as correct English curly double quotes — **keep it** (do NOT convert to corner brackets). Nested single quotes use `` `…' ``. Watch the nested `` ``no means no''（`` `不要'就是`不要' ''） `` — render just `` ``no means no'' `` and drop the now-redundant Chinese gloss.
* **Redundant glosses:** where the source is `中文（English）` and the English already names the concept (anti-slut defense, mechanism design, utility, Castle Doctrine, PrEP/PEP, …), use the English term **once** and drop the parenthetical. Keep genuinely informative parentheticals.
* **Titles:** `《Work》` → italics `\textit{Work}` (e.g. `《了不起的盖茨比》` → `\textit{The Great Gatsby}`); the four appendix essay `《…》` titles double as their `\section{}` headers (without brackets).
* **Layout to preserve:** lone `\ ` (backslash-space) spacer paragraphs, `\\` breaks, the long `------…` rule lines separating each essay from its postscript, and bare blog URLs (`https://sinyalee.com/blog/?p=NNN`) — keep verbatim.

# Structural files (English localization)

Keep `\documentclass[…]{ctexbook}` (xelatex handles Latin fine and falls back gracefully for any stray CJK). Localize ctex's auto-generated Chinese labels to English (in `package.tex`, and re-set for the appendix in `book.tex`):

* `\renewcommand{\contentsname}{Contents}`, `\renewcommand{\figurename}{Figure}`, `\renewcommand{\tablename}{Table}`.
* `\ctexset{ chapter/name={Chapter\ ,}, chapter/number=\arabic{chapter} }`; after `\appendix`, re-set `chapter/name={Appendix\ ,}, chapter/number=\Alph{chapter}` so chapters read "Chapter 1…" and appendices "Appendix A/B".
* Theorem environments: `\newtheorem{axiom}{Axiom}`, `{theorem}{Theorem}`, `{corollary}{Corollary}`.
* `book.tex` must `\include{translations/English/…}` (paths resolve from the project root, where `build.py` runs latexmk — NOT relative to the main file).
* `config.tex` macro values: `\bookname` → "The Married Woman Dating Guide", `\authorname` → "Sinya Lee", `\bookdate` → "June 2026", `\bookversionstring` → "First Edition v1.6", `\authoraddress` → "Fifth Avenue, Manhattan, New York, USA"; leave `\bookversion`, email, homepage.
* `title.tex` literal lines: `本书纯属虚构，如果雷同实属巧合` → "This book is a work of fiction; any resemblance to real persons is purely coincidental"; `不设版权，请随意转发分享` → "No copyright — please share and redistribute freely" (keep `\cczero\;`).
* `dedication.tex`: translate the dedication to the father (李松坚, chairman of Shanghai Mingyuan Group); the centered `{\Large \it …}` slogan must read **identically** to the one in `appendix_mingyuan.tex` — "Live in a Mingyuan property, live a cuckold's life". Keep `\vspace*{\fill}`, `\noindent`, `\\`, `\begin{center}`.
* `author.tex`: `\chapter*{About the Author}` (starred/unnumbered). Bio facts: born 1991 in Shantou; graduated the Tsinghua "Yao Class", MIT, Brown; worked at Amazon, Facebook, Citadel Securities; founder & CEO of **Alpha Star Research** (阿尔法星研究, an AI quantitative-trading firm); best-known essay `\textit{My Father, Li Songjian}` (a.k.a. `\textit{Three Faces}`), linked via `\hyperref[3faces]{Appendix}`. Keep the `figures/author.jpg` figure block.

# Punctuation, numbers, currency

* Full-width Chinese punctuation → half-width English (`，。：；！？` → `, . : ; ! ?`); inline 顿号 `、` → comma (or "and" before the last item); 破折号 `——` → em dash `—`.
* Currency: keep the author's RMB figures, rendered in English number style ("60 million yuan", "500 million yuan", "300,000-yuan bride price"); do not convert to USD. Gloss non-metric units once: `200斤` → `200 jin ($\approx$100 kg)` — write `$\approx$`, **not** a literal `≈` (see *Build gotchas*). `虚岁` → "nominal age (xusui)".

# Build (and non-obvious gotchas)

`python3 scripts/build.py --language English`, run from the project root. Then confirm the PDF built and scan the log. Things that are easy to get wrong and cost real time:

* **`book.tex` include paths resolve from the project ROOT, not from `book.tex`'s own folder.** `build.py` runs `latexmk` from the repo root *without* `-cd`, so `\input`/`\include` are relative to the root. `book.tex` MUST use `\include{translations/English/chapter_why.tex}` (and `\input{translations/English/config.tex}`, etc.). If you copy the original's `\include{text/...}`, the build **silently compiles the original Chinese instead of the translation** — no error, wrong PDF. (This is exactly the latent bug in `translations/Traditional Chinese/book.tex`.) The English directory name has no space, which also keeps `\include` happy.
* **`\include{translations/English/package.tex}` lives in the preamble** (before `\begin{document}`), mirroring the original `book.tex`. It prints a harmless `LaTeX Warning: \include should only be used after \begin{document}` — leave it; packages load and the build succeeds.
* **The Latin text font (Latin Modern) is missing some exotic Unicode glyphs.** A literal `≈` (U+2248) yields a "Missing character" warning and a blank in the PDF — write `$\approx$` instead. (Accented Latin such as `Đông Kinh` renders fine.) If the log says "Missing character", grep the `.tex` for that glyph and swap in a math or ASCII equivalent, then rebuild.
* **Appendix section numbers are positional.** In `appendix_articles.tex` the four `\section`s are A.1–A.4 in source order; *My Father, Li Songjian* must remain 3rd (A.3) and *My Sister, Li Xinying* 4th (A.4) so `\hyperref[3faces]` / `\hyperref[sister]` and the hardcoded "Appendix A.3/A.4" link text resolve correctly.
* **Healthy output looks like:** ~140 pages; TOC reads "Contents / Chapter 1–7 / Appendix A–B"; no "Missing character", no "undefined reference" in the log. Report any LaTeX/escaping error rather than leaving it.
