# Lessons

Mined from Kaga's build history across UWA, MyLand.ai, Kamwe Forex, Frozen Basket, Kaga Hotel, Bulungi Town, Gig Economy, and the portfolio. Read in Phase 1 of every build, before planning. Rule first, evidence after. Also read `~/.claude/kaga/lessons.md` if it exists: it holds lessons learned since this file was last released, written by `/kaga-retro`.

## Corrections that cost the most rounds

1. **First builds ship bland.** Said on four builds in a row: "plain and vanilla", "ABSOLUTELY BLAND", "not wow", "I still see Claude default font and styling". The cause each time was references summarised rather than reproduced, thin imagery, and defaults leaking. Rule: Law 7. Before showing anything, screenshot it beside each named reference move and confirm the move is actually there. His words: "if you test and don't see that it is that, then we aren't done."

2. **The default font leaks into small text.** Prices, numerals, labels, and card metadata fell back to a default sans on UWA and Kaga Hotel. Rule: one font system on every text node, numerals included. Verify with the computed-font audit in `kaga-launch-check`, not by eye.

3. **Em dashes reached a rendered site** (Kaga Hotel), through generated copy. Scan the rendered page text, not only the repo.

4. **The brand's signature was missed.** Kamwe Forex: "there's really no yellow on the site, and their main colours are a gradient of purple and sky blue." Rule: in Track A, pull colours from the logo and the client's own assets, name the signature element (a gradient, an accent, a shape) and confirm it with Kaga before art direction. The signature must show up in components, not only in the logo.

5. **Images missing, thin, or broken once hosted.** Logo and favicon missing (UWA, Frozen Basket); barely any images (Kamwe); images that load locally but not on the hosted site (2026-09-23). Rule: source images yourself first ("can't you research those photos?") and ask only for what must be real. Verify every image, the logo, and the favicon on the deployed URL, where paths are case-sensitive.

6. **The hero takes the most revision rounds on every build** (UWA, MyLand slider, Frozen Basket, Kamwe, Kaga Hotel). Rule: build the hero first, get it approved, then build the rest. Spend the adversarial gate and any paid consultant call on the hero before anything else.

7. **Fixes that did not stick.** The UWA grey divider lines were raised three times. Rule: after a fix, look at the same element at the same breakpoint the user saw. Never report "fixed" from a diff.

8. **The architecture was not followed on its own test run.** Frozen Basket: "I thought this project was going to run on the architecture I specified." Rule: at the start of Phase 2, print the crew table with the model actually running each phase. Name any deviation immediately (Law 1).

9. **A model was unreachable mid-build** ("it says it can't access luna"). Rule: before a phase depends on a non-default model, preflight it with a one-token call.

## Standing preferences

- **Opus leads, cheaper agents do the heavy lifting.** Said on at least seven builds. It is now the default; never make him repeat it.
- **Be frugal with tokens.** Said about ten times. Reuse scripts instead of spawning agents for re-checks, give every agent an iteration cap (Kaga Hotel agents burned 230K to 360K tokens each), read only the screenshots that decide a question, and keep status replies short.
- **No unnecessary code comments.** Rationale goes in docs, never narrated in code. Put this in every builder prompt.
- **No sound anywhere** unless he asks: no audio, no sound toggle, silent video.
- **Content is sacred on a redesign.** Copy, prices, phone numbers, and logos are lifted verbatim. The redesign changes presentation, never facts.
- **He tweaks colours himself.** Keep every colour in the token file and, when asked, point to the exact file and line.
- **Demo builds can defer security and the quote** ("leave security for now, this is just a demo"). Visual quality cannot be deferred.
- **Mobile is expected by default**, with specific layouts per element (cards keep their curve and overlap, two per row). Never leave "make it responsive" for him to ask.
- **He is still learning the tooling.** When he has to act (keys, dashboards, deploy settings), give numbered steps with exact clicks, one action at a time.

## Process

- **Usage limits hit mid-build repeatedly.** Update `docs/PROGRESS.md` before every long phase so a resume costs one read.
- **"What's still running?", "how far?", "has everything been done?"** come up constantly. End each phase with a three-line status. After an interruption, check what actually finished before continuing.
- **Stop dev servers and background tasks** when a phase ends.
- **Never ask for secrets in chat.** Four API keys were pasted into chat on one project. Give him the exact `.env` path and variable name instead. If a key is pasted anyway, say so and advise rotating it. Server keys never get `NEXT_PUBLIC_` or `VITE_` prefixes.
- **"Blend both" is ambiguous.** When he names a "structural design" or asks to blend two images, confirm which image supplies the form before generating. Getting it backwards cost a hero round on Kaga Hotel.
- **Figma MCP on his Starter plan allows about 20 calls per period, and every call counts.** Do not plan a Figma build through MCP without an upgrade.
- **Warm reload and back-navigation broke animation state** (Frozen Basket: the nav turned white and sections vanished until a hard reload). Test reload, back and forward, and route change on every GSAP build.
- **The collapsed mobile nav button failed** (Frozen Basket). Always tap it at a real narrow width.
- **Photos marked ASK CLIENT arrive late** on almost every job. Raise the ask in week one.

## Tooling facts (re-verify prices before relying on them)

- Image generation: `google/gemini-2.5-flash-image` at about $0.039 per image matched the pricier 3.1 model on isolated subjects. For cutouts, key on colour (hue), never brightness, or cast shadows stay as grey halos. Shoot green subjects on magenta. Models cannot spell small signage, so generate blank signs and set the text with a script.
- OpenRouter Batch accepts images only as public URLs. The video API accepts inline base64 frames. `google/veo-3.1-lite` costs about $0.05 per second at 1080p, silent.
- `ffmpeg` on this machine rejects `-vsync`; use `-fps_mode passthrough`.
- YouTube blocks caption downloads from this IP after a burst of requests. Space them out, or ask for pasted transcripts.
