# Section guide

Full guidance for the PRD sections this skill owns. Keep the exact headings. Each section opens with the decision; tables for anything comparable; sourced figures carry "checked YYYY-MM-DD"; no placeholders; stable IDs (G-1, F-001, S-01, E-01, R-1, OQ-1, D-01); sentence case headings.

### 12. Infrastructure and environments
Hosting topology diagram or table, an environment matrix (URL, data, secrets, who can deploy), domains and DNS, email authentication records, CDN and caching, scaling approach and the thresholds that trigger it, backups with stated RPO and RTO, disaster recovery steps, infrastructure as code choice, observability (logs, metrics, traces, uptime checks, alerts, status page), and the cost guardrails from the frizzy-stack skill.

### 15. Development workflow
Delivery method and cadence, branching and commit conventions, code review rules, CI stages in order, pre-commit hooks, linters and formatters, local setup in copy-pasteable commands, an environment variable table (name, purpose, example shape, where set, secret or not), scripts reference, documentation habits, and an agent instructions block for coding agents: repository conventions, commands to run before finishing, files not to touch, and the definition of done.

### 16. Deployment and shipping plan
Pipeline from commit to production, preview and staging flow, release strategy (feature flags, canary, staged rollout), database migration policy, versioning and changelog, rollback steps with a tested drill, and a launch checklist covering legal pages live, consent working, monitoring on, backups verified, DNS and email authentication correct, store assets ready, support channel ready, and a communication plan. Add the first 72 hours after launch (what to watch, who is on call) and the maintenance cadence (dependency updates, credential rotation, backup restore test, policy review). Stores: submission steps, review timelines, and rejection fallback.
