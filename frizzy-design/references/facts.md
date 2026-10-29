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
| GSAP | Free for commercial use including formerly paid plugins, with a restriction for products that let end users build animations visually | 2026-10-24 | gsap.com license |
| React Bits | MIT with the Commons Clause: fine inside a product, not for resale | 2026-10-24 | github.com/DavidHDev/react-bits |
| Emil Kowalski skills | Install `npx skills@latest add emilkowalski/skills`. Strong on animation and interaction craft. | 2026-10-24 | github.com/emilkowalski/skills |
| Taste skill | Install `npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"`. Aimed at landing pages, portfolios, and redesigns, not dashboards. | 2026-10-24 | github.com/Leonxlnx/taste-skill |
