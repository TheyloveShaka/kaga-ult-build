# Cost, models, and prompt shape

Reference for `kaga-ult-build`. Read only when the phase needs it.

### How paid routing actually works, and what it cannot do

A correction worth having before anyone tries to configure this. Agent frontmatter `model:` accepts `opus`, `sonnet`, `haiku`, or `fable` only. You **cannot** put an OpenRouter id like `openai/gpt-5.6-luna` in an agent file and have that agent route to OpenRouter. Routing to OpenRouter is a **session-level** decision made by environment variables before Claude Code starts, so one session equals one provider and one model family.

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
