---
name: kaga-ult-build
description: Kaga's master build orchestrator for premium client websites and web apps. Use for any new site, redesign, landing page, major feature, or visual overhaul where the output must look like a $10k+ agency build. Runs Plan then Act then Audit, always via a delegated agent crew (art direction, UX, frontend, motion, backend, content/SEO, security, UAT, integration). Enforces researched colour palettes and typography, a real image plan, zero default styling, and produces a client quote. Triggers on "build a site", "redesign", "new project", "landing page", "make this look premium", "client build", "kaga build".
---

# Kaga Ult-Build

The house method. Every premium build runs through it. No exceptions, no shortcuts, no "this one is small so I'll just do it inline".

## The five laws

These override convenience. If you are about to break one, stop and say so out loud instead.

**1. Delegation is binding.** When the plan assigns a role or model to a phase, you spawn that agent with the `Agent` tool. Doing it inline in the main thread collapses the cost/quality tradeoff and erases the second-pair-of-eyes review that made the plan worth writing. This rule exists because a full six-phase redesign plan was once executed in one direct session with zero handoffs. If you ever skip a delegation the plan called for, flag it immediately and unprompted.

**2. Zero defaults.** No system font stack. No Tailwind palette straight out of the box (`bg-blue-500`, `text-gray-700`). No unstyled shadcn component shipped as-is. No default border radius applied uniformly. Every surface gets a deliberate decision. If a component looks like the framework's demo, it is not done.

**3. Plan, Act, Audit.** Three separate passes with separate actors. The agent that built a thing never signs off on it. Audit is not a formality, it has authority to send work back.

**4. No em dashes.** Anywhere. Not in code comments, not in copy, not in commit messages, not in the client quote. Use a comma, a colon, a semicolon, or two sentences.

**5. Images are the product.** A site with placeholder greyboxes is not a deliverable at any price. Every build carries an image plan that is resolved before launch, either with sourced stock, generated assets, or a specific written ask to the client.

## Choosing the track

Read the brief, then pick:

**Track A, Brand Adherence.** The client has an existing site, logo, or brand kit. The job is a redesign or rebuild that must stay recognisably theirs. Starts with extraction.

**Track B, Cinematic Net-New.** No existing brand, or explicit licence to reinvent. The job is an immersive, award-shortlist-grade build. Starts with art direction from scratch.

**Track C, Feature or Update.** Existing codebase of ours, adding or reworking a slice. Skips extraction and full crew, runs a trimmed crew, but still Plan, Act, Audit.

State which track you picked and why in one line before proceeding.

---

## Phase 0: Reference Hunt (always first, never skipped)

Before any colour, any layout, any code. Invoke `kaga-reference-hunt`.

Deliver exactly **10 reference sites** to the user as a numbered list. For each: the URL, one line on what it does well, and the specific transferable move (not "nice design", but "the way the nav collapses into a floating pill after 40vh"). Cover a spread: 3 direct competitors or same-sector, 4 aspirational cross-sector, 2 pure motion or interaction studies, 1 deliberate outlier.

Then stop and ask which ones land and what specifically they like from each. Do not proceed to art direction without that answer. The user has said they want to be exact about this.

Write the verdict into `docs/REFERENCES.md`.

---

## Phase 1: Plan

Runs in plan mode where available. No file writes except planning docs.

### 1a. Extraction (Track A only)

Pull the client's existing brand truth before inventing anything:
- Scrape the live URL for logo, favicon, OG images, hex codes, font families, spacing rhythm, tone of voice.
- Use `WebFetch` for the raw HTML, or Firecrawl if the user has it connected, or the Browser pane tools to read a rendered page when the site is JS-heavy.
- Record what is worth keeping versus what is holding them back. Redesign means improving, not preserving mistakes.
- Output: `docs/BRAND-EXTRACT.md`.

### 1b. Art direction

Invoke `kaga-art-direction`. This produces the non-negotiable spine of the build:
- A researched colour palette with rationale, not vibes. Named tokens, hex values, contrast ratios stated, dark mode mapping.
- A typography pairing with real reasoning about the audience and the medium. Load strategy included.
- A motion language: what moves, how fast, on what easing, and what stays still.
- A spacing and radius scale.
- Output: `docs/ART-DIRECTION.md` plus the token file for the chosen stack.

### 1c. Architecture and crew assignment

Write `docs/PLAN.md` containing:
- Page and route inventory.
- Section-by-section wireframe intent for each page.
- The image plan (see `kaga-imagery`), with every slot marked `stock`, `generate`, or `ASK CLIENT`.
- Data model and backend surface if any.
- **The crew table.** Every phase gets a named agent and a model. This table is binding under Law 1.

Crew table format:

| Phase | Agent | Model | Deliverable | Depends on |
|---|---|---|---|---|
| P1 | kaga-art-director | opus | tokens + ART-DIRECTION.md | Phase 0 |
| P2 | kaga-ux-architect | opus | route map, section specs | P1 |
| P3 | kaga-frontend-engineer | sonnet | components, pages | P1, P2 |
| P4 | kaga-motion-engineer | sonnet | scroll and interaction layer | P3 |
| P5 | kaga-backend-engineer | sonnet | data, auth, API | P2 |
| P6 | kaga-content-seo | sonnet | copy, metadata, JSON-LD | P2 |
| P7 | kaga-security-auditor | opus | SECURITY-AUDIT.md | P3, P5 |
| P8 | kaga-uat-agent | sonnet | UAT-REPORT.md | all build phases |
| P9 | kaga-integrator | opus | merged, coherent build | all |

Adjust rows to the job. Never delete the audit rows.

### 1d. Project CLAUDE.md

Create or update the project's `CLAUDE.md` before building, not after. It must carry: the stack, the commands, the art direction tokens summary, the crew convention, and any project-specific law. If one exists, update it rather than overwriting, and preserve hard-won rules already in it.

Get plan approval from the user before Act.

---

## Phase 2: Act

Execute the crew table. For each phase, spawn the assigned agent with `Agent`, passing:
- The full contents of `docs/ART-DIRECTION.md` (agents start cold and cannot see your context).
- The specific slice of `docs/PLAN.md` they own.
- The explicit boundary: what they must not touch.

Run independent phases in parallel where the dependency column allows it. P3, P5, and P6 usually can overlap.

Each agent writes its own files and reports back. You do not rewrite their work in the main thread, you send it back with notes if it misses.

Then **P9 integration is a real phase**, not a merge commit. The integrator's job is to make nine agents' output read as one designer's hand: consistent spacing rhythm, consistent motion timing, consistent copy voice, no orphaned components, no two spinners with different easing.

### Stack default

Next.js 15 App Router + TypeScript + Tailwind + shadcn/ui, deployed to Vercel. Chosen for the metadata API, JSON-LD, OG image generation, and image optimisation, which the SEO deliverable depends on. Override to Vite + React 19 for app-like dashboards with no SEO surface. Supabase for data and auth unless the job says otherwise, matching the existing house stack.

### Motion arsenal

Reach for these, in this order of preference by job:
- **GSAP + ScrollTrigger** for scroll narrative, pinning, scrubbing.
- **Framer Motion** for component-level state transitions and layout animation.
- **Lenis or Locomotive** for smooth scroll, only when the design earns it.
- **React Three Fiber / Three.js** for genuine 3D. Not for decoration.
- **Lottie or Rive** for illustrated micro-interaction.
- **CSS + `@property` + view transitions** when that is genuinely enough. Restraint is a choice, blandness is not.

The `claude-design-skillstack` marketplace carries deep skills for each of these. Enable it and defer to those skills for implementation detail rather than improvising.

Every motion decision respects `prefers-reduced-motion`. Non-negotiable.

---

## Phase 3: Audit

Three audits, run by agents that did not build the thing.

**Security** (`kaga-security-auditor`, see `kaga-audit`): dependency CVEs, secret leakage, auth and RLS correctness, input validation, XSS and injection surface, CSP and headers, rate limiting, exposed admin routes.

**Quality and UAT** (`kaga-uat-agent`): does it match `PLAN.md`, does every acceptance criterion pass, responsive at 375 / 768 / 1440, keyboard path, screen reader landmarks, WCAG AA contrast, Lighthouse, real browser verification via the Browser pane tools with screenshots as proof.

**Design integrity** (`kaga-art-director`, returning): does the built thing match the art direction, or did defaults creep back in. Explicit hunt for: default fonts, default palette values, unstyled components, inconsistent radii, bland empty states, missing hover and focus states, greybox images.

Findings go to `docs/AUDIT.md` with severity. Blockers get fixed and re-audited. Do not report a build as done with open blockers.

---

## Phase 4: Business Doc

Invoke `kaga-quote`. Produces `docs/BUSINESS-CASE.md`: true development cost, tool and subscription burn, overheads, margin, and the single number to put in front of the client. This is a separate deliverable from the build and is never shown to the client as-is, it is the internal basis for the quote.

---

## Standing quality bar

Before you call anything finished, all of these are true:

- [ ] Fonts are deliberately chosen and self-hosted or preloaded, never a system fallback by accident
- [ ] Palette comes from `ART-DIRECTION.md`, zero raw Tailwind default colour classes in the codebase
- [ ] Every interactive element has hover, focus-visible, active, and disabled states
- [ ] Every empty state, loading state, and error state is designed, not default
- [ ] Every image slot is filled or has an open written ask to the client
- [ ] Motion respects reduced-motion and runs at 60fps on mid-range hardware
- [ ] Responsive verified at 375, 768, 1440 with screenshots
- [ ] Metadata, OG, and JSON-LD present on every route
- [ ] No em dashes anywhere in the repo
- [ ] Security audit clean or accepted-with-reason
- [ ] Project `CLAUDE.md` current
