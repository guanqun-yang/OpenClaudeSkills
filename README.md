# Open Claude Skills

A collection of reusable [Claude Code](https://claude.com/claude-code) skills and `CLAUDE.md` templates, aimed at academic writing and research workflows.

This repository is a curated public mirror — a private working repo holds the full set, and only the entries that are self-contained and useful outside my own machine get published here.

## Skills

| Skill | What it does |
|---|---|
| `academic-graphic-design` | Style guide for publication-quality figures and tables: color palettes, typography, layout, inline annotations. |
| `backup` | Snapshots a LaTeX manuscript into `fallback/<tag>/` with an auto-incremented version tag and a manifest row, before any significant edit. |
| `detect-prompt-injection` | Scans PDFs for hidden prompt-injection text (zero-width glyphs, `ActualText` entries) before an LLM reads them. Bundles its own scanners. |
| `en-zh-translation` | Practices for English → Simplified Chinese prose translation: terminology consistency, sentence restructuring, punctuation, bilingual LaTeX typesetting. |
| `humanize` | Makes Claude-written prose read as human, with per-1,000-word budgets for the tics that actually show up under measurement (`rather than`, negation frames, em dashes, bold and table scaffolding) and rewrites for each. |
| `latex-paper-project` | File layout and editing conventions for LaTeX paper projects (`main.tex`, `sections/`, `figures/`, `tables/`, `zotero.bib`). |
| `modern-cli` | Prefers faster CLI replacements (eza, bat, fd, rg, dust, tokei, xh) with flags that suppress interactive TUI output. |
| `paper-summary` | Turns paper PDFs into structured two-section deep dives: executive summary plus method walkthrough. |
| `system-branding` | Generates names for CS research systems, then checks uniqueness against Google Scholar, GitHub, and DBLP. |

## `CLAUDE.md` templates

Drop-in project instructions for a given kind of work: `blog`, `coding`, `paper-writing`, `poster`, `rebuttal`.

## Installation

Copy the directories you want into your project:

```bash
mkdir -p .claude/skills
cp -r skills/modern-cli .claude/skills/
cp claudemd/paper-writing/CLAUDE.md ./CLAUDE.md
```

Skills also work from `~/.claude/skills/` if you want them available in every project.

## How skills work

A skill is a directory containing a `SKILL.md` — YAML frontmatter plus a markdown body:

```markdown
---
name: my-skill
description: Short summary used for auto-matching, roughly 250 characters.
---

# My Skill

Instructions, conventions, and examples.
```

Claude Code loads every installed skill's **description** into context, but only pulls in the body when the skill is actually invoked — either explicitly with `/my-skill`, or automatically when Claude judges the description relevant to your request. The explicit form is the reliable one.

See the [skills documentation](https://docs.claude.com/en/docs/claude-code/skills) for the full specification.

## Skills vs. `CLAUDE.md`

|  | Skills | `CLAUDE.md` |
|---|---|---|
| **Loaded** | Description always, body on demand | In full, every conversation |
| **Best for** | Reusable recipes, optional conventions | Mandatory rules you never want skipped |
| **Invoked** | `/skill-name`, or auto-matched | Automatic |

Rule of thumb: if you would be annoyed when Claude forgets a rule, it belongs in `CLAUDE.md`. If it is a recipe you reach for occasionally, make it a skill.

## License

MIT
