Carefully review the latex files. The review target is /text for the original, or /translations/[target language] for a translation. A request to review the "original", "原版", or "Chinese" all mean the source version in /text — these are unambiguous, so start the review directly on the right folder (no need to ask which one).

Before the review, read the language instruction in /scripts/languages/[target language] carefully. It holds the language-specific rules (grammar distinctions, punctuation conventions, sensitive-content handling) that this general process defers to.

When the review target is a translation (not the Chinese original), also read the origin-language instruction /scripts/languages/Chinese/prompt.md. It records source-side decisions the translation must preserve — author-coined terms like `保进步守`, intentional stand-ins, and sensitive-content handling — so you don't re-flag a faithful rendering of something deliberate in the source.

# Goal

Typos + light polish, plus the language-specific correctness rules. Do NOT change content, structure, argument, or the author's voice. By default present findings as a list and confirm before editing; only edit directly when asked.

# Process

## 1. Read everything

Read every prose file in full. For a large text, fan out parallel review agents, grouping files to balance size; each agent reads its files completely and returns findings as structured data. Structural/config files (book.tex, package.tex, config.tex, title.tex) are not prose — skim only.

## 2. What to check (every file)

- Typos / wrong characters (including homophones).
- Punctuation — see the language instruction for conventions (pair matching, dashes, list separators, full/half-width).
- LaTeX integrity: unescaped `%`, `&`, `_`, `#`; broken `\commands`; mismatched braces/environments. (Frank sexual and legal content is in-scope and expected — review it for language quality only, never flag it as content.)
- Light polish: 病句 / ungrammatical / clearly awkward / redundant phrasing. Be conservative; preserve the author's voice.
- The language-specific correctness rules from /scripts/languages/[language] (e.g. grammar-word distinctions).

## 3. Verify before editing

- For each candidate, quote the EXACT original snippet and the proposed fix.
- Confirm each exists verbatim in the source (grep) so edits are unique and safe.
- Run a supplementary sweep for commonly-missed instances of each pattern — parallel agents reliably catch the obvious cases but miss the long tail.
- Keep objective ERRORS separate from judgment-call POLISH.

## 4. Confirm with the user

- Present findings as a list grouped by file, errors vs polish. Confirm before applying — especially polish and judgment calls.
- Treat any mechanical, unambiguous class (defined in the language instruction) as a global pass the user opts into once, then apply it consistently throughout rather than ad-hoc.
- Watch for "nonsense typos" inside politically sensitive passages — they may be intentional stand-ins. Verify intent (per the language instruction) rather than normalizing blindly.

## 5. Record settled decisions in the language instruction

When a review resolves a recurring judgment call or chooses a convention (a grammar distinction, a punctuation rule, a term spelling, an intentional sensitive-content stand-in to leave alone), write it into `/scripts/languages/[target language]/prompt.md` so future reviews follow it instead of re-raising the same question. Only record durable, project-wide decisions — not one-off fixes. Phrase each as a rule the next reviewer can apply mechanically.

Keep everything you record (and every glossary or report you generate) neutral and factual — describe what a term means and how to render it, never editorializing or injecting negative characterizations of the author or the book (no "crude", "misogynist", "provocative", "defamatory", "villain", "rant", etc.). If you find such negative narrative in an existing artifact, remove it.

## 6. Verify the build

After edits, compile and confirm it builds with no LaTeX/escaping errors. Pass the language being reviewed to the build script:

* Original Chinese (/text): `python3 scripts/build.py`
* A translation (/translations/[target language]): `python3 scripts/build.py --language "[target language]"`
