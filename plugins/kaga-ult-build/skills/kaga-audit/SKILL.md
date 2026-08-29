---
name: kaga-audit
description: Run the three-pass audit that closes a Kaga build - security review, quality and UAT verification in a real browser, and design integrity against the art direction. Use before shipping any build or feature, or when the user asks to audit, review, check, verify, or harden a site, or asks whether something is ready to launch.
---

# Audit

The third pass of Plan, Act, Audit. Run by agents that did not do the building. Audit has authority to send work back, it is not a rubber stamp.

Three passes, all three required, findings merged into `docs/AUDIT.md`.

---

## Pass 1: Security

Owner: `kaga-security-auditor`.

### Secrets and configuration
- No key, token, or connection string committed. Check history, not just the working tree.
- Server-only keys never reach the client bundle. On Next.js, confirm nothing sensitive sits outside a server component or route handler, and that `NEXT_PUBLIC_` is only on things that are genuinely public.
- `.env.example` present and current, real `.env` gitignored.

### Auth and data access
- Supabase RLS enabled on every table, with policies read line by line. An RLS-enabled table with a permissive `true` policy is not protected.
- Anon key paths can only reach what the public is meant to reach.
- Admin routes actually check a session server side, not just hide the link.
- Service role key used only in server-side scripts, never shipped.

### Input and output
- Every user input validated server side, with a schema, not just client-side form checks.
- No SQL string interpolation. Parameterised or ORM only.
- User content escaped on render. Any `dangerouslySetInnerHTML` sanitised and justified.
- File uploads: type checked by content not extension, size capped, stored outside the web root or in object storage with correct ACLs.

### Transport and headers
- HTTPS enforced, HSTS set.
- CSP present and meaningful, not `unsafe-inline` everywhere.
- `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy` set.
- CORS scoped to known origins, never `*` on anything authenticated.

### Dependencies and abuse
- `npm audit`, resolve high and critical or write down why not.
- No abandoned packages on critical paths.
- Rate limiting on auth, contact forms, and anything that costs money per call.
- Bot protection on public forms.

Report severity as Critical, High, Medium, Low, with the file and line, the concrete exploit path, and the fix. No finding without a failure scenario.

---

## Pass 2: Quality and UAT

Owner: `kaga-uat-agent`. Verified in a real browser, not asserted.

Use the Browser pane tools. `preview_start` the dev server, then drive it. A claim that something works, made without opening it, is not a UAT result.

### Functional
- Every acceptance criterion in `docs/PLAN.md`, walked and marked pass or fail.
- Every form: submit valid, submit invalid, submit empty, double submit.
- Every link and route, including the 404.
- Loading, empty, and error states triggered deliberately and inspected.

### Responsive
Screenshots at 375, 768, and 1440 minimum. Look for: horizontal overflow, text collision, tap targets under 44px, images cropping the subject out of frame, nav that breaks between breakpoints.

### Accessibility, WCAG AA
- Keyboard only: tab the whole page, confirm visible focus on every stop, confirm no trap, confirm logical order.
- Landmarks and heading hierarchy, no skipped levels.
- All images have correct `alt`.
- Form inputs have real labels, errors announced.
- Contrast checked with numbers against the art direction table.
- `prefers-reduced-motion` honoured, verified by emulating it.

### Performance
- Lighthouse or equivalent, report the numbers.
- LCP element identified and optimised.
- No layout shift.
- Bundle checked for anything large that should have been dynamic.

### SEO
- Unique title and meta description per route.
- OG and Twitter cards, with an image that actually renders.
- JSON-LD schema appropriate to the business type, validated.
- Canonicals, sitemap, robots.
- Semantic HTML, one `h1` per page.

---

## Pass 3: Design integrity

Owner: `kaga-art-director`, returning to judge the built result against the document they wrote.

This pass exists because defaults creep back in during implementation. Hunt specifically for:

- [ ] Any raw Tailwind default colour class in the codebase (`grep` for `bg-gray-`, `text-blue-`, and friends)
- [ ] Any system font fallback rendering because a face failed to load
- [ ] Any shadcn component shipped visually unmodified
- [ ] Radius, spacing, or shadow values not from the token scale
- [ ] Missing hover, focus-visible, active, or disabled states
- [ ] Empty states that are just blank, error states that are just red text
- [ ] Greybox or placeholder images still present
- [ ] Motion timings that do not match the motion language
- [ ] Copy voice drifting between sections built by different agents
- [ ] Em dashes anywhere in the repo

That last one is checkable, and the pattern must use the escape rather than the literal character so the check does not match itself:

```bash
grep -rnP "\x{2014}" . --exclude-dir=node_modules --exclude-dir=.git
```

It is a house rule, so treat a hit as a finding.

---

## Reporting

`docs/AUDIT.md`, findings ranked most severe first, each with file, line, what breaks, and the fix. Blockers get fixed and re-audited by the same pass. A build with open blockers is not done, and saying it is done anyway is worse than the bug.
