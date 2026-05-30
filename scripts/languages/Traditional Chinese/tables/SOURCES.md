# Table sources

`01_characters.csv` is the only generated table. `build_tables.py` (this folder) builds it from
the OpenCC dictionary (<https://github.com/BYVoid/OpenCC>, `data/dictionary/STCharacters.txt`,
Apache-2.0): one row per simplified character → its traditional candidate(s) concatenated with
no separator (each is a single character, default first), `ambiguous=Y` when there is more than
one. The source is cached here as `_raw_STCharacters.txt`.

The two vocabulary tables are hand-maintained (`sc,chosen`) and are **not** generated:
`../02_vocab_stable.csv` (words to keep, e.g. 比特币→比特幣) and `../03_vocab_change.csv`
(words to change, e.g. 软件→軟體).

## Refresh

```sh
python3 build_tables.py            # re-download STCharacters and rebuild ../01
python3 build_tables.py --offline  # rebuild from the cached _raw_STCharacters.txt
```

This overwrites `../01_characters.csv` only; the vocabulary tables are left untouched.
