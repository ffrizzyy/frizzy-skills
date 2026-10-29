# Project types, lifecycles, and what changes in the PRD

Contents
- Picking a delivery method
- Web apps, SaaS, and websites
- Mobile apps
- Desktop software, CLI tools, and libraries
- Browser and editor extensions
- Games
- APIs and backend services
- AI-powered features and agents
- Bots and platform integrations
- Embedded and IoT
- Combined projects

Per-type security standards, testing, shipping, and stack choices live in the by-type files of the sibling skills (frizzy-security, frizzy-test, frizzy-ship, frizzy-stack). This file keeps the lifecycle, exit criteria, and PRD swaps.

Fees, store rules, and engine licenses change. Treat every number below as a starting point to confirm by search, and put the confirmed number and the date in the PRD.

## Picking a delivery method

Choose one method per project and say why. A method that fits the team's size is better than the one with the most ceremony.

| Situation | Method | Reason |
|---|---|---|
| One developer or a very small team, requirements still moving | Kanban with a work-in-progress limit of 2 and a weekly demo | No ceremony to maintain, and the backlog can change daily |
| 2 to 8 people with a steady backlog | Scrum with 2-week sprints | Gives a rhythm for planning, review, and retrospectives |
| Small team, fuzzy problems, wants fixed time with variable scope | Shape Up: 6-week cycles with a 2-week cooldown | Scope shrinks to fit the time instead of the time stretching |
| Heavy regulation or safety (medical, automotive, core banking) | V-model or stage-gate with traceability, agile inside each stage | Auditors need requirement-to-test links |
| Game | GDLC, described below | Fun has to be proven before content is built |
| Hardware or firmware | Stage-gate with prototype, EVT, DVT, PVT builds | Tooling and certification lead times are long |

Add these to every software method:

- Trunk-based development with short-lived branches and feature flags for unfinished work.
- CI on every push: lint, type check, unit tests, dependency and secret scanning.
- A definition of done that includes tests, accessibility, security checks, and docs.
- Preview deployments per pull request where the platform supports them.

## Web apps, SaaS, and websites

Lifecycle: agile delivery inside a DevSecOps pipeline.

| Phase | Exit criteria |
|---|---|
| Discovery | Problem validated with at least a handful of target users or credible evidence; scope of the MVP agreed |
| Foundations | Repo, CI, environments, auth, design tokens, and one deployed "hello world" slice |
| MVP build | Features done in priority order, each deployed behind a flag when risky |
| Private beta | 10 to 50 real users, error rate and performance within budget, top bugs closed |
| Public launch | Legal pages live, monitoring and alerts live, rollback tested |
| Iterate | Weekly or biweekly releases driven by analytics and support tickets |

PRD swaps: use the full template. Add SEO (metadata, sitemap, structured data, Open Graph), performance budgets (Core Web Vitals), and browser support.

## Mobile apps

Lifecycle: agile with a release train and staged rollouts.

| Phase | Exit criteria |
|---|---|
| Discovery and prototype | Clickable prototype tested with real users on a real phone |
| Build | Internal builds every sprint through TestFlight and Play internal testing |
| Closed beta | Crash-free sessions above the target; permission prompts and onboarding tested |
| Store review | Privacy labels, data safety form, screenshots, and review notes prepared in advance |
| Staged rollout | Release to a small percentage first, widen as crash rates stay low |
| Iterate | Monthly releases, forced-update path for breaking API changes |

PRD swaps: replace the sitemap with a navigation map; add offline and sync behavior, push notification plan, permission rationale (why each permission, when asked), deep links, app size and startup budgets, device and OS support matrix, store listing assets, and in-app purchase flows if any.

## Desktop software, CLI tools, and libraries

Lifecycle: agile with a release train. Libraries and CLIs add docs-first design and semantic versioning.

PRD swaps:
- Desktop apps: installer and update strategy, code signing (Windows certificate, Apple notarization), crash reporting, offline behavior, file associations, auto-update signature verification, and a shell choice (Tauri, Electron, or native) with a reason.
- CLI tools: command reference with examples, exit codes, config file format, shell completions, and output formats for humans and scripts.
- Libraries and SDKs: public API surface, semver policy, deprecation policy, supported runtimes, examples, and a docs site.

## Browser and editor extensions

Lifecycle: spike the permission model first, then build, then plan for store review time.

| Phase | Exit criteria |
|---|---|
| Permission spike | The smallest permission set that supports the core feature works in a throwaway build |
| Build | Service worker, content scripts, and UI work in Chrome; cross-browser plan written |
| Store prep | Single-purpose statement, privacy practices form, permission justifications, screenshots |
| Review and staged release | Review passes; rollout percentage increased gradually |
| Maintain | Track browser API changes and policy emails; update cadence monthly |

Chrome first with Manifest V3, then Firefox and Edge (Safari needs a conversion step and a developer account). Popups are size-limited (Chrome caps them around 800 by 600 pixels), so the design section must plan for that.

PRD swaps: replace the API section with the manifest (as a JSON block), permissions table (permission, why needed, what breaks without it), host permissions, content-script surfaces, message passing between parts, storage use and quotas, and update behavior.

## Games

Lifecycle: GDLC (game development life cycle). Fun gets proven before content gets made.

| Phase | What happens | Exit gate |
|---|---|---|
| Concept | Pitch, pillars, target player, platform, scope guardrails | One-page pitch and a list of what the game will not do |
| Pre-production | Paper or greybox prototype, core loop, tooling and pipeline setup, vertical slice plan | The core loop is fun with placeholder art; a 5-minute slice is playable |
| Production | Content and systems built in milestones: first playable, alpha (features complete), beta (content complete) | Each milestone has a playtest and a performance check |
| Polish | Balancing, juice, audio, accessibility, localization, bug bash | Crash-free on minimum spec; playtesters finish without help |
| Release | Store page, trailer, certification where needed, gold build, day-one patch plan | Platform checklists pass |
| Live ops | Patches, events, seasons, telemetry reviews, community | Retention and revenue targets reviewed monthly |

Small teams compress this to: prototype (find the fun) then vertical slice then production then polish then release, with a playtest at every transition.

PRD swaps: replace the features, data, and API sections with a game design section: pillars, core loop, mechanics and rules, progression, economy and balance, level or content plan, narrative, controls and input devices, camera, UI and HUD, art direction, audio direction, and tech notes (networking model, save system, target frame rate, minimum spec). Keep security, legal, testing, deployment, and costs.

## APIs and backend services

Lifecycle: API-first. Write the contract (OpenAPI for REST, AsyncAPI for events, GraphQL schema) before the implementation, and generate mocks and clients from it.

PRD swaps: the API section grows to cover versioning, pagination, idempotency keys, rate limits per plan, webhooks with signature verification, error model, SLOs, and a developer portal plan (docs, examples, API keys, sandbox).

## AI-powered features and agents

Lifecycle: add an LLMOps loop to the normal method: prototype prompts, build an evaluation set, add guardrails, ship behind a flag to a small group, then monitor quality, cost, and drift.

PRD swaps: model selection with a fallback, prompt and tool versioning, evaluation plan (test set, metrics, pass thresholds), cost per request and per user with hard caps, latency budget, retrieval design if used, data handling (what leaves your system, provider retention and training terms), human review for risky actions, and abuse handling.

## Bots and platform integrations

Covers Discord, Telegram, Slack, WhatsApp, Shopify apps, and similar.

Lifecycle: small agile cycles; the platform's review process often sets the schedule.

PRD swaps: platform permissions and scopes (least privilege), event and webhook handling, signature verification, rate-limit behavior, idempotency, install and uninstall flows, data deletion on uninstall, and marketplace listing requirements.

## Embedded and IoT

Short guidance only; escalate to a specialist for safety-critical work.

Lifecycle: stage-gate with prototype, validation, and production builds. Security: secure boot, signed over-the-air updates, unique device credentials, no default passwords, and an update path for the product's whole supported life. PRD swaps: hardware bill of materials, firmware architecture, power budget, certification (CE, FCC, and regional equivalents), and manufacturing test plan.

## Combined projects

Many briefs mix types: a web app with a mobile companion, a game with a web leaderboard, an extension with a backend. Handle them this way.

1. Name one primary type. It sets the lifecycle and the main structure of the PRD. Secondary types contribute sections.
2. Share what can be shared: one backend and API contract, one auth system, one design token source, one repository (a monorepo with workspaces, such as pnpm workspaces plus Turborepo or Nx).
3. Write the API contract before the clients so web, mobile, and extension teams can move in parallel.
4. Version the contract and plan for old mobile clients, since app-store users update slowly.
5. Give each surface its own testing and shipping section, because review processes and rollout controls differ.
6. In the roadmap, ship the primary surface first. Add secondary surfaces only after the shared core is stable, unless the idea only works with both.
7. Run the lint script with every relevant profile, for example `--profile web --profile mobile`.
