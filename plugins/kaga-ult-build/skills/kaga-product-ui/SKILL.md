---
name: kaga-product-ui
description: Kaga's house design language for dashboards, admin panels, and app interfaces, plus the rules for state-complete components. Warm neutral canvas, one dark anchor, two saturated accents, bento grid, big numerals, pills, floating dock. Use for any dashboard, admin area, SaaS screen, portal, or in-app UI, and whenever a component has async states such as upload, payment, save, or search.
---

# Product UI

Marketing sites persuade. Product UI gets used every day by the same people. Different job, different rules, and this skill owns the second one. The house language below is Kaga's chosen default for every dashboard and app surface unless a client brand overrides it.

## The house dashboard language

Derived from a concept reference Kaga selected as his main dashboard direction. It is a concept, not a shipped product, so the rules below keep its look and add the discipline a concept skips: contrast, density, and real data.

### Canvas and anchor

- **Warm off-white canvas.** The app ground is a tinted near-white, never pure `#fff`, never cool grey. Content sits in one large rounded panel on that ground.
- **One dark anchor per view.** A single near-black element gives the page weight: the icon rail, or one hero card such as a balance total. One, not several. Two dark blocks compete, one anchors.
- **Everything else is light.** Cards are white or near-white on the tinted canvas, separated by space and a whisper of shadow, never by borders.

### Colour

- **Two saturated accents, used as full fills.** A hot orange or coral and an acid lime, each filling one hero card completely. They are surfaces, not sprinkles. A dashboard with the accent on every icon has no accent.
- **One soft tint** as a third, quieter surface: a peach or blush wash for a secondary feature card.
- **Status colour as text or a tinted pill**, never a solid saturated badge. Upcoming, In Progress, Scheduled, Failed, Successful: coloured words or a pale pill with a darker label.
- **Check the accents for contrast every time.** White text on a hot orange commonly lands near 3:1 and fails AA for body text. Use near-black text on the lime and either dark text or large bold white on the orange, and state the ratio in `ART-DIRECTION.md`.

### Layout

- **Bento grid.** Mixed card spans on a consistent gutter, large radius, generous internal padding. Hero cards span wider or taller; supporting cards stay compact.
- **Group with space, not containers.** See the content-layout rule below. A card holds one idea; inside it, whitespace separates the parts. No nested boxes, no internal dividers unless a table genuinely needs row rules.
- **A designed empty slot.** Where a user can add something, show a dashed-outline card with a single centred action. The empty state is part of the layout, not a gap in it.

### Type and numbers

- **Numerals are the hero.** Each stat card leads with a large display number, with a small muted label under it. "44 hours", "13 tasks", "$70,147.41".
- **Tabular figures** for anything that changes or aligns: money, time, counts, table columns. Use `font-variant-numeric: tabular-nums`.
- **Two text weights do most of the work**: a heavy weight for numbers and card titles, regular for everything else. Labels drop in size and contrast rather than gaining weight.
- Name the family explicitly per `kaga-art-direction`. A clean geometric sans suits this language; pick one from a real source (General Sans or Satoshi from Fontshare, or Plus Jakarta Sans from Google Fonts are good fits) rather than letting a default through.

### Components

- **Pills for everything interactive or categorical**: nav items, tabs, segmented controls, filters, status tags, and primary buttons. Primary action is a solid near-black pill; secondary is a pale pill.
- **Floating bottom dock** for switching between top-level views: a compact dark segmented pill fixed at the bottom centre. It keeps navigation reachable without a heavy header.
- **Top bar as a row of small pills**: home, a primary add action, search, notifications, plus ambient context such as time and weather.
- **Dark icon rail** with a notched active state: the active icon sits in a curved cut-out that joins the rail to the content panel, so position reads without a label.
- **Date pickers as chip rows**: day name over date, the selected day a solid dark chip.
- **Event and list rows** carry a thin left accent bar in their status colour.
- **Organic gradient shapes inside stat cards** as decoration, low contrast, kept to the card corners so they never sit behind numbers.

### Charts

- Smooth spline lines in the accent colours, no heavy axes, faint or no gridlines.
- **Data labels as small dark pills** sitting on the line, instead of a legend the eye has to cross-reference.
- Highlight the current or selected value with a soft column wash and a floating pill tooltip.
- Read `dataviz` before writing the first line of any chart code.

### Warmth

A personal greeting with the user's name and a short line of welcome, and ambient context such as local time and weather. It costs almost nothing and it is most of why this language feels like a product someone cares about rather than an admin template.

### Motion

Cards lift a few pixels on hover. Numbers count up once on first load, never on every re-render. View changes cross-fade within the panel while the rail and dock stay still. All of it respects `prefers-reduced-motion`.

## Content layout, not container layout

The most common reason generated UI looks cheap: every group gets its own box. Header in a tinted block, stats in another tinted block, a divider under that, the whole thing inside a card.

Do the opposite. **Let whitespace form the groups first.** Proximity alone tells the eye what belongs together. Then, and only where something deserves emphasis, add a surface: a coloured header, a filled card, a tinted row. Surfaces become a tool for hierarchy instead of a habit applied to everything.

Test: remove every background fill and border inside a card. If the groups still read, the layout is right and you can add back one surface for emphasis. If they collapse, the spacing is wrong, and more boxes will not fix it.

## State-complete components

A component is not finished when its happy path works. Every async or multi-step component designs all of its states, and this is where premium product UI visibly separates from templates.

For any upload, payment, save, submit, search, or sync:

| State | What it must show |
|---|---|
| Idle | The affordance and what it accepts: file types, limits, what happens next |
| Hover or drag-over | The target responds before the drop or click lands |
| In progress, per item | Each item's own progress, not one shared spinner |
| Partial failure | Which items failed, why, and a retry on that item alone |
| Aggregate | A plain summary: "3 of 4 uploaded, 1 failed" |
| Success | A clear, calm confirmation, then a way forward |
| Empty | Designed, never blank |

Principles:

- **The object reflects the state.** In a checkout, the card itself glows while processing and turns green on success; the form steps back so attention lands on the thing that matters. Feedback lives on the object, not in a toast in the corner.
- **Input drives the object.** Focusing the security code field flips the card to its back. The UI shows the user where the thing they are typing lives.
- **Say what is happening.** Replace a generic spinner with an indicator that names the state: searching, uploading, verifying, processing payment. The open-source `thinking-orbs` package (MIT, v0.3.2 at time of writing, plain 2D canvas, respects reduced motion) is a good fit for AI and long-running states. Verify its current version and licence before adding it to a client build.
- **Never lose work on failure.** A failed payment keeps the form filled. A failed upload keeps the file listed with a retry.
- **Warn inline, at the field.** A security or validation warning appears beside the field that caused it, not at the top of the form.

Implementation notes that make these feel expensive: animate position changes with FLIP transforms rather than layout thrash, use `@property` to make custom properties animatable, prefer spring easing for anything that follows the pointer, and route real choreography to `motion-framer` or `gsap-scrolltrigger` per Law 6.

## Navigation pattern: the refined top bar

For product and marketing nav alike: a compact bar, a sliding highlight that follows hover between items rather than each item lighting up independently, and search that expands inline from an icon instead of occupying permanent width. Frosted glass is fine over imagery, but the text must still pass contrast against the busiest thing that can scroll under it.

## Before sign-off

- [ ] One dark anchor per view, not several
- [ ] Accents used as whole-card fills, not scattered, with contrast ratios stated
- [ ] Groups formed by space; the remove-every-fill test passes
- [ ] Numbers use tabular figures and lead each stat card
- [ ] Every async component covers idle, in progress per item, partial failure with retry, aggregate, success, and empty
- [ ] No generic spinner where the state can be named
- [ ] Empty slots and empty states designed
- [ ] Font named and sourced, not defaulted
- [ ] Reduced motion honoured
