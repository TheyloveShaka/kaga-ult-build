# Lessons

Mined from Kaga's build history across UWA, MyLand.ai, Kamwe Forex, Frozen Basket, Kaga Hotel, Bulungi Town, Gig Economy, and the portfolio. Read in Phase 1 of every build, before planning. Rule first, evidence after. Also read `~/.claude/kaga/lessons.md` if it exists: it holds lessons learned since this file was last released, written by `/kaga-retro`.

## Corrections that cost the most rounds

1. **First builds ship bland.** Said on four builds in a row: "plain and vanilla", "ABSOLUTELY BLAND", "not wow", "I still see Claude default font and styling". The cause each time was references summarised rather than reproduced, thin imagery, and defaults leaking. Rule: Law 7. Before showing anything, screenshot it beside each named reference move and confirm the move is actually there. His words: "if you test and don't see that it is that, then we aren't done."

2. **The default font leaks into small text.** Prices, numerals, labels, and card metadata fell back to a default sans on UWA and Kaga Hotel. Rule: one font system on every text node, numerals included. Verify with the computed-font audit in `kaga-launch-check`, not by eye.

3. **Em dashes reached a rendered site** (Kaga Hotel), through generated copy. Scan the rendered page text, not only the repo.

4. **The brand's signature was missed.** Kamwe Forex: "there's really no yellow on the site, and their main colours are a gradient of purple and sky blue." Rule: in Track A, pull colours from the logo and the client's own assets, name the signature element (a gradient, an accent, a shape) and confirm it with Kaga before art direction. The signature must show up in components, not only in the logo. It recurred on Eden of Kora (2026-10-12): "you didn't use the green accents from the palette I gave you, why is the ribbon black now." Hex values Kaga or the client supplies are locked tokens from the first commit; compare the rendered colours against them every round.

5. **Images missing, thin, or broken once hosted.** Logo and favicon missing (UWA, Frozen Basket); barely any images (Kamwe); images that load locally but not on the hosted site (2026-09-23). Rule: source images yourself first ("can't you research those photos?") and ask only for what must be real. Verify every image, the logo, and the favicon on the deployed URL, where paths are case-sensitive.

6. **The hero takes the most revision rounds on every build** (UWA, MyLand slider, Frozen Basket, Kamwe, Kaga Hotel). Rule: build the hero first, get it approved, then build the rest. Spend the adversarial gate and any paid consultant call on the hero before anything else.

7. **Fixes that did not stick.** The UWA grey divider lines were raised three times. Rule: after a fix, look at the same element at the same breakpoint the user saw. Never report "fixed" from a diff.

8. **The architecture was not followed on its own test run.** Frozen Basket: "I thought this project was going to run on the architecture I specified." Rule: at the start of Phase 2, print the crew table with the model actually running each phase. Name any deviation immediately (Law 1).

9. **A model was unreachable mid-build** ("it says it can't access luna"). Rule: before a phase depends on a non-default model, preflight it with a one-token call.

10. **Builders report pass on broken screens.** Kaga Hotel v1: builders reported clean twice while a desktop stage scrolled 430px sideways, a clip never played, and a DRAFT label was on screen; three non-builder audits found 10 blockers. Rule: one script shoots every screen at every viewport into contact sheets, and the lead opens them before and after each agent. A builder's "pass" is not a look.

11. **The deployed site was slow or dead past the hero** (Kaga Hotel, 2026-09-23: "the page still takes yearssss", "the rest of the page doesn't load except for the hero"). Rule: a loader never gates content, and "done" is checked on the deployed URL with a throttled mobile profile, not on localhost.

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
- **Agents ignore soft iteration caps** (256, 149, and 102 calls against caps of 90, 70, and 60 on the portfolio overhaul). Give each agent one small, file-scoped task, and resume an agent rather than spawning a new one.
- **An agent spawn costs about 100K tokens before it does anything** (eTaxi: a 5-call plan attack used 101K, a 26-call audit 263K). Batch real work into few agents, and let the lead make one-line CSS fixes itself with a script to verify.
- **Build the QA scripts first.** `scripts/qa/shots.cjs` and `probe.cjs` (Playwright) replaced most visual re-check agents at near-zero cost. Send repo sweeps that remain to Haiku 5.5.
- **Session limits kill agents mid-task.** Check `find -newer` against a marker file, then resume the same agent with SendMessage, telling it what is already on disk. Auditors write evidence to disk as they go; restart the preview server before resuming.
- **Measure a video reference from its frames** before writing geometry into the plan. On eTaxi the road was planned at 38vw from memory; the reference had it on the centre line.
- **Never reuse the climax image earlier on the page.** The eTaxi camera card first used the arrival photo and spoiled the reveal.
- **Copy sits in the space the image leaves** ("the words should be in the space left by the taxi"). Plan the image with that negative space, then place the type in it.
- **Judge a translucent brand colour over the brightest image it sits on**, not on the swatch. Kaga Hotel's deep green read as sage at 80 percent over ivory stone and sky; it needed .86 plus a brightness cut behind the blur.
- **Check the OpenRouter balance before paid calls**, and budget a cheap Astra batch UI/UX audit after each build. Kaga asks for both routinely.
- **Dashboard hand-offs need exact paths.** On MyLand he could not find the Vercel env vars and asked which were secret or config. Label every variable secret or config, give the dashboard path for each, and set up custom SMTP (for example Resend) before launch, because Supabase's built-in mailer is limited.
- **His terminal is PowerShell.** A bash-style pipe to `clip` failed. Give PowerShell commands, or write the file yourself and give him the path.
- **Pinterest short links (`pin.it`) arrive as main references.** Resolve them to the full image before using them.
- **The install command in a reel can point to someone else's package.** A demo site said `npm install gooey-toast`; its own repo published under another name, so the command installed an unrelated two-star package. Vet every reel-sourced package per `references/sources.md` before it enters a build.

## Tooling facts (re-verify prices before relying on them)

- Image generation: `google/gemini-2.5-flash-image` at about $0.039 per image matched the pricier 3.1 model on isolated subjects. For cutouts, key on colour (hue), never brightness, or cast shadows stay as grey halos. Shoot green subjects on magenta. Models cannot spell small signage, so generate blank signs and set the text with a script.
- OpenRouter Batch accepts images only as public URLs. The video API accepts inline base64 frames. `google/veo-3.1-lite` costs about $0.05 per second at 1080p, silent.
- `ffmpeg` on this machine rejects `-vsync`; use `-fps_mode passthrough`.
- Phone clips carry rotation metadata: `ffprobe` reports the unrotated size while `ffmpeg` auto-rotates, so scaling to the probed size squashes portrait video (Eden of Kora, 7 of 9 clips). Scale with one fixed side and `-2`, then look at a frame of every encode.
- YouTube blocks caption downloads from this IP after a burst of requests. Space them out, or ask for pasted transcripts.
