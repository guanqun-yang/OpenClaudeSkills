---
name: humanize
description: Make Claude-written prose read as human. Budgets and rewrites for the tics that actually show up under measurement - "rather than", definition by negation, copular framing and the "X is Y, and Z is W" couplet, counting reflexes, em dashes, missing commas after openers, and bold/table scaffolding. Calibrated on 520K words of Claude prose against register-matched human corpora.
---

# Humanize

Apply when writing or revising prose a person will read: blog posts, notes, papers, rebuttals, README bodies, reports, emails. Not for code, and not for chat replies in the terminal.

The rules below are calibrated, not guessed. They come from a survey of 520 K words of Claude-written prose (676 files across 185 sessions) measured against 820 K words of register-matched human prose: pre-2023 technical blogs, trade non-fiction, and ACL/EMNLP papers. Numbers cited as *(Claude 4.3, human 0.24)* are occurrences per 1 000 words in that survey.

## 1. Do Not Bother Banning the Famous Words

Under measurement, none of the internet's AI-slop vocabulary appears in Claude's prose at above-human rates:

| Marker | Claude | Human blogs | Human papers |
|---|---|---|---|
| *delve* | 0.00 | 0.00 | 0.01 |
| *moreover* | 0.00 | 0.04 | 0.20 |
| *furthermore* | 0.00 | 0.04 | 0.13 |
| *leverage* (verb) | 0.02 | 0.02 | 0.32 |
| *it's worth noting* | 0.00 | 0.00 | 0.02 |
| *not just X but Y* | 0.02 | 0.03 | 0.06 |
| *, ensuring / allowing / enabling* | 0.02 | 0.03 | 0.07 |
| *myriad / tapestry / testament to* | 0.00 | 0.00 | 0.00 |

Spending attention here buys nothing. The real tics are syntactic and structural, and they are all in the sections below.

## 2. Budget Card

Per 1 000 words of finished prose. The middle column is what Claude does unprompted; the right column is the ceiling to write to.

| Feature | Claude does | Budget | Human baseline |
|---|---|---|---|
| `rather than` | 1.7 | **≤ 0.3** (about one per document) | 0.19 |
| Negation frames (`not a`, `with no`, `there is no`, `none of`, `at all`) | 3.3 | **≤ 1.0** | 0.8 |
| Copular identification (`X is the Y`, `which is why`, `is what`, `is the only`) | 6.1 | **≤ 3.0** | 1.9 |
| Counting absolutes (`every`, `all three`, `exactly`, `the two`) | 3.7 | **≤ 1.5** | 1.1 |
| Em dash | 4.3 | **≤ 1.0** | 0.24 |
| Semicolon | 7.7 | **≤ 3.0** | 2.9 |
| Mid-sentence colon | 11.6 | **≤ 6.0** | 5.3 |
| Arrow (`→`, `->`) in running prose | 1.0 | **0** | 0.08 |
| Hedges (`may`, `often`, `typically`, `tends to`) | 1.0 | **≥ 2.0** | 2.9 |

Page furniture, per 100 prose blocks (a block is one paragraph or one bullet):

| Feature | Claude does | Budget | Human baseline |
|---|---|---|---|
| Bold spans | 73 | **≤ 15** | 7–10 |
| Table lines | 38 | **≤ 5** | 0.2–0.9 |
| Bullets with a bold lead-in | 25 % of bullets | **≤ 10 %** | rare |
| One-sentence paragraphs | 41 % | **≤ 20 %** | — |
| Mean sentences per paragraph | 2.1 | **≥ 3.0** | — |

Bullet share itself is fine: Claude runs 38 % of blocks as bullets, human technical bloggers run 44 %. Cut the bold and the tables, not the lists.

## 3. The Contrast Reflex

`rather than` is the single strongest tell in the survey: 9× human technical blogs, 13× human papers, and steady across every document type. Claude reaches for it to say a thing by fencing it off from a neighbouring thing the reader was never considering.

Three fixes, in order of preference.

**Delete it.** Most of the time, the rejected alternative is not live for the reader.

> **Don't:** The shorter window strengthens that call rather than weakening it.
> **Do:** The shorter window strengthens that call.

**Give the alternative its own sentence,** when the contrast is the point.

> **Don't:** Define the action space at the level FeatGEO used, structural and content features, rather than free-form token rewriting.
> **Do:** Define the action space the way FeatGEO did, over structural and content features. Token-level rewriting is a different problem and out of scope here.

**Name the choice, not the rejection.** If two options are genuinely on the table, say who prefers which and why, in the ordinary way: *A over B*, *A instead of B*, *we picked A because*.

The same reflex hides in `not X but Y`, `less about X than Y`, `it's not that X, it's that Y`. All of them front-load a negative the reader has to hold before the positive arrives.

## 4. Definition by Negation

`not a`, `with no`, `there is no`, `none of`, `at all`, `nothing`, `cannot` all run about 4× human. Any one of them is fine. The tell is the density: paragraph after paragraph that establishes what is absent.

> **Don't:** A tool contribution, not a methodological or empirical advance: it introduces no new algorithm, no new fairness metric, and reports no user study.
> **Do:** This is a tool contribution. The algorithm and the fairness metric both come from prior work, and the evaluation is a walkthrough on two public datasets.

> **Don't:** With an Amazon-only brand there is no factory spec to check against.
> **Do:** Amazon-only brands publish loft and lie themselves, so the spec you check is the seller's.

The test: does the reader currently believe the thing being negated? If yes, negate it. If not, state what is there.

Where absence really is the finding, say it once, plainly, and move on. "Prior audits disagree and there is no standardized test bed" is a good sentence. It becomes a tic when the next three sentences also start from what is missing.

## 5. Copular Identification

`X is the Y`, `this is the`, `which is why`, `is what`, `is the only` run 3–10× human. The copula tells the reader what something *is*; a verb tells them what it *does*, which is nearly always the more useful sentence.

> **Don't:** Knowing that the standard answer breaks, and being able to say why, is the point of the follow-up.
> **Do:** The follow-up asks whether you know the standard answer breaks, and whether you can say why.

> **Don't:** It is the only option where you can hold six used 7-irons, hit each one, and walk out under USD 100.
> **Do:** Everywhere else, you order blind. There, you can hold six used 7-irons, hit each one, and walk out under USD 100.

> **Don't:** That is the paper's central claim, and the honest form of it is parity.
> **Do:** The paper claims parity. Table 3 supports that reading.

`which is why` deserves its own mention: it welds a consequence onto a sentence that had already finished. Break it into two sentences or use *so*.

## 5b. Abstractions as Actors

The copula rule above says to prefer a verb. The failure mode it does not catch is giving that verb to a subject that cannot act. Claude writes *the argument carries*, *the comparison places*, *the ordering holds*, *the column decides*, *the analysis shows*, and the reader has to work out who actually did the thing.

This one does not show up in any word count, so it survives every other pass in this file. It is also the tic most likely to make a sentence genuinely hard to parse for a reader working in a second language, because the metaphor and the missing agent compound.

> **Don't:** Five label budgets across three datasets, each with a supervised anchor trained at the same budget, place the comparison where annotation cost binds.
> **Do:** The authors label 1, 5, 10, 50, and 100 percent of the training data. At each budget, they also train a plain supervised model.

> **Don't:** N1 carries the argument at 29.3 against 24.0 for the strongest baseline.
> **Do:** On stage N1, the model reaches 29.3 F1, against 24.0 for the best baseline.

The test: ask who or what performed the verb. If the answer is a person, a system, a model, a paper, or a table, the sentence is fine. If the answer is an argument, a comparison, an ordering, a budget, or an analysis, rewrite with the real actor in front.

A second pattern travels with it: a short cryptic sentence followed by a colon and a longer sentence that explains it. Split it into two sentences, put the explanation first, and drop the colon.

## 5c. The Copular Couplet

Two short copular clauses joined by *and*, the first stating a fact and the second passing a verdict on it: *The problem is one wrong field, and the fault is mine.* *The fix is small, and the risk is low.* *The answer is no, and the reason is cost.* Section 5 already flags each half. The couplet is worse than the sum, because the balance itself is the tell: it reads as a line composed to be quoted, and Claude produces it as a default way to open or close a paragraph, especially in emails and summaries. It was not measured in the survey; it was added on 16 September 2026 after a reader flagged it in an email draft. Treat the budget as zero.

The test: the sentence has the shape *the N is N, and the N is N* or *N is A, and N is A*, and the two halves could swap places without loss. A sentence-final verdict tail does the same job in one clause: *..., and that is the honest reading*, *..., which is the whole point*, *..., and that is the problem*.

Fix: give the fact a verb and an agent. Then either drop the verdict, because the fact now carries it, or let the verdict be a plain sentence of its own.

> **Don't:** The problem is one wrong field, and the fault is mine.
> **Do:** When I committed the paper, I entered one field wrong, and that mistake caused everything below.

> **Don't:** The fix is small, and the risk is low.
> **Do:** The fix changes one line and touches nothing else.

> **Don't:** A rejection would be a usable answer, and silence is the only one I cannot act on.
> **Do:** I can act on a rejection. Silence gives me nothing to act on.

## 6. Counting and Absolutes

`every`, `all three`, `exactly`, `the two`, `the only` run 3–11× human. The enumerative reflex reads as machine-tidy because real writers rarely notice that their reasons happen to number three.

> **Don't:** Three properties make it work, and all three are worth protecting. Every post is a folder, not a file.
> **Do:** A post is a folder, with the body in `README.md` inside it. That is what makes the other two properties possible.

Concretely: do not announce a count before a list unless the count is load-bearing. Do not close a list by referring back to its cardinality (*all three*, *both of these*, *each of the four*). Do not write *every* where *a* or *the* will do.

## 7. Punctuation That Is Doing Syntax's Job

Em dashes are 17× human technical blogs, and the distribution matters: 59 % of Claude's longer documents contain none at all, while planning notes run 66 per 10 K words. It is a mode, not a constant. When a draft is over budget, it is usually over budget badly.

> **Don't:** Its spread is 63.2 to 64.2 — one point — while Table 2 reports a seed-level standard deviation of 0.5.
> **Do:** Its spread is 63.2 to 64.2, one point, while Table 2 reports a seed-level standard deviation of 0.5 for the same configuration.

> **Don't:** The MCP server — the primary way this project is used — lives at `tests/mcp/`, which is both wrong and brittle.
> **Do:** The MCP server is the primary way this project is used, and it lives under `tests/mcp/`. That location is both semantically wrong and brittle.

The same applies to the mid-sentence colon (2.2×) and the semicolon (2.6×). Each is a device for cramming a second clause into a sentence that had finished its job. Ask whether the material after the mark is a gloss (use a comma), a consequence (use a new sentence), or a list (keep the colon).

Arrows in running prose (`x -> y`, `→`) read as notation. Keep them in tables, diagrams, and pipelines; spell them out in sentences.

### 7b. The Comma After an Opener

Claude drops the comma after an introductory phrase: *As a result the chairs see the wrong forum.* *On 11 September 2026 I asked the General Chair.* *In the three runs reported the gap closes.* Put the comma in, every time:

- after a conjunctive adverb or a sentence adverb: *As a result,* *However,* *In other words,* *For example,* *In practice,*
- after an introductory phrase that carries a date, a place, a condition, or a scope: *On 11 September 2026,* *At each budget,* *Under the signed contract,* *For a week,*
- after a dependent clause: *If the folder does not exist,* *When a draft is over budget,*

Some style guides allow the comma to be omitted after a very short prepositional phrase (*In 2024 we moved*). Do not take that permission. The readers of these documents are often parsing in a second language, and the comma marks where the subject of the sentence begins; without it, *On 11 September 2026 I asked* makes the reader find the boundary themselves. This rule was not measured in the survey; it was added on 16 September 2026 from the same reader feedback as section 5c.

## 8. Certainty and Conversational Repair

Claude hedges at **one third** the human rate in every baseline, and leaves out the connectives humans use to slow down and repair:

| | Claude | Human blogs | Trade books |
|---|---|---|---|
| Hedges | 1.0 | 2.9 | 2.8 |
| `But` sentence-initial | 0.16 | 0.46 | 1.9 |
| `let's` / `we'll` | 0.38 | 1.6 | 1.6 |
| `in other words` / `simply put` | 0.00 | 0.05 | 0.15 |

So the correction is *not* "be more direct". It is the opposite:

- Where a claim rests on one benchmark, one source, or one reading, put that in the sentence: *on this benchmark*, *in the three runs reported*, *as far as the logs show*.
- Use *usually*, *often*, *tends to* when the claim is a tendency. Claude states tendencies as laws.
- Let *But* start a sentence. Let *In other words* restate something the reader may not have caught the first time.
- Attribute. *The authors argue*, *the docs claim*, *I could not reproduce* all carry more information than a flat assertion does.

## 9. Page Furniture

Bold is 10× human and tables are roughly 190× human. Both are ways of avoiding the work of a paragraph.

- **Bold** marks a term the reader must retain, once, at first use. It does not mark the first three words of every bullet, and it does not mark a phrase for emphasis mid-sentence. If a bulleted list has a bold lead-in on every item, the list wants to be a table or a set of short paragraphs.
- **Tables** are for data with two or more real dimensions. Three rows of prose with a colon in each are not a table.
- **Headings** every few paragraphs turn an argument into a directory listing. Use them where a reader would want to jump; not as a substitute for a transition.
- **Paragraphs** should carry three or four sentences. The one-sentence punchline paragraph is fine once or twice per document, and Claude currently uses it in 41 % of paragraphs.
- **Lists** should be roughly parallel and roughly complete. Do not pad to three, and do not split one thought across two bullets so the list looks fuller.

## 10. Register

Not every rule applies everywhere. In LaTeX, the template already suppresses the punctuation and furniture habits (measured em dash 0.04 per 1 000 words, no bold, no markdown tables), but the syntactic reflexes survive intact and in fact get worse (`rather than` at 13× the rate in real papers).

| Rule | Markdown notes, blogs, READMEs | LaTeX papers | Email |
|---|---|---|---|
| §3 contrast, §4 negation, §5 copula, §6 counting | apply | apply, most important here | apply |
| §7 punctuation | apply | already suppressed by the template | apply |
| §8 hedging and repair | apply | apply, with attribution rather than *I* | apply |
| §9 furniture | apply | not applicable | keep to a single short list |

Trade and narrative prose is the one place where the punctuation budget loosens: professionally edited non-fiction runs 5.5 em dashes per 1 000 words, higher than Claude. If the target register is a book chapter or an essay, §7 is advisory. Everywhere else it is the rule.

## 11. Revision Pass

Given a finished draft, work in this order. Highest yield first, and each pass is mechanical enough to do without re-reading for meaning.

1. Count em dashes, `rather than`, semicolons, and arrows. Any over budget gets fixed before anything else. These are the cheapest and most visible wins.
2. Strip bold to terms at first use. Convert any all-bold-lead-in bullet list to plain sentences or to one real table.
3. Merge one-sentence paragraphs into their neighbours until the mean is three or more sentences.
4. Read only the sentences that contain `is`, `are`, `was`, `were`. Rewrite the ones where a real verb was available (§5). While there, catch every *N is N, and N is N* couplet and every *, and that is* tail (§5c).
5. Read only the sentences containing `no`, `not`, `never`, `none`, `nothing`. Keep the ones that correct a belief the reader actually holds (§4).
6. Delete every count that is not load-bearing (§6).
7. Add the hedges and attributions back where the claim rests on one source (§8).
8. Read the first sentence of each paragraph in sequence. If they form a list of definitions, the draft is still a glossary, not an argument.
9. Search for sentence openers (`As a result`, `In other words`, `On <date>`, `At <time>`, `If`, `When`, `Under`) and confirm each is followed by a comma (§7b).

A quick numeric check on a file, if useful:

```bash
w=$(wc -w < FILE)
rg -o -- '—' FILE | wc -l          # budget: w/1000 * 1
rg -oi -- 'rather than' FILE | wc -l  # budget: w/1000 * 0.3
rg -o -- '\*\*[^*]+\*\*' FILE | wc -l # budget: 15 per 100 prose blocks
```

## 12. Do Not Overcorrect

- Do not delete tables that hold real data. The problem is prose reformatted as a table, not tabulation.
- Do not remove every em dash. One per thousand words is human; zero reads as stilted.
- Do not add hedges to claims that are actually certain. A measured number is a measured number.
- Do not swap the banned constructions for synonyms of themselves. Replacing `rather than` with `as opposed to` fixes the count and none of the writing.
- Do not chase burstiness. Claude's sentence-length mean (21.9 words) and variance already sit inside the human range; sentence length is not the tell and does not need engineering.
