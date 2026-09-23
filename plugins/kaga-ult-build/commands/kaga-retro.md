---
description: Learn from past builds. Mine chat history for Kaga's corrections, then update the lessons file so the next build does not repeat them.
argument-hint: [since date YYYY-MM-DD, defaults to the last retro]
---

Run a retro for the kaga-ult-build method.

1. Find the plugin's `scripts/mine_history.py` (under `${CLAUDE_PLUGIN_ROOT}`, or search `~/.claude/plugins` for it). Run it with `--out` pointing at the session scratchpad and `--since` set to $ARGUMENTS, or to the date in the last line of `~/.claude/kaga/lessons.md` if no date was given. Exclude the current session id. The script redacts secrets; if anything key-like survives, drop it and never copy it anywhere.
2. Read only the `[C]` lines and the interrupt counts first. Open surrounding messages only when a correction is unclear.
3. Keep a lesson only if it repeated, cost a revision round, or broke something. One-off taste notes belong in that project's docs, not here.
4. Update `~/.claude/kaga/lessons.md`: rule first, then one line of evidence (project and date). Merge into an existing entry rather than duplicating it, and note the repeat. Create the file if it does not exist.
5. Check the lessons already in the plugin's `references/lessons.md`. If one keeps recurring, the rule is not working: say so and propose a stronger fix, such as a check in `kaga-launch-check`.
6. End the file with `Last retro: <today's date>`.

Report in five lines or fewer: new lessons, repeats, and anything seen three or more times that should be promoted into the shipped `references/lessons.md` or a skill rule. Promotion is Kaga's call.
