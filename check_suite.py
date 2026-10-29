#!/usr/bin/env python3
"""Consistency check for the project-frizzy skill suite. For maintainers, not for PRDs.

Run from the folder that holds the six skill folders:  python3 check_suite.py [--root .]

Checks:
  1. Frontmatter: name equals folder name, description present.
  2. Backticked paths (references/..., scripts/...) exist inside the same skill.
  3. section.py examples resolve to a real heading in the same skill.
  4. Every PRD section 0 to 21 has exactly one owner, and the owner's contract row matches
     the orchestrator's table (number, name, cap).
  5. Section names are recognized by the PRD linter, and linter profiles match SKILL.md.
  6. Bare mentions of files that live in another skill (for example "intake.md" inside frizzy-design).
  7. Skill names mentioned in text exist.
  8. Facts rows carry a checked date, with stale rows (over 60 days) listed.
  9. No em or en dashes. SKILL.md size budget.
"""
import argparse, importlib.util, re, sys
from datetime import date, datetime
from pathlib import Path

SKILLS = ["project-frizzy", "frizzy-design", "frizzy-stack", "frizzy-security", "frizzy-test", "frizzy-ship"]

def load(root, name):
    spec = importlib.util.spec_from_file_location(name, root / "project-frizzy" / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--root", default="."); ap.add_argument("--budget", type=int, default=16000)
    a = ap.parse_args(); root = Path(a.root).resolve()
    sec, lint = load(root, "section"), load(root, "lint_prd")
    out = []
    add = lambda lv, m: out.append((lv, m))
    files = {}
    for s in SKILLS:
        d = root / s
        if not (d / "SKILL.md").exists():
            add("ERROR", f"{s}: SKILL.md missing"); continue
        for f in [d / "SKILL.md", *sorted((d / "references").glob("*.md"))]:
            files[f] = (s, f.read_text(encoding="utf-8"))

    # 1 frontmatter
    for s in SKILLS:
        t = files.get(root / s / "SKILL.md", (None, ""))[1]
        m = re.match(r"---\nname: (.+)\ndescription: (.+)\n---\n", t)
        if not m: add("ERROR", f"{s}: bad frontmatter")
        elif m.group(1).strip() != s: add("ERROR", f"{s}: frontmatter name is {m.group(1)}")
        elif len(m.group(2)) > 1024: add("ERROR", f"{s}: description over 1024 characters ({len(m.group(2))})")

    # 2 and 3 paths and section.py examples
    own_files = {}
    for f, (s, t) in files.items():
        own = root / s
        for m in re.finditer(r"`((?:references|scripts)/[\w./-]+)`", t):
            if not (own / m.group(1)).exists(): add("ERROR", f"{s}/{f.name}: path does not exist: {m.group(1)}")
        for m in re.finditer(r'(references/[\w.-]+\.md)::"([^"]+)"', t):
            if (own / m.group(1)).exists() and not sec.pull(str(own / m.group(1)), m.group(2)):
                add("ERROR", f'{s}/{f.name}: no heading "{m.group(2)}" in {m.group(1)}')
        for m in re.finditer(r'section\.py (references/[\w.-]+\.md) "([^"<]+)"', t):
            if (own / m.group(1)).exists() and not sec.pull(str(own / m.group(1)), m.group(2)):
                add("ERROR", f'{s}/{f.name}: no heading "{m.group(2)}" in {m.group(1)}')

    # 4 ownership and contracts
    orch = files[root / "project-frizzy" / "SKILL.md"][1]
    table = {int(n): (name.strip(), int(cap), own.strip()) for n, name, cap, own in
             re.findall(r"^\| (\d+) \| ([^|]+) \| (\d+) \|.*\| ([^|]+) \|$", orch, re.M)}
    if sorted(table) != list(range(22)): add("ERROR", f"orchestrator table covers sections {sorted(table)}")
    contracts = {}
    for s in SKILLS[1:]:
        t = files[root / s / "SKILL.md"][1]
        for n, name, cap in re.findall(r"^\| (\d+) \| ([^|]+) \| (\d+) \|", t, re.M):
            n = int(n)
            if n in contracts: add("ERROR", f"section {n} claimed by {contracts[n][0]} and {s}")
            contracts[n] = (s, name.strip(), int(cap))
    for n, (name, cap, own) in table.items():
        if own.startswith("frizzy-"):
            c = contracts.get(n)
            if not c: add("ERROR", f"section {n} owned by {own} in the orchestrator but has no contract there")
            elif c[0] != own or c[1] != name or c[2] != cap:
                add("ERROR", f"section {n}: orchestrator says {own}/{name}/{cap}, owner says {c}")
            guide = root / own / "references" / "section-guide.md"
            if guide.exists() and not re.search(rf"^### {n}\. ", guide.read_text(encoding="utf-8"), re.M):
                add("ERROR", f"{own}: section-guide.md lacks section {n}")
    for n in contracts:
        if n not in table or not table[n][2].startswith("frizzy-"): add("ERROR", f"{contracts[n][0]} claims section {n} the orchestrator does not delegate")
    tmpl = files[root / "project-frizzy" / "references" / "prd-template.md"][1]
    tmpl_heads = {int(n): nm.strip() for n, nm in re.findall(r"^### (\d+)\. (.+)$", tmpl, re.M)}
    for n, (name, cap, own) in table.items():
        if n in (0, 21): continue
        if tmpl_heads.get(n, "").lower() != name.lower(): add("ERROR", f"prd-template.md section {n} is '{tmpl_heads.get(n)}', table says '{name}'")
        if not any(re.search(p, name, re.I) for p in lint.SECTION_GROUPS.values()): add("ERROR", f"linter would not recognize '{name}'")

    # 5 profiles
    m = re.search(r"one `--profile` per project type: ([a-z, ]+)\)", orch)
    if m and {p.strip() for p in m.group(1).split(",")} != set(lint.PROFILE_EXTRA): add("ERROR", "profiles differ from the linter")

    # 6 bare file mentions that live in another skill
    where = {}
    for f, (s, t) in files.items(): where.setdefault(f.name, set()).add(s)
    for f, (s, t) in files.items():
        for name in re.findall(r"\b([\w-]+\.md)\b", t):
            if name in ("SKILL.md", "PRD.md", "AGENTS.md", "DESIGN.md", "STACK.md", "SECURITY.md", "TEST-PLAN.md", "SHIP.md", "README.md", "GRAPH_REPORT.md", "MEMORY.md"): continue
            if name in where and s not in where[name]:
                add("ERROR", f"{s}/{f.name}: mentions {name}, which lives in {sorted(where[name])}, not in this skill")

    # 7 skill names
    for f, (s, t) in files.items():
        for name in set(re.findall(r"\b(frizzy-[a-z]+|project-frizzy)\b", t)):
            if name not in SKILLS: add("ERROR", f"{s}/{f.name}: unknown skill name {name}")

    # 8 facts
    today = date.today(); stale = []
    for s in SKILLS:
        p = root / s / "references" / "facts.md"
        if not p.exists(): continue
        for row in p.read_text(encoding="utf-8").splitlines():
            if row.startswith("|") and not row.startswith("|---"):
                cells = [c.strip() for c in row.strip("|").split("|")]
                if len(cells) >= 3:
                    d = re.search(r"\b(20\d\d-\d\d-\d\d)\b", cells[2])
                    if d:
                        age = (today - datetime.strptime(d.group(1), "%Y-%m-%d").date()).days
                        if age > 60: stale.append(f"{s}: {cells[0][:30]} ({age}d)")
                    elif cells[0] not in ("Topic", "Service") and "Not checked" not in row:
                        add("ERROR", f"{s}/facts.md row without a checked date: {cells[0][:40]}")
    if stale: add("WARN", "facts older than 60 days: " + "; ".join(stale))

    # 9 dashes and size
    for f, (s, t) in files.items():
        for i, line in enumerate(t.splitlines(), 1):
            if re.search(r"[\u2014\u2013]", line): add("ERROR", f"{s}/{f.name}:{i}: em or en dash")
    for s in SKILLS:
        p = root / s / "SKILL.md"
        if p.exists():
            size = p.stat().st_size; add("INFO", f"{s}/SKILL.md {size:,} bytes")
            if size > a.budget: add("ERROR", f"{s}/SKILL.md exceeds {a.budget:,} bytes")

    order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    for lv, m in sorted(out, key=lambda x: order[x[0]]): print(f"{lv:5} {m}")
    e = sum(1 for lv, _ in out if lv == "ERROR")
    print(f"\n{e} error(s), {sum(1 for lv, _ in out if lv == 'WARN')} warning(s)")
    return 1 if e else 0

if __name__ == "__main__": sys.exit(main())
