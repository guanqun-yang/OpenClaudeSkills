---
name: minto
description: Structure a document as a Minto pyramid before writing it, or reverse-engineer a draft into one and repair it. One reader Question, a Situation-Complication introduction, Key Line groups ordered by time, structure or degree and summarized by their insight. Memos, Slack messages, reports, proposals, papers, rebuttals.
argument-hint: <topic, draft path, or "polish <path>">
---

# Minto

The method from Barbara Minto's *The Pyramid Principle*, reduced to what can be checked. Apply when writing anything a reader has to follow as an argument. On the business side: a Slack or email message that asks for something, a memo, an approval request, a decision document, a proposal, a status review, a report. On the academic side: a paper's abstract and introduction, a project note, a rebuttal, a grant narrative. Not for code, and not for Claude's own replies in the terminal.

The claim behind the method is that clarity comes from the order of the ideas, not from the sentences. Minto's own before/after memos differ hardly at all in wording. So this skill front-loads a structure step and makes it visible; a document that skipped that step has not used the skill. The visible outline is skipped only for messages under about 150 words, where the pyramid is built silently and the reader sees the Answer in the first line. Wording is handled afterwards by `humanize`, which runs last.

The pyramid is the same in both registers. What differs is where its parts land on the page, which §9 spells out; a paper hides the Key Line in a contribution list under headings the venue fixed, a Slack message *is* the Key Line with no headings at all.

## 1. The Pyramid in One Page

A document makes one point, and that point answers one question the reader already has. Everything below exists to explain or defend the point above it.

| Rule | Test |
|---|---|
| Every point summarizes the group under it | Cover the group; can the reader predict it from the point alone? |
| Every group is the same kind of idea | Name the group with one plural noun: *reasons*, *steps*, *changes*, *criteria*, *risks* |
| Every group is in a logical order | Say why the second item is second. Time, structure, or degree; nothing else |

**Vertically**, each point raises a question in the reader's mind (Why? How? Which? So what?) and the group below answers it. Nothing gets answered before it is asked, and nothing gets asked without an answer on the next line down.

**Horizontally**, a group answers in one of two ways and never both at once:

- *Deductive*: a statement, a second statement that comments on the first, and a "therefore". At most four points; the summary above rests on the last one. Easy to follow in a paragraph, tedious across ten pages, so push deduction down the pyramid.
- *Inductive*: several ideas of the same kind, and an inference about what their similarity means. At most five points. Use this on the Key Line unless the reader cannot accept the Answer without first walking the reasoning.

## 2. Workflow A: Write

Top-down first. Bottom-up only when the top will not come.

### Top-down

1. **Subject.** One noun phrase.
2. **Reader and Question.** Name the reader. Write the single question they have about the Subject, in their words. Two questions must collapse into one (*should we, and if so how* is *how*, since *no* ends the document). Then write the reader's stake and their power relative to you in one line each. If the reader can refuse, the document is an approval request whatever the writer feels about the history, and the Answer is a question the reader can say yes to.
3. **Answer.** One sentence with the Subject as its subject. This is the top of the pyramid.
4. **Situation.** The first thing about the Subject the reader will accept without argument. If nothing comes, the Subject is wrong or the story starts in the wrong place.
5. **Complication.** What happened inside that Situation to raise the Question. Now check: does Situation plus Complication produce exactly the Question written in step 2? If not, change the Question or the Complication until they match. This check is the whole point of the exercise.
6. **New question.** State the Answer to the reader and write down what they ask next. Almost always *Why?* (→ reasons) or *How?* (→ steps). Name the plural noun.
7. **Key Line.** The points that answer the new question. Each is a full idea sentence, not a topic. Five at most, in an order you can defend (§4).
8. **One level down.** Under each Key Line point, the group that answers its question. Stop structuring here and write; lower levels arrive as you draft.

Write the result as an indented outline and show it. For anything longer than a page, wait for the user's confirmation before drafting prose. The outline is what gets argued about; prose written before it is agreed tends to get defended instead of fixed.

```
Q  (VP Engineering): Should I approve the second on-call rotation?
A  Yes: a second rotation is the only fix that clears the pager backlog this quarter.
   S  One rotation of six engineers has covered production since March.
   C  Pages have doubled since the EU launch; two people have burned out.
   why? → reasons
   1. Backlog cannot wait: SLA breaches started in week 3 and cost credits.
   2. A second rotation halves pages per person; no other option does.
   3. Cost is two headcount-months, under the credits already paid.
   4. It also gives EU customers a same-timezone responder.
```

```
Q  (reviewer of a retrieval paper): Is the hybrid index worth its cost?
A  Hybrid retrieval pays for itself on long queries and nowhere else.
   S  Dense retrieval is the default in our pipeline.
   C  Adding a BM25 leg doubled index size and raised p95 latency 40 %.
   why? → reasons
   1. On queries over 12 tokens it lifts nDCG@10 by 6 points (Table 2).
   2. On short queries the lift is inside seed variance.
   3. Routing by query length keeps 90 % of the gain at 15 % of the cost.
```

### Bottom-up

When the Subject or Question refuses to come clear:

1. List every point you might make, one line each.
2. Find the relationships. Which are causes and which effects? Which are parts of one structure? Which are members of one class? Which say the same thing twice?
3. Draw the conclusion each cluster implies.
4. Work backwards: why would the reader need these conclusions? That is the Question. What situation made them ask it? That is the introduction.

Then return to the top-down list at step 6.

## 3. Introductions

An introduction reminds; it does not inform. Everything in it is something the reader already knows or will accept as plainly true. Evidence, tables, and new claims belong in the body. All history and chronology belong in the introduction, because the body can hold only ideas, and a sequence of events is not an idea.

**No grievance.** A log of who failed to reply, and when, is chronology the reader does not need in order to act; it belongs in your own notes. The same goes for a sentence explaining why each person is copied, and for any sentence whose job is to show the reader that you have been patient. Include only the facts the reader must accept in order to say yes. This was added on 16 September 2026 after a draft escalation email put a week of unanswered messages into its introduction and read, to its reader, as a public complaint.

**Length** is whatever it takes to bring the reader to the Question: one sentence for a colleague (*You asked whether…*), three or four paragraphs for a cold reader. Never more. If the introduction needs exhibits, it is overstating the obvious.

**Order** changes tone, not content. All four parts stay; their sequence is a choice:

| Order | Reads as |
|---|---|
| Situation → Complication → Answer | standard, neutral |
| Answer → Situation → Complication | direct; the reader already trusts you |
| Complication → Situation → Answer | concerned; something has gone wrong |
| Question → Situation → Complication | aggressive; forcing the issue |

**Four questions** cover nearly every document. Their skeletons:

| Reader's question | Situation | Complication | Key Line noun |
|---|---|---|---|
| What should we do? | Here is how things run now | It no longer produces what we need | changes |
| How do we do it? | We have decided on X | We are not set up to do X | steps |
| Should we do it? | We have a problem | A solution has been proposed, at a cost | reasons |
| Why did it happen? | We expected X | We got Y | causes |

**Business documents** are instances of those four, with the Question usually implied by the form. Spell it out for yourself anyway; a memo whose writer never wrote down the Question is the one that rambles.

| Form | Situation | Complication | Question (often unstated) | Key Line |
|---|---|---|---|---|
| Directive / request | We want to do X | We need you to do Y | How do I do Y? | steps, each with an owner and a date |
| Approval request | We have a problem | We have a fix, and it costs $N | Should I approve? | the four standard reasons, below |
| How-to / procedure | Here is the process as it runs today | It does not do what it should | What changes? | the differences between today's process and the intended one, laid side by side first |
| Decision memo | We want to do X | We have A, B, C as ways to do it | Which one? | criteria the winner meets; or *A if you want P, B if you want Q* when no option wins outright |
| Proposal | You have this problem | You want outside help with it | How will you go about it? | the approach, with experience woven in; terms go in a cover note |
| Status / progress review | We told you X last time | You asked us to check Y; we have | What did you find? | findings, then what changes next |

The four standard reasons under an approval request, in this order: the problem cannot wait; this fix solves it (or is the best of the options the reader already knows); the cost is covered by the return; any side benefits. Only the first three carry the decision. The fourth is included when true, never invented.

A decision memo never structures the Key Line as *A is no good, B is no good, therefore C*. The reason to do C is that it solves the problem, and alternatives appear in the Complication only when the reader already knows them.

An *either A or B* Key Line is an ultimatum when the reader could simply approve A. Use the decision form only when the reader genuinely has to choose between options of comparable cost. When one option is a one-line approval and the other is the writer walking away, the document is an approval request for A, and B is at most a clause of fallback (*or let me know how you would prefer to proceed*).

**From a problem to an introduction.** For a paper, proposal, or report, lay the problem out first and read the introduction off it:

- *Opening scene*: the structure or process where the problem lives, at the level a well-informed outsider would picture it.
- *Disturbing event*: what changed (external, internal, or newly noticed).
- *R1*: the result nobody wants. *R2*: the result wanted instead, stated so you would know when you had it.
- *What has been tried*: nothing, a proposed fix, a fix that failed, several candidates.

Read left to right; the last thing the reader knows is the Complication. Where the reader stands fixes the Question:

| Reader knows | Question |
|---|---|
| R1 and R2, no solution | How do we get from R1 to R2? |
| a proposed solution | Is it the right one? / How do we implement it? |
| a solution that failed | What should we do now? |
| several candidates | Which one? |
| R1 but not R2 | What should we be aiming at? |
| R2 but unsure about R1 | Do we have a problem? |

**Every Key Line point gets its own short introduction**, the same S-C-Q shape, sized to where the reader now stands: after the first point, remind them why this subject matters to the main point; after later points, how this subject follows from the previous one. A heading and a bare assertion is not an introduction.

**Set the Key Line out in the introduction** of any document longer than a few paragraphs, so the reader has the entire argument in the first thirty seconds and can stop there if they trust you. Short documents use the points as topic sentences instead.

## 4. Groups

**The order test.** Every inductive group has one of three orders, and the order tells you where the group came from:

| Order | Source | Example |
|---|---|---|
| Time | you visualized a process; the items are its steps | collect, label, train, evaluate |
| Structure | you divided a whole into parts (no overlaps, nothing left out) | encoder, retriever, reranker |
| Degree | you classified like things; strongest first | the three failure modes, by frequency |

No order means the ideas do not belong together or the group is missing something. Either way, stop and fix the group before summarizing it.

**Five at most.** A longer list hides a subgroup. Find it and name it; the subgrouping is usually the insight the document was missing.

**Action ideas** (steps, recommendations, changes):

- Word each so it implies an end product you could hold: not *improve retrieval quality* but *add a length-based router in front of the index*.
- Separate levels. Two actions sit at the same level if the reader does one *before* the other; one sits below if the reader does it *so that* the other becomes possible.
- The summary of a set of actions is the effect of doing all of them, worded as an end product. If doing them does not produce it, a step is missing.

**Situation ideas** (reasons, findings, problems):

- Strip each to its essence: subject, verb, object.
- Look for the similarity in the subjects, in the predicates, or in the judgment each implies. That similarity is what licenses the group.
- Anything that shares no similarity is news, not thinking. It leaves the document.
- A list of "factors" or "variables" that turns out to have a time order was a list of steps all along. Treat it as one.

**Deduction, when you use it.** Second point comments on the subject or predicate of the first; third draws the consequence. Chain at most two "therefores". Keep the whole thing inside one paragraph or one section, never spread across the Key Line.

## 5. Summaries

A point that names the *kind* of idea below it, instead of the idea, is empty. It anchors nothing, and it hides thinking that was never finished.

> **Don't:** We identified three issues with the vendor onboarding process.
> **Do:** Vendor onboarding stalls because nobody owns the hand-off between legal and procurement.

> **Don't:** There are three reasons the hybrid index should stay.
> **Do:** The hybrid index stays because its gain is concentrated where users feel latency least.

> **Don't:** The evaluation has four limitations.
> **Do:** Every limitation of the evaluation points the same way: it flatters the baseline.

Two recipes, by kind of group:

- **Actions** → state the direct effect of carrying them all out, as an end product.
- **Situations** → state the inference their similarity implies.

Two checks on the result. The inference must not reach past the group: three symptoms do not establish a "profit opportunity", they establish three symptoms with one cause. And the summary must let the reader predict the group; if any item would surprise them, the summary is at the wrong level.

The payoff is not only for the reader. A real summary can be commented on (deduction) or matched with others like it (induction), so it moves the thinking forward. A blank one ends it.

## 6. On the Page

- **Headings are ideas.** A heading names the point of its section, in the same words the outline used. Never *Introduction*, *Background*, *Findings*, *Discussion*, *Conclusions*: those name categories and have no scanning value.
- **Never one heading at a level.** A heading marks one member of a group. A lone subsection means the division was not real.
- **Parallel form within a group.** If the first heading in a group starts with a verb, all do.
- **Headings are outside the text.** The reader may not read them. The first sentence under a heading announces the turn; the document reads whole with every heading deleted.
- **Introduce every group of headings.** State the point the group defends and the ideas to come. A section heading never follows the title directly, and a subsection heading never follows its section heading directly.
- **Transitions look both ways.** Carry a word or phrase from the previous section into the first sentence of the next. Say what the sections *say*, not what they *do* (*this section examined… the next examines…* is not a transition).
- **Summaries only after long sections.** Restate the section's point and its reasons in the outline's words.
- **Conclusions are optional.** A proper introduction and pyramid have already answered the Question. Add a closing paragraph only if it changes what the reader will do or feel; a restatement of the top point is filler.
- **Next Steps** hold only actions the reader will not question. Anything arguable belongs in the body where it can be defended.

The thirty-second test: from the title, introduction, and Key Line alone, can a hurried reader state your point and your reasons? If not, the document is not finished, however good the sections are.

## 7. Sentences

Ideas are held as images; sentences are copies of them. When a sentence will not come clear, do not rearrange the words:

1. Underline the concrete nouns.
2. Draw how they relate: a box, an arrow, a before and an after.
3. Write what the drawing shows.

> **Don't:** Alignment on cross-functional ownership of the incident-response lifecycle remains an open dependency for the Q3 reliability roadmap.
> **Do:** Nobody owns incident response after the on-call engineer hands off, so the Q3 reliability work cannot start until someone does.

> **Don't:** A primary opportunity area lies in the re-scoping of annotation workflows toward the requirements implied by the revised label taxonomy.
> **Do:** The new taxonomy has more labels than the annotators were trained on, so the annotation guide has to be rewritten before the next batch.

## 8. Workflow B: Polish an Existing Draft

1. **Recover the introduction.** Write the draft's Situation, Complication, Question, and Answer in one line each. If the draft has no Question, derive one from the body: why would the reader need these points?
2. **Recover the tree.** Map every heading and every paragraph's topic sentence into an indented outline. Blank spots and crossed branches are the diagnosis.
3. **Audit** against the list below.
4. **Rebuild the outline** to pass, show it, and get agreement.
5. **Rewrite top-down** from the agreed outline, keeping sentences from the draft wherever they still fit.

Audit list, in order of damage done:

1. No single Question, or two that did not collapse into one.
2. The introduction informs (evidence, new claims) or the body reminds (things the reader already knew).
3. History or chronology in the body.
4. A blank assertion at the top of any group (*there are N…*).
5. A heading that names a category, or a lone heading at its level.
6. A group with no defensible order.
7. A group over five, or a deductive chain over four.
8. A deductive argument stretched across the Key Line where induction would do.
9. Items at mixed levels: a *so that* step listed beside the *before* steps it enables.
10. Action items without an end product; situation items with no shared subject, predicate, or judgment.
11. News: a true fact that supports no point above it.
12. A Key Line point that arrives without its own short introduction.

## 9. Where the Pyramid Lands

Same pyramid, different page. The two tables say where each part goes.

### Business

| Kind | Answer | Introduction | Key Line | Headings |
|---|---|---|---|---|
| Slack / chat message | First line, as a sentence the reader could act on alone | Usually none; one clause of Situation if the reader lacks context (*Since the EU launch…*) | At most three lines, each one reason or step; the ask or decision needed is the last line | None. No bold lead-ins, no nested bullets |
| Email | First line | *You asked…* / *Since X…*, one or two sentences | Two to four reasons or steps as short paragraphs or a flat list | None; points are topic sentences |
| Email, request upward (to someone senior, or with power to refuse) | First paragraph: the request and its date, as a question the reader can answer yes to, with one clause of fallback | One paragraph: the fact that created the need, and the cost of yes, stated in one clause | One or two short paragraphs; no chronology of who did not reply, no explanation of the copy list | None. Reference links, if any, in a short list at the end |
| Memo / directive | First paragraph, after a one-paragraph S-C | S-C in the first paragraph; Question implied | Steps with owner and date, set out as a list, then one short section each | One heading per Key Line point, worded as the step |
| Approval request | *We recommend approving X* | Problem (S), fix and cost (C) | The standard reasons (§3), strongest first | One per reason, or none if under a page |
| Decision memo | The chosen option, named | S, then the options as C | Criteria the choice meets, or objectives if no option wins | One per criterion |
| Status / progress review | What was found, in one sentence | *Last time we told you X; you asked us to check Y* | Findings, then next steps | Headings as findings; a dot-dash outline if it will be read around a table |
| Report / proposal | Executive summary is the whole top of the pyramid: S-C-Q-A plus the Key Line set out | One to three pages, and the only place chronology is allowed | One section per Key Line point, each with its own S-C-Q lead-in | Hierarchical, ideas not categories, never a lone heading |

A message that fits on one screen carries the whole pyramid in its top two levels. If it needs a third level, it is a document and should become one; do not nest bullets in Slack to avoid writing a memo.

### Academic

| Kind | Answer | Introduction | Key Line | Headings |
|---|---|---|---|---|
| Paper | The abstract's first sentence or two, and the last paragraph of §1 | §1 is the S-C-Q story: background the reviewer accepts (S), the gap (C), the question this paper answers (Q). Related work is Situation, not a separate argument | The contribution list, as ideas (*routing recovers 90 % of the gain at 15 % of the cost*), not topics (*we study routing*) | Fixed by the venue; see the caveat below |
| Abstract | Sentence one | One sentence of S and one of C | The contributions, one sentence each | None |
| Note / blog | First paragraph | One or two paragraphs of S-C | Recommendations or findings, set out as a list, then one section each | Headings echo the Key Line |
| Rebuttal | One Answer per reviewer point, in the first sentence of that reply | One sentence restating the concern in the reviewer's words (that sentence is the C) | Reasons, strongest first, evidence under each | The reviewer's own labels |
| Grant narrative | Specific aims are the Key Line; the one-sentence goal is the Answer | Significance section is S-C | Aims, each worded as an end product | Fixed by the funder |

**The paper heading caveat.** Venue templates dictate *Introduction*, *Method*, *Experiments*, *Related Work*, which are exactly the category headings §6 forbids. Do not fight the template. In a paper the pyramid shows in three places instead: the contribution list at the end of §1, the first sentence of every section (which states that section's point before any detail), and the topic sentence of every paragraph. Subsection titles are usually free, and there the rule applies in full: *Routing by query length* is a topic, *Routing keeps 90 % of the gain* is an idea.

**The rebuttal caveat.** A rebuttal answers several Questions, one per reviewer point, so it is several small pyramids, not one. Do not force a single top point over them; do give them a shared order (by severity, or the reviewer's order) and say which you chose.

## 10. Limits

- The method orders ideas; it does not supply them. Bottom-up on an empty list produces nothing.
- Five per group and four per chain are limits on what a reader holds, not targets. Two good points beat three padded ones.
- Degree order can be reversed for effect (weakest to strongest). That is a style choice; note that you made it.
- Do not apply the audit to the introduction's own sentences as if they were a pyramid. The introduction is a story, and the story order is deliberate.
- Do not let the outline step become the deliverable. It is scaffolding; the reader sees prose.
