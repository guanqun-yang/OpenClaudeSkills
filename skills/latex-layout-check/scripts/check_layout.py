"""Report layout problems after a LaTeX build: loose or overfull lines, and headings not in Title Case.

Usage:  python3 -I scripts/check_layout.py [main.log] [--threshold 2000] [--strict]

Run automatically by latexmkrc after every build. Each loose or overfull line is reported with the
source file and line range from the log, so it can be fixed where it was written (CLAUDE.md A2).
Lines in the bibliography are listed separately: the venue's .bst controls them.
The exit code is 0 unless --strict is given and a problem outside the bibliography is found.
"""

import argparse
import re
import sys
from pathlib import Path

# APA title case (linked from the ACL formatting guide): lowercase only these short words
SMALL = {"a", "an", "the", "and", "but", "or", "nor", "for", "so", "yet",
         "as", "at", "by", "in", "of", "off", "on", "per", "to", "up", "via", "vs", "vs."}
HEADING = re.compile(r"\\(section|subsection|subsubsection|paragraph)\*?\{((?:[^{}]|\{[^{}]*\})*)\}")
BOX = re.compile(r"(Underfull|Overfull) \\hbox \((?:badness (\d+)|([\d.]+)pt too wide)\) "
                 r"(?:in paragraph|in alignment) at lines (\d+)--(\d+)")
FILE_OPEN = re.compile(r"\((\.?/[^\s()]+?\.(?:tex|bbl|sty|cls|cfg|def|fd|clo|aux|out|toc))")


def boxes(log):
    """Yield (kind, badness_or_pt, file, first_line, last_line, text) with a file stack."""
    stack, i = [], 0
    events = []
    for m in re.finditer(r"\(|\)|" + BOX.pattern, log):
        tok = m.group(0)
        if tok == "(":
            f = FILE_OPEN.match(log, m.start())
            stack.append(f.group(1) if f else None)
        elif tok == ")":
            if stack:
                stack.pop()
        else:
            b = BOX.match(log, m.start())
            current = next((s for s in reversed(stack) if s), "?")
            text = log[b.end():b.end() + 160].split("\n\n")[0].replace("\n", "")
            text = re.sub(r"\\[A-Z0-9]+/[^ ]+ (\([+-]?\d+\) )?|\[\]|\$", "", text).strip()
            events.append((b.group(1), int(b.group(2)) if b.group(2) else float(b.group(3)),
                           current, int(b.group(4)), int(b.group(5)), text[:90]))
    return events


def heading_problems(paths):
    out = []
    for p in paths:
        for n, line in enumerate(p.read_text().splitlines(), 1):
            for m in HEADING.finditer(line):
                title = re.sub(r"\\[a-zA-Z]+\{[^{}]*\}|\\[a-zA-Z]+|\$[^$]*\$|[{}]", " ", m.group(2))
                words = [w for w in re.split(r"\s+", title) if w]
                for k, w in enumerate(words):
                    for j, part in enumerate(w.split("-")):
                        core = part.strip("().,:;\"'`\\")
                        if not core or not core[0].isalpha() or any(c.isdigit() for c in core):
                            continue
                        first = j == 0 and (k == 0 or words[k - 1].endswith(":"))
                        if core[0].islower() and (first or core.lower().rstrip(".") not in SMALL):
                            out.append((p, n, m.group(2), core))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("log", nargs="?", default="main.log")
    ap.add_argument("--threshold", type=int, default=2000)
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()
    log_path = Path(args.log)
    if not log_path.exists():
        return 0
    log = log_path.read_text(encoding="latin-1")
    found = [e for e in boxes(log) if e[0] == "Overfull" or e[1] >= args.threshold]
    text = [e for e in found if not e[2].endswith(".bbl")]
    bib = [e for e in found if e[2].endswith(".bbl")]
    heads = heading_problems(sorted(Path("sections").glob("*.tex")))

    print(f"layout check: {len(text)} loose/overfull line(s) in the text, {len(bib)} in the bibliography, "
          f"{len(heads)} heading(s) not in Title Case (badness threshold {args.threshold})")
    for kind, val, f, a, b, snippet in text:
        size = f"{val:.1f}pt too wide" if kind == "Overfull" else f"badness {val}"
        print(f"  {f}:{a}-{b}  {kind.lower()}, {size}: {snippet}")
    for p, n, title, word in heads:
        print(f"  {p}:{n}  heading '{title}': capitalize '{word}'")
    if bib:
        print(f"  ({len(bib)} bibliography line(s) not listed; the .bst sets that layout)")
    return 1 if args.strict and (text or heads) else 0


if __name__ == "__main__":
    sys.exit(main())
