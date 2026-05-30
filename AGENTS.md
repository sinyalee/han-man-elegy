# Instructions for AIs

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
* Get Release
    - Prompt: get_release.md
    - Aliases: get, show, show me, give me, fetch, download

A command often carries extra context that the prompt needs — for example a target language ("translate to English", "审查英文翻译"), a specific file, or a release version. Extract that context from the user's request and pass it along to the prompt so it can act on the right target.

## Language Usage

The root README.md and the original text in /text are in Chinese. Translated text are in respective languages. Everything else should be in English.

When talking with users, you should use the language that the user is using, except when referring to the specific text. For example, when a user gives you a command in Chinese: "审查英文翻译"，you should respond in Chinese, with quotes to original English text. This practice would allow users to translate to target languages they are not fully proficient in.

## Language versions

We would create In this project, "Chinese" means Mandarin Chinese with simplified characters by default. "Simplified Chinese" refers to Simplified Chinese for Mainland China.
