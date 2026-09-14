# Rebuttal Writing Conventions

Conventions for writing author responses (rebuttals) to peer reviews, typically posted as markdown on OpenReview or a similar system for ARR (ACL, EMNLP, NAACL), COLM, or the pure-ML venues (ICLR, NeurIPS, ICML). This file is paper-agnostic: it documents structure, style, grounding, tone, timing, and audit conventions, not the content of any one rebuttal. It incorporates the relevant prose and grounding rules from the paper-writing conventions, adapted from LaTeX to markdown.

The governing principle: **the rebuttal is read by an impatient reviewer and by the Area Chair who decides, and both may act on it in a few minutes.** Every rule below serves making the response easy to act on and impossible to dismiss.

## 1. Workflow

- **Clarify before executing.** Before drafting or editing, present the plan, name the exact numbers and wording you intend to use, and wait for confirmation. A wrong plan costs more to redo than to check.
- **Verify every cited link by title match, not just HTTP 200.** Fetch the page, confirm the title and authors match the citation, then commit the URL.
- **Sleep before writing.** Do not send an angry first draft. Do not vent on social media. Do not email the program chairs except for a real process violation (missing reviews, abusive language). "The reviewer is wrong" is not a process violation.

## 2. File and Directory Layout

```
rebuttal/
  <YYYY-MM-DD>/
    README.md            # day strategy log: reviewer roles, item-to-experiment map, number set, posting plan
    <ReviewerID>.md      # one self-contained response file per reviewer
  rebuttal.bib           # shared reference list, author-maintained; new papers only
  <experiment-results>/  # the raw results every number traces to
```

- **One response file per reviewer**, named by the reviewer's identifier. Each file is fully self-contained (see Section 5).
- **Each response file ends with an "Author Notes (not for posting)" block** below a divider (two horizontal rules). It holds the number-to-source audit trail, the camera-ready commitments, the per-reviewer strategy, and any honesty flags. It is never posted; everything above the divider is what the reviewer sees.
- **`rebuttal.bib` is author-maintained.** Do not hand-write entries if it exports from a reference manager; instead list the entries the author should add. It holds only the newly cited support papers, not baselines already in the paper.

## 3. Audience and Voice

Assume the reviewer has this profile, and write for it in every sentence:

- **Impatient.** Will skim past any paragraph that does not pay off in one line. Lead with the answer; defer the buildup.
- **Non-native English speaker** with solid technical English but no fluency in idiom or metaphor.
- **Shaky on statistics.** Reads `p < 0.05` as "good" without parsing it. Any probabilistic claim needs a plain-English clause beside it.
- **May not have reread the paper, and may not remember their own review.** The response must stand on its own (Section 5).
- **Often a self-styled expert with a large ego, and the review may be partly AI-written.** This does not lower the technical bar; it raises the tone bar.

**Ego-safe framing is mandatory.** Never signal that you think the reviewer forgot something, misread, or needs simplification.

- Do not write "As a reminder", "In plain terms", "As you know", "Recall that", or any heading like "A reminder of the setup". Provide context as **notation, definitions, and experiment description**, which reads as precision, not as remediation.
- When the reviewer misread the paper, put the fault on your own writing ("we may not have made this clear in the paper"), never on their reading.
- Credit valid points plainly ("This is the right control to ask for", "The reviewer is right that ...").
- Persuade two readers at once: an automated reader that latches onto explicit structure, "therefore", and exact numbers, and a human who wants one clear takeaway per point.

## 4. Structure of a Response File

### 4.1 Opening: three paragraphs, untitled

1. **Thanks and reflected strength.** One brief thanks, then reflect the reviewer's strongest favorable point back. This arms the reviewer who will argue for the paper and softens the pushback that follows.
2. **Point-to-point declaration and keys.** State that you answer every item one at a time and quote each first. Label the reviewer's items with keys: **W1, W2, ...** for Weaknesses, **Q1, Q2, ...** for Questions, **C1, C2, ...** for Comments, in the order the reviewer raised them.
3. **Conventions and setup.** Define, once, the dataset, task, metrics, and notation so every later number is self-contained, plus the digit and percentage conventions. Frame this as setting notation, not as reminding the reader.

Do not use a separate `## Overall` heading; fold the favorable reflection into paragraph 1.

### 4.2 Keys, one section per reviewer item

- Use **W# / Q# / C#**, never a bare "R#" (ambiguous between Reviewer and Reason).
- **Address every weakness, every question, and every comment,** including positive comments (acknowledge them) and figure or typo comments (commit the fix).
- When two items overlap, put the substance in one section and make the other a one-line pointer to it.
- Headings frame the answer, not the worry ("Isolating the Selector from the Retriever", not "Is the Comparison Fair"), and reuse the reviewer's own vocabulary where they gave a usable phrase.

### 4.3 Per-point pattern

1. **Quote the reviewer verbatim** as a blockquote, byte-exact, with any truncation marked by "...".
2. **A glance-clear bold lead:** one plain sentence that states the conclusion and is understandable at first glance, even if it runs longer. Spell out the meaning; do not compress it into abstract nouns. Weak: "It is a prior, not a leak." Strong: "The prompt only tells the agent how often the fix appears at each rank in general; it never reveals which item is the answer for any test case."
3. **Embed the setting and the numbers** inline, as a small table where possible (Section 5).
4. **Plain explanation.** Short sentences; a table or bullets for three or more items.
5. **A future-tense commitment** for anything that will go into the camera-ready ("we will add this table").

### 4.4 References and Author Notes

- End the posted portion with a `## References` section (Section 6).
- Then the divider and the `# Author Notes (not for posting)` block.

## 5. Self-Containment

Assume the reviewer will not open the paper, the code, or any note.

- **The posted text references no external file, path, note, or "see the repo".** This includes the authors' own working files: the bibliography source (`rebuttal.bib` or any `.bib`), experiment-result files, strategy notes, and the `README.md`. Those names live only in the Author Notes. The reviewer sees results and citations, never the filenames they came from. Every number appears with the setting that produced it.
- For each numeric claim, state the evaluation setting in one clause (dataset and its size, the metric definition, what each compared method is), then show the numbers.
- **Prefer a table** to prose for any comparison or any list of three or more numbers. Reproduce the actual result table inside the response rather than describing it.
- **Define every metric and every statistical term inline on first use** (see Section 7).

## 6. Citations

- **Cite only the new support papers** you introduce in the rebuttal. Baselines and prior work already cited in the paper are named in prose, not numbered.
- **The `## References` block is only the numbered list, nothing else.** No preamble sentence. Do not explain which entries are baselines versus new work, do not write "already cited in the paper", and do not name the `.bib` or any other internal file as the source. Such a sentence both leaks a filename and risks mislabeling prior work as a "baseline" when it is not one. The heading, then the list.
- **Citation markers.** The `## References` block is a markdown ordered list (`1.`, `2.`, `3.`, auto-numbered by markdown). Inline citations are "Author et al. [N]" with the number in square brackets, matching the reference-list number.
- **Per-file local numbering.** Each self-contained file numbers its own references from 1. The author draws them from the shared bibliography, but that source is never named in the posted text.
- Verify every URL resolves and title-matches before citing.

## 7. Language and Style

These adapt the paper-writing prose rules to the rebuttal.

- **No em dashes (U+2014), ever.** Restructure with a comma, semicolon, colon, parenthesis, or a new sentence. En dashes (U+2013) only in numeric ranges; in prose write "to" for a range ("from 12 to 18 percent"). The single exception is inside a verbatim reviewer quote, which is reproduced as written.
- **No native-speaker-only idioms.** Substitute the literal equivalent: "edge out" to "narrowly beat", "sweet spot" to "best setting", "out of the box" to "without modification", "moving the needle" to "producing measurable improvement", "runs in our favor" to "is better for us", "load-bearing" to "necessary".
- **Plain-English rephrasing for statistical claims.** Keep the jargon (its absence reads as under-engineered), and attach a plain clause right after it. "significant (McNemar's exact test, p = 2.4e-44), a paired test for whether two methods differ on the same items"; "95% confidence interval [56.7, 63.5], the range the score would fall in across repeated samples"; "p < 0.05, unlikely to arise by chance if the methods were equivalent". Numbers whose meaning is self-evident ("accuracy 72% to 81%") are exempt.
- **Avoid AI-favored words:** delve, underscore, harness, illuminate, facilitate, bolster, streamline, robust, comprehensive, leverage, "pave the way", "shed light on", "a nuanced understanding", "seamless", "cutting-edge". Prefer plain, direct wording. (Reusing a word the reviewer themselves used, to mirror their vocabulary, is allowed.)
- **Complete sentences only.** Every sentence has a subject and a finite verb. No noun-phrase fragment standing in for a sentence, especially at the head of the conventions paragraph. "Conventions used throughout, so every number below is self-contained." is a fragment ("Conventions used throughout" has no verb); write "We use the following conventions throughout, so that every number below is self-contained." A non-native reviewer reads a fragment as a language error and discounts the whole response.
- **No "pipeline" for an agentic system;** use "workflow", "loop", or "system".
- **Hyphens only out of necessity:** compound adjectives before their noun ("a well-known result"), disambiguating prefixes ("non-trivial"). Not for `-ly` adverbs ("newly added", not "newly-added") or predicative compounds ("the result is well known").
- **Commas:** always after an introductory phrase, and before a coordinating conjunction joining two independent clauses, with no length exemption.
- **Non-essential content:** since dashes are forbidden, choose the wrapper by role: appositive commas for a renaming noun phrase; "namely" or "specifically" for an emphasized instance; "such as" or "including" for an open example list; parentheses for a genuinely skippable side note; a new sentence for a standalone thought.
- **Title Case for all headings.**
- **Model names in plaintext** (GPT-4o, Llama-3.1-70B-Instruct); no code font, math, or small caps.
- **Numeric convention: `%` for absolute scores, `pp` (percentage points) for the difference between two scores.** Declare this once in the opening. Example: "PatchHolmes reaches 59.95% and the baseline 34.61%, a 25.34 pp gap." Report scores to the precision the data allows, up to four significant digits, and keep one digit policy across the file.
- **Currency: write `USD N`, never `$N`.** Two `$` on the same line are parsed as math delimiters by KaTeX, MathJax, and Pandoc with `--mathjax`, and the prose between them is silently swallowed. Write `USD 500` or `500 USD`; spell the ISO code for other currencies (`EUR 500`, `JPY 5000`). The only remaining `$` in the file should be inside a genuine math span (`$\alpha$`) or a fenced code block.
- **Paragraphs under about 150 words;** three or more items become bullets or a table.
- **Tense:** present for the system and for results referencing a table ("the agent reaches 59.95%", "Table 1 shows"); past for actions performed during the rebuttal window ("we ran the control"); future for camera-ready commitments ("we will add").

## 8. Tone and Persuasion

- **Polite, never obsequious.** One thanks, not many.
- **Do not apologize, do not trivialize your own contribution, and do not defend.** Each of these invites a lower score. A control that exposes a confound supports your design rule; it is not an argument to replace your system.
- **Lead each answer with the answer** in the first three words ("We ran this control", "Not quite", "We now report", "Added"), then give the evidence.
- **Start from common ground** ("We agree that X, and ...").
- **Concede cleanly where warranted, and bound it with precedent** ("this is the field-standard setting; systems A, B, and C evaluate the same way"). A concise concession with a citation reads as competence.
- **Answer the intent, not only the literal words.** A narrow question usually stands in for a broader worry; address both.
- **Per-reviewer strategy:**
  - **Champion (highest score):** answer every point fully and arm them with quotable evidence; they argue for the paper in committee.
  - **Borderline:** new data for each concern; the realistic goal is to hold the score or nudge it, not to flip it.
  - **Likely-reject or low-confidence:** write for the Area Chair, stay dispassionate, and do not ask for a score change. A clean, quotable record is the goal.
  - **Ethics flag:** a separate confidential note to the chairs; cite only what the paper documents.

## 9. Grounding and Traceability

- **Single source of truth for every number.** One results artifact (raw logs plus the script or file that aggregates them) is the authority. The chain is: raw logs to a results file to the rebuttal table to the rebuttal prose. A number that cannot be traced to the results file is not allowed.
- **Author Notes audit trail.** Every %, count, and score in the posted file has a row in the audit trail mapping it to its source file. Record non-delivery too (an analysis promised but not run).
- **Reviewer quotes are byte-exact** against the review text, including curly versus straight quotes, hyphens, and spacing. Mark any truncation with "...". Inner double quotes may be nested as single quotes. A misquote the reviewer catches is unrecoverable in committee.
- **Selective-reporting honesty flag.** If you omit results that would undercut the narrative (for example, a subset of runs where the claim is weaker), record the omission and a fallback framing in the Author Notes, and be ready to disclose if a reviewer asks. Never present a favorable subset as the whole.
- **Cite the compiled PDF's section and table numbers**, not source labels, when pointing to the paper.

## 10. Timing and Endgame

The mechanics vary by venue; the cadence below is the default. Adjust to your submission system.

- **Post early to mid-window, not at the deadline.** A first response about one-third of the way into the discussion period converts to a score change most often.
- **Reply within 24 hours** to any reviewer who engages. Engagement velocity is the strongest single predictor of a score increase.
- **Do not chase.** At most one factual midpoint nudge to a silent reviewer, surfacing the specific added result, then stop. Daily reminders make a reviewer keep their score rather than raise it. Do not chase a confirmed detractor in the second half of the window.
- **The move ladder:** (1) the response; (2) if a movable reviewer stays silent, one confidential note to the Area Chair; (3) a short closing summary near the deadline with three parts, resolved, still open, current standing. Post the closing after the last reply, never before.
- **Reader settings.** Post the main response and substantive public replies visible to all reviewers plus the Area Chair, so the AC witnesses the engagement. Reserve the confidential AC channel for escalation. Set the Readers field deliberately per comment.
- **Write for the Area Chair throughout.** The AC decides, has likely not reread the paper, and may read only the reviews and your response. Apply the test: could a neutral third party tell the concern was resolved from your response alone? If not, you are writing for yourself.

## 11. Pre-Submission Audit

A mechanical sweep of each posted file (above the divider), under 30 minutes. Skipping it risks a "the rebuttal misquoted me" comment, which is unrecoverable.

1. **Anonymity:** zero local paths, usernames, or institution names above the divider.
2. **Dashes:** zero em dashes; en dashes only in numeric ranges. Grep for the glyphs, and separately grep the bold-bullet pattern where a dash hides between bold tokens.
3. **AI-favored words and idioms:** zero (allowing words the reviewer themselves used).
4. **Reviewer-quote audit:** each blockquote is a verbatim substring of the review, allowing marked "..." truncation and standard inner-quote nesting.
5. **Number audit:** every %, count, and score traces to a row in the Author Notes audit trail.
6. **Self-containment:** no reference to an external file, note, or path in the posted text, including the `.bib`, experiment files, and the `README`; every number carries its setting.
7. **Citation format:** ordered-list `1.` references and `[N]` inline; the `## References` block is the bare numbered list with no preamble sentence; every URL verified reachable and title-matched.
8. **Grammar:** no noun-phrase fragments; every sentence has a subject and a finite verb.
9. **Paragraph length** under about 150 words; three-or-more-item lists are bullets or tables.
10. **Keys:** every weakness, question, and comment has a W# / Q# / C# section; duplicates are one-line pointers.
