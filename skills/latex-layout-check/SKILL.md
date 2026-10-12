---
name: latex-layout-check
description: After a LaTeX build, list loose or overfull lines with their source file and line, and headings not in Title Case. Install it into a paper project's scripts/ and latexmkrc so it runs after every latexmk build; use when a PDF shows stretched word spacing or before declaring a draft done.
---

# LaTeX Layout Check

`scripts/check_layout.py` reads `main.log` after a build and prints three kinds of problems:

- Loose lines (underfull `\hbox`) with badness at or above the threshold (default 2000), and every overfull line. Each one carries the source file and line range from the log, plus the start of the offending text.
- Headings in `sections/*.tex` (`\section`, `\subsection`, `\subsubsection`, `\paragraph`) that are not in APA Title Case, the style the ACL formatting guide links to. Only articles, short conjunctions, and prepositions of three letters or fewer stay lowercase (`a`, `the`, `and`, `of`, `to`, `vs.`), so `With` and `From` are capitalized. Words containing digits, such as `v1`, are skipped.
- A count of loose lines in the bibliography, listed apart because the venue's `.bst` sets that layout.

The exit code is 0, so a build never fails on layout. Pass `--strict` to exit 1 when the text or a heading has a problem.

## Install Into a Paper Project

1. Copy `scripts/check_layout.py` from this skill into the project's `scripts/`.
2. Add these lines to the project's `latexmkrc`:

   ```perl
   $ENV{'max_print_line'} = '10000';  # unwrapped log lines, so file names and warnings stay intact
   END { system('python3', '-I', 'scripts/check_layout.py', 'main.log') if -e 'main.log' && -e 'scripts/check_layout.py'; }
   ```

3. Make sure the preamble block of the paper-writing `CLAUDE.md` §A2 is in place. Without it the checker reports many lines that the preamble would have removed.

## Run by Hand

```bash
python3 -I scripts/check_layout.py main.log            # report
python3 -I scripts/check_layout.py main.log --strict   # exit 1 on a problem in the text
python3 -I scripts/check_layout.py --threshold 1000    # also report milder loose lines
```

Fix each reported line by rewording, as the paper-writing `CLAUDE.md` §A2 item 5 describes, then rebuild until the text has no reported line. Check the page budget after each fix: rewording can move the end of the main text.

## Limits

- The source location is the paragraph's line range in the file that was open when TeX finished the paragraph. A paragraph that spans an `\input` can point to the outer file.
- The heading check reads one heading per source line and strips macros such as `\system`, so a heading built mostly from macros is checked only on its plain words.
