Give the user a released PDF.

First read releases/README.md to understand the structure of the released PDF files. Then locate the release the user asked for:

* A translation / language version → `releases/languages/<language>.pdf`
* The original (uncensored) Chinese → `releases/languages/Chinese.pdf`
* A historic Simplified Chinese version → `releases/cn_versions/人妻约会指南v<version>.pdf`
* A historic English version → `releases/en_versions/<bookname>v<version>.pdf`
* The latest canonical (Simplified Chinese) version → `releases/人妻约会指南.pdf`
* The latest English version → `releases/<bookname>.pdf`

Only Simplified Chinese and English have a top-level `releases/<name>.pdf` copy and a versioned archive (`cn_versions/`, `en_versions/`). Every other language — including the Chinese original — lives only under `releases/languages/`.

If the requested PDF exists, give it to the user — provide the path as a clickable link.

If it does not exist, ask the user whether they want to generate it. Generating a language version means running the commands in order:

1. Translate (translate.md) to produce /translations/<language>/, if it isn't there yet.
2. Release (release.md): `python3 scripts/build.py --release --language "<language>"`

Do not generate without confirming with the user first.
