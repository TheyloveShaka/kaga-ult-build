---
name: kaga-budget
description: Hard cost control for builds that route to paid API models. Enforces the single-shot rule for expensive models, per-call token caps, a running ledger, the Astra long-context cliff guard, and the stop-at-budget rule. Use before dispatching any phase to a paid model, when the user mentions budget, cost, credits, OpenRouter, or spend, and at the close of every build.
---

# Budget

The pipeline can route phases to paid API models. This skill is what stops that being expensive. It is not advisory. A phase that skips it is a bug.

Kaga's current ceiling: **$10 per month on OpenRouter**, on top of a Claude Pro plan. That number is small enough that a single unguarded loop consumes it, so the guards below are sized to it.

## The arithmetic that drives every rule here

Verified against the OpenRouter models API on 2026-09-09, per million tokens:

| Model | In | Out | Batch in | Batch out | Role |
|---|---|---|---|---|---|
| `anthropic/claude-fable-5.1` | $10.00 | $50.00 | $5.00 | $25.00 | Judgment only |
| `openai/gpt-6-astra` | $10.00 | $50.00 | $5.00 | $25.00 | Optional second opinion |
| `openai/gpt-5.6-luna` | $0.20 | $1.20 | $0.10 | $0.60 | Workhorse |
| `deepseek/deepseek-v4-flash` | $0.08 | $0.16 | n/a | n/a | Bulk mechanical |
| `deepseek/deepseek-v4-pro` | $0.95 | $1.89 | $0.66 | $1.98 | Mid tier |
| `google/gemini-3.8-flash` | $0.75 | $3.75 | $0.38 | $1.88 | Vision |
| `cohere/north-mini-code:free` | free | free | | | Rate limited |

Fable and Astra are **50x the input price and 40x the output price of the workhorse**. One 200K-token integrator pass on Fable costs $2.00 in input alone, a fifth of the month, before it writes a word.

`:batch` is confirmed available and is exactly half price on both directions. Use it whenever the result is not needed in the next few minutes.

## Rule 1: expensive models are single-shot, never loops

This is the rule that matters most. An agentic loop re-sends the whole conversation on every turn, so a twelve-turn loop on Fable pays for the context twelve times. That is how a $10 month disappears in one phase.

So: **Fable and Astra get called once, with everything they need, and they return a document.** No tool-use loop, no iterative refinement, no file exploration, no reading the repo themselves.

Concretely, before dispatching to a paid judgment model:

- Gather the inputs yourself, on a cheap model or in the main thread.
- Assemble one complete prompt.
- Call once. Receive one artifact: `ART-DIRECTION.md`, an integration plan, a critique.
- Apply the artifact using cheap models.

If the output is wrong, fix the prompt and call once more. Never let the expensive model drive the fixing.

**Cheap models may loop. Expensive models may not.** Loops belong to `gpt-5.6-luna` and `deepseek-v4-flash`, where a twelve-turn loop costs cents.

## Rule 2: hard caps per call

Check the input size before dispatch. If it exceeds the cap, summarise or trim first, on a cheap model. Do not dispatch and hope.

| Phase | Model | Max input | Max output | Batch | Est. cost |
|---|---|---|---|---|---|
| P1 art direction | fable-5.1 | 60K | 16K | yes | ~$0.70 |
| P9 integration plan | fable-5.1 | 120K | 16K | yes | ~$1.00 |
| Optional second opinion | astra | 150K | 8K | yes | ~$0.95 |
| Everything else | luna / v4-flash | no cap needed | | | cents |

**Maximum two paid-judgment calls per build.** A third requires the user to say yes, with the running total shown.

**No expensive model may spawn another expensive model.** Fable does not get to call Astra.

## Rule 3: the Astra long-context cliff

Past **272K input tokens**, `gpt-6-astra` bills 2x input and cache and 1.5x output, moving to roughly $20/$75. An autonomous run can cross that line silently and triple a phase's cost with no error and no warning.

So Astra is capped at **150K input, hard**, which leaves a wide margin. Count before dispatch. If the input is larger, it is the wrong tool: summarise on a cheap model first, or use Fable, which has no such cliff.

Astra is a plan diff and second-opinion partner. It is never a workhorse. Running Astra and Fable both as workhorses is the single most expensive configuration this pipeline can be put into.

## Rule 4: the ledger

Every paid call is written to `docs/COST-LEDGER.md` **before** it is made, then updated with actuals:

```
| date | phase | model | in | out | batch | est | actual | running |
|------|-------|-------|----|-----|-------|-----|--------|---------|
| 2026-09-09 | P1 art direction | fable-5.1:batch | 48K | 12K | yes | $0.54 | $0.51 | $0.51 |
```

Estimate before, record after, keep a running monthly total. Estimating after the fact defeats the point, since the decision to spend has already been made.

At **80% of the monthly ceiling**, stop dispatching to paid models, report the position, and ask. Do not quietly continue and report an overrun afterwards. At 100%, the build finishes on Pro and free models or it waits for next month.

## Rule 5: no silent retries on paid models

A failed or unsatisfactory paid call is reported, not retried automatically. Retrying a $1 call three times because the output looked thin is how a budget vanishes with nothing to show.

`stop_reason: max_tokens` is a **failed attempt**, not a signal to retry at the same cap. Never cap `max_tokens` low to save money: a truncated response is billed in full and solves nothing. Set 64K for build phases, 128K at high effort, and control length through the prompt and the effort parameter instead.

## Rule 6: route by what the work actually is

| Work | Model | Why |
|---|---|---|
| Visual spine, final coherence judgment | fable-5.1 | The two places taste compounds |
| Adversarial concept review | astra, or Opus on Pro | A different vendor catches different holes |
| Component and page building | gpt-5.6-luna | Volume work, 50x cheaper |
| Mechanical edits, renames, sweeps | deepseek-v4-flash | Near free |
| Security audit, UAT | Opus / Sonnet on Pro | Already paid for, no API cost |
| Bulk research, link checks | north-mini-code:free | Free, rate limited |

**Anything that can run on the Pro plan should.** Pro capacity is already bought. The API budget exists for what Pro cannot do well, which is Fable-grade visual judgment. Spending API credits on work Sonnet handles is pure waste.

## Preflight, every build

Before Phase 2 dispatch, state in one block:

```
Budget preflight
  Month to date:      $X.XX of $10.00
  This build, planned: P1 fable-5.1:batch ~$0.70, P9 fable-5.1:batch ~$1.00
  Astra:              off
  Projected after:    $X.XX
  Remaining builds at this rate: N
```

If projected spend crosses the ceiling, say so and propose the cheaper configuration rather than starting and stopping halfway.
