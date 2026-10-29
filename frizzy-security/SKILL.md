---
name: frizzy-security
description: Security, privacy, and compliance planning for any project: named standards with editions, OWASP mapping, threat model, data map, plans for the privacy policy, terms, cookies and consent, regional law, store rules, payments, incident response, and a pre-launch code audit. Use for security, threat modeling, GDPR, privacy, consent, age ratings, or section 13, even if they only say make it secure. Plans only, never legal text.
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
3. Check `references/facts.md` for standards and regions (reuse rules at the top). Search only for a region, store, or row it does not cover. Unverified items go in a "not verified" line.
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

Writing rules: one title, sentence case headings, no emoji or horizontal rules, no em or en dashes (write ranges with "to"), no bold labels on list items, no "not just X but Y", no staged openers, and none of crucial, pivotal, seamless, leverage, robust, vibrant, showcase, delve, cutting-edge, holistic, empower. Name specifics, decision before reasoning, straight quotes. No placeholders: unknowns become open questions with an owner and a date.

## Reference map

| File | Use |
|---|---|
| `references/security-compliance.md` | Baseline controls, standards by type, OWASP mapping, legal documents, consent, data map, regions, store policies, payments, audit plan, incident response |
| `references/security-by-type.md` | Per-type security standards, policy checkpoints, age classification |
| `references/section-guide.md` | Full-mode guidance for section 13 |
| `references/facts.md` | Dated facts on standards, regions, and the audit skill |
| `scripts/section.py` | Print only the headings you need |
