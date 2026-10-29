# Verified facts (reuse rules inside)

Purpose: lean mode skips searches for facts verified recently. Every row has the date it was checked, which is the date to write in the PRD ("checked 2026-10-24"), never today's date.

Reuse rules
- Stable rows (standards, fees, rules) may be reused for 60 days after the checked date without searching. After that, re-verify with one search and update this file.
- Volatile rows (prices, free-tier limits) must be re-verified by search whenever the service is actually chosen for the PRD, unless it was checked within the last 14 days.
- Rows marked "unverified" must be searched or labeled as unverified in the PRD.
- A project that touches a region, store, or tool not listed here needs its own search.
- Source names are for the PRD's research appendix. Paraphrase, never quote.

## Stores and platforms (stable, except where marked)

| Topic | Fact | Checked | Source |
|---|---|---|---|
| Expo EAS (volatile) | Free plan 30 builds a month, up to 15 for iOS, low priority queue. Starter 19 USD with 45 USD of credit. | 2026-10-24 | docs.expo.dev |

## Tools and libraries

| Topic | Fact | Checked | Source |
|---|---|---|---|
| Godot | Latest stable seen 4.7.2 (2026-08-18). MIT license. Web export is single-threaded by default since 4.3 and needs no special headers. C# projects cannot export to the web in Godot 4. Engine docs warn of problems on macOS and iOS browsers (docs page was the unstable version). | 2026-10-24 | apkmirror.com listings, summerengine.com, docs.godotengine.org |

## AI features

| Topic | Fact | Checked | Source |
|---|---|---|---|
| Chrome Summarizer API | Stable from Chrome 138. Runs Gemini Nano on the device, downloaded on first use. Languages: English, Japanese, Spanish, German, French. Not available in Web Workers. Not supported on Android, iOS, or ChromeOS on non-Chromebook Plus devices. Has hardware requirements listed on its docs page. Whether `key-points` with `medium` length yields five bullets is unverified. | 2026-10-24 | developer.chrome.com/docs/ai/summarizer-api |
| Gemini free tier | Free of charge with per-project limits that vary by guide. Submitted content can be used to improve Google's products. Not available for serving users in the EU, EEA, UK, and Switzerland. | 2026-10-24 | yingtu.ai, spurnow.com, tinkerllm.com, laozhang.ai |
| Chrome on-device model hardware | Reported by extension store listings (secondary source, confirm on Chrome's docs page): Chrome 138 or newer, Windows 10 or 11 or macOS 13 or newer, 4 GB or more of GPU memory or 16 GB of RAM with 4 or more cores, 22 GB free storage for a one-time model download of a few GB | 2026-10-24 | chromewebstore.google.com listings, extensionauditor.com |
| AI Chrome extension privacy | An Incogni study from January 2026 of 442 AI Chrome extensions (115.5 million downloads) found 52% collect user data and 29% collect personally identifiable information | 2026-10-24 | fast.io roundup |
| On-device summarizer extensions | Several already exist with tiny audiences: Private AI Summary (open source, key-points format, zero network requests, 4 users), AI-Select, Free AI Summarizer, AutoSummarizer, SummaPage. Article Summarizer is a free competitor with 7,000 or more users and a Featured badge. | 2026-10-24 | chromewebstore.google.com, extensionauditor.com, peerpush.com |
| Low-cost model price stand-in (volatile) | 0.10 USD per million input tokens and 0.40 USD per million output tokens for Gemini 2.5 Flash-Lite, from a February 2026 guide. Not verified for the current model. | 2026-10-24 | laozhang.ai |

## Services with free tiers (volatile: re-verify when chosen)

| Service | Last seen | Checked | Source |
|---|---|---|---|
| Supabase | Free: 500 MB database, 50,000 monthly active users, 5 GB egress, two active projects, pauses after one week idle, no automatic backups. Pro 25 USD: 8 GB database, 100,000 monthly active users. | 2026-10-24 | supabase.com/pricing and guides |
| Cloudflare Workers static assets | Static requests free and unlimited. Code on the free plan: 100,000 requests a day, 10 ms CPU. Paid plan 5 USD a month. Recommended over Pages for new projects. | 2026-10-24 | cloudflare docs and guides |
| Resend | Free 3,000 emails a month and 100 a day, one domain. Pro 20 USD for 50,000 a month. | 2026-10-24 | resend.com |
| Vercel Hobby | Limited to non-commercial use. Not re-verified in this session. | Not checked | Search if chosen |
