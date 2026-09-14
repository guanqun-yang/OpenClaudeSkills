---
name: modern-cli
description: Use faster modern CLI replacements (eza, bat, fd, rg, dust, tokei, xh) instead of traditional Unix commands (ls, cat, find, grep, du, wc, curl) when available. Detects installed tools and applies agent-friendly flags to suppress rich TUI output.
---

# Modern CLI Replacements

When executing shell commands, prefer faster modern alternatives over traditional Unix utilities **if they are installed**. These Rust-based tools offer significant speed improvements through parallel execution and SIMD acceleration.

**Important:** Many modern tools default to colorized, icon-heavy, or interactive output that is noisy for agents. Always use the plain/machine-readable flags listed below.

## Replacement Table

### `eza` instead of `ls`

Traditional: `ls -la`, `ls -R`, `tree`
Modern:
```bash
eza -la --no-icons --color=never          # plain long listing
eza -la --no-icons --color=never --git     # with git status column
eza --tree --no-icons --color=never        # recursive tree (replaces `tree`)
eza -la --sort=modified --no-icons --color=never  # sort by modification time
```

Key flags for agent use:
- `--no-icons` — suppress Nerd Font icons
- `--color=never` — disable ANSI colors

### `bat` instead of `cat`

Traditional: `cat file.txt`, `cat -n file.txt`
Modern:
```bash
bat --plain --color=never file.txt         # plain output, no decorations
bat --plain --color=never -n file.txt      # with line numbers
bat --plain --color=never -r 10:20 file.txt  # line range (like sed -n '10,20p')
```

Key flags for agent use:
- `--plain` (or `-p`) — no line numbers, no header, no grid
- `--color=never` — disable ANSI colors
- `-r START:END` — show only a range of lines (useful for large files)

Note: On Debian/Ubuntu, `bat` may be installed as `batcat`.

### `fd` instead of `find`

Traditional: `find . -name "*.py"`, `find . -type d`
Modern:
```bash
fd '\.py$'                                 # find files matching regex
fd '\.py$' src/                            # search in specific directory
fd -t d 'models'                           # find directories only
fd -t f -e json                            # find files by extension
fd -H -I '\.env'                           # include hidden and ignored files
fd -e py -x wc -l {}                       # execute command on each result
fd -e py --max-depth 3                     # limit search depth
```

Key flags for agent use:
- `--color=never` — disable colors (default when piped, but explicit is safer)
- `-H` — include hidden files
- `-I` — do not respect .gitignore (when you need everything)
- `-a` / `--absolute-path` — output absolute paths

Note: `fd` respects `.gitignore` by default, which is usually desirable but may hide files. Use `-I` to override. On Debian/Ubuntu, `fd` may be installed as `fdfind`.

### `rg` (ripgrep) instead of `grep`

Traditional: `grep -r "pattern" .`, `grep -rn "pattern" --include="*.py"`
Modern:
```bash
rg 'pattern'                               # recursive search (default)
rg 'pattern' src/                          # search in specific directory
rg -t py 'def main'                        # filter by file type
rg -l 'TODO'                               # list matching files only
rg -c 'import'                             # count matches per file
rg --json 'pattern'                        # machine-readable JSON output
rg -F 'exact.string'                       # fixed string (no regex)
rg -g '*.ts' -g '!*.test.ts' 'pattern'    # glob include/exclude
rg -U 'struct \{[\s\S]*?field'            # multiline matching
```

Key flags for agent use:
- `--color=never` — disable colors (default when piped)
- `--no-heading` — don't group by file (one result per line)
- `--json` — structured JSON output for programmatic parsing
- `-l` / `--files-with-matches` — just file paths
- `--sort=path` — deterministic output ordering

Note: Claude Code already has a built-in `Grep` tool backed by ripgrep. Prefer the built-in tool when possible. Use `rg` directly in Bash only when you need advanced flags (e.g., `--json`, `-U` multiline, `-x` line-match).

### `dust` instead of `du`

Traditional: `du -sh *`, `du -sh * | sort -rh`
Modern:
```bash
dust                                       # visual disk usage of current dir
dust -r                                    # reverse sort (smallest first)
dust -n 20                                 # show top 20 entries
dust -d 2 src/                             # limit depth to 2
```

Note: `dust` output is inherently visual (block chart). For scripting, `du -sh * | sort -rh` may still be preferable when machine-readable output is needed.

### `tokei` instead of `wc -l` / `cloc`

Traditional: `find . -name "*.py" | xargs wc -l`, `cloc .`
Modern:
```bash
tokei                                      # count lines of code by language
tokei src/                                 # count in specific directory
tokei -e tests -e node_modules             # exclude directories
tokei -t Python,Rust                       # only specific languages
tokei -o json                              # JSON output for parsing
```

Key flags for agent use:
- `-o json` — machine-readable JSON output
- `-e DIR` — exclude directories

### `xh` instead of `curl`

Traditional: `curl -s -H "Content-Type: application/json" -d '{"key":"val"}' URL`
Modern:
```bash
xh GET https://api.example.com             # simple GET
xh POST https://api.example.com key=val    # POST with JSON body
xh GET https://api.example.com Authorization:Bearer\ token  # custom header
xh --print=b https://api.example.com       # print response body only
xh --print=h https://api.example.com       # print response headers only
xh -d https://api.example.com              # download file
```

Key flags for agent use:
- `--print=b` — body only (no headers, no status line)
- `--print=hb` — headers + body
- `--style=plain` — no colors
- `-I` / `--ignore-stdin` — prevent hanging on stdin

## Tools NOT recommended for agent use

These modern tools are excellent for human developers but are **interactive/TUI-based** and should not be used by coding agents:

| Tool | Replaces | Why not for agents |
|------|----------|--------------------|
| `btop` | `top` | Full-screen interactive TUI |
| `fzf` | `cd` / history | Interactive fuzzy finder requiring user input |
| `yazi` | `ranger` | Interactive file manager TUI |

For process monitoring, use `ps aux` or `ps aux --sort=-%mem` instead of `btop`.

## Detection

Before using a modern tool, verify it exists:
```bash
command -v eza && eza --version
command -v bat && bat --version
command -v fd && fd --version
command -v rg && rg --version
command -v dust && dust --version
command -v tokei && tokei --version
command -v xh && xh --version
```

If a tool is not installed, fall back to the traditional equivalent silently. Do not ask the user to install anything.

## Installation (reference only)

If the user asks to install these tools:

```bash
# macOS (Homebrew)
brew install eza bat fd ripgrep dust tokei xh

# Ubuntu/Debian
sudo apt install bat fd-find ripgrep
# Note: bat -> batcat, fd -> fdfind on Debian/Ubuntu
# Other tools may need cargo: cargo install eza dust tokei xh

# Arch Linux
sudo pacman -S eza bat fd ripgrep dust tokei xh
```
