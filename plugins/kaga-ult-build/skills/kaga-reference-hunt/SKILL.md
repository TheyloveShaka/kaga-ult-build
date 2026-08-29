---
name: kaga-reference-hunt
description: Research and present exactly 10 reference sites before any design work starts, each with the specific transferable move worth stealing. Use at the opening of any new build, redesign, or major visual feature, or when the user asks for design references, inspiration, competitor analysis, or "show me some examples". Always ends by asking which references land and what specifically the user likes from each.
---

# Reference Hunt

Runs before art direction. Design decisions made without references are just the model's priors, and the model's priors are what "AI-looking site" means.

## The brief you need first

If not already known, establish in one short exchange:
- Sector and what the business actually sells
- Who the visitor is and what they came to do
- The feeling: authoritative, playful, luxurious, technical, warm, stark
- Any hard constraint: existing brand, accessibility, market, language

Do not run a hunt without this. A hunt without a brief returns generic awards-site slop.

## The spread

Return exactly 10, in this mix:

| Count | Category | Why |
|---|---|---|
| 3 | Direct sector | Shows the conventions the audience already expects |
| 4 | Aspirational cross-sector | Where the quality bar actually is |
| 2 | Motion or interaction study | One specific technique, studied in isolation |
| 1 | Deliberate outlier | Something that should not work for this brief, to test the edges |

## Where to look

Use `WebSearch` and `WebFetch`. Productive sources:
- Awwwards, FWA, Godly, Land-book, Httpster, Minimal Gallery, One Page Love
- Dribbble and Behance for direction, but never as a build reference, they are static
- The actual competitors, found by searching the sector plus the market

For each candidate, open it. A reference you have not looked at is a guess.

When a site is JS-heavy or the fetch returns a shell, use the Browser pane: `preview_start` with the URL, then `get_page_text` or a screenshot. Read what is really there.

## Output format

Present as a numbered list. Each entry:

```
N. <Name> - <url>
   Category: direct sector | aspirational | motion study | outlier
   Does well: <one line, specific>
   Steal this: <the exact transferable move, concrete enough to build>
   Watch out: <the thing that would not work for this brief>
```

"Steal this" is the whole point. Write moves, not adjectives.

Bad: "Great use of whitespace and clean typography."
Good: "Hero holds a single 12vw headline with the product image bleeding off the right edge, and the nav only appears on scroll-up after 60vh."

## The ask

End every hunt with the question, and stop:

> Which of these land, and what specifically do you like from each? Point at moves, not whole sites, so I can compose rather than copy.

Do not proceed to `kaga-art-direction` until answered. Kaga has explicitly asked to be exact at this step.

## Recording

Write the shortlist and the user's verdict to `docs/REFERENCES.md`, structured as: what we are taking, from where, and what we are deliberately rejecting. The rejections matter as much as the picks, they stop the same debate reopening in phase 3.
