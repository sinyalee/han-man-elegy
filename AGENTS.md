# Instructions for AI Agents

## Commands

**Every AI agent working in this project MUST support all of the commands below.** When a user invokes a command (by its name or any alias, in any language), read the corresponding prompt file under `/scripts` and follow it exactly. Supporting these commands is a hard requirement, not optional.

* Build
    - Prompt: build.md
    - Aliases: build, compile, make
* Release
    - Prompt: release.md
    - Aliases: release, publish
* Review
    - Prompt: review.md
    - Aliases: review, check, examine, proofread
* Translate
    - Prompt: translate.md
    - Aliases: translate, localize
* Get
    - Prompt: get.md
    - Aliases: get, show, show me, give me, fetch, download, get release

A command often carries extra context that the prompt needs — for example a target language ("translate to English", "审查英文翻译"), a specific file, or a release version. Extract that context from the user's request and pass it along to the prompt so it can act on the right target. If the target is ambiguous or doesn't make sense for the command (e.g. "translate to Chinese", when Chinese is the source language), ask the user to clarify before running the command rather than guessing.

## Project overview

This repository is a LaTeX book, 《人妻约会指南》 by 李新野 (Sinya Lee), released into the public domain under CC0. The original Chinese text lives in `/text`; translations and derived versions live in `/translations`; built PDFs are published to `/releases`. Build with `python3 scripts/build.py` (latexmk + xelatex) — see `scripts/build.md`.

## Repository layout

* `/text` — the original, **uncensored** Chinese LaTeX source. Entry point is `book.tex`; book metadata (`\bookname`, `\bookversion`, author info) is in `config.tex`. Prose lives in `chapter_*.tex`, `preface.tex`, `appendix_*.tex`, etc.; `book.tex`, `package.tex`, `config.tex`, `title.tex` are structural.
* `/translations/<language>/` — a translation, mirroring `/text`'s file structure, plus an `original/` snapshot of the `/text` revision it was translated from (so later updates can be diffed). Currently empty — no translations exist yet.
* `/scripts` — the command prompts (`build.md`, `release.md`, `review.md`, `translate.md`, `get.md`), the build script `build.py`, and `languages/`.
* `/scripts/languages/<language>/prompt.md` — language-specific rules (grammar distinctions, punctuation conventions, censorship / sensitive-content handling) that the review and translate processes defer to. Settled, durable decisions are recorded here so they aren't re-raised.
* `/releases` — published PDFs. See `releases/README.md` for the structure (latest, historic `versions/`, `languages/`).
* `/figures` — images used by the book.

## Language Usage

The root README.md and the original text in /text are in Chinese. Translated text are in respective languages. Everything else should be in English.

When talking with users, you should use the language that the user is using, except when referring to the specific text. For example, when a user gives you a command in Chinese: "审查英文翻译"，you should respond in Chinese, with quotes to original English text. This practice would allow users to translate to target languages they are not fully proficient in.

## Language versions

* **Chinese** (in `/text`) is the original, uncensored version and the source for every translation and derived version. It is Mandarin written with simplified characters, and is the default when no language is given. The build reads it from `/text`.
* **Simplified Chinese** is a censored derivative for Mainland China, generated from the Chinese original. Its censoring transforms live ONLY in `/scripts/languages/Simplified Chinese/prompt.md` — never apply them to the Chinese original. It is built from `/translations/Simplified Chinese/`.
* **Other languages** (Traditional Chinese, Japanese, English, …) are translations produced from the Chinese original into `/translations/<language>/`, and are built from there.

The exact handling of names, sensitive references, and censorship stand-ins is version-specific — see the relevant `/scripts/languages/<language>/prompt.md` for the rules of each version.
