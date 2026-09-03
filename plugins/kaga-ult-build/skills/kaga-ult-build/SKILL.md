---
name: kaga-ult-build
description: Kaga's master build orchestrator for premium client websites and web apps. Use for any new site, redesign, landing page, major feature, or visual overhaul where the output must look like a $10k+ agency build. Runs Plan then Act then Audit, always via a delegated agent crew (art direction, UX, frontend, motion, backend, content/SEO, security, UAT, integration). Enforces researched colour palettes and typography, a real image plan, zero default styling, and produces a client quote. Triggers on "build a site", "redesign", "new project", "landing page", "make this look premium", "client build", "kaga build".
---

# Kaga Ult-Build

The house method. Every premium build runs through it. No exceptions, no shortcuts, no "this one is small so I'll just do it inline".

## The six laws

These override convenience. If you are about to break one, stop and say so out loud instead.

**1. Delegation is binding.** When the plan assigns a role or model to a phase, you spawn that agent with the `Agent` tool. Doing it inline in the main thread collapses the cost/quality tradeoff and erases the second-pair-of-eyes review that made the plan worth writing. This rule exists because a full six-phase redesign plan was once executed in one direct session with zero handoffs. If you ever skip a delegation the plan called for, flag it immediately and unprompted.

**2. Zero defaults.** No system font stack. No Tailwind palette straight out of the box (`bg-blue-500`, `text-gray-700`). No unstyled shadcn component shipped as-is. No default border radius applied uniformly. Every surface gets a deliberate decision. If a component looks like the framework's demo, it is not done.

**3. Plan, Act, Audit.** Three separate passes with separate actors. The agent that built a thing never signs off on it. Audit is not a formality, it has authority to send work back.

**4. No em dashes.** Anywhere. Not in code comments, not in copy, not in commit messages, not in the client quote. Use a comma, a colon, a semicolon, or two sentences.

**5. Images are the product.** A site with placeholder greyboxes is not a deliverable at any price. Every build carries an image plan that is resolved before launch, either with sourced stock, generated assets, or a specific written ask to the client.

**6. Do not reinvent an installed skill.** The environment carries specialist skills for accessibility, design systems, motion, SEO copy, security review, and deployment. Route to them. Hand-rolling a worse version of something already installed is the most common way this pipeline wastes money. See the skill routing table below.

## Choosing the track

Read the brief, then pick:

**Track A, Brand Adherence.** The client has an existing site, logo, or brand kit. The job is a redesign or rebuild that must stay recognisably theirs. Starts with extraction.

**Track B, Cinematic Net-New.** No existing brand, or explicit licence to reinvent. The job is an immersive, award-shortlist-grade build. Starts with art direction from scratch.

**Track C, Feature or Update.** Existing codebase of ours, adding or reworking a slice. Skips extraction and full crew, runs a trimmed crew, but still Plan, Act, Audit.

State which track you picked and why in one line before proceeding.

---

## Skill routing

**Law 6: do not reinvent an installed skill.** Kaga's environment carries deep skills that already solve most of what this pipeline needs. Writing your own accessibility pass when `design:accessibility-review` exists is wasted work and a worse result. Before any phase, check this table and invoke what is listed.

| Phase | Invoke these skills | Delegate to these agents |
|---|---|---|
| 0 Reference hunt | `kaga-reference-hunt`, `modern-web-design` | |
| 1a Extraction | `kaga-art-direction` | |
| 1b Concepts + adversarial gate | `kaga-scroll-narrative` for the structure of each concept | a *different* agent attacks the chosen concept |
| 1c Art direction | `kaga-art-direction`, `kaga-conversion`, `design:design-system`, `anthropic-skills:theme-factory`, `modern-web-design` | `kaga-art-director`, `modern-web-design:modern-web-design-specialist` |
| 2 Conversion pass | `kaga-conversion`, `design:ux-copy` | `kaga-content-seo`, `kaga-ux-architect` |
| 1d Architecture | `engineering:system-design`, `engineering:architecture` (ADR for any real tech choice), `design:user-research`, `design:research-synthesis` | `kaga-ux-architect` |
| 1d Shot list + image plan | `kaga-scroll-narrative`, `kaga-imagery` | |
| 2 Scroll narrative | `kaga-scroll-narrative`, `gsap-scrolltrigger` | `kaga-motion-engineer` |
| 2 Frontend | `modern-web-design`, `animated-component-libraries` | `kaga-frontend-engineer`, `animated-component-libraries:animated-component-libraries-specialist` |
| 2 Motion | pick per job, see below | see below |
| 2 Backend | `engineering:system-design`, `engineering:architecture` | `kaga-backend-engineer` |
| 2 Content and SEO | `design:ux-copy` | `kaga-content-seo` |
| 2 Charts or data UI | `dataviz` | |
| 3 Security | `security-review`, `engineering:code-review` | `kaga-security-auditor` |
| 3 UAT | `design:accessibility-review`, `engineering:testing-strategy`, `run` | `kaga-uat-agent` |
| 3 Design integrity | `design:design-critique` | `kaga-art-director` in audit mode |
| 3 Integration | `simplify`, `engineering:tech-debt` | `kaga-integrator` |
| 3 Launch sweep | `kaga-launch-check` (the 20-point gate, mandatory) | `kaga-uat-agent` |
| 4 Quote | `kaga-quote`, `anthropic-skills:docx` or `anthropic-skills:pptx` for the client-facing version | |
| 5 Launch | `engineering:deploy-checklist`, `design:design-handoff`, `engineering:documentation` | |

Reference material that arrives as video (a competitor walkthrough, a technique tutorial, a client's own screen recording) goes through the `watch` skill, which transcribes it and extracts frames so it becomes usable context instead of something you guess at. It needs `yt-dlp` and `ffmpeg` on the machine.

### Motion routing

Do not hand-roll animation. Route to the specialist for the technique:

| Need | Skill | Agent |
|---|---|---|
| Scroll narrative, pinning, scrubbing, parallax | `gsap-scrolltrigger` | `gsap-scrolltrigger:gsap-scrolltrigger-choreographer` |
| Component state, layout, gesture, presence | `motion-framer` | `motion-framer:motion-framer-choreographer` |
| Real 3D, product configurators, immersive scenes | `react-three-fiber` | `react-three-fiber:react-three-fiber-architect` |
| Smooth scroll, viewport detection | `locomotive-scroll` | `locomotive-scroll:locomotive-scroll-specialist` |
| Illustrated micro-interaction, animated icons | `lottie-animations` | `lottie-animations:lottie-animations-choreographer` |
| Pre-built animated components, Magic UI, React Bits | `animated-component-libraries` | `animated-component-libraries:animated-component-libraries-specialist` |

`kaga-motion-engineer` stays the owner of the motion layer. Its job is to choose the technique, delegate to the right specialist, and enforce the motion language, reduced-motion fallback, and frame budget across whatever comes back. It does not implement what a specialist does better.

### Crew memory

Borrowed from harness designs that treat memory as infrastructure. The gap it fixes: every agent here starts cold, so context gets re-derived, decisions get silently reversed between phases, and nothing learned on one build reaches the next.

Three files, all cheap to maintain:

**`docs/CREW-LOG.md`**, the shared blackboard for this build. Every agent appends before returning: what it decided, what it assumed, what it left for someone else, what it could not resolve. Every agent reads it before starting. This is what stops the frontend engineer inventing a value the art director already settled, and it costs far less than passing full context to nine cold agents.

Append-only, one block per handoff:

```
## P3 kaga-frontend-engineer
Decided: card radius 12px per token scale, not the 8px in the mockup
Assumed: testimonial count is variable, built for 2 to 6
Left for: motion engineer, hooks on .card-grid, expects stagger on entry
Unresolved: hero image slot still ASK CLIENT
```

**`docs/DECISIONS.md`**, the short list of things now settled. Anything reopened must be argued against what is written here, not re-litigated from scratch. Keep it to one line per decision.

**`PATTERNS.md`** at the plugin root, the only file that crosses projects. After a build ships, append what actually worked and what cost time: a palette structure that landed, a section pattern clients kept approving, a library that fought the stack, a client-ask that always arrives late. Read it during Phase 1 of the next build. This is the compounding part, and it is the single highest-value idea in that whole harness.

Keep all three terse. A log nobody reads because it is bloated is worse than no log.

### What was deliberately not taken

Auto-routing hooks and a large ambient tool surface were rejected on purpose. They conflict with Law 1: routing here is an explicit crew table the user approves, not a background decision. Automatic coordination would make delegation invisible, which is exactly the failure this whole method was built to prevent.

**The one-prompt, one-shot framing was also rejected.** Every source this method borrowed from sells the same story: drop in a skill, type one sentence, receive a finished premium site. It is the claim that gets the views, and it is not what produced their own results.

Watch what they actually do. They spend twenty to thirty minutes gathering references before writing anything. They build a shot list. They identify the typeface by name because the model guesses wrong from an image. They generate a still, approve it, and only then pay to animate it. They run a full review pass and send a batch of corrections. They iterate on the video three or four times before one is usable.

That is a process. The "one shot" is the edit.

This matters practically, not just as pedantry. If you believe the framing, you skip Phase 0, accept the first concept, let the font be inferred, and spend credits animating a frame nobody approved. You then get the output that framing actually produces, which is a generic site with an expensive header.

So: take the techniques, refuse the promise. The reference hunt, the concept gate, the shot list, and the named font are the parts doing the work, and each of them is a step someone chose to take before prompting. When a source claims otherwise, look at what they did on screen rather than what they said, and record the technique rather than the pitch.

### Full inventory: the rest of what is installed

The routing table above covers the main path. These apply less often but are still installed, and reaching for them beats improvising. Law 6 covers all of them.

**Build-adjacent**

| Skill | When |
|---|---|
| `init` | Phase 1d, generating or refreshing the project `CLAUDE.md`. Use it instead of hand-writing that file. |
| `claude-api` | **Mandatory** before writing any code that calls Claude or any LLM: model ids, pricing, tool use, caching, streaming. Never answer a model or pricing question from memory. Applies to AI features inside client builds, which is a recurring pattern in this portfolio. |
| `mcp-builder` | The build needs a custom MCP server to reach a client's internal system. |
| `run` | Launching and driving the project's app to prove a change works. |

**Design surfaces beyond the site itself**

| Skill | When |
|---|---|
| `design` (canvas) | Mockups, wireframes, or screen flows the user wants to tweak visually before any code exists. Multi-artboard, pan and zoom, published as an Artifact. Strong fit between Phase 1b and Phase 2 when the direction needs to be seen before it is built. |
| `canvas-design` | Print and static collateral for the client: posters, flyers, launch graphics. A site build often has marketing pieces attached. |
| `artifact-design` | **Required** before writing any Artifact, including a Markdown one. Load it before, not after. |
| `artifact-diagramming` | Diagrams inside an Artifact: architecture, flows, mechanism drawings that must read in both themes. |
| `artifact-capabilities` | The Artifact needs runtime behaviour: persistence, shared state, live data, viewer identity, file storage. Load before declaring any capability. |
| `web-artifacts-builder` | The deliverable is an elaborate multi-component Artifact rather than a deployed site. |

**Client inputs and outputs**

| Skill | When |
|---|---|
| `pdf` | Track A extraction where the client sends a brand book, style guide, or existing collateral as PDF. Pull the real palette and type out of it rather than guessing from screenshots. |
| `xlsx` | The client hands over a product list, price sheet, vendor roster, or inventory as a spreadsheet that has to become seed data. Recurring on catalogue and directory builds. |
| `docx` / `pptx` | The client-facing quote and proposal, per `kaga-quote` Step 5. |
| `dataviz` | Any chart, dashboard, stat tile, or sparkline, read before the first line of chart code. |

**Running the work**

| Skill | When |
|---|---|
| `standup` | Client progress updates. A weekly written update from actual commits and PRs is the cheapest thing that keeps a client calm on a multi-week build. |
| `task-management` | Tracking build tasks and commitments across a longer job. |
| `memory-management` | Decoding a client's shorthand, internal names, and acronyms so their brief is understood the way a colleague would understand it. |
| `incident-response` | A shipped client site goes down or breaks. Triage, communicate, then a blameless postmortem. Applies to anything under a maintenance arrangement. |
| `schedule` / `loop` | Recurring post-launch checks on a live client site: uptime, form delivery, analytics sanity. |
| `skill-creator` | Extending or fixing this plugin itself. Use it rather than hand-editing skill frontmatter and guessing at description triggering. |
| `security-review` / `code-review` / `simplify` / `engineering:*` | Per the routing table and `kaga-audit`. |

### If a skill is missing

These come from the `design`, `engineering`, `anthropic-skills`, and `claude-design-skillstack` plugins. If one is not available, say so, name the plugin that provides it, and fall back to doing the work directly. Never silently skip the step.

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
- If the client sends a brand book, style guide, or collateral as PDF, run it through the `pdf` skill and pull the real palette, type, and spacing out of it. Do not eyeball a brand guide from a screenshot.
- If they hand over a product list, price sheet, or roster as a spreadsheet, `xlsx` turns it into seed data.
- Record what is worth keeping versus what is holding them back. Redesign means improving, not preserving mistakes.
- Output: `docs/BRAND-EXTRACT.md`.

### 1b. Three concepts, then an adversarial gate

Cheap divergence before expensive convergence. The most costly mistake on a premium build is executing the first idea beautifully, because a well-built weak concept still fails and you pay full price to find out.

**Propose three distinct directions**, not three shades of one. Each gets a name, the narrative structure it uses (see `kaga-scroll-narrative`), the feeling it targets, and one line on why it fits the brief. They must be genuinely different bets: if two could share the same shot list, you have two, not three.

Then present them and let the user pick. If they want to see more than one built, build them in parallel as separate agents and compare, but say what that costs first.

**Then the adversarial gate, before any asset or component exists.** Hand the chosen concept to a *different* agent whose only job is to attack it:

- Where does this concept fail on mobile?
- What does it cost to build, and is the payoff worth it?
- Which beat is decorative rather than persuasive?
- What will the client's actual customer not understand?
- Has this been done so often it now reads as generic?
- What is the single weakest beat, and what replaces it?

The reviewer does not get to redesign, only to find the holes. The concept either survives with fixes or gets replaced. Record the outcome in `docs/DECISIONS.md`.

This gate is deliberately early because it is the cheapest place in the whole pipeline to be wrong. An hour here saves a rebuild.

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

### 1c. Art direction

Invoke `kaga-art-direction`. This produces the non-negotiable spine of the build:
- A researched colour palette with rationale, not vibes. Named tokens, hex values, contrast ratios stated, dark mode mapping.
- A typography pairing with real reasoning about the audience and the medium. Load strategy included.
- A motion language: what moves, how fast, on what easing, and what stays still.
- A spacing and radius scale.
- Output: `docs/ART-DIRECTION.md` plus the token file for the chosen stack.

### 1d. Architecture and crew assignment

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

### 1e. Project CLAUDE.md

Use the `init` skill to generate or refresh it rather than hand-writing the file. Create or update the project's `CLAUDE.md` before building, not after. It must carry: the stack, the commands, the art direction tokens summary, the crew convention, and any project-specific law. If one exists, update it rather than overwriting, and preserve hard-won rules already in it.

Get plan approval from the user before Act.

---

## Phase 2: Act

Execute the crew table. For each phase, spawn the assigned agent with `Agent`, passing:
- The full contents of `docs/ART-DIRECTION.md` (agents start cold and cannot see your context).
- The specific slice of `docs/PLAN.md` they own.
- The explicit boundary: what they must not touch.

Run independent phases in parallel where the dependency column allows it. P3, P5, and P6 usually can overlap.

Each agent writes its own files and reports back. You do not rewrite their work in the main thread, you send it back with notes if it misses.

### Review in batches, not one fix at a time

When a build comes back, do one uninterrupted pass through the whole site and write down everything wrong, then send it all as a single set of revisions. Fixing one thing at a time costs a full round trip per item, and it hides the pattern: five spacing complaints in one list is a token-scale problem, whereas the same five reported one by one get patched individually and the cause survives.

Route the batch by weight: structural or design-level changes go back to the model that owns that decision, while mechanical edits (type sizes, spacing, removing a stray divider) go to a cheap model. Do not spend top-tier tokens deleting a border.

Then **P9 integration is a real phase**, not a merge commit. The integrator's job is to make nine agents' output read as one designer's hand: consistent spacing rhythm, consistent motion timing, consistent copy voice, no orphaned components, no two spinners with different easing.

### Show it before you build it

When the direction needs to be seen rather than described, or the user is likely to want to move things by hand, use the `design` canvas skill to lay out artboards first. Cheaper to redirect a mockup than a built page, and it gives the user something to react to instead of approving a document.

### AI features

Any client build with an LLM feature in it: read `claude-api` before writing the first line. Model ids, pricing, tool use, and caching change, and answering from memory is how a client gets quoted against a model that no longer exists.

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

Each of these has a dedicated skill and a specialist agent installed. Route to them per the motion routing table above rather than improvising. Law 6 applies here more than anywhere: hand-written GSAP when `gsap-scrolltrigger` is installed is the single clearest example of the waste that law exists to prevent.

Every motion decision respects `prefers-reduced-motion`. Non-negotiable.

---

## Phase 3: Audit

Three audits, run by agents that did not build the thing.

**Security** (`kaga-security-auditor`, see `kaga-audit`): dependency CVEs, secret leakage, auth and RLS correctness, input validation, XSS and injection surface, CSP and headers, rate limiting, exposed admin routes.

**Quality and UAT** (`kaga-uat-agent`): does it match `PLAN.md`, does every acceptance criterion pass, responsive at 375 / 768 / 1440, keyboard path, screen reader landmarks, WCAG AA contrast, Lighthouse, real browser verification via the Browser pane tools with screenshots as proof. Run `design:accessibility-review` for the WCAG pass rather than improvising a checklist, and `engineering:testing-strategy` when the build needs an actual test suite rather than a one-off walkthrough.

**Design integrity** (`kaga-art-director`, returning): does the built thing match the art direction, or did defaults creep back in. Explicit hunt for: default fonts, default palette values, unstyled components, inconsistent radii, bland empty states, missing hover and focus states, greybox images.

**Launch sweep** (`kaga-launch-check`): the twenty-point gate covering horizontal scroll, broken links and buttons, mobile menu, favicon, titles, meta descriptions, custom 404, dynamic copyright year, compressed images, placeholder text, dead nav, clickable logo, `tel:` and `mailto:` links, and designed success and error states. Mandatory on every build. These are the things a client's customer hits in the first thirty seconds, and every one of them is cheap to fix and embarrassing to miss.

Findings go to `docs/AUDIT.md` with severity. Blockers get fixed and re-audited. Do not report a build as done with open blockers.

### Enforcement: prove the specialists were used

Law 6 is checkable, so check it. Before signing off Phase 3, answer these in writing in `docs/AUDIT.md`. A "no" is a finding against the build, not a note.

- Which type foundry did the display and text faces come from, and is the licence valid for commercial client use? Neither may be on the banned list in `kaga-art-direction` without a written justification.
- Which animated component library supplied the interactive components, and were they restyled to the tokens rather than shipped in their default skin?
- Which motion specialist implemented each animation, and does every timing trace back to the motion language?
- Are all page transitions and entrance choreography accounted for, with a reduced-motion fallback verified by emulation?
- Was every image sourced against a written per-section intent, and is the whole set graded as one?
- Are there any raw Tailwind default colour classes left in the codebase?

If any answer is "we hand-rolled it", that is the exact waste Law 6 exists to prevent. Say so plainly rather than letting it pass.

---

## Phase 4: Business Doc

Invoke `kaga-quote`. Produces `docs/BUSINESS-CASE.md`: true development cost, tool and subscription burn, overheads, margin, and the single number to put in front of the client. This is a separate deliverable from the build and is never shown to the client as-is, it is the internal basis for the quote.

For the client-facing `docs/QUOTE.md`, render it as a real document rather than a markdown file in a repo the client cannot open. Use `anthropic-skills:docx` for a written proposal, or `anthropic-skills:pptx` when the pitch is a meeting rather than an email. A $10k proposal delivered as raw markdown undercuts the price before they read the number.

---

## Phase 5: Launch

Only after Phase 3 has no open blockers.

Run `engineering:deploy-checklist` first. It covers CI state, migrations, feature flags, approvals, and rollback triggers, so do not write your own version of that list.

**Deploying.** If the Vercel MCP tools are connected, use them rather than shelling out: `deploy_to_vercel` to ship, `get_deployment_build_logs` when a build fails, `get_runtime_errors` and `get_runtime_logs` to confirm the deployed site is actually healthy rather than merely built. `check_domain_availability_and_price` and `buy_domain` handle the domain, but a purchase spends the user's money, so surface the price and get an explicit yes before buying anything.

**After deploy, verify the live URL, not just the build.** A green build is not a working site. Open the deployed URL in the Browser pane, walk the critical path, and check `get_runtime_errors` before telling anyone it is live.

**Handoff.** Run `design:design-handoff` for the spec sheet and `engineering:documentation` for the README and any runbook the client's own developer will need. Give the client: the live URL, the repo, the ongoing costs they now carry, and the written record of what they own.

---

## Standing quality bar

Before you call anything finished, all of these are true:

- [ ] `kaga-launch-check` run in full, every item PASS or explicitly N/A, zero UNVERIFIED
- [ ] Fonts come from a named foundry, are licensed for commercial use, self-hosted or preloaded, and are not on the banned default list
- [ ] Premium components and animation came from the installed specialist libraries, restyled to tokens, not hand-rolled
- [ ] Every image sourced against a written per-section intent and graded as one set
- [ ] `kaga-conversion` checklist passed: hero answers who/what/next in five seconds, CTAs are the highest-contrast element, no ghost button carries a primary action
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
