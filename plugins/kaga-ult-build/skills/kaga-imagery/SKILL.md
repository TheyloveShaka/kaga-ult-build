---
name: kaga-imagery
description: Build and resolve the image plan for a site - inventory every image slot, decide stock vs generated vs client-supplied, source or prompt the assets, and produce a written ask for anything only the client can provide. Use during planning of any site build and again before launch, or when the user mentions images, photography, hero image, assets, stock photos, placeholders, or greyboxes.
---

# Imagery

Images sell the site. A beautiful layout wrapped around greyboxes reads as unfinished at any price point, and a site with one bad stock photo reads as cheap regardless of the code quality.

Every build carries an image plan. It is created in Plan and it must be fully resolved before the build is called done.

## Step 1: Inventory every slot

Walk the route map and list every image the design needs. For each:

```
ID:        hero-primary
Route:     /
Role:      Hero background, full bleed, text overlays left third
Ratio:     16:9 desktop, 4:5 mobile crop
Weight:    Critical (first paint, LCP element)
Subject:   <what must literally be in frame>
Source:    stock | generate | ASK CLIENT | existing
Status:    open | sourced | approved
```

Weight matters: a critical hero justifies a licensed photo or a commissioned shoot. A tertiary card thumbnail does not.

## Step 2: Decide the source

**ASK CLIENT** when the image must be true. Real premises, real staff, real product, real work. No amount of stock or generation substitutes for a photo of the actual thing, and faking it is a credibility risk for the client. Default to this for local businesses, venues, services, and portfolios.

**Stock** for context, texture, atmosphere, and abstract support. Prefer sources whose licence is clean for commercial client work:
- Unsplash, Pexels, Pixabay for free commercial use, but audit for the overused shots
- Paid libraries when the budget carries it, and put the line item in the quote

Screen every stock candidate against: does this look like stock. If it has the glossy handshake energy, reject it.

For an African or Ugandan market build, actively source imagery that reflects the actual audience. Generic Western stock in a Kampala business's hero is a visible mistake and clients notice it.

**Generate** for assets that do not exist and do not need to be true: abstract textures, 3D product renders, exploded views, gradients, background art, pattern work.

The asset-assembly move worth knowing: generate a clean hero render of the subject and a matching exploded or deconstructed version, then drive the transition between them with scroll. Write the generation prompt with full specificity, subject, lighting, material, camera, background, aspect, and keep both renders on the same seed and framing so they align.

**Existing** for Track A rebuilds, where the client's current site already has usable assets. Extract them, then judge them honestly. Reusing a bad image because it was already there is not a saving.

## Step 3: Produce the client ask

Anything marked ASK CLIENT becomes a single consolidated request, written for a non-technical reader. Not a scattering of questions across a build.

```markdown
## Photos we need from you

To finish the site we need <N> images. Phone photos are fine if they are
well lit and horizontal.

1. **The main hero shot**: <exact description of what to photograph>
   Why: this is the first thing every visitor sees.
   Ideal: landscape, good natural light, <specific guidance>.

2. ...

If any of these do not exist, tell us and we will source an alternative.
```

Surface this to Kaga early, not at launch. Clients are slow, and a build that stalls waiting on photos is a build that ran late for a reason that was predictable in week one.

## Step 4: Technical treatment

Non-negotiable for every image that ships:

- Modern format with fallback: AVIF or WebP, JPEG behind it
- Correct dimensions per breakpoint, `srcset` and `sizes` set honestly
- `next/image` on Next.js builds, which handles most of the above, but the `sizes` prop still has to be right
- LCP image preloaded and never lazy loaded, everything below the fold lazy
- Explicit width and height or aspect-ratio to reserve layout space, zero CLS
- Real `alt` text written for meaning, empty `alt=""` only for genuine decoration
- Art direction with `<picture>` where the mobile crop needs different framing, not just a squeeze

Treatment for cohesion: pick one grade and apply it across every photo. A consistent grade, a consistent grain, or a consistent duotone is what makes mixed-source imagery look commissioned rather than collected.

## Step 5: Close the plan

Before the build is done, every slot reads `approved`. Any slot still `open` is a launch blocker, and it goes in `docs/AUDIT.md` as one.

Write the plan to `docs/IMAGE-PLAN.md` and keep the status column current as the build runs.
