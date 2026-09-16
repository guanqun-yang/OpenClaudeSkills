# Coding Project

## General

- Write clean, readable code. Prefer clarity over cleverness.
- Follow the existing style and conventions of the codebase.
- Do not add comments unless the logic is non-obvious.
- Do not add type annotations, docstrings, or logging to code you did not change.

## Changes

- Make minimal, focused changes. A bug fix does not need surrounding cleanup.
- Do not add features, refactor, or "improve" beyond what was asked.
- Do not add error handling for scenarios that cannot happen.
- Do not create abstractions for one-time operations.
- Do not over-engineer or over-defend. Start with the simplest solution that works. Add complexity only when the simple version demonstrably fails.
- When adding a significant feature, check for regression on a more basic version of the code before declaring it done.

## Append-Only Directories

- `pdfs/`, `baselines/`, `datasets/` are **append-and-read-only** if they exist. You may add new files, but never modify or delete existing ones.
- **Never import from or directly depend on these directories.** Do not use `import`, `from ... import`, or hardcoded path references that create a dependency. If you need logic from a baseline or dataset loader, copy the relevant code into your own module.
- New processed datasets may be written to `datasets/`, but once written they are immutable.

## LLM Inference

- **Prefer Response APIs over Chat Completion APIs.** Many providers offer both; Response APIs expose more information (reasoning traces, token usage, tool calls). Use them whenever available.
- **Parallelize inference whenever possible.** Use async/concurrent calls for API-based models. For local models served with vLLM, verify that batched requests are actually processed in parallel.
- **Support all major providers.** Code must work with: vLLM (local), OpenRouter, Anthropic, OpenAI, Gemini, Kimi, Z.ai, and MiniMax. Use a provider-agnostic interface where possible.
- **Explicitly handle these parameters** for every inference call:
  1. `max_context_length` — respect per-model limits, truncate or chunk inputs accordingly.
  2. `reasoning` — whether extended thinking / chain-of-thought is enabled.
  3. `reasoning_strength` — budget or effort level for reasoning (e.g., Anthropic's `budget_tokens`, OpenAI's `reasoning_effort`).
  4. `temperature`, `top_k`, `top_p` — always explicitly set, never rely on provider defaults.
- **Separate actual output from reasoning output.** The response object must cleanly distinguish the final answer from any reasoning/thinking trace. This must be well-tested with assertions.
- **Always use Pydantic for structured output.** Define response schemas as Pydantic models and validate all LLM responses against them. Never parse raw JSON or text without validation.

## Agentic Workflows

- **Always parallelize task completion using Docker containers** when running agentic workflows against external APIs (Anthropic, OpenAI, Gemini, OpenRouter, etc.) or local vLLM servers. Each independent task (per-sample, per-seed, per-setting) runs in its own container so tasks make progress concurrently and one task's failure cannot corrupt another's state.
- **Do not run agentic workflows sequentially.** A single Python loop that calls the API once per item is the wrong default — it wastes wall-clock time and serializes work that has no real dependency.
- **Do not use process-based separation (e.g., `multiprocessing`, `joblib`, `concurrent.futures`) as the production path.** It shares the host filesystem, environment, and Python interpreter state, which makes failures contagious and reproducibility weak. Containers give clean per-task isolation that processes do not.
- **The only exception is debugging.** A sequential or single-process run is allowed when you need a deterministic, attachable debugger session. Switch back to containerized parallel execution before declaring the workflow done.
- **Cap concurrency at the provider rate limit**, not at the host CPU count. For vLLM, cap at the server's measured batched-throughput sweet spot.

## Experiments

- **Interleave by seed, not by setting.** When running multiple settings with multiple random seeds, iterate the outer loop over seeds and the inner loop over settings — i.e., run `(setting 1, seed A), (setting 2, seed A), (setting 3, seed A), (setting 1, seed B), …` rather than finishing all seeds for setting 1 before starting setting 2. This way, an early stop still yields one complete sweep across all settings, which is far more useful than three repeats of one setting and nothing for the others.

## Logging

- Implement real-time logging of all loggable content. Logs go in `logs/YYYYMMDD-HHMMSS-<desc>/` at the project root.
- For LLM inference or agentic workflows, log everything: queries, responses, reasoning/thought, tool uses, and tool results.
- Use structured formats (JSON lines, etc.) so logs are machine-parseable.

## Testing

- Run existing tests after making changes.
- If adding a new feature, add a test if the project has a test suite.
- Do not mock internal code unless absolutely necessary.
