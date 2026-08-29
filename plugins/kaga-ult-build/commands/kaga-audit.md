---
description: Run the three-pass Kaga audit - security, quality and UAT in a real browser, and design integrity against the art direction.
argument-hint: [path or scope, defaults to the whole project]
---

Run the `kaga-audit` skill on:

$ARGUMENTS

All three passes, each spawned as its own agent, because the builder does not audit its own work:

1. `kaga-security-auditor`
2. `kaga-uat-agent`, verified in a real browser with screenshots, never asserted
3. `kaga-art-director` in audit mode, hunting for defaults that crept back in

Merge findings into `docs/AUDIT.md`, ranked most severe first, each with file, line, failure scenario, and fix.

End with a plain verdict: ready to ship or not. If not, list the blockers. Do not soften it.
