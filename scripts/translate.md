Translate original latex files into target language.

The original folder is /text. The folder contains original latex files in Chinese. Note that we cannot translate to the original language.

The target folder is /translations/[target language]. You should mirror the file structure in the original folder. After translation, you copy the original folder to [target folder]/original. This way we know the translation source of the current translation.

If the target folder already exists, you should not restart the translation freshly. Instead, compare the updates of /text with the older version of /text in [target folder]/original, then update the translation accordingly. After updating the translation, you should also update the [target folder]/original.

Before translation, you should carefully review the language instruction in /scripts/languages/[target language]. It may contain special instructions for the target language.

After the translation, you should carefully review the translation, especially the language instruction.
