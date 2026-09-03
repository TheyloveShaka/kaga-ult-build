---
name: kaga-launch-check
description: The mandatory pre-launch sweep that catches everything a vibecoded site gets wrong - horizontal scroll, broken links and buttons, missing mobile menu, favicon, page titles, meta descriptions, custom 404, stale copyright year, uncompressed images, placeholder text, dead nav items, unclickable logo/phone/email, and missing success and error states. Every item is verified in a real browser, never assumed. Use before any site ships, on every build and every redesign, and whenever the user asks whether a site is ready to launch.
---

# Launch Check

The sweep that separates a shipped site from a demo. Every one of these is something clients and their customers notice immediately, and every one of them is cheap to fix and expensive to miss.

**Verify each item, do not assume it.** Open the site in the Browser pane and check. An item you did not test is `UNVERIFIED`, never `PASS`. This is the same rule that governs `kaga-uat-agent`, and it exists because a checklist filled in from memory is worse than no checklist, it just launders a guess into a green tick.

Record results in `docs/LAUNCH-CHECK.md` as a table with a status and evidence per item.

---

## Block A: Layout and responsive

**1. No horizontal scroll, any breakpoint.** Test 320, 375, 768, 1024, 1440. The usual culprits are fixed widths, unconstrained images, `100vw` with a scrollbar present, long unbroken strings, and negative margins.

```js
document.documentElement.scrollWidth > document.documentElement.clientWidth
```
Run it at each width. Then find the offender:
```js
[...document.querySelectorAll('*')].filter(el => el.getBoundingClientRect().right > document.documentElement.clientWidth + 1)
```

**2. No mobile overflow of any element.** Related but distinct from page scroll: a table, a code block, or a wide card that clips its own content. Wide content scrolls inside its own `overflow-x: auto` container. The page body never scrolls sideways.

**3. Mobile menu exists and works.** Below the nav breakpoint there is a real menu. Open it, close it, navigate from it. Check: it traps focus while open, `Escape` closes it, the trigger has an accessible name, body scroll locks while it is open, and it closes on route change.

**4. Genuinely mobile optimised.** Not merely "does not break". Tap targets 44px minimum with real spacing between them, font sizes at least 16px on inputs so iOS does not zoom, thumb-reachable primary actions, and no hover-only interaction that has no tap equivalent.

## Block B: Links, buttons, and navigation

**5. Zero broken links.** Crawl every internal link and check the status. Externals too, they rot and a 404 on a client's partner link looks careless.

**6. Zero broken or dead buttons.** Every button does something. Click each one. A button wired to nothing, or to a `#` href, is a bug. Watch the console while clicking.

**7. Footer links all resolve.** Footers are where placeholder links survive longest because nobody scrolls down during review. Check every one, including the social icons, which are frequently left pointing at the platform homepage rather than the client's profile.

**8. No unused or dead nav items.** A nav entry pointing at a page that does not exist, or at a section that was cut, gets removed. Do not leave "Blog" in the nav for a site with no blog.

**9. Logo is clickable and returns home.** On every page including the 404. Universally expected, frequently missed.

## Block C: Contact affordances

These three convert. On a local business site they are often the entire point of the page, and leaving them as plain text is the most costly small mistake on this list.

**10. Phone numbers are `tel:` links.** `<a href="tel:+256700000000">`. Keep the display format human, keep the href in E.164.

**11. Email addresses are `mailto:` links.** Real address, no obfuscation that breaks the click.

**12. Physical addresses link to maps** where the business has premises visitors need to find.

## Block D: Content integrity

**13. Zero placeholder text.** No lorem ipsum, no "Your Company Here", no `TODO`, no "Lorem", no dummy names, no `example.com`. Grep for it, then read the rendered pages, because placeholders hide in `alt`, `title`, meta tags, and empty states.

**14. Copyright year is dynamic.** Not hardcoded. A footer reading a past year on a client's site tells every visitor the site is abandoned.

**15. Success messages exist and are designed.** Every form, every action, tells the user it worked. A form that silently resets reads as broken and the user submits again.

**16. Error messages exist, are specific, and are designed.** Not a raw stack trace, not a generic "Something went wrong" where the app knows exactly what went wrong. Say what failed and what to do about it. Test by deliberately failing: submit empty, submit invalid, kill the network.

**17. Custom 404 page.** Branded, with navigation back into the site and a search or a set of useful links. The framework's default 404 is a dead end that looks unfinished.

## Block E: Metadata and assets

**18. Favicon present, all formats.** `favicon.ico`, a 180px apple-touch-icon, and a manifest icon set. Confirm it actually renders in the tab, do not just confirm the file exists.

**19. Page titles are unique, descriptive, and correctly ordered.** Roughly 50 to 60 characters, specific page first, brand last. No "Home", no "React App", no title repeated across routes.

**20. Meta descriptions on every route.** Roughly 150 to 160 characters, written to earn a click, unique per page.

**21. Images compressed and correctly served.** AVIF or WebP with fallback, sized to their display box rather than shipped at 4000px, lazy loaded below the fold, LCP image preloaded and never lazy, explicit dimensions so nothing shifts. Check the transferred bytes in the network panel, not the source file size.

---

## Beyond the list

The twenty above are the floor, not the bar. A build going out at premium price also clears:

- **Open Graph and Twitter cards** on every route, with an image that actually renders. Test the real link preview, do not assume the tags are enough.
- **JSON-LD** appropriate to the business, validated.
- **`sitemap.xml` and `robots.txt`**, with robots not accidentally blocking the site. Shipping a staging `Disallow: /` to production is a classic and it is invisible until traffic never arrives.
- **Canonical URLs**, especially if the site is reachable on both apex and www.
- **HTTPS enforced**, HSTS set, no mixed content.
- **Analytics installed and confirmed firing**, if the client expects to measure anything.
- **A real `<html lang>`**, correct for the market.
- **Focus visible on every interactive element**, and a skip link.
- **`prefers-reduced-motion` honoured**, verified by emulating it.
- **Forms actually deliver.** Submit a real test entry and confirm it arrives where the client will look for it. A contact form that posts to nowhere is the single worst launch bug on this list, and it is silent.

## Reporting

`docs/LAUNCH-CHECK.md`, one row per item:

| # | Item | Status | Evidence |
|---|---|---|---|
| 1 | No horizontal scroll | PASS | 320/375/768/1440 all clientWidth == scrollWidth |
| 14 | Copyright year | FAIL | `Footer.tsx:41` hardcodes 2024, needs `new Date().getFullYear()` |

`PASS`, `FAIL`, `UNVERIFIED`, or `N/A` with a reason. Any `FAIL` is a launch blocker. Any `UNVERIFIED` is reported as unverified, never quietly upgraded.

End with a plain verdict. If the site is not ready, say so and list the blockers. Do not soften it to be agreeable.
