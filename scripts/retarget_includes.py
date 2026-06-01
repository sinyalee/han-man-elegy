#!/usr/bin/env python3
r"""
retarget_includes.py - point a book.tex's \input / \include paths at its own folder.

book.tex is the structural entry point; it is copied verbatim into each language's
folder (text/ for the original, translations/<language>/ for every derivative). The
build always runs from the repo ROOT, so the paths inside book.tex must be ROOT-relative
and must point at the *same* folder book.tex lives in -- otherwise a translation's
book.tex would \include the original text/... files instead of its own.

This script rewrites every \input{...}/\include{...} in a given book.tex so its target
becomes "<dir-of-this-book.tex>/<basename>", where the directory is taken relative to
ROOT. Only the directory part changes; the basename is preserved. It is therefore
idempotent: running it again on an already-correct book.tex changes nothing.

\includegraphics is intentionally left untouched -- figures are referenced ROOT-relative
(figures/...) from the chapter files and must stay that way.

Usage (run once per translate, after the language's book.tex is in place):
    python3 scripts/retarget_includes.py "translations/Simplified Chinese/book.tex"
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# \input{...} or \include{...} (but NOT \includegraphics{...}: the brace must follow
# the command name directly, and "graphics" sits between "include" and "{").
_INCLUDE_RE = re.compile(r"(\\(?:input|include)\s*\{)([^}]*)\}")


def retarget(book_tex):
    """Rewrite book_tex's include/input paths to its own ROOT-relative folder.
    Returns True if the file changed."""
    book_tex = os.path.abspath(book_tex)
    if not os.path.isfile(book_tex):
        sys.exit(f"error: not a file: {book_tex}")

    # Directory prefix, relative to ROOT, with forward slashes (LaTeX path separator).
    prefix = os.path.relpath(os.path.dirname(book_tex), ROOT).replace(os.sep, "/")
    if prefix == ".":
        prefix = ""

    def repl(m):
        head, target = m.group(1), m.group(2)
        basename = target.rsplit("/", 1)[-1]                 # drop any existing dir
        new_target = f"{prefix}/{basename}" if prefix else basename
        return f"{head}{new_target}}}"

    with open(book_tex, encoding="utf-8") as f:
        src = f.read()
    out = _INCLUDE_RE.sub(repl, src)

    if out != src:
        with open(book_tex, "w", encoding="utf-8") as f:
            f.write(out)
        return True
    return False


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: python3 scripts/retarget_includes.py <path-to-book.tex>")
    book_tex = sys.argv[1]
    changed = retarget(book_tex)
    rel = os.path.relpath(os.path.abspath(book_tex), ROOT)
    print(f"{'retargeted' if changed else 'already current'}: {rel}")


if __name__ == "__main__":
    main()
