# PRD template and section guide

Contents
- Document rules
- Section order
- Section guidance
- Swaps by project type
- Skeleton to copy

## Document rules

- One file named `PRD.md`. A table of contents follows the title block. Each major section opens with the decision or the answer, then the detail.
- Two readers. An owner who may not be technical reads the TL;DR, context, users, flows, costs, and risks. A developer or coding agent reads the rest. Use plain words first and define each term once in the glossary.
- Diagrams are Mermaid in fenced blocks (they render on GitHub and most editors): `flowchart` for user flows and architecture, `erDiagram` for the schema, `sequenceDiagram` for auth, payments, and webhooks, `stateDiagram-v2` for lifecycles. Add an ASCII wireframe for each key screen.
- Tables for anything comparable (decisions, schema, endpoints, costs, risks). Prose for reasoning.
- Every figure with a source gets a "checked on YYYY-MM-DD" date. Every estimate is labeled as an estimate.
- No placeholders. If something is unknown, write it as an open question with an owner and a decision date.
- Stable IDs for cross-reference: goals G-1, features F-001, screens S-01, tables as their names, endpoints E-01, risks R-1, open questions OQ-1, decisions D-01. Roadmap tickets cite feature IDs.
- Sentence case headings, one title, no emoji, no horizontal rules, no dashes (see writing-style.md).
- Depth follows the project. A one-screen utility does not need ten personas. Keep every section, but let a small project answer a section in a paragraph.

## Section order

0. Title block
1. TL;DR
2. Context and problem
3. Users
4. Goals, metrics, and non-goals
5. Scope and release plan
6. Features and requirements
7. User flows and information architecture
8. Design system
9. Architecture and tech stack
10. Data model
11. Backend and API
12. Infrastructure and environments
13. Security, privacy, and compliance
14. Testing and quality
15. Development workflow
16. Deployment and shipping plan
17. Analytics, growth, and monetization
18. Roadmap and milestones
19. Costs
20. Risks, open questions, and decisions
21. Appendices

## Section guidance

### 0. Title block
Name, one-line description, version, date, status (draft, in review, approved), owner, project type or types, delivery method, target launch window. If the project name is not decided, propose three names with a note on availability checks (domain, store, trademark search), and use the first as the working name.

### 1. TL;DR
Must fit on one screen. Contents: what it is and who it is for (two sentences), the problem in one sentence, MVP scope in five bullets or fewer, stack in one line (free path and ideal path), cost to launch and monthly running cost on both paths, timeline, the three biggest risks, design direction in one line, and the assumptions table from intake. An owner who reads only this section should know whether to proceed.

### 2. Context and problem
- Background: the situation and why now.
- Problem statements: each one names who is affected, what happens today, and the cost of the problem (time, money, frustration). Use evidence found in research and cite it with dates. If no evidence was found, say so and mark the claim as an assumption to validate.
- Alternatives today: a table of 3 to 6 competitors or workarounds with what they do, price, strengths, and the gap this project fills. Use only what research found.
- Opportunity and vision: what changes for the user when this exists.

### 3. Users
Two or three personas at most. Each has context, goals, frustrations, tech comfort, devices, and accessibility needs. Add the main jobs to be done and the first-run scenario. For B2B, include buyer versus user.

### 4. Goals, metrics, and non-goals
Goals G-1 and so on, each with a metric, a target, a measurement method, and a time frame. Add guardrail metrics (error rate, load time, support volume). Non-goals list what the project will not do and why, which protects scope.

### 5. Scope and release plan
MoSCoW table (must, should, could, won't for now) tied to feature IDs. MVP definition in a sentence. Release plan by phase. Constraints (budget, time, skills, legal, platform), assumptions, and dependencies on third parties.

### 6. Features and requirements
For each feature: ID, name, priority, user story, acceptance criteria in Given-When-Then form, edge cases, empty and error states, analytics events fired, permissions needed, and effort (S, M, L). Group by surface. Include non-functional requirements as a table: performance targets, availability target, browser or device support, accessibility level, localization, privacy and data retention limits.

### 7. User flows and information architecture
Sitemap or screen inventory with IDs. A Mermaid flow for each core journey (first run, signup and login, the main task, payment, account deletion, consent banner). State coverage per screen: loading, empty, error, offline, success. UX writing guidance: voice, terminology list, error-message pattern (what happened, how to fix it). ASCII wireframes for the key screens.

### 8. Design system
Owned by the frizzy-design skill. Its section guide holds the full guidance, and the lean contract is in the section table of `SKILL.md`.

### 9. Architecture and tech stack
Owned by the frizzy-stack skill. Its section guide holds the full guidance, and the lean contract is in the section table of `SKILL.md`.

### 10. Data model
Owned by the frizzy-stack skill. Its section guide holds the full guidance, and the lean contract is in the section table of `SKILL.md`.

### 11. Backend and API
Owned by the frizzy-stack skill. Its section guide holds the full guidance, and the lean contract is in the section table of `SKILL.md`.

### 12. Infrastructure and environments
Owned by the frizzy-ship skill. Its section guide holds the full guidance, and the lean contract is in the section table of `SKILL.md`.

### 13. Security, privacy, and compliance
Owned by the frizzy-security skill. Its section guide holds the full guidance, and the lean contract is in the section table of `SKILL.md`.

### 14. Testing and quality
Owned by the frizzy-test skill. Its section guide holds the full guidance, and the lean contract is in the section table of `SKILL.md`.

### 15. Development workflow
Owned by the frizzy-ship skill. Its section guide holds the full guidance, and the lean contract is in the section table of `SKILL.md`.

### 16. Deployment and shipping plan
Owned by the frizzy-ship skill. Its section guide holds the full guidance, and the lean contract is in the section table of `SKILL.md`.

### 17. Analytics, growth, and monetization
Event taxonomy (name, trigger, properties, consent class), funnels, dashboards, privacy treatment of analytics. SEO plan for web (metadata, sitemap, structured data, Open Graph, performance), app store optimization for mobile, and a lightweight launch plan (channels, assets, timing). Pricing model, plans, free tier limits, payment flow, tax handling, and refund policy.

### 18. Roadmap and milestones
Phases with exit criteria. Each milestone lists tickets as checkboxes, each ticket small enough for one working session and citing feature IDs, with an effort estimate. Mark the critical path and the first vertical slice. Include dates relative to the start (week 1, week 2) so the plan survives a late start. Games use milestones named first playable, vertical slice, alpha, beta, gold.

### 19. Costs
Owned by the frizzy-stack skill. Its section guide holds the full guidance, and the lean contract is in the section table of `SKILL.md`.

### 20. Risks, open questions, and decisions
Risk table: ID, description, likelihood, impact, mitigation, owner, trigger. Open questions with owner and decision date. A decision log with date, decision, reason, and the cost of changing it later.

### 21. Appendices
A. Glossary. B. Policy fact sheet and data map. C. Research notes and sources, with URL and date checked for each source. D. Environment variables. E. Agent instructions. F. Full endpoint or schema listings if they would bloat the main sections. G. Changelog of this document.

## Swaps by project type

| Type | Replace or add |
|---|---|
| Game | Replace sections 6, 10, 11 with a game design section (pillars, core loop, mechanics, progression, economy, content plan, controls, UI and HUD, art and audio direction, tech notes). Keep a save-data model. Add playtest plans, platform certification, and live operations. |
| Mobile | Add navigation map, offline and sync, push plan, permissions rationale, deep links, device matrix, store listing, in-app purchase flows. |
| Extension | Replace section 11 with manifest, permission table, content-script surfaces, messaging, storage, and store listing and privacy form content. |
| CLI or library | Replace sections 7 and 8 with command reference or public API surface, output formats, and docs plan. Keep security and shipping. |
| API product | Expand section 11 with contract-first workflow, SLOs, developer portal, SDKs, and deprecation policy. |
| AI feature | Add model selection, prompt versioning, evaluation plan, cost caps, guardrails, and provider data terms to sections 9, 11, and 13. |
| Combined | Keep one PRD. Put shared parts first, then a subsection per surface in sections 6, 7, 14, and 16. |

## Skeleton to copy

```markdown
# <Project name>

<One-line description>

| Field | Value |
|---|---|
| Version | 0.1 |
| Date | YYYY-MM-DD |
| Status | Draft |
| Owner | <name> |
| Type | <web app, mobile app, game, ...> |
| Delivery method | <Kanban, Scrum, GDLC, ...> |

## Contents

## TL;DR

## Context and problem

## Users

## Goals, metrics, and non-goals

## Scope and release plan

## Features and requirements

## User flows and information architecture

## Design system

## Architecture and tech stack

## Data model

## Backend and API

## Infrastructure and environments

## Security, privacy, and compliance

## Testing and quality

## Development workflow

## Deployment and shipping plan

## Analytics, growth, and monetization

## Roadmap and milestones

## Costs

## Risks, open questions, and decisions

## Appendices
```
