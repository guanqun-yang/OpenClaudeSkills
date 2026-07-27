# Blog Post Conventions

## Audience

Write for an **impatient CS undergraduate** whose background is:

- **Comfortable with:** algorithms 101 (Big-O, sorting, graph traversal, dynamic programming) and the 101 level of ML / DL / RecSys / LLMs / agentic workflows (gradient descent, backprop, attention, embeddings, train/val/test split, accuracy/F1, collaborative filtering vs. content-based, what a transformer is, what training and inference mean).
- **Shaky on:** advanced statistics (Bayesian inference, measure theory, causal identification, hypothesis-testing nuances) and niche subfields. Assume **no working knowledge** of OS, computer networks, cryptography, computer graphics, or hardware internals beyond name recognition (e.g., "TLB" or "GPU memory hierarchy" may ring a bell but the precise definition does not).
- **Impatient:** will close the tab if the first paragraph does not pay off, or if any one section drags. Lead with the punchline; defer the buildup.

Gloss every term beyond the comfort zone on first use in **one short clause** — e.g., *"RLHF (reinforcement learning from human feedback — the model is tuned on rankings produced by humans)"*. Inline the gloss; never link out for the definition. Do not gloss anything inside the comfort zone — defining "gradient descent" insults the reader.

## Self-Containment

- The post must stand alone. A reader who has not opened any cited paper, repo, or prior post should still understand every claim.
- Do not write "as we saw in the previous post" or "see this other file". Either restate the background inline or link to a public external source.
- Include a short primer for any prerequisite concept beyond the comfort zone defined above.

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
4. **Readability** — break up long paragraphs, cut filler words, replace AI-favored phrases and native-speaker-only idioms flagged above.
5. **Links** — re-verify every link still resolves.
6. **Citations** — every author name, year, or `[N]` marker is a clickable link to the original paper or website (publisher page, arXiv abs, or official site). No bare-name citations.
7. **Paper summaries** — confirm each is foldable, was produced via the `paper-summary` skill, and lives inside the Appendix.
8. **TOC and numbering** — confirm the TOC is present, renders on the target platform, and lists every numbered heading in the main narrative; confirm every section, subsection, and sub-subsection has its dotted number written into the heading text (`1.`, `1.1`, `1.1.1`); confirm the Appendix heading is unnumbered and absent from the TOC.
9. **Mermaid** — every diagram has been rendered with `mmdc` (or `mermaid.live`) without parse errors; default direction is portrait (`TD`/`TB`); no row exceeds ~4 nodes; font is readable at ~800 px column width.
10. **Currency notation** — `grep` the draft for `$` and confirm every currency mention uses `USD N` / `EUR N` / etc.; the only remaining `$` should be inside fenced code blocks or genuine `$...$` math delimiters.
11. **Self-containment** — read the post pretending you have never seen the underlying papers, repos, or prior posts; every claim must still make sense from the text alone.
