---
description: Stage every change in the current repository, commit it with a message that explains why, and push
argument-hint: <optional: what this change is for, used for the commit message>
---
Stage, commit and push everything that has changed in the current repository.
Context from the user, if any: $ARGUMENTS

Work through these steps in order and stop at the first one that fails.

1. **Look before staging.** Run `git status --short` and `git diff --stat`. If the
   working tree is clean and nothing is staged, say so and stop. Otherwise list
   the untracked files that are about to be added for the first time, and refuse
   to continue if any of them looks like a secret (`.env`, `*.pem`, `*.key`,
   `credentials*`, `*token*`) or is larger than 10 MB; name the file and ask
   what to do. `.gitignore` is respected automatically; do not force-add.
2. **Run the repository's own pre-commit step, if it documents one.** Check the
   repository's `CLAUDE.md` or `README.md` for a step that must run before a
   commit (an index generator, a formatter, a link check). Run it and stage its
   output with the rest. Do not invent such a step where none is documented.
3. **Stage everything:** `git add -A`.
4. **Write the commit message from the diff.** Read `git diff --cached` far
   enough to know what changed. The subject line is at most 72 characters and
   states the purpose; the body, when needed, explains why the change was made,
   not what was changed, because the diff already shows that. Use the user's
   context from above when it says why. End the message with whatever
   attribution trailer the harness asks for in this session, and nothing else.
   Commit with `git commit -F -` fed through a heredoc so the message keeps its
   line breaks.
5. **Push.** If the branch has an upstream, `git push`; otherwise
   `git push -u origin <branch>`. Do not use `--force`. If the push is rejected
   because the remote is ahead, run `git pull --rebase` once, and if that
   produces conflicts, stop and report them instead of resolving them.
6. **Report in one short message:** the commit hash and subject, the branch and
   remote, and anything a `pre-push` hook printed (for example a site deploy
   started in the background), so the user knows where to look next.

Never commit on a branch other than the current one, never rewrite history,
and never touch files the user has deliberately left unstaged if they say so in
the context above.
