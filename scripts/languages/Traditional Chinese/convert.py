#!/usr/bin/env python3
r"""
convert.py - mechanically convert the Simplified-Chinese original (/text) toward
Traditional Chinese, using the three tables in tables/. It produces a *draft*: only
the conversions that are guaranteed safe are treated as final; everything else is a
RECOMMENDATION that a human/AI must review.

What is safe to apply silently:
  * A 1-character -> 1-option -> 1-character mapping (e.g. 这->這, 国->國, 软->軟).
    There is exactly one traditional form, so it cannot be wrong. (个 is NOT such a case:
    it is 个->個/箇, one-to-many, so it is flagged for review, not finalized.)

What is only a RECOMMENDATION (the script writes its best guess, but it MUST be reviewed
one by one, because context can flip the right answer):
  * One-to-many characters (干 -> 幹/乾/干): the script picks the most common form.
  * Phrases that resolve an ambiguous character (头发 -> 頭髮) - the phrase dictionary's
    word boundary may be wrong, e.g. "汕头|发财" must become 汕頭發財, not 汕頭髮財.
  * Regional vocabulary substitutions (宏 -> 巨集): the computer "macro" sense is wrong
    in 宏大. The book-specific choices live in 03_vocab_regional.csv's `chosen` column.

Outputs (under translations/Traditional Chinese/):
  converted/<file>.tex   the pristine script output - ALWAYS overwritten, never hand-edited.
  <file>.tex             the reviewed/working copy - seeded from the script output on first
                         run, then PRESERVED across re-runs so review edits are not lost
                         (use --force to reseed). The build reads these. `diff converted/ .`
                         shows exactly what the review changed.
  original/              snapshot of the /text revision this draft was made from.

The list of recommendations is printed to STDOUT (run with --recommendations for every
site); no report file is written. The reviewer edits ONLY the working .tex files - never
the tables or these scripts.

Usage:
    python3 convert.py                   # convert; preserve any existing working .tex
    python3 convert.py --force           # reseed the working .tex from the script output
    python3 convert.py --recommendations # also print every site to review, grouped by file
"""

import argparse
import csv
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TABLES = os.path.join(HERE, "tables")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
TEXT = os.path.join(ROOT, "text")
OUT = os.path.join(ROOT, "translations", "Traditional Chinese")
CONVERTED = os.path.join(OUT, "converted")


def load_map(path):
    """Load a sc,tc,ambiguous table -> {sc: (default, [candidates], ambiguous_bool)}."""
    m = {}
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            sc = row["sc"]
            cands = row["tc"].split()
            if sc and cands:
                m[sc] = (cands[0], cands, row.get("ambiguous", "") == "Y")
    return m


def load_regional(path):
    """Return (overrides, undecided):
       overrides = {general: chosen} for rows the author decided (chosen filled, != general)
       undecided = [general, ...] for rows still blank (setup incomplete)."""
    overrides, undecided = {}, []
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            general = row["general"].strip()
            chosen = row.get("chosen", "").strip()
            if chosen and chosen != general:
                overrides[general] = chosen
            elif not chosen:
                undecided.append(general)
    return overrides, undecided


def build_matcher(*maps):
    """Merge maps (later wins on key clash) into one greedy-longest-match dict."""
    D = {}
    for m in maps:
        D.update(m)
    maxlen = max((len(k) for k in D), default=1)
    firsts = {k[0] for k in D}
    return D, maxlen, firsts


def convert(s, D, maxlen, firsts, ambig_chars):
    """Greedy longest-match conversion. Returns (result, recs). The result is the best
    guess. recs lists sites that are NOT a safe 1->1 single character and so must be
    reviewed: each is (pos, src_segment, chosen_default, [candidates])."""
    out, recs = [], []
    i, n = 0, len(s)
    while i < n:
        c = s[i]
        if c not in firsts:                 # not the start of any key (ASCII, space, ...)
            out.append(c)
            i += 1
            continue
        hit = None
        for length in range(min(maxlen, n - i), 0, -1):
            seg = s[i:i + length]
            if seg in D:
                hit = (seg, D[seg])
                break
        if hit is None:
            out.append(c)
            i += 1
            continue
        seg, (default, cands, amb) = hit
        out.append(default)
        if len(seg) == 1:
            review = amb                                        # one-to-many character
        else:
            review = amb or any(ch in ambig_chars for ch in seg)  # phrase touching an ambiguity
        if review:
            recs.append((i, seg, default, cands))
        i += len(seg)
    return "".join(out), recs


def apply_overrides(s, overrides):
    """Greedy longest-match replacement of decided regional terms on traditional text.
    Returns (result, sites) where sites = [(pos_in_result, general, chosen), ...]."""
    if not overrides:
        return s, []
    keys = sorted(overrides, key=len, reverse=True)
    maxlen = len(keys[0])
    firsts = {k[0] for k in overrides}
    out, sites = [], []
    i, n, pos = 0, len(s), 0
    while i < n:
        c = s[i]
        if c not in firsts:
            out.append(c)
            pos += 1
            i += 1
            continue
        hit = None
        for length in range(min(maxlen, n - i), 0, -1):
            seg = s[i:i + length]
            if seg in overrides:
                hit = seg
                break
        if hit is None:
            out.append(c)
            pos += 1
            i += 1
            continue
        val = overrides[hit]
        sites.append((pos, hit, val))
        out.append(val)
        pos += len(val)
        i += len(hit)
    return "".join(out), sites


def convert_quotes(s):
    r"""Rewrite LaTeX quotes to Traditional-Chinese corner brackets, nesting-aware.
    ``...'' -> 「...」, an inner `...' -> 『...』 (alternating by depth). A single ' is
    treated as a closing bracket ONLY when a `-opened single quote is on the stack, so
    English apostrophes (Fisher's, Ruth's) and math primes ($p_i'$) are preserved."""
    out, stack = [], []   # stack items: 'D' for a ``..'' level, 'S' for a `..' level
    i, n = 0, len(s)
    while i < n:
        two = s[i:i + 2]
        if two == "``":
            out.append("「" if len(stack) % 2 == 0 else "『")
            stack.append("D")
            i += 2
        elif two == "''" and stack and stack[-1] == "D":
            stack.pop()
            out.append("」" if len(stack) % 2 == 0 else "』")
            i += 2
        elif s[i] == "`":
            out.append("「" if len(stack) % 2 == 0 else "『")
            stack.append("S")
            i += 1
        elif s[i] == "'" and stack and stack[-1] == "S":
            stack.pop()
            out.append("」" if len(stack) % 2 == 0 else "』")
            i += 1
        else:
            out.append(s[i])
            i += 1
    return "".join(out)


def line_of(text, pos):
    """1-based line number and the line's stripped content for a character offset."""
    line_no = text.count("\n", 0, pos) + 1
    start = text.rfind("\n", 0, pos) + 1
    end = text.find("\n", pos)
    line = text[start:end if end != -1 else len(text)].strip()
    return line_no, line


def snippet(line, width=58):
    line = line.replace("|", "\\|")
    return line if len(line) <= width else line[:width] + "…"


def main():
    ap = argparse.ArgumentParser(description="Convert /text (Simplified) toward Traditional Chinese.")
    ap.add_argument("--force", action="store_true",
                    help="reseed the working .tex from the script output (loses review edits)")
    ap.add_argument("--recommendations", action="store_true",
                    help="print every site to review, grouped by file")
    args = ap.parse_args()

    for t in ("01_characters.csv", "02_vocab_general.csv", "03_vocab_regional.csv"):
        if not os.path.isfile(os.path.join(TABLES, t)):
            sys.exit(f"error: missing table {t}. Run build_tables.py first.")

    chars = load_map(os.path.join(TABLES, "01_characters.csv"))
    general = load_map(os.path.join(TABLES, "02_vocab_general.csv"))
    overrides, undecided = load_regional(os.path.join(TABLES, "03_vocab_regional.csv"))
    D, maxlen, firsts = build_matcher(chars, general)            # phrases override single chars
    ambig_chars = {sc for sc, (_d, _c, amb) in chars.items() if amb and len(sc) == 1}

    tex_files = sorted(f for f in os.listdir(TEXT) if f.endswith(".tex"))
    os.makedirs(CONVERTED, exist_ok=True)
    os.makedirs(OUT, exist_ok=True)

    existing_main = [f for f in tex_files if os.path.isfile(os.path.join(OUT, f))]
    reseed = args.force or not existing_main

    char_recs, vocab_recs = {}, {}
    for name in tex_files:
        with open(os.path.join(TEXT, name), encoding="utf-8") as f:
            src = f.read()
        result, recs = convert(src, D, maxlen, firsts, ambig_chars)
        result, sites = apply_overrides(result, overrides)
        result_q = convert_quotes(result)

        with open(os.path.join(CONVERTED, name), "w", encoding="utf-8") as f:
            f.write(result_q)                                   # pristine script output (always)
        if reseed or not os.path.isfile(os.path.join(OUT, name)):
            with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
                f.write(result_q)                               # seed/refresh working copy

        # Line numbers are valid in both coordinate spaces because no pass (dict match,
        # override, quote rewrite) ever adds or removes a newline: char recs carry SOURCE
        # offsets, vocab sites carry CONVERTED-text offsets, and src/result have identical
        # line breaks. Preserve this invariant if you add a newline-affecting replacement.
        if recs:
            char_recs[name] = [(line_of(src, p), seg, dflt, cands) for p, seg, dflt, cands in recs]
        if sites:
            vocab_recs[name] = [(line_of(result, p), gen, val) for p, gen, val in sites]

    orig = os.path.join(OUT, "original")                        # source-revision snapshot
    if os.path.isdir(orig):
        shutil.rmtree(orig)
    shutil.copytree(TEXT, orig)

    report(tex_files, char_recs, vocab_recs, ambig_chars, chars,
           reseed, existing_main, undecided, args.recommendations)


def report(tex_files, char_recs, vocab_recs, ambig_chars, chars, reseed, existing_main,
           undecided, show_detail):
    n_char = sum(len(v) for v in char_recs.values())
    n_phrase = sum(1 for v in char_recs.values() for ln, seg, *_ in v if len(seg) > 1)
    n_single = n_char - n_phrase
    n_vocab = sum(len(v) for v in vocab_recs.values())

    print(f"Converted {len(tex_files)} file(s):")
    print(f"  translations/Traditional Chinese/converted/   pristine script output (always refreshed)")
    if reseed:
        print(f"  translations/Traditional Chinese/             working copy seeded from it")
    else:
        print(f"  translations/Traditional Chinese/             {len(existing_main)} working file(s) "
              f"PRESERVED (review kept); use --force to reseed")
    print()
    print("Only 1->1 single-character conversions are final. To review (best-guess applied):")
    print(f"  one-to-many characters     : {n_single}")
    print(f"  ambiguous-character phrases: {n_phrase}")
    print(f"  regional substitutions     : {n_vocab}")
    if undecided:
        print(f"  ! {len(undecided)} regional term(s) still undecided - fill `chosen` in "
              f"tables/03_vocab_regional.csv")
    if not show_detail:
        print("\nRun with --recommendations to list every site, grouped by file.")
        return

    print("\n" + "=" * 70)
    print("RECOMMENDATIONS - review each in the working file; fix where context disagrees.")
    print("=" * 70)
    for name in tex_files:
        crs, vrs = char_recs.get(name, []), vocab_recs.get(name, [])
        if not crs and not vrs:
            continue
        print(f"\n### {name}")
        singles = [(ln, seg, dflt, cands) for (ln, line), seg, dflt, cands in crs if len(seg) == 1]
        phrases = [((ln, line), seg, dflt, cands) for (ln, line), seg, dflt, cands in crs if len(seg) > 1]
        if singles:
            print("  one-to-many characters:")
            for ln, seg, dflt, cands in singles:
                print(f"    L{ln}: {seg} -> {dflt}   [alts: {' '.join(cands)}]")
        if phrases:
            print("  ambiguous-character phrases (verify the word boundary):")
            for (ln, line), seg, dflt, cands in phrases:
                amb = " ".join(f"{ch}:{'/'.join(chars[ch][1])}" for ch in seg if ch in ambig_chars)
                print(f"    L{ln}: {seg} -> {dflt}   [{amb}]   {snippet(line)}")
        if vrs:
            print("  regional substitutions:")
            for (ln, line), gen, val in vrs:
                print(f"    L{ln}: {gen} -> {val}   {snippet(line)}")


if __name__ == "__main__":
    main()
