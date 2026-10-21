# Cost, models, and prompt shape

Reference for `kaga-ult-build`. Read only when the phase needs it.

### How paid routing actually works, and what it cannot do

A correction worth having before anyone tries to configure this. Agent frontmatter `model:` accepts an alias (`opus`, `sonnet`, `haiku`, `fable`), `inherit`, or a full Anthropic model id such as `claude-sonnet-5-5`, which the worker agents use so the alias cannot drift to an older Sonnet. You **cannot** put an OpenRouter id like `openai/gpt-5.6-luna` in an agent file and have that agent route to OpenRouter. Routing to OpenRouter is a **session-level** decision made by environment variables before Claude Code starts, so one session equals one provider and one model family.

What that means in practice:

- **Within a Pro session**, the crew table assigns Claude models to phases, as it does now. No API cost.
- **To use a paid model for one phase**, run that phase in its own session pointed at OpenRouter, hand it the prompt, take the artifact back, and continue on Pro. This is exactly the single-shot pattern `kaga-budget` requires, and the constraint turns out to be a feature: it makes an expensive agentic loop structurally impossible.
- The `kplan` / `kbuild` / `kreview` / `kastra` profile scripts exist for this. One command per phase, not a background router.

Do not attempt per-agent paid routing inside one build. It is not supported, and the workaround people reach for, running the whole build against a paid model, is the most expensive configuration available.

### Proposed crew table, UNTESTED, now superseded

Superseded on 2026-09-23 by the Opus 5.5 lead default in the main skill. Kept for the reasoning.

Recorded from research, not yet validated on a real build. **Do not adopt wholesale.** Run one build on a non-client project and confirm it clears the P7 and P8 audit passes first.

| Phase | Agent | Current | Proposed | Where |
|---|---|---|---|---|
| P1 | kaga-art-director | opus | fable-5.1 | API, single shot |
| P2 | kaga-ux-architect | opus | sonnet | Pro |
| P3 | kaga-frontend-engineer | sonnet | luna | API session |
| P4 | kaga-motion-engineer | sonnet | luna | API session |
| P5 | kaga-backend-engineer | sonnet | sonnet, keep | Pro |
| P6 | kaga-content-seo | sonnet | luna | API session |
| P7 | kaga-security-auditor | opus | opus, keep | Pro |
| P8 | kaga-uat-agent | sonnet | sonnet, keep | Pro |
| P9 | kaga-integrator | opus | fable-5.1 | API, single shot |

Reasoning: Opus phases drop from four to one, which is the heaviest draw on the 5-hour Pro window, and Fable concentrated on the two genuine judgment phases beats Opus spread across four. Every API row must clear `kaga-budget` first.

### Model tiering

Put the expensive model where judgement compounds, and cheap models on the mechanical work. Spending top-tier tokens on scaffolding is waste, and spending cheap tokens on art direction shows in the output.

| Expensive model owns | Cheap models handle |
|---|---|
| Art direction, palette, typography | Minor edits: type sizes, spacing, removing a divider |
| Concept and narrative structure | Cost and credit arithmetic |
| The shot list | Consistency and link checking |
| Architecture decisions | Mechanical refactors and renames |
| The adversarial gate | Recon, inventory, and file sweeps |

The crew table in 1d is where this gets recorded, and Law 1 makes it binding. Cross-validate design decisions with a *different* model rather than the one that made them, because a model reviewing its own judgement mostly agrees with itself.

### The Claude tiers (verified 2026-10-21)

| Model | ID | API price per MTok, in / out | Use for |
|---|---|---|---|
| Fable 5.1 | `claude-fable-5-1` | $10 / $50 | Single-shot hardest judgement, under `kaga-budget` |
| Opus 5.5 | `claude-opus-5-5` | $4 / $20 | The lead: plans, gates, sign-off |
| Sonnet 5.5 | `claude-sonnet-5-5` | $2 / $10 | Builders and auditors, pinned in the agent files |
| Haiku 5.5 | `claude-haiku-5-5` | from $0.10 / $0.50 | Read-only swarm: maps, greps, docs, sweeps |

All four have a 1M context window. On Kaga's Pro plan they draw on usage limits rather than dollars, but the price ratios still show how fast each one burns the allowance. On the Anthropic API the `sonnet` and `haiku` aliases now resolve to the 5.5 models; the agent files pin full IDs anyway, so an alias change can never move a build.

Switches worth knowing, all documented in Claude Code's model configuration:

- `CLAUDE_CODE_SUBAGENT_MODEL=haiku` sends any subagent without its own `model:` (Explore, general-purpose) to Haiku 5.5. The Kaga agents keep their pinned models because frontmatter wins.
- `claude --model opusplan` runs Opus 5.5 in plan mode and Sonnet 5.5 for execution. Lean mode, only when Kaga asks for it.
- `fallbackModel` in settings, for example `["claude-sonnet-5-5", "claude-haiku-5-5"]`, switches model for one turn when the primary is overloaded or unavailable. Rate limits and billing errors do not trigger it, so it is not a guarantee. It is the cheap fix for lesson 9, a model unreachable mid-build.

### Routing without a thinker

Most forks in a build need no model: which file to read, which tool to run, whether to retry or stop. Settle them in code or in a fixed rule, and send only the forks that genuinely split to a model. A social post called this "JEV engineering"; the principle is worth taking, the product attached to it is not (see `rejected.md`).

- **A fixed routing table.** The crew table, `routing.md`, and the tier table above decide who does what before the build starts. Nobody asks a model which model to use.
- **The retry budget lives in the rule.** One retry with the error output attached. The same failure twice goes to the lead, then to Kaga. No open-ended loops.
- **Scripts are the sensors.** A check that can be a script is a script: the `kaga-launch-check` audits, `scripts/qa` screenshot and probe scripts, the history miner. The model reads the evidence; it does not re-derive it. Done is decided by the evidence, not by the builder's report.
- **Dual encoding for the laws.** State the rule in words for the model, then add a mechanical gate where one is cheap: the rendered em-dash scan and computed-font audit, contract checks in each brief, acceptance criteria in the UX spec.
- **Every delegation is a bounded contract:** deliverable (exact files), constraints, non-goals, and the acceptance check. Without one, a model quietly solves an easier task and reports success.
- **A map, not an encyclopedia.** Agents get `docs/PROGRESS.md`, the token file, and a pointer to the one file they need, never a dump of every doc.

### Prompt shape and caching

**Prompt shape matters more than prompt content here.** Build every agent prompt in two parts, in this order:

**Part 1, byte-stable prefix, identical across every agent in the build:**
- The seven laws
- The stack defaults
- The design tokens

End Part 1 with an explicit cache breakpoint.

**Part 2, after the breakpoint, agent-specific:**
- Its slice of `docs/PLAN.md`
- Its boundary: what it must not touch
- A one-paragraph direction summary

Order is load-bearing. Static content first, dynamic last. Any byte that changes in the prefix invalidates everything cached after it, so the prefix must be assembled once and reused verbatim, not regenerated per agent.

**Reserve the full `docs/ART-DIRECTION.md` for P1, P9, and the audit passes**, which actually adjudicate against it. The other six agents get the tokens block plus their own section. Passing the whole document to all nine is correct for cold starts and is also the single largest duplicated input in the build.

Use the **1-hour cache TTL**. The plan gate puts a human in the loop between phases, so a 5-minute TTL expires during the wait. The 1-hour tier writes at 2x instead of 1.25x and pays for itself on the first prevented miss.

Note the limit honestly: a subagent shares no cache with its parent, so caching helps within an agent's own turns, not across the nine. The prefix discipline still matters because agents that re-run, and phases that retry, hit a warm prefix.

**Verify it is working.** On a warmed build, `cache_read_input_tokens` should dominate `input_tokens`, and `cache_creation_input_tokens` should be about one turn's worth rather than the whole conversation. If it reads zero, hunt for a cache breaker: changing `thinking` or `effort` between requests, changing a task budget mid-task, a context-editing pass, or switching models mid-conversation, since caches are per-model.

### Output length, and the trap

**Do not cap `max_tokens` to control verbosity.** Measured: a 16,384 cap ended 15 percent of Opus 5's attempts and a third of Fable 5's, none of them solved, and cost per solved task did not improve. The model never sees `max_tokens`, so hitting it truncates mid-thought and you pay in full for an unusable answer.

Set `max_tokens` to 64,000 for build phases, 128,000 at `xhigh` or `max` effort, and stream anything that large. Treat `stop_reason: max_tokens` as a **failed attempt**, not something to retry at the same cap.

To actually reduce chatter, do it in the prompt:

- **Specify the output shape with an example.** "Return a diff and a three-line summary, no preamble."
- **Give agents an early exit.** Have them emit `<BLOCKED: reason>` and stop, rather than spending tokens explaining at length why they cannot proceed.

To shorten reasoning rather than visible output, that is the `effort` parameter, not `max_tokens`.

### Effort per phase

Measured curves, not guesses:

| Phase | Effort | Why |
|---|---|---|
| P0 reference hunt, P6 content | `low` | Research curves are nearly flat: `low` gives up 1 to 3 points for a third to half off |
| P3, P4 execution | `low`, re-run failures at default | 93 percent pass at ~$0.70/task, against 91.7 percent at $1.39 running everything at default |
| P1 art direction, P9 integration | `high` | Judgment phases, where the curve is steep |
| P7 security audit | `high` | Correctness over cost |

P8 UAT is already the failure signal this pattern needs. Wire it to feed failures back at higher effort rather than running every phase high from the start.

Keep effort **stable within a phase**. Changing `effort` or `thinking` between requests is a cache breaker, so varying it mid-phase costs more than the effort setting saves.
