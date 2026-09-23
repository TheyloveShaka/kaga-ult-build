---
name: kaga-conversion
description: The discipline that stops a beautiful site from losing the client money - clarity, scannability, motivation, friction removal, visual hierarchy, and CTA design. Use alongside art direction on every client build, and whenever a site looks good but is not converting, or the user asks about conversion, CTAs, buttons, landing page structure, or why a redesign underperformed.
---

# Conversion

A redesign can be cleaner, more modern, and objectively more beautiful than what it replaced, and still cut the client's sales. This happens, it happens to good designers, and it is the single most expensive way a premium build can fail: the client paid more and earns less, and no amount of craft argues them out of that.

So beauty is necessary here, not sufficient. `kaga-art-direction` owns how it looks. This skill owns whether it works.

## The three that matter

**Clarity.** Within five seconds a visitor knows who this is, what is on offer, and what to do next. Test it by showing the hero to someone who knows nothing about the client and asking those three questions. If they hesitate, the hero fails, regardless of how good it looks.

Clarity is usually lost to cleverness. A headline that is a pun, a metaphor, or a mood instead of a statement. "Redefining tomorrow" says nothing. "Wedding venues in Kampala, with real prices" says everything.

**Scannability.** Nobody reads a web page, they scan it and stop where something catches. Design for that: short blocks, real subheadings, one idea per section, front-loaded sentences, and the important thing never buried in the middle of a paragraph. If the page only makes sense read top to bottom in full, it does not work.

**Motivation.** Say the thing the visitor actually cares about, not the thing the client is proud of. The client wants to talk about their twenty years of heritage. The visitor wants to know whether you have their date free and what it costs. Serve the visitor, and the client gets the sale that pays for the heritage paragraph.

## Visual hierarchy, not the F pattern

The F-pattern advice, that people read top-left, across, back, down, is outdated and repeated well past its evidence. Do not lay out a page around it.

What actually governs attention is hierarchy. On every section, rank the elements and design to that ranking:

1. The one thing they must notice: biggest, boldest, highest contrast.
2. The support: present, clearly secondary.
3. Everything else: turn the volume down. Smaller, lighter, quieter.

If three things on a section are all shouting, none of them is heard. Deliberate de-emphasis is the harder half of this and the part most often skipped.

## Why premium feels premium

- **The halo effect.** Visitors judge a site in about 50 milliseconds, and that judgment colours everything after it. Name the single feeling the hero must create in that first glance (calm, confidence, excitement) and build the hero around it. This is why the hero comes first in every build.
- **Cognitive fluency.** What is easy to process reads as trustworthy and high quality. Every removed element, clearer grouping, and simpler nav raises perceived quality, not just usability.
- **The peak-end rule.** People remember the most intense moment and the ending, not the average. Design the peaks (a satisfying micro-interaction, a hero moment) and the ending: the last section, the success state, the confirmation.
- **Start from intent, not visuals.** Decide what the visitor came to do and design that first (a search bar before a hero image on a booking site). Expand the interface only as the intent expands.

## Borrowed luxury is a trap

Luxury houses show almost nothing: no benefits, no explanation, a name and a photograph. That works because demand already exists and millions of people already want the product. An unknown brand copying that minimalism gets the emptiness without the demand.

A premium look for a small or new business comes from the same restraint in the visuals, plus the evidence a stranger needs to trust them: who they are, what they do and for whom, what they specialise in, how they work, real photos of the real people, social proof, and prices or a range. Where choosing is hard, guide it: a short quiz or selector that recommends the right option converts better than a catalogue.

## UX laws that change decisions

From lawsofux.com. Only the ones that should change what gets built:

| Law | Apply it as |
|---|---|
| Jakob's law | Keep conventions (nav at top, top-to-bottom flow, obvious CTAs); be distinctive inside them, not against them |
| Hick's law | Fewer choices per step; split complex tasks into steps |
| Fitts's law | Primary targets large and near the thumb or cursor path |
| Von Restorff effect | The primary action looks unlike everything around it |
| Serial position | The most important nav items go first and last |
| Doherty threshold | Every interaction answers within 400ms: optimistic updates, skeletons, instant feedback |
| Zeigarnik effect | Show progress on multi-step forms and onboarding |
| Postel's law | Accept input loosely (phone numbers with spaces or +256), normalise it server side |
| Tesler's law | Complexity moves into the system, not onto the user |
| Aesthetic-usability effect | Beauty buys tolerance but hides usability problems, so test with tasks, not opinions |

## CTAs

The whole point of most sections is that somebody clicks. Design accordingly.

- **Highest contrast on the page.** The primary action should be the most visually distinct element in its section. If it blends into a tasteful palette, the palette won.
- **No ghost buttons for primary actions.** Outline-only buttons with no fill read as decoration, get overlooked, and get clicked less. They look sophisticated in a mockup and underperform in production. Use them for genuinely secondary actions only, and never as the single action on a hero.
- **Say what happens next.** "Check availability" beats "Learn more". "Get a quote" beats "Submit". The label is a promise about the next screen.
- **One primary action per section.** Two competing CTAs halve each other.
- **Repeat the primary CTA** down a long page. A visitor convinced at 70% scroll should not have to hunt.
- **Real states.** Hover, focus-visible, active, loading, disabled, and a success state after the click.

## Friction

Every step between wanting and doing costs conversions.

- Ask for the minimum. Every extra form field loses people. Justify each one.
- Never demand an account before value is delivered.
- Contact details are one tap: `tel:`, `mailto:`, a map link. See `kaga-launch-check`.
- Prices, or at least a range. A hidden price is a bounce on a local services site.
- Answer the objection where it arises, not in a FAQ at the bottom.
- Confirm every action visibly. Silence reads as failure and produces double submissions.

## Design for the audience, not the room

It does not matter whether you like the design. It does not matter whether the client likes the design. It matters whether it works for the people who visit.

This is the hardest conversation in client work, and the skill is to reframe rather than fight: not "your logo should be smaller", but "the visitors we tested with could not find the booking button, here is what happens when we fix that." Bring evidence, not taste.

Where the client's stated preference will measurably cost them, say so once, plainly, in writing, with the reason. Then respect the decision and record it in `docs/DECISIONS.md`. You are accountable for telling them, not for overruling them.

Match motion intensity to the audience too. A younger audience tolerates and enjoys heavy cinematic motion. An older or hurried audience reads the same treatment as an obstacle. `kaga-scroll-narrative` gets calibrated to who is actually visiting.

## Before sign-off

- [ ] Hero answers who, what, and what next, in five seconds, tested on someone cold
- [ ] Every section has a ranked hierarchy, with real de-emphasis
- [ ] Primary CTA is the highest-contrast element in its section
- [ ] No ghost button carries a primary action
- [ ] CTA labels describe the outcome
- [ ] Primary action repeats down long pages
- [ ] Form fields justified one by one
- [ ] Contact details one tap
- [ ] Price or range visible where the market expects it
- [ ] Every action visibly confirmed
- [ ] Motion intensity matched to the real audience
- [ ] Any conversion-costly client preference recorded in writing

Findings go into `docs/AUDIT.md` alongside the design-integrity pass. A build that is beautiful and unpersuasive is not finished.
