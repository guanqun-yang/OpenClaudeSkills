---
name: academic-graphic-design
description: Style guide for publication-quality academic figures and tables, based on Tongshuang Wu's HCI/NLP papers. Covers color palettes, typography, layout, tables, inline annotations, and figure preparation.
---

# Academic Graphic Design Style Guide

Style conventions extracted from Tongshuang Wu's research papers (AI Chains, Polyjuice, PromptChainer, ScatterShot, LLMs as Workers). Apply these when creating or reviewing figures, tables, and visual elements for academic papers.

## 1. Color Palette

### Core Reusable Colors

These colors recur across multiple papers and form a consistent visual language:

| Role | Name | Value | Usage |
|------|------|-------|-------|
| Prompt text | `cprompt` | `#3c4043` | Inline quoted text, prompt content |
| Example text | `cexample` | `rgb(0.23, 0.30, 0.45)` | Inline examples, darker blue-gray |
| Light gray | `clightgrey` | `#80868b` | Secondary text, annotations |
| LLM output bg | `cgenback` | `#F1F3F4` | Background for AI-generated content |
| LLM output text | `cgenfront` | `#0076BA` | Blue foreground for generated text |
| Generated text | `cgenerate` | `#3B4D73` | Monospace LLM output |

### Semantic Colors

| Role | Value | When to use |
|------|-------|-------------|
| Input (primary) | `#3182bd` | User input, source data |
| Input (secondary) | `#6baed6` | Secondary input channel |
| Output (primary) | `#137333` | Model output, success |
| Output (secondary) | `#1e8e3e` | Secondary output |
| Error / deletion | `#E15759` or `#EC6742` | Failed tests, removals |
| Success / addition | `#59A14F` or `#499D5E` | Passing tests, additions |
| System / AI | `#4B2E83` | System-generated, UW purple branding |

### Case Study Palette (8-color)

For multi-category figures with many distinct elements:

| Color | Hex | Role in AI Chains |
|-------|-----|-------------------|
| Cyan | `#00BBD4` | Concept, VegaLite-0 |
| Orange | `#FF9701` | Interaction, trait |
| Yellow | `#FFD932` | Suggestion, expand |
| Green | `#4DAE50` | Rewrite, metaphor |
| Blue | `#0076BA` | Rule, acronym, generated |
| Orange-red | `#F27200` | Description, has-acronym |
| Pink | `#FF968D` | Valid result |
| Teal | `#00AB8E` | Full sentence |

### Diff / Change Visualization

For showing additions, deletions, and swaps (e.g., counterfactuals):

```latex
% Addition: green text on mint background
\definecolor{caddback}{rgb}{0.90, 0.98, 0.96}
\definecolor{cadd}{rgb}{0, 0.47, 0.34}

% Deletion: orange-red text on pink background
\definecolor{cdelback}{rgb}{1, 0.94, 0.92}
\definecolor{cdel}{rgb}{0.83, 0.32, 0.16}

\newcommand{\add}[1]{\colbox{caddback}{\color{cadd}#1\xspace}}
\newcommand{\remove}[1]{\colbox{cdelback}{{\color{cdel}#1\xspace}}}
\newcommand{\swap}[2]{\remove{#1}~$\rightarrow$~\add{#2}}
```

### Table Cell Category Backgrounds

For coloring table columns by evaluation category:

| Category | Hex | Visual |
|----------|-----|--------|
| In-domain | `#dae8f5` | Pastel blue |
| Out-of-domain | `#d8f0d3` | Pastel green |
| Contrast set | `#fee9d4` | Pastel peach |

### General Palette Philosophy

- Use **Tableau 10** for categorical data.
- Use **semantic colors** consistently: red = error/bad, green = success/good, blue = input/system.
- Use **Value-Suppressing Uncertainty Palettes (VSUPs)** when encoding both value and reliability.
- Avoid gratuitous color. High data-to-ink ratio (Tufte-style minimalism).

## 2. Typography

### Body Text

- **Serif** for body: Computer Modern (LaTeX default) for ACL, Libertine/Biolinum via `acmart` for CHI.
- **Sans-serif** for figures/charts: Arial, Helvetica, or Roboto at 8--10pt.
- **Monospace** for code/prompts: Courier or Fira Code via `\texttt{}`.

### Font Sizes in Context

| Context | Size | Leading | Example |
|---------|------|---------|---------|
| Body text (ACL) | 11pt | 13pt | `\documentclass[11pt,a4paper]{article}` |
| Body text (CHI) | 10pt | 12pt | `\documentclass[sigconf]{acmart}` |
| Figure captions | 10pt | 12pt | Set by template |
| Small inline text | 9pt | 11pt | `\fontsize{9pt}{11pt}\selectfont` |
| Table content | 7.5--8.5pt | 8--9pt | `\fontsize{7.5}{8}\selectfont` |

### Logo / System Name Typography

- **Font:** Geometric sans-serifs: Inter, Roboto, Open Sans, or Encode Sans.
- **Case:** Lowercase (`polyjuice`) for modern feel, or Title Case (`ScatterShot`).
- **Weight:** Bold for name, Light/Regular for descriptors.
- **Kerning:** Slightly increased letter spacing for a premium feel.
- **Icon trick:** Replace or modify one letter with a geometric symbol (spark, node, link).
- **The 32px test:** Logo must be legible at favicon size.

## 3. Figure Preparation

### Creation Workflow

1. **Design** in Keynote, Figma, or Illustrator (never raw TikZ for complex figures).
2. **Export as PDF** for infinite scalability in LaTeX.
3. **Crop in LaTeX** using `trim={left bottom right top}, clip` on `\includegraphics`.

This trim/clip pattern is used extensively — figures are exported as full-page PDFs and surgically cropped:

```latex
\includegraphics[trim={0 13.5cm 39cm 0cm}, clip, width=1\linewidth]{figures/pipeline.pdf}
```

### Sizing Conventions

| Context | Width | Example |
|---------|-------|---------|
| Full-width figure (`figure*`) | `0.85--1.0\linewidth` | Most common |
| Single-column figure | `1\columnwidth` | Narrow diagrams |
| Inset / secondary | `0.7\linewidth` | Appendix, detail views |

Common widths: `1\linewidth`, `0.95\linewidth`, `0.9\linewidth`, `0.85\linewidth`, `0.7\linewidth`.

### Placement

- Use `\begin{figure*}[t]` (full-width, top) as the default for main figures.
- Use `\begin{figure}[t]` (single-column, top) for narrow supplementary figures.
- Add `\vspace{-15pt}` between image and caption, `\vspace{-10pt}` after the figure environment to tighten spacing.

### Layout Patterns

- **Linked Dashboard:** Multiple panels (a, b, c) showing overview, faceted view, and case study.
- **Tufte-style minimalism:** No unnecessary gridlines, borders, or 3D effects.
- **Node-Link Diagrams:** For LLM pipelines and chaining flows.
- **Bolding & colored spans:** Within sentences to show perturbations or emphasis.
- **Tags / pills:** Stylized background-colored labels like `[NEGATION]`, `[ENTITY]`.

## 4. Table Styling

### Essential Packages

```latex
\usepackage{booktabs}    % \toprule, \midrule, \bottomrule
\usepackage{multirow}    % spanning rows
\usepackage{colortbl}    % \cellcolor, \arrayrulecolor
\usepackage{subcaption}  % subtables
```

### Typography in Tables

```latex
\fontsize{7.5}{8}\selectfont   % tight tables (most common)
\fontsize{8.5}{9}\selectfont   % slightly more readable tables
```

### Spacing

```latex
\setlength{\tabcolsep}{3pt}        % tight (most common: 3--5pt)
\renewcommand{\arraystretch}{0.9}   % slightly compressed rows (range: 0.8--1.1)
```

### Rules

Use booktabs rules with gray sub-rules to separate groups within a table:

```latex
\newcommand{\subrule}{\arrayrulecolor{black!30}\midrule}    % light gray divider
\newcommand{\mainrule}{\arrayrulecolor{black!100}\midrule}   % full black divider
```

### Custom Column Types

Fixed-width columns with controlled alignment:

```latex
\newcolumntype{L}[1]{>{\raggedright\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}
\newcolumntype{C}[1]{>{\centering\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}
\newcolumntype{R}[1]{>{\raggedleft\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}
```

### Scaling

When a table is slightly too wide, scale it rather than rewriting:

```latex
\scalebox{0.79}{\begin{tabular}{...}...\end{tabular}}
```

### Table Placement

- Default: `\begin{table*}[t]` (full-width, top).
- Subtables side-by-side: use `\begin{subtable}[ht]{0.48\textwidth}` with spacers.

## 5. Inline Annotations & Visual Macros

### Quoted Examples

```latex
\newcommand{\exinline}[1]{{\color{cprompt}``#1''\xspace}}
\newcommand{\quoteinline}[1]{{\color{cprompt}\emph{``#1''}\xspace}}
```

### Prompt / Generated Text

```latex
% Prompt text: dark gray monospace
\newcommand{\tprompt}[1]{{\color{cprompt}\texttt{#1}}\xspace}

% Generated text: dark blue monospace
\newcommand{\tgenerate}[1]{{\color{cgenerate}\texttt{#1}}\xspace}

% LLM output: light gray background + underline
\newcommand{\primLLMGen}[1]{\colbox{cgenback}{\underline{#1}\xspace}}
```

### Check / Cross Marks

```latex
\usepackage{pifont}
\newcommand{\cmark}{{\ding{51}}}
\newcommand{\xmark}{{\ding{55}}}
\newcommand{\cmarkcolor}{{\color{ccmark}{\cmark}}\xspace}   % green #499D5E
\newcommand{\xmarkcolor}{{\color{cxmark}{\xmark}}\xspace}   % red #EC6742
```

### Circled Numbers (for figure callouts)

```latex
\newcommand*\textcircle[1]{\tikz[baseline=(char.base)]{
    \node[shape=circle,draw,inner sep=0.5pt] (char) {#1};}}
```

### Example Box

```latex
\fboxrule=0.1pt
\newcommand{\ebox}[1]{%
    \vspace{2pt}
    \noindent\fcolorbox{gray}{white}{
        \begin{minipage}{0.95\linewidth}
            \fontsize{9pt}{11pt}\selectfont {#1}
        \end{minipage}
    }
    \vspace{-2pt}
}
```

### Q&A Box

```latex
\newcommand{\qbox}[2]{%
    \begin{center}
        \noindent\fbox{
        \begin{minipage}{0.95\linewidth}
            \textbf{Q:} #1\newline
            \textbf{A:} #2
        \end{minipage}
    }
    \end{center}
}
```

### Colored Comparison Labels

```latex
\newcommand{\crowdpipe}{\textcolor{blue}{Crowd. pipelines}:\xspace}
\newcommand{\llmchain}{\textcolor{orange}{LLM chains}:\xspace}
```

### Bold Paragraph Headings

```latex
\newcommand{\paragraphBold}[1]{\paragraph{\emph{\textbf{#1}}}}
```

## 6. Hyperlink Styling

```latex
\definecolor{darkblue}{rgb}{0, 0, 0.5}
\hypersetup{colorlinks=true, citecolor=darkblue, linkcolor=darkblue, urlcolor=darkblue}
```

## 7. Key Packages Checklist

Common packages across all papers:

```latex
\usepackage{microtype}       % subtle typographic improvements
\usepackage{tikz}            % circled numbers, inline graphics
\usepackage{soul}            % \hl (highlight), \st (strikethrough)
\usepackage{subcaption}      % subfigures and subtables
\usepackage{booktabs}        % professional table rules
\usepackage{enumitem}        % customized lists
\usepackage{xspace}          % smart spacing after macros
\usepackage{pifont}          % check/cross marks
\usepackage{cleveref}        % smart cross-references (\cref)
```

## 8. TikZ Diagram Best Practices

When TikZ is used (instead of Keynote/Figma), follow these rules for clean system diagrams.

### Font and Text

- **Use Inter** as the sans-serif font: `\usepackage[sfdefault]{inter}`. It is modern, highly legible at small sizes, and has excellent weight range.
- **Use FontAwesome5** for icons: `\usepackage{fontawesome5}`. Icons like `\faRobot`, `\faVial`, `\faTerminal`, `\faGlobe`, `\faEye`, `\faBug`, `\faClipboardCheck` add instant visual recognition to nodes without custom artwork.
- **Font sizes by context:**
  - Headings/panel titles: 9--9.5pt bold (`\fontsize{9}{11}\selectfont\bfseries`)
  - Node titles: 8--8.5pt bold
  - Node descriptions: 6--6.5pt regular (`\fontsize{6}{7}\selectfont`)
  - Section labels / annotations: 6--6.5pt italic
  - Edge labels: 6.5--7pt
- **Two-level node text.** Icon + bold title on line 1, small description on line 2:

```latex
{{\color{agentbord}\faRobot}~~\textbf{Coding Agent}\\[-2pt]
 {\fontsize{6}{7}\selectfont 30 turns budget}}
```

### Color Palette for Diagrams

Use Material Design-inspired colors. Each node type gets a **fill/border pair** where the fill is light (HTML pastel) and the border is the saturated version of the same hue:

```latex
% Example pairs: fill + border
\definecolor{agentfill}{HTML}{E3F2FD}    % light blue
\definecolor{agentbord}{HTML}{1976D2}    % strong blue
\definecolor{testfill}{HTML}{F5F5F5}     % light gray
\definecolor{testbord}{HTML}{616161}     % dark gray
\definecolor{errorfill}{HTML}{FFEBEE}    % light red
\definecolor{errorbord}{HTML}{C62828}    % deep red
\definecolor{successfill}{HTML}{E8F5E9}  % light green
\definecolor{successbord}{HTML}{2E7D32}  % dark green
\definecolor{watchfill}{HTML}{FFF8E1}    % light amber (contributions/novel)
\definecolor{watchbord}{HTML}{F9A825}    % amber
```

**Rules:**
- Fill is the HTML pastel, not `color!8` which is too faint for print. Target 15--25% visual weight.
- Border color is the saturated hue of the same family.
- Icon color inside nodes matches the border: `{\color{agentbord}\faRobot}`.
- Semantic consistency: blue = agents/system, gray = tests/infrastructure, red = errors/fail, green = success/pass, amber/yellow = contributions/novel modules.
- Deemphasize secondary components (e.g., routing logic) by using gray fill + gray border.

### Connectors

Bad connectors are the most common TikZ mistake. Rules:

- **Always use `rounded corners=3-4pt`** on every path. Sharp 90-degree bends look amateurish.
- **Route orthogonally.** Use `|-` and `-|` with rounded corners. Never use diagonal lines in system diagrams.
- **Small, consistent arrow tips.** `Stealth[length=4.5pt, width=3pt]` is clean. Define once in `>=`:

```latex
>={Stealth[length=4.5pt, width=3pt]}
```

- **Color-code paths by semantics:** gray for normal flow, green for success, red for error, amber for feedback/contribution.
- **Avoid overlapping paths.** Offset parallel lines using `xshift`/`yshift` on coordinates.
- **Use named anchors** (`.north`, `.south`, `.east`, `.west`) instead of letting TikZ guess connection points. Spread multiple connections across different anchors of the same node.
- **Minimize crossings.** Rearrange node positions to eliminate crossings. If a bypass path would cross nodes, route it far enough outside to clear them entirely.
- **Line widths:** 0.7--0.8pt for arrows, 0.8--0.9pt for node borders, 0.4--0.5pt for background decorations (fan lines, grouping).

### Layout and Storytelling

- **Don't show everything at once.** Complex systems need a two-panel approach:
  - **(a) Backbone/overview:** Show the main pipeline as a simple left-to-right flow. Novel modules appear as dashed placeholder boxes with a "see (b)" label.
  - **(b) Zoom-in detail:** Show internals of the novel module in a separate panel below.
- **Zoom-in visual effect:** Connect (a) to (b) with fan lines from the placeholder's bottom corners to the detail box's top corners. Add a subtle gradient fill between them and a `\faSearchPlus` icon at the midpoint:

```latex
\begin{scope}[on background layer]
  \fill[watchbord!6]
    (wp.south west) -- (zoombox.north west)
    -- (zoombox.north east) -- (wp.south east) -- cycle;
  \draw[line width=0.4pt, color=watchbord!25]
    (wp.south west) -- (zoombox.north west);
  \draw[line width=0.4pt, color=watchbord!25]
    (wp.south east) -- (zoombox.north east);
\end{scope}
\node[font=\fontsize{10}{12}\selectfont, text=watchbord!45, fill=white,
      inner sep=2pt] at ($(wp.south)!0.5!(zoombox.north)$) {\faSearchPlus};
```

- **Consistent flow direction.** Left-to-right for the main pipeline, top-to-bottom for branches/fallbacks. Never reverse direction mid-row.
- **Use absolute coordinates** for primary node placement (e.g., `at (5.0, 0)`) to maintain a clean grid. Use `positioning` library (`below=8pt of node`) only for labels and annotations.
- **Group related nodes** with a `fit` box on the background layer. Place the group label as a separate node centered on `zoombox.north` with `fill=white` so it sits on the border cleanly.
- **Interface labels outside grouped boxes.** Input/output arrows of a module should start/end at the group border, not at internal nodes. Labels go above the arrows, outside the box:

```latex
\coordinate (inputstart) at ([xshift=-36pt]zoombox.west |- zerr);
\draw[->, ...] (inputstart) -- (zoombox.west |- zerr);
\node[..., above=1pt] at ($(inputstart)!0.5!(zoombox.west |- zerr)$) {test errors};
```

- **Compact spacing.** Keep gaps tight: ~3.4--3.6cm between node centers horizontally, ~1.7--1.9cm vertically for branches. Reduce `inner xsep` and `inner ysep` on group boxes to 12pt and 16pt respectively. Too much whitespace wastes page space and weakens visual grouping.

### Node Styling

- **Minimum dimensions.** Primary nodes: `minimum width=2.4cm, minimum height=0.85cm`. Secondary/small nodes: `minimum width=2.0cm, minimum height=0.75cm`.
- **Rounded corners=3--4pt** on all rectangles. Match with the rounded corners on connectors.
- **Decision diamonds:** `aspect=2.2` makes them wide enough to fit "pass?" text without looking cramped.
- **Outcome badges:** Smaller than regular nodes (`minimum height=0.5cm, minimum width=1.1cm`), with icon + text: `{\faCheckCircle}~Pass`.
- **Dashed borders for contributions.** Novel/proposed modules use `draw, dashed, line width=1.1pt` to visually distinguish them from standard components.
- **Developer analogy annotations.** Small italic text below agent nodes connecting to real-world practice: `{\faUser}~{\itshape like a dev using browser DevTools}`. Use the agent's border color. Font size 5.5--6pt.

### Useful Specialized Packages

For common diagram types, prefer specialized packages over raw TikZ:

| Package | Use Case | Key Advantage |
|---------|----------|---------------|
| `tikz-cd` | Commutative diagrams, pipeline flows | Clean arrow syntax (`\arrow{r}{f}`), auto-layout |
| `forest` | Trees (parse trees, decision trees, file hierarchies) | Bracket notation, auto-spacing |
| `smartdiagram` | Quick circular/flow/bubble diagrams | Zero-config presets, one-line syntax |
| `tikz-network` | Network/graph visualization | `\Vertex` + `\Edge` API, automatic styling |
| `tikz-dependency` | NLP dependency parsing arcs | Auto arc positioning, no overlaps |
| `nicematrix` | Colored/annotated matrices | `\Block` fills, named cells, dotted lines |
| `circuitikz` | Circuit diagrams | Full component library (R, L, C, op-amps) |
| `pgfgantt` | Gantt charts / timelines | `\ganttbar{label}{start}{end}` syntax |
| `algorithm2e` | Algorithm pseudocode | `\For`, `\If`, `\KwData` structured blocks |
| `pgf-pie` | Pie charts | `\pie{35/A, 25/B, ...}` one-liner |

### Reusable Style Template

Complete boilerplate for system diagrams:

```latex
\documentclass[border=6pt]{standalone}
\usepackage[T1]{fontenc}
\usepackage{tikz}
\usepackage[sfdefault]{inter}
\usepackage{fontawesome5}
\usetikzlibrary{arrows.meta, positioning, shapes.geometric,
                 fit, backgrounds, calc}

\begin{document}
\begin{tikzpicture}[
  font=\sffamily\fontsize{8}{10}\selectfont,
  >={Stealth[length=4.5pt, width=3pt]},
  flow/.style={->, line width=0.7pt, color=gray!60, rounded corners=3pt},
  flowok/.style={->, line width=0.7pt, color=green!50!black, rounded corners=3pt},
  flowerr/.style={->, line width=0.7pt, color=red!60!black, rounded corners=3pt},
  block/.style 2 args={
    rectangle, rounded corners=3pt,
    minimum height=0.85cm, minimum width=2.4cm,
    draw=#1, fill=#2, text=darkgray,
    line width=0.8pt, align=center,
  },
  decision/.style={
    diamond, aspect=2.2,
    draw=gray, fill=white, text=darkgray,
    line width=0.8pt, inner sep=1.5pt,
    font=\sffamily\fontsize{7.5}{9}\selectfont,
  },
]
% ... nodes and edges ...
\end{tikzpicture}
\end{document}
```

## 9. Design Principles Summary

1. **Perceptual accuracy over aesthetics.** Colors are chosen for distinguishability, not beauty.
2. **Consistent semantic mapping.** Red = bad, green = good, blue = input/system, gray = neutral. Never swap these.
3. **Figures are pre-rendered PDFs.** Design in Keynote/Figma, export PDF, crop in LaTeX. No raw TikZ for complex diagrams.
4. **Tables are tight and dense.** 7.5--8.5pt font, 3--5pt column separation, booktabs rules, gray sub-rules.
5. **LLM content is visually distinct.** Light gray background (`#F1F3F4`) + underline or blue text (`#0076BA`).
6. **Diff is green-on-mint / red-on-pink.** Universally understood addition/deletion encoding.
7. **Minimize chart junk.** No unnecessary gridlines, borders, or 3D effects. High data-to-ink ratio.
8. **Full-width figures dominate.** Use `figure*` with `\linewidth` sizing for maximum impact.
