---
name: project-frizzy
description: Plans any software project into a complete PRD.md, lean by default. Covers web, SaaS, mobile, desktop, CLI, extensions, games, APIs, bots, and AI features, and coordinates the design, stack, security, test, and ship skills. Use for /project-frizzy, or any ask to plan, scope, spec, or kick off a product, or for a PRD, roadmap, or product spec, even if they never say PRD.
---

# project-frizzy

Turns a project idea into one `PRD.md` that an owner can read and a developer or coding agent can build from. Researched, costed with free options first, secure by default, written in plain language.

Invoked as `/project-frizzy` plus an idea, or by describing something to build.

## The skill suite

This skill owns the PRD itself and the sections about the product. Five field skills own the specialist sections. Each also works alone when someone asks only for its field.

| Skill | Owns sections | Standalone file |
|---|---|---|
| project-frizzy (this skill) | 0 to 7, 17, 18, 20, 21, plus intake, lifecycle, linting | `PRD.md` |
| frizzy-design | 8 | `DESIGN.md` |
| frizzy-stack | 9, 10, 11, 19 | `STACK.md` |
| frizzy-security | 13 | `SECURITY.md` |
| frizzy-test | 14 | `TEST-PLAN.md` |
| frizzy-ship | 12, 15, 16 | `SHIP.md` |

Run `bash scripts/find_suite.sh` once to see which siblings are installed. For each owner the project needs, read only that owner's `SKILL.md` (all needed ones in one call) and apply its workflow, section contract, and handoffs. Skip owners the project does not need (a CLI tool has no design section). This skill stays the single writer of `PRD.md`, so the document has one voice and the build takes the same few tool calls. If a sibling is missing, write its sections from the lean contract in the table below and tell the person which skill to install for more depth.

## Modes

| Mode | When | PRD length | Searches | Tool calls |
|---|---|---|---|---|
| Lean (default) | Always, unless the person asks otherwise | 350 to 600 lines | 4 to 8, standard mode | About 12 to 16 |
| Full | The person says "full", "detailed", "thorough", or "enterprise" | 1,000 to 1,800 lines | 10 to 25 | 40 or more |

For full mode, read `references/full-mode.md` and follow it. Everything else in this file is lean mode. Lean cuts depth, never coverage: every section still exists, every safety item still appears, and any section can be expanded later ("expand section 13") without rewriting the rest.

## Principles

- Decide, don't survey. One pick per decision with a reason. Two columns only for money and taste: the free or cheapest pick beside the ideal pick, with its price and the trigger to switch.
- Free first, ideal alongside. The plan works at zero cost, and the ideal column prevents building into a corner.
- Dated facts. Prices, limits, store rules, and laws change, so every figure carries "checked YYYY-MM-DD". Each field skill keeps its own dated facts with reuse rules.
- The design is a swappable layer (tokens, a direction statement, a component list). A new reference changes only the design section.
- Two readers: the owner (TL;DR, problem, flows, costs, risks) and the developer (the rest). Plain words first.
- Honest limits. No invented statistics, quotes, or competitor facts. Legal documents are plans and fact sheets, never full text, and need a lawyer's review.
- The PRD never names this skill suite's own scripts, files, or references. Its reader does not have them.

## Lean workflow

### 1. Read the brief and ask only if blocked

Classify the primary type and any secondary types (web, mobile, desktop, CLI or library, extension, game, API, bot, AI feature, embedded). Ask only when a missing answer changes the plan's shape (unclear idea, ambiguous platform, regulated domain with unknown region, existing codebase): one batch of at most three questions, each with a recommended default first, via `ask_user_input_v0` when available, otherwise a numbered list where "go" accepts all defaults. If the person says "just decide" or gives enough, ask nothing.

Everything else becomes an assumption: show an assumptions table in the TL;DR (assumption, why, how to change it). Defaults: free or cheapest first; global audience with a GDPR-grade baseline plus the person's country if known; one developer with an AI coding agent; MVP in 6 to 10 weeks of part-time work; no payments in the MVP. When the genre or concept is left open, choose the smallest replayable or useful scope, say so in the TL;DR, and log it as a high-cost-to-change assumption with an open question.

Design is never a blocker. Invite a reference in one line: "Send screenshots, links, or a few words about the look and I will rebuild the design section around it. Otherwise I choose and say what I chose."

### 2. Environment check (only when it helps)

Skip it in the claude.ai container (`/mnt/user-data` exists) and for projects with no browser surface; then write "not checked in the planning environment" wherever the PRD mentions installed tools. Otherwise run `bash scripts/check_env.sh` once and follow the frizzy-test rules for playwright-cli (ask before installing, never without a yes).

### 3. Gather, then research

Call A: read only what you need from this skill, for example
`python3 scripts/section.py references/project-types.md::"Browser and editor" references/intake.md::"Reading shorthand"`.
Use `--list <file>` to see headings. Then run `scripts/find_suite.sh` and read the owners' `SKILL.md` files in one call.

Call B onward: web search in standard mode, one search per need, 4 to 8 in total, stopping at the budget:

1. Competitors and alternatives (1 search, this skill). Never skip. Include an honest note on how crowded the space is.
2. Prices and free-tier limits of the two or three services in the free pick (frizzy-stack, 1 search each, skipping rows checked within 14 days).
3. Store, platform, and regional law not already in the owners' facts within 60 days (frizzy-security and frizzy-ship).
4. Design: only if the person gave references to look up (frizzy-design).

Skip `web_fetch` unless a search result is unusable. Unverified items go in a "not verified" line, never guessed. Use the real current date from the conversation.

### 4. Decide, then write the PRD once

Decide in this order: delivery method, architecture, stack (free and ideal), data model, security and compliance baseline, design direction, test plan, ship plan. The owners' workflows say how.

Write `PRD.md` in two or three calls (create the file with sections 1 to 10, append sections 11 to 21, a third call only if needed). Write each section once in final form. Do not read the file back; the linter output is the check.

Section list and body caps (lines, tables count per row). Keep these exact headings so the linter and the owner can navigate:

| # | Section | Cap | Lean content | Owner |
|---|---|---|---|---|
| 0 | Title block and contents | 15 | Name, version, date, type, method, target launch, working name | this skill |
| 1 | TL;DR | 25 | What and for whom, free and ideal path table, MVP in five bullets, design direction, top three risks, assumptions table | this skill |
| 2 | Context and problem | 25 | Problem table with evidence, competitor table of 4 to 6 rows, differentiation in two sentences | this skill |
| 3 | Users | 10 | Two personas in two sentences each, jobs to be done in five lines | this skill |
| 4 | Goals, metrics, and non-goals | 12 | Table of 4 to 6 goals with target and measure, five non-goals | this skill |
| 5 | Scope and release plan | 15 | MoSCoW table, MVP in one sentence, phases with exit criteria | this skill |
| 6 | Features and requirements | 40 | One table: ID, feature, priority, effort, acceptance criteria in one line. Games and others swap this for a design section. | this skill |
| 7 | User flows and information architecture | 30 | Screen list, one Mermaid flow, states table, one ASCII wireframe | this skill with frizzy-design |
| 8 | Design system | 50 | Design read, base and flavor, tokens table with real values and contrast ratios plus a short CSS block, type, icons, 6-row motion map with reduced-motion fallback, component list, accessibility line, swap protocol in five lines | frizzy-design |
| 9 | Architecture and tech stack | 30 | Decision table (decision, free pick, ideal pick with price, switch trigger and reason), one diagram in a code block or Mermaid, repo tree | frizzy-stack |
| 10 | Data model | 35 | Tables with columns on one line each, authorization rules, retention, one ER diagram only if 4 or more tables | frizzy-stack |
| 11 | Backend and API | 30 | Endpoint table with auth and limits, one example request, error model, jobs | frizzy-stack |
| 12 | Infrastructure and environments | 20 | Environment table, backups with recovery point and time, observability, alert thresholds | frizzy-ship |
| 13 | Security, privacy, and compliance | 50 | Standards with edition years, OWASP mapping table limited to rows that apply (others get one line saying why not), threat table of 5 to 8 rows, data map, legal documents plan with heading outlines only, consent design, regional table, store policy checklist, incident line, and a planned pre-launch code security audit | frizzy-security |
| 14 | Testing and quality | 20 | Layer table with tools and targets (including a code security audit row), key end-to-end flows, beta plan, definition of done, playwright-cli note | frizzy-test |
| 15 | Development workflow | 25 | Method, setup commands, a build kit of up to four tools, environment variable table, agent instructions in 8 bullets or fewer | frizzy-ship |
| 16 | Deployment and shipping plan | 25 | Pipeline, rollback, launch checklist (with the audit item), first 72 hours, store steps if any | frizzy-ship |
| 17 | Analytics, growth, and monetization | 10 | Measurement approach, launch plan, monetization options | this skill |
| 18 | Roadmap and milestones | 35 | 5 to 7 milestones with dates, 4 to 6 checkbox tickets each citing feature IDs, with an audit ticket before the beta and another on the release candidate | this skill |
| 19 | Costs | 25 | One-time table and one monthly table showing free and ideal at launch, growth, and scale, upgrade triggers | frizzy-stack |
| 20 | Risks, open questions, and decisions | 30 | Risk table, open questions with owners and dates, short decision log | this skill |
| 21 | Appendices | 25 | Policy fact sheet (from frizzy-security), sources with dates, "not verified" line, changelog. Glossary only if jargon needs it. | this skill |

Never cut, even in lean mode: security standard names with editions, the legal documents plan and consent design, dated free and ideal costs, rollback, risks with mitigations, real token values, named test tools, and checkable roadmap tickets.

Writing rules: one title, sentence case headings, no emoji or horizontal rules, no em or en dashes (write ranges with "to"), no bold labels on list items, no "not just X but Y", no staged openers, and none of crucial, pivotal, seamless, leverage, robust, vibrant, showcase, delve, cutting-edge, holistic, empower. Name specifics, decision before reasoning, straight quotes. No placeholders: unknowns become open questions with an owner and a date. No full text of any privacy policy, terms, or cookie policy. Full style list: `references/writing-style.md`.

Type notes: games use a game design section instead of features, a save-data model instead of a database, and must check national age-rating rules; extensions include the manifest as JSON and a permission table; AI features follow the order built-in model, bring-your-own-key, free tier after reading data terms, paid hosted tier, and record rejected options; combined projects keep one PRD with a shared core and a subsection per surface.

### 5. Lint once, fix once

Run `python3 scripts/lint_prd.py PRD.md --lean --profile <type>` (one `--profile` per project type: web, mobile, desktop, extension, game, api, cli, ai, bot). Fix every error and any warning that points at a real problem in one pass, then re-run once. Without re-reading the file, check that numbers agree across the title block, TL;DR, scope, roadmap, and costs, and for an extension that the manifest permissions equal the permission table.

### 6. Deliver

Save the file as `PRD.md` (repo root, or `docs/` if it exists; in claude.ai write to `/mnt/user-data/outputs/PRD.md` and call `present_files`). Do not publish it as a page. Reply in a few lines: what it covers, the headline picks (stack, cost to launch, timeline), assumptions to confirm, open questions, and the offer to send a design reference or expand any section. Do not paste the PRD into the chat.

## After delivery

Route each change to the owner of the section it touches, then bump the version and add a changelog line:

- New design reference or words: frizzy-design (section 8, section 7 notes).
- Stack change: frizzy-stack, then search the file for old names; frizzy-ship and frizzy-test update hosting, pipeline, and test rows.
- Scope change: this skill (features, roadmap, risks) and frizzy-stack (costs).
- "Expand section N" or "full mode": add depth to that section from its owner's section guide, without rewriting the rest.
- Starting the build: follow the roadmap one milestone at a time as frizzy-ship describes, and keep the PRD current.

## Reference map

| File | Use |
|---|---|
| `references/project-types.md` | Lifecycle and exit criteria per type, delivery method, combined projects |
| `references/intake.md` | Question rules and shorthand, for unusual briefs |
| `references/prd-template.md` | Section guidance for the sections this skill owns, swaps by type, skeleton |
| `references/writing-style.md` | Detailed writing rules, used in full mode or to fix stubborn warnings |
| `references/full-mode.md` | The detailed workflow for full mode |
| `scripts/section.py` | Print only the sections you need from any reference |
| `scripts/lint_prd.py` | Linter, with `--lean` for lean PRDs |
| `scripts/check_env.sh` | Environment check |
| `scripts/find_suite.sh` | Locate the sibling field skills |
