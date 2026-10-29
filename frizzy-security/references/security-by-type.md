# Security and policy by project type

Read the part for the project's type. Standards change, so confirm the edition by search and write its year in the PRD.

## Web apps, SaaS, and websites

Security standard: OWASP Top 10 plus ASVS (level 1 for most MVPs, level 2 when handling payments, health, or identity data). Add the OWASP API Security Top 10 if the app exposes an API.

## Mobile apps

Security standard: OWASP MASVS (verification levels) and MASTG for test procedures. Store credentials in the platform keychain or keystore, pin certificates only with a rotation plan, and validate purchase receipts on the server.

Policy checkpoints: Apple App Review Guidelines (account deletion, privacy nutrition labels, Sign in with Apple rules when other social logins exist), Google Play policies (Data safety form, target API level, account deletion, closed-testing requirements for new personal developer accounts). Confirm the current rules by search.

## Desktop software, CLI tools, and libraries

Security standard: for Electron, follow the framework's security checklist (context isolation, no remote code, strict CSP); sign every release; verify update signatures. For packages, use two-factor on registry accounts, provenance attestations where supported, a minimal dependency tree, and SLSA-style build practices.

## Browser and editor extensions

Security standard: least privilege for permissions, no remotely hosted code, strict extension-page CSP, sanitize anything injected into pages, never trust page content, store no secrets in the extension. Review each permission against what the store will ask you to justify.

## Games

Age classification: every storefront has its own questionnaire, and several countries run national systems. Search for the rules of each country where players will be. Example found in 2026 research: Indonesia's IGRS has been mandatory since January 2026 for local and foreign games, with self-assessed categories 3+, 7+, 13+, 15+, 18+ and RC, labels required in the game and on store pages, and take-downs threatened for wrong ratings. Treat a missing or wrong rating as a launch blocker and put the steps in the PRD.

Security standard: server-authoritative logic for anything that matters in multiplayer, signed or checksummed saves, receipt validation for purchases, rate limits on matchmaking and chat, and anti-cheat proportional to the stakes. Add child safety if minors can play, loot-box rules by region, chat moderation, and age ratings (IARC, ESRB, PEGI).

## APIs and backend services

Security standard: OWASP API Security Top 10 (2023 edition at the time of writing; confirm). Cover broken object-level authorization first, since it is the most common failure.

## AI-powered features and agents

Security standard: OWASP Top 10 for LLM Applications (confirm the current edition). Cover prompt injection (direct and through retrieved content), insecure output handling, excessive agency (limit tools and scopes), sensitive data disclosure, and unbounded consumption (rate limits and spend caps).

## Bots and platform integrations

Security standard: verify every webhook signature, store tokens encrypted, request minimal OAuth scopes, and handle token rotation.
