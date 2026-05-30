This is the **Traditional Chinese** version of the book: a translation produced from the
Chinese original in `/text` into `/translations/Traditional Chinese/`, and built from there
(`python3 scripts/build.py --language "Traditional Chinese"`).

It is **uncensored**, like the original — keep the real names (陳良宇、蔣超良) and references
(六四事件), and do not apply the Simplified-Chinese censorship transforms. Frank sexual and
legal content stays; review it for language quality only, never as content.

# How the translation is made

Source and target share an alphabet, so most of the work is a mechanical Simplified→Traditional
conversion. `convert.py` does it in seconds and writes a draft. The catch is that some
conversions depend on context, so the script applies its best guess and flags every
non-trivial spot with an inline **mark**. Resolving those marks (plus a wording pass) is the
job — far cheaper than translating by hand, and it catches the errors a blind script makes.

**Marks** (each a single character; the build will not compile until every one is resolved):

* `¹` — a one-to-many character (干 → 幹/乾/干): the script wrote the common form; choose the
  one the context demands.
* `²` — a match in `02_vocab_stable.csv` (a word we keep): confirm it was not drifted regional.
* `³` — a match in `03_vocab_change.csv` (a word we change, 软件 → 軟體): confirm it fits.

The only thing converted **silently** is a single character with exactly one traditional form
(这 → 這) — it cannot be wrong. There is no phrase dictionary, so an ambiguous character that
is not inside a 02/03 word is just marked `¹` (头发: 头 → 頭 silent, 发 → 發`¹`) — which is why
汕头|发财 → 汕頭發財 is caught instead of being mis-guessed as 汕頭髮財.

# The three tables

`01_characters.csv` is generated from OpenCC by `tables/build_tables.py` (see `tables/SOURCES.md`).
It is large and machine-only — convert.py reads it; you do not need to memorize it.

`02_vocab_stable.csv` and `03_vocab_change.csv` are hand-maintained, with columns
`sc,chosen,explain`. **Read both tables in full before resolving marks** — the `explain` column
tells you what each entry means and how to apply it, so a `²`/`³` spot is confirmed the same way
every time (and so you can see any caveats, e.g. an entry meant for one specific phrase only).
convert.py reads only `sc,chosen`; `explain` is documentation for the reviewer (you).

* **stable** = keep the standard/mainland form (比特币 → 比特幣, 万象城 → 萬象城, the name
  李松坚 → 李松堅). Pinning the full word also resolves an ambiguous character inside it (万 → 萬).
* **change** = use a different TC form (软件 → 軟體, 计算机科学 → 電腦科學).

**Only table a word whose source has one meaning.** A table entry hits every occurrence, so a
context-dependent word must stay out and be reviewed per spot: 对象 (partner vs. object),
默认 (acquiesce vs. computing default), 窗口 (window vs. 窗口期), 程序 (procedure vs. program),
信息 (a message vs. information). Tabling one would mistranslate its other sense. If you must
table a phrase that could collide with a longer string (e.g. 大冲 the place vs. 大+冲 in 重大冲突),
say so in its `explain` so the reviewer confirms the `²`/`³` rather than trusting it blindly.

# Settled conventions (do not re-litigate)

* **Characters: OpenCC standard / mainland-traditional; no Taiwan/HK glyph pass.** Keep `爲`
  (not 為), `裏` (not 裡), the particle `着` (接着、看着; 著 still appears in 著名／著作), `麪`
  (not 麵). Regional choices happen only at the word level, via the change table.
* **Quotes: corner brackets 「…」 outer, 『…』 nested** (convert.py rewrites ``` ``…'' ``` and
  `` `…' `` by depth). Do not reintroduce ``` `` `` ``` or curly “ ”. A 句號 closing a full
  quoted sentence goes inside 」.

# Workflow (run from the repo root; quote paths with spaces)

1. **Build 01** (first setup or refresh from upstream only):
   `python3 "scripts/languages/Traditional Chinese/tables/build_tables.py"` (`--offline` skips
   the download). It never touches 02/03.
2. **Convert:** `python3 "scripts/languages/Traditional Chinese/convert.py"`. Writes the working
   `.tex` (seeded once, then preserved; `--force` reseeds) and `original/` (the `/text` snapshot),
   and prints a per-file mark tally. Pass file names to restrict the run to just those files
   (e.g. `convert.py --force chapter_how.tex`) — it reseeds and re-snapshots only those, leaving
   every other reviewed file and its snapshot alone.
3. **Resolve every `¹²³` mark** in the working `.tex` (the build fails otherwise), using the
   watchlist below for `¹`. While there, check the TC reads naturally — idiomatic TC, not just
   de-simplified Mandarin. Confirm a mark by deleting it; fix a wrong one and, if it recurs,
   record it (word → 02/03, character rule → here) before deleting.
4. **Wording pass** with `scripts/review.md` and `scripts/languages/Chinese/prompt.md`
   (author-coined terms, intentional stand-ins, sensitive content the translation must keep).
5. **Build:** `python3 scripts/build.py --language "Traditional Chinese"`; fix any LaTeX errors.

Do not edit `01_characters.csv` or the scripts during a translation run — vocabulary decisions
go in 02/03, review edits go in the working `.tex`. For an incremental update after `/text`
changes, run `convert.py --update` (optionally with file names): it diffs each `original/`
snapshot against the new source and re-marks **only the changed lines**, keeping the reviewed
rest and advancing the snapshot — so you resolve a few new marks instead of re-reviewing whole
files. A file whose working copy no longer matches its snapshot line-for-line is reported and
left untouched (merge by hand, or `--force` reseed that one file). See `scripts/translate.md`.

# Reviewing `¹` — contested one-to-many characters

Most one-to-many characters have a default that is almost always right (个 → 個, 了 → 了). These
are the ones whose non-default form really occurs in this book — pick by sense:

* `干` → `幹` (do / trunk: 幹活、樹幹), `乾` (dry: 乾淨、乾杯), `干` (shield: 干戈、干預).
* `后` → `後` (after / behind — almost always), `后` (sovereign / queen: 皇后、太后、皇天后土、蜂后 queen bee).
* `里` → `裏` (inside — default here), `里` (li-unit 公里, place/surnames 故里、里長).
* `面` → `面` (face / side — default), `麪` (flour / noodles: 麪條、麪粉).
* `发` → `發` (emit / happen: 發生、發布), `髮` (hair: 頭髮、理髮).
* `表` → `表` (surface / table — default), `錶` (watch: 手錶、鐘錶).
* `松` → `松` (pine / **the name 李松堅** — default, correct), `鬆` (loose: 輕鬆、放鬆).
* `谷` → `谷` (valley — default), `穀` (grain: 穀物、五穀).
* `系` → `係` (relation: 關係), `繫` (tie: 繫鞋帶、聯繫), `系` (department / system: 系統、體系).
* `复` → `復` (resume / again: 恢復、復仇), `複` (multiple: 複雜、複製), `覆` (cover / reply: 覆蓋、答覆).
* `制` → `制` (system: 制度、機制 — default), `製` (manufacture: 製造、製作、編製).
* `斗` → `鬥` (fight: 鬥爭 — default), `斗` (dipper / unit: 北斗、斗笠).
* `致` → `致` (cause / convey — default), `緻` (fine: 細緻、精緻).
* `别` → `別` (other / don't — default), `彆` (彆扭).
* `脏` → `髒` (dirty: 骯髒), `臟` (organ: 心臟、內臟).
* `术` → `術` (art / technique — default), `朮` (the herb 白朮).
* `只` → `只` (only — default), `隻` (counter for animals / one-of-a-pair: 一隻動物、腳踏兩隻船).
* `板` → `板` (board — default), `闆` (only 老闆／老闆娘; pinned 老板→老闆 in `02_vocab_stable.csv`).
* `御` → `御` (imperial — default), `禦` (defend: 防禦、抵禦).
* `借` → `借` (borrow — default), `藉` (by means of: 憑藉、藉口；but 借鑑 keeps 借).
* `奸` → `奸` (treacherous: 奸詐、奸臣 — default), `姦` (illicit sex / rape: 強姦、姦淫). Every occurrence in this book is 強姦 (pinned 强奸→強姦 in `02_vocab_stable.csv`).
* `托` → `託` (entrust: 委託、託付、白帝城託孤 — default), `托` (hold up / foil / transliteration: 襯托、烘托、托盤、波托菲諾). 波托菲諾 is pinned in `02_vocab_stable.csv`.
* `钟`(`鍾`) → `鍾` (surname / 鍾情 — default), `鐘` (clock / time: 分鐘、點鐘、鐘錶、鬧鐘).
* `注` → `注` (pour / focus: 注意、注重、關注 — default), `註` (register / annotate: 註冊、註解、備註). 注冊→註冊 pinned in `02_vocab_stable.csv`.
* `愈` → `愈` (the more…the more: 愈來愈 — default), `癒` (heal: 治癒、痊癒). 治愈→治癒 pinned in `02_vocab_stable.csv`.
* `舍` → `舍` (house / proper name: 宿舍、慕舍 — default), `捨` (give up: 捨不得、取捨、捨棄).
* `赞`(`贊`) → `贊` (support: 贊成、贊助 — default), `讚` (praise / like: 點讚、盛讚、稱讚、讚嘆). Every occurrence in this book is the praise/like sense → 讚.
* `向` → `向` (direction / toward / tend — default), `嚮` (yearn: 嚮往). 向往→嚮往 pinned in `02_vocab_stable.csv`.
* `准`(`準`) → `準` (accurate / standard / prepare: 標準、準備、精準 — default), `准` (permit: 批准、准許、准予).
* `签`(`籤`) → `籤` (lottery / label: 抽籤、標籤、書籤 — default), `簽` (sign: 簽名、簽署、簽下、網簽). Every occurrence in this book is the sign sense → 簽.
* `徵` → `徵` (levy / sign: 特徵、象徵、徵收 — default), `征` (conquer / journey: 征服、長征、出征).

Settled: the name **李松堅** keeps 松 (not 鬆); it is pinned in `02_vocab_stable.csv`, so just
confirm the `²`. The words 關係／聯繫／複製／製造 (the 系→係／繫 and 复／制 char defaults are wrong
inside them) are pinned in `02_vocab_stable.csv` so they convert correctly.

# Punctuation & LaTeX

* 破折號 is two em-dashes (——); in-line lists use 頓號「、」. Titles use 《…》 / 〈…〉; do not trap a
  句號 inside 《》 or a `\hyperref`. Watch 全形/半形 mixing (e.g. a stray space after 數字\%).
* convert.py never touches ASCII, so commands / math / braces survive; still check for unescaped
  `% & _ #`, broken `\commands`, and mismatched braces, and confirm the build compiles.

# Recording settled decisions

When a review settles a recurring call, record it so it is not re-raised — but only durable,
project-wide ones, phrased as a mechanical rule:

* a kept word → `02_vocab_stable.csv`; a changed word → `03_vocab_change.csv` — each only if the
  source is single-sense (a context-dependent word like 默认 / 窗口 belongs in neither);
* a contested character that should always resolve one way, or a new coinage → the watchlist here.
