# Writing and typography for the PRD

The PRD's prose must pass the humanizer skill. That skill removes the habits that make text read as machine-written, and a PRD is long enough for those habits to pile up. This file says how to apply it to a PRD and what the linter checks on its behalf.

## When to run it

1. Draft the whole PRD first. Editing a finished draft is easier than writing carefully and losing momentum.
2. Run the humanizer skill in file mode on `PRD.md`. It changes prose only and leaves code blocks, inline code, commands, paths, data, and link targets alone. Tables are data, but the sentences inside table cells count as prose, so tidy them too.
3. Run `scripts/lint_prd.py`. Fix every error. Read each warning and fix it unless there is a reason to keep the phrase.
4. Read the TL;DR and the first paragraph of three other sections as the owner would. If any sentence could be deleted without losing a fact, delete it.

If the humanizer skill is not installed, apply the rules below by hand.

## Rules that matter most in a PRD

Facts first
- Every sentence adds a fact, a decision, or a reason. Drop sentences that announce importance or summarize what the reader just read.
- Do not invent numbers, quotes, market sizes, user counts, or competitor details. If research did not find a figure, say so or leave the claim out.
- Name the specific thing. "Postgres on Supabase, free plan, 500 MB limit, checked 2026-10-23" beats "a scalable database solution".

Staging and contrast
- State the point directly. Avoid "not just X but Y", "it's not X, it's Y", and "this doesn't mean X, it means Y". Keep a contrast only when the first half corrects a belief the reader actually has.
- Cut one-line closers that repeat the paragraph ("That is the real win.").
- No staged openers such as "Let's dive in" or "Here's what you need to know".

Rhythm
- Use triads only when there are three real items. Vary sentence length.
- Do not use em dashes or en dashes anywhere in the prose. Use a period, comma, colon, or parentheses. Write ranges with "to" ("2 to 4 weeks"). Hyphens inside compound words and code are fine.

Word choice
- Prefer "is", "are", and "has" over "serves as", "boasts", "features".
- Avoid stock words: additionally, crucial, delve, pivotal, showcase, seamless, leverage, robust (when figurative), vibrant, tapestry, testament, underscore, cutting-edge, world-class, holistic.
- No sales language. A PRD describes a product to the people building and funding it, so claims must be checkable.
- No inflated significance ("a pivotal step", "the future looks bright"). End sections on the last concrete fact.
- Prefer active voice and name the actor.

Formatting and typography
- Headings in sentence case. One title at the top, not repeated in the first sentence.
- No emoji. No arrows or decoration in headings. No horizontal rules between sections.
- No bold for decoration. Do not give list items a bold label and a colon. Use a table when items have attributes, or plain prose when they do not.
- Straight quotes and apostrophes in the file. Consistent code fences with a language tag.
- Do not write about the document itself ("this section describes", "the table below compares") unless the reader needs a convention explained once.

Plain language for the owner
- Explain a technical term the first time it matters, or point to the glossary. Prefer the plain word when both are accurate ("saved data" over "persistence layer").
- Put the decision before the reasoning, and the reasoning before the detail.

## Before and after, in PRD voice

Before:
> Our robust and scalable architecture seamlessly leverages cutting-edge serverless technology, ensuring a pivotal foundation for growth.

After:
> The API runs as serverless functions on Cloudflare Workers. The free plan covers the first 100,000 requests a day (checked 2026-10-23), enough for the first few thousand users.

Before:
> This isn't just a to-do app, it's a complete productivity ecosystem. Let's dive into the features.

After:
> The app lets a person capture tasks by voice or text, group them by project, and see today's list on one screen.

Before:
> Security is crucial. We will implement best practices, ensuring user data is protected, trusted, and safe.

After:
> Passwords are hashed with Argon2id. Every table has row-level security, and the authorization matrix in section 13 is tested in CI. Backups are encrypted, and a restore test runs before launch.

## What the linter checks

Errors: dashes, emoji, placeholder text, chatbot residue, missing sections, missing OWASP, privacy policy, terms, and consent coverage.

Warnings: staged contrasts, staged openers, stock words, horizontal rules, title-case headings, curly quotes, bold-label lists, multiple top-level headings, empty sections, missing dates, too few diagrams, and a short document.

The linter is a floor, not a judge. A clean report does not prove the prose is good, so the read-through in step 4 still matters.
