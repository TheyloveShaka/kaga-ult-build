---
description: Build the internal business case and the client-facing quote - true cost, tooling burn, overhead, risk, margin, and the number to send.
argument-hint: [project name or scope, defaults to the current project]
---

Run the `kaga-quote` skill for:

$ARGUMENTS

Read `config/rates.yml` from the kaga-ult-build plugin first. If `confirmed: false`, mark every number provisional and say so at the top of both documents.

Produce two separate files:
- `docs/BUSINESS-CASE.md`, internal, showing cost, margin, risk, and effective hourly
- `docs/QUOTE.md`, client-facing, showing scope, value, price, exclusions, and terms, with no margin visible

Run all three sanity checks on the final number: against the market, against the value to the client, and against the walk-away floor. If they disagree sharply, show me the range and the reasoning instead of picking one silently.
