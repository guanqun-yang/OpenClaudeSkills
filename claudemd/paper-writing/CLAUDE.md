# LaTeX Paper Project Conventions

## Table of Contents

1. [Project Structure](#1-project-structure)
   - 1.1 [Content vs. Style Separation](#11-content-vs-style-separation)
2. [Content Rules](#2-content-rules)
   - 2.1 [Grounding and Traceability](#21-grounding-and-traceability)
   - 2.2 [Audience](#22-audience)
     - 2.2.1 [Plain-English rephrasing for statistical claims](#221-plain-english-rephrasing-for-statistical-claims)
3. [Style and Structure Rules](#3-style-and-structure-rules)
   - 3.1 [Entry Point](#31-entry-point)
   - 3.2 [Sections (`sections/`)](#32-sections-sections)
   - 3.3 [Figures (`figures/`)](#33-figures-figures)
   - 3.4 [Tables (`tables/`)](#34-tables-tables)
   - 3.5 [Float Placement (Main Text Only)](#35-float-placement-main-text-only)
   - 3.6 [Bibliography (`zotero.bib`)](#36-bibliography-zoterobib)
   - 3.7 [Fallback (`fallback/`)](#37-fallback-fallback)
   - 3.8 [Literature Search](#38-literature-search)
   - 3.9 [Numerical Precision](#39-numerical-precision)
   - 3.10 [Venue-Aware Structure and Signposting](#310-venue-aware-structure-and-signposting)
     - 3.10.1 [Option A: ACM-Style](#3101-option-a-acm-style-acmart-hci-vis-se-venues)
     - 3.10.2 [Option B1: ARR Venues](#3102-option-b1-arr-venues-acl--emnlp--naacl)
     - 3.10.3 [Option B2: COLM](#3103-option-b2-colm)
     - 3.10.4 [Pure-ML Venues](#3104-pure-ml-venues-iclr--neurips--icml)
   - 3.11 [Writing Style](#311-writing-style)
4. [Appendix](#4-appendix)
   - A1. [ARR Per-Section Length and Structure (1000-paper survey)](#a1-arr-per-section-length-and-structure-1000-paper-survey)
   - A2. [Monospaced Identifiers and Line-Break Robustness](#a2-monospaced-identifiers-and-line-break-robustness)

## 1. Project Structure

```
.
├── main.tex              # Entry point; compiles the full paper
├── assets/               # venue-specific style files (e.g., acl.sty, neurips.sty)
├── tikz/                 # TikZ source for figures/, one .tex per figure
├── sections/
│   ├── 001-<desc>.tex    # e.g. 001-intro.tex
│   ├── 002-<desc>.tex    # e.g. 002-background.tex
│   └── ...
├── figures/
│   ├── 001-<desc>.<ext>  # e.g. 001-overview.pdf
│   └── ...
├── tables/
│   ├── 001-<desc>.tex    # e.g. 001-main-results.tex
│   └── ...
├── fallback/             # Snapshot history; managed by the `backup` skill
│   ├── MANIFEST.md       # Tag | Timestamp | Description, one row per snapshot
│   └── v0001-<desc>/     # one subfolder per tag, copy of compile-essential files
└── zotero.bib            # Bibliography, live exported from Zotero
```

### 1.1 Content vs. Style Separation

Every float has two layers that live in different places:

- **Content (the "meat") lives in `figures/` or `tables/`.** This means the rendered image (`figures/001-overview.pdf`) or the raw `tabular` rows (`tables/001-main-results.tex`).
- **Style (the aesthetics) lives in the main text.** The `figure` / `table` / `subfigure` / `subcaption` environments, `\caption{}`, `\label{}`, column alignment wrappers, and float placement specifiers are written in the section file at the point of inclusion, not inside `tables/` or `figures/`.

Concretely: `tables/001-main-results.tex` contains only the `tabular` environment and its rows. The surrounding `\begin{table}...\caption{...}\label{...}\end{table}` wrapper is written in the section file. This keeps the content reusable and the aesthetics tunable without touching the data.

## 2. Content Rules

Two principles govern what the paper *says*: the truthfulness of every claim toward the underlying experiment logs, and the comprehensibility of every claim to the target audience. The *Style and Structure Rules* in the next section are subordinate to both.

### 2.1 Grounding and Traceability

Every claim in the paper must trace back to raw evidence through an explicit chain. Maintain this chain end-to-end, in this order:

```
raw logs / scripts
        ↓
experiment-logs/README.md           (every number reproduced by a script in scripts/)
        ↓
result tables (tables/*.tex)        (every cell grounded in a README row)
        ↓
experiment-section prose            (every number traces to a table cell)
        ↓
last portion of the introduction    (each contribution restates a §Experiments finding)
        ↓
abstract                             (each key message restates an intro contribution)
```

Enforce each link:

- **Raw logs → README:** `experiment-logs/README.md` is the single source of truth. Every numeric claim in the README has a `scripts/<name>.py` (or equivalent) that regenerates it from the raw trial-level logs. Drift between the README and the underlying scripts is not allowed; if a number changes in the script output, the README must update before any downstream layer touches it.
- **README → tables:** every cell in every `tables/*.tex` traces to a specific row in `experiment-logs/README.md`. Add a `% source: …` comment at the top of each table file pointing to the README section it derives from. If a table cannot be produced by reading the README alone, the README is incomplete; do not patch the table by hand.
- **Tables → experiment-section prose:** every number that appears in the `\section{Experiments}` prose must be found verbatim in a table cell. Before submitting, scan §Experiments and annotate each number with the table/row/column it came from. A number that cannot be located in any table is not allowed.
- **Experiment-section prose → introduction (last portion):** the contribution list (and any "headline numbers" paragraph just before it) at the end of §Introduction must restate findings from §Experiments. Each contribution should be backed by at least one specific experimental finding; an intro claim that has no matching experimental statement is a broken link.
- **Introduction → abstract:** the abstract reuses the contributions, more compactly. Every claim in the abstract must be restatable as a contribution from §Introduction. Abstract claims that do not appear in the contributions are over-claiming.

If any link breaks, the paper is not ready to submit. A broken link is a README number not regenerable from a script, a table cell not in the README, a §Experiments number not in a table, an intro claim not in §Experiments, or an abstract claim not in the intro. Fix the chain before touching surface prose.

### 2.2 Audience

**Understandability is the most important content criterion, second only to truthfulness toward the experiment logs.** A paper that the reader cannot follow has failed regardless of how strong the contribution is, and the rules below are subordinate to this principle: if a rule and understandability conflict in a specific sentence, understandability wins.

The reader is the one in the user-level profile: impatient, reading in a second language, and shaky on advanced statistics. The paper-specific consequence of the last trait is that the reader treats `p < 0.05` as "good" without parsing what the p-value quantifies, and does not know the textbook distinctions between Bayesian inference and frequentist hypothesis testing, the assumptions behind a goodness-of-fit test, or what "robust to heteroskedasticity" implies for the conclusion. The rule below follows from that, and it applies to every section of the paper.

#### 2.2.1 Plain-English rephrasing for statistical claims

Statistical and methodological jargon must appear in the paper. Its absence is its own signal: a CS reviewer who scans an Experiments section and does not see `p < 0.05`, "confidence interval", "consistent estimator", "non-parametric test", "Bayes factor", "robust to heteroskedasticity", or similar terms reads the paper as under-engineered or casual. The terms intimidate, and intimidation is part of how reviewers gauge rigor and comprehensiveness on the first pass. **Keep the jargon.**

The problem is that the same terms cause non-expert reviewers, and impatient expert ones, to skip the paragraph if they cannot parse it on first read. The fix is not to drop the term but to attach a plain-English clarification right after it, in a comma-separated clause or short parenthetical. The pattern is **`<jargon term first, plain meaning right after>`**:

- "The improvement is statistically significant (p < 0.05, meaning the observed gap is unlikely to arise by chance if the two methods were actually equivalent)."
- "Our 95% confidence interval is [0.12, 0.18]; across many repetitions of this experiment, an interval constructed this way would contain the true effect about 95% of the time."
- "The estimator is consistent (as the sample size grows it converges to the true value), and the residuals are heteroskedastic (their variance changes across the range of inputs)."
- "We use a non-parametric Mann–Whitney U test (it ranks samples instead of assuming a Gaussian distribution, so heavy tails do not bias the comparison)."
- "The posterior is concentrated around `θ = 0.42` with a 90% credible interval of [0.39, 0.45] (after seeing the data, the model assigns 90% probability to the true value sitting inside that interval)."

Do not drop the term in pursuit of accessibility, and do not drop the clarification in pursuit of concision. The jargon serves the expert reviewer; the clarification serves everyone else. Both are load-bearing, and the paragraph that has one without the other fails one audience.

Numerical results are exempt only when both the statistic and its conclusion are self-evident to a non-statistician (e.g., "accuracy improved from 72% to 81%"). Anything that asks the reader to interpret a probabilistic claim is not exempt.

## 3. Style and Structure Rules

The rules below are grouped by topic: directory-level conventions first (how each subdirectory is laid out and edited), then research tooling, then prose-level conventions.

### 3.1 Entry Point

- `main.tex` is the only file that gets compiled directly.
- It contains `\input{sections/001-...}`, `\input{sections/002-...}`, etc. in numerical order.
- When adding a new section, insert the `\input{}` line in the correct numerical position in `main.tex`.
- **Always compile with `-synctex=1` so the source and PDF are two-way syncable.** Invoke `pdflatex -synctex=1 main.tex` or `latexmk -synctex=1 -pdf main.tex`. This emits `main.synctex.gz` and enables forward search (source line → PDF location) and reverse search (Ctrl/Cmd+click in the PDF → source line) in editors that support SyncTeX (VS Code LaTeX Workshop, TeXstudio, TeXShop, Skim). The `.synctex.gz` artifact is regenerated each build and is already gitignored. Two-way sync is the difference between a 5-second jump to the offending paragraph and a 5-minute scroll-and-grep search; the flag is non-optional.

### 3.2 Sections (`sections/`)

- Files are numbered with zero-padded prefixes: `001-`, `002-`, ..., preserving insertion order.
- Edit sections individually; do **not** inline section content into `main.tex`.
- **Before any significant edit, snapshot via the `backup` skill.** Invoke `Skill(skill="backup", args="<brief-kebab-desc>")` to capture the current state into `fallback/<tag>/` and append a row to `fallback/MANIFEST.md`. "Significant" includes section restructures, rewrites of more than one paragraph, deletions of figures or tables, and any change to the contribution claim. Routine typo fixes do not need a snapshot. The previous `\begin{comment}...\end{comment}` edit-with-backup convention has been retired in favor of this skill; see §3.7 (*Fallback*).
- **Watch the line after `\end{comment}`.** A blank line immediately after `\end{comment}` is treated as a paragraph break, which silently inserts a new paragraph in the rendered output and can split a sentence or push a float. Place the next visible content on the line directly after `\end{comment}` (no blank line in between), or use a `%` at the end of the `\end{comment}` line to absorb the newline. Verify after compile by checking that no unintended paragraph indent appears where the comment used to live.

### 3.3 Figures (`figures/`)

- Numbered with the same zero-padded scheme: `001-`, `002-`, etc.
- Figures are **pre-rendered image files** (PDF, PNG, SVG, etc.).
- Reference them with `\includegraphics{figures/001-<desc>.<ext>}`.
- TikZ source files live in `tikz/<name>.tex`. Each is compiled separately and the output is deterministically mapped to `figures/<num>-<name>.pdf` (e.g., `tikz/system.tex` → `figures/001-system.pdf`). Never put raw TikZ code in section files.

### 3.4 Tables (`tables/`)

- Numbered with the same zero-padded scheme: `001-`, `002-`, etc.
- Each file contains a standalone `tabular` (or similar) environment.
- Include them from sections via `\input{tables/001-<desc>.tex}`.

### 3.5 Float Placement (Main Text Only)

- **All tables and figures must be placed immediately after their section or subsection heading.** In Introduction and Method, place them after the `\section` title. In Experiments, place them after the `\subsection` title. This keeps visual elements at the top of their section, visible as soon as the reader enters it.
- If a section/subsection contains **multiple** tables or figures, group them together (e.g., using subfigures or subtables within a single float) and place the group right after the heading.
- Use `[t]` or `[tp]` for float placement. Do **not** use `[H]` (which forces inline placement and creates ugly whitespace).
- This rule applies to the **main text only** (Introduction, Related Work, Method, Experiments, Conclusion). The Appendix may place floats wherever they are most readable.

### 3.6 Bibliography (`zotero.bib`)

- This file is **live exported from Zotero** and auto-updates when the Zotero library changes.
- **Never edit `zotero.bib` manually.** Changes will be overwritten on the next Zotero sync.
- To add or fix a citation, update the entry in Zotero, then let the export refresh.
- Use only `\citep{key}` or `\citet{key}`. Default to `\citep{}` for inline citations. Use `\citet{}` only when the citation begins a complete sentence (e.g., `\citet{Foo2025} propose...`).
- **Never type "XYZ et al." as plain text.** Every reference to prior work, including in-line author mentions in the body and Related Work, must be produced by `\citep{key}` or `\citet{key}`. Writing the author name and year manually (e.g., `Smith et al. (2023)` typed as prose) breaks the bibliography link, drifts when the entry is updated in Zotero, and is the single most common cause of "missing citation" reviewer comments. If the macro renders the wrong format, fix the bibstyle, not the prose.

### 3.7 Fallback (`fallback/`)

The recoverability layer. Every significant edit must be preceded by a snapshot here so the prior state is reachable from the same repository, without relying on `git reflog` or the author's memory.

- **Layout.** One subfolder per tag (e.g., `fallback/v0001-initial-version/`, `fallback/v0002-page-limited-version/`), each containing a copy of `main.tex`, `zotero.bib`, `sections/`, `figures/`, `tables/`, `tikz/`, and `assets/` as of the snapshot moment. One `fallback/MANIFEST.md` at the top of `fallback/` indexes every tag.
- **Tag format.** `v\d{4}-brief-kebab-desc`. Version numbers increment monotonically from `v0001` (e.g., `v0001-initial-version`, `v0002-page-limited-version`, `v0003-before-method-rewrite`). Brief descriptions are kebab-case, 1 to 6 tokens. There is no reserved version number for camera-ready or any other milestone; the camera-ready snapshot is the next free number with `camera-ready-version` (or similar) as the description.
- **Manifest.** `fallback/MANIFEST.md` has one row per tag with columns `Tag | Timestamp | Description`. The Description column carries the full sentence-form description; the tag suffix is the kebab-case short form.
- **Snapshot via the `backup` skill, not by hand.** Invoke `Skill(skill="backup", args="<brief-kebab-desc>")`. The skill handles version-number increment, file copy, and manifest update atomically, and refuses to overwrite an existing tag.
- **Snapshots are immutable.** Never edit a previous `fallback/<tag>/` subfolder or rewrite a past manifest row. To correct a description, append a new row clarifying.
- **Committed to git, not gitignored.** A fresh clone or a coauthor's checkout must include the snapshot history. Do not add `fallback/` to `.gitignore`.
- **Compile-essential only.** Snapshots exclude `notes/`, `scripts/`, `pdfs/`, `resources/`, `logs/`, and build artifacts. They include everything needed to recompile the PDF as of the tag.

### 3.8 Literature Search

- **Prioritize `quicksearch` and `seek-zotero` MCP tools** over generic `WebSearch` when searching for relevant papers.
- Use `quicksearch` for discovering papers from top CS conferences and `seek-zotero` for accessing papers already in the Zotero library.
- **`quicksearch` usage is a two-call pattern.** Call `mcp__quicksearch__search_papers(query=...)` first, then for every candidate hit call `mcp__quicksearch__get_paper_details(paper_id=...)` and read **both title AND abstract** before deciding relevance. Title alone is never sufficient.
- Fall back to `WebSearch` only when the MCP tools do not return sufficient results.

### 3.9 Numerical Precision

- **Tables and figures:** report digits as precisely as the underlying data allows, up to **4 significant digits**. Do not truncate further for cosmetic reasons.
- **Text:** within the narrative, use a **consistent digit policy** across the paper: either 1 decimal digit everywhere or 2 decimal digits everywhere. Pick one and stick with it.
- **No unnecessary rounding in text.** Do not round a number down to fewer digits than the policy allows just because it "reads cleaner." The policy sets a floor, not a ceiling that invites sloppiness.
- **One unit style for percentages, prefer `%`.** Do not mix `pp` (percentage points) and `%` in the same paper. Default to `%` throughout (e.g., "accuracy improves by 3.2\%"). Reserve `pp` only when the paper is making a strict statistical distinction between an absolute change in a probability and a relative change, and even then pick one term and apply it uniformly. Writing "+3.2 pp" in one paragraph and "+3.2\%" in the next looks like inconsistent reporting, not nuance.
- **Numbers and metric names stay in plaintext, not math mode.** Wrap neither the digits nor the metric label in `$...$` for ordinary reporting. `$F_1$ of $87.3$\%` produces awkward spacing around the digits, the percent sign, and any adjacent punctuation. Write `F1 of 87.3\%` (or `\textsc{F1}` / `F$_1$` for the subscript only) in running prose. Math mode is reserved for actual mathematical expressions, not for typesetting a metric name and its value.

### 3.10 Venue-Aware Structure and Signposting

Pick the convention that matches the target venue. This decision is venue-driven, not preference-driven; mixing the two looks out-of-genre to a reviewer.

#### 3.10.1 Option A: ACM-Style (acmart, HCI, vis, SE venues)

- **§Experiments structure:** organize around explicit **RQ1 / RQ2 / RQ3** declared at the start of §Experiments. Each subsection answers one RQ. This is conventional at CHI, VIS, ICSE, FSE, ASE, and similar venues, where reviewers expect a clear roadmap.
- **Takeaway boxes:** use **explicit call-out boxes** (e.g., `\begin{tcolorbox}`, `\begin{mdframed}`) so that even impatient readers immediately notice the message. A subtle tinted-background box at end of each results subsection works well.
- **Visual flourish is welcomed:** colored boxes, bolded inline labels, and call-outs are in-genre.

#### 3.10.2 Option B1: ARR Venues (ACL / EMNLP / NAACL)

These three venues share the ACL Rolling Review submission system and follow effectively identical structural conventions. The numbers below come from a 1000-paper random sample across ACL 2024/2025, EMNLP 2024/2025, and NAACL 2024/2025 main-track long papers.

- **§Experiments structure:** use the **canonical** `Setup → Main Results → Comparison → (optional) Ablation → Analysis` subsection sequence. **No numbered RQs by default.** A survey of 200 random EMNLP 2024-2025 papers shows ~70% use this canonical structure; only 7% use numbered RQs (though that share grew from 3.5% in 2024 to 9.6% in 2025 and may be acceptable for applied-empirical work; see venue-specific notes).
- **Ablation is optional, Setup is modal.** In the 1000-paper sample, **Ablation appears in only ~21% of Experiments sections**, and deferring it to the Appendix when the experimental envelope is wide is in-genre. Setup by contrast is the most common subsection (~46% have one explicitly).
- **Related Work is optional.** About **8% of ARR papers omit Related Work entirely**, folding the prose into the introduction or a Background section. Reviewers do not penalize this. When present, the concision rule under §3.11 (*Writing Style*) applies.
- **Takeaway boxes:** do **not** use visual boxes. A scan of 200 EMNLP 2024-2025 papers found 0 use of tcolorbox/mdframed for takeaways. Instead use one of:
  1. `\paragraph{Takeaway.}` plain bold label, then 1 to 3 sentences (~3% of EMNLP papers; the cleanest signposted option in-genre);
  2. Inline `In summary, …` wrap-up sentence at end of subsection (~20% of EMNLP papers; the modal pattern);
  3. No explicit marker; let the topic sentence do the work (majority of papers).
- **Visual flourish is discouraged:** avoid colored boxes, decorative call-outs, and slide-deck artifacts. NLP reviewers read them as workshop-style or out-of-genre.

#### 3.10.3 Option B2: COLM

COLM uses the same structural conventions as the ARR venues (canonical `Setup → Main Results → Comparison → (optional) Ablation → Analysis`, no RQs, no visual takeaway boxes), but runs its own submission and review system independently of ACL Rolling Review. Treat it as Option B1 for structure, signposting, and prose style. The independent submission system affects deadlines and the rebuttal timeline, not the paper's section layout. The 1000-paper survey did not cover COLM, so the ARR-specific numerical findings above (21% Ablation rate, 8% Related Work omission, etc.) have not been independently verified for COLM but are expected to be similar.

#### 3.10.4 Pure-ML Venues (ICLR / NeurIPS / ICML)

Closer to Option B1 than Option A. No RQs (rate <10% even among random accepted papers). No visual takeaway boxes. The canonical Setup → Main Results → Ablation → Analysis sequence is universal. Use Option B1 unless the venue's own template explicitly suggests otherwise.

For empirical word-count budgets, subsection counts, abstract and introduction templates, the section-sequence distribution, and the conclusion-length distribution from the 1000-paper ARR survey, see §A1.

### 3.11 Writing Style

- **Related Work** must be concise and precise: (1) each sentence should convey the main message of the cited paper, (2) every sentence should be tied to a citation unless it sets up background context or describes how the proposed work differs from existing literature.
- **Code listings** must use the `lstlisting` environment with line numbers (`numbers=left`), not `verbatim`.
- **Takeaway signposting:** see §3.10 (*Venue-Aware Structure and Signposting*). ACM-style: explicit call-out boxes. NLP-style: `\paragraph{Takeaway.}` or `In summary, …`. Never both in the same paper.
- **System name:** always refer to the system via `\system` macro (defined in preamble, e.g., `\newcommand{\system}{WatchPoint\xspace}`). Never hard-code the system name in section files; this allows renaming in one place.
- **Section heading for the contribution:** if your contribution has a name (a system, dataset, benchmark, framework, task), use the name as the heading of the §Method-equivalent section rather than the generic word "Method". The structural slot (the section after Introduction and Related Work, before Experiments) communicates that this is the Method section; the named heading communicates the contribution. About 47% of detected Method sections in a 1000-paper ARR sample use a system or task name (e.g., SLIM-LLM, OPTQ, RESET, URS Benchmark) instead of "Method", "Methods", "Methodology", "Approach", or "Model".
- **Name the system early in the Introduction.** Mention the proposed system by name within the first 200 words of the Introduction, typically in the second paragraph. About 9 of 10 introductions in the 1000-paper ARR sample do this; deferring the name past paragraph 2 makes the reviewer hunt for the contribution.
- **Lead with a headline number in the Introduction.** Include a quantitative result (e.g., "X improves Y by Z%") in the Introduction itself, typically in a "We show ..." paragraph just before the contribution list. Around 60% of introductions in the sample have such a paragraph. Reviewers who see the headline number in the Introduction read the rest charitably; reviewers who reach §Experiments before seeing a number skim.
- **Model names stay in plaintext.** Write `GPT-4o`, `Claude Sonnet 4.5`, `Llama-3.1-70B-Instruct`, `Qwen2.5-7B` directly in the prose. Do not wrap them in `\texttt{}`, math mode, or `\textsc{}`. Mixed-case model names already read as identifiers, and the extra typography produces awkward spacing next to punctuation and adjacent words. The main text names the model; it does not specify the exact provider checkpoint.
- **Provider-identifier table in the paper's Appendix.** Add one Appendix table (e.g., `tables/0XX-model-identifiers.tex`) that lists, for every model used in the paper: the plaintext name used in the main text, the **exact** provider identifier (e.g., OpenRouter `anthropic/claude-sonnet-4-5`, Anthropic API `claude-sonnet-4-5-20250929`, OpenAI API `gpt-4o-2024-08-06`, HuggingFace `meta-llama/Llama-3.1-70B-Instruct`), the access date, and the provider it was queried through. This is the only place those long identifiers should appear; the main text refers to models by their plaintext name and points to this table on first use.
- **Use hyphens only out of necessity.** Default to two separate words and let context disambiguate. Hyphens are appropriate in exactly three cases: (a) compound adjectives directly before the noun they modify ("a well-known result", "a 30-day window"); (b) prefixes that need disambiguation ("re-cover" vs "recover", "non-trivial"); (c) chemical, mathematical, or proper-name compounds where the unhyphenated form is genuinely ambiguous. Hyphens are **not** appropriate for: (a) adverb-adjective pairs whose adverb ends in `-ly` ("a newly added column", not "newly-added"); (b) predicative compounds after a linking verb ("the result is well known", not "the result is well-known"); (c) field-of-art noun phrases that are conventionally written open ("real world data", "open source software", "machine learning model"). When uncertain, prefer the unhyphenated form, and audit the draft for `-` characters before submission.
- **Em dashes are absolutely forbidden; en dashes are allowed sparingly.** Em dashes (the Unicode `—` and the LaTeX `---`) have no exception of any kind: always restructure using a comma, semicolon, colon, parenthesis, or a separate sentence. Em dashes are an AI-favored tic and a reviewer signal. En dashes (the Unicode `–` and the LaTeX `--`) may be used **sparingly**, only in two cases: (a) numeric or page ranges where typesetting demands the en-dash glyph (`pp. 12–18`), and (b) minor-attribution compounds where both elements stand on equal footing ("the Stone–Weierstrass theorem", "the BERT–GPT divergence"). In running prose, default to "to" for ranges (`from 12 to 18 percent`).
- **Always use the comma after an introductory phrase and before a coordinating conjunction joining two independent clauses.** No length threshold exempts: even a 3-word intro keeps the comma. A missing comma forces the reader to backtrack to locate the boundary between the introductory phrase and the main subject, a high cost for the impatient non-native reader of §2.2. Write "In this paper, we present X" (not "In this paper we present X"); "When the bell rang, the students left" (not "When the bell rang the students left"); "We tested the baseline, but it failed to converge" (not "...baseline but it failed...").
- **Non-essential content: pick the wrapper contextually.** Em dashes are forbidden under the rule above, and parentheses are no longer the automatic fallback. When inserting non-essential information, choose the wrapper that matches the role of the content:
  - **Appositive commas** ("the comma sandwich") for a short noun phrase that renames or clarifies the preceding noun. *"The primary baseline, matrix factorization, achieves …"*.
  - **A transition word** for an emphasized specific instance: `namely`, `specifically`, `notably`. *"complex architectures, specifically Graph Neural Networks"*.
  - **`such as` / `including`** for an open list of examples (not exhaustive). *"common metrics, such as BLEU and ROUGE"*.
  - **Parentheses** for genuinely skippable side notes: citations, equation references, abbreviations on first use.
  - **A new sentence** for a complete or standalone thought, especially when the content runs longer than about 10 words.
  - **A `\footnote{}`** for a deeply technical caveat or hardware-config detail that does not belong in the main paragraph flow.
- **Heading case: Title Case everywhere, ending with a period for `\paragraph{}`.** Apply uniformly across `\section{}`, `\subsection{}`, `\subsubsection{}`, and `\paragraph{}`. Never mix sentence case and Title Case inside one paper. Concretely:
  - `\section{Background and Related Work}` uses Title Case; short prepositions, articles, and conjunctions stay lowercase (`and`, `of`, `the`, `to`, `for`).
  - `\subsection{Decoding Strategy}` uses the same convention.
  - `\paragraph{Effect of Training Data.}` uses Title Case with a terminal period.
  - Avoid sentence case (`\section{Background and related work}`) and avoid ALL-CAPS source (`\section{BACKGROUND AND RELATED WORK}`); the latter only happens at the rendered layer in ICLR/ICML small-caps templates, never in the source.
  - **Why:** a corpus survey of 497 accepted papers (71 each from ACL, EMNLP, EACL, COLM, NeurIPS, ICLR, ICML) found Title Case in 96% to 100% of `\section{}` and 90% to 100% of `\paragraph{}` headings across every venue with visible bold rendering. Sentence-case paragraphs appear in 43% of papers, but always as accidental mixing. Committing to one style across the paper is the reviewer-safe choice. Survey artifacts live at `notes/<ts>-PARAGRAPH-HEADING-CONVENTIONS.md` and `scripts/heading_survey.py`.
- **Plain-English rephrasing of statistical claims** (§2.2) applies to every section, not just the Introduction or the abstract.
- **Tense conventions for CS academic writing:**
  - **Related Work → present tense.** A paper's contribution is permanent: "X propose..." / "Y achieves..." Use past tense only for finished historical events ("Early versions were trained on...").
  - **Proposed Method → present tense.** Treat the system as a mathematical truth: "The agent selects the next tool based on state $s_t$."
  - **Experimental Setup → past tense.** Actions performed in a specific run: "We trained for 48 hours..." / "The dataset was split..."
  - **Results → present tense when referencing tables/figures** ("Table 1 shows..."), **past tense for specific outcomes** ("The model failed to converge on...").
  - **Abstract → mixed.** "We present [Method]... It outperformed [Baselines]."

## 4. Appendix

Supporting material referenced from the *Style and Structure Rules* above. *A1* is the empirical evidence behind the venue-specific budget guidance for ARR papers; *A2* is the technical recipe for typesetting code identifiers cleanly. Neither is itself a rule; both are reference material the agent consults when the corresponding rule needs more depth.

### A1. ARR Per-Section Length and Structure (1000-paper survey)

Quantitative budgets and structural patterns from a 1000-paper random sample stratified across ACL 2024/2025, EMNLP 2024/2025, NAACL 2024/2025 main-track long papers (sampled with `random.seed(42)` from the ACL Anthology volume indexes). Use these for budget decisions; use the prose conventions elsewhere in this file for style decisions.

**Word-count budget (median plus 25th to 75th percentile):**

| Section | Median | 25th to 75th percentile |
|---|---|---|
| Abstract | 182 | 159 to 203 |
| Introduction | 774 | 654 to 917 |
| Related Work | 489 | 376 to 657 |
| Method | 956 | 496 to 1467 |
| Experiments | 1420 | 800 to 2176 |
| Conclusion | 160 | 105 to 534 |

Total body prose at the median is roughly 3,900 to 4,500 words, which fits the 8-page two-column ARR limit once figures, tables, captions, and citations land. Method is comparable in length to Experiments at the median, contrary to the common intuition that Experiments dominates.

**Subsection counts.** Method has a median of 2 subsections (27% of papers use a single block with 0 subsections; 29% have 4 or more). Experiments has a median of 3 subsections (15% have 0; 46% have 4 or more). The most common Experiments subsection categories, in descending order, are Setup (46% of papers), Analysis (32%), Dataset (31%), Baselines (22%), Ablation (21%), Main Results (19%), Model (14%), Metrics (11%).

**Abstract template (5 sentences, modal pattern):**

1. Context or problem (1 sentence). Around 1 in 5 abstracts open with "Large language models" or a recent-progress framing.
2. Specific gap or claim (1 sentence). Often "However, ..." or "Yet ..."
3. This paper's contribution, named (1 sentence). "We present X.", "We propose X.", "We introduce X."
4. Method one-liner (1 sentence). What the system does, mechanically.
5. Results one-liner (1 sentence). Headline number plus one comparator.

**Introduction template (5 paragraphs, modal pattern):**

1. Domain motivation (1 paragraph, ~150 words). What is the area, why is it important right now.
2. Specific gap (1 paragraph, ~150 words). What prior work has missed.
3. This paper's claim and approach (1 paragraph, ~200 words). Named system, one-sentence mechanism.
4. Headline results paragraph (1 paragraph, ~150 words). Specific quantitative findings. Roughly 60% of introductions in the sample have a "We show ..." paragraph here.
5. Contributions list (a bulleted block or one final paragraph, ~150 words). 3 to 5 contributions, each a noun phrase or short clause.

**Section sequence.** The canonical sequence `Introduction, Related Work, Method, Experiments, Conclusion` is followed strictly by only **9.1%** of papers in the sample. The remaining 91% deviate in one of three common ways, all in-genre at ARR venues:

- ~22% put Related Work *after* Experiments, often as the penultimate section before Conclusion.
- ~30% have multiple top-level Method-flavored sections (the contribution split into two separable pieces).
- ~15% split Experiments into multiple top-level sections ("Main Results" plus "Analysis").

The "block-canonical" share (canonical block order, tolerating split Method and split Experiments) is 31.2%. Median top-level section count is 7 (interquartile range 6 to 8).

**Conclusion length is bimodal.** 57% of papers come in at 200 words or less (the short closing paragraph that mirrors the abstract); 20% come in at 1000 words or more (Limitations and Ethics folded into the Conclusion's numbered section). The canonical pattern is to keep Limitations and Ethics as separate unnumbered top-level sections at the very end (between the numbered Conclusion and the References block), but folding them into the Conclusion is common (~20%) and not penalized.

### A2. Monospaced Identifiers and Line-Break Robustness

LaTeX's default `\texttt{}` mishandles two common cases when typesetting code identifiers in prose. First, the underscore character renders with a visible kerning gap (the `\_` macro disables kerning around `\textunderscore`, and several common mono fonts compound the issue with wide underscore side-bearings). Second, long hyphenated identifiers (file paths, task names, function identifiers like `flood-risk-analysis` or `liu_refined`) refuse to break across lines, producing loose paragraphs, stretched word-spacing, and orphan commas. Apply all five fixes below together; partial application leaves visible residue.

**1. Preamble.** Add the following to `main.tex`:

```latex
\usepackage{inconsolata}          % mono font with tight underscore glyph
\usepackage{underscore}           % literal _ in text mode, no kerning gap
\usepackage{url}
\makeatletter
\g@addto@macro\UrlBreaks{\do\-}   % allow line breaks at hyphens
\DeclareUrlCommand{\tool@inner}{\urlstyle{tt}}
\DeclareRobustCommand{\tool}{\tool@inner}
\makeatother
```

This gives two macros for monospaced text:

- `\texttt{...}` for short, single-word identifiers that fit on a line (`bm25`, `none`, `pytest`, `SKILL.md`).
- `\tool{...}` for long hyphenated or underscored identifiers (`liu_refined`, `flood-risk-analysis`, `/path/to/file`). Built on the `url` package, so it breaks at `-`, `_`, `/`, `.` and is robust in moving arguments like `\caption{}` and `\footnote{}`.

Write identifiers literally inside `\tool{}`, with no `\_` escape needed. `\tool{liu_refined}` is correct; `\tool{liu\_refined}` is wrong.

**2. Mono font choice.** Default Computer Modern Typewriter and Bera Mono render `_` with visible side-bearings. `inconsolata` does not. If a linter or template adds another mono-font package (e.g., `\usepackage[scaled=0.85]{beramono}`), remove it: the later-loaded package overrides `inconsolata`. The `underscore` package only helps if the active mono font has a tight `_` glyph in the first place.

**3. Avoid rigid spacing compounds in captions.** A construct like `34K\,$\times$\,Backbone` glues those three tokens into one unbreakable unit via thin non-breaking spaces. Inside a narrow caption box this forces ugly word-spacing stretches elsewhere in the caption. Restructure to plain prose ("on the 34K pool with Backbone") or use regular spaces around the cross product (`34K $\times$ Backbone`) so LaTeX can break at the spaces. The same rule applies to any chained `\,...\,` compound in narrow boxes.

**4. Dense `\texttt{}` lists need structural rewriting, not just `\allowbreak`.** Adding `\allowbreak` after each item lets LaTeX break *before* the next comma, producing orphan commas on their own lines, which is worse than the original problem. The right fix is one of:

- Use `\tool{}` instead, so the items themselves can break at hyphens/underscores; OR
- Restructure the sentence so the identifier list sits at the end of a clause with room to break. For example, rewrite *"...where the gold matches closely (`\tool{a-b-c}`, `\tool{d-e-f}`, `\tool{g-h-i}`: +0.89 to +1.00 gain)"* as *"The largest positive lifts (+0.89 to +1.00) occur on tasks like `\tool{a-b-c}` and `\tool{d-e-f}`."* Fewer examples per parenthetical, and the long identifiers end the clause where LaTeX has room.

**5. Pull function-call signatures out of `\tool{}`.** Because `\tool` is built on `\url`, its argument cannot contain spaces. Write `\tool{func_name}(arg1, arg2)` rather than `\tool{func_name(arg1, arg2)}`. The identifier itself stays monospaced; the call signature is plain prose. The same applies to type annotations, dictionary key/value pairs, and any other monospaced span with internal spaces.
