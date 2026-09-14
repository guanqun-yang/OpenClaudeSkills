---
name: backup
description: Snapshot the current LaTeX manuscript into fallback/<tag>/ with an auto-incremented v\d{4} tag, and append a row to fallback/MANIFEST.md. Use before any significant edit so the prior state is recoverable from the same repository.
argument-hint: <brief-kebab-case-description>
---

# Backup Skill

Capture an immutable snapshot of the current LaTeX manuscript before a significant edit. Each snapshot lives at `fallback/<tag>/` and is accompanied by a row in `fallback/MANIFEST.md` documenting what the tag means.

This is the **only** sanctioned backup mechanism for paper projects. The previous `\begin{comment}...\end{comment}` edit-with-backup convention has been retired: it bloated source files, lacked atomic snapshots, and broke compile in subtle ways (paragraph breaks after `\end{comment}`, stray catcode issues in `tabular`, drift between the live copy and the commented original).

## Input

`$ARGUMENTS`: A kebab-case description of why this snapshot is being taken (e.g., `before-method-rewrite`, `page-limited-version`, `camera-ready-version`). If omitted, derive one from the recent `git diff` and TODO context, then confirm with the user before running.

## Workflow

### Step 1 — Determine the next tag

1. If `fallback/MANIFEST.md` exists, read the rows and extract the highest `v\d{4}` prefix seen. The next tag's number is that maximum + 1.
2. If no manifest exists, start at `v0001`.
3. There is no reserved version number for camera-ready or any other special milestone. The camera-ready snapshot is simply the next free number with `camera-ready-version` (or similar) as the kebab-case description.

### Step 2 — Derive the brief description

1. If the user supplied one via `$ARGUMENTS`, validate it: lowercase letters, digits, and `-` only; 1 to 6 hyphen-separated tokens.
2. If not, compose one from project state:
   - `git log -5 --oneline` for what has been happening.
   - `git diff --stat HEAD` for what is about to change.
   - Pick a short phrase like `before-experiments-rewrite` or `pre-related-work-cut`.
3. Show the proposed tag and full sentence-form description to the user and **wait for confirmation** when the AI derived the description. Skip the confirmation only when the user supplied the kebab-case description directly.

### Step 3 — Snapshot

Run the bundled script from the manuscript root:

```bash
bash skills/backup/scripts/snapshot.sh "<tag>" "<full sentence description>"
```

What the script does:

- Verifies `main.tex` exists (sanity check that you are at a manuscript root).
- Validates the tag matches `^v[0-9]{4}-[a-z0-9-]+$`.
- Refuses to overwrite an existing `fallback/<tag>/`.
- Creates `fallback/<tag>/` and copies the compile-essential set: `main.tex`, `zotero.bib`, `sections/`, `figures/`, `tables/`, `tikz/`, `assets/` (whichever exist).
- Appends `| <tag> | <timestamp> | <description> |` to `fallback/MANIFEST.md`, creating the manifest with its header on first run.

### Step 4 — Report and remind to commit

Print the new tag, the snapshot path, and a one-line reminder:

```
Snapshot fallback/<tag>/ created.
Manifest updated.
Reminder: `git add fallback/<tag>/ fallback/MANIFEST.md` and commit before the edit.
```

The skill does **not** commit on the user's behalf. The user owns the commit.

## Rules

- **Snapshot before the edit, never after.** If the edit has already overwritten the prior state, the snapshot is useless. The value of this skill depends on running it *before* the change.
- **Snapshots are immutable.** Never modify a previous `fallback/<tag>/` subfolder or rewrite a past manifest row. To correct a manifest description, append a new row clarifying.
- **Compile-essential only.** Do not include `notes/`, `scripts/`, `pdfs/`, `resources/`, `logs/`, or build artifacts (`*.aux`, `*.log`, `*.pdf`, `*.synctex.gz`). The bundled script enforces this by listing the copy targets explicitly.
- **`fallback/` is committed to git, not gitignored.** A fresh clone or a coauthor's checkout must include the snapshot history. Confirm `fallback/` is absent from `.gitignore` before declaring the skill done.
- **Significant edits trigger this skill.** Section restructures, rewrites of more than one paragraph, deletions of figures or tables, and any change to the contribution claim all qualify. Routine typo fixes and single-word edits do not.
- **One snapshot per significant edit.** If two edits happen in sequence, two snapshots are taken. Do not batch multiple edits under one tag.
