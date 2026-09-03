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

**Stock** for context, texture, atmosphere, and abstract support.

### Sourcing premium stock, per section

Source images **during the build, section by section**, against that section's role and the art direction. Do not batch-pick a folder of nice photos up front and distribute them afterwards, that is how a site ends up looking like a mood board rather than a designed thing.

For each slot, write the search intent from the art direction before searching: subject, mood, palette fit, orientation, and where the text will overlay. Then pick against that intent rather than picking whatever looks nice.

| Source | Licence | Best for |
|---|---|---|
| **Unsplash** | Free commercial, no attribution required | Editorial, atmospheric, texture. Deep but heavily overused, so go past page one. |
| **Pexels** | Free commercial | Lifestyle, people, video too. |
| **Pixabay** | Free commercial | Fills gaps, generally weaker curation. |
| **Burst** (Shopify) | Free commercial | Product and ecommerce contexts. |
| **Nappy** | Free commercial | Genuinely good imagery of Black and brown people, which most libraries handle poorly. |
| **Unsplash+ / Adobe Stock / Stocksy** | Paid | When the hero has to carry the whole page. Stocksy in particular does not look like stock. Put the licence in `docs/BUSINESS-CASE.md`. |

**Reject on sight:** the glossy handshake, the laughing-alone-with-salad genre, fake diverse-team-around-a-laptop, anything with a visible competitor's branding, and any shot you have already seen on three other sites. If a candidate feels familiar, it is overused, and a client who recognises their hero image from a template has lost confidence in the whole build.

**Market fit is not optional.** For a Ugandan or East African client, source imagery that reflects the actual audience and setting. Generic Western stock in a Kampala business's hero is immediately visible to the people it is meant to convert, and clients notice it before they notice anything you did well. `Nappy` and targeted searches on the free libraries handle most of this; where they do not, that slot becomes an `ASK CLIENT`.

### Cohesion

Mixed-source imagery only looks commissioned if it is graded as one set. Pick one treatment in `ART-DIRECTION.md` and apply it to every photo: a consistent colour grade, a consistent contrast curve, an optional shared grain or duotone. State the treatment, then apply it, and check the set side by side rather than image by image.

**Generate** for assets that do not exist and do not need to be true: abstract textures, 3D product renders, exploded views, gradients, background art, pattern work.

The asset-assembly move worth knowing: generate a clean hero render of the subject and a matching exploded or deconstructed version, then drive the transition between them with scroll. Write the generation prompt with full specificity, subject, lighting, material, camera, background, aspect, and keep both renders on the same seed and framing so they align.

### Generated video, and how not to overspend on it

On a cinematic build the hero is often generated video rather than a still, and it is usually the largest single cost on the job. Four rules keep it sane:

1. **Silent unless the site uses audio.** Rendering with audio costs materially more and most sites never play it. This is the most common avoidable waste on this kind of build.
2. **Lock the shot list first.** See `kaga-scroll-narrative`. Regenerating because the narrative shifted is the expensive mistake, and it is entirely preventable.
3. **Stills before film.** Lock composition with cheap still renders, then spend on motion only for the beats that genuinely need it. Not every beat has to be film.
4. **Same seed, same camera, same grade across beats.** Continuity is what makes generated media read as one production. Two beautiful mismatched shots look worse than two plain matched ones.

Budget the credits as a real line in `docs/BUSINESS-CASE.md`, get the user's agreement before spending on a client job, and record actual spend as you go.

**Higgsfield** is the generation service this method was designed against: image and video models behind one CLI, authenticated by device login, driven in plain language once connected. It is paid and billed in credits. If it is not connected, say so rather than pretending, and fall back to stock video, a stills-plus-GSAP narrative, or a client-supplied asset. A well-choreographed stills build beats a generic site with a stock video header.

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
