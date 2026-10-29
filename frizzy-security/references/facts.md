# Verified facts (reuse rules inside)

Every row carries its checked date; cite that date in the PRD, never today's. Stable rows (standards, fees, rules) are reusable for 60 days. Volatile rows (prices, limits) are re-verified by search unless checked within 14 days. Unverified rows get searched or labeled unverified. Source names feed the research appendix; paraphrase, never quote.

## Standards (stable)

| Topic | Fact | Checked | Source |
|---|---|---|---|
| OWASP Top 10 | 2025 edition is current (announced November 2025, final January 2026). Replaced the 2021 list. New categories: software supply chain failures, mishandling of exceptional conditions. Names as used in earlier PRDs: A01 Broken access control, A02 Security misconfiguration, A03 Software supply chain failures, A04 Cryptographic failures, A05 Injection, A06 Insecure design, A07 Authentication failures, A08 Software or data integrity failures, A09 Security logging and alerting failures, A10 Mishandling of exceptional conditions. Only the two new categories were confirmed by the sources; the rest is from memory, so confirm order if it matters. | 2026-10-24 | theregister.com, parasoft.com, qualys.com |
| OWASP LLM Top 10 | 2025 edition is current. LLM01 Prompt injection, LLM02 Sensitive information disclosure, LLM03 Supply chain, LLM04 Data and model poisoning, LLM05 Improper output handling, LLM06 Excessive agency, LLM07 System prompt leakage, LLM08 Vector and embedding weaknesses, LLM09 Misinformation, LLM10 Unbounded consumption | 2026-10-24 | aigl.blog, bdemerson.com, qualys.com |
| OWASP others | API Security Top 10 is the 2023 edition. MASVS and MASTG for mobile. ASVS current version unverified. | 2026-10-24 | Unverified, search if the version matters |

## Regions (moving fast, re-check within 60 days)

| Topic | Fact | Checked | Source |
|---|---|---|---|
| Indonesia, data protection | UU PDP (Law No. 27 of 2022) in force after a two-year transition. Government Regulation 33 of 2026 promulgated 16 July 2026, with first priorities before 16 January 2027. Explicit consent; consent bundled with general terms may be treated as ambiguous. Breach notice within 3 x 24 hours per the PP 33/2026 alert (one explainer says 14 days, use the stricter). Data protection authority not yet set up when PwC published. | 2026-10-24 | rsm.global, pwc.com/id, kaamel.com, conventuslaw.com, xpnd.co.id |
| Indonesia, operator registration | Private electronic system operators must register (Regulation 5 of 2020, Articles 2 and 4). The ministry issued warnings between June and September 2026 and named access blocking as a sanction. Guide: s.komdigi.go.id/pendaftaranpseprivat. Whether a given small project meets the criteria is unverified. | 2026-10-24 | jawapos.com, bisnis.com, selular.id, rri.co.id |
| Indonesia, games | IGRS age classification is mandatory for games distributed in Indonesia from January 2026. Categories 3+, 7+, 13+, 15+, 18+, RC. Developers self-assess and the ministry checks. Wrong ratings can lead to take-down. In April 2026 the ministry said Steam's IGRS labels were not official and began an investigation. Fees unverified. | 2026-10-24 | detik.com, bisnis.com, selular.id, goodnewsfromindonesia.id |
| Other regions | EU and UK GDPR baseline, US state laws and COPPA, Singapore PDPA, Brazil LGPD, India DPDP Act 2023: names only, details unverified. | Not checked | Search if targeted |

## Tools and libraries

| Topic | Fact | Checked | Source |
|---|---|---|---|
| Cloudflare security-audit skill | MIT. A coding-agent skill that audits an existing codebase in six phases using isolated agents: reconnaissance, coverage-led hunting, candidate validation, structured output (`findings.json` with verdicts confirmed, needs_validation, rejected), independent record verification, and reporting. Needs an agent that supports tool use and parallel sub-agents, Node.js for its validators, and an OS-enforced sandbox before it runs any target code (otherwise it keeps the lead as needs_validation). Install: `npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit` (add `--global` for a user-level install). Trigger by asking "security audit this codebase". Default output: `~/security-audit-skill/<repo-name>/run-<N>`. Repeated runs are additive, and the authors report a single run found about half of what repeated runs found. It is multi-agent, so budget real agent usage. | 2026-10-25 | github.com/cloudflare/security-audit-skill |
