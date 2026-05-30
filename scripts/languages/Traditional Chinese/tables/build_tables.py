#!/usr/bin/env python3
r"""
build_tables.py - regenerate ../01_characters.csv from the OpenCC dictionary (Apache-2.0).

01_characters.csv is one row per simplified character -> its traditional candidate(s)
concatenated with no separator (each candidate is a single character, default first), with
ambiguous=Y when there is more than one. convert.py reads it; this is the ONLY generated table.

The two vocabulary tables beside it are hand-maintained and NOT touched here:
  ../02_vocab_stable.csv   words to keep as standard/mainland traditional (比特币->比特幣).
  ../03_vocab_change.csv   words to change to another TC form (软件->軟體).

The OpenCC source (STCharacters) is cached here as _raw_STCharacters.txt.

Usage:
    python3 build_tables.py            # download STCharacters from OpenCC, rebuild ../01
    python3 build_tables.py --offline  # rebuild from the cached _raw_STCharacters.txt
"""

import argparse
import csv
import os
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))   # .../Traditional Chinese/tables
ROOT = os.path.dirname(HERE)                         # .../Traditional Chinese (where CSVs live)

OPENCC = "https://raw.githubusercontent.com/BYVoid/OpenCC/master/data/dictionary"
SOURCE = "STCharacters"   # the only trusted-source file we still pull


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


def build_chars(text):
    """sc, tc (single-character candidates concatenated, default first), ambiguous (Y if >1)."""
    rows = []
    for key, cands in parse(text):
        rows.append([key, "".join(cands), "Y" if len(cands) > 1 else ""])
    return rows


def main():
    ap = argparse.ArgumentParser(description="Rebuild ../01_characters.csv from OpenCC.")
    ap.add_argument("--offline", action="store_true", help="reuse cached _raw_STCharacters.txt")
    args = ap.parse_args()

    print("Fetching trusted-source dictionary (OpenCC STCharacters, Apache-2.0)...")
    raw = fetch(SOURCE, args.offline)

    rows = build_chars(raw)
    out = os.path.join(ROOT, "01_characters.csv")
    with open(out, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["sc", "tc", "ambiguous"])
        w.writerows(rows)
    print(f"  wrote {os.path.relpath(out, HERE)}  ({len(rows)} rows)")
    print("Done. The hand-maintained 02_vocab_stable.csv / 03_vocab_change.csv were not touched.")


if __name__ == "__main__":
    main()
