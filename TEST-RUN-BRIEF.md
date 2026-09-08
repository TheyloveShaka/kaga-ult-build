# Test-run brief for kaga-ult-build v1.7.0

Paste this into the session where you are running the test build.

## State

Plugin is at v1.7.0, installed at user scope, repo `TheyloveShaka/kaga-ult-build`.
Working copy: `Desktop/projects/Passsion projects/kaga-ult-build`.

## Run it with

```
/kaga-build <your brief>
```

## What is new in this version, and therefore what you are testing

1. **The plan gate is a hard stop.** Phase 1 ends and waits for you. If the run
   approves its own plan and continues, that is a bug and the single most
   important thing to catch.
2. **Prompt shape.** Agent prompts should be a byte-stable prefix (six laws,
   stack, tokens), one cache breakpoint, then agent-specific material. Full
   `ART-DIRECTION.md` only to P1, P9 and the audits, not all nine agents.
3. **Budget preflight** before any paid dispatch, printed as a block with a
   running monthly total.
4. **Conditional parallelism.** P3, P5, P6 sequential when headroom is short.
5. **New gates:** three concepts plus an adversarial review before art
   direction, a conversion pass, and the 20-point `kaga-launch-check`.

## Budget guardrails, non-negotiable

Ceiling is **$10 per month** on OpenRouter.

- Fable 5.1 and Astra are **single-shot only**. One call, one complete prompt,
  one document back. No tool loop, no file exploration, no iterative refinement.
  A loop re-sends the whole context every turn, which is how the month goes.
- Use `:batch` (`anthropic/claude-fable-5.1:batch`) whenever the result is not
  needed in minutes. Verified: exactly half price both directions.
- **Astra stays off** unless you deliberately turn it on. Cap 150K input, hard.
  Past 272K it silently bills 2x input and 1.5x output.
- Maximum two paid calls per build. A third needs your explicit yes.
- Stop at 80 percent of ceiling and report. Never overrun then explain.
- Do not cap `max_tokens` to save money. A truncated answer is billed in full.

**Recommended first run: Pro plan only, $0.00.** It exercises every
architectural change above. Only add Fable on P1 once the pipeline itself is
proven, at roughly $0.70 batch.

## Known constraint

Per-agent OpenRouter routing does not work. Agent frontmatter `model:` accepts
`opus`, `sonnet`, `haiku`, `fable` only. Paid routing is session-level via
environment variables, one session per provider. To use Fable for one phase,
run that phase in its own session, take the artifact, continue on Pro.

## What to report back

- Did the Phase 1 gate actually stop?
- `cache_read_input_tokens` vs `input_tokens` on a warmed build. If cache reads
  are zero, look for a cache breaker: effort or thinking changed between
  requests, a task budget changed mid-task, or a model switch.
- Did P7 security and P8 UAT pass?
- Actual spend against the preflight estimate.
- Anything the crew hand-rolled that an installed skill already does (Law 6).
