# Full mode: detailed workflow

Read this file only when the person asks for a full, detailed, or thorough PRD, or when the project is high stakes enough that depth is worth the cost (payments handled directly, health data, children, regulated industries). Lean mode in `SKILL.md` is the default. Full mode keeps the same section list and checks, with deeper research (10 to 25 searches), longer sections, and the complete reference files read in full.

Everything below assumes the principles in `SKILL.md`.

## Workflow (full mode)

Work through these steps in order. Steps 0 to 2 are quick, step 3 is where most of the effort goes, and steps 5 and 6 turn the research into a document that passes the quality bar.

### Step 0: check the environment

Run `bash scripts/check_env.sh` from this skill's folder (resolve the path from where this file was loaded). It prints key-value lines and installs nothing. Read the output like this:

- `sandbox: yes` means the shell is a claude.ai container, not the person's computer. Do not install anything there. Put the install commands in the PRD's development workflow section and tell the person in the final message.
- `playwright-cli: missing` and the project has a browser surface (web app, PWA, browser extension, web game, marketing site): ask permission before installing. Explain in one or two sentences that playwright-cli lets the agent open the app, resize to phone, tablet, and desktop widths, take screenshots, read console and network output, record flows, and generate end-to-end tests, which keeps the build honest to the design. Offer the commands `npm install -g @playwright/cli@latest` and `playwright-cli install --skills` (Node 18 or newer). Install only after a clear yes, and only when `network_npm_registry` is reachable and the shell is the person's machine. If they decline, write `@playwright/test` as a project dependency into the testing plan instead. Skip the question for projects without a browser surface.
- Missing design skills (`emil-design-eng`, `design-taste-frontend`): mention the install commands from the script output. Ask before installing, because skills change the person's agent setup.
- Missing `humanizer`: follow `references/writing-style.md` by hand.

Use `ask_user_input_v0` for the permission question when it is available. Otherwise ask in plain text with a yes or no.

### Step 1: read the brief and classify

Decide the primary project type and any secondary types. Read `references/project-types.md` for each type involved. It gives the lifecycle and gates, security standard, test and ship paths, and which PRD sections to swap. Combined projects keep one PRD with a shared core and a subsection per surface.

Flag anything that raises the stakes: children, health, money, identity documents, AI-generated content, user-generated content, or a regulated industry.

### Step 2: fill gaps with as few questions as possible

Read `references/intake.md`. Ask only for blocking gaps, in one batch of at most three questions, each with a recommended default. If the brief is clear enough, ask nothing. Show an assumptions table and invite corrections, and include the design invitation (send screenshots, links, or a few words about the look, or let me choose).

If the person says to just decide, proceed on defaults.

### Step 3: research

Use web search. A full run usually takes 10 to 25 searches. Cover:

1. Alternatives and competitors (3 to 6). Never skip this, even for games, extensions, and small tools: what they do, price, and what users complain about, plus an honest note on how crowded the space is. Prefer official pages and review or community sources. Summarize in your own words and do not quote at length.
2. Technology currency: current stable versions of the chosen frameworks, deprecations, and signs a library is maintained.
3. Prices and free-tier limits for every service in both the free and ideal columns, from official pricing pages. Record limit, price, and date. Convert currency only with a stated rate.
4. Platform rules for this project type: store policies, extension rules, engine license terms, payment provider terms, merchant-of-record options.
5. Law and standards: the current edition of each OWASP list that applies, plus privacy, consent, and children's rules for the regions in play.
6. Design: if the person sent references, study them. If not, look at three to five well-regarded examples for the chosen direction to ground the choices. Describe qualities, never copy assets.

Keep a running list of sources with URL and date for the research appendix. If a search cannot confirm something, say so in the PRD instead of guessing. Use the real current date from the conversation context in queries and "checked on" stamps.

### Step 4: decide

Make decisions in this order, since each one constrains the next: delivery method, architecture shape, stack (free and ideal), data model, security and compliance baseline, design direction, test plan, ship plan. Read:

- The frizzy-stack skill for decision records, candidate services, verification, and cost tables (sections 9, 10, 11, 19).
- The frizzy-security skill for the OWASP mapping, legal documents, consent design, and regional rules (section 13).
- The frizzy-design skill for design direction, tokens, motion, icons, and style flavors (section 8).
- The frizzy-test and frizzy-ship skills for sections 14, 12, 15, and 16.

Write each major decision as a decision record with the pick, the ideal alternative, the reason, and the switch trigger.

### Step 5: write the PRD

Read `references/prd-template.md` for the section order and what each section this skill owns must contain. For sections 8 to 16 and 19, read the owning skill's section guide and follow its workflow (find the installed skills with `bash scripts/find_suite.sh`). Write one `PRD.md`; this skill stays the single writer.

Build it in passes so each tool call stays manageable: skeleton with every heading, then sections in order, then diagrams, then cost tables, then the roadmap. A full PRD is long, and that is expected, but each section starts with the answer and stays specific.

Hard requirements for the content:

- Covers context, the problems solved, users, goals, scope, features with acceptance criteria, user flows, design system, architecture and tech stack, data model or database schema, backend and API, infrastructure, security, privacy and legal, testing, development workflow, deployment and shipping, analytics and monetization, roadmap, costs, risks, and appendices.
- Security names its standards with edition years, maps OWASP risks to controls, and plans the privacy policy, terms of service, cookie policy and consent banner, data map, user-rights flows, and regional compliance. The PRD never contains the full text of a privacy policy, terms of service, or cookie policy. It holds the documents plan and the policy fact sheet, which is what a lawyer or policy generator needs.
- Costs show the free or cheapest path and the ideal path with prices, dated, plus upgrade triggers.
- Design is token-based, includes real values, a motion map, an icon choice, a style direction, and the swap protocol.
- A testing plan that includes Playwright, and a dev setup that lists the tools to install.
- Roadmap tickets are small, checkable, and cite feature IDs, so a coding agent can pick one up.
- Mermaid diagrams for flows, data, and architecture; ASCII wireframes for key screens.
- The PRD never mentions this skill's own scripts, files, or reference documents. Its reader does not have them. Say what was done ("contrast ratios calculated with the WCAG formula"), not which tool did it.

### Step 6: humanize and lint

1. Run the humanizer skill on the PRD's prose (see `references/writing-style.md`). Embedded or file mode, prose only.
2. Run `python3 scripts/lint_prd.py PRD.md --profile <type>` with one `--profile` per project type (web, mobile, desktop, extension, game, api, cli, ai, bot). Fix all errors and review warnings.
3. Read the TL;DR as the owner. It must stand alone. Then check that numbers agree across sections: timeline in the title block, TL;DR, scope, and roadmap; costs in the TL;DR and the cost tables; feature IDs in scope, features, and roadmap; risk and question IDs wherever they are cited; section numbers in cross-references. For an extension, parse the manifest block and confirm its permissions equal the permission table. Inconsistencies between sections are the most common defect the linter cannot see.
4. Re-run the linter until there are no errors.

Also plan the pre-launch code security audit described by the frizzy-security skill (section "Pre-launch code security audit") and mirror it in the roadmap, testing, and launch checklist.

Choose and document the build kit (section 15 of the PRD) as described by the frizzy-ship skill: at most four tools, at most two always-on, one build discipline.

### Step 7: deliver

- Write the file as `PRD.md`. In a repository, put it at the root, or in `docs/` if that folder exists. In claude.ai, write to `/mnt/user-data/outputs/PRD.md` and call `present_files`. Do not publish it as a hosted page, since the person asked for a markdown file.
- Reply briefly. Say what the PRD covers in a sentence, give the headline picks (stack, cost to launch, timeline), list the assumptions to confirm and any open questions, and remind the person they can send a reference to change the look. Offer one or two next steps, such as starting milestone 1 or producing a design preview.
- Do not paste the whole PRD into the chat.

## After delivery: changes

- New design reference or description: follow the frizzy-design skill's "Changing the design later" protocol. Edit the design section, tokens, motion map, and screen notes, then re-lint.
- Stack change: update the decision record, architecture, data model, API, infrastructure, testing, deployment, and cost tables. Search the file for the old names so no stale mention remains.
- Scope change: update features, roadmap, costs, and risks.
- Every change adds a line to the changelog appendix and a bumped version in the title block.

## Starting the build

When the person says to start, work through the roadmap one milestone at a time. Use playwright-cli for visual verification (open, resize to 375, 768, 1280, and 1920 pixels, screenshot, read console and requests), the Emil Kowalski skills for motion review, and the PRD's security checklist at each milestone gate. Keep the PRD current as decisions change.
