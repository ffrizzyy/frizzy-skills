---
name: frizzy-design
description: Design direction and a swappable design system for any project: tokens with real values and WCAG contrast, typography, icons, motion map, style flavors, components, accessibility, and a restyle protocol. Use for a design system, palette, font pairing, motion plan, restyle, "make it look like these screenshots", or section 8 of a PRD, even if they never say design system.
---

# frizzy-design

Owns PRD section 8 (design system) and the design notes in section 7 (wireframes and screen states). The design is a swappable layer: tokens, a direction statement, and a component list. Behavior, flows, data, and API do not change when the look changes.

## Two ways to run

- Called by project-frizzy: take the handoff (project type, surfaces, audience, vibe words, any references, region), write only section 8 at lean depth, and return it for insertion. Do no research the handoff already covers.
- Standalone: the person asks for a design system, palette, motion plan, or restyle directly. Write `DESIGN.md` (same headings as below) or answer inline when the ask is small. Ask nothing unless the surface is unknown (web, mobile, game, extension).

## Workflow

1. Classify the surfaces: marketing or brand, product UI, mobile, extension popup, game, CLI (a CLI-only project has no design section; say so and stop).
2. Read only what you need in one call, for example
   `python3 scripts/section.py references/design-system.md::"Step 3" references/design-system.md::"Style flavors" references/design-system.md::"Per-surface"`.
   Use `--list references/design-system.md` to see headings.
3. Find the direction. A reference from the person (screenshots, links, words) follows Case A in the reference. Otherwise infer from audience and category with the three dials (variance, motion, density) and say what you chose. Search only when the person gave links to look up. Never ask for a reference as a blocker; invite one in a single line: "Send screenshots, links, or a few words about the look and I will rebuild the design section around it. Otherwise I choose and say what I chose."
4. Decide one base system plus at most one lead flavor, one type pairing, one icon family, and a motion stack that is the lightest tool for each job.
5. Compute every contrast ratio: `python3 scripts/contrast.py "#fg:#bg" ...`. Write the real numbers. Never estimate.
6. Write the section once in final form.

## Section contract

| # | Section | Cap | Lean content |
|---|---|---|---|
| 8 | Design system | 50 | Design read, base and flavor, tokens table with real values and contrast ratios plus a short CSS block, type, icons, 6-row motion map with reduced-motion fallback, component list, accessibility line, swap protocol in five lines |

Full mode lifts the cap and adds the reference mapping table, light and dark values for every role, the component state matrix, imagery and audio guidance, and ASCII wireframes. The full outline is the last heading of `references/design-system.md`.

## After delivery: changing the design

A new reference or a new vibe edits section 8, the screen notes in section 7, and the token, motion, icon, and type values only. Keep token names stable. Read the protocol with `python3 scripts/section.py references/design-system.md "Changing the design later"`. Flows, features, data, API, and costs stay untouched except for asset or library costs the new style adds. Bump the PRD version and add a changelog line.

## Handoffs to sibling skills

- To frizzy-test: the accessibility targets (WCAG 2.2 AA, axe in CI) and the viewport set for screenshot checks (375, 768, 1280, 1920 pixels).
- To frizzy-stack: licenses for fonts, icons, and animation libraries for the cost and license appendix.
- From frizzy-security: the consent banner states (first visit, accepted, rejected, customized, changed later) that need a design.

## Facts

`references/facts.md` holds dated facts about GSAP, React Bits, and the two design skills; the reuse rules are at the top. Cite the checked date in the PRD.

Writing rules: one title, sentence case headings, no emoji or horizontal rules, no em or en dashes (write ranges with "to"), no bold labels on list items, no "not just X but Y", no staged openers, and none of crucial, pivotal, seamless, leverage, robust, vibrant, showcase, delve, cutting-edge, holistic, empower. Name specifics, decision before reasoning, straight quotes. No placeholders: unknowns become open questions with an owner and a date.

## Reference map

| File | Use |
|---|---|
| `references/design-system.md` | Direction, tokens, typography, icons, motion, flavors, per-surface guidance, change protocol |
| `references/section-guide.md` | Full-mode guidance for section 8 |
| `references/facts.md` | Dated facts for design libraries and skills |
| `scripts/contrast.py` | WCAG contrast ratios |
| `scripts/section.py` | Print only the headings you need |
