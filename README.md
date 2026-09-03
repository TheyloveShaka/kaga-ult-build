# Kaga Ult-Build

A Claude Code plugin. The house method for building premium client websites, encoded so it runs the same way every time.

## Why this exists

Most of what circulates about building with AI is engagement bait. The same handful of prompts recycled endlessly, workflows that only ever worked in the demo, and a lot of LARPing by people who have not shipped the thing they are teaching. A fair amount of it is simply fake.

But it is not all noise. Scattered through it there are real ideas, usually one or two per source, sitting underneath the theatre.

So I went through a lot of it. I kept what survived contact with an actual build, threw out the rest, and turned what was left into this: one map, in one place, for anyone who wants to make things with Claude that are both beautiful and functional.

It is opinionated on purpose. Take it, fork it, or argue with it.

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
Phase 5   Launch                deploy checklist, ship, verify live, handoff
```

## The six laws

1. **Delegation is binding.** A plan that assigns an agent to a phase means that agent gets spawned. Doing it inline collapses the cost/quality tradeoff and erases the independent review.
2. **Zero defaults.** No system fonts, no stock Tailwind palette, no unstyled shadcn shipped as-is.
3. **Plan, Act, Audit.** Separate passes, separate actors. The builder never signs off on its own work.
4. **No em dashes.** Anywhere in the repo.
5. **Images are the product.** Every slot resolved before launch, or it is a blocker.
6. **Do not reinvent an installed skill.** Route to the specialist. Hand-rolling a worse version of something already installed is the most common way this pipeline wastes money.

## It orchestrates, it does not duplicate

This plugin is a conductor. The depth lives in skills that already exist, and every phase routes to them rather than reimplementing them.

| Phase | Routes to |
|---|---|
| Art direction | `modern-web-design`, `design:design-system`, `anthropic-skills:theme-factory` |
| Architecture | `engineering:system-design`, `engineering:architecture`, `design:user-research` |
| Frontend | `modern-web-design`, `animated-component-libraries`, `dataviz` |
| Motion | `gsap-scrolltrigger`, `motion-framer`, `react-three-fiber`, `locomotive-scroll`, `lottie-animations`, each with its own specialist agent |
| Copy and SEO | `design:ux-copy`, `engineering:documentation` |
| Security | `security-review`, `engineering:code-review` |
| UAT | `design:accessibility-review`, `engineering:testing-strategy`, `run` |
| Integration | `simplify`, `engineering:tech-debt`, `design:design-critique` |
| Quote | `anthropic-skills:docx`, `anthropic-skills:pptx` |
| Launch sweep | `kaga-launch-check`, mandatory on every build |
| Launch | `engineering:deploy-checklist`, `design:design-handoff`, Vercel MCP tools |
| Video references | `watch` (needs `yt-dlp` and `ffmpeg`) |

What this plugin adds on top: the pipeline order, the crew table and the rule that it binds, the six laws, the reference-hunt gate, the image plan, and the costed quote. If a routed skill is not installed, the orchestrator says so by name and falls back to doing the work directly rather than silently skipping it.

### Recommended companions

```bash
claude plugin marketplace add freshtechbro/claudedesignskills
```

Then install at least `modern-web-design`, `gsap-scrolltrigger`, `motion-framer`, `react-three-fiber`, `locomotive-scroll`, `lottie-animations`, `animated-component-libraries`. The `design`, `engineering`, and `anthropic-skills` plugins supply the rest. Connect the Vercel MCP for Phase 5 deployment and live-error verification.

## Commands

| Command | Does |
|---|---|
| `/kaga-build <brief>` | Full pipeline, Phase 0 through 4 |
| `/kaga-refs <sector, audience, feeling>` | Just the reference hunt |
| `/kaga-audit [scope]` | Just the three-pass audit |
| `/kaga-launch-check [url]` | The 20-point pre-launch sweep |
| `/kaga-quote [project]` | Just the business case and client quote |

## Skills

| Skill | Owns |
|---|---|
| `kaga-ult-build` | The orchestrator and the five laws |
| `kaga-reference-hunt` | 10 references, the transferable move from each |
| `kaga-art-direction` | Palette, typography, motion language, spacing |
| `kaga-imagery` | Image inventory, sourcing, and the client ask |
| `kaga-audit` | The three audit passes |
| `kaga-launch-check` | The 20-point pre-launch sweep, verified in a browser |
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

## Licence

MIT
