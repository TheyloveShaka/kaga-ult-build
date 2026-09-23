---
name: kaga-ult-build
description: Kaga's master build orchestrator for premium client websites and web apps. Use for any new site, redesign, landing page, major feature, or visual overhaul where the output must look like a $10k+ agency build. Opus 5.5 leads (Astra only on explicit instruction), a delegated crew builds, and every phase runs Plan then Act then Audit with a human gate. Enforces researched palettes and typography, a real image plan, zero default styling, reference fidelity, and learns from past builds. Triggers on "build a site", "redesign", "new project", "landing page", "make this look premium", "client build", "kaga build".
---

# Kaga Ult-Build

The house method. Every premium build runs through it, small ones included.

## Before anything

1. **Read the lessons.** `references/lessons.md`, then `~/.claude/kaga/lessons.md` if it exists. They are the mistakes past builds already paid for. Do not repeat one.
2. **State the lead and the track** in one line each.
3. **Open `docs/PROGRESS.md`** and keep it current. Usage limits interrupt builds; a resume should cost one read.

## Lead and crew

- **Opus 5.5 (`claude-opus-5-5`) leads by default.** The main session orchestrates: it plans, judges, and routes. If the session is on another model, say so in one line rather than proceeding as if it were Opus.
- **Astra leads only when Kaga explicitly says so** ("Astra leads", "use Astra as the orchestrator"). Asking Astra for a review is a consultant call, not a lead change. Astra-lead mode is the most expensive configuration there is; its rules live in `kaga-budget` and apply in full.
- **Cheaper agents do the volume.** The lead never builds components, reads large files, or runs sweeps itself. It delegates, then judges what comes back.
- **Paid consultants are single-shot.** Fable or Astra review something once, with a complete prompt, when Kaga asks or the approved plan names them. Always governed by `kaga-budget`.

Default crew, binding under Law 1:

| Phase | Agent | Model | Deliverable |
|---|---|---|---|
| P1 | kaga-art-director | opus | `ART-DIRECTION.md` + tokens |
| P2 | kaga-ux-architect | sonnet | route map, section specs, acceptance criteria |
| P3 | kaga-frontend-engineer | sonnet | components, pages |
| P4 | kaga-motion-engineer | sonnet | motion layer, delegated to specialists |
| P5 | kaga-backend-engineer | sonnet | data, auth, API |
| P6 | kaga-content-seo | sonnet | copy, metadata, JSON-LD |
| P7 | kaga-security-auditor | opus | `SECURITY-AUDIT.md` |
| P8 | kaga-uat-agent | sonnet | `UAT-REPORT.md` |
| P9 | kaga-integrator | opus | one coherent build |

Adjust rows to the job. Never delete the audit rows.

## The seven laws

These override convenience. If you are about to break one, say so out loud instead.

1. **Delegation is binding.** A phase the plan assigns to an agent gets that agent, spawned with the `Agent` tool. Doing it inline erases the independent review that made the plan worth writing. If you skip a delegation, say so immediately.
2. **Zero defaults.** No system font stack, no stock Tailwind palette, no unstyled shadcn, no uniform radius. If it looks like the framework's demo, it is not done.
3. **Plan, Act, Audit, with a human gate.** The builder never signs off its own work. **An autonomous run stops at the end of Phase 1 and waits for Kaga.** A plan approved by the thing that wrote it is not a checkpoint.
4. **No em dashes, and no narrating code comments.** Anywhere, including rendered copy. Rationale lives in docs, not in code.
5. **Images are the product.** No greybox ships. Every slot is sourced, generated, or a written ask to the client.
6. **Do not reinvent an installed skill.** Route to the specialist; see `references/routing.md`. Hand-rolling what is installed is the most common waste. If a routed skill is missing, name the plugin that provides it and do the work directly; never skip the step silently.
7. **Look before you show.** Render it, screenshot it beside each reference move it was meant to reproduce, and fix what does not match before Kaga sees it. First builds shipping bland is the most repeated correction in this history.

## Tracks

- **A, Brand adherence.** Existing brand. Starts with extraction. Content is sacred: copy, prices, contacts, and logos are lifted verbatim.
- **B, Cinematic net-new.** Licence to reinvent. Starts with art direction.
- **C, Feature or update.** Our codebase. Trimmed crew, same gates.
- **D, Demo.** A pitch or proof. Skips backend, security, and the quote; keeps every visual gate.

## Phase 0: References

Run `kaga-reference-hunt`: ten references, the specific move worth taking from each. **Stop** until Kaga says which land and what he likes. Record in `docs/REFERENCES.md`, including a checklist of every move he picked; Law 7 is checked against that list.

## Phase 1: Plan

- **1a Extraction (Track A).** Pull logo, favicon, colours, fonts, and copy from the live site and the client's own files (`pdf`, `xlsx`). Name the brand's signature element and confirm it with Kaga. Output `docs/BRAND-EXTRACT.md`.
- **1b Concepts and the adversarial gate.** Three genuinely different directions, each with its narrative structure (`kaga-scroll-narrative`). Kaga picks. Then a *different* agent attacks the pick: where it fails on mobile, which beat is decorative, what reads as generic, the weakest beat and its replacement. It finds holes, it does not redesign. Record the outcome in `docs/DECISIONS.md`.
- **1c Art direction.** `kaga-art-direction` plus `kaga-conversion`: palette with contrast ratios, named and licensed fonts, motion language, spacing scale. Dashboards and app screens use the house language in `kaga-product-ui`.
- **1d Plan.** `docs/PLAN.md`: routes, section intents, the image plan (`kaga-imagery`), data model, acceptance criteria, and the crew table.
- **1e Project `CLAUDE.md`** via `init`. Update, never overwrite; keep hard-won rules.

**HARD STOP.** Present the plan, the crew table, and the `kaga-budget` preflight. Wait for Kaga. If nobody answers, end here with the plan written and say so.

## Phase 2: Act

- **Print the crew table** with the model actually running each phase. Preflight any non-default model with a one-token call.
- **Hero first.** Build the hero, apply Law 7 to it, get Kaga's approval, then build the rest. The hero takes the most revision rounds on every build.
- **Prompt shape.** Every agent prompt is a byte-stable prefix (laws, stack, tokens, then one cache breakpoint) followed by its own slice of the plan, its boundary, an output shape ("a diff and a three-line summary"), an iteration cap, and the `<BLOCKED: reason>` early exit. The full `ART-DIRECTION.md` goes only to P1, P9, and the auditors. Details in `references/cost-and-models.md`.
- **Parallel only with headroom.** P3, P5, and P6 can overlap, but parallelism spends the same tokens faster. When the window or budget is short, run in sequence.
- **Mobile is part of P3,** designed per element, not a later request.
- **Review in batches.** One full pass, every issue listed, one set of revisions. Structural fixes go back to the owner; mechanical ones (sizes, spacing, a stray divider) go to a cheap model.
- **Verify every fix** at the element and breakpoint where it was reported. Never report "fixed" from a diff.
- **P9 integration is real work**: one spacing rhythm, one motion timing, one copy voice, no duplicate components.
- Stack default: Next.js 15 App Router, TypeScript, Tailwind on CSS custom properties, shadcn restyled, Supabase, Vercel. Vite and React 19 for app-like builds with no SEO surface. Any LLM feature: read `claude-api` first.

## Phase 3: Audit

Run by agents that did not build it (`kaga-audit`):

- **Security**: `kaga-security-auditor`, including the commonly missed list (skipped in Track D).
- **UAT**: `kaga-uat-agent` in a real browser, with screenshots, plus `design:accessibility-review`.
- **Design integrity**: `kaga-art-director` returns to hunt for defaults, and checks every move on the `REFERENCES.md` checklist is actually present.
- **Launch sweep**: `kaga-launch-check`, mandatory, including the font audit and the rendered em-dash scan.

Then prove Law 6 in writing in `docs/AUDIT.md`: which foundry supplied the fonts, which component library, which motion specialist, and that no Tailwind default colours remain. "We hand-rolled it" is a finding. Open blockers mean the build is not done.

## Phase 4: Quote

`kaga-quote` (skipped in Track D). Internal `BUSINESS-CASE.md`; client-facing proposal via `docx` or `pptx`, never raw markdown.

## Phase 5: Launch

`engineering:deploy-checklist`, then deploy (Vercel MCP when connected). **Verify the live URL, not the build**: every image, the logo, and the favicon load (paths are case-sensitive once hosted), the critical path works, and `get_runtime_errors` is clean. Buying a domain spends Kaga's money, so get a yes first. Hand off with `design:design-handoff`. Stop dev servers and background tasks.

## Phase 6: Retro

Before closing, append one to three lessons from this build to `~/.claude/kaga/lessons.md`. Take them from what Kaga corrected and what cost a revision round, rule first with one line of evidence. `/kaga-retro` mines the full history when a deeper pass is due. This is how the method gets better instead of repeating itself.

## Crew memory

- `docs/CREW-LOG.md`: append-only. Every agent reads it first and appends before returning: decided, assumed, left for others, unresolved.
- `docs/DECISIONS.md`: one line per settled decision. Reopening one means arguing against the record.
- `docs/PROGRESS.md`: where the build stands, updated at every phase boundary with a three-line status.

## Standing quality bar

- [ ] Every Phase 0 reference move present, checked side by side (Law 7)
- [ ] `kaga-launch-check` complete, zero UNVERIFIED
- [ ] One named, licensed font system on every text node, numerals included
- [ ] Palette from `ART-DIRECTION.md`; brand signature visible in components
- [ ] Components and motion from the installed specialists, restyled to tokens
- [ ] Every image sourced to a per-section intent, graded as one set, loading on the live URL
- [ ] `kaga-conversion` passed; hero answers who, what, and what next in five seconds
- [ ] Hover, focus-visible, active, disabled, empty, loading, and error states all designed
- [ ] Responsive at 375, 768, and 1440, verified with screenshots; reduced motion honoured
- [ ] Metadata, OG, and JSON-LD on every route
- [ ] No em dashes, no narrating comments, no sound unless asked
- [ ] Security clean or accepted with a reason (Tracks A to C)

## References

Read only when the phase needs them:

- `references/lessons.md`: what past builds taught. **Always read.**
- `references/routing.md`: which skill and agent to use for every phase and task
- `references/cost-and-models.md`: paid routing, prompt shape and caching, effort, output length
- `references/sources.md`: vetted component libraries and inspiration sources, and how to vet a new one
- `references/rejected.md`: ideas deliberately not adopted, and why
