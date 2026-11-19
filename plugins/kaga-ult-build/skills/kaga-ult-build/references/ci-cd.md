# CI/CD

Checks that run on every push cost no Claude tokens. The pipeline does the mechanical verifying; the model reads only the lines that failed and spends its tokens on judgement.

## By track

| Track | Pipeline |
|---|---|
| D | `ci.yml` only, launch spec included. Vercel's Git integration may deploy main directly |
| A to C | All three workflows, branch protection on main, production only from a green main |

## The flow

1. **Every push and PR:** `ci.yml` runs typecheck, lint, unit tests, build, then the Playwright UAT specs and `launch.spec.ts` against the built app on the runner, then a secret scan and `npm audit --omit=dev --audit-level=high`.
2. **Merge:** branch protection on main requires `ci`; client repos take changes by PR only.
3. **Every preview:** Vercel's Git integration builds the branch and sends `repository_dispatch` (`vercel.deployment.success`) when it is ready. `e2e.yml` reruns the specs against `client_payload.url` to catch what only the hosted build shows: env vars, image paths, headers. It runs from main's workflow file, so it reports rather than gates. Previews behind Vercel Authentication need the `x-vercel-protection-bypass` header from the project's automation bypass secret.
4. **Production:** `vercel.json` turns off Git deploys for main, so nothing ships without the gate. `deploy.yml` reruns `ci` on main, applies migrations, then builds and deploys with the Vercel CLI.
5. **Database:** migrations live in `supabase/migrations` and are applied by `supabase db push` in `deploy.yml`, never by hand in the dashboard. Write them additive first (add, backfill, then drop in a later release) so a code rollback never meets a schema it cannot read.
6. **Rollback:** `vercel rollback` or the Vercel MCP `request_rollback`. A bad migration gets a forward fix, not a down migration on live data.
7. **Upkeep:** Dependabot weekly for `npm` and `github-actions`, minor and patch grouped into one PR.

Secrets (`VERCEL_TOKEN`, `VERCEL_ORG_ID`, `VERCEL_PROJECT_ID`, `SUPABASE_ACCESS_TOKEN`, `SUPABASE_DB_PASSWORD`, `SUPABASE_PROJECT_ID`, `VERCEL_AUTOMATION_BYPASS_SECRET`) go in the repo's Actions secrets. Kaga sets them in GitHub; they are never pasted into chat or committed. Public env vars the build needs go in Actions variables. Tests never touch the production database: point them at a Supabase branch or a local `supabase start`.

## Templates

Action versions checked 2026-11-19. On a client repo, pin third-party actions to a full commit SHA.

`vercel.json` (merge into the existing file):

```json
{ "git": { "deploymentEnabled": { "main": false } } }
```

`.github/workflows/ci.yml`:

```yaml
name: ci
on:
  push:
  pull_request:
  workflow_call:
jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
        with:
          fetch-depth: 0
      - uses: actions/setup-node@v7
        with:
          node-version: 22
          cache: npm
      - run: npm ci
      - run: npx tsc --noEmit
      - run: npm run lint
      - run: npm test --if-present
      - run: npm run build
      - run: npx playwright install --with-deps chromium
      - run: npx playwright test --reporter=line
      - run: npm audit --omit=dev --audit-level=high
      - uses: gitleaks/gitleaks-action@v3
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

The gitleaks action is free on personal accounts; an organisation repo needs `GITLEAKS_LICENSE` or the gitleaks binary run directly.

`.github/workflows/e2e.yml`:

```yaml
name: e2e
on:
  repository_dispatch:
    types: [vercel.deployment.success]
jobs:
  e2e:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-node@v7
        with:
          node-version: 22
          cache: npm
      - run: npm ci && npx playwright install --with-deps chromium
      - run: npx playwright test --reporter=line
        env:
          BASE_URL: ${{ github.event.client_payload.url }}
          VERCEL_AUTOMATION_BYPASS_SECRET: ${{ secrets.VERCEL_AUTOMATION_BYPASS_SECRET }}
```

`.github/workflows/deploy.yml`:

```yaml
name: deploy
on:
  push:
    branches: [main]
concurrency: production
jobs:
  ci:
    uses: ./.github/workflows/ci.yml
  deploy:
    needs: ci
    runs-on: ubuntu-latest
    env:
      VERCEL_TOKEN: ${{ secrets.VERCEL_TOKEN }}
      VERCEL_ORG_ID: ${{ secrets.VERCEL_ORG_ID }}
      VERCEL_PROJECT_ID: ${{ secrets.VERCEL_PROJECT_ID }}
    steps:
      - uses: actions/checkout@v7
      - uses: supabase/setup-cli@v3
        if: hashFiles('supabase/migrations/*.sql') != ''
      - if: hashFiles('supabase/migrations/*.sql') != ''
        run: supabase link --project-ref "$SUPABASE_PROJECT_ID" && supabase db push
        env:
          SUPABASE_ACCESS_TOKEN: ${{ secrets.SUPABASE_ACCESS_TOKEN }}
          SUPABASE_DB_PASSWORD: ${{ secrets.SUPABASE_DB_PASSWORD }}
          SUPABASE_PROJECT_ID: ${{ secrets.SUPABASE_PROJECT_ID }}
      - run: npm install --global vercel@latest
      - run: vercel pull --yes --environment=production --token="$VERCEL_TOKEN"
      - run: vercel build --prod --token="$VERCEL_TOKEN"
      - run: vercel deploy --prebuilt --prod --token="$VERCEL_TOKEN"
```

`playwright.config.ts` starts the built app when no `BASE_URL` is given (Vite: `npm run preview -- --port 3000`) and sends the bypass header when the secret is set:

```ts
import { defineConfig } from '@playwright/test';

export default defineConfig({
  use: {
    baseURL: process.env.BASE_URL ?? 'http://localhost:3000',
    extraHTTPHeaders: process.env.VERCEL_AUTOMATION_BYPASS_SECRET
      ? { 'x-vercel-protection-bypass': process.env.VERCEL_AUTOMATION_BYPASS_SECRET }
      : {},
  },
  webServer: process.env.BASE_URL
    ? undefined
    : { command: 'npm run start', url: 'http://localhost:3000', reuseExistingServer: true },
});
```

## The launch scan as a test

Copy the Block F scan from `kaga-launch-check` into `tests/launch-scan.js` and change its last line from `({ fonts, ... })` to `return { fonts, ... };`. Then:

```ts
import { test, expect } from '@playwright/test';
import { readFileSync } from 'node:fs';

const scan = `(() => { ${readFileSync('tests/launch-scan.js', 'utf8')} })()`;

test('no AI-default look on the home page', async ({ page }) => {
  await page.setViewportSize({ width: 1440, height: 900 });
  await page.goto('/');
  const r = await page.evaluate(scan);
  const families = r.hues.filter((h, i, a) => i === 0 || h - a[i - 1] > 30).length
    - (r.hues[0] === 0 && r.hues.at(-1) === 330 ? 1 : 0);
  expect(r.fonts).toEqual([]);
  expect(r.heroActions).toBeLessThanOrEqual(1);
  expect(r.eyebrow).toBe(false);
  expect(r.accentItalics + r.gradientText).toBe(0);
  expect(families).toBeLessThanOrEqual(2);
});

test('no horizontal scroll at 375 and a real 404', async ({ page }) => {
  await page.setViewportSize({ width: 375, height: 812 });
  await page.goto('/');
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
  const res = await page.goto('/kaga-404-probe');
  expect(res?.status()).toBe(404);
});

test('no em or en dashes in rendered text', async ({ page }) => {
  await page.goto('/');
  expect(await page.evaluate(() => /[–—]/.test(document.body.innerText))).toBe(false);
});
```

The browser half of `kaga-launch-check` still runs once before launch for what a test cannot judge: whether the hero composition, imagery, and copy are any good.

## Reading CI cheaply

- One failing run: `gh run view <id> --log-failed | tail -60`. Never pull the full log into context.
- Waiting on a run: `gh run watch <id> --exit-status` once, in the background. No sleep loops.
- Two red runs on the same failure: Opus looks at it (the "same failure twice" rule), not another blind retry.
