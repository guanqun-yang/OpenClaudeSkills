# Blog Post Conventions

## Audience

Write for an **impatient CS undergraduate** whose background is:

- **Comfortable with:** algorithms 101 (Big-O, sorting, graph traversal, dynamic programming) and the 101 level of ML / DL / RecSys / LLMs / agentic workflows (gradient descent, backprop, attention, embeddings, train/val/test split, accuracy/F1, collaborative filtering vs. content-based, what a transformer is, what training and inference mean).
- **Shaky on:** advanced statistics (Bayesian inference, measure theory, causal identification, hypothesis-testing nuances) and niche subfields. Assume **no working knowledge** of OS, computer networks, cryptography, computer graphics, or hardware internals beyond name recognition (e.g., "TLB" or "GPU memory hierarchy" may ring a bell but the precise definition does not).
- **Impatient:** will close the tab if the first paragraph does not pay off, or if any one section drags. Lead with the punchline; defer the buildup.
- **Reading English as a second language:** assume solid technical English but no childhood exposure to the language. This reader parses a figurative use of a common word literally, stops, and works out what you meant. The vocabulary is not the obstacle; the figurative layer sitting on top of familiar vocabulary is. Combined with impatience, this sets the standard every sentence must meet: **understood on the first pass, with no rereading and no guessing.**

Gloss every term beyond the comfort zone on first use in **one short clause** — e.g., *"RLHF (reinforcement learning from human feedback — the model is tuned on rankings produced by humans)"*. Inline the gloss; never link out for the definition. Do not gloss anything inside the comfort zone — defining "gradient descent" insults the reader.

## Plain Language

The audience above is impatient *and* reading in a second language. Both make the same demand, so these rules serve both. They are the ones most often missed, because the writer already knows what the sentence means.

- **Expand every abbreviation and proper name on first use**, including ones that feel too well known to explain. Conference names (ACL, NAACL, ICML, ECIR, ARR), licenses (CC0, MIT, Apache 2.0), organizations, funding programs, and dataset names each need one clause saying what they are. "NAACL" means nothing outside natural language processing, and a reader who has to search for it has already left the post. The test is not "is this famous" but "is this famous *inside the reader's stated comfort zone*."
- **Never make a definite reference to something you have not introduced.** "The target venue", "the standard approach", "the obvious version", "the usual template" all assume the reader shares a context they do not have. Name the thing on first mention, then refer back to it.
- **Every metric arrives with its scale and its direction**, in the same sentence as its first number. Not "overlap ranged from 0.000 to 0.695" but "overlap, the share of people appearing in both lists, ranged from 0.000, meaning no one in common, to 0.695." This applies to **table column headers**, which is where undefined metrics usually hide: define them in a sentence directly above the table, not in the reader's imagination.
- **Collect repeated vocabulary into one table near the front.** Inline glossing at first use is still required, but a reader who jumps straight into the middle of a long post needs a single place to look. Once a post needs more than about five glosses, give the two or three load-bearing terms a paragraph each and put the rest in a two-column table (`Term` / `What it means in this post`).
- **Every sentence needs a subject and a verb.** Answer-fragments ("Nobody who should.", "Not anymore.", "Same problem, different field.") read as incomplete to someone parsing carefully, and they force a reread. The rhetorical punch is not worth the stall.
- **Absolute dates, never relative ones.** "Nine weeks from now" is unreadable six months later; write "5 October 2026, roughly nine weeks after this post." The same applies to "recently", "last year", "the current version", and "as of today".
- **One spelling standard per post.** Do not mix "artefact" with "labeling". Pick American or British, then grep for the frequent offenders: `artefact|defence|judgement|labelling|behaviour|analyse|organisation`.

## Self-Containment

- The post must stand alone. A reader who has not opened any cited paper, repo, or prior post should still understand every claim.
- Do not write "as we saw in the previous post" or "see this other file". Either restate the background inline or link to a public external source.
- Include a short primer for any prerequisite concept beyond the comfort zone defined above.
- **Read the finished draft as a stranger.** Every unnamed referent, unexpanded acronym, and undefined metric is a self-containment failure, not a style preference. See the Plain Language section above.

## Structure

- **Table of contents is mandatory.** Place a TOC immediately after the title and before the first section. Every top-level and second-level heading of the main narrative must appear in it. Use the blog platform's native TOC syntax (e.g., `[toc]` for Typora, `{:toc}` for Jekyll, `<!-- toc -->` for markdown-it, or a hand-written linked list) — pick the one that matches the target platform and confirm it renders.
- **The Appendix is excluded from the TOC.** Paper summaries live in an Appendix at the end of the post and must **not** appear in the TOC. If the platform's auto-TOC includes everything by default, mark the Appendix heading with the platform's "exclude from TOC" hint (e.g., `{: .no_toc }` for Jekyll/Kramdown, `<!-- omit in toc -->` for markdown-it, or hand-write the TOC and simply omit the Appendix entry).
- **Number every section heading.** Top-level sections are `1. Title`, `2. Title`, …; subsections are `1.1 Title`, `1.2 Title`, …; sub-subsections are `1.1.1 Title`. The number is part of the heading text, written into the Markdown — do not rely on CSS or font size to convey hierarchy, because font-size differences alone are hard to tell apart on a quick scroll. The Appendix is the only top-level heading that is not numbered.
- The TOC reproduces those numbers so the reader can jump by index, not by trying to remember which title belonged to which depth.

## Citations

- **Every citation must be a clickable link** that resolves to the **original** paper or website — never to a secondary write-up, slide deck, or aggregator. Preferred targets, in priority order:
  1. The publisher's canonical page (e.g., `aclanthology.org`, `doi.org`, `dl.acm.org`, `openreview.net`).
  2. The arXiv abstract page (`arxiv.org/abs/XXXX.XXXXX`) when no canonical venue page exists or when the venue link is paywalled.
  3. The official project website for non-paper references (GitHub repo root, documentation root, official blog post).
- **No bare-name citations.** Writing "Smith et al. (2023) show that …" without a hyperlink on the author name, the year, or a `[1]` reference is forbidden. If you cannot find a verified URL, ask the user.
- **Verify every citation URL** by fetching it before publishing; treat 404, timeout, and paywall-redirect as failures.
- When a numbered reference list is used, every `[N]` in the body must be a clickable link to the same URL the entry in the reference list points to.

## Linking Rules

- **Never link to files inside the project.** Do not hyperlink to anything in `resources/`, `notes/`, or other local folders. The reader does not have access to them.
- **Source material in `resources/` is usually public.** Most of it (GitHub repos, papers, blog posts, documentation) exists on the open web. Find the public URL and link to that instead.
- If you cannot find the public URL with confidence, **ask the user for the exact link** rather than guessing.
- **Verify every link before inserting it.** Fetch the URL and confirm it returns a valid response (not 404, timeout, or other error).
- **Private GitHub repos are an exception.** If a link returns a 404 and the repo may be private, ask the user to confirm before either inserting the link anyway or omitting it.

## Paper Summaries

- When the post requires summarizing a paper, call **`Skill(skill="paper-summary", args="<pdf-path>")`**. Do not improvise a summary — the explicit `Skill` call is mandatory.
- Paper summaries live in an **Appendix** at the end of the post, after the main narrative. The Appendix heading is a top-level heading (e.g., `## Appendix`) and is **excluded from the TOC** (see the Structure section for the platform-specific exclusion hint).
- The Appendix heading is **not numbered** — it is the only top-level heading exempt from the dotted-number rule.
- Each paper summary inside the Appendix must be **independently foldable** (e.g., wrapped in a `<details><summary>...</summary>...</details>` block in Markdown/HTML, or the platform's equivalent).
- The main body of the post may reference a paper by name and link to its foldable in the Appendix, but the full summary lives only in the Appendix.

## Diagrams and Plots

- **Use Mermaid for every diagram or plot.** Flowcharts, sequence diagrams, state machines, class diagrams, gantt charts, pie charts, ER diagrams, and architecture sketches all go in fenced ` ```mermaid ` code blocks.
- **Never use ASCII art for plots or diagrams.** ASCII boxes-and-arrows, hand-drawn pipelines, and plain-text bar charts are forbidden — they render inconsistently across blog platforms, break on mobile, and look unprofessional. If a Mermaid diagram type does not exist for what you need, embed a real image (PNG/SVG) instead; do not fall back to ASCII.
- **Verify the Mermaid syntax with a real renderer before publishing.** Mermaid is unforgiving with unescaped parentheses, quotes, slashes, and certain characters in node labels, and "looks right" is not the same as "compiles." Run the Mermaid CLI:

  ```bash
  npx -y @mermaid-js/mermaid-cli -i diagram.mmd -o diagram.svg
  ```

  If `mmdc` is not available, fall back to `https://mermaid.live/` (paste the source, confirm it renders, then copy back). Treat a parse error the same as a broken link — it must be fixed before the post ships.
- **Never commit the rendered SVG or PNG of a Mermaid diagram.** The site renders Mermaid at read time: `pipeline.blog.publish` turns each ` ```mermaid ` fence into `<div class="mermaid">…</div>`, and the generated page loads Mermaid 11 from a CDN and converts that div into an `<svg>` in the reader's browser. The fence is therefore the deliverable, and a committed image file would be a second copy that goes stale the moment the fence is edited. The `mmdc` output from the verification step above is a throwaway artifact: write it to a scratch directory, confirm it compiles, and leave it there. No post in this repository ships a `.svg` or `.png` for a Mermaid diagram, and none should.
- **A fence that looks blank locally is almost always the previewer, not the diagram.** The Markdown preview built into VS Code does not render Mermaid unless an extension is installed, so a perfectly correct diagram appears there as an empty block or as raw source. GitHub renders the fence, and so does the published page. Before concluding that a diagram is broken, check it where it will actually be read:

  ```bash
  python3 -c "import sys; sys.path.insert(0,'pipeline/src'); from pathlib import Path; from pipeline.blog import publish_all; publish_all(Path('.'), site_pages_blog=Path('/tmp/site'))"
  grep -c 'class="mermaid"' /tmp/site/<slug>.html
  ```

  The count must equal the number of fences in the post. The emitted HTML escapes `-->` as `--&gt;` and `<br/>` as `&lt;br/&gt;`; that is correct and not a bug, because the browser decodes those entities back before Mermaid reads the element's text.
- **Pick a layout that keeps the font readable on a mobile screen.** Blog posts render inside a column roughly 700–800 px wide; anything wider gets scaled down and the labels become unreadable.
  - **Default to portrait (top-down) layout.** Use `flowchart TD` (or `TB`) rather than `flowchart LR` so the diagram grows downward, matching the scroll direction.
  - **Convert ultra-wide left-to-right diagrams to portrait.** If a `flowchart LR` has more than 4–5 nodes across, rewrite it as `flowchart TD`. If the logical flow really is sequential, switch to a vertical sequence diagram or stack the stages into rows with `subgraph`.
  - **Cap the widest row at ~4 nodes.** Beyond that, group related nodes inside a `subgraph` and let the subgraph wrap.
  - **Do not shrink the font to fit a wide diagram.** Rework the layout instead. If the diagram still does not fit, render it to SVG/PNG and embed it as an image with a fixed max-width.

## Writing Style

- **No em dashes or en dashes.** Use a comma, semicolon, or separate sentence instead. Never use `—` or `–`.
- **No bare dollar signs for currency.** Write `USD 50` (or `50 USD`), not `$50`. Two or more `$` on the same line are parsed as math delimiters by most Markdown-to-HTML pipelines (KaTeX, MathJax, Pandoc with `--mathjax`), which silently swallows the prose between them. Reserve `$...$` and `$$...$$` strictly for actual math. For non-USD currencies, spell the ISO code (`EUR 50`, `JPY 5000`).
- **No native-speaker-only idioms.** Replace common English words used in a special, idiomatic, or metaphorical sense that a non-native reader with solid technical English would not necessarily catch. The word itself may be familiar; the figurative meaning is the problem. Blog readers are international, and an impatient reader who has to pause to decode an idiom closes the tab. Substitute the literal equivalent:
  - "sign off" → "approve"
  - "edge" / "edge out" → "narrowly beat" / "outperform by a small margin"
  - "lever" → "choice" / "parameter" / "knob"
  - "sweet spot" → "best choice" / "optimal setting"
  - "out of the box" → "without modification" / "by default"
  - "ballpark" → "approximate" / "rough estimate"
  - "low-hanging fruit" → "easy gain" / "straightforward improvement"
  - "moving the needle" → "producing measurable improvement"
  - "rule of thumb" → "common practice" / "heuristic"
  - "across the board" → "in every setting" / "uniformly"
  - "double down on" → "commit further to" / "intensify"
  - "punch above its weight" → "outperform expectations for its size"

  The rule applies even when the idiomatic phrase is shorter or more vivid. Accessibility outranks stylistic flair.
- **The larger risk is the figurative use of an ordinary word, which no list can enumerate.** The word is common, the reader knows it, and the intended meaning is metaphorical. The most frequent source is writing about an abstract thing as if it were alive or physical. Watch for it especially in research writing, where it is nearly invisible to the author:
  - a proposal or idea that "dies", is "killed", or "survives" → fails, is ruled out, holds up
  - a research area that is "stuck", "crowded", "thin", or "hot" → has not produced an answer, already has several papers, has few papers, is heavily published
  - fields that "have never spoken to each other" or "never met" → have never cited each other
  - a paper that "sits on top of" another → builds directly on
  - work that is "off limits" → cannot be used
  - to "lean on" a dataset → rely mainly on
  - to "smuggle in" a fact → add without our noticing
  - an "echo chamber" → a system that reinforces its own early opinions
  - a "cautionary tale" → a warning
  - a result that "carries the weight" of a section → is the section's main claim

  **The test:** if a reader taking the words literally would picture a physical action or a living thing, rewrite it. Do this even when the metaphor is the natural way to say it, and even when the replacement is longer.
- **Avoid AI-favored words and phrases.** Use sparingly or replace with plainer alternatives:
  - **Verbs/phrases to watch:** delve into (→ examine, explore), underscore (→ show, highlight), harness (→ use), illuminate (→ explain, clarify), facilitate (→ help, enable), bolster (→ support, strengthen), streamline (→ simplify), revolutionize/transformative/game-changing (→ be specific about what changed)
  - **Transitions to watch:** "That being said," "At its core," "This underscores the importance of," "From a broader perspective," "A key takeaway is" — prefer shorter, less formulaic transitions
  - **Hedges to watch:** "generally speaking," "arguably," "to some extent," "broadly speaking" — either commit to the claim or qualify it precisely
  - **Structural tells:** "provide a comprehensive," "a nuanced understanding," "the complex interplay," "play a pivotal/crucial role," "a multi-faceted approach," "pave the way," "shed light on," "navigate the complex," "far-reaching implications," "a significant milestone"
  - **Buzzwords to watch:** "cutting-edge," "innovative," "seamless integration," "scalable solution"
- **No "pipeline" for agentic systems.** Use "workflow," "loop," or "system" instead.
- Prefer short paragraphs and short sentences. A blog reader scrolls; they do not parse.

## Final Polish Pass

When you believe the post is done, do a **dedicated sweep** of the entire draft before declaring it finished. Check:

1. **Flow** — does each section lead naturally into the next?
2. **Logic** — are claims supported? Are there gaps a 101-level reader would stumble over?
3. **Bridges** — add or tighten transitions between sections so the post reads as one piece, not a stack of notes.
4. **Readability** — break up long paragraphs, cut filler words, replace AI-favored phrases and native-speaker-only idioms flagged above. Read each sentence asking whether someone parsing carefully in a second language gets it on the first pass.
5. **Links** — re-verify every link still resolves.
6. **Citations** — every author name, year, or `[N]` marker is a clickable link to the original paper or website (publisher page, arXiv abs, or official site). No bare-name citations.
7. **Paper summaries** — confirm each is foldable, was produced via the `paper-summary` skill, and lives inside the Appendix.
8. **TOC and numbering** — confirm the TOC is present, renders on the target platform, and lists every numbered heading in the main narrative; confirm every section, subsection, and sub-subsection has its dotted number written into the heading text (`1.`, `1.1`, `1.1.1`); confirm the Appendix heading is unnumbered and absent from the TOC.
9. **Mermaid** — every diagram has been rendered with `mmdc` (or `mermaid.live`) without parse errors; default direction is portrait (`TD`/`TB`); no row exceeds ~4 nodes; font is readable at ~800 px column width; the post folder contains no `.svg` or `.png` left over from that check; and `grep -c 'class="mermaid"'` on the built page equals the number of fences in the post.
10. **Currency notation** — `grep` the draft for `$` and confirm every currency mention uses `USD N` / `EUR N` / etc.; the only remaining `$` should be inside fenced code blocks or genuine `$...$` math delimiters.
11. **Self-containment** — read the post pretending you have never seen the underlying papers, repos, or prior posts; every claim must still make sense from the text alone.
12. **Plain language sweep** — five mechanical checks, done as a dedicated pass rather than while reading for sense:
    - **Abbreviations.** Grep for runs of 2 to 6 capital letters and confirm each is expanded at first use. Venue names, license names, and program names count.
    - **Definite references.** Search for "the target", "the standard", "the obvious", "the usual", "the above". Each must point at something already named in the text.
    - **Metrics.** Every number with a unit or a 0-to-1 scale, and every table column header, states what it measures and which direction is better.
    - **Dates.** No "now", "recently", "last year", or "N weeks from now" without an absolute date beside it.
    - **Figurative language.** Reread hunting only for ordinary words used metaphorically, especially abstractions described as alive or physical. This pass finds what the idiom list cannot, because the list is never complete.
13. **Chinese version** — the post is not finished until `README.zh.md` exists and passes the checklist in the Chinese Version section below.

## Chinese Version (Mandatory)

Every post ships with a Simplified Chinese version at `<post-folder>/README.zh.md`. A post whose folder has no `README.zh.md` is an unfinished post.

**Do not produce it by translating the finished English post.** Translating anchors the Chinese to English clause boundaries and paragraph rhythm, and the output reads as translated however strongly the instruction says otherwise. Telling yourself to "restructure rather than mirror" does not escape this, because the English sentences are still the input. Remove them from the input instead.

### The workflow: one skeleton, two drafts

**Step 1. Write the skeleton** in the scratch directory, not the post folder. It holds:

- the numbered section list, plus one note per section saying what that section must establish
- a claim inventory: every factual assertion the post will make, each with its source location
- the citation table: every URL, and what it supports
- every table's contents as data
- every Mermaid diagram's node and edge list
- the term glossary, English term to Chinese term, locked before either draft starts
- one register sample: a single Chinese paragraph, approved by the user, that the Chinese draft is written to match

**The skeleton must contain no finished sentences in either language.** Notes, fragments, and data only. The moment it holds prose, that language becomes the anchor and you are translating again.

**Step 2. Write the English post** from the skeleton.

**Step 3. Write the Chinese post** from the skeleton, with the English post closed. Do not read it while drafting, and never work through it sentence by sentence.

Under roughly 1,500 English words the skeleton is overhead. Write the English, then list the claims of each paragraph, close the English, and write the Chinese from that list.

### What stays parallel, and what may differ

Parallel, and checked mechanically: the dotted section numbers and heading count, the set of URLs, table data, code blocks, math, identifiers, proper names, and the presence of every claim in the inventory.

Free to differ: heading wording, paragraph boundaries, sentence count, clause order within a section, and the title. `6.2 The Reader's Mental Energy Is Spent on Three Things` and `6.2 读者的注意力分三份` are the same section; only the `6.2` has to match.

### Register

Chinese technical prose has two failure modes, and both occur in practice:

- **Calque**, from translating: 这是关于读者的事实，不是关于咨询顾问的事实 / 一份作为工作单元的文档.
- **Overcorrection into slang**, from trying to sound native: 说白了、凭什么、吃三个条件、一堆零碎、塌得最频繁.

The target is plain written Chinese: short clauses, verbs rather than nominalizations, few `的` chains, sparse attribution. Lock it with the register sample in the skeleton instead of guessing, and ask the user to approve that sample before drafting.

The `en-zh-translation` skill is still a useful reference for punctuation conventions, glossary locking, and rendering idioms semantically; read those parts. Ignore its framing of the task as translation, and its LaTeX, EPUB, and running-head sections.

### Where the file goes

Write `<post-folder>/README.zh.md`, next to the English `README.md`. Never create a separate `-zh` post folder. `pipeline.blog.publish` walks `YYYY-MM-DD-*/README.md` to decide what a post is, then renders any `README.zh.md` sitting beside it as a second page, `<slug>.zh.html`, and links to it from the English page with a 中文版 switch. The Chinese version is deliberately never appended to the article list, so it gets a URL a reader can open but never its own entry in the blog index. A `-zh` folder would instead create a duplicate post in that index. Copy the English YAML frontmatter verbatim and add one line, `lang: zh-CN`.

### What is written in Chinese, and what stays English

Write in Chinese: the running prose, every heading, every table cell and column header, list items, and Mermaid node and edge labels.

Leave in English: fenced code blocks including their comments, all LaTeX math between `$...$` and `$$...$$`, code identifiers and event or field names, URLs, author names, paper and dataset titles, venue names, and system names. The goal is natural Chinese, not exhaustive substitution; a term whose English form is what a Chinese reader actually uses stays English.

If a display formula contains English words inside `\text{}`, leave the formula untouched and make the Chinese sentence that introduces it complete on its own, so a reader who skips the formula loses nothing.

### Rules specific to the Chinese version

- **Never hard-wrap a Chinese paragraph.** One paragraph, one line, however long. A line break inside a paragraph renders as a space: invisible between Latin words, but a visible gap between two Chinese characters (`所 以`, `场景： 一位`). The English post may be wrapped; do not copy that habit across.
- **Lock a glossary before writing any Chinese.** One Chinese rendering per concept for the whole post. Give the English in full-width parentheses on first mention only, for example 共形预测（conformal prediction）, then Chinese alone afterward.
- **The no-dash rule in the Writing Style section applies here too.** Do not use `—`, `–`, or the Chinese double em-dash `——`, even though the translation skill permits the last one. Use a comma, a semicolon, `、`, or a separate sentence.
- **Full-width Chinese punctuation throughout**: `，。；：？！`, `、` between list items, `“”` for quotes, `《》` for titles, `……` for ellipsis. Do not mix half-width punctuation into Chinese sentences. Pick one quote style and keep it for the whole post.
- **Keep the dotted section numbers** (`1.`, `1.1`, `1.1.1`) exactly as in the English post, so the two versions line up section by section.
- **Rebuild the table of contents** from the Chinese headings. Anchors follow the GitHub rule: lowercase, drop every character that is not a word character, space, or hyphen (which removes `.`, `：`, `“”`, `？`), then replace spaces with hyphens. CJK characters are kept. So `### 7.3 共形风险控制：给漏掉的违规设一个上界` becomes `#73-共形风险控制给漏掉的违规设一个上界`.
- **Rewrite inline cross-references** such as "see section 4.1" as `[第 4.1 节](#41-...)` pointing at the Chinese anchor.
- **Re-verify every Mermaid diagram** once its labels are in Chinese, using the same procedure the Diagrams and Plots section requires for the English post. A diagram that fails is a blocking failure in both languages.

### Keeping the two versions in sync

When you edit an English post that already has a `README.zh.md`, update the claim inventory first, then apply the change to both files in the same turn. Two versions that disagree are worse than one version. Because the prose is not sentence-mapped, the claim inventory is the only thing that tells you which Chinese paragraph a given English edit affects; if the skeleton was discarded, reconstruct the affected claims before editing.

### Checklist before declaring the Chinese version done

1. [ ] `README.zh.md` exists in the post folder, with frontmatter copied plus `lang: zh-CN`
2. [ ] Heading count and dotted section numbers match the English post exactly
3. [ ] Every claim in the inventory appears in both versions, and neither asserts anything the other does not
4. [ ] Every TOC entry and every inline `#anchor` resolves to a real heading
5. [ ] The set of URLs in the Chinese file is identical to the set in the English file
6. [ ] Every Mermaid diagram renders, verified the way the Diagrams and Plots section requires
7. [ ] No `—`, `–`, or `——` anywhere outside code blocks
8. [ ] No paragraph is hard-wrapped: no line ends with a Chinese character while the next begins with one
9. [ ] Glossary terms grep to a single Chinese form each, with no competing variant
10. [ ] No calque and no slang: grep the rejected forms listed under Register
11. [ ] Code blocks, math, identifiers, and proper names are byte-identical to the English post
12. [ ] The Chinese has been read once on its own, with the English hidden, and no sentence forced a reread
