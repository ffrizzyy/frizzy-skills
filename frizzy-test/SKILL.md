---
name: frizzy-test
description: Test strategy and quality planning for any project: test layers with tools and numeric targets, Playwright end-to-end flows, accessibility and performance checks, API contract and load tests, AI evaluations, playtests, a beta plan, definition of done, and visual checks from phone to desktop widths. Use for a test plan, QA, accessibility, beta, or section 14 of a PRD, even if they never say test plan.
---

# frizzy-test

Owns PRD section 14 (testing and quality) and the environment check for the build tooling (playwright-cli). Also guides visual and flow verification while the build runs.

## Two ways to run

- Called by project-frizzy: take the handoff (project type, key flows, endpoints, security rows, accessibility target), write section 14 at lean depth, and return it.
- Standalone: the person asks for a test plan, a QA checklist, or help setting up Playwright. Write `TEST-PLAN.md` with the same headings, or answer inline for a small ask.

## Environment check (only when it helps)

Skip it in the claude.ai container (`/mnt/user-data` exists) and for projects with no browser surface; then write "not checked in the planning environment" wherever the PRD mentions installed tools. Otherwise run `bash scripts/check_env.sh` once. If `playwright-cli` is missing and the project has a browser surface, ask before installing it (commands in `references/facts.md`, only on the person's own machine). Never install any tool without a yes. If skipped or declined, put the install commands in the PRD's tooling note and plan `@playwright/test` as a project dependency instead.

## Workflow

1. Read what you need in one call:
   `python3 scripts/section.py references/testing-by-type.md::"Web apps" references/section-guide.md::"14"`.
2. Pick the layers that fit the project and set numeric targets (coverage, performance budgets, crash-free sessions). A small project answers in one table, but never drops the layers it needs.
3. List the key end-to-end flows by feature ID (first run, signup and login, the main task, payment, account deletion, consent banner).
4. Add the security rows from frizzy-security: SAST, dependency and secret scanning, authorization matrix tests, and the planned pre-launch code security audit.
5. Write the beta plan (who, how many, how feedback arrives; games add playtests), the definition of done, and the bug severity scale with response targets.
6. Write the section once in final form.

## Section contract

| # | Section | Cap | Lean content |
|---|---|---|---|
| 14 | Testing and quality | 20 | Layer table with tools and targets (including a code security audit row), key end-to-end flows, beta plan, definition of done, playwright-cli note |

## During the build

Verify visually at 375, 768, 1280, and 1920 pixel widths with playwright-cli when it is installed: open the app, resize, take a screenshot, read console and network output, record a flow, generate an end-to-end test. Compare against the design reference when one exists. Run the planned security audits at their milestone gates and keep the PRD's definition of done as the exit check for each milestone.

## Handoffs to sibling skills

- From frizzy-design: accessibility targets and the viewport set.
- From frizzy-security: security test rows and the audit plan.
- From frizzy-stack: the endpoint list and authorization matrix.
- To frizzy-ship: the CI stages that run each layer and the checks that gate a release.

Writing rules: one title, sentence case headings, no emoji or horizontal rules, no em or en dashes (write ranges with "to"), no bold labels on list items, no "not just X but Y", no staged openers, and none of crucial, pivotal, seamless, leverage, robust, vibrant, showcase, delve, cutting-edge, holistic, empower. Name specifics, decision before reasoning, straight quotes. No placeholders: unknowns become open questions with an owner and a date.

## Reference map

| File | Use |
|---|---|
| `references/testing-by-type.md` | Test layers for web, game, API, and AI projects |
| `references/section-guide.md` | Full-mode guidance for section 14 |
| `references/facts.md` | Dated facts for playwright-cli |
| `scripts/check_env.sh` | Read-only environment check |
| `scripts/section.py` | Print only the headings you need |
