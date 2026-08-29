---
name: kaga-quote
description: Produce the internal business case and the client-facing quote for a build - true development cost, tool and subscription burn, overheads, risk buffer, margin, and the final number to put in front of the client. Use when scoping a new client project, when the user asks what to charge, how much to quote, what a project costs, or asks for a proposal, invoice basis, or pricing breakdown.
---

# Quote

Two documents, never confused with each other:

- `docs/BUSINESS-CASE.md` is **internal**. It shows cost, margin, and risk. The client never sees it.
- `docs/QUOTE.md` is **client-facing**. It shows value, scope, and a number. It never shows margin.

Rates live in `config/rates.yml` inside this plugin. Read that file first.

That file is gitignored, because it holds the cost basis and the walk-away floor. If it is missing, `config/rates.example.yml` is the template: tell the user to copy it and fill it in, and do not invent numbers to fill the gap.

If `rates.yml` exists but `confirmed: false`, use the values, say plainly at the top of both documents that the rate card is unconfirmed, and mark every figure provisional.

---

## Step 1: Scope to hours

Break the build into the crew phases from `docs/PLAN.md` and estimate hours per phase. Estimate honestly, then apply the complexity multiplier.

| Phase | Typical share |
|---|---|
| Reference hunt and art direction | 10% |
| UX architecture and content model | 12% |
| Frontend build | 30% |
| Motion and interaction | 12% |
| Backend, data, auth | 15% |
| Content, copy, SEO | 8% |
| Security audit, UAT, fixes | 10% |
| Integration and launch | 3% |

Complexity multipliers, applied to the total:
- Brochure or marketing site, static content: 1.0
- Content-driven with CMS or database: 1.4
- Auth, accounts, dashboards: 1.9
- Payments, bookings, or real-time: 2.4
- Heavy 3D, WebGL, or scroll-narrative: +0.5 on top

## Step 2: True cost

Cost is not just hours times a rate. Count all of it:

**Direct labour.** Hours times your effective rate. Use the internal cost rate from `rates.yml`, not the billing rate. The gap between them is where the business lives.

**Tooling, amortised.** Take the monthly subscription burn, divide by how many projects run concurrently, multiply by project duration in months. A $250 per month stack across two concurrent projects on a six week build is roughly $175 charged to this job.

**Project-specific spend.** Domain, licensed fonts, paid stock, generation credits, paid API tiers, a paid Supabase or Vercel plan the client's traffic actually needs. These are real and they are often forgotten.

**Overhead.** Power, internet, hardware amortisation, and the unbilled hours: sales calls, scoping, admin, chasing the invoice. Apply the overhead rate from `rates.yml` to direct labour.

**Risk buffer.** Scope creep, client silence, revision rounds beyond the agreed count. Default 15% for a known client, 25% for a new one.

## Step 3: Margin and the number

```
Subtotal cost   = labour + tooling + project spend + overhead
With risk       = subtotal x (1 + risk rate)
Quote           = with-risk / (1 - target margin)
```

Divide by `(1 - margin)`, do not multiply by `(1 + margin)`. A 40% target margin means cost is 60% of price, so the divisor is correct and the multiplier undercharges by a meaningful amount.

Then sanity check the result three ways:
1. **Against the market.** Does this land where comparable work in the market lands.
2. **Against the value.** What is this site worth to the client per year. A booking site that converts twenty extra clients justifies more than a business card site.
3. **Against your floor.** Never quote below the walk-away number in `rates.yml`, regardless of how much you want the job.

If the three checks disagree sharply, present the range to Kaga with the reasoning rather than picking silently.

## Step 4: The internal document

`docs/BUSINESS-CASE.md`:

```markdown
# Business Case: <Project>

## Scope summary
<2 lines>

## Effort
| Phase | Hours | Cost |
Total hours, complexity multiplier applied, adjusted hours.

## Cost stack
| Line | Amount | Note |
Direct labour / tooling amortised / project spend / overhead / risk buffer
**True cost:** <n>

## Pricing
Target margin, computed price, market check, value check, floor check.
**Recommended quote:** <n>
**Walk-away floor:** <n>

## Profit
Gross profit, effective hourly, margin achieved.

## Risks
What could push this over, and the trigger for a change order.

## Payment structure
Deposit, milestones, final. Never start on zero deposit.
```

## Step 5: The client document

`docs/QUOTE.md` shows scope, deliverables, timeline, price, and terms. It reframes cost lines as value lines. The client reads "brand and art direction, researched palette and typography", not "10% of hours".

Always include:
- What is in scope, itemised concretely
- What is explicitly **not** in scope, this is the clause that prevents scope creep
- Revision rounds included, and the rate beyond them
- What you need from them and by when, including the photos from `docs/IMAGE-PLAN.md`
- Payment schedule and terms
- Ongoing costs they carry after launch: hosting, domain, any paid tier. Be upfront, a surprise bill in month two costs you the referral.
- Quote validity window

Present both currencies where the client is local: UGX primary, USD reference, with the exchange rate and the date it was taken.

## Honesty rule

If the defaults in `rates.yml` have not been confirmed by Kaga, every number carries a provisional marker and the output says so at the top. Confident fake numbers are worse than an obvious placeholder, because a placeholder gets corrected and a confident wrong number gets sent to the client.
