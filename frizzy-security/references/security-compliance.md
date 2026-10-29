# Security, privacy, and compliance

Contents
- How to use this file
- Baseline for every project
- Standards by project type
- OWASP mapping table for the PRD
- Legal documents plan
- Cookies, tracking, and consent
- Data map and user rights
- Regional rules
- Store and platform policies
- Payments
- Vulnerability management and incident response

## How to use this file

The PRD's security section has to be specific: named standards, a mapping from each risk to a control in this project, and a list of legal documents with the facts they will state. A section that says "we follow best practices" fails the bar.

Laws and standards change. Search for the current edition of each standard and the current text of each regional rule, and write the year or version into the PRD. State plainly that the PRD is a plan and not legal advice, and that policies need review by a qualified lawyer before launch. This matters most for payments, health, children's data, and anything sold in the EU.

## Baseline for every project

Include a short table in the PRD with each control, the choice made, and where it lives in the design.

Identity and access
- Prefer a managed auth provider or a mature library over custom code. If passwords exist, hash with Argon2id (or scrypt or bcrypt with sensible cost factors). Offer passkeys or MFA for anything beyond a toy.
- Authorization is checked on the server for every object, not only in the UI. Use row-level security or a central policy layer. Write an authorization matrix (role by resource by action) in the PRD.
- Sessions: HttpOnly, Secure, SameSite cookies; short-lived access tokens; rotation and revocation; idle and absolute timeouts.

Input and output
- Validate input at the boundary with a schema library; encode output for its context; use parameterized queries only.
- Uploads: allow-list types, check magic bytes, cap size, store outside the web root, scan if public sharing exists, and serve from a separate origin.
- Protect against CSRF, SSRF, open redirects, and mass assignment.

Transport and headers
- HTTPS everywhere with HSTS. Set CSP, X-Content-Type-Options, Referrer-Policy, Permissions-Policy, and frame protections. Configure CORS to named origins.

Secrets and supply chain
- No secrets in the repo or client bundle. Use the platform's secret store, separate secrets per environment, and a rotation plan.
- Lockfiles committed, Dependabot or Renovate enabled, `npm audit` or OSV scanning in CI, secret scanning (gitleaks or the platform's), CodeQL or Semgrep for static analysis, pinned CI actions, and least-privilege CI tokens.
- Generate an SBOM for releases if customers will ask for one.

Data protection
- Encrypt in transit and at rest (managed databases do this by default; confirm). Classify data (public, internal, personal, sensitive) and note where each class lives.
- Logs never hold passwords, tokens, or full personal data. Set log retention.
- Backups: automated, encrypted, restore tested once before launch and on a schedule after. State RPO and RTO in plain numbers.

Abuse and availability
- Rate limits on login, signup, password reset, search, and expensive endpoints. Bot protection on public forms (Cloudflare Turnstile is a free option; confirm). Budget alerts on every metered service.

Threat modeling
- Run a lightweight STRIDE pass on each main flow (signup, login, payment, upload, admin). Record assets, entry points, threats, and mitigations in a table. Repeat when a new surface ships.

## Standards by project type

| Project | Primary standards | Also read |
|---|---|---|
| Web app or site | OWASP Top 10, OWASP ASVS (level 1 for MVPs, level 2 for sensitive data), OWASP Proactive Controls | OWASP Cheat Sheet Series for each feature (auth, sessions, file upload, CSP) |
| API or backend | OWASP API Security Top 10 | ASVS sections on APIs and authentication |
| Mobile app | OWASP MASVS and MASTG | Apple and Google platform security guides |
| AI or LLM feature | OWASP Top 10 for LLM Applications | Provider data-use terms; NIST AI RMF for governance language |
| Desktop app | Framework hardening guide (for example Electron's security checklist), code signing practices | OS sandboxing and notarization docs |
| Browser extension | Store policies, least-privilege permissions, Manifest V3 security model | OWASP Top 10 for any web surface the extension talks to |
| Game | Server-authoritative design, save integrity, receipt validation, anti-cheat appropriate to stakes | Platform certification rules, child safety rules |
| CI/CD and releases | OWASP Top 10 CI/CD Security Risks, SLSA levels | Provider hardening guides |
| Payments | PCI DSS (aim for the smallest scope, usually SAQ A with hosted checkout) | Provider integration security guide |

Search for the current edition of each list and write the edition year in the PRD. If an edition has just changed, say which one the plan targets.

## OWASP mapping table for the PRD

Use the Top 10 categories of the current edition as rows. For each row write the project-specific control and the place it lives. The example rows use the OWASP Top 10:2025 names (announced November 2025, final January 2026). The 2021 list it replaced is still quoted widely, so confirm the current edition by search and write the year in the PRD.

| Risk | Control in this project | Where |
|---|---|---|
| A01 Broken access control (server-side request forgery is folded in here) | Row-level security on every table; authorization matrix tests in CI; allow-list outbound hosts for any fetch-by-URL feature | Data model, API sections |
| A02 Security misconfiguration | Header baseline, environment parity, IaC review, no default credentials | Infrastructure, CI |
| A03 Software supply chain failures | Lockfile, Renovate weekly, OSV scan blocks merges on high severity, pinned CI actions, SBOM on release | CI |
| A04 Cryptographic failures | Managed TLS, encrypted database, Argon2id for any passwords, no custom crypto | Infrastructure |
| A05 Injection | ORM or parameterized queries; schema validation on every endpoint | Backend |
| A06 Insecure design | Threat model per flow; abuse cases in user stories | Security section |
| A07 Authentication failures | Managed auth, MFA option, rate-limited login, breached-password check | Auth flow |
| A08 Software or data integrity failures | Signed releases, verified update channel, idempotent writes | Deployment |
| A09 Security logging and alerting failures | Structured logs, auth and admin events audited, alerts on anomalies | Observability |
| A10 Mishandling of exceptional conditions | Fail closed, retries with backoff, friendly error states, global error reporting | Backend, front end |

Adjust for the project: drop rows that cannot apply and say why in one line, add rows from the type-specific list (API, mobile, LLM).

## Legal documents plan

Create a table in the PRD with one row per document: purpose, where it lives, when the user sees it, how versions are tracked, and who owns updates. Then give a policy fact sheet (see "Data map") so a lawyer or policy generator can draft from facts instead of guesses. Do not write the full text of any policy or terms document into the PRD. The plan, the fact sheet, and a heading outline for each document are the limit.

| Document | Needed when | Where it appears |
|---|---|---|
| Privacy policy | Any personal data, analytics, or accounts. Required by app stores and most laws. | Footer link, signup screen, app store listing, in-app settings |
| Terms of service (or EULA for software and games) | Accounts, payments, user content, or usage limits | Signup checkbox or "by continuing" notice, footer, settings |
| Cookie policy and consent banner | Any cookies or similar storage beyond the strictly necessary, especially with EU or UK users | First visit banner, footer "cookie settings" link |
| Acceptable use policy and community guidelines | User-generated content, chat, or public profiles | Linked from terms, report flow |
| Copyright takedown process | User uploads or user-posted content | Footer, report flow |
| Refund and cancellation policy | Paid products | Checkout, terms |
| Data processing agreement and subprocessor list | Business customers, or any processing on behalf of other companies | Legal page, on request |
| Children's privacy notice | Product may reach minors | Signup flow, privacy policy |
| Accessibility statement | Public-sector customers, EU market, or good practice | Footer |
| Security contact (security.txt) and disclosure policy | Any public service | /.well-known/security.txt |

Operational pieces that come with the documents: account deletion and data export flows (app stores require in-app deletion for apps with accounts), a record of consent with timestamp and version, retention schedule per data class, a breach response plan, and a plain-language changelog for policy updates with notice to users when changes are material.

## Cookies, tracking, and consent

Design rules to write into the PRD:

1. Classify every cookie, local-storage key, pixel, and SDK as strictly necessary, preferences, analytics, or marketing. Put the list in the policy fact sheet.
2. In regimes that need opt-in consent (the EU and UK, and a growing number of others), load nothing outside the strictly necessary class before the person agrees. Prefer analytics that need no cookies and no consent where the law allows (confirm for the region), since it also removes the banner friction.
3. Make rejecting as easy as accepting: same screen, same visual weight, no pre-ticked boxes, no dark patterns. Offer granular choices behind a "customize" control.
4. Record the choice with a version and timestamp, let people change it at any time from a footer link, and ask again when categories change or after a set period.
5. If ads or measurement run through Google, implement Consent Mode v2 and use a consent management platform certified for it. Confirm current requirements.
6. Honor Global Privacy Control and similar signals where the law requires it (for example, several US states).
7. Mobile apps follow the platform prompts (App Tracking Transparency on iOS) and the store's data disclosure forms. Games add telemetry consent, and any under-age flow follows COPPA and local equivalents.

Provide the banner's states in the user flow section: first visit, accepted, rejected, customized, and changed later.

## Data map and user rights

Create the data map table once and reuse it everywhere (privacy policy, store forms, DPA):

| Data item | Purpose | Legal basis (where relevant) | Stored where | Shared with | Retention | Deletable by user |
|---|---|---|---|---|---|---|

Then plan the rights flows: access and export, correction, deletion, objection or opt-out, and portability. Give each a user-facing path (a settings page, not an email-only process), a backend job, and a target response time. Under GDPR the standard response window is one month, and a personal data breach has to be reported to the regulator within 72 hours when it creates risk. Confirm for each region in scope.

## Regional rules

List only the regions that apply, and state what each one changes in the build. Verify each by search and write the date.

| Region | Main rules to check | What it usually changes |
|---|---|---|
| EU and UK | GDPR or UK GDPR, ePrivacy (cookies), Digital Services Act for platforms, age rules for children's consent | Consent banner, data export and deletion, lawful basis, processor agreements, possibly a representative |
| United States | State privacy laws (California CCPA and CPRA and others), COPPA for under-13, CAN-SPAM, accessibility claims under the ADA | "Do not sell or share" link where it applies, parental consent flows, email unsubscribe |
| Indonesia | Personal Data Protection Law (UU PDP, Law No. 27 of 2022, in force after a two-year transition). Its implementing regulation, Government Regulation 33 of 2026, was promulgated in July 2026 and sets lawful bases, rights handling, processing records, breach duties, and transfer rules. Private electronic system operator registration under Ministry of Communication and Information Regulation 5 of 2020 (Articles 2 and 4) is being enforced with warnings and access blocking. The ITE law also applies. | Explicit consent kept separate from general terms (law firms warn that bundled consent may be treated as ambiguous), a processing inventory, a breach procedure (sources disagree on the window, use the stricter 3 x 24 hours until counsel says otherwise), a rights process, a legal basis for storing data abroad, and a registration check before launch. Verify all of this by search, because the regulation and its enforcement were still moving. |
| Singapore | PDPA | Consent, purpose limitation, a named data protection officer |
| Brazil | LGPD | Rights flows, lawful basis, local contact |
| India | Digital Personal Data Protection Act 2023 | Consent notices, grievance contact |
| Canada, Australia, Japan | PIPEDA, Privacy Act, APPI | Consent, cross-border transfer notices |

When the target region is unknown, default to a GDPR-grade baseline and add a line telling the owner which regions to confirm before launch.

## Store and platform policies

- Apple: privacy nutrition labels, in-app account deletion, Sign in with Apple rules when third-party login exists (confirm current guideline), in-app purchase rules for digital goods, and review notes with test credentials.
- Google Play: Data safety form, account deletion, target API level, testing track requirements for new personal developer accounts, and payments policy.
- Chrome Web Store: single purpose, narrowly scoped permissions with justification, privacy practices disclosure, no remote code.
- Steam and console stores: content descriptions, age rating, tax and banking setup, and platform certification checklists.
- National game rating systems: some countries require their own age label on top of the store's (Indonesia's IGRS has been mandatory since January 2026). Search for the rules in every player country, self-assess early, keep the answers on file, and do not copy a label shown by a storefront unless it matches the official record.
- Merchant of record services (for example Paddle, Lemon Squeezy, Polar) handle sales tax and VAT for you. Confirm current terms and fees. They are often the simplest route for a solo seller.

## Payments

- Never touch raw card numbers. Use hosted checkout or hosted fields so PCI scope stays at the smallest level (usually SAQ A).
- Verify webhook signatures, make handlers idempotent, store the provider's customer and subscription IDs, and treat the provider as the source of truth for payment state.
- Plan for failed payments, refunds, chargebacks, proration, trials, tax invoices, and cancellation flows. Each needs a user-flow entry.
- Show total price including taxes and fees before payment, and make cancellation as easy as signup (several jurisdictions require it).

## Pre-launch code security audit

The PRD plans a code audit for the build stage. Nothing is audited during planning, because there is no code yet. Cloudflare's open-source `security-audit` skill (MIT) is the recommended tool: it runs reconnaissance, coverage-led hunting, adversarial validation by a different agent than the finder, structured findings, independent verification, and a report. See `facts.md` for its requirements and install command.

What the PRD records (lean mode: five or six lines in the security section):
1. When: a first pass once the core features exist and before the beta, and a second pass on the release candidate. Repeated runs are additive and find more than one run.
2. How: install with `npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit` (ask before installing), then ask the agent "security audit this codebase". Write the output outside the repository, for example `~/audits/<project>/`, or in an ignored folder.
3. Requirements: a coding agent with parallel sub-agents (not a plain chat window), Node.js, and an OS-enforced sandbox with no external network for any target code it runs. Without the sandbox it leaves leads as `needs_validation`.
4. Triage rule: every `confirmed` finding is fixed or explicitly accepted by the owner before the milestone closes; every `needs_validation` item gets an owner and a date; `rejected` items are ignored. Findings never go into a public repository.
5. Cost: it uses many agents, so budget it as agent usage and plan two runs. Name it as a cost line (usage, not dollars) so it is not a surprise.
6. Scope hints: the audit chooses its own attack classes from reconnaissance, but the PRD can name the classes likely to matter so the owner can steer it.

Likely attack classes by project type (the class names come from that repository's file list):

| Project | Classes likely to matter |
|---|---|
| Every project | Core, wildcard, and obvious-things classes; supply chain and release (dependencies, CI, signing, updates, plugins) |
| Web app or site | Web protocol and auth; client side (DOM injection, messaging trust, UI redress, prototype pollution); data isolation and lifecycle if users have separate data |
| API or backend | Web protocol and auth; protocols, RPC, and messaging; resource exhaustion and availability; data isolation and lifecycle |
| Browser extension | Client side; supply chain and release (extension updates); desktop, mobile, and local IPC (messaging between parts); AI and LLM if a model is used |
| AI feature or agent | AI and LLM (prompt injection, agent and tool risks, output handling); resource exhaustion (spend); data isolation |
| Mobile or desktop app | Desktop, mobile, and local IPC (deep links, webviews, exported components, helpers); supply chain and release; memory safety and binary for native code |
| Game | Supply chain and release; desktop and local IPC for desktop builds; save and input parsing under the core classes; memory safety only for native modules |
| Bot or integration | Protocols, RPC, and messaging (webhooks); web protocol and auth; resource exhaustion |
| Infrastructure as code, containers, serverless | Cloud and deployment |

For a cheaper layer on every diff, ponytail's `/ponytail-review` is an option (see the build kit in frizzy-ship); it does not replace the audit, and the two should not both run on every change. Do not treat the audit as a replacement for the controls in this reference. It finds boundary failures in code that exists, and the standards, threat model, and tests still define what the code must do.

## Vulnerability management and incident response

Include in the PRD:

- A severity scale and fix targets, for example critical within 24 hours and high within 7 days, adjusted to team size.
- A security contact and disclosure policy.
- An incident runbook outline: detect, contain, assess, notify (users and regulators where required), fix, review. Name the role that decides, even if the team is one person.
- A monitoring list: failed logins, privilege changes, unusual export volume, error spikes, billing anomalies.
- A yearly review date for dependencies, credentials, backups, and policies.
