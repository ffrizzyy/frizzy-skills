# frizzy skills

Plan any software project into a `PRD.md`. Install all six skills together.

| Skill | Owns |
|---|---|
| `project-frizzy` | The PRD, intake, scope, roadmap, linter (also the `/project-frizzy` command) |
| `frizzy-design` | Design system (section 8) |
| `frizzy-stack` | Stack, data model, API, costs (sections 9, 10, 11, 19) |
| `frizzy-security` | Security, privacy, compliance (section 13) |
| `frizzy-test` | Testing and quality (section 14) |
| `frizzy-ship` | Infrastructure, workflow, deployment (sections 12, 15, 16) |

Each skill also works on its own. If a sibling skill is missing, `project-frizzy` writes that section from its lean rules.

## Install

- Claude Code: copy or symlink the six folders into `~/.claude/skills/` (or `.claude/skills/` in a project).
- Claude.ai: zip each skill folder and upload it under Settings, Capabilities, Skills.

## Maintain

Run `python3 check_suite.py --root .` after any edit. It checks section ownership, file paths, cross-skill references, fact dates, and dashes.
