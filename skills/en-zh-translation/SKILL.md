---
name: en-zh-translation
description: Best practices for translating English prose into Simplified Chinese. Covers terminology consistency, sentence restructuring, punctuation conventions, voice preservation, bilingual LaTeX typesetting, and the book-length workflow (pre-extraction, per-turn cadence, running-head fix, quality control). Distilled from translating a full 245-page pop-psychology trade book end-to-end in LaTeX.
---

# English → Simplified Chinese Translation

Practical guide for producing natural, fluent Simplified Chinese from English prose — distilled from first-hand translation of a full book (12 chapters + 4 parts + epilogue + about-the-authors, ~130 K English tokens → 245-page bilingual PDF). Apply when translating books, essays, articles, or any long-form content yourself (not via a third-party translation tool).

## 1. Read the Whole Thing First

Never translate paragraph-by-paragraph in isolation. That is exactly what produces the stilted "machine-translation" feel:

- Pronouns drift (the 他/她 in paragraph 5 loses its antecedent from paragraph 3).
- Terminology drifts (*attachment style* becomes 依恋风格 here, 依恋类型 there).
- Register drifts (a character's inner monologue becomes clinical in one paragraph and colloquial in the next).

**Load the whole chapter (or ideally the whole book) into context before producing any Chinese.** Read it once for narrative, once for terms, then translate with both the English source and the already-translated Chinese paragraphs visible to yourself.

**The first chapter sets terminology for the whole book.** The choices you make in chapter 1 cascade to chapters 12, epilogue, the index — everywhere. Spend disproportionate effort on chapter 1's glossary; fixing a term-choice in chapter 7 means revisiting all prior chapters.

## 2. Build a Glossary Before You Type — and Grow It Explicitly

Before writing a single Chinese paragraph, enumerate the recurring terms and lock in renderings:

- **Technical terms** — one Chinese equivalent per concept, no exceptions. Example locks from a real book:
  - `attachment style` → 依恋类型 (never 风格)
  - `secure / anxious / avoidant` → 安全型 / 焦虑型 / 回避型
  - `attachment figure` → 依恋对象
  - `secure base` → 安全基地
  - `protest behavior` → 抗议行为
  - `activating / deactivating strategies` → 激活策略 / 失活策略
  - `codependency` → 共依存 (keep English in parens on first mention)
  - `working model` → 工作模型
  - `dependency paradox` → 依赖悖论
  - `smoking gun` → 冒烟的枪 (metaphor preserved)
  - `phantom ex` → 幻影前任
- **Proper names** — Mandarin transliteration, English in parens on first mention, Chinese alone afterward.
  - `Tamara` → 塔玛拉（Tamara） first time, 塔玛拉 after
  - `John Bowlby` → 约翰·鲍尔比（John Bowlby） first time, 鲍尔比 after
  - `Dr. Smith` → 史密斯博士 — note 博士 is postposed
- **Titled works** — Chinese title in 《》, English italic in parens.
  - `Psychological Care of Infant and Child` → 《婴儿与儿童的心理照料》（\textit{Psychological Care of Infant and Child}）
  - Movie/book titles: same pattern.

Write the glossary at the top of your working notes; refuse to deviate without reason.

**Disambiguate name collisions early.** A book often reuses given names across case studies (two "Greg"s, three "Steve"s). Settle a convention: either differentiate in Chinese (格雷格 vs. 葛瑞格) or rely on context and full name. Pick one — don't let collisions silently accumulate.

**Extract all people/places/works to a name map by the end of chapter 2.** For a trade book, expect 40–80 named entities total. Catching them early prevents inconsistent renderings later.

## 3. Restructure Sentences, Don't Mirror Them

English allows 50-word sentences with nested clauses. Chinese prefers shorter clauses connected by commas, semicolons, and em-dashes (——). Break English long sentences into 2–3 Chinese sentences.

**Don't:** 尽管凯伦再三鼓励他并向他保证自己会和他一起跳，他还是做不到，甚至到最后把所有装备都脱了下来并转身准备走人。
**Do:** 凯伦一再鼓励他，并向他保证自己会和他一起跳，他就是做不到——到最后甚至把所有装备都脱了下来，转身准备走人。

Translate the **meaning and rhythm**, not the syntax.

**English em-dash chains → Chinese em-dash + clause breaks.** English happily strings three em-dashes per sentence; Chinese tolerates —— but reads cleaner when you break at the second one and start a new clause with 而/但/于是.

**Gendered "s/he, his/her"** — English self-help uses "s/he" for clinical neutrality. Chinese `他/她` works but feels clunky when repeated. In natural prose, it is often fine to collapse to 他 or 她 based on the example's implied subject, or rephrase to avoid the pronoun ("that person" → 这样一个人).

## 4. Translate Idioms and Phrasal Verbs Semantically

Never calque English idioms word-for-word.

| English | Literal (wrong) | Idiomatic |
|---|---|---|
| *looking back* | 回头我看见 | 回过头看 |
| *fell by the wayside* | 掉在路旁 | 几乎不费力就被划掉了 |
| *at the finish line they were beaten* | 他们被打败了 | 却在终点线被反超 |
| *cold feet* | 冷脚 | 临阵退缩 |
| *put out fires* | 扑灭火焰 | 扑火（即：处理麻烦） |
| *make up your mind* | 做你的思想 | 下定决心 |
| *wear your heart on your sleeve* | 把心戴在袖子上 | 把心放在袖子上（然后解释：坦诚、不加掩饰） |
| *a white-light moment* | 白光一刻 | \,``白光''\,一刻（即：顿悟的瞬间） |
| *get cold feet* | 脚变冷 | 临阵退缩 |

When in doubt, restate the English in plain English in your head first, then render that meaning in natural Chinese. Sometimes keeping the metaphor and explaining it briefly (e.g., "*smoking gun* → 冒烟的枪（即：铁证）") preserves the book's voice better than dropping the metaphor.

## 5. Compress Filler, Don't Expand It

English prose has many transitional fillers that don't all need Chinese equivalents:

- *It seems that...* → 看起来……
- *As it turned out...* → 结果……
- *What's more...* → 不仅如此/更重要的是……
- *Indeed...* → 事实上……
- *After all...* → 毕竟……
- *In fact...* → 事实上……

But don't translate every one. Sometimes just drop or merge — English's 3-word filler may fit in a single Chinese conjunction (而/且/于是/便/却). Watch the paragraph shrink by ~10-15% in Chinese; that's usually the right direction.

## 6. Preserve Voice and Register

Match the tone of the original:

- **First-person monologue** (a character's inner voice) → use 我 consistently, conversational grammar (可是 over 然而, 挺 over 颇为, 其实 over 实际上). Allow em-dashes and ellipses to carry hesitation.
- **Authors' narration** (pop-science trade book "we") → keep 我们 plural throughout; readable but literate register. Neither academic (不宜使用 "乃"、"即") nor colloquial (不宜使用 "挺挺的").
- **Quoted dialogue** → introduce with `：`, wrap in `""` (或 `「」`), match the speaker's voice.
- **Never default to 您** unless the source is genuinely formal — 你 is the right register for trade/self-help books.

If the English has a joke or warmth, your Chinese must too; if it's clinical, yours is too.

**The author's "we" is plural; never collapse to 我.** A book by co-authors is narrated by a plural subject; keeping 我们 plural throughout is a surprisingly easy place to slip.

## 7. Punctuation Conventions

Use Chinese punctuation for Chinese text — mixing English punctuation in Chinese sentences looks unpolished.

| Purpose | Chinese | Notes |
|---|---|---|
| Period | 。 | Full-width, not `.` |
| Comma | ， | Full-width |
| Em-dash | —— | Two em-dash characters; used for parenthetical asides |
| Parentheses | （） | Full-width for Chinese content; `()` for English runs |
| Quotes | ```` ``...'' ```` (LaTeX) / `"…"` / `「…」` | Pick one style per document and stick to it |
| Book titles | 《》 | Always |
| Ellipsis | …… | Two U+2026 characters |
| Enumeration comma | 、 | Between items in a list: 苹果、橘子、香蕉 |

In LaTeX, use `\,` for hair-space kerning between CJK and Latin characters: `\,``共依存''\,（codependency）`. Without it, the opening quote looks glued to the Chinese.

**Chinese em-dash is doubled (——).** A single — is reserved for en-dashes in ranges. For pauses and asides, always use ——.

## 8. Technical Term Convention on First Mention

Establish a pattern the reader can trust:

> …这套机制被称为\textit{依恋系统}（attachment system），它由一系列情绪和行为组成……

- Italicize or bold the Chinese term
- Put the English in parentheses right after
- Use Chinese alone in all subsequent mentions
- Do this **the first time** the term appears in the whole work, not just the chapter

This lets a bilingual reader verify the rendering once and then read fluently.

**Don't re-gloss a term in every chapter.** Once introduced, the reader can look back. Re-glossing clutters the prose.

## 9. Handle Emphasis Correctly

English italics carry several distinct meanings. Each maps to a different Chinese device:

| English | Chinese |
|---|---|
| *Title of work* | 《中文书名》（*English Title*） |
| *Technical term on introduction* | \textit{技术术语}（English term） |
| *Emphatic sentence stress* (*I did love her*) | \textbf{确实}爱她 or \emph{的确}爱她（bold/重读） |
| *Foreign word* (*sensu stricto*) | Keep Latin, maybe italic |

Never italicize Chinese characters for no reason — 着重号 (·) or 加粗 is how Chinese adds emphasis. In LaTeX without 着重号 support, `\textbf{}` or `\emph{}` (which renders as italic-on-Latin / upright-on-CJK) work fine.

## 10. Cultural Bridging

Cultural references that your reader will recognize → translate directly. References they won't → add a minimal gloss in parens.

- `TV reality show` → 真人秀 (recognizable, no gloss)
- `Seattle Love Lab` → 西雅图\,``爱情实验室''\,(first mention: add English)
- `golf course` → 高尔夫球场 (recognizable)
- `Amtrak / Bell Atlantic` → 美铁 / 贝尔大西洋公司 (gloss needed)
- `Fourth of July` → 独立日 (recognizable)
- `Brooklyn Bridge` → 布鲁克林大桥 (recognizable)
- `Miranda warning` → 米兰达警告 (needs brief context if unfamiliar)

Don't over-explain — a few readers skimming over a name is fine; footnoting every Western cultural reference makes the book feel translated.

## 11. Bilingual LaTeX Layout — Full Preamble, Not Just Fonts

If producing an interleaved bilingual PDF, the preamble matters more than you think. A minimal working version:

```latex
\documentclass[11pt,oneside]{ctexart}
\usepackage{xcolor}
\usepackage[margin=1.1in]{geometry}
\usepackage{amssymb}         % for $\square$ in questionnaires
\usepackage{longtable}       % for multi-page tables (questionnaires, lists)
\usepackage{booktabs}
\usepackage{array}
\usepackage{fancyhdr}        % for running heads — CRITICAL for books
\usepackage[unicode]{hyperref}   % MUST be last

\hypersetup{
  colorlinks=true,
  linkcolor=NavyBlue,
  urlcolor=RoyalBlue,
  pdftitle={Book Title (EN–ZH Bilingual)},
  pdfauthor={Authors},
  bookmarksnumbered=true,
  bookmarksopen=true
}

\setCJKmainfont{Songti SC}
\setCJKsansfont{Heiti SC}
\setmainfont{Times New Roman}

\linespread{1.32}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.35em}

\definecolor{engray}{gray}{0.22}
\newcommand{\engpar}[1]{{\color{engray}\rmfamily #1\par}}
\newcommand{\zhpar}[1]{#1\par\vspace{0.75em}}

% Running heads — see §11.1 below
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.3pt}
\fancyhead[L]{\small\itshape\nouppercase{\leftmark}}
\fancyhead[R]{\small\thepage}
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\small\thepage}\renewcommand{\headrulewidth}{0pt}}
```

Key points:
- English in subtle gray (gray 0.20–0.25), Chinese in pure black — the eye picks up which language without switching fonts.
- Tight space **within** a paragraph pair (EN → ZH), larger space **between** pairs (`\vspace{0.75em}`).
- Section heads are bilingual on two lines: `Chapter 1 · Decoding Relationship Behavior / 第一章 · 解读亲密关系中的行为`.
- Always run xelatex at least twice (three times if TOC + cross-refs) for hyperlink resolution.
- `hyperref` must be loaded **last** — options from other packages need to be known before it wraps them.

### 11.1 The Running-Head Trap (critical)

`\section*{...}` does **not** update `\leftmark`. If you use `\tableofcontents` + starred sections, every page of your book will have "目录" (Contents) as the running head, forever. This looks like a typesetting bug but is a LaTeX semantics issue.

**Fix:** after every starred section, add `\markboth{...}{...}` with the section title. If you already have `\addcontentsline{toc}{section}{TITLE}`, you can automate it:

```python
# one-liner to fix an already-written .tex
re.sub(r'\\addcontentsline\{toc\}\{section\}\{([^}]+)\}',
       lambda m: m.group(0) + '\n\\markboth{' + m.group(1) + '}{' + m.group(1) + '}',
       tex)
```

Verify afterward by running `python -c "import fitz; d=fitz.open('book.pdf'); [print(i, d[i].get_text().split(chr(10))[0]) for i in (10,50,100,150,200)]"` — the first line of each page should show the correct chapter title.

### 11.2 Questionnaires and Check-Boxes

For Likert-scale questionnaires or category-assignment quizzes (common in trade books), use `longtable` (pages may overflow) with `$\square$` for empty check-boxes:

```latex
\begin{longtable}{@{}p{0.74\textwidth}@{\hspace{0.6em}}c@{\hspace{0.4em}}c@{\hspace{0.4em}}c@{}}
\toprule
\textbf{Statement \,/\, 陈述} & \textbf{A} & \textbf{B} & \textbf{C} \\
\midrule
\endhead
{\color{engray}\textit{1.\ English statement.}}\newline 1.\ 中文陈述。 & $\square$ & & \\[0.3em]
...
\end{longtable}
```

When the questionnaire's answer-key is hidden (reader fills in a column), put the `$\square$` in only the correct column per item — pre-category assignment is usually encoded in the source EPUB as an `<img src=checkbox.jpg>` cell; extract that programmatically.

### 11.3 Compile Hygiene

Three xelatex passes, then clean aux files:

```bash
xelatex -interaction=nonstopmode book.tex
xelatex -interaction=nonstopmode book.tex  # resolve TOC
xelatex -interaction=nonstopmode book.tex  # resolve \leftmark and bookmarks
rm -f book.aux book.log book.toc book.out
```

Don't chain with `&&` — xelatex exits nonzero on harmless font warnings, which aborts your shell pipeline and leaves you without a PDF. Use `;` to continue unconditionally.

## 12. Self-Check Before Finalizing a Chapter

Before declaring a chapter done, re-read the Chinese **alone** (hide the English):

- Does every paragraph sound like something a native speaker would write?
- If a reader pauses or rereads any sentence, restructure it.
- Do pronouns and references still track correctly from paragraph to paragraph?
- Spot-check 3 paragraphs against the English source for semantic drift.
- Verify all glossary terms appear in their locked-in Chinese form via grep.

**Quality-control greps after a full book is compiled:**

```bash
# Stale markers (common when iterating from a sample to full book)
grep -n "sample\|试译\|第一章样章\|TODO\|FIXME\|placeholder\|draft" book.tex

# Paragraph-pair symmetry — these counts should match exactly
grep -c "^\\\\engpar{" book.tex
grep -c "^\\\\zhpar{" book.tex

# Running-head wiring — should equal number of starred sections
grep -c "\\\\markboth" book.tex

# Terminology consistency — should be zero hits for wrong variants
grep -n "依恋风格" book.tex       # should find nothing if you locked to 依恋类型
```

**Inspect PDF metadata after compile** — when you iterate from a sample to a full book, the `\hypersetup{pdftitle=...}` often still says "Chapter 1 (Sample)". Verify:

```bash
python -c "import fitz; print(fitz.open('book.pdf').metadata)"
```

Common issues caught at this stage: 他/她 confusion, verb-tense leakage ("已经"/"了" misplacement), over-literal metaphors, missed negations, stale title page.

## 13. When to Use Which Model

If you are Claude itself producing the translation (in-context, no API):

- **Opus 4.7 (1M context)** — load the whole book, translate with full context. Produces the best prose. Observed rate: ~5–7 K English tokens of source per turn = roughly one mid-length chapter. A full 130 K-token book is ~25–30 assistant turns of translation + 2–4 turns of compilation/fixes. Plan for ~30 turns.
- **Sonnet** — OK for individual chapters but will lose long-range consistency; keep a glossary in the prompt.

If you must call an external model:

- Always include at least **3–5 surrounding paragraphs** as context plus the full glossary.
- Never send a single paragraph with no context.
- Prefer `gpt-4o`, `claude-sonnet-4.6`+, or `claude-opus-4.6`+ over cheaper minis for prose.

**Per-turn output budget is the limiting resource, not context.** A big chapter (~8 K English words, e.g., long case-study chapters with questionnaires and multiple vignettes) will need to be split across 2 turns. Plan the split at a natural subsection boundary, not mid-anecdote.

## 14. Book-Length Workflow — Pre-Extract, Then Iterate

For a full-book translation, do this once up front, then iterate per chapter:

### Pre-extraction (one time, cheap)

Extract each chapter to a plain-text file under `outputs/_chapters/<book>/` using ebooklib + bs4 — with paragraph tag markers like `[p]`, `[h3]`, `[li]`. This lets each subsequent turn open one chapter by name without re-parsing the EPUB.

```python
import ebooklib, os
from ebooklib import epub
from bs4 import BeautifulSoup
for bookfile, outdir in [('attached.epub','outputs/_chapters/attached')]:
    os.makedirs(outdir, exist_ok=True)
    b = epub.read_epub(bookfile)
    for item in b.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        with open(f'{outdir}/{item.file_name}.txt','w') as f:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            for p in soup.find_all(['p','h1','h2','h3','h4','li']):
                t = p.get_text().strip()
                if t: f.write(f'[{p.name}] {t}\n')
```

For questionnaires with hidden category assignments stored as `<img>` cells in table rows, extract the category mapping separately:

```python
for tr in table.find_all('tr'):
    tds = tr.find_all(['td','th'])
    stmt = tds[0].get_text(strip=True)
    category = next((c for i,c in zip(tds[1:], 'ABC') if i.find_all('img')), None)
```

### Per-turn cadence

One chapter (or one logical section of a long chapter) per turn. Each turn:

1. Read the pre-extracted chapter file.
2. Translate paragraph-by-paragraph with the whole chapter visible in context.
3. Append to the growing `book.tex` via `Edit` (replace `\end{document}` with new content + `\end{document}`).
4. Run `xelatex` twice, check page count, `rm` aux files.
5. Report progress (page count, chapter count done).

Keep `\end{document}` always at the very end; new content goes just before it. This makes the file compilable at every intermediate state.

### Common traps during multi-turn translation

- **Stale title/metadata.** The title page you wrote for a 1-chapter sample says "Chapter 1 Sample" forever. Re-read the title page after each big milestone.
- **Inconsistent `\markboth`.** New sections added later may forget `\markboth`. A quick fix pass with the regex from §11.1 regenerates them.
- **Name collisions across chapters.** Track name mappings in a mental glossary; verify via `grep` that you use one Chinese form per English name.
- **Forgetting Part-header pages.** Between chapters there are Part pages ("Part One", "Part Two"). They need their own `\section*` + `\addcontentsline` + `\markboth` + a `\newpage`.
- **Questionnaire-table width warnings.** longtable warnings "table widths have changed — rerun" need an extra compile pass.

## 15. Anti-Patterns to Reject

- Calling a pipeline "done" after one translation pass. Natural Chinese needs at least an editing pass (polish for flow, verify glossary).
- Translating paragraph-by-paragraph via API with no surrounding context.
- Letting the output tool shape the translation style (e.g., accepting Pandoc's fragmented HTML paragraph boundaries as final sentence units).
- Wholesale replacement of author voice with a generic Chinese translator voice.
- Leaving transliterated names without their English original on first mention.
- Mixing full-width and half-width punctuation in the same paragraph.
- **Shipping with "目录" in every running head** (see §11.1).
- **Shipping with stale sample metadata** (PDF title, "试译", "第一章样章" in author line). Grep before declaring done.

## Summary Checklist — Full-Book Edition

Before shipping a translated book:

1. [ ] Full chapter read in English before any Chinese written
2. [ ] Glossary locked; grep confirms consistency across all chapters
3. [ ] Name map: one Chinese rendering per English name; collisions disambiguated
4. [ ] Proper names carry English gloss on first mention (once per book, not per chapter)
5. [ ] Sentences restructured (not mirrored) for Chinese rhythm
6. [ ] Idioms rendered semantically, not literally
7. [ ] Chinese punctuation used throughout CJK text (including Chinese em-dash ——)
8. [ ] Italics mapped correctly to Chinese emphasis devices
9. [ ] Each chapter re-read in Chinese alone for flow
10. [ ] Spot-check 3 paragraphs per chapter vs English for drift
11. [ ] Bilingual layout: EN in subtle gray, ZH in black, tight intra-pair spacing
12. [ ] Running heads show current chapter (`\markboth` after every starred section)
13. [ ] PDF metadata reflects the final scope (not a sample title)
14. [ ] No `sample` / `TODO` / `FIXME` / `试译` / `第一章样章` leftover
15. [ ] `\engpar` count equals `\zhpar` count
16. [ ] Three xelatex passes; no unresolved references; clean aux files
