# Build-phase kit

Companion tools for the build, not for planning. Nothing here runs while the PRD is written. Read only the section you need with `scripts/section.py`. Facts and install commands are in `facts.md`. Claims below are the authors' own unless stated.

## The tools

| Tool | Use for | Token profile | Notes |
|---|---|---|---|
| security-audit (Cloudflare) | Deep code security audit at gates | On demand, multi-agent, heavy | Needs sub-agents, Node.js, and a sandbox. Details in the frizzy-security skill. |
| ponytail | Reuse-first discipline: check the repo, standard library, platform, and installed dependencies before writing code. `/ponytail-review` per diff, `/ponytail-audit` for the repo, `/ponytail-debt` for deferred shortcuts. | Always-on prompt, with lite, full, and ultra levels | Never cuts validation, security, or accessibility. Authors report on 39 tasks in Claude Code: 53% less code, 45% fewer tokens. |
| caveman | Shorter agent replies, shrinking of logs, JSON, and CSV before the agent reads them, and `/caveman-compress` for memory files such as `AGENTS.md` | The voice rules cost about 1,160 input tokens. Authors report the voice adds little over "answer concisely", and reading less cut input tokens 33% per session. | Never rewrites the user's prompts, since its own research found that hurts answers. |
| superpowers | A full method: brainstorm, plan, execute, test first, review | Always-on bootstrap. Subagent execution is the most thorough and the costliest, inline execution is the cheapest. | Skills trigger automatically and are mandatory workflows. |
| graphify | Query an existing codebase as a graph instead of reading files; also maps docs, SQL schemas, and PDFs | Build on demand. Code parsing is local with no model. Docs and PDFs use a model. | Official package is `graphifyy` (double y). Its Cloud product is paid, and its 80% saving claim is the vendor's. |
| playwright-cli | Visual and flow checks | On demand | Install commands in the frizzy-test skill. |

## Choosing the kit

At most four tools in any PRD.

| Project | Kit | Why |
|---|---|---|
| New, small, solo | ponytail, playwright-cli, security-audit at the gates; caveman skill-only if replies are chatty | A small codebase needs no graph and no heavy process |
| New, several milestones, tests matter | superpowers with inline plan execution, playwright-cli, security-audit at the gates | A written plan and test-first work earn their cost |
| Existing or large codebase | graphify built from code only, plus one of the rows above | Querying beats reading file after file |
| High stakes (payments, health, children) | superpowers with subagent review on risky milestones, two security-audit runs | Independent checking is the point |

## Rules that keep it consistent and cheap

1. Always-on budget: at most two always-on tools. Everything else is invoked when needed.
2. One build discipline per project. ponytail and superpowers both set always-on rules about minimal code and tests (ponytail leaves one small test for logic, superpowers enforces red-green test-first). Pick one. Running both is untested here.
3. Caveman voice is for agent chatter only. Never for PRD prose, legal text, or user-facing copy, and never for security warnings (caveman itself switches to full sentences there). Leave the user's prompts alone.
4. Review layers differ: `/ponytail-review` is a cheap review of each diff, the security audit is deep and runs at the gates. Do not run both on every change.
5. graphify: index code only first (`--code-only` on a mixed repo, or `GRAPHIFY_BACKEND=none`), add docs only if they matter. Skip it for a new project until the first milestone produces code.
6. `AGENTS.md` stays at 8 bullets or fewer and holds project rules only. Name the installed tools but do not paste their rules, and do not add two unconditional graph instruction blocks (graphify's own guidance for combining its CLI and MCP setups).
7. Privacy flags go into the PRD: caveman's CLI sends usage statistics unless `caveman telemetry off` or `DO_NOT_TRACK=1` is set (the skill-only install sends nothing); superpowers' optional visual companion loads a logo that reveals the version unless `SUPERPOWERS_DISABLE_TELEMETRY` is set; graphify writes a local query log, disabled with `GRAPHIFY_QUERY_LOG_DISABLE=1`; ponytail's band keeps data in `~/.config/ponytail/`.
8. Install hygiene: ask first, use the official source only, check the exact package name, read any `curl | bash` script before running it, and pin versions. Apply the same 14-day minimum age used for project dependencies where practical.
9. Quote benchmark numbers as "the authors report", never as established facts.

## Starting the build with a kit

- Any kit: tell the agent `PRD.md` is the specification and work one milestone at a time.
- superpowers: say that `PRD.md` is the approved design and ask for a plan for the first milestone. The PRD's tickets are milestone-sized, so the plan expands them into small tasks. How it behaves with an existing PRD is untested here.
- graphify: after the first milestone (or at once for an existing repo) run `graphify install`, then `/graphify .` and let the agent query the graph before searching files.
- caveman: install the skill only, and keep the PRD and legal text out of its scope.
- security-audit: follow the plan in the PRD's security section.
