#!/usr/bin/env python3
r"""
build_tables.py - (re)generate the three SC->TC conversion tables from a TRUSTED
SOURCE (the OpenCC dictionary data, Apache-2.0) plus a scan of the book.

It produces, under tables/:
  01_characters.csv      Table 1 - single-character SC->TC map (OpenCC STCharacters).
                         Keeps one-to-many entries (e.g. 干 -> 幹 乾 干); the first
                         candidate is the default, the rest are alternatives the
                         converter flags for an AI/human to decide.
  02_vocab_general.csv   Table 2 - phrase-level SC->TC map (OpenCC STPhrases). This
                         is what disambiguates most one-to-many characters in
                         context (头发 -> 頭髮, 干净 -> 乾淨), so only genuinely
                         ambiguous leftovers reach the AI.
  03_vocab_regional.csv  Table 3 - regional vocabulary that differs across Taiwan /
                         Hong Kong / overseas Chinese (OpenCC TWPhrases), FILTERED to
                         terms that actually occur in /text. The `chosen` column is
                         left BLANK for the author to fill in per term.

Run this only to create or refresh the tables. The day-to-day translation is done
by convert.py, which reads these CSVs and needs no network.

Usage:
    python3 build_tables.py            # download from OpenCC, rebuild all three tables
    python3 build_tables.py --offline  # reuse cached tables/_raw_*.txt instead of downloading
"""

import argparse
import csv
import os
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
TABLES = os.path.join(HERE, "tables")
# Project root = scripts/languages/Traditional Chinese -> up three -> repo root
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
TEXT = os.path.join(ROOT, "text")

OPENCC = "https://raw.githubusercontent.com/BYVoid/OpenCC/master/data/dictionary"
# The trusted-source files we pull and what each feeds.
NEEDED = ["STCharacters", "STPhrases", "TWPhrases", "TSCharacters"]


def fetch(name, offline):
    """Return the raw text of an OpenCC dict file. By default DOWNLOAD a fresh copy (and
    refresh the local cache); with --offline, reuse the cache instead of the network."""
    cache = os.path.join(TABLES, f"_raw_{name}.txt")
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


def write_csv(path, header, rows):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    print(f"  wrote {os.path.relpath(path, HERE)}  ({len(rows)} rows)")


def build_chars(text):
    """Table 1: sc, tc (space-joined candidates, default first), ambiguous (Y if >1)."""
    rows = []
    for key, cands in parse(text):
        rows.append([key, " ".join(cands), "Y" if len(cands) > 1 else ""])
    return rows


def build_general(text):
    """Table 2: sc, tc (space-joined candidates), ambiguous (Y if >1)."""
    rows = []
    for key, cands in parse(text):
        rows.append([key, " ".join(cands), "Y" if len(cands) > 1 else ""])
    return rows


def t2s_map(ts_text):
    """Char-level Traditional->Simplified map (first candidate) to reverse TWPhrases
    keys (which are traditional) back to the simplified forms used in /text."""
    m = {}
    for key, cands in parse(ts_text):
        if len(key) == 1:
            m[key] = cands[0]
    return m


def read_text_corpus():
    """Concatenate every .tex file under /text (for occurrence counting)."""
    blobs = {}
    for name in sorted(os.listdir(TEXT)):
        if name.endswith(".tex"):
            with open(os.path.join(TEXT, name), encoding="utf-8") as f:
                blobs[name] = f.read()
    return blobs


def read_existing_chosen(path):
    """Preserve the author's hand-made decisions across a refresh: {sc: chosen}."""
    keep = {}
    if os.path.isfile(path):
        with open(path, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("chosen", "").strip():
                    keep[row["sc"]] = row["chosen"].strip()
    return keep


def build_regional(tw_text, ts_text, keep_chosen):
    """Table 3: scan the book for terms whose Taiwan form diverges from the general
    (HK / overseas) form. Columns: sc, general, taiwan, chosen, count, example.
    `chosen` is carried over from any existing table (by sc) so a refresh does NOT
    destroy the author's decisions; new terms get a blank `chosen`."""
    t2s = t2s_map(ts_text)
    corpus = read_text_corpus()
    rows = []
    for key, cands in parse(tw_text):                 # key = general traditional form
        simp = "".join(t2s.get(c, c) for c in key)    # -> simplified form used in /text
        count = sum(blob.count(simp) for blob in corpus.values())
        if count == 0:
            continue
        example = ""
        for blob in corpus.values():
            i = blob.find(simp)
            if i != -1:
                snippet = blob[max(0, i - 8):i + len(simp) + 8].replace("\n", " ")
                example = snippet.strip()
                break
        rows.append([simp, key, " ".join(cands), keep_chosen.get(simp, ""), count, example])
    rows.sort(key=lambda r: -r[4])                    # most frequent first
    return rows


def main():
    ap = argparse.ArgumentParser(description="Rebuild the SC->TC tables from OpenCC + a book scan.")
    ap.add_argument("--offline", action="store_true", help="reuse cached tables/_raw_*.txt")
    args = ap.parse_args()

    os.makedirs(TABLES, exist_ok=True)
    print("Fetching trusted-source dictionaries (OpenCC, Apache-2.0)...")
    raw = {name: fetch(name, args.offline) for name in NEEDED}

    print("Building tables...")
    write_csv(os.path.join(TABLES, "01_characters.csv"),
              ["sc", "tc", "ambiguous"], build_chars(raw["STCharacters"]))
    write_csv(os.path.join(TABLES, "02_vocab_general.csv"),
              ["sc", "tc", "ambiguous"], build_general(raw["STPhrases"]))
    p03 = os.path.join(TABLES, "03_vocab_regional.csv")
    keep_chosen = read_existing_chosen(p03)           # carry the author's decisions forward
    if keep_chosen:
        print(f"  preserving {len(keep_chosen)} existing `chosen` decision(s) in table 3")
    write_csv(p03, ["sc", "general", "taiwan", "chosen", "count", "example"],
              build_regional(raw["TWPhrases"], raw["TSCharacters"], keep_chosen))
    print("Done. Review 03_vocab_regional.csv and fill in any blank `chosen` cells.")


if __name__ == "__main__":
    main()
