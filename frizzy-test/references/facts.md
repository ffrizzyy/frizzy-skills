# Verified facts (reuse rules inside)

Purpose: lean mode skips searches for facts verified recently. Every row has the date it was checked, which is the date to write in the PRD ("checked 2026-10-24"), never today's date.

Reuse rules
- Stable rows (standards, fees, rules) may be reused for 60 days after the checked date without searching. After that, re-verify with one search and update this file.
- Volatile rows (prices, free-tier limits) must be re-verified by search whenever the service is actually chosen for the PRD, unless it was checked within the last 14 days.
- Rows marked "unverified" must be searched or labeled as unverified in the PRD.
- A project that touches a region, store, or tool not listed here needs its own search.
- Source names are for the PRD's research appendix. Paraphrase, never quote.

## Tools and libraries

| Topic | Fact | Checked | Source |
|---|---|---|---|
| playwright-cli | `npm install -g @playwright/cli@latest`, then `playwright-cli install --skills`. Node 18 or newer. Run `playwright-cli --help` for commands. | 2026-10-24 | github.com/microsoft/playwright-cli |
