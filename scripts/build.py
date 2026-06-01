r"""
build.py — full build script for the book (cross-platform: macOS / Linux / Windows).

It will:
  1. Locate the project root automatically (this script lives in scripts/, so the
     root is its parent directory).
  2. Pick the source by language: "Chinese" (the original, uncensored version) builds
     from text/; any other language builds from translations/<language>/ (where the
     translated or derived source lives — e.g. the censored "Simplified Chinese").
  3. Generate a temporary latexmkrc on the fly (deleted afterwards) and compile with
     latexmk + xelatex.
  4. Name the PDF after \bookname in the source's config.tex (fallback "book") and keep
     a copy at the project root. With --release, also publish copies under releases/.
  5. Be "self-contained" by default: clean intermediates before and after.

Publishing rules (only with --release, after a successful build):
  - always:                       releases/languages/<language>.pdf
  - Simplified Chinese & English: releases/<bookname>.pdf  (top-level canonical copy)
  - Simplified Chinese only:      releases/cn_versions/<bookname>v<bookversion>.pdf
  - English only:                 releases/en_versions/<bookname>v<bookversion>.pdf
  (The uncensored Chinese original and any other language get the languages/ copy only —
   no top-level copy and no versioned archive.)

Usage (can be run from any directory):
    python scripts/build.py                                 build Chinese, the original (from text/)
    python scripts/build.py --language "Simplified Chinese"  build the censored version (from translations/)
    python scripts/build.py --language Japanese              build from translations/Japanese/
    python scripts/build.py --release               build and also publish into releases/
    python scripts/build.py --keep                  keep intermediates, build incrementally
On Windows, if `python` is unavailable, try `py scripts/build.py`.
"""

import argparse
import glob
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata

# Project root = the parent of this script's directory (scripts/)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

JOB = "book"                       # latexmk job name -> intermediates are all book.*
DEFAULT_NAME = "book"              # fallback output name when \bookname is missing
DEFAULT_LANGUAGE = "Chinese"       # the original, uncensored version; builds from text/

# Canonical spellings used to normalize the --language value.
OFFICIAL_LANGUAGES = {
    "chinese": "Chinese",
    "simplified chinese": "Simplified Chinese",
    "traditional chinese": "Traditional Chinese",
    "japanese": "Japanese",
    "english": "English",
}

# ---- colors: only on an interactive terminal; on Windows try to enable ANSI ----
_color = sys.stdout.isatty()
if _color and platform.system() == "Windows":
    try:
        import ctypes
        h = ctypes.windll.kernel32.GetStdHandle(-11)          # STD_OUTPUT_HANDLE
        ctypes.windll.kernel32.SetConsoleMode(h, 7)           # ENABLE_VIRTUAL_TERMINAL_PROCESSING
    except Exception:
        _color = False


def _c(code):
    return code if _color else ""


GRN, YLW, RED, BLD, RST = (_c("\033[32m"), _c("\033[33m"), _c("\033[31m"),
                           _c("\033[1m"), _c("\033[0m"))


def info(msg):
    print(f"{GRN}==>{RST} {msg}")


def warn(msg):
    print(f"{YLW}warning:{RST} {msg}")


def err(msg):
    print(f"{RED}error:{RST} {msg}", file=sys.stderr)


def read_macro(config_path, macro):
    r"""Return the value of \newcommand{\<macro>}{...} in a LaTeX file, or None."""
    try:
        with open(config_path, encoding="utf-8") as f:
            pattern = r"\\newcommand\*?\s*\{\\" + re.escape(macro) + r"\}\s*\{(.+?)\}"
            m = re.search(pattern, f.read())
            return m.group(1).strip() if m else None
    except OSError:
        return None


def tex_install_help():
    name = platform.system()
    if name == "Darwin":
        print("  macOS: install MacTeX (full distribution, includes latexmk and all packages):")
        print("      brew install --cask mactex      # or download from https://www.tug.org/mactex/")
        print("    Smaller option, BasicTeX: brew install --cask basictex")
        print("      (then: sudo tlmgr install latexmk ctex ccicons algorithm2e diagbox titlesec)")
    elif name == "Linux":
        print("  Linux:")
        print("    - Debian/Ubuntu:  sudo apt-get install texlive-full latexmk")
        print("    - Fedora:         sudo dnf install texlive-scheme-full")
    elif name == "Windows":
        print("  Windows: MiKTeX is recommended (auto-installs missing packages): https://miktex.org/download")
        print("    or TeX Live: https://www.tug.org/texlive/ (both include latexmk)")
    else:
        print("  Install TeX Live from https://www.tug.org/texlive/ (includes latexmk).")


def make_latexmkrc():
    """Generate a temporary latexmkrc (deleted after use) so latexmk uses xelatex."""
    fd, path = tempfile.mkstemp(prefix="latexmkrc-", suffix=".pl")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write("# Auto-generated by scripts/build.py; removed after the build\n")
        f.write("$pdf_mode = 5;\n")                                    # 5 = xelatex
        f.write("$xelatex  = 'xelatex -interaction=nonstopmode %O %S';\n")
    return path


def clean(srcdir):
    """Remove intermediate files (leaves any .pdf in place)."""
    subprocess.run(["latexmk", "-c", f"{srcdir}/book.tex"],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for f in glob.glob(f"{srcdir}/*.aux"):     # .aux files \include creates in the source dir
        try:
            os.remove(f)
        except OSError:
            pass


def publish(src_pdf, dest):
    """Copy src_pdf to dest, creating parent dirs and overwriting any (read-only) existing file."""
    os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
    if os.path.exists(dest):
        try:
            os.remove(dest)
        except OSError:
            pass
    shutil.copyfile(src_pdf, dest)
    return dest


def _dwidth(s):
    """Display width counting CJK characters as 2 columns (for aligned output)."""
    return sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in s)


def print_summary(language, srcdir, bookname, version, produced):
    line = "-" * 64
    width = max(_dwidth(p) for p, _ in produced)
    print()
    print(f"{GRN}{line}{RST}")
    print(f"{BLD}  Build complete{RST}")
    print(f"  Language : {language}")
    print(f"  Source   : {srcdir}/")
    print(f"  Book     : {bookname}" + (f"   (version {version})" if version else ""))
    print("  Outputs  :")
    for path, label in produced:
        pad = " " * (width - _dwidth(path))
        print(f"    {path}{pad}   {label}")
    print(f"{GRN}{line}{RST}")


def main():
    parser = argparse.ArgumentParser(
        description="Build the book PDF with latexmk + xelatex, and publish to releases/.")
    parser.add_argument("--language", default=DEFAULT_LANGUAGE,
                        help='language to build (default "Chinese", the original, from text/); '
                             'other languages build from translations/<language>/')
    parser.add_argument("--release", action="store_true",
                        help="also publish copies into releases/ (by default only a local PDF is built)")
    parser.add_argument("--keep", action="store_true",
                        help="keep intermediate files and build incrementally (faster, for debugging)")
    args = parser.parse_args()

    os.chdir(ROOT)

    # Normalize the language: canonical spelling for the official ones, as-typed otherwise.
    lang_key = args.language.strip().lower()
    language = OFFICIAL_LANGUAGES.get(lang_key, args.language.strip())
    is_original = lang_key == DEFAULT_LANGUAGE.lower()   # "chinese" -> the original in text/

    srcdir = "text" if is_original else f"translations/{language}"
    main_tex = f"{srcdir}/book.tex"
    config_tex = f"{srcdir}/config.tex"

    if not os.path.isfile(main_tex):
        err(f"source not found: {main_tex}")
        if not is_original:
            print(f"  Put the {language} source under {srcdir}/ first "
                  f"(mirroring the text/ folder, including a config.tex).")
            if lang_key == "simplified chinese":
                print("  (Simplified Chinese is the censored version — generate it from the "
                      "Chinese original per scripts/languages/Simplified Chinese/prompt.md.)")
        sys.exit(1)

    missing = [t for t in ("latexmk", "xelatex") if shutil.which(t) is None]
    if missing:
        err("not found: " + ", ".join(missing))
        tex_install_help()
        sys.exit(1)

    bookname = read_macro(config_tex, "bookname")
    if not bookname:
        warn(rf"no \bookname found in {config_tex}; using '{DEFAULT_NAME}'. "
             rf"Please set \bookname in the source.")
        bookname = DEFAULT_NAME
    version = read_macro(config_tex, "bookversion")

    rc = make_latexmkrc()
    try:
        if not args.keep:
            info("Cleaning old intermediate files...")
            clean(srcdir)

        info(f"Building {BLD}{language}{RST} from {srcdir}/ (latexmk + xelatex)...")
        code = subprocess.run(["latexmk", "-r", rc, main_tex]).returncode
        if code != 0:
            err(f"build failed; {JOB}.log was kept for inspection. If a package is missing:")
            print("  - TeX Live / MacTeX:  sudo tlmgr install <package>")
            print("  - MiKTeX (Windows):   usually auto-installs, or use the MiKTeX Console")
            sys.exit(1)

        built = JOB + ".pdf"
        if not os.path.exists(built):
            err(f"build finished but {built} is missing.")
            sys.exit(1)

        # ---- local output (always) ----
        produced = []
        local_pdf = f"{bookname}.pdf"
        if local_pdf != built:
            shutil.copyfile(built, local_pdf)
        produced.append((local_pdf, "local build output (project root)"))

        # ---- publish to releases/ (opt-in via --release) ----
        if args.release:
            produced.append((publish(built, f"releases/languages/{language}.pdf"),
                             "by language"))
            # Only the censored Simplified Chinese (the canonical version) and English get
            # a top-level <bookname>.pdf and a versioned archive; the uncensored Chinese
            # original and any other language get the languages/ copy only.
            archive_dir = {
                "simplified chinese": "cn_versions",
                "english": "en_versions",
            }.get(lang_key)
            if archive_dir:
                produced.append((publish(built, f"releases/{bookname}.pdf"),
                                 "top-level release"))
                if version:
                    produced.append((publish(built, f"releases/{archive_dir}/{bookname}v{version}.pdf"),
                                     "version archive"))
                else:
                    warn(rf"no \bookversion in {config_tex}; skipping the releases/{archive_dir}/ copy.")

        if not args.keep:
            info("Cleaning intermediate files...")
            clean(srcdir)
            if local_pdf != built and os.path.exists(built):
                os.remove(built)        # drop the raw intermediate; keep the named output

        print_summary(language, srcdir, bookname, version, produced)
    finally:
        try:
            os.remove(rc)               # delete the temporary latexmkrc
        except OSError:
            pass


if __name__ == "__main__":
    main()
