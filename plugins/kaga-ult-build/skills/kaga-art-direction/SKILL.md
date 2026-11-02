---
name: kaga-art-direction
description: Research and lock the visual spine of a build - colour palette with rationale and contrast maths, typography pairing with load strategy, motion language, and spacing/radius scale - then emit the token file for the stack. Use after reference hunt and before any component is written, or when the user asks about colours, colour palettes, fonts, typography, design tokens, theming, dark mode, or says a design looks bland or generic.
---

# Art Direction

Produces `docs/ART-DIRECTION.md` and the token file. Everything downstream reads from these. An agent that invents a colour is out of spec.

## Colour

### Research, do not vibe

Start from the brief and the references, then research the actual sector. Colour carries meaning that varies by market and category. State the reasoning in one line per decision.

Sources worth consulting: the extracted brand (Track A), competitor palettes to deliberately differ from, cultural colour associations in the target market, and accessibility constraints.

For the East African and Ugandan market specifically, check the assumption before importing a Western palette convention wholesale.

### Build it from a source, in OKLCH

Palettes invented from adjectives ("modern, trustworthy") land on the same few AI choices every time. Start from something real, in this order: the client's own assets (Track A), the hero photograph (sample its dominant and accent colours), or a reference Kaga picked. Name the source next to every hue.

Build the ramps in OKLCH, not hex. Lightness should be the only thing that steps between shades; hex hides that, and HSL greys out its darkest and lightest shades. oklch.com is a quick picker and checker.

- **Neutrals first.** Choose the neutral ground, then tint it toward the brand hue at very low chroma (about 0.005 to 0.02) so it belongs to the palette.
- **Surfaces by lightness.** Dark mode: the base, then roughly +0.05 and +0.10 lightness for raised and top surfaces; the lighter the surface, the closer it feels, so save the lightest for what matters. Light mode: start from 1 minus each value, then adjust so the top surface is the lightest and the base the darkest.
- **Two text shades.** Headings high contrast but not pure white or black (around 0.95 lightness in dark mode); body slightly muted (around 0.75 to 0.8). Both still pass.
- **One brand colour, chroma kept sane.** UI colour rarely needs chroma above 0.15 to 0.2. Hover and pressed states move lightness, not hue.
- **Light comes from above.** In dark mode a gradient between two surface shades plus a slightly lighter top border reads as a lit edge. In light mode the border matches the surface and depth comes from a two-layer shadow: a short darker one plus a long soft one.
- Emit tokens as `oklch()` values; every current browser supports them, including Chrome on mid-range Android.

### The structure

Do not ship a single brand colour and five greys. Build:

| Role | Count | Notes |
|---|---|---|
| Primary | 1 + 9 step ramp | The brand's spine |
| Secondary | 1 + ramp | Supports, never competes |
| Accent | 1 | Used sparingly, earns attention |
| Neutral | 10 step ramp | Warm or cool, chosen deliberately, never pure `#000`/`#fff` unless argued for |
| Semantic | success, warning, danger, info | Tuned to the palette, not stock red/green |
| Surface | 3 to 4 elevations | Background, raised, overlay, sunken |

### Distribution: roughly 60 / 30 / 10

Having the right colours is not the same as using them in the right proportion. A palette applied evenly reads as loud and cheap.

- **~60% dominant**, usually the neutral ground: backgrounds, surfaces, large fields.
- **~30% brand**, carrying identity across sections without saturating them.
- **~10% accent**, reserved so it still has force where it lands: primary CTAs, the one thing per section that must be noticed.

Not a law, a starting discipline. Break it deliberately and say why. The common failure is spending the accent everywhere, after which nothing stands out and the CTA competes with decoration. See `kaga-conversion`.

### Premium colour signals

Premium palettes usually lean on near-black, near-white, and restrained neutrals so the imagery carries the colour. Loud yellows and reds read as sale, fast food, and impulse buying unless that is the intent. This is a default for premium work, not a law: bright colour can be premium when it is deliberate and used sparingly. For a premium wordmark, a clean, well-set name with no pictogram is the convention in fashion and lifestyle; other sectors, such as watches and cars, differ, so check the sector's references.

### Palettes that read as AI-made

Avoid unless the client's brand or Kaga's chosen reference supplies them: indigo or violet primaries, indigo-to-purple and blue-to-teal gradients, lime or neon green on near-black, gradient headline text, Tailwind's stock hues, multi-colour mesh backgrounds behind body text, and an accent spent on every icon. A gradient, when used, stays within one hue.

### Rules

- Every value gets a token name. No hex in components.
- State the contrast ratio for every text-on-surface pairing. Body text hits 4.5:1, large text 3:1, UI borders 3:1. Show the number, do not assert it.
- Neutrals are almost never pure grey. Tint them toward the primary's hue for cohesion, and say by how much.
- Dark mode is a designed mapping, not an inversion. Dark surfaces lift, saturated colours desaturate, pure white text becomes a near-white.
- Zero raw Tailwind defaults in the codebase. `bg-blue-500` is a bug.

### Emit

CSS custom properties on `:root`, redefined under `@media (prefers-color-scheme: dark)` guarded with `:root:not([data-theme="light"])`, and again under `:root[data-theme="dark"]` so an explicit toggle wins both ways. Wire Tailwind's theme to those variables rather than duplicating the hexes.

## Typography

### Pairing

Choose two, occasionally three. Justify each against the audience and the medium, not against fashion.

- **Display / headline**: carries the personality. Can be expressive, can be a variable font, can be tight-tracked at large sizes.
- **Text / body**: carries the reading load. Optimised for the actual paragraph length on the page.
- **Mono**, only if the product has code, data, or numerics that need it.

### Banned by default

Two lists. The first are the faces reached for when no decision is made. The second is the newer AI default: the faces generated sites land on so often that Kaga reads them as "Claude defaults" on sight.

- **Generic defaults:** `Inter`, `Roboto`, `Open Sans`, `Lato`, `Montserrat`, `Poppins`, `Nunito`, `Raleway`, `Source Sans`, `system-ui` as a primary, and any bare `font-sans` / `font-serif` / `font-mono` Tailwind default.
- **The AI-default look:** `Geist`, `Geist Mono`, `Instrument Serif`, `Space Grotesk`, `DM Sans`, `Manrope`, `Plus Jakarta Sans`, `JetBrains Mono`, `Satoshi`, `Clash Display`, `General Sans`, `Cabinet Grotesk`, `Switzer`, `Fraunces`, `Bricolage Grotesque`, `Sora`, `Outfit`.

Banned as patterns too, whatever the face: an italic serif accent word inside a sans headline, uppercase mono eyebrow labels with wide tracking, and a small tag pill above the hero headline. Together they are the most recognisable AI hero.

A face from either list ships only if Kaga picks it from a rendered specimen (see "Kaga picks from specimens"). A written justification is not enough.

### Where to actually look

Search by character, not by name. A named shortlist in this file would become the next default, so there deliberately is none. Describe what the brief needs ("a warm humanist serif that holds up at 16px", "a condensed grotesque with real weight at display sizes") and search for that.

| Source | How to use it |
|---|---|
| **Fontshare** (fontshare.com) | Free for commercial use. Filter by category and go well past the first page; the front page is the default set. |
| **Google Fonts** | Free, self-hostable. Sort by newest or trending, never by most popular. |
| **Libre foundries** (Velvetyne, Collletttivo) and **uncut.wtf** as a catalogue | Characterful display faces that generated sites rarely use. Check each licence; uncut.wtf lists faces under mixed terms. |
| **Future Fonts** (futurefonts.xyz) | Inexpensive in-progress faces from independent designers. |
| **Adobe Fonts** | Included with a Creative Cloud seat. |
| **Foundries** (Klim, Grilli Type, Pangram Pangram, Colophon, Displaay, ABC Dinamo, Commercial Type) | When the budget carries a licence. At $10k a display licence is a legitimate line in `docs/BUSINESS-CASE.md`. Pangram Pangram's free downloads are for personal use only. |
| **Variable fonts** | One file, full weight and optical-size range. Prefer them above three weights, and for restrained weight or slant animation. |

Never carry the previous build's pick into the next one by default. Faces Kaga approved before (Boska with Martian Mono on Kaga Systems) belong to that build.

**Check the licence before you commit.** Free for personal use is not free for a paying client's commercial site. Record the licence for every face in `ART-DIRECTION.md`, and if a paid licence is needed, say who buys it, you or the client.

### Pairing that reads as one system

Two faces, occasionally three, and they must relate deliberately:

- **Contrast pairing**: expressive display against a quiet workhorse text face. The most reliable premium look.
- **Superfamily**: a serif and sans from the same designer, sharing skeleton and metrics. Cohesive by construction.
- **Single family, worked hard**: one variable face used across a real range of weight, size, and optical size. Restraint, done properly, reads as confidence.

Whatever the approach, the two faces must not merely coexist, they must look chosen together. State the relationship in one line.

### Market fit

Match the face to the audience, not to a Dribbble shot. For a Ugandan or East African client, check that the face carries any diacritics the copy needs, that it renders correctly at the sizes real users will see it on mid-range Android, and that the whole set is small enough to load on a slower connection. A beautiful face that ships 400KB and blocks first paint is a worse decision than a plain one.

### Scale and rhythm

- A modular scale with a stated ratio. 1.2 for dense UI, 1.25 to 1.333 for marketing, 1.5+ only for editorial drama.
- Fluid sizing with `clamp()` for anything above body size.
- Line height inverse to size: tight for display, generous for body.
- Measure capped at 60 to 75 characters. `max-w-prose` is not automatic, set it deliberately.
- Optical tracking: negative at display sizes, near zero at body, positive for small caps and eyebrows.

### Name the font, never let it be inferred

A model shown a reference image will guess the typeface, and it guesses wrong. The result is a build that looks close but not right, and the reason is invisible until someone names it.

So identify the face explicitly, then pass the name to whoever builds. To match a face from a reference: compare against a catalogue of popular faces visually, or use a font identification service (for a logo, fontinlogo.com lists the faces behind well-known marks), then confirm by setting the same string in the same weight and comparing letterforms side by side. Look at `a`, `g`, `R`, and the numerals, which differ most between similar faces.

Then in every downstream prompt and spec: state the family name and where it loads from. "Use [family], self-hosted from [source], weights 400 and 700" is a specification. "Match the font in the reference" is a guess with extra steps.

### Loading

Self-host or `next/font`. Preload the display face. `font-display: swap` with a metric-matched fallback so the layout does not jump. State the strategy, do not leave it to the framework.

## Kaga picks from specimens

Hex swatches and font names in a document are not a decision; they are how defaults slip through. For the palette and for the type pairing, render three genuinely different options on the real hero section: the actual background, headline, body, a card, and the primary button, at 1440px and 375px. Kaga picks one or mixes. Record the pick and the two rejected options in `ART-DIRECTION.md`. Nothing downstream starts until this is done.

## Motion language

Write it down once, then every agent follows it:

- **Durations**: a scale, typically 120ms micro, 240ms standard, 400ms entrance, 700ms+ narrative. No arbitrary numbers in components.
- **Easing**: name the curves. A custom cubic-bezier for the brand's feel beats `ease-in-out` everywhere.
- **What moves**: entrances, state changes, scroll narrative. **What does not**: body copy, form fields under input, anything that would delay a user's action.
- **Stagger**: the interval and the direction.
- **Reduced motion**: the fallback for every single one of the above. Not "animations off", a designed static state.

## Craft numbers

The small, specific settings that separate a professional finish from a default one. Starting points, not laws; deviate on purpose.

- **Large type**: tracking about -2% to -3%, line height 110% to 120%. Untightened display type is the quickest tell of a default build.
- **Size count**: per view, about four sizes and two weights; across a landing page, about six sizes. Count them before showing; more is the beginner tell. Dashboards keep body and labels at 24px or below; hero stat numerals are the exception.
- **Spacing on a 4px base**, with related items grouped tighter than unrelated ones (for example 8 to 16px inside a group, 32px or more between groups). The spacing itself carries the hierarchy.
- **Shadows**: low opacity, large blur. Cards need very little; popovers and modals need more. If the shadow is the first thing you notice, it is wrong.
- **Dark mode depth** comes from lighter surfaces, not shadows: the more elevated, the lighter. Borders drop in contrast, chips lose saturation, and deep purples, reds, or greens are all valid darks, not only navy and grey.
- **Icons sized to the line height** of the text beside them, 24px icon to 24px line height. Oversized icons are the common mistake.
- **Button padding** about twice as wide as tall, with default, hover, pressed, disabled, and loading states.
- **One radius per size class.** Small components (inputs, buttons, chips) share one radius, and twins such as Back and Skip are identical in size, radius, and style.
- **Pills are a shape decision, not a default.** Full rounding is one stop on the radius scale, used only where the chosen reference uses it. Count the pill shapes on a page; more than a handful on a marketing page is the AI look Kaga rejects.
- **Effects earn their place.** Remove a shadow before tuning it, keep gradients within one hue, and delete arrows, strokes, and labels that repeat what a heading already says.
- **Icons from one library** with matched stroke width, corners, and fill. Different styles only in visually separate zones. Unfamiliar icons get a label or tooltip.
- **One primary colour**, with tints for backgrounds and shades for text. Semantic colours carry meaning (blue trust, red danger, amber warning, green success) and are never decoration.

## Spacing, radius, elevation

**Content layout before container layout.** Let whitespace form groups first, then add a surface only where something deserves emphasis. Boxing every group is the most common reason generated UI looks cheap. The full rule and its test live in `kaga-product-ui`.


- Spacing scale on a consistent base, usually 4px, stated explicitly.
- Radius scale with a rule for which elements get which. Uniform radius everywhere is a default, and defaults are banned.
- Elevation as a designed shadow ramp, tinted with the palette's hue, never `box-shadow: 0 1px 3px rgba(0,0,0,.1)` copied four times.

## Output

`docs/ART-DIRECTION.md` contains every decision above with its one-line rationale, plus a swatch table with hex and contrast numbers. The token file lands in the codebase. Both are passed verbatim into every downstream agent's prompt, because agents start cold.

## Self-check before handoff

- [ ] Every colour has a name, a role, and a reason
- [ ] Every text pairing has a stated contrast ratio that passes
- [ ] Dark mode is mapped, not inverted
- [ ] Fonts are chosen with an argument, and the load strategy is written
- [ ] Motion has durations, curves, and a reduced-motion fallback
- [ ] Nothing in the document is a framework default
- [ ] No face from either banned list unless Kaga picked it from a specimen
- [ ] The palette names its source and was picked from three rendered options
- [ ] Pill shapes appear only where the radius scale assigns them
