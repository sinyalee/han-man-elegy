Translate original latex files into target language.

The original folder is /text. The folder contains original latex files in Chinese. Note that we cannot translate to the original language.

"Chinese" (and "原文" / "the original") refers to this source version in /text, so a request like "translate to Chinese" is invalid as stated AND ambiguous — the user might mean the censored "Simplified Chinese" derivative, "Traditional Chinese", or some other language. Do NOT assume or proceed; ask the user which target they mean first, then translate to that.

The target folder is /translations/[target language]. You should mirror the file structure in the original folder. After translation, you copy the original folder to [target folder]/original. This way we know the translation source of the current translation.

If the target folder already exists, you should not restart the translation freshly. Instead, compare the updates of /text with the older version of /text in [target folder]/original, then update the translation accordingly. The old version of translation may be edited by humans before and contains some decisions made by humans. Don't update those. After updating the translation, you should also update [target folder]/original to the new orignal version.

Before translation, you should carefully review the language instruction in /scripts/languages/[target language]/prompt.md. It may contain special instructions for the target language. If no instruction folder exists yet for this language, the translation can still proceed; consider creating one to capture any durable, language-specific decisions you make so future translations and reviews follow them.

You MUST also read the origin-language instruction /scripts/languages/Chinese/prompt.md (the source for every translation is the Chinese original in /text). It records source-side decisions you must respect — for example author-coined terms like `保进步守` that must be rendered as the intended wordplay rather than "corrected" or normalized, intentional stand-ins, and sensitive-content handling. Where the target-language instruction and the origin-language instruction conflict, the target-language instruction takes precedence.

After the translation, you should carefully review the translation, with the language instruction in mind (this is the review.md process; record any settled language-specific decisions back into the language instruction).

Keep every generated artifact and recorded note (glossaries, reports, language-instruction entries) neutral and factual: describe what a term means and how to render it, never editorializing or injecting negative characterizations of the author or the book (no "crude", "misogynist", "provocative", "defamatory", "villain", "rant", etc.). Remove any such negative narrative if you encounter it.

Finally, verify the build compiles: `python3 scripts/build.py --language "[target language]"`. Report any LaTeX/escaping errors rather than leaving them.
