# Technical Report Conventions

## Audience

Write for an impatient CS undergraduate: comfortable with algorithms 101 (Big-O, sorting, graph traversal, dynamic programming) and the 101 level of ML/DL/RecSys/LLMs (gradient descent, backprop, attention, embeddings, train/val/test split, accuracy/F1, what training and inference mean); shaky on advanced statistics and niche subfields; no assumed knowledge of OS, networks, cryptography, graphics, or hardware internals beyond name recognition.

Gloss every term beyond that comfort zone on first use, in one short clause, inline, never a link-out. Do not gloss anything inside the comfort zone.

## Plain Language

- Expand every abbreviation and proper name on first use, including conference names, licenses, organizations, and dataset names. Test: familiar *inside the reader's comfort zone*, not famous in general.
- Never make a definite reference ("the standard approach," "the usual template") to something not yet introduced. Name it first, then refer back.
- Give every metric its scale and direction in the sentence with its first number. This includes table column headers.
- Collect repeated vocabulary into one table near the front once a report needs more than about five glosses.
- Every sentence needs a subject and a verb; cut answer-fragments.
- Absolute dates, never relative ones: "5 October 2026," not "nine weeks from now," "recently," or "the current version."
- One spelling standard per report, American or British, never mixed.

## Self-Containment

The report stands alone: a reader who has opened no cited paper, repo, or prior report still understands every claim. Restate background inline instead of pointing at another file. Read the finished draft as a stranger; an unnamed referent, an unexpanded acronym, or an undefined metric is a self-containment failure.

## Structure

- A table of contents is mandatory, placed right after the title, listing every top-level and second-level heading of the main narrative. Use the platform's native TOC syntax (`[toc]` for Typora, `{:toc}` for Jekyll, `<!-- toc -->` for markdown-it, or a hand-written linked list), and confirm it renders.
- The Appendix is excluded from the TOC. Mark it with the platform's exclusion hint (`{: .no_toc }` for Jekyll/Kramdown, `<!-- omit in toc -->` for markdown-it, or omit it from a hand-written TOC).

## Citations

- Every citation is a clickable link to the original paper or website, never a secondary write-up or aggregator. Priority: the publisher's canonical page (`aclanthology.org`, `doi.org`, `openreview.net`), then the arXiv abstract page, then the official project site.
- No bare-name citations. "Smith et al. (2023) show that..." needs a hyperlink on the name, the year, or a `[1]` marker. Ask the user if no verified URL exists.
- Verify every citation URL by fetching it before publishing; a 404, timeout, or paywall redirect is a failure.
- Every `[N]` in the body links to the same URL as its entry in the reference list.

## Linking Rules

- Never link to files inside the project (`resources/`, `notes/`, or other local folders); the reader cannot open them.
- Most material in `resources/` is public (GitHub repos, papers, blog posts). Find the public URL and link to that instead.
- Ask the user for the exact link rather than guessing when no public URL is found with confidence.
- A private GitHub repo is the exception: if a link 404s and the repo may be private, confirm with the user before inserting it anyway or omitting it.

## Paper Summaries

- Call `Skill(skill="paper-summary", args="<pdf-path>")` to summarize a paper. Do not improvise a summary.
- Paper summaries live in an Appendix at the end of the report, excluded from the TOC. Each summary is independently foldable (`<details><summary>...</summary>...</details>` or the platform's equivalent).
- The main body may reference a paper by name and link to its foldable in the Appendix; the full summary lives only there.

## Diagrams and Plots

- **Default to TikZ, compiled to PDF, then converted to a high-resolution PNG.** This handles a simple figure and a complex one with the same workflow, and it is the deliverable: commit the `.tex` source and the rendered PNG side by side in the report folder, and embed the PNG with a fixed max-width. Load `positioning` whenever a node is placed with `right=of`/`below=of`, and `arrows.meta` for arrow tips:

  ```latex
  \usetikzlibrary{shapes.geometric,arrows.meta,positioning,fit,backgrounds}
  ```

  ```bash
  pdflatex -interaction=nonstopmode -halt-on-error diagram.tex
  pdftocairo -png -r 400 -singlefile diagram.pdf diagram
  ```

  Render once at low resolution first (`-r 150`) to check the layout, fix overlaps or crowded text, then render the final version at `-r 400`.
- Use Mermaid instead only for a simple flowchart or sequence diagram where TikZ's extra control buys nothing, in a fenced `mermaid` code block. Verify it renders (`npx -y @mermaid-js/mermaid-cli -i diagram.mmd -o diagram.svg`, or paste into `https://mermaid.live/`) before publishing, and never commit a rendered Mermaid image; the fence itself is the deliverable, rendered client-side.
- ASCII only for a small structure a reader takes in at a glance, such as a directory tree, never for a plot or anything with real layout.
- Keep every diagram readable at a roughly 700-800px column width. Default to a top-down or portrait layout; cap the widest row at about four nodes, and group related nodes instead of widening.

## Writing Style

- No em dashes or en dashes. Use a comma, semicolon, or separate sentence.
- Watch for the figurative use of an ordinary word, especially writing about an abstract thing as alive or physical: a proposal that "dies" or "survives" (fails, holds up), a research area that is "crowded" or "hot" (has many papers, is heavily published), work that is "off limits" (cannot be used), a result that "carries the weight" of a section (is the section's main claim). Rewrite these even when the replacement is longer.
- Prefer short paragraphs and short sentences; a reader skims first, they do not parse.

## Final Polish Pass

Before declaring a report done, sweep the whole draft:

1. Flow and logic: does each section lead into the next, and are claims supported?
2. Readability: break up long paragraphs, cut filler, replace idioms and figurative language.
3. Links and citations: every link resolves, every citation is a clickable link to the original source.
4. Paper summaries: each is foldable, produced via the `paper-summary` skill, and lives in the Appendix.
5. TOC: present, renders, lists every heading in the main narrative; the Appendix is absent from it.
6. Diagrams: every TikZ figure's PNG is current with its `.tex` source and readable at mobile width; every Mermaid fence parses with no leftover rendered image file.
7. Currency: `grep` for `$`; every mention is `USD N` / `EUR N`, with `$` appearing only inside code blocks or genuine math delimiters.
8. Self-containment: read the report as a stranger; every claim holds from the text alone.
9. Plain language: abbreviations expanded, no dangling definite references, every metric scaled and directed, no relative dates, no figurative ordinary words.
