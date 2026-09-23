# Skill routing

Reference for `kaga-ult-build`. Read only when the phase needs it.

## Main routing table

**Law 6: do not reinvent an installed skill.** Kaga's environment carries deep skills that already solve most of what this pipeline needs. Writing your own accessibility pass when `design:accessibility-review` exists is wasted work and a worse result. Before any phase, check this table and invoke what is listed.

| Phase | Invoke these skills | Delegate to these agents |
|---|---|---|
| Before any paid dispatch | `kaga-budget` (mandatory when routing to API models) | |
| 0 Reference hunt | `kaga-reference-hunt`, `modern-web-design` | |
| 1a Extraction | `kaga-art-direction` | |
| 1b Concepts + adversarial gate | `kaga-scroll-narrative` for the structure of each concept | a *different* agent attacks the chosen concept |
| 1c Art direction | `kaga-art-direction`, `kaga-conversion`, `design:design-system`, `anthropic-skills:theme-factory`, `modern-web-design` | `kaga-art-director`, `modern-web-design:modern-web-design-specialist` |
| 2 Conversion pass | `kaga-conversion`, `design:ux-copy` | `kaga-content-seo`, `kaga-ux-architect` |
| 1d Architecture | `engineering:system-design`, `engineering:architecture` (ADR for any real tech choice), `design:user-research`, `design:research-synthesis` | `kaga-ux-architect` |
| 1d Shot list + image plan | `kaga-scroll-narrative`, `kaga-imagery` | |
| 2 Scroll narrative | `kaga-scroll-narrative`, `gsap-scrolltrigger` | `kaga-motion-engineer` |
| 2 Product UI, dashboards, app screens | `kaga-product-ui` (house dashboard language, state-complete components) | `kaga-frontend-engineer` |
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
