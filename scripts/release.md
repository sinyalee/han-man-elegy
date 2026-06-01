Build the latex files, generate the PDF, and release it to /releases using the build.py script.

Run the build with the `--release` flag, which publishes the PDF copies into /releases/:

* Default (no language) releases the Chinese original from /text:
  `python3 scripts/build.py --release`
* Any other language releases from /translations/<language>/:
  `python3 scripts/build.py --release --language "English"`

Pass through the target language the user asks for. If the build fails, report the LaTeX/escaping error rather than publishing a broken PDF.

Where each version lands under /releases (the script handles this automatically):

* Every language gets a copy at `releases/languages/<language>.pdf`.
* Only **Simplified Chinese** and **English** also get a top-level canonical copy at `releases/<bookname>.pdf`, plus a versioned archive copy — Simplified Chinese in `releases/cn_versions/`, English in `releases/en_versions/`.
* The uncensored Chinese original and any other language get the `releases/languages/` copy only — no top-level copy and no versioned archive.

As with `build`, never run two builds/releases at once — they share the same job name and output paths and would clobber each other. Release multiple languages sequentially (see "Do not run builds in parallel" in build.md).
