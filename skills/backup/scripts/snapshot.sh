#!/usr/bin/env bash
# Snapshot the LaTeX manuscript at the current working directory into
# fallback/<tag>/ and append a row to fallback/MANIFEST.md.
#
# Usage:
#   snapshot.sh <tag> <description>
#
# Example:
#   snapshot.sh v0002-page-limited-version "Trimmed to 8 pages for the ARR limit"
set -euo pipefail

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <tag> <description>" >&2
    exit 2
fi

TAG="$1"
DESC="$2"

if [ ! -f "main.tex" ]; then
    echo "Error: main.tex not found in $(pwd). Run snapshot.sh from a manuscript root." >&2
    exit 1
fi

if ! printf '%s' "$TAG" | grep -Eq '^v[0-9]{4}-[a-z0-9-]+$'; then
    echo "Error: tag '$TAG' does not match v0001-brief-kebab-desc format." >&2
    exit 1
fi

DEST="fallback/$TAG"
if [ -e "$DEST" ]; then
    echo "Error: $DEST already exists. Tags are immutable; pick the next free version number." >&2
    exit 1
fi
mkdir -p "$DEST"

for item in main.tex zotero.bib sections figures tables tikz assets; do
    if [ -e "$item" ]; then
        cp -R "$item" "$DEST/"
    fi
done

MANIFEST="fallback/MANIFEST.md"
if [ ! -f "$MANIFEST" ]; then
    cat > "$MANIFEST" <<'EOF'
# Manuscript Fallback Manifest

One row per snapshot, oldest at the top. Tags are immutable; correct a
description by appending a new row that clarifies, never by rewriting history.

| Tag | Timestamp | Description |
|---|---|---|
EOF
fi

TS=$(date '+%Y-%m-%d %H:%M:%S %z')
printf '| %s | %s | %s |\n' "$TAG" "$TS" "$DESC" >> "$MANIFEST"

echo "Snapshot created at $DEST/"
echo "Manifest updated: $MANIFEST"
echo "Reminder: git add $DEST/ $MANIFEST  &&  git commit  -- before the edit."
