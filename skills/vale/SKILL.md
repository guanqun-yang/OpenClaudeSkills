---
name: vale
description: "Run the Vale prose linter over a manuscript as a deterministic editing pass. Applies the fixes each rule defines, lists the alerts that need judgment, and names the error classes Vale cannot see so the human reading pass is targeted. Invoke explicitly, last, after minto and humanize."
argument-hint: <file-or-directory>
---

# Vale

A pattern linter decides some errors and cannot decide others. This skill spends the linter on the first group so attention goes to the second.

Invoke it explicitly. It is the last pass on a manuscript: `minto` settles the structure, `humanize` settles the wording, Vale catches the mechanical errors that survive both. Running it earlier wastes the run, because the text still changes afterwards.

## 1. What Vale Decides, and What It Cannot

Vale matches regular expressions and word lists against a tagged token stream. It has no parser, so whole classes of error are invisible to it. Measured on sixteen common errors with the configuration below, Vale caught five.

| Vale decides | Vale cannot see |
|---|---|
| Doubled words (*the the*) | Subject-verb agreement (*the results was*) |
| *then* for *than* after a comparative | *Its* for *It's* at the start of a sentence |
| *alot*, *irregardless*, and other non-words | *a* for *an* before a vowel |
| Missing comma after a discourse marker | *their* for *they're*, *affect* for *effect* |
| Spelling, against a project vocabulary | *should of*, *we seen*, *comprised of* |
| Typography, redundant acronyms, date forms | Anything that depends on the sentence's meaning |

Both columns belong in the report. The first is what the run covers, the second is what the reading pass must cover, and stating it turns that pass into a search for four or five specific mistakes.

## 2. Install Gate

Check first, and stop if Vale is missing. Never skip the run silently.

```bash
command -v vale >/dev/null || echo "not installed"
vale --version
```

If it is absent, print the line for the platform and stop:

- **macOS**: `brew install vale`, or `sudo port install vale`
- **Linux**: `sudo apt install vale` (Debian, Ubuntu), `sudo pacman -S vale` (Arch), `sudo snap install vale` (any), or `brew install vale`
- **Anywhere**: the release archives at <https://github.com/vale-cli/vale/releases>, or `go install github.com/vale-cli/vale/v3/cmd/vale@latest`

Confirm with `vale --version` before going on. Everything below assumes v3.22.0 or later.

## 3. Configuration

Copy [`config/.vale.ini`](config/.vale.ini) to the project root if there is none, add `.vale-styles/` to `.gitignore`, and run `vale sync` to download the packages. Re-run `vale sync` whenever `Packages` changes.

The shipped configuration enables the built-in `Vale` style and `Harper` in full, then names the mechanical rules from `proselint` and `write-good` one by one. A rule can be switched on without its whole style, which is why the file is a short list of what runs instead of a long list of what does not.

That selection is the whole design. `write-good` and `proselint` mostly emit opinions about wording, *'it is' is too wordy*, *Remove 'very'*, and by the time this skill runs, `humanize` has already decided those questions against measured budgets. Enabling them in full produced 44 alerts on a 1,398-word note, 27 of them from `write-good.E-Prime` alone, which objects to every form of *to be*. The selection below produced 2 alerts on the same file, both real.

To see the wording opinions anyway, add `BasedOnStyles = Vale, Harper, write-good, proselint` for one run. Treat everything it says about wording as advisory, and let `humanize` win any disagreement.

## 4. The Editing Pass

**Step 1: run, and keep the output as data.**

```bash
vale --no-global --output=JSON <path> > /tmp/vale.json
```

`--output=line` is for reading (`path:line:col:rule:message`); JSON is the only stable format to parse. `--no-global` ignores the machine's own Vale configuration so the run depends on the project alone.

**Step 2: apply every fix the rule defines, without reading the sentence.** Each alert carries `Action`, and an action with a name and parameters is the replacement the rule itself specifies:

```json
{"Check": "Harper.ThenThan", "Line": 2, "Span": [24, 27], "Match": "then",
 "Action": {"Name": "replace", "Params": ["than"]}}
```

`replace` substitutes the parameter for the span. `edit` applies the named operation (`truncate` on a doubled word). Apply these directly and report them afterwards as a list of line, rule, and change. Do not re-derive the wording from the message; the rule already decided.

`suggest` is not in this group. `Vale.Spelling` returns a list of candidate spellings, which needs a decision (§5).

**Step 3: list the alerts that need judgment,** with line numbers and the rule that fired. `Harper.DiscourseMarkers` says a comma is missing and does not say where the clause ends; that is a reading. Decide each against the manuscript, and say which you changed and which you left.

**Step 4: read for the right column of §1.** Those errors will not appear in any Vale output. Read the manuscript once looking only for them, which is a narrower job than reading for everything.

**Step 5: re-run.** The count should drop and nothing new should appear. Run the linter once per draft. It is idempotent on text you fixed, but it re-raises every alert you decided to leave, with no memory of the decision, so a second pass tends to undo a considered judgment.

**Step 6: report.**

```
Vale pass on sections/003-method.tex
  Applied automatically   4   (2 then/than, 1 doubled word, 1 non-word)
  Decided by reading      2   (1 comma added, 1 left: the clause is correct)
  Vocabulary additions    3   (agentic, MLHat, cyberattacks)
  Found by reading        1   (subject-verb: "each of the runs were")
  Remaining               0 errors, 0 warnings, 2 suggestions
```

Only `error` sets a non-zero exit code. Warnings and suggestions exit 0, so the exit status never means the file is clean. Report counts, not the exit code.

## 5. Spelling and the Project Vocabulary

A domain term that trips spell check is not a misspelling, and disabling `Vale.Spelling` over one product name stops checking every other word. Collect what actually fired:

```bash
vale --no-global --output=JSON <path> \
  | jq -r '.[][] | select(.Check == "Vale.Spelling") | .Match' | sort | uniq -c | sort -rn
```

Add the correct ones, one per line, to `.vale-styles/config/vocabularies/Project/accept.txt`, which the configuration names with `Vocab = Project`. The vocabulary directory is the one part of `StylesPath` that survives `vale sync`. `reject.txt` beside it flags terms the project has banned, which is the place for a spelling the group has ruled out.

Confirm a term before adding it. The vocabulary becomes the reference the rest of the manuscript follows.

## 6. LaTeX

Vale has no LaTeX parser. The shipped configuration maps `tex` to the Markdown parser and ignores whole macros:

```ini
[formats]
tex = md

[*.tex]
BasedOnStyles = Vale, Harper
TokenIgnores = (\\[a-zA-Z]+\{[^}]*\})
```

`TokenIgnores` removes `\citep{foo}`, `\ref{tab:main}`, and `\textbf{...}` before the rules run, which is what keeps citation keys out of the spelling report. On a 1,748-word dissertation section this produced 3 alerts, all domain terms for the vocabulary.

Two limits to state when reporting on `.tex`: the mapping reads macro arguments as prose where the macro is not wholly ignored, and math is not skipped, so a formula can produce spelling noise. `vale --ignore-syntax file.tex` reads the file as plain text instead, which is worse for markup and better when the file is mostly prose.

## 7. Where This Sits

- **`minto`** decides what the document says and in what order. Before this.
- **`humanize`** decides the wording: tics, tone, punctuation budgets. Before this, and it wins every disagreement about a word.
- **`vale`** decides the mechanics that survive both, and names what it cannot decide.

Do not silence a rule to make a run pass. Fixing the prose is the point, and a rule that is wrong for the whole project gets switched off in the configuration with a comment saying why.

For repository-wide adoption, triage of a large first run, and CI wiring, Vale publishes its own Claude Code plugin: `/plugin marketplace add vale-cli/agent-tools` then `/plugin install vale@agent-tools`. Its skills assume a documentation repository and act at `error` level only, so they are the wrong shape for a manuscript, and the right shape for `docs/`.
