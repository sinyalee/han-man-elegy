Translate original latex files into target language.

The original folder is /text. The folder contains original latex files in Chinese. Note that we cannot translate to the original language.

"Chinese" (and "原文" / "the original") refers to this source version in /text, so a request like "translate to Chinese" is invalid as stated AND ambiguous — the user might mean the censored "Simplified Chinese" derivative, "Traditional Chinese", or some other language. Do NOT assume or proceed; ask the user which target they mean first, then translate to that.

The target folder is /translations/[target language]. You should mirror the file structure in the original folder. After translation, you copy the original folder to [target folder]/original. This way we know the translation source of the current translation. Do this copy as the **final** step, only once the translation is complete, so the snapshot records exactly the revision the translation reflects (see the lockstep rule under incremental updates below).

`book.tex` is the structural entry point and is copied verbatim from /text, where its `\input`/`\include` paths point at `text/...`. The build always runs from the repo root, so a translation's `book.tex` must point at its OWN folder instead — otherwise it pulls in the original /text files (the build will appear to "succeed" but actually compile the source language). You MUST therefore run the retarget script on the target `book.tex` **every time you create or update a translation** — it is idempotent and leaves `\includegraphics{figures/...}` alone, so running it again when it is already correct is harmless:

    python3 scripts/retarget_includes.py "translations/[target language]/book.tex"

Run it as the last step before building, on a fresh translation and on every incremental update alike (in particular whenever `book.tex` was (re)written from /text — e.g. by `convert.py`'s seed/`--force`/`--update`, or by copying it over by hand). When in doubt, just run it: being idempotent, the only thing it can do is fix a wrong path.

If the target folder already exists, you should not restart the translation freshly. Instead, compare the updates of /text with the older version of /text in [target folder]/original, then update the translation accordingly. The old version of translation may be edited by humans before and contains some decisions made by humans. Don't update those. After updating the translation, you should also update [target folder]/original to the new original version.

**Critical — keep `[target]/original` in lockstep with the translation; never let the snapshot run ahead of it.** `[target]/original` is a promise: "every line of `/text` at this revision is faithfully reflected in the translation." The next update trusts that promise — it diffs `/text` against the snapshot and re-translates *only* the differences. So an incremental update MUST happen in this order:

1. **Diff first.** Compare `/text` against `[target]/original` and collect every changed / added / removed span (per file). Do this *before* touching the snapshot.
2. **Translate every span** into the working files (keeping prior human decisions on the unchanged lines).
3. **Snapshot last.** Only after step 2, copy the new `/text` into `[target]/original` — and only for the files you actually brought up to date.

Never refresh the snapshot first, in bulk, or "to be safe." If `[target]/original` is advanced to a revision whose changes are not yet translated, those changes become **invisible**: the next update diffs against the already-advanced snapshot, sees no difference, and silently skips them — no error, the edit is just lost. This is a real, observed failure mode (a snapshot once moved ahead of the translation, and a later update dropped a `\_\_`→explicit source rewrite). If you must defer translating a changed file, leave **that file's** snapshot at the OLD revision so the change resurfaces next time — do not advance it.

**Self-check before you finish:** `diff` each `/text` file against its `[target]/original` counterpart. The invariant is: a file's snapshot equals the current source **iff** that file's translation already reflects that source revision. A file you retranslated should now match `/text`; a file you did not retranslate must still show its old (un-advanced) snapshot — not the new source.

Before translation, you should carefully review the language instruction in /scripts/languages/[target language]/prompt.md. It may contain special instructions for the target language. If no instruction folder exists yet for this language, the translation can still proceed; consider creating one to capture any durable, language-specific decisions you make so future translations and reviews follow them.

You MUST also read /scripts/languages/Translation Guide/prompt.md (the source for every translation is the Chinese original in /text). It holds source-text background every translation needs — real public figures, recurring characters, author-coined terms like `保进步守` that must be rendered as the intended wordplay rather than "corrected" or normalized, sensitive references, and easily-mistaken facts. Where the target-language instruction and the Translation Guide conflict, the target-language instruction takes precedence — except that author coinages must always be preserved as wordplay.

After the translation, you should carefully review the translation, with the language instruction in mind (this is the review.md process; record any settled language-specific decisions back into the language instruction).

Keep every generated artifact and recorded note (glossaries, reports, language-instruction entries) neutral and factual: describe what a term means and how to render it, never editorializing or injecting negative characterizations of the author or the book (no "crude", "misogynist", "provocative", "defamatory", "villain", "rant", etc.). Remove any such negative narrative if you encounter it.

Finally, verify the build compiles: `python3 scripts/build.py --language "[target language]"`. Report any LaTeX/escaping errors rather than leaving them.
