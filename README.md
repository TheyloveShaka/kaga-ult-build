# Kaga Ult-Build

A Claude Code plugin. The house method for building premium client websites, encoded so it runs the same way every time.

## Install

```bash
claude plugin marketplace add TheyloveShaka/kaga-ult-build
```

```bash
claude plugin install kaga-ult-build@kaga-ult-build
```

## What it does

Turns a brief into a shipped site through a fixed pipeline, run by a crew of specialist agents rather than one generalist thread.

```
Phase 0   Reference hunt        10 sites, the specific move to steal from each
Phase 1   Plan                  extraction, art direction, crew table, project CLAUDE.md
Phase 2   Act                   nine agents, delegated, parallel where possible
Phase 3   Audit                 security, UAT in a real browser, design integrity
Phase 4   Business case         true cost, margin, the number to quote
```

## The five laws

1. **Delegation is binding.** A plan that assigns an agent to a phase means that agent gets spawned. Doing it inline collapses the cost/quality tradeoff and erases the independent review.
2. **Zero defaults.** No system fonts, no stock Tailwind palette, no unstyled shadcn shipped as-is.
3. **Plan, Act, Audit.** Separate passes, separate actors. The builder never signs off on its own work.
4. **No em dashes.** Anywhere in the repo.
5. **Images are the product.** Every slot resolved before launch, or it is a blocker.

## Commands

| Command | Does |
|---|---|
| `/kaga-build <brief>` | Full pipeline, Phase 0 through 4 |
| `/kaga-refs <sector, audience, feeling>` | Just the reference hunt |
| `/kaga-audit [scope]` | Just the three-pass audit |
| `/kaga-quote [project]` | Just the business case and client quote |

## Skills

| Skill | Owns |
|---|---|
| `kaga-ult-build` | The orchestrator and the five laws |
| `kaga-reference-hunt` | 10 references, the transferable move from each |
| `kaga-art-direction` | Palette, typography, motion language, spacing |
| `kaga-imagery` | Image inventory, sourcing, and the client ask |
| `kaga-audit` | The three audit passes |
| `kaga-quote` | Cost, margin, and the client quote |

## Agents

`kaga-art-director` (opus), `kaga-ux-architect` (opus), `kaga-frontend-engineer` (sonnet), `kaga-motion-engineer` (sonnet), `kaga-backend-engineer` (sonnet), `kaga-content-seo` (sonnet), `kaga-security-auditor` (opus), `kaga-uat-agent` (sonnet), `kaga-integrator` (opus).

Each starts cold, so the orchestrator passes it the art direction verbatim. Each has explicit boundaries on what it must not touch.

## Configure before first real quote

The rate card holds your cost basis, margin, and walk-away floor, so it is **gitignored and never published**. Set it up once:

```bash
cp plugins/kaga-ult-build/config/rates.example.yml plugins/kaga-ult-build/config/rates.yml
```

Fill in your real numbers and set `confirmed: true`. Every future quote then uses them. Until that file exists and is confirmed, quotes come out marked provisional, which is deliberate: a confident wrong number gets sent to a client, an obvious placeholder gets corrected.

## Default stack

Next.js 15 App Router, TypeScript, Tailwind wired to CSS custom properties, shadcn/ui restyled, Supabase, Vercel. Chosen for the metadata API, JSON-LD, and image optimisation the SEO deliverable depends on. Override to Vite + React 19 for app-like builds with no SEO surface.

## Pairs well with

The `claude-design-skillstack` marketplace, which carries deep implementation skills for GSAP ScrollTrigger, React Three Fiber, Three.js, Framer Motion, Locomotive Scroll, Lottie, Rive, and Spline. The motion engineer defers to those skills when they are enabled.

```bash
claude plugin marketplace add freshtechbro/claudedesignskills
```

## Licence

MIT
