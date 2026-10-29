---
name: frizzy-ship
description: Infrastructure, development workflow, deployment, and launch planning for any software project. Environments and backups with recovery targets, observability and alerts, CI/CD pipeline, rollback, launch checklist, first 72 hours, app store and extension store submission steps and fees, and a lean build kit for the coding agent (reuse-first discipline, shorter agent replies, codebase graphs, test-first method) with a setup that fits the project size. Use this whenever the user asks how to deploy, host, or launch something, wants a CI/CD or release plan, a launch checklist, store submission steps, environment or backup planning, how to set up a project for a coding agent, an AGENTS.md, a development workflow, or sections 12, 15, and 16 of a project-frizzy PRD, even if they only say "how do I ship this".
---

# frizzy-ship

Owns PRD sections 12 (infrastructure and environments), 15 (development workflow), and 16 (deployment and shipping plan), plus the build kit used while the project is built.

## Two ways to run

- Called by project-frizzy: take the handoff (project type, hosting and services chosen, delivery method, team, region), write sections 12, 15, and 16 at lean depth, and return them.
- Standalone: the person asks for a deploy plan, a launch checklist, store steps, or a project setup for a coding agent. Write `SHIP.md` with the same headings, or answer inline. Ask only when the target (web, store, package registry) is ambiguous.

## Workflow

1. Read what you need in one call:
   `python3 scripts/section.py references/shipping-by-type.md::"Web apps" references/ecosystem.md::"Choosing the kit" references/section-guide.md::"16"`.
2. Use the delivery method from the PRD title block. When standalone, choose: Kanban with a work-in-progress limit of 2 for one developer, Scrum for 2 to 8 people with a steady backlog, GDLC for games.
3. Store and platform fees and rules come from `references/facts.md`. Stable rows are reusable for 60 days after the checked date; the PRD cites that date. Search (standard mode) only for a store or platform not listed or a row older than 60 days.
4. Choose the build kit for section 15 with the table in `references/ecosystem.md`: at most four tools, at most two always-on, one build discipline. Ask before installing anything, use official sources only, and record privacy flags and install commands in the PRD.
5. Write the sections once in final form.

## Section contract

| # | Section | Cap | Lean content |
|---|---|---|---|
| 12 | Infrastructure and environments | 20 | Environment table, backups with recovery point and time, observability, alert thresholds |
| 15 | Development workflow | 25 | Method, setup commands, a build kit of up to four tools, environment variable table, agent instructions in 8 bullets or fewer |
| 16 | Deployment and shipping plan | 25 | Pipeline, rollback, launch checklist (with the audit item), first 72 hours, store steps if any |

Never cut: rollback, the backup recovery point and time, the launch checklist items for legal pages and consent, and the security audit item.

## Starting the build

Work one milestone at a time from the PRD roadmap and keep the PRD current. Tell the agent that `PRD.md` is the specification. Follow the kit's handoff notes in `references/ecosystem.md` ("Starting the build with a kit"). Use playwright-cli for visual checks when frizzy-test finds it installed, and run the planned security audits at their milestones.

## Handoffs to sibling skills

- From frizzy-stack: hosting choice, environments, and environment variable names.
- From frizzy-security: header baseline, secret handling, backup numbers, and the launch checklist items for legal pages and consent.
- From frizzy-test: the CI stages that run each test layer and the release gates.
- To project-frizzy: the roadmap tickets for pipeline, launch, and store steps, with feature IDs where they apply.

Writing rules for any text this skill produces for a PRD: sentence case headings, no emoji, no horizontal rules, no em or en dashes (write ranges with "to"), no bold labels on list items, no "not just X but Y" or "it is not X, it is Y", no staged openers or one-line closers, none of crucial, pivotal, seamless, leverage, robust, vibrant, showcase, delve, cutting-edge, holistic, empower. Name specifics instead of adjectives, decision before reasoning, straight quotes. No placeholders: unknowns become open questions with an owner and a date.

## Reference map

| File | Use |
|---|---|
| `references/ecosystem.md` | Build kit by project size, consistency rules, handoff notes |
| `references/shipping-by-type.md` | Shipping paths, fees, and hosting watch-outs per type |
| `references/section-guide.md` | Full-mode guidance for sections 12, 15, and 16 |
| `references/facts.md` | Dated store, platform, and build-kit tool facts |
| `scripts/section.py` | Print only the headings you need |
