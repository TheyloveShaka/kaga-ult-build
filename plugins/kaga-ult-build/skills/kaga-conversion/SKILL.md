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
