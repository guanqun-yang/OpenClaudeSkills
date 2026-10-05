---
name: paper-summary
description: Summarize academic paper PDFs into structured two-section deep dives with executive summary and method deep dive. Use when the user provides PDFs to summarize.
argument-hint: <pdf-path-or-glob>
---

# Paper Summary Skill

Read academic paper PDF(s) and produce a structured two-section summary for each.

## Audience

Write for a **CS undergraduate** whose background is:

- **Comfortable with:** algorithms 101 (Big-O, sorting, graph traversal, dynamic programming), and the 101 level of ML / DL / RecSys (gradient descent, backprop, attention, embeddings, train/val/test split, accuracy/F1, collaborative filtering vs. content-based).
- **Shaky on:** advanced statistics (Bayesian inference, measure theory, causal identification, hypothesis-testing nuances), and niche subfields. Assume **no working knowledge** of OS, computer networks, cryptography, computer graphics, or hardware internals beyond name recognition (e.g., "TLB" or "GPU memory hierarchy" may ring a bell but the precise definition does not).

When the paper depends on a concept outside the comfort zone, define it in **one short clause** before using it — e.g., *"a Merkle tree (a hash tree where each parent node hashes its children)"*. Do not link out; inline the gloss. Do not gloss concepts already inside the comfort zone — defining "gradient descent" insults the reader.

## Plain English

- **Prefer the everyday word** when it is technically equivalent. "Speeds up training" beats "accelerates the optimization trajectory."
- **Unpack jargon on first use.** Use the jargon term afterwards so the reader learns it, but never on its own first.
- **Short sentences.** One claim per sentence. Split anything with two `,` clauses or an "and" that joins two ideas.
- **Concrete over abstract.** Replace "the system" with the actual name. Replace "various datasets" with the dataset names.
- **Technical accuracy is not negotiable.** Plain English means simpler words and shorter sentences — never weaker claims, hand-waving, or dropped quantifiers. If a simplification would change the math, keep the math.

### Rules from ASD-STE100

A paper summary has the same job as a maintenance manual: a reader who is not an expert, and often not a native English speaker, has to follow a procedure without misreading it. [ASD-STE100](https://www.asd-ste100.org/) is the controlled language written for that job. Four of its rules close gaps the list above leaves open. Each is measured on 26 real summaries from this skill, 37 K words with math and Chinese stripped.

- **Name the actor; use the active voice** (STE 3.6). Measured at 60.3 passive constructions per 10 K words, the largest gap in current output. A method description in the passive hides who or what performs the step, which is the one thing the reader needs. *"Topics are described by their top feature descriptions"* becomes *"The method describes each topic by its top feature descriptions."* The passive is correct only where the agent is genuinely unknown or irrelevant, which in a method section is rare.
- **At most three words before the head noun** (STE 2.1 and 2.2). Measured at 23.9 hyphenated compounds per 10 K words, twice the rate in human technical blogs. *"Retrieval-augmented generation pipeline component"* makes the reader work out which of four modifiers attaches to *component*. Write the relation out, or hyphenate only the pair that acts as one unit.
- **Give information gradually; use a vertical list for anything enumerated** (STE 6.1 and 4.3). When a sentence defines three or more items, it becomes a list. One real example from the corpus packs three slice definitions and their formulas into 39 words; as three bullets it is readable without a second pass.
- **One term per concept** (STE 1.11). Having introduced *slice*, never switch to *subgroup*, *cohort*, or *segment* for the same thing. Synonym rotation is a readability defect here, not variety: the reader cannot tell whether a new word means a new concept. This matters most where the paper itself is inconsistent; pick the paper's dominant term, say so once, and keep it.

**Sentence length is a target, not a cap.** STE allows 25 words in descriptive text, and 9.7 % of current sentences exceed it against a median of 14. Treat 25 as the point where you check whether the sentence holds two claims, not as a number to trim a necessary qualifier to reach. A 30-word sentence that states one thing precisely beats two short ones that lose the condition.

**Not taken from the standard:** the approved-word dictionary (rule 1.1), the ban on `-ing` forms (3.5), the ban on contractions (4.2), the five permitted tenses (3.2), and the ban on semicolons (8.1). Those buy unambiguity by giving up ordinary English, which is the right trade for a maintenance manual and the wrong one here. The phrasal-verb ban (9.3) is omitted for a different reason: at 1.3 per 10 K words, this skill's output already has almost none.

## Input

`$ARGUMENTS`: Path to a PDF file, a glob pattern (e.g., `resources/*.pdf`), or a directory containing PDFs.

If multiple PDFs, launch parallel agents (2 PDFs per agent) to read them concurrently.

## Output Format

For each paper, produce the following two sections. **Each field must start on its own line with a blank line before it** so that Markdown renders them as separate paragraphs (not one merged block).

### Section 1: Executive Summary

```markdown
**Problem:** What problem the authors are trying to solve. Be specific and concise.

**Proposed method:**

- **Input:** Formal description using math notation ($x$, $\mathcal{D}$, etc.) or code.
- **Key formulation:** The core algorithm/formula. Use display math ($$...$$) for important equations.
- **Output:** What the method produces.

**Baselines:** List what the authors compare against.

**Results:** Quantitative results with specific numbers. Use markdown tables when comparing multiple methods/benchmarks. Always name the base model explicitly (e.g., "CodeLlama-34B", not "a large model").

**Context:** Situate the work — venue/year, whether it's foundational or incremental, and how it relates to the broader field.
```

### Section 2: Method Deep Dive

If the proposed method is a multi-step pipeline, document **every step** as a bullet point:

```markdown
- **Step 1: {Step name}** — What goes in, what happens (hyperparameters, loss functions, architecture details), what comes out.
- **Step 2: {Step name}** — ...
- **Step 3: {Step name}** — ...
```

For complex steps that need more detail, expand into sub-bullets:

```markdown
- **Step 1: {Step name}**
  - **Input:** What goes in.
  - **Process:** What happens (be precise).
  - **Output:** What comes out.
```

Cover the full pipeline, not just the novel parts.

## Formatting Rules

These rules prevent rendering issues in `publish.py` and common Markdown renderers.

### Blank lines between fields (CRITICAL)

Every `**Field:**` must be preceded by a blank line. Without it, consecutive fields merge into one paragraph:

```markdown
<!-- WRONG: renders as single paragraph -->
**Problem:** Text about the problem.
**Method:** Text about the method.

<!-- CORRECT: renders as separate paragraphs -->
**Problem:** Text about the problem.

**Method:** Text about the method.
```

### Steps must be bullet points (CRITICAL)

Never put multiple steps on one line. Each step must be a separate `- ` bullet:

```markdown
<!-- WRONG: renders as unreadable wall of text -->
**Step 1:** Do X. **Step 2:** Do Y. **Step 3:** Do Z.

<!-- CORRECT: renders as a clean list -->
- **Step 1:** Do X.
- **Step 2:** Do Y.
- **Step 3:** Do Z.
```

### Foldable wrapper for blog appendices

When writing summaries inside `<details>` blocks for blog appendices, use this pattern:

```html
<details markdown="1">
<summary><b>Paper Title Here</b> (Author et al., Year)</summary>

### Executive Summary

**Problem:** ...

**Method:** ...

**Results:** ...

**Context:** ...

### Method Deep Dive

- **Step 1: {name}** — ...
- **Step 2: {name}** — ...

</details>
```

Key points:
- `markdown="1"` on the `<details>` tag is required for Markdown inside HTML blocks.
- Do NOT use `<span style="color:...">` in summary titles unless the user specifically requests color coding. The section heading identifies the category.
- `### Executive Summary` and `### Method Deep Dive` render as `<h3>` inside the foldable.

### Math and LaTeX

- Use `$...$` for inline math and `$$...$$` for display math.
- Reproduce key formulas exactly from the paper — do not paraphrase math into plain English.
- Do NOT use LaTeX color commands (`$\color{blue}{\textsf{...}}$`) — they don't render in HTML. Use HTML `<span style="color:...">` if color is needed.

## Quality Checklist

- [ ] Every formula uses LaTeX math (`$...$` or `$$...$$`)
- [ ] Every `**Field:**` label is preceded by a blank line
- [ ] Every step is a separate `- ` bullet point, never inline
- [ ] Results include specific numbers and named models/benchmarks
- [ ] Method deep dive covers ALL pipeline steps
- [ ] If wrapped in `<details>`, the tag has `markdown="1"`
- [ ] Every concept outside the undergrad comfort zone (advanced stats, OS, networks, crypto, graphics, hardware) is glossed inline on first use
- [ ] No sentence relies on jargon that has not been unpacked
- [ ] Plain English used throughout — short sentences, one claim each, concrete names — without weakening any technical claim
- [ ] Every step names the actor that performs it; the passive appears only where the agent is genuinely unknown
- [ ] No noun phrase stacks more than three words before its head noun
- [ ] Any sentence defining three or more items is a vertical list instead
- [ ] One term per concept throughout, even where the paper alternates
