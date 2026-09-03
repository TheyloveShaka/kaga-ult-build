---
description: Run the 20-point pre-launch sweep - horizontal scroll, broken links and buttons, mobile menu, favicon, titles, meta, 404, copyright year, placeholder text, clickable contact details, success and error states.
argument-hint: [url or project, defaults to the current project]
---

Run the `kaga-launch-check` skill against:

$ARGUMENTS

Verify every item in a real browser using the Browser pane. Do not mark anything PASS that you did not actually test. An untested item is UNVERIFIED.

Write `docs/LAUNCH-CHECK.md` as a table with status and evidence per item, then give a plain verdict: ready to ship, or the list of blockers. Do not soften it.
