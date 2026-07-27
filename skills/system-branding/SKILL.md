---
name: system-branding
description: Name computer science research systems. Generates memorable, concise system names (acronyms, portmanteaus, or short tags) from a technical description, then validates uniqueness via WebSearch against Google Scholar, GitHub, and DBLP.
---

# System Branding for CS Research

Generate and validate system names for computer science and computational social science research papers.

## Naming Constraints

- **Length:** 20 characters maximum. Shorter is better.
- **Phonetics:** Must be easy to pronounce aloud (presentations, conversation).
- **Domain fit:** Should sound like a CS/CSS system, not a consumer product.
- **Name the big picture, not an internal detail.** The name should convey the essence of the whole system, not a single module, hyperparameter, or implementation trick. A reader who sees only the name (on a slide title, in a citation, in a tweet) should form a roughly correct mental model of what the system does before reading the paper. Names that key on peripheral details fail this test.

  *Example:* **WatchPoint** for a feedback module in a coding agent that periodically watches task-completion progress at specific checkpoints. "Watch" and "point" are both standard terms; together they telegraph "periodic observation at checkpoints," so a reader roughly knows the function before opening the paper.

## Scale Tier (Pick Before Generating)

A name must match the scope of what it labels. Decide the tier first; it constrains which naming strategy is appropriate.

| Tier | Scope | Strategy | Goal | Examples |
| --- | --- | --- | --- | --- |
| **1. Functional** | Local module, CLI utility, single-purpose API | Literal, predictable | Zero ambiguity, immediate clarity | `ripgrep`, `fzf` |
| **2. Conceptual** | Framework, workflow engine, developer tool | Active metaphor | Build an intuitive mental map of the workflow | `Raycast`, `BelayCUA` |
| **3. Metaphorical** | Platform, distributed system, database, cloud architecture | Abstract or phonetic | Project scale, stability, prestige | `Docker`, `Kafka`, `Cassandra` |

- A tiny utility named like a platform sounds pretentious.
- A platform named like a utility sounds disposable.
- For most CS research systems, default to **Tier 2** (conceptual / active metaphor). Reach for Tier 3 only when the system is a multi-component platform.

## Linguistic Principles

Apply these on every candidate before validation.

### A. Hard consonants for operational rigidity

Names that carry **K, C, G, D, T, P, B** sound structural and load-bearing; names dominated by sibilants (`S`, `Sh`) or breathy `H` sounds feel unstable.

- Strong: **D**o**ck**er, **K**af**k**a, **G**i**t**, S**p**ar**k**, **Cl**i**ck**House.
- Weak: anything where every syllable is a soft fricative.

This complements the "easy to pronounce" rule in *Naming Constraints* — easy *and* hard-edged beats easy *and* mushy.

### B. The Standup Test

A non-native English speaker must be able to say the name cleanly on the first try, in a meeting, without resorting to an acronym. If the team will silently invent a shorter handle within a week (e.g., *Kubernetes → K8s*), the name failed the test. Read every candidate aloud five times fast before shortlisting it.

### C. Geography, mythology, and heritage for big systems

For Tier 3 names, ground the candidate in physical geography, celestial bodies, mythological figures, or historical architecture rather than literal software terms. This grants an abstract software stack a sense of permanence and decouples it from any single feature.

- Examples: **Cassandra** (mythological authority), **Trino** (crisp phonetics, no literal meaning), Apple's macOS line (**Mojave**, **Sonoma**).
- Avoid the inverse failure: do **not** pick a name whose dictionary meaning contradicts the system's purpose. *Apache Subversion* literally means "undermining authority" — the opposite of what you want for mission-critical version control.

## Naming Strategies

Try all three strategies below and present the best candidates from each.

### Strategy A: Acronym from a Descriptive Phrase

Derive an abbreviation from a phrase that accurately describes the contribution.

- The source phrase must use well-established technical terms.
- The phrase must make academic sense on its own — do not contort wording just to force a clever acronym.
- **No non-standard vocabulary to hit target letters.** If the phrase has to introduce invented words, obscure synonyms, or unnatural grammar to produce the acronym, drop the candidate. A forced acronym built on vocabulary the field does not use is worse than no acronym at all.

### Strategy B: Portmanteau / Word Aggregation

Combine two or three short words into a single compound name (e.g., *GraphFlow*, *NetSense*).

- Use this when an acronym feels forced.
- The meaning should be immediately apparent without explanation.

### Strategy C: Short Abstract Tag

Create a 3–4 letter all-caps tag (e.g., *BOLT*, *FLAN*).

- Acceptable even if the letters do not literally stand for anything.
- Must be distinct and visually clean in figures and tables.

## Validation (Required)

Before recommending any name, run the following checks:

1. **arXiv** — Search using the `quicksearch` MCP tool (preferred) or fall back to WebSearch with `"<name>" site:arxiv.org`. With `quicksearch`, call `mcp__quicksearch__search_papers(query="<name>")` then `mcp__quicksearch__get_paper_details(paper_id=...)` for each hit and read **both title AND abstract** — a title match alone may be a false positive; the abstract confirms whether the prior paper uses the name as a system/method name. Reject if it does.
2. **Google Scholar** — Search `"<name>" site:scholar.google.com` or equivalent via WebSearch. Reject if a well-known paper or system already uses the name in the same or adjacent field.
3. **GitHub** — Search `"<name>"` on GitHub via WebSearch. Reject if a popular repository (100+ stars) shares the exact name.
4. **DBLP** — Search `"<name>"` on dblp.org via WebSearch. Reject if a published system paper uses the name.
5. **CLI / library conflicts** — Reject names that collide with common command-line tools, package names, or reserved keywords.

Report the search results for each candidate so the user can make an informed choice.

## Pre-Lock Checklist

Run every surviving candidate through these four filters in order. Any "no" sends the name back to the strategies section.

1. **Tier match.** Is the candidate's style consistent with the system's scale (utility vs. framework vs. platform)?
2. **Standup Test.** Said aloud five times fast, does it stay punchy, or does it collapse into an acronym in your mouth?
3. **Hard-edged phonetics.** Does at least one plosive or velar consonant (K, C, G, D, T, P, B) carry the word?
4. **Lock-in cost is worth paying.** Renaming a system later means rewriting repos, schemas, citations, docs, and slide decks. Pick a name you can commit to today rather than chasing a marginally better one next month.

## Case Study: BelayCUA (5 rounds, ~30 candidates)

Real example of how the process runs end-to-end. Expect iteration; first-round candidates rarely survive.

**Round 1 — Strategy A, plain acronyms.**
Proposed: RHEA, MERIT, GAMUT, REGAL, CURB, VERGE, CRANE, TIDE, RECAP, GoalTrace, PlanTrace, TETHER, POISE, LEDGER.
Validation killed most: RHEA (Rolling Horizon Evolutionary Algorithm), REGAL (two existing agent papers), MERIT (multiple LLM systems), VERGE (verifiable LLM reasoning, 2026), CRANE (constrained LLM generation, ICML 2025), RECAP (Recursive Context-Aware Planning for LLM agents, 2025), TIDE (multiple LLM systems).
Survivors (TETHER, POISE, GAMUT, CURB) rejected by user: "trying too hard, mouthful and non-established words put together."
**Lesson:** forced acronyms from non-standard vocabulary fail, even after validation.

**Round 2 — Strategy B, real-word compounds.**
Proposed: TreadBack, SureFoot, FootHold, HoldFast, CrumbTrail, PlanSlide.
Validation killed WatchStep (direct conflict with "Watch Every Step!" EMNLP 2024) and PathFold (space saturated by FoldAgent, AgentFold, FoldAct, FoldPath).
User feedback: earlier candidates "capture only one ingredient"; the system needed **cautious-step + reversibility + goal-anchor together**.
**Lesson:** a good name must carry every key ingredient of the system, not just one.

**Round 3 — Strategy B, all ingredients in one word.**
Aimed for compounds where one term does triple duty. Proposed: TackBack, AnchorStep, TetherStep, MoorAgent, CrumbStep, InchBack, PeekStep.
Validation killed AnchorAgent late (WebAnchor + Anchor-GRPO in the same agent-planning space).
User asked for the **[Word]Agent** pattern (field convention: BacktrackAgent, VerificAgent, ProactiveAgent).
**Lesson:** match the field's naming convention early; re-check the surrounding literature for suffix trends.

**Round 4 — [Word]Agent pattern.**
Proposed: BelayAgent, TackAgent, TetherAgent, MoorAgent, TreadAgent, CrumbAgent, CinchAgent.
**Belay** carried all three ingredients in one technical term: anchored to a fixed point, advance one careful action at a time, rope catches a fall and permits retreat.
User pointed out: "none of these signal CUA work."
**Lesson:** a metaphor that fits the behavior still needs a **domain marker** so readers know the application area.

**Round 5 — Metaphor + domain marker.**
Combined the metaphor with the field's emerging suffixes (GUI, Click, OS, CUA — cf. ShowUI, SeeClick, ClickAgent, OS-Atlas, UI-TARS, VeriGUI, TreeCUA, UltraCUA).
Proposed: BelayGUI, SureClick, ClickBack, TackGUI, CrumbGUI, TreadGUI, **BelayCUA**.
**Final pick: BelayCUA.** Belay names the exact behavior (anchored goal, verified action-at-a-time, rewind to a known-safe state); CUA plants it in the family alongside UltraCUA and TreeCUA. No published collision.

**Takeaways for the agent running this skill:**

1. Plan for **≥3 rounds**. A single shortlist almost never contains the final name.
2. After each round, **summarize why each survivor was rejected** and feed that back into the next round's generation.
3. Validation (arXiv/Scholar/GitHub/DBLP) is not optional — it killed roughly half the Round-1 candidates here.
4. When the user says "trying too hard" or "captures only one ingredient," shift strategy (A → B, or broaden the metaphor) rather than producing minor variants of rejected names.
5. Name must encode: the **behavior** (what the system does) + the **domain marker** (what field it works in). A name that does one but not the other is incomplete.

## Output Format

Present results as a ranked shortlist:

```
## Candidates

| Rank | Name | Strategy | Source Phrase / Rationale | Conflicts Found |
|------|------|----------|--------------------------|-----------------|
| 1    | …    | A/B/C    | …                        | None / …        |
| 2    | …    | A/B/C    | …                        | None / …        |
| …    | …    | …        | …                        | …               |
```

Include 5–8 candidates. Flag any with potential conflicts but let the user decide.
