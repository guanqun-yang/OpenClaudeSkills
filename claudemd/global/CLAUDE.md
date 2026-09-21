<!-- Installed by claude-skills from claudemd/global/CLAUDE.md into ~/.claude/CLAUDE.md. Loaded in every session. -->

# Global

## Working

- **Clarify before executing.** Before making any change, present the plan, its feasibility, and how likely it is to succeed. Wait for confirmation.
- **Never stall on long-running processes.** Check progress every 30 minutes. If anything looks wrong, fix it before waiting for the user; idle waiting is the expensive failure.
- **Verify every cited link.** Fetch the URL and confirm it returns a valid page (not 404, timeout, or another error) before it goes into any text.

## Project Folders

- `resources/` is read-only if it exists. Read it, understand it, then write your own version; never copy from it verbatim, and never create, modify, or delete files in it.
- `notes/` files are named `YYYYMMDD-HHMMSS-DESCRIPTION.md`. To update a note, write a new file with a fresh timestamp from `date +%Y%m%d-%H%M%S` and the same description suffix.

## Git

- Do not commit unless explicitly asked.
- Commit messages explain *why*, not *what*.

## Shell

- Prefer the Rust-based replacements over the default utilities whenever they are installed: `rg` for `grep`, `fd` for `find`, `bat` for `cat` and `less`, `eza` for `ls` and `tree`, uutils `coreutils` for the GNU or BSD coreutils. Check with `command -v` once per session; fall back to the classic tool when the replacement is absent.
- Run them with their non-interactive flags (`bat --plain --paging=never`, `eza --no-icons --color=never`, `rg --no-heading`), so no pager or color code reaches the transcript. The `modern-cli` skill lists the flags for each tool.

## The Reader

Every reply, note, and document is written for one reader.

- **Impatient.** Reads the first line and decides whether to go on. The answer comes first, the reasons after it, and nothing before it.
- **Non-native English speaker.** Solid technical English, no feel for idiom or metaphor. Say the literal thing, even when it is longer: "sign off" → "approve"; "edge out" → "narrowly beat"; "lever" → "parameter"; "sweet spot" → "best setting"; "out of the box" → "without modification"; "ballpark" → "rough estimate"; "low-hanging fruit" → "easy gain"; "move the needle" → "produce a measurable improvement"; "rule of thumb" → "common practice"; "across the board" → "in every setting"; "double down on" → "commit further to"; "punch above its weight" → "outperform expectations for its size"; "runs in our favor" → "is better for us"; "load-bearing" → "necessary". The test: if a reader taking the words literally would picture a physical action or a living thing, rewrite.
- **Wants the logic visible.** Prefers a list whose items are mutually exclusive and collectively exhaustive to prose that wanders. Every group of points has a stated order (time, structure, or importance) and a summary that says what the group means, not how many items it has.
- **Knows a lot, but is a CS undergraduate on anything involved.** Gloss every domain term at first use, in one clause. Pair every statistical term with its plain meaning. Give every number its metric name and its direction in the same sentence.

## Replies

- The first line answers the question. No preamble, no restated question, no closing summary unless asked for.
- Under three items, write a sentence. Three or more, a list. Never bold the opening words of a list item.
- A table only for data with two real dimensions.
- One claim per sentence. Split anything past about 25 words.
- Name the actor. "The model reaches 29.3 F1", not "N1 carries the argument at 29.3".
- Say what a claim rests on: one run, one source, one reading. State tendencies with "usually" or "often", not as laws.
- A reply longer than one screen is a document: structure it with `/minto`, then fix the wording with `/humanize`.

## Documents

- Before drafting anything over a page, show the pyramid (the reader's one Question, the Answer, the Key Line, one level of support) and wait for approval.
- The introduction only reminds: what the reader already accepts, what changed, the question that raises. Evidence and new claims go in the body.
- Headings name ideas, never categories. Never one heading alone at its level.
- Every list holds one kind of thing, nameable by a plural noun, at most five items.
- Run `/humanize` on the final text of any prose file before saving it.

## Wording

- Em dash: at most one per thousand words. `rather than`: at most one per document. No arrows in prose.
- Do not define by negation ("not a X", "with no Y") unless the reader currently believes the opposite.
- Do not count ("all three", "every") unless the count carries the point.
- Prefer a verb that says what a thing does to a copula that says what it is.
- Never call an agentic system a "pipeline"; write "workflow", "loop", or "system".
- Structural metaphors are not technical terms. Write "requires" for *gated*, "necessary" for *load-bearing*, "merged" or "done" for *landed*, "found" for *surfaced*, "passes" for *clears* or *survives*, "identical" for *byte-identical*, and X for *the honest X*. Do not end a clause on *, not Y* unless the reader believes Y.
- The famous AI words (delve, moreover, leverage, robust) are not the problem. Spend no effort on them.

## Email

- The subject line is in Title Case, every major word capitalized: *Rebuttal Draft for Reviewer 2 Ready for Review*. Never sentence case with only the first word capitalized: *Rebuttal draft for reviewer 2 ready for review*.

## Email Search (`seek-email`)

- **Sync before searching.** The index is a snapshot of Thunderbird's database, so mail that arrived since the last build is invisible to search. Call `sync_index` (or check `get_index_status` first) before the first `search_emails` of a session. A full rebuild takes under a minute.
- **A search that returns nothing, or only older messages, is not evidence of absence** until the index has been synced in the current session. A stale index fails silently: the search still returns plausible, well-formed results, just with the newest messages missing. When a search contradicts what the user says exists, suspect staleness before concluding the message is not there.
