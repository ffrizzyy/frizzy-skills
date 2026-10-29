---
name: frizzy-stack
description: Tech stack, architecture, data model, API, and cost planning for any software project, free first with the ideal option beside it. Decision records with prices, free-tier limits and the trigger to upgrade, starting stacks per project type, database schema with authorization rules, endpoint tables, and one-time, monthly, and scale cost tables. Use this whenever the user asks which tech stack, framework, database, auth, hosting or services to use, how much a project will cost to run, for a database schema, an API design, free-tier limits or alternatives, "what should I build this with", or sections 9, 10, 11, and 19 of a project-frizzy PRD, even if they never say "stack".
---

# frizzy-stack

Owns PRD sections 9 (architecture and tech stack), 10 (data model), 11 (backend and API), and 19 (costs). The plan works at zero cost, and the ideal column keeps the owner from building into a corner.

## Two ways to run

- Called by project-frizzy: take the handoff (project type, scale hints, team, region, budget stance, assumptions), write sections 9, 10, 11, and 19, and return them with a three-number headline for the TL;DR (cost to launch, monthly cost on the cheapest path, monthly cost on the ideal path).
- Standalone: the person asks for a stack, a schema, an API, or a cost estimate. Write `STACK.md` with the same headings, or answer inline for a small ask. Ask only when the platform is ambiguous ("an app": web, mobile, or both).

## Principles

- Decide, do not survey. One pick per decision with a reason. Two columns only for money and taste: the free or cheapest pick beside the ideal pick, with its price and the switch trigger.
- Boring, widely used, documented tools beat clever ones. Fewer moving parts. Avoid lock-in where it is cheap to avoid.
- Every figure carries "checked YYYY-MM-DD". Unverified items go in a "not verified" line, never guessed.
- A stack the owner cannot debug costs more than a paid one.

## Workflow

1. Read what you need in one call:
   `python3 scripts/section.py references/stack-and-costs.md::"Candidate services" references/stack-and-costs.md::"Starting stacks" references/stack-and-costs.md::"Free-tier traps" references/stack-by-type.md::"Mobile apps"`.
2. Decide in this order: architecture shape, stack (free and ideal), data model, API surface, then costs.
3. Research prices and limits of the two or three services in the free pick, one standard-mode search each. Skip any service whose row in `references/facts.md` was checked within 14 days. Stable rows may be reused for 60 days after their checked date. Volatile rows (prices, limits) are re-verified when the service is chosen.
4. Write each decision as a record (pick, ideal, reason, switch trigger, migration effort, rejected options) and keep the full records short in lean mode.
5. Compute costs with the math visible (for AI features: tokens per request times requests per user per month).

## Section contract

| # | Section | Cap | Lean content |
|---|---|---|---|
| 9 | Architecture and tech stack | 30 | Decision table (decision, free pick, ideal pick with price, switch trigger and reason), one diagram in a code block or Mermaid, repo tree |
| 10 | Data model | 35 | Tables with columns on one line each, authorization rules, retention, one ER diagram only if 4 or more tables |
| 11 | Backend and API | 30 | Endpoint table with auth and limits, one example request, error model, jobs |
| 19 | Costs | 25 | One-time table and one monthly table showing free and ideal at launch, growth, and scale, upgrade triggers |

Never cut dated free and ideal costs, the switch triggers, or the authorization rules on the data model.

Type notes: games use a save-data model instead of a database and drop the API section unless there is a backend; extensions replace section 11 with the manifest as JSON and a permission table (permission, why needed, what breaks without it); CLI tools replace it with the command reference; AI features follow the order built-in model, bring-your-own-key, free tier after reading data terms, paid hosted tier, and record rejected options with the reason; combined projects share one backend contract and one auth system.

## Handoffs to sibling skills

- To frizzy-security: the third-party service list with the data each one receives, and the data classes per table, so the data map and policy fact sheet are accurate.
- To frizzy-ship: environments, hosting choice, and the environment variable names.
- To frizzy-test: the authorization matrix and the endpoint list for contract and permission tests.
- To project-frizzy: the cost headline numbers and any open questions with an owner and a date.

Writing rules for any text this skill produces for a PRD: sentence case headings, no emoji, no horizontal rules, no em or en dashes (write ranges with "to"), no bold labels on list items, no "not just X but Y" or "it is not X, it is Y", no staged openers or one-line closers, none of crucial, pivotal, seamless, leverage, robust, vibrant, showcase, delve, cutting-edge, holistic, empower. Name specifics instead of adjectives, decision before reasoning, straight quotes. No placeholders: unknowns become open questions with an owner and a date.

## Reference map

| File | Use |
|---|---|
| `references/stack-and-costs.md` | Principles, decision record, candidate services, starting stacks, price verification, free-tier traps, cost tables, guardrails |
| `references/stack-by-type.md` | Mobile path, game engine, AI model order, web export notes |
| `references/section-guide.md` | Full-mode guidance for sections 9, 10, 11, and 19 |
| `references/facts.md` | Dated prices, limits, and library facts |
| `scripts/section.py` | Print only the headings you need |
