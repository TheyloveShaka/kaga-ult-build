# Sources

Reference for `kaga-ult-build`. Component libraries and inspiration sources Kaga has flagged, each verified before listing. Read when choosing components (P3, P4) or hunting references (Phase 0).

## Vet before you install

Sources found in reels are marketing first. The install command on screen is not proof of anything. Before any package from a reel enters a client build:

1. **The domain resolves and the repo exists.** Follow the site's own GitHub link rather than searching for the name.
2. **The package name on npm belongs to that repo.** Check `npm view <name> repository.url`. A reel once showed `npm install gooey-toast` while the demo site's repo published under a different name, so the command installed an unrelated package from another author.
3. **A real licence.** MIT, Apache, or BSD is fine for client work. `none` or `NOASSERTION` means read the licence file yourself or do not ship it.
4. **Signs of life.** Stars, recent pushes, open issues answered. A two-star package created last month is a risk, however good the demo looks.
5. **Restyle to the tokens.** A library component in its default skin breaks Law 2 exactly as much as a default Tailwind palette does.

Record the source, version, and licence of every third-party component in `docs/AUDIT.md`.

## Component libraries

Verified 2026-09-23. Re-check versions and licences at the time of use.

| Library | What it is | Licence | Status |
|---|---|---|---|
| **Rare UI** (rareui.com, `swamimalode07/rare-ui`) | Rare animated React components, installed with the shadcn CLI. **Kaga likes these components.** | Not detected by GitHub | Live, 1.4k stars. Read the licence file before any client build |
| **SmoothUI** (smoothui.dev, `educlopez/smoothui`) | 130 animated components that drop into shadcn, one command each | MIT | Live, about 1k stars |
| **Amicro** (amicro.vercel.app, `Subhan-code/Amicro--Micro-transitions-`) | Micro-transitions and monochrome charts via a CLI. Strong fit for `kaga-product-ui` dashboards once recoloured to the accents | MIT | Live, 2.5k stars |
| **Bencho** (bencho.dev) | Interactive blocks you tweak live before copying: checklists, assignees, slide to confirm, search | No public repo found | Live. Licence unknown, so use as a pattern reference, not a dependency, until confirmed |
| **goey-toast** (`goey-toast`, `anl331/goey-toast`) | Morphing toast notifications with promise tracking: loading, then success or error in one element. Bundles an Agent Skill | MIT | v0.5.0, 1.3k stars. Use this, **not** `gooey-toast` |
| **thinking-orbs** (`thinking-orbs`) | Named loading states for AI and long-running work | MIT | v0.3.2 |

Promise-tracking toasts and named loading states are the fastest way to meet the state-complete rule in `kaga-product-ui`.

## Inspiration sources

For Phase 0 hunting. These show live interaction, which static galleries miss.

| Source | Best for |
|---|---|
| **Inspora** (inspora.design) | Motion, product, branding, and 3D, sorted by category, mostly video, updated hourly |
| **Best Designs on X** (bestdesignsonx.com) | Curated design Twitter: logos, UI, and branding without the doomscroll |
| **Scrolltide** (scrolltide.co) | A library of scroll interactions, each with a prompt to build it. Treat a prompt as a starting technique, not a finished design: it still goes through the shot list, art direction, and the reference-fidelity check |
