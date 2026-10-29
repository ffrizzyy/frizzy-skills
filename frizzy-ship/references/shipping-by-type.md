# Shipping, fees, and hosting watch-outs by project type

Fees and store rules change. Confirm each figure by search and write the date.

## Web apps, SaaS, and websites

Shipping: Git-based deploys with preview URLs, staging that mirrors production, database migrations run by CI, and a one-step rollback.

Watch for: free hosting plans that forbid commercial use, cold starts, bandwidth overage, database projects that pause when idle, and email deliverability (SPF, DKIM, DMARC) on the first day.

## Mobile apps

Fees to confirm: Apple Developer Program is a yearly fee; Google Play is a one-time fee.

## Desktop software, CLI tools, and libraries

Shipping: GitHub Releases or package registries; release automation with changesets or release-please; checksums and signatures published with each artifact.

## Browser and editor extensions

Fees to confirm: Chrome Web Store charges a small one-time developer fee; Firefox and Edge add-on programs are free at the time of writing.

## Games

Shipping: itch.io for the cheapest first release, Steam (per-title fee, confirm the amount), mobile stores, web builds on your own domain. Plan the store page and wishlist campaign months ahead of launch.

## APIs and backend services

Shipping: blue-green or canary deploys, database migrations that stay backward compatible for one release, and a deprecation policy with dated notices.
