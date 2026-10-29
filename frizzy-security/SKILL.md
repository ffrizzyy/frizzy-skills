---
name: frizzy-security
description: Security, privacy, and compliance planning for any software project. Named standards with edition years (OWASP Top 10, ASVS, API Security, MASVS, LLM Top 10), an OWASP-to-controls mapping, threat model, data map, plans for the privacy policy, terms of service, cookie policy and consent banner, regional law (GDPR, US states, Indonesia UU PDP, and more), app store and age-rating rules, payment handling, incident response, and a planned pre-launch code security audit. Use this whenever the user asks about app security, a threat model, OWASP, GDPR or privacy law, a privacy policy or terms plan, cookie consent, store privacy forms, age ratings, PCI or payments compliance, or section 13 of a project-frizzy PRD, even if they only say "make it secure" or "is this legal". Produces plans and fact sheets, never full legal text.
---

# frizzy-security

Owns PRD section 13 (security, privacy, and compliance) and supplies the policy fact sheet for the appendix. Output is a plan and fact sheets. It is never the full text of a privacy policy, terms of service, or cookie policy, and it is not legal advice: say so, and say that a qualified lawyer reviews every policy before launch.

## Two ways to run

- Called by project-frizzy: take the handoff (project type, data kinds, audience including children, regions, services in the stack, payments yes or no), write section 13 at lean depth, and return it with the pieces other sections need (see handoffs).
- Standalone: the person asks for a threat model, a compliance checklist, a policy plan, or a review of an existing plan. Write `SECURITY.md` with the same headings, or answer inline. For regulated domains (health, finance, children, identity documents), ask for region and kind of data first, in one batch of at most two questions with a recommended default.

## Workflow

1. Flag the stakes: children, health, payments handled directly, identity documents, user content, AI-generated content, regulated industry. A flag expands section 13 only.
2. Read only what you need in one call, for example
   `python3 scripts/section.py references/security-compliance.md::"Baseline" references/security-compliance.md::"OWASP mapping" references/security-compliance.md::"Legal documents" references/security-by-type.md::"Games"`.
3. Check `references/facts.md` for standards and regions. Stable rows are reusable for 60 days after the checked date and the PRD cites that date. Search (standard mode) only for a region or store not listed there, or a row older than 60 days. Unverified items go in a "not verified" line.
4. Write the section once in final form. Write the edition year of every standard. Default to a GDPR-grade baseline plus the person's country when the region is unknown, and tell the owner which regions to confirm.

## Section contract

| # | Section | Cap | Lean content |
|---|---|---|---|
| 13 | Security, privacy, and compliance | 50 | Standards with edition years, OWASP mapping table limited to rows that apply (others get one line saying why not), threat table of 5 to 8 rows, data map, legal documents plan with heading outlines only, consent design, regional table, store policy checklist, incident line, and a planned pre-launch code security audit |

Never cut: standard names with editions, the legal documents plan and consent design, the data map, the OWASP mapping, the incident line, and the audit plan. If a high-stakes flag applies, expand with `python3 scripts/section.py references/security-compliance.md "<heading>"`.

## Pre-launch code security audit

Nothing runs during planning because there is no code yet. Recommend Cloudflare's open-source `security-audit` skill. Read the plan with `python3 scripts/section.py references/security-compliance.md "Pre-launch code security audit"`. Record in section 13 when, how, requirements, triage rule, likely attack classes, and that it is budgeted as agent usage. Never install it unasked. The plan must also appear as a roadmap ticket (before the beta and on the release candidate), a testing row, and a launch checklist item.

## Handoffs to sibling skills

- To project-frizzy: the policy fact sheet and data map for the appendix, the top security and privacy risks for the risk table, and the roadmap audit tickets.
- To frizzy-design: consent banner states and the account deletion and data export screens.
- To frizzy-test: the security test rows (SAST, dependency and secret scanning, authorization matrix tests, the audit).
- To frizzy-ship: the secret handling rules, header baseline, backup and recovery numbers, and the launch checklist items (legal pages live, consent working).
- From frizzy-stack: the third-party services and the data each one receives.

Writing rules for any text this skill produces for a PRD: sentence case headings, no emoji, no horizontal rules, no em or en dashes (write ranges with "to"), no bold labels on list items, no "not just X but Y" or "it is not X, it is Y", no staged openers or one-line closers, none of crucial, pivotal, seamless, leverage, robust, vibrant, showcase, delve, cutting-edge, holistic, empower. Name specifics instead of adjectives, decision before reasoning, straight quotes. No placeholders: unknowns become open questions with an owner and a date.

## Reference map

| File | Use |
|---|---|
| `references/security-compliance.md` | Baseline controls, standards by type, OWASP mapping, legal documents, consent, data map, regions, store policies, payments, audit plan, incident response |
| `references/security-by-type.md` | Per-type security standards, policy checkpoints, age classification |
| `references/section-guide.md` | Full-mode guidance for section 13 |
| `references/facts.md` | Dated facts on standards, regions, and the audit skill |
| `scripts/section.py` | Print only the headings you need |
