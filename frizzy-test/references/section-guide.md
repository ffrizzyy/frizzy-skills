# Section guide

Full guidance for the PRD sections this skill owns. Keep the exact section headings so the PRD linter and the owner can navigate. Rules for every PRD section: each section opens with the decision or the answer. Tables for anything comparable. Every sourced figure carries "checked YYYY-MM-DD". No placeholders: unknowns become open questions with an owner and a date. Stable IDs: goals G-1, features F-001, screens S-01, endpoints E-01, risks R-1, open questions OQ-1, decisions D-01. Sentence case headings, no emoji, no horizontal rules, no em or en dashes.

### 14. Testing and quality
- Strategy: test pyramid with target proportions and the tools for each layer.
- Unit and integration tests, end-to-end tests with Playwright covering each core flow, accessibility checks with axe, visual checks with screenshots at the breakpoint set, performance checks with Lighthouse CI, security scans (SAST, dependency, secrets, DAST where useful), and load tests where traffic matters.
- Test data and fixtures, device and browser matrix, coverage targets stated as numbers, flaky-test policy.
- Beta and UAT plan: who, how many, how feedback is collected. Games add playtest plans.
- Definition of done and a bug severity scale with response targets.
- Playwright tooling note: playwright-cli commands for local verification (open, resize, screenshot, console, requests, record, generate tests) and how tests run in CI. If the owner declined the global CLI install, use `@playwright/test` as a project dependency instead.
