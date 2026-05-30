This is the **Simplified Chinese** version — a **censored derivative** of the Chinese
original in `/text`, for distribution in Mainland China. It is generated into
`/translations/Simplified Chinese/` and built from there
(`python3 scripts/build.py --language "Simplified Chinese"`). It is the canonical release
(`releases/<bookname>.pdf`); the uncensored original publishes as `Original.pdf`.

It is **identical to the Chinese original except for a small set of substitutions** that keep
specific sensitive references from tripping Beijing's automated filters. The original is
already Mandarin in simplified characters, so there is **no script conversion and no
rewrite** — only the substitutions are applied. These transforms live **only here**; never
apply them to `/text` (see `scripts/languages/Chinese/prompt.md`).

# The model — `convert.py` + `censor.csv`

The whole censorship is one hand-maintained table, `censor.csv`, columns `origin,target,
occurrence`:

* **`origin`** — the exact source string to replace. Include **enough surrounding context**
  that the rule matches only the place(s) it should; the same word elsewhere can take a
  different substitution (or none).
* **`target`** — what that span becomes (surrounding text outside `origin` is untouched).
* **`occurrence`** — how many times `origin` appeared in `/text` at the last human-reviewed
  baseline. A **checksum, not a setting.**

`convert.py` regenerates the derivative from `/text` (longest `origin` wins at each position;
a replacement is never re-scanned), then recounts each `origin`:

* **count == occurrence** → covers exactly the set already reviewed: **PASS** (`✓`).
* **count != occurrence** → the original gained or lost an occurrence; a new one may need a
  different swap or signal new sensitive content nearby. **The run FAILS (exit 1)** for review.

The censorship is encoded **entirely in `censor.csv`** so the derivative stays reproducible.
The working `.tex` are **generated artifacts, regenerated every run** — do **not** hand-edit
them; add or refine a `censor.csv` rule instead.

# Scope — censorship only, driven by edits to the original

This version exists **only to censor**, and it tracks the original — it is not a place to
re-review the book. Two rules keep the work bounded:

* **Do the language review on the original, not here.** Typos, grammar, punctuation, wording
  — all of that is reviewed in `/text` (see `scripts/review.md`,
  `scripts/languages/Chinese/prompt.md`). A wording fix belongs in `/text`, then regenerate.
  Do **not** run a separate language pass on this derivative; it mirrors the original verbatim
  apart from the substitutions.
* **Only re-examine what changed in the original.** The sensitive-content review has already
  been done on the current `/text`; the result is exactly the rules in `censor.csv`. Do
  **not** re-scan the whole book or re-raise passages already decided to keep (see "Settled"
  below). The only trigger for new censorship work is an **edit to `/text`**: when the
  original changes, review just the changed/new spans.

So the recurring loop is small: regenerate, and if anything drifted, look only at the new
edits — nothing else.

# Workflow

Run from the repo root; quote paths with spaces.

1. **Generate + check:**
   `python3 "scripts/languages/Simplified Chinese/convert.py"` (use `--check` to verify
   counts without writing). It writes the working `.tex`, refreshes `original/`, prints a
   per-rule `✓`/`✗` tally, and exits non-zero on any drift.
2. **If something drifted (`✗`) or the original was edited:** diff `/text` against
   `translations/Simplified Chinese/original/` and read **only the changed/new spans**.
   For each `✗` rule, confirm the swap still fits its occurrences. In the new spans, watch
   for content sensitive to Beijing that needs its own rule (criteria below). Then re-baseline:
   `convert.py --update-counts` (only **after** reviewing). Take the diff **before** re-running,
   since `convert.py` refreshes `original/` on every write.
3. **Build:** `python3 scripts/build.py --language "Simplified Chinese"`.

If nothing drifted and the original was not edited, you are done at step 1 — there is nothing
to review.

# What to censor (when new content appears)

Censor the content **most sensitive to Beijing**, and pin the full term with context in
`censor.csv`. The clearest examples — but not the only things to watch for — are:

* **June-Fourth / Tiananmen 1989 references** (any allusion or euphemism).
* **Named high-ranking Communist Party / state officials in a scandal or critical light.**

**Do not over-censor.** Sex and legal content are in scope and stay. The book's other loaded
references are commonly discussed in Mainland China and stay as written (background list in
`scripts/languages/Chinese/prompt.md` under "Sensitive references" — context, not a censor
list). When unsure whether new content rises to the level above, ask the user rather than
silently swapping or leaving it; record each settled decision as a `censor.csv` rule (or, if
it is a judgment principle, here under "Settled").

The substitutions are **deliberate stand-ins, not typos** — a wording review must not "fix"
them back, and must leave the author's own `\_\_` redactions untouched.

# Settled — do not re-raise

The current `/text` has been reviewed in full. Everything that needs censoring is already in
`censor.csv`. The following were considered and **deliberately kept** — do not flag them again
unless the surrounding original text is edited:

* The author's own social critique (e.g. system-as-prison / 劳改 metaphors) and rhetorical
  passages — these are the author's voice, not banned references.
* The mention of being detained by the cyber-police (`网警`) / a `公安二代` jab — kept.

Add to this list whenever a future review settles on keeping a new borderline passage, so it
is not re-examined every run.
