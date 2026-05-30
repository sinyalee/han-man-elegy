#!/usr/bin/env python3
r"""
convert.py - generate the "Simplified Chinese" version from the Chinese original
(/text) by applying the censorship substitutions in censor.csv.

Simplified Chinese is a censored derivative for Mainland China. It is character-for-
character identical to the original EXCEPT for a small, fixed set of substitutions that
keep specific sensitive references from tripping Beijing's automated filters (a named
senior official's given name swapped for a stand-in, a June-Fourth reference swapped for
a vague phrase). Unlike the Traditional-Chinese conversion, there is NO script change and
no wholesale rewrite -- the output equals /text with only the censor.csv rules applied.

  censor.csv   the only table (hand-maintained). Columns:
                 origin       the exact source string to replace (pin the FULL name /
                              phrase, never a bare shared character -- 良 alone occurs in
                              both 陈良宇 and 蒋超良 and elsewhere).
                 target       what it becomes (陈良宇 -> 陈ら宇, 六四事件 -> 几十年前).
                              Only the matched span is swapped; surrounding words stay,
                              so "六四事件之后" -> "几十年前之后".
                 occurrence   how many times `origin` appeared in /text at the last
                              human-reviewed baseline -- a checksum, NOT a setting.

The occurrence column is the review gate. Every run recounts each origin in /text:
  - count == occurrence  -> the rule applies to exactly the set already reviewed: PASS.
  - count != occurrence  -> the original gained or lost an occurrence since the baseline.
                            A new occurrence may sit in a context where the blanket swap
                            is wrong, or signal newly-added sensitive content nearby.
                            The run FAILS (exit 1) so a human reviews the changed sites,
                            then re-baselines with --update-counts.

This catches drift around KNOWN terms. It does NOT catch brand-new sensitive content with
no rule yet (a newly-named official, a fresh June-Fourth allusion) -- that is the review
pass in prompt.md: diff translations/Simplified Chinese/original against /text and read the
new spans for anything that needs a new rule. Sex and legal content is in scope and stays.

The censorship is encoded ENTIRELY in censor.csv so the derivative is reproducible and
auditable. The working .tex under translations/Simplified Chinese/ are generated artifacts
and are regenerated on every run -- do NOT hand-edit them; add a rule to censor.csv instead
(make the origin string long enough to be unique if the swap is context-specific).

Outputs (under translations/Simplified Chinese/):
  <file>.tex   /text mirror with censor.csv applied (regenerated every run).
  original/    snapshot of the /text revision this derivative was made from (for the
               review diff and incremental updates, per scripts/translate.md).

Usage:
    python3 convert.py                  # regenerate the derivative and check occurrences
    python3 convert.py --check          # check occurrences only; write nothing
    python3 convert.py --update-counts  # re-baseline censor.csv to the current counts
                                        #   (run only AFTER reviewing the changed sites)
"""

import argparse
import csv
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
TEXT = os.path.join(ROOT, "text")
OUT = os.path.join(ROOT, "translations", "Simplified Chinese")
CSV = os.path.join(HERE, "censor.csv")

OK, BAD = "✓", "✗"   # ✓ ✗


def load_rules(path):
    """Load censor.csv -> list of dicts {origin, target, occurrence}. Longest origin
    first, so a longer rule wins over a shorter one that is its prefix (六四事件 > 六四)."""
    rules = []
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            origin = (row.get("origin") or "").strip()
            target = (row.get("target") or "").strip()
            occ = (row.get("occurrence") or "").strip()
            if not origin:
                continue
            rules.append({"origin": origin, "target": target,
                          "occurrence": int(occ) if occ.isdigit() else 0})
    rules.sort(key=lambda r: len(r["origin"]), reverse=True)
    return rules


def censor(text, rules, counts):
    """Apply the rules to `text` in a single left-to-right pass (longest origin wins at
    each position, and a replacement is never re-scanned). Tally hits into `counts`."""
    out = []
    i, n = 0, len(text)
    while i < n:
        for r in rules:                       # rules are longest-first
            o = r["origin"]
            if text.startswith(o, i):
                out.append(r["target"])
                counts[o] += 1
                i += len(o)
                break
        else:
            out.append(text[i])
            i += 1
    return "".join(out)


def main():
    ap = argparse.ArgumentParser(
        description="Generate the censored Simplified Chinese derivative from /text.")
    ap.add_argument("--check", action="store_true",
                    help="verify occurrence counts only; do not write any output")
    ap.add_argument("--update-counts", action="store_true",
                    help="re-baseline censor.csv to the current counts (after review)")
    args = ap.parse_args()

    if not os.path.isfile(CSV):
        sys.exit(f"error: missing {CSV}")
    rules = load_rules(CSV)
    if not rules:
        sys.exit(f"error: no rules in {CSV}")

    tex_files = sorted(f for f in os.listdir(TEXT) if f.endswith(".tex"))
    counts = {r["origin"]: 0 for r in rules}

    write = not (args.check or args.update_counts)
    if write:
        os.makedirs(OUT, exist_ok=True)
    for name in tex_files:
        with open(os.path.join(TEXT, name), encoding="utf-8") as f:
            src = f.read()
        result = censor(src, rules, counts)
        if write:
            with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
                f.write(result)

    if write:
        orig = os.path.join(OUT, "original")               # source-revision snapshot
        if os.path.isdir(orig):
            shutil.rmtree(orig)
        shutil.copytree(TEXT, orig)

    if args.update_counts:
        update_counts(rules, counts)
        return

    report(rules, counts, tex_files, write)
    if any(counts[r["origin"]] != r["occurrence"] for r in rules):
        sys.exit(1)                                        # gate: force a review


def update_counts(rules, counts):
    """Rewrite censor.csv with the current occurrence counts (re-baseline)."""
    changed = [(r["origin"], r["occurrence"], counts[r["origin"]])
               for r in rules if r["occurrence"] != counts[r["origin"]]]
    by_origin = {r["origin"]: r for r in rules}
    rows = sorted(rules, key=lambda r: len(r["origin"]))   # restore a readable order
    with open(CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["origin", "target", "occurrence"])
        for r in rows:
            w.writerow([r["origin"], r["target"], counts[r["origin"]]])
    if changed:
        print("Re-baselined censor.csv:")
        for o, old, new in changed:
            print(f"  {o}: {old} -> {new}")
    else:
        print("censor.csv already matches the current counts; nothing changed.")


def report(rules, counts, tex_files, wrote):
    print(f"{'Censored' if wrote else 'Checked'} {len(tex_files)} file(s)"
          + (" into translations/Simplified Chinese/" if wrote else " (no output written)"))
    if wrote:
        print("  output regenerated from /text via censor.csv\n")
    else:
        print()
    bad = 0
    print(f"{len(rules)} rule(s) checked:")
    for r in sorted(rules, key=lambda r: len(r["origin"])):
        o = r["origin"]
        got, want = counts[o], r["occurrence"]
        mark = OK if got == want else BAD
        if got != want:
            bad += 1
        print(f"  {mark} {o} → {r['target']}\t{got}/{want}")
    if bad:
        print(f"\n{bad} rule(s) need review: the occurrence count changed since the last")
        print("baseline. Read every gained/lost occurrence in /text -- confirm the swap")
        print("still fits and no new sensitive content appeared nearby -- then re-baseline:")
        print("    python3 \"scripts/languages/Simplified Chinese/convert.py\" --update-counts")
        print("Also diff translations/Simplified Chinese/original against /text for NEW")
        print("sensitive content with no rule yet (see prompt.md).")


if __name__ == "__main__":
    main()
