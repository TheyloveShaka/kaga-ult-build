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

Never ship the framework default. Never ship a system stack by accident. Inter is not a decision, it is the absence of one, so if you land on it, argue for it explicitly.

Good hunting grounds: Google Fonts for licence-free production use, Fontshare, and the variable font catalogues. For a $10k build, a licensed foundry face is a legitimate line item in the quote.

### Scale and rhythm

- A modular scale with a stated ratio. 1.2 for dense UI, 1.25 to 1.333 for marketing, 1.5+ only for editorial drama.
- Fluid sizing with `clamp()` for anything above body size.
- Line height inverse to size: tight for display, generous for body.
- Measure capped at 60 to 75 characters. `max-w-prose` is not automatic, set it deliberately.
- Optical tracking: negative at display sizes, near zero at body, positive for small caps and eyebrows.

### Loading

Self-host or `next/font`. Preload the display face. `font-display: swap` with a metric-matched fallback so the layout does not jump. State the strategy, do not leave it to the framework.

## Motion language

Write it down once, then every agent follows it:

- **Durations**: a scale, typically 120ms micro, 240ms standard, 400ms entrance, 700ms+ narrative. No arbitrary numbers in components.
- **Easing**: name the curves. A custom cubic-bezier for the brand's feel beats `ease-in-out` everywhere.
- **What moves**: entrances, state changes, scroll narrative. **What does not**: body copy, form fields under input, anything that would delay a user's action.
- **Stagger**: the interval and the direction.
- **Reduced motion**: the fallback for every single one of the above. Not "animations off", a designed static state.

## Spacing, radius, elevation

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
