Build the latex files and generate the PDF using the build.py script.

Run `python3 scripts/build.py` (use `python scripts/build.py` on Windows).

Pass the target language through to the script when the user asks for one:

* Default (no language) builds the Chinese original from /text:
  `python3 scripts/build.py`
* Any other language builds from /translations/<language>/:
  `python3 scripts/build.py --language "English"`

If the build fails, report the LaTeX/escaping error to the user rather than silently ignoring it.
