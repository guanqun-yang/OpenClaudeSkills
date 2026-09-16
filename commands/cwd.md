---
description: Set or create the working folder for this task inside the current repository
argument-hint: <folder, type @ to autocomplete an existing one>
---
Set the working directory for this task to `$ARGUMENTS`, a folder under the
current repository root. A leading `@` or trailing `/` in the argument is just
how the path was autocompleted; strip it.

1. If the folder does not exist, create it, with an empty `README.md` inside.
2. Run `cd` into it with Bash, so the harness records it as the primary working
   directory.
3. From here on, treat that folder as the home of this task: the deliverable is
   its `README.md`, supporting files go beside it, and the repository's
   `CLAUDE.md` conventions apply.
4. Reply with one line giving the absolute path, then wait for the task.
