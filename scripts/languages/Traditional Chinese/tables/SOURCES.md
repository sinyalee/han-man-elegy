# Table sources

`01_characters.csv` is the only generated table. `build_tables.py` (this folder) builds it from
two OpenCC dictionaries (<https://github.com/BYVoid/OpenCC>, `data/dictionary/`, Apache-2.0),
cached here as `_raw_<name>.txt`:

* **`STCharacters.txt`** — the base: one row per simplified character → its traditional
  candidate(s) concatenated with no separator (each is a single character, default first),
  `ambiguous=Y` when there is more than one.
* **`TWVariants.txt`** — an overlay mapping each orthodox-traditional glyph to its more
  widely-used Taiwan variant (爲→為, 麪→麵, 牀→床, 羣→群, 衆→眾, 喫→吃, …). It is applied two ways:
  to the candidate **values** above (so 为→為 not 爲), and as extra **pass-through rows** for
  variant glyphs that are identical in simplified and so never had an STCharacters row
  (踊→踴, …). The `KEEP_STANDARD` set in `build_tables.py` is excluded from the overlay, so
  those stay in OpenCC-standard form (currently **着**, **裏**, **污**, **泄**, **檐**, **睾**, **棱**).

The two vocabulary tables are hand-maintained (`sc,chosen`) and are **not** generated:
`../02_vocab_stable.csv` (words to keep, e.g. 比特币→比特幣) and `../03_vocab_change.csv`
(words to change, e.g. 软件→軟體).

## Refresh

```sh
python3 build_tables.py            # re-download STCharacters + TWVariants and rebuild ../01
python3 build_tables.py --offline  # rebuild from the cached _raw_*.txt
```

This overwrites `../01_characters.csv` only; the vocabulary tables are left untouched.
