# Section guide

Full guidance for the PRD sections this skill owns. Keep the exact headings. Each section opens with the decision; tables for anything comparable; sourced figures carry "checked YYYY-MM-DD"; no placeholders; stable IDs (G-1, F-001, S-01, E-01, R-1, OQ-1, D-01); sentence case headings.

### 14. Testing and quality
- Strategy: test pyramid with target proportions and the tools for each layer.
- Unit and integration tests, end-to-end tests with Playwright covering each core flow, accessibility checks with axe, visual checks with screenshots at the breakpoint set, performance checks with Lighthouse CI, security scans (SAST, dependency, secrets, DAST where useful), and load tests where traffic matters.
- Test data and fixtures, device and browser matrix, coverage targets stated as numbers, flaky-test policy.
- Beta and UAT plan: who, how many, how feedback is collected. Games add playtest plans.
- Definition of done and a bug severity scale with response targets.
- Playwright tooling note: playwright-cli commands for local verification (open, resize, screenshot, console, requests, record, generate tests) and how tests run in CI. If the owner declined the global CLI install, use `@playwright/test` as a project dependency instead.
