Build the latex files, generate the PDF, and release it to /releases using the build.py script.

Run the build with the `--release` flag, which publishes the PDF copies into /releases/:

* Default (no language) releases the Chinese original from /text:
  `python3 scripts/build.py --release`
* Any other language releases from /translations/<language>/:
  `python3 scripts/build.py --release --language "English"`

Pass through the target language the user asks for. If the build fails, report the LaTeX/escaping error rather than publishing a broken PDF.
