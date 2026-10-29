# Stack choices and costs

Contents
- Principles
- Decision record format
- Candidate services by category
- Starting stacks by project type
- Verifying prices and limits
- Free-tier traps
- Cost tables for the PRD
- Cost guardrails

## Principles

1. Pick the cheapest option that meets the launch requirements, then show the ideal option next to it with its price and the signal that says it is time to move. Free first keeps a project alive on a zero budget. The ideal column keeps the owner from boxing themselves in.
2. Prefer boring, widely used, well-documented tools. A coding agent and a future hire both do better with a stack that has years of public examples.
3. Fewer moving parts beat clever parts. Every extra service adds a bill, a login, a failure mode, and a security review.
4. Avoid lock-in where it is cheap to avoid: standard Postgres, S3-compatible storage, OpenAPI contracts, and portable auth data make later moves possible.
5. A free tier counts only if its limits fit the launch and its terms allow the use (commercial use, data location, uptime expectations).
6. Match the team's skills. A stack the owner cannot debug is more expensive than a paid one.

## Decision record format

Use this block for each major decision (frontend framework, backend, database, auth, hosting, payments, and so on). Put the full records in the stack section and a one-line summary table in the TL;DR.

| Field | Content |
|---|---|
| Decision | What is being chosen |
| Free or cheapest pick | Name, cost, the limit that matters, checked on YYYY-MM-DD |
| Ideal pick | Name, cost at launch scale, what it adds |
| Why this pick | Two or three sentences with the actual reason (fit, skills, maturity, license) |
| Switch trigger | The measurable signal for moving to the ideal pick (for example, database over 400 MB or more than 5,000 monthly active users) |
| Migration effort | Small, medium, or large, and what moves |
| Rejected options | One line each with the reason |

## Candidate services by category

These are starting points. Confirm every name, price, and limit by search before using it. The lists reflect what was common at the time of writing and will drift.

| Category | Free or cheapest candidates | Ideal candidates | Notes |
|---|---|---|---|
| Web framework | Next.js, Astro, SvelteKit, Nuxt, Remix or React Router, plain Vite and React | Same, with paid hosting | Astro suits content sites; Next.js suits app-like products with server rendering |
| Mobile framework | PWA, Capacitor, Expo (React Native), Flutter | Native Swift and Kotlin | PWA has zero store fees |
| Hosting (frontend and edge) | Cloudflare Pages or Workers, Netlify, Vercel hobby (check commercial-use terms), GitHub Pages for static sites | Vercel Pro, Cloudflare paid plans, Fly.io, AWS | Hobby plans on some hosts forbid commercial use |
| Backend runtime | Serverless functions, Cloudflare Workers, a single small container on a free or low-cost host (Render, Railway, Fly.io; confirm free allowances) | Managed containers, Kubernetes only at real scale | A monolith first is usually right |
| Database | Postgres from Supabase, Neon, or similar free tiers; SQLite or Turso for small apps; Firebase Firestore for simple mobile | Managed Postgres with backups and read replicas | Free databases may pause when idle or cap storage |
| Auth | Supabase Auth, Better Auth, Auth.js, Clerk free tier, Firebase Auth | Clerk, Auth0, WorkOS (when enterprise SSO appears) | Check monthly-active-user limits and SSO paywalls |
| File storage | Cloudflare R2, Supabase Storage, Backblaze B2, Firebase Storage | S3 with CloudFront | Compare egress fees, not just storage price |
| Email (transactional) | Resend, Brevo, Postmark trial, Amazon SES | Postmark, SES with a dedicated IP | Set SPF, DKIM, and DMARC on day one |
| Payments | Stripe (no monthly fee, per-transaction fee), Lemon Squeezy, Paddle, Polar (merchant of record) | Stripe plus a tax service, or a merchant of record at scale | Merchant of record handles tax and VAT |
| Analytics | Plausible self-hosted, Umami, PostHog free tier, Cloudflare Web Analytics | PostHog paid, Amplitude, Mixpanel | Cookieless options reduce consent friction |
| Error monitoring | Sentry free tier, GlitchTip self-hosted | Sentry paid, Datadog | Scrub personal data before sending |
| Logs and metrics | Platform logs, Grafana Cloud free tier, Better Stack free tier | Datadog, Grafana paid | Set retention to match the privacy policy |
| CI/CD | GitHub Actions free minutes, GitLab CI | Larger runners, Buildkite | Public repos get more free minutes |
| Search | Postgres full text, Meilisearch or Typesense self-hosted, Algolia free tier | Algolia or Elastic Cloud paid | Start with the database's own search |
| Realtime | Supabase Realtime, Firebase, Ably or Pusher free tiers, PartyKit | Dedicated realtime service | Check concurrent-connection caps |
| Queues and cron | Platform cron, Cloudflare Queues, Inngest or Trigger.dev free tiers, GitHub Actions schedules | SQS, managed workflow engines | |
| Push notifications | FCM and APNs (free), OneSignal free tier, Expo push | OneSignal or Braze paid | |
| Maps | MapLibre with OpenStreetMap tiles, Mapbox free tier | Google Maps Platform, Mapbox paid | Read the tile usage policy |
| CMS | Markdown in the repo, Decap CMS, Payload, Directus self-hosted, Sanity free tier | Contentful, Sanity paid | |
| AI models | Provider free tiers, Cloudflare Workers AI, Ollama for local development | Frontier model APIs with caching and evals | Always cap spend per user |
| Domain and DNS | Registrar at cost (about the price of a coffee each month), Cloudflare DNS | Same | Do not let the registrar and DNS live under one fragile login |
| Design assets | Open fonts (OFL), Phosphor or Tabler icons, Unsplash or Pexels photos (check license terms) | Commissioned illustration, licensed fonts, stock subscription | Keep a license list in the PRD appendix |
| Game engines | Godot, Phaser, PixiJS, Bevy | Unity or Unreal if the team already knows them (read current license) | |
| Store and developer accounts | Chrome Web Store (small one-time fee), Google Play (one-time fee), Apple Developer Program (yearly fee), Steam (per-title fee), itch.io (no fee) | Same | Confirm current amounts |

## Starting stacks by project type

Offer one starting stack per project in the PRD, then adjust to the brief and the research. These are shapes, not prescriptions.

- Content or marketing site: Astro, Markdown content, Cloudflare Pages, Plausible or Umami, a form provider.
- Web app with accounts: SvelteKit or Next.js, Postgres (Supabase or Neon), managed auth, Resend, Sentry free, GitHub Actions, Cloudflare or Vercel hosting.
- Mobile app: start as a PWA if features allow; otherwise Expo with a Supabase or Firebase backend and EAS builds on the free queue.
- Browser extension: TypeScript, WXT or Plasmo or plain Vite, a small serverless backend only if a feature needs one.
- 2D game: Godot with exports to web and desktop; itch.io for the first release.
- API product: a typed framework (Hono, Fastify, FastAPI, or similar), OpenAPI generated from code, Postgres, a free hosting tier for staging.
- AI feature: a thin server route that calls the model, with caching, a per-user daily cap, and an evaluation script in CI.

## Verifying prices and limits

Pricing pages change without notice, so verify each item rather than trusting this file.

1. Search for the official pricing page of each service in both columns. Prefer the vendor's own page over blog posts.
2. Record the limits that matter for this project (requests, storage, bandwidth, monthly active users, build minutes, seats, commercial-use terms).
3. Write the figure with the date: "50,000 monthly active users, checked 2026-10-23".
4. If a figure cannot be confirmed, say so in the PRD and give the range you found, with the source.
5. Note the currency. Convert to the owner's local currency only with a stated rate and date, and keep the original currency beside it.

## Free-tier traps

Add each trap that applies to the "watch for" line of the relevant decision record.

- Commercial-use bans on hobby plans.
- Projects that pause after inactivity, which looks like an outage to the first visitor after a quiet week.
- Egress and bandwidth charges that appear only after the free allowance.
- Per-seat pricing that jumps when a second teammate joins.
- Free tiers that disappear. Keep an exit path.
- Single-region hosting that conflicts with data-residency rules.
- No uptime guarantee on free plans.
- Free databases that include no automatic backups. Plan your own encrypted dumps and a tested restore, and make a paid plan the trigger for dropping them.
- Build minutes and image-transformation quotas that heavy previews can drain.
- Free email tiers that cap daily sends, which breaks password resets during a launch spike.
- Free map and font CDNs that carry privacy implications under GDPR. Self-host fonts and assets where possible.

## Cost tables for the PRD

Provide all three tables, in the project's currency, with the date of the research.

One-time and yearly fixed costs

| Item | Free or cheapest path | Cost | Ideal path | Cost | Needed by |
|---|---|---|---|---|---|

Include the domain, developer accounts, legal review, logo and brand work, fonts and icons, stock assets, code-signing certificates, and trademark search if relevant.

Monthly running costs at three sizes

| Service | Launch (about 0 to 100 users) | Growth (about 1,000 users) | Scale (about 10,000 users) | Notes |
|---|---|---|---|---|

Show the free or cheapest stack and the ideal stack as two blocks of rows with a total for each. Choose user counts that suit the product, and show the math behind any usage-based line (for example, cost per AI request times requests per user per month).

Upgrade triggers

| Trigger | Threshold | Action | Added monthly cost |
|---|---|---|---|

Summarize the headline numbers in the TL;DR: cost to launch, cost per month at launch on the cheapest path, and cost per month on the ideal path.

## Cost guardrails

- Budget alerts at 50, 80, and 100 percent on every metered service.
- Hard spending caps on AI and any pay-per-use API, enforced in code per user and per day.
- A monthly cost review in the maintenance plan.
- Prefer services that stop at a cap over services that bill without limit while the project is small.
