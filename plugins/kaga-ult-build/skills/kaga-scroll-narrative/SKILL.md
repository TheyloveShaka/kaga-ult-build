---
name: kaga-scroll-narrative
description: Design the scroll as a story rather than a sequence of sections - the descent, the transformation, the assembly, the reveal - and specify the shot list, generated media, and choreography that make a site read as a premium cinematic build. Use for any hero-led marketing site, product launch, or flagship page where the scroll itself is the experience, or when the user asks for a cinematic, immersive, Apple-style, or award-shortlist site.
---

# Scroll Narrative

The difference between an animated site and a beautiful one is that a beautiful one is *about* something as you move through it. Sections that merely fade in on scroll are a site with animation applied. A scroll narrative is a site with a spine.

Use this when the scroll is the experience. Skip it for dashboards, directories, and anything where the user came to complete a task rather than to be persuaded.

## The structures that work

Pick one and commit. Mixing two produces incoherence, which is exactly what `kaga-integrator` will flag.

**Descent.** The viewer travels downward through space: through cloud, into a valley, down to the property, into the water. Each scroll beat is a layer of altitude, and copy arrives as you pass through. Works for place, travel, property, and anything with physical scale.

**Assembly.** Components enter separately and converge into the finished product at the bottom. Fruit falls, tumbles, blends, becomes the bottle. The product is the payoff and it is the last thing you see. Works for anything manufactured, mixed, crafted, or composed.

**Exploded to whole, or whole to exploded.** The object separates into its parts so you can see the engineering, then reassembles. Two renders on identical framing and seed, scrubbed against each other. Works for hardware, tools, engineered goods, and anything where craft is the selling point.

**Transformation.** One thing becomes another across the scroll: raw to finished, before to after, problem to solution. Works for services and process-led businesses.

**Journey or timeline.** Linear progression through stages, each a beat. Works for process explanation and origin stories, and it is the safest of the five when the subject has no strong physical form.

## Build the shot list before you build anything

The shot list is the deliverable of this skill. Write it into `docs/SCROLL-NARRATIVE.md` before any component or asset exists, because the media has to be generated to fit the beats and regenerating it later is the expensive mistake.

```
Beat 1  0 to 15vh
  Visual:    single strawberry, frozen mid-fall, hard top light, deep shadow
  Media:     generated still, 16:9, seed locked
  Copy:      eyebrow + one line, "Picked at dawn"
  Motion:    pinned, scrub-driven rotation, no autoplay
  Exit:      hands off to beat 2 at matching vertical position

Beat 2  15 to 35vh
  ...
```

Every beat states: the visual, where the media comes from, the copy intent, the motion behaviour, and how it hands off to the next beat. Handoff is where these sites break: two beats that each look fine but jump at the seam.

## Rules that separate premium from busy

**One idea per beat.** If a beat needs two sentences to explain, it is two beats.

**The payoff is last.** Whatever you are selling arrives at the bottom, fully assembled. Everything above is the argument.

**Scrub, do not autoplay.** The viewer controls the timeline. Motion tied to scroll position reads as craft. Motion that plays on its own schedule while the viewer scrolls past reads as a banner ad.

**Continuity of framing across beats.** Generated media must share seed, camera, lighting, and background treatment. Two beautiful renders that do not match are worse than two plain ones that do.

**Earn the pin.** Pinning a section steals the viewer's scroll. Only pin when something is genuinely happening in that held frame.

**Leave the exits open.** A narrative site still needs a nav, a way to skip to the CTA, and a route out. Immersive is not a reason to trap someone.

**Reduced motion gets a designed static version**, not an empty page. The narrative collapses to a well-composed stack of the key frames with the copy intact. Specify it beat by beat, and verify it by emulating the setting.

## Cost discipline for generated media

Generated video is usually the single largest line item on this kind of build, and it is easy to spend badly.

- **Generate audio only if the site uses audio.** Most do not. Rendering silent cuts the credit cost substantially, and it is the most common avoidable waste.
- **Lock the concept before you render.** Regenerating a shot because the narrative changed is the expensive mistake, which is exactly why the shot list comes first.
- **Prompt with full specificity**: subject, material, lighting, camera, lens feel, background, aspect, motion. A vague prompt costs the same as a precise one and gets thrown away.
- **Reuse framing across beats** rather than generating each one from scratch.
- **Render at the delivered resolution**, not above it.
- **Budget the credits into `docs/BUSINESS-CASE.md`** as a real project cost, and record actual spend as you go.

Sequence: still frames first to lock composition cheaply, then video only for the beats that genuinely need motion. A site does not need every beat to be film.

## Generative media sources

The pipeline is source-agnostic. Whatever is connected, the requirements are the same: seed and framing continuity, silent unless audio is designed, and specified rather than improvised prompts.

**Higgsfield** is the option this method was designed against. It carries image and video models behind one CLI, authenticated with a device login, and once connected the generation can be driven in plain language. It is a paid service billed in credits, so treat it as a project cost, get the user's agreement before spending on a client job, and record what was spent.

If nothing is connected, say so and fall back: source the hero from stock video, build the narrative from stills with CSS and GSAP transforms, or mark the beat as an asset the client must supply. A scroll narrative built on stills and good choreography still beats a generic site with a stock video header.

## Verify it, do not describe it

Open the built page in the Browser pane and scroll it. Watch the beats. Check the seams. Confirm the frame rate holds on a mid-range budget, confirm the mobile variant does not just run the desktop choreography at a worse cost, and confirm the reduced-motion fallback renders a real page.

Screenshots at each beat go into the UAT report as evidence.
