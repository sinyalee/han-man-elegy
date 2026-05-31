#!/usr/bin/env python3
r"""
build_tables.py - regenerate ../01_characters.csv from the OpenCC dictionary (Apache-2.0).

01_characters.csv is one row per simplified character -> its traditional candidate(s)
concatenated with no separator (each candidate is a single character, default first), with
ambiguous=Y when there is more than one. convert.py reads it; this is the ONLY generated table.

Two OpenCC sources are combined:
  * STCharacters - simplified -> orthodox-traditional candidates (the base table).
  * TWVariants   - orthodox-traditional -> widely-used Taiwan glyph (an overlay). Applying it
                   makes the table yield the more widely-understood form (爲->為, 麪->麵, 牀->床,
                   羣->群, 衆->眾, ...) instead of the orthodox one. A small KEEP_STANDARD set is
                   excluded from the overlay so those stay in standard form (着, 裏, 污, 泄, 檐, 睾, 棱).
Both are cached here as _raw_<name>.txt.

The two vocabulary tables beside it are hand-maintained and NOT touched here:
  ../02_vocab_stable.csv   words to keep as standard/mainland traditional (比特币->比特幣).
  ../03_vocab_change.csv   words to change to another TC form (软件->軟體).

Usage:
    python3 build_tables.py            # download STCharacters + TWVariants from OpenCC, rebuild ../01
    python3 build_tables.py --offline  # rebuild from the cached _raw_*.txt
"""

import argparse
import csv
import os
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))   # .../Traditional Chinese/tables
ROOT = os.path.dirname(HERE)                         # .../Traditional Chinese (where CSVs live)

OPENCC = "https://raw.githubusercontent.com/BYVoid/OpenCC/master/data/dictionary"
SOURCE = "STCharacters"    # simplified -> traditional candidates (the base table)
VARIANTS = "TWVariants"    # orthodox-traditional -> widely-used Taiwan glyph (the overlay)

# Characters kept in the OpenCC-standard (orthodox) form instead of their Taiwan variant.
# Everything else in TWVariants is applied, so the table yields the more widely-understood
# glyph. These are settled exceptions, deliberately kept standard.
KEEP_STANDARD = {"着", "裏", "污", "泄", "檐", "睾", "棱"}


def fetch(name, offline):
    """Return the raw text of an OpenCC dict file. By default DOWNLOAD a fresh copy (and
    refresh the local cache); with --offline, reuse the cache instead of the network."""
    cache = os.path.join(HERE, f"_raw_{name}.txt")
    if offline:
        if not os.path.isfile(cache):
            sys.exit(f"error: --offline but cache missing: {cache} (run once online first)")
        with open(cache, encoding="utf-8") as f:
            return f.read()
    url = f"{OPENCC}/{name}.txt"
    print(f"  downloading {url}")
    with urllib.request.urlopen(url) as r:        # noqa: S310 (trusted host)
        data = r.read().decode("utf-8")
    with open(cache, "w", encoding="utf-8") as f:  # refresh the cache (for later --offline)
        f.write(data)
    return data


def parse(text):
    """Parse an OpenCC dict: 'key\\tval1 val2 ...' lines, skipping # comments.
    Yields (key, [values])."""
    for line in text.splitlines():
        line = line.rstrip("\n")
        if not line or line.startswith("#"):
            continue
        if "\t" not in line:
            continue
        key, vals = line.split("\t", 1)
        cands = vals.split()
        if key and cands:
            yield key, cands


def build_variant_map(text, exclude):
    """orthodox char -> widely-used Taiwan glyph, from TWVariants (first candidate), minus
    the KEEP_STANDARD exceptions."""
    return {k: cands[0] for k, cands in parse(text) if k not in exclude}


def build_chars(text, vmap):
    """sc, tc (single-character candidates concatenated, default first), ambiguous (Y if >1).
    Each traditional candidate is mapped through vmap to its widely-used Taiwan glyph; the
    overlay can merge two candidates into one (吃: 喫吃 -> 吃), so candidates are de-duplicated
    in order and the ambiguous flag is recomputed on the result."""
    rows = []
    for key, cands in parse(text):
        mapped = [vmap.get(c, c) for c in cands]
        deduped = list(dict.fromkeys(mapped))   # preserve order, drop repeats
        rows.append([key, "".join(deduped), "Y" if len(deduped) > 1 else ""])
    return rows


def main():
    ap = argparse.ArgumentParser(description="Rebuild ../01_characters.csv from OpenCC.")
    ap.add_argument("--offline", action="store_true", help="reuse cached _raw_*.txt")
    args = ap.parse_args()

    print("Fetching trusted-source dictionaries (OpenCC STCharacters + TWVariants, Apache-2.0)...")
    raw = fetch(SOURCE, args.offline)
    variants = fetch(VARIANTS, args.offline)

    vmap = build_variant_map(variants, KEEP_STANDARD)
    rows = build_chars(raw, vmap)

    # An orthodox glyph can also reach the text as pass-through: the simplified source already
    # contains it (e.g. 踊 is identical in simplified and orthodox-traditional), so there is no
    # STCharacters row and convert.py would leave it unchanged. Add an explicit row for every
    # non-excluded TWVariants key so such chars are normalized to the widely-used form too
    # (踊->踴, ...). KEEP_STANDARD keys are absent from vmap, so 着/裏/污/泄/檐/睾/棱 pass through.
    have = {r[0] for r in rows}
    passthru = [[k, v, ""] for k, v in vmap.items() if k not in have]
    rows.extend(passthru)
    print(f"  + {len(passthru)} pass-through variant rows (踊->踴, ...)")
    out = os.path.join(ROOT, "01_characters.csv")
    with open(out, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["sc", "tc", "ambiguous"])
        w.writerows(rows)
    print(f"  wrote {os.path.relpath(out, HERE)}  ({len(rows)} rows)")
    print("Done. The hand-maintained 02_vocab_stable.csv / 03_vocab_change.csv were not touched.")


if __name__ == "__main__":
    main()
