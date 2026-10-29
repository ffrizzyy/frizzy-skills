# Intake: what to ask and what to assume

Read this at step 2. The aim is a plan the person can trust without sitting through an interview. Most briefs arrive as one or two sentences, so most of the plan comes from your decisions. Ask only when a missing answer would change the shape of the plan.

## The brief at a glance

| Field | Why it matters | Default when unanswered |
|---|---|---|
| Idea in one or two sentences | Everything depends on it | None. Ask. |
| Who it is for | Personas, tone, accessibility, legal exposure | Infer from the idea. Ask only if two readings lead to different products. |
| Project type and platforms | Picks lifecycle, stack, store rules | Infer from wording. A bare "app" is ambiguous, so ask. |
| Where the users live | Privacy law, payments, languages | Global, with a GDPR-grade baseline, plus the person's own country if known |
| Budget stance | Stack and cost tables | Free or cheapest first, ideal path shown beside it |
| Money model | Payments, tax, store fees, architecture | None for the MVP, with a "later" note |
| Team and skills | Stack choice, lifecycle | One developer working with an AI coding agent |
| Deadline or launch target | Scope cuts | MVP in 6 to 8 weeks of part-time work |
| Look and feel | Design direction | Inferred from audience. A reference is invited, never required. |

## What counts as blocking

Ask when the answer changes the plan's shape:

- The idea is unclear enough that two reasonable readers would build different things.
- The platform is ambiguous in a way that changes the stack ("an app": web, mobile, or both?).
- The domain is regulated (health, finance, children, education, identity documents). You need the region and the kind of data.
- An existing codebase or mandatory stack exists. Read the repo first if you have access, then ask only what the repo does not answer.
- The budget or deadline is stated vaguely and the vagueness matters ("cheap", "soon").

Everything else is an assumption: names, colors, exact feature lists, tool preferences, pricing numbers, tone of voice. State it, let the person correct it, and move on.

## How to ask

- One batch, at most three questions, each with a recommended default listed first so the person can accept with one tap or one word.
- In claude.ai and other clients that offer `ask_user_input_v0`, use it: two to four short options per question. Elsewhere, send a numbered list and say that replying "go" accepts every default.
- Do not ask what you can research: competitors, prices, store rules, library maturity.
- Do not ask about design in this batch unless the project is design-led (portfolio, brand site, game). The design invitation goes in the assumptions block instead.
- After the answers arrive, do not ask again unless a new blocker appears.
- If the person says "just decide", skip questions entirely and proceed on defaults.

Example batch for "I want to build a habit tracker":

1. Where should it run? (Web app that also installs on phones [recommended] / Native iOS and Android app / Web only)
2. Who is it for? (General public [recommended] / A specific group such as students, athletes, patients)
3. Will it ever charge money? (Free for now, maybe later [recommended] / Subscription from day one / One-time purchase)

## The assumptions block

Before writing, show a short table and repeat it in the PRD's TL;DR:

| Assumption | Why | How to change it |
|---|---|---|

Keep it to the five or six assumptions that would most change the plan. Add one line inviting corrections.

## Design invitation

Include this near the assumptions block, in your own words:

"If you have a look in mind, send screenshots, links, or a few words (for example "calm editorial with a bit of neon") and I will build the design system around it. If you skip this, I will pick a direction from the audience and tell you what I picked."

## Scaling the brief

- Very large ideas ("like Uber", "my own operating system"). Propose the thinnest slice worth shipping, say what is deferred, write the PRD for that slice, and add a short later-phases outline.
- Existing projects. Read package files, README, schema, and CI config first. The PRD describes the change. Keep the current stack unless it is the problem.
- Regulated domains. Say in the TL;DR that professional legal review is required before launch, and list which documents and registrations.
- Children under 13, health data, or handling card numbers directly. Raise these as top risks and confirm the region.
- A genre or concept left open ("I want to make a game"). Decide it for them: choose the smallest scope that stays replayable, say plainly in the TL;DR that you chose it, and record it in the decision log as a high-cost-to-change assumption with an open question asking them to confirm. Never let an unconfirmed concept pass as the person's choice.
- A person who has already decided the stack. Respect it. Show the free and ideal options only for the pieces they have not chosen.

## Reading shorthand

| They say | Read it as |
|---|---|
| SaaS | Web app with accounts, billing, a settings area, and an admin view |
| Landing page | Static site with a waitlist or contact form, strong on speed and SEO |
| Mobile app | Ask iOS, Android, or both. Default to cross-platform (a PWA is the cheapest start). |
| Game | Ask genre and platform. Default to a small 2D game in Godot or a browser engine. |
| Extension | Chrome (Manifest V3) first, Firefox and Edge ports second |
| Bot | Ask which platform (Discord, Telegram, Slack, WhatsApp) |
| Tool or utility | Ask whether it runs in the browser, on the desktop, or in a terminal |
| Marketplace | Two user types, payments with payouts, trust and safety, dispute handling |
| "With AI" | LLM feature with cost caps, evals, and prompt-injection defenses (see project-types.md) |
