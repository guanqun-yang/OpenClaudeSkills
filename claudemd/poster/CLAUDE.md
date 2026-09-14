# Poster Project Conventions

Distilled from one full poster build (Stevens beamerposter template, A0 landscape, COLM/AgenticSE workshop). Read top-to-bottom before starting iteration.

## Hard-earned communication rules (read first)

These are the lessons that cost the most iteration time. Internalize them.

- **Always clarify ambiguous layout vocabulary on first use.** "Two-column block", "centerpiece", "wide block", "fill the gap", "occupies two columns" — every one of these has multiple plausible meanings. Ask once instead of guessing. A 10-second clarification beats 3 compile cycles undoing the wrong interpretation.
- **"Too X" means scale, not delete.** When the user says "the figure is too big" or "the block is too wide", default to *shrinking* it, not removing it from the layout. Removal is rarely the implied fix.
- **Distinguish "spiritually right" from "details wrong".** When the user signals macro architecture is OK and only details need tweaking, freeze the architecture and iterate on details only. Don't restructure. This shortcut saves a lot of swing.
- **Predict column heights before compiling.** Each block has a rough height at a given column width. Sum them per column before running pdflatex. Discovering overflow via warnings burns iterations; estimating ahead avoids most of them.
- **Don't conflate "fix the symptom" with "delete the symptom".** If a wide block looks wasteful, ask whether it's the *width* or the *placement* that's the issue before moving content.
- **Use TodoWrite from turn three onward.** Multi-restructure sessions are exactly what TodoWrite is for. Externalize "the figure stays in old place" so you don't undo it the next turn.

## Project structure

```
.
├── main.tex                # Entry point; compiles the full poster
├── assets/                 # Theme .sty files, logos
├── tikz/                   # Source for any TikZ figures
├── figures/                # Pre-rendered PDFs/PNGs included by main
├── sections/
│   ├── 001-<desc>.tex      # zero-padded prefix, insertion order
│   ├── 002-<desc>.tex
│   └── ...
└── tables/
    ├── 001-<desc>.tex      # bare \tabular only; the wrapper is in sections/
    └── ...
```

Same content/style separation as the latex-paper-project skill: `tables/` holds bare `tabular` rows, `figures/` holds rendered images, the float wrapper (caption, label, placement) lives in the section file at the inclusion point.

## Layout decision tree

Posters at A0 typically need a hybrid layout. Decide upfront which of the following you're committing to, because conversion between them is expensive:

1. **Pure `multicols{4}` auto-flow** — sections stream by height balance. Simplest. Use when the figure is small enough to live inside one column.
2. **Three Beamer page-columns, figure alone in middle** — outer cols hold text streams, center holds only the workflow figure. Use when the figure must be a centerpiece with no text directly above/below it. Outer columns will have ~30cm of slack each — fill with content or accept whitespace.
3. **Three page-columns, figure in middle with `multicols{2}` below it** — outer cols hold text streams; the wide center holds the figure on top and a 2-sub-column flow of supporting blocks below. Best when figure must be prominent *and* you have section-2 detail (algorithm, agent table) that benefits from being visually grouped with the figure.
4. **Four visually-equal columns via 0.235/0.510/0.235** — outer Beamer columns at 0.235 each, center at 0.510 split via `multicols{2}` so all four visible columns render at ~28cm. Strongest when the user wants "equal columns" and the figure spans the inner two.

Reading order is **column-by-column, top-to-bottom**. Section 2 cannot be in column 3 if you want it read second. If the narrative requires section 2 to span left-and-center, the algorithm/Why-Single-Shot blocks can live in the center column's upper half (read after left column completes).

## Beamer / multicols tactics that worked

- **`\BeforeBeginEnvironment{block}{...minipage[t]{\linewidth}}`** wraps every block in an atomic minipage so multicols moves whole blocks between sub-columns. Without this, multicols slices blocks mid-content.
- **`\columnbreak` inside a `multicols{2}` region** forces a specific block (e.g., the algorithm) to claim a sub-column alone. Use when block-height balancing won't put what you want where you want.
- **`multicols` inside a Beamer column** works but heights aren't auto-bounded; supply `\setlength{\columnsep}{...}` and place the largest atomic block first to nudge the balance.
- **Figure at column width**: `\includegraphics[width=\linewidth, height=Xcm, keepaspectratio]{...}` — the height cap activates when natural-width-rendering would be too tall. Indispensable when figure aspect ratio fights column geometry.
- **Don't use `[H]` float placement** — beamerposter's body isn't a float context. Use `\begin{center}\includegraphics{...}\end{center}` for inline figures.

## Style patterns that worked

- **Custom `takeawaybox` via `tcolorbox`** for per-result conclusions. Light cream body (`RGB 255,250,235`), red left rule, red bold "Takeaway." prefix. Avoids the creepy white-text-on-red look that paragraph-length body chunks get with the template's `colorblock` environment.
- **`\begin{contribblock}`** (red header, light-gray body, black text) for the merged "RQs & Contributions" block and the final "Take-Home" closer.
- **Algorithms via `algorithm` + `algpseudocode` packages**, not `lstlisting` pseudocode. The proper environment gives numbered lines, `Input:` / `Output:` headers, ▷ comments, indented `\If`/`\For`/`\Return` keywords. Use `\algorithmicx`'s `\Call`, `\State`, `\Comment` rather than freehand.
- **Section numbering in block titles** ("1. Motivation & RW", "2. Design", "3. Dataset", "4. RQs & Contributions") makes column-by-column reading order explicit so the reader doesn't have to guess.
- **QR codes via `\usepackage{qrcode}`** + `\qrcode[height=10cm]{\someurl}`. No image files needed. Pair with a `\codelabel` macro for caption text; keep the visible label short ("Code: r/WatchPoint") even when the encoded URL is long.

## Style patterns to avoid

- **White-text-on-red body chunks** (i.e. paragraph-length text inside `colorblock[white]{stevensred}{...}`) read as "creepy". The block title bar in white-on-red is fine; the body should be a light background with dark text.
- **Section titles like "Why Two Agents" placed visually after section 3** in reading order — even if logically section 2 — break the narrative for the reader.
- **Wide single-column blocks with short content** (e.g. 4-bullet list at 50cm width) waste horizontal space. Either use `multicols{2}` internally, or move the block to a narrower column.
- **Banner-figure-on-top layouts** are usually rejected when "centerpiece" is the goal; figure-in-center surrounded by text is the typical preferred form.

## Content-fit ritual after each layout change

1. List blocks in each column with rough heights at the column's render width.
2. Sum per column. Compare to body height (~68 cm for A0 landscape minus header/footer).
3. If a column overflows by < 5 cm: trim prose; reduce inter-block `\addvspace`; consider scriptsize for tables.
4. If a column overflows by > 5 cm: redistribute blocks; don't try to trim your way out.
5. If a column has > 15 cm whitespace and the user wants density: pull a block from a fuller column or add a takeaway/example block from manuscript content.

## Geometry constants (A0 landscape, scale=1.15)

- Total textwidth: ~110 cm (varies slightly by margin).
- Body height after header + footer: ~68–75 cm depending on header content.
- Figure aspect ratio dominates — a 1.3:1 figure cannot be both half-page-width AND short. Surface this constraint to the user instead of attempting impossible layouts.

## URL handling

- Verify any cited URL via `curl -sIL` or `WebFetch` before encoding it into a QR code or footer link. 200 = OK.
- Cloudflare-protected URLs (anonymous.4open.science, some preprint services) often return 403 to non-browser clients. Flag this to the user with the suggestion to verify in a real browser; don't fabricate confirmation.
- The Stevens template has a `\projecturl` / `\codeurl` / `\projectlabel` / `\codelabel` macro pattern. Encode the *URL* in the QR (`\qrcode[height=...]{\projecturl}`) but display the *label* under the QR (`\projectlabel`) — they can differ to keep captions short.

## Per-iteration rhythm

Aim for: 1 architecture-changing turn for every 3–4 detail-polishing turns. If the ratio inverts, you're swinging on macro decisions and need to clarify before the next change. Detail polish (table size, line spacing, label text, font size, column widths) is cheap; architecture changes (column count, figure placement, section reorder) are expensive — defend the architecture once it's signaled "spiritually right".
