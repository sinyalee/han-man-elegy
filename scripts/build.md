Build the latex files and generate the PDF using the build.py script.

Run `python3 scripts/build.py` (use `python scripts/build.py` on Windows).

Pass the target language through to the script when the user asks for one:

* Default (no language) builds the Chinese original from /text:
  `python3 scripts/build.py`
* Any other language builds from /translations/<language>/:
  `python3 scripts/build.py --language "English"`

If the build fails, report the LaTeX/escaping error to the user rather than silently ignoring it.

## Building a translation: retarget its `book.tex` first

When building any non-Chinese language (i.e. from `/translations/<language>/`), first make sure that translation's `book.tex` points at its OWN folder, not at `text/`. A translation's `book.tex` is copied verbatim from `/text`, where the `\input`/`\include` paths read `text/...`; if they were never retargeted, the build runs from the repo root and silently compiles the **original** `/text` files instead — it "succeeds" but produces a wrong-language PDF (the bug is invisible unless you check the content). So before building a translation, run the idempotent retarget script (it only ever fixes wrong paths and leaves `\includegraphics{figures/...}` alone):

    python3 scripts/retarget_includes.py "translations/<language>/book.tex"

This is the same step `translate.md` requires after creating or updating a translation. Running it here too is cheap insurance — if the paths are already correct it changes nothing. The Chinese original in `/text` needs no retarget (its paths already point at `text/`).

## Do not run builds in parallel

Only one build (`build.py`) may run at a time — never start a second build, in any language, while one is still running. The script always runs latexmk from the repo root under a single fixed job name (`book`), so every invocation reads and writes the same shared paths: the `book.*` intermediates and `book.pdf` at the root, the named `<bookname>.pdf` copy, and (with `--release`) the files under `releases/`. It also cleans those intermediates before and after each run. Two concurrent builds therefore clobber each other's intermediates and outputs, producing corrupt or wrong-language PDFs and spurious failures.

When you need to build several languages (e.g. the original plus a translation), run them strictly **sequentially** — wait for each build to finish before starting the next.
