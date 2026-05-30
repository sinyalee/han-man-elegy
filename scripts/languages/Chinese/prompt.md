This is the original, uncensored "Chinese" version, kept in /text. It is the source for all translations and for the censored "Simplified Chinese" derivative. The censorship transforms live ONLY in /scripts/languages/Simplified Chinese — do NOT apply them here. In the Chinese version, keep the real names and real references:

* Real names: "陈良宇", "蒋超良" (not the censored "陈ら宇" / "蒋超ら").
* Real references to sensitive events, e.g. "六四事件" (not the censored stand-in "几十年前").

# Review rules specific to Chinese

Use these together with the general process in /scripts/review.md.

## 的 / 地 / 得 — distinguish correctly throughout

* 的 = attributive, before a noun (美丽的花)
* 地 = adverbial, before a verb/adjective (狠狠地打、认真地回答)
* 得 = complement, after a verb/adjective (跑得快、搜集得差不多)

Fix 状语+的→地 and 动词+的+补语→得. Leave genuinely attributive 的 alone. This is a mechanical, unambiguous class — apply it as one global pass throughout, then sweep for missed cases (especially reduplicated adverb + 的: 狠狠的 / 慢慢的 / 认真的 / 仔仔细细的 + 动词).

## 权力 vs 权利

* 权利 = a right / entitlement someone holds (正当防卫权利、追求幸福的权利、没有权利干预)
* 权力 = authority or force to compel; institutional power, OR coercive leverage over a person (权力斗争、权力和资本勾结、获取诬告权力)

Decide once and apply consistently. In legal / rights passages it is almost always 权利. But coercive leverage is 权力, not 权利 — settled case: `获取诬告权力的控制行为` in chapter_sex is correct as 权力 (the power to control a man via the threat of a false accusation that can jail him, i.e. a force to compel). Do NOT "fix" it to 权利.

## 写到 / 写道 — by register (formal vs casual)

The author distinguishes the two by the register of what is being quoted:

* 写到 — for casual / personal writing being quoted (微信签名, blog posts, personal recollection). E.g. `微信签名写到：…`, `博客文章里面写到，…`, `我当时写到：…`.
* 写道 — for formal quotations (declarations, formal documents). E.g. `法国大革命的人权宣言写道``人生而自由''`.

Apply this distinction; do NOT blindly normalize one form to the other. Only flag a 写到/写道 if it is on the wrong side of this casual/formal line.

## Emphatic 是 + verb phrase — leave as-is

The author uses an affirmative/emphatic 是 before a verb phrase to assert a state, often with the trailing 的 dropped (e.g. `无论是撤退还是战斗，你都是做好准备`; cf. the parallel `都是非常有利的` in the same paragraph). Do NOT treat 是 + verb phrase as a 病句 (missing 了 / missing 的) and do NOT remove the 是 — keep it.

## Author-coined terms — leave intact (and flag for translators)

The author deliberately coins terms; do NOT "correct" them as 错别字 or 病句. Known coinages:

* `保进步守` — a deliberate wordplay splitting 保守 around 进步, contrasting 进步 (progress) with 保守 (retreating to tradition). Appears in chapter_how (`美国，基本没有保进步守的人`). Leave it untouched. Translators must render the wordplay (the 进步/保守 contrast), not normalize it to plain 保守.

When a review confirms a new author coinage, add it here so future reviews don't re-flag it and translators know to preserve the wordplay.

## 标点 conventions

* Chinese 破折号 is exactly two characters: —— (not ————).
* In-line lists use 顿号「、」between items, not commas.
* Quotation marks must pair correctly; the book body uses LaTeX ``…'' style — keep it consistent and never open with a closing mark (”…”). This is a settled, project-wide convention: convert any full-width curly quotes “…” to ``…'' as one mechanical global pass (glyph swap only — `“`→` `` `, `”`→`''`), preserving each quote's existing terminal-punctuation placement.
* A closing 句号 for a complete quoted sentence goes inside the closing quote; do not trap a 句号 inside 书名号《》 or inside a \hyperref link.
* Watch 全角/半角 mixing (e.g. a stray half-width space after 数字\%).

## Common 错别字 patterns

Homophone / near-form slips seen in this text: 做为→作为、活得→获得、防治→防止（非"防治疾病"语境）、即使→及时、抗→扛、帐户→账户、千万记→千万计、称为→成为、掌拓→掌跖、雄峰→雄蜂, and 他/她 指代错误. Duplicated particles: 的的、是是.

## Sensitive content

Frank sex and legal discussion are in-scope and fine. As the uncensored original, restore any garbled / censored sensitive terms to their true forms (see top). Still verify intent for anything that looks like a deliberate stand-in before changing it.

# General knowledge (applies to all non-Chinese translations)

Shared, target-language-INDEPENDENT background on the source text. Per scripts/translate.md every translation reads this file, so the facts below help any translator (into any language) understand the Chinese original. This section is neutral and factual; it does not judge the author or the book. Detailed per-term *English* renderings live in scripts/languages/English/glossary.md — that file is for English only; the facts here are language-neutral. For people: use each figure's established (non-pinyin) name where one exists (Taiwan/HK/overseas figures, and anyone with a well-known foreign-language name); otherwise romanize per the target language's convention. This is the UNCENSORED book — all real names and references below stay intact (do not censor them).

## Real public figures

* 陈良宇 — disgraced former Shanghai Party Secretary (2006 pension-fund scandal); "双开" (expelled from Party and office).
* 蒋超良 — former Hubei Party Secretary.
* 毛主席 — Mao Zedong, referenced praising the 1950 Marriage Law.
* 张桂梅 — real educator, founder of Huaping Girls' High School; a state-celebrated figure.
* 杨笠 — Chinese stand-up comedian, quoted "男人那么普通又那么自信".
* 吴亦凡 — celebrity (Kris Wu); cited as one of the author's claimed "two miscarriages of justice" (rape-conviction context).
* 刘强东 — JD.com founder (Richard Liu); the author cites his "明州案件" (Minnesota case).
* 苏享茂 — WePhone founder who died by suicide (the "苏享茂案").
* 翟欣欣 — the woman convicted in the Su Xiangmao case.
* 胖猫 — online nickname of the young man in the widely-publicized 2024 "胖猫自杀事件" (Fat Cat suicide).
* 谭竹 — the Chongqing woman named in the Fat Cat case.
* 董志民 — the husband in the "徐州铁链女" (Xuzhou chained-woman) case; named as the other claimed "冤案".
* 曹德旺 — billionaire founder of Fuyao Glass (used as a face simile for the father).
* 宗馥莉 — Wahaha chairwoman/heiress (established English name Kelly Zong; daughter of Zong Qinghou).
* 姚期智 — Andrew Yao; Turing Award laureate, founder of Tsinghua's Yao Class (姚班); the author's advisor.
* 焦恩俊 — Taiwanese actor (established stage name Vincent Chiao, not pinyin "Jiao Enjun").
* Other real figures named in the text: 徐沛东 (Shanghai Conservatory professor, accused), 施利毅 (Shanghai University nano-tech professor), 高亢 (ex-Two Sigma quant, founded Ruitian/Yanfu), 李硕 (former Renren/校内网 internet celebrity), 汪小菲 (businessman), 汪峰 / 崔健 (rock musicians), 陈履生 (former National Museum of China deputy director, painter), 杨植麟 (Moonshot AI / Kimi founder, claimed competition-class alumnus), 郑林楷 ("脑王", claimed competition-class alumnus), 童锦程 (internet PUA figure). Foreign figures use established names: 特朗普 Trump, 马斯克 Musk, 巴菲特 Buffett, 贝佐斯 Bezos, 比尔盖茨 Bill Gates, 切格瓦拉 Che Guevara, 亨利八世 Henry VIII, 歌德 Goethe, 拿破仑 Napoleon, 斯科特·菲茨杰拉德 F. Scott Fitzgerald.

## Recurring characters & their relationships

* 李新野 — the author and first-person narrator (established English name Sinya Lee; pinyin Li Xinye). Born 1991 in Shantou, Guangdong.
* 李松坚 — the author's father; chairman of Shanghai Mingyuan Group (明园集团). "李松坚们" = his cohort of older cuckolded patriarchs.
* 凌菲菲 — the "小三" (mistress) who, per the narrative, defrauded and cuckolded the father and seized billions. Recurs across the book.
* 许洁 — the father's legally-married wife; the narrative claims she was formerly a sex worker / escort.
* 李新莹 — the author's elder sister (subject of the appendix essay 《我的姐姐李新莹》).
* 李新权 — the author's half-brother, the son born late to the father by 许洁.
* 郭菊阳 (intimate form 菊阳) — the author's recurring 人妻 (married-woman) date / case study; speaks the 潮阳话 (Chaoyang dialect) line. Treat as a character name (possibly a pseudonym).
* 李丽丽 — the author's maternal aunt (大姨), former principal of 金山中学 (金中).
* Other characters: 黄姓小孩 = the child surnamed Huang whom Ling Feifei allegedly raised (i.e. not the father's, hence the cuckolding).

## Author-coined terms — meaning

These are deliberate coinages; preserve the wordplay/device, do not normalize. (English renderings are in glossary.md; the meanings below are language-neutral.)

* 保进步守 — a three-character blend that wraps 保…守 (conservative) around 进步 (progress): "conservatively guarding an old progressivism". Reproduce the conservative+progressive fusion.
* 铁绿帽法 — 绿帽 (cuckold's green hat) + 铁帽子王 (Qing perpetual-hereditary "iron-cap prince"): a law making the cuckoldry permanent/unremovable (forcing a man to support another man's child). Keep both the cuckold and the "iron/permanent" device.
* 奋斗鸡 / 奋斗嫖客 — parallel coinages on 奋斗 (the loaded "hustle/struggle" buzzword): 奋斗 + 鸡 (whore) = a woman who hustles by selling her body; 奋斗 + 嫖客 (john) = the man who believes winning earns him "会所嫩模". Keep the hustle + whore/john blend and the parallelism.
* 教授鸡 — 教授 (professor) + 鸡 (whore): epithet for 许洁 (a professorship allegedly bought). Keep both halves.
* 猪精 / 狐狸精 — 猪 (pig) + 精 (spirit/demon) for the father; 狐狸 (fox) + 精 for 凌菲菲 (classic seductress idiom). Needed for the recurring zoology joke (even-toed pig 偶蹄目 vs carnivore fox 食肉目). The mother's Chaoshan-dialect form is 猪哥精 ("lecherous boar-spirit").
* 女拳头子 — 女拳 (the derisive homophone of 女权 "feminism", lit. "female fist") + 头子 (ringleader/boss). Keep the militant "fist" pun on 权/拳 (also drives 打拳 = pejorative for feminist activism).
* 和稀泥法 — built on the idiom 和稀泥 (fudging/papering-over a dispute by appeasing both sides): split-the-difference jurisprudence. Keep the idiom.
* Other coinages to preserve: 爱情神教 (treating romantic love as a religion/cult), 感觉人 ("feeling man", the female counterpart to 理性经济人/homo economicus), 老龟男/龟男/龟公 (turtle imagery for cuckold/pimp), 南山必胜客 (nickname for Tencent, punning 必胜客 "Pizza Hut" on 必胜 "sure to win" in the Nanshan court), 数值怪 (RPG "stat monster"), 血包 (gaming "blood bag" to be drained), 思想钢印 (Three-Body Problem term for an indelible mental imprint). Many manosphere/PUA terms (弃猫效应, 家暴效应, 反荡妇机制, 预选机制, 男性可弃置性, 女本位主义) are glossed in the source itself.

## Sensitive references

* 六四事件 — the June Fourth / Tiananmen Square events of 1989. (Censored derivative replaces it with a vague stand-in; here it stays explicit.)
* 计划生育 — China's family-planning / one-child birth-control regime; tied in the text to 堕女婴 (sex-selective abortion) and the surplus-male ("光棍"/"bare branches") problem.
* 维稳 — the Party-state's "stability maintenance" (weiwen) priority.
* 共同富裕 — the Xi-era "common prosperity" slogan.
* 中华民族的伟大复兴 — the Xi-era "Great Rejuvenation of the Chinese Nation" slogan.
* 东北大下岗 — the late-1990s ("1998年") Northeast China state-enterprise mass layoffs (xiagang); paired with the laid-off-worker-pimping-his-wife trope.
* Other loaded references: 文革 (Cultural Revolution), 批斗 (struggle session), 双开 (expelled from Party + office), 解放战争 (the 1946-49 civil war, "War of Liberation"), 妇女解放, 正能量 (state-approved "positive energy"), 暴恐分子 ("violent-terrorist elements"), 1644神州陆沉 (the Ming collapse / Qing conquest, a Han-nativist framing), 重庆姐弟坠亡案 (the 2020 Chongqing case of children thrown from a high-rise), 土客械斗 (the 19th-c. Punti–Hakka clan wars). The author was once "被网警拘留" (detained by the cyber police).

## Easily-mistaken facts

* 东京粿 (glossed "Pho") — 东京 here = Đông Kinh / Tonkin / the OLD NAME FOR HANOI (northern Vietnam); it is the Chaoshan/Teochew name for Vietnamese pho. It is NOT Tokyo (the city 东京/Tokyo also appears in the book separately — do not conflate the two).
* 出花园 — the Chaoshan/Teochew coming-of-age rite, performed at age 15 (虚岁), often at 七夕节.
* 虚岁 — East Asian nominal age, counting birth as age 1 (so 15虚岁 ≈ 14 by Western count). Convert/gloss as needed.
* 斤 (jin) = 0.5 kg, so 200斤 ≈ 100 kg (the "扛过200斤大米" anecdote).
* Money figures (6000万, 5亿, etc.) are in RMB / 人民币; label the currency consistently.
* 潮阳 (Chaoyang, a Shantou district / dialect) is distinct from Beijing's 朝阳 (also "Chaoyang"). Guo Juyang's quoted line is in the 潮阳话 dialect, with a Mandarin gloss in a source footnote.
* 潮汕 (Chaoshan) = the region; the dialect/people are "Teochew". The author calls himself a "潮汕土人" (Chaoshan native/Punti), opposite the 客家 (Hakka).
* "南山必胜客" puns on 必胜客 (Pizza Hut); "苏（州河）南/苏北" puns Suzhou Creek's banks on the Sunan/Subei regional terms — both are puns, not literal places.
* Several proper nouns appear in Latin script already in the source (e.g. Silvio Micali, Sivon, Coco Park, Palo Alto, Chicago Loop, mechanism design, fraternity, hive mind, hack, etc.) — keep them as written.
* LaTeX "\_\_" blanks in the explicit passages are deliberate coy redactions left by the author for legal cover; preserve the blanks, do not fill them in.
