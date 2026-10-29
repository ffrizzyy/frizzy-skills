#!/usr/bin/env python3
"""Lint a project-frizzy PRD.md.

Checks three things:
  1. Coverage: the sections and topics a complete PRD needs for the project type.
  2. Leftovers: placeholders and chat residue that must not ship.
  3. Writing: the mechanical subset of the humanizer rules (dashes, emoji, stock words,
     staged contrasts, decorative formatting). Judgment calls stay with the humanizer pass.

Usage:
  python3 lint_prd.py PRD.md --profile web --profile mobile
  python3 lint_prd.py PRD.md --profile game --json

Profiles: web, mobile, desktop, extension, game, api, cli, ai, bot.
Combined projects pass several --profile flags; required sections are the union.
Exit code is 1 when any ERROR is reported, otherwise 0.
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

# ---------------------------------------------------------------- coverage

# Each group is satisfied when any heading matches any pattern.
SECTION_GROUPS = {
    "tldr": r"tl;?dr|at a glance|summary",
    "context": r"context|background|overview",
    "problem": r"problem|pain|why this",
    "users": r"users?\b|personas?|audience",
    "goals": r"goals?|success metrics?|objectives?|non-goals?",
    "scope": r"scope|mvp|release plan",
    "features": r"features?|requirements?|user stories",
    "user_flow": r"user flows?|journeys?|information architecture|screens?|navigation",
    "design": r"design system|design direction|visual design|ui design|art direction|look and feel|style guide",
    "stack": r"tech stack|technology|architecture|stack",
    "data": r"database|data model|schema|data design|data and storage|save data",
    "backend_api": r"\bapi\b|backend|endpoints?|server",
    "infra": r"infrastructure|environments?|hosting|devops",
    "security": r"security|owasp|threat",
    "privacy_legal": r"privacy|legal|compliance|polic(?:y|ies)|terms|cookie|consent",
    "testing": r"testing|quality|\bqa\b",
    "deployment": r"deploy|shipping|release|launch|distribution",
    "costs": r"costs?|budget|pricing",
    "roadmap": r"roadmap|milestones?|timeline|phases?",
    "risks": r"risks?",
    "workflow": r"development workflow|dev workflow|local setup",
    "analytics": r"analytics|growth|monetization",
    "game_design": r"game design|core loop|gameplay|mechanics",
    "extension_surface": r"manifest|permissions?",
    "cli_surface": r"commands?|public api|interface|usage",
    "mobile_surface": r"offline|push|permissions?|store listing",
}

BASE = [
    "tldr", "context", "problem", "users", "goals", "scope", "features",
    "user_flow", "design", "stack", "security", "privacy_legal", "testing",
    "deployment", "costs", "roadmap", "risks", "workflow", "analytics",
]
PROFILE_EXTRA = {
    "web": ["data", "backend_api", "infra"],
    "mobile": ["data", "backend_api", "infra", "mobile_surface"],
    "desktop": ["data", "infra"],
    "extension": ["extension_surface"],
    "game": ["game_design"],
    "api": ["data", "backend_api", "infra"],
    "cli": ["cli_surface"],
    "ai": ["data", "backend_api", "infra"],
    "bot": ["backend_api", "infra"],
}

# A base section is skipped only when every selected profile skips it. A game swaps its
# features section for a game design section; a CLI-only project has no screens or visual design.
PROFILE_SKIP = {
    "game": ["features"],
    "cli": ["user_flow", "design"],
}

# ---------------------------------------------------------------- writing tells

AI_WORDS = [
    "additionally", "align with", "bolstered", "crucial", "deep dive", "delve",
    "enduring", "garner", "interplay", "intricate", "intricacies", "meticulous",
    "meticulously", "pivotal", "showcase", "showcasing", "tapestry", "testament",
    "underscore", "underscores", "vibrant", "seamless", "seamlessly", "leverage",
    "leveraging", "cutting-edge", "game-changer", "world-class", "best-in-class",
    "state-of-the-art", "unlock the", "empower", "elevate", "holistic", "synergy",
]

CONTRAST_PATTERNS = [
    r"\bnot (?:just|only|merely|simply)\b[^.;\n]{0,80}(?:\bbut\b|[,;]\s*(?:it'?s|it is|they'?re|this is)\b)",
    r"\bit'?s not\b[^.;\n]{0,80}[,;] it'?s\b",
    r"\b(?:isn'?t|aren'?t) (?:just|only|merely)\b",
    r"\bthis (?:does not|doesn'?t) mean\b",
]
STAGING_PATTERNS = [
    r"\blet'?s (?:dive|explore|break|unpack)\b",
    r"here'?s what you need to know",
    r"\bwithout further ado\b",
    r"\bin today'?s (?:fast-paced|digital|modern)\b",
    r"\bthat'?s the (?:real|whole) (?:win|point|magic)\b",
    r"\bat its core\b",
    r"\bthe real (?:question|win|value)\b",
]
CHAT_RESIDUE = r"i hope this helps|let me know if|great question|certainly!|of course!|would you like me to|as an ai\b"
PLACEHOLDERS = r"\bTBD\b|\bTODO\b|\bFIXME\b|lorem ipsum|\[insert[^\]]*\]|<placeholder>|\bXXX\b|\?\?\?"

EMOJI = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U00002B50\U00002B06\U0001F000-\U0001F2FF]"
)
DASHES = re.compile(r"[\u2014\u2013]| -- ")
CURLY = re.compile(r"[\u201C\u201D\u2018\u2019]")


class Report:
    def __init__(self):
        self.items = []  # (level, rule, message, lines)

    def add(self, level, rule, message, lines=None):
        self.items.append((level, rule, message, sorted(set(lines or []))))

    @property
    def errors(self):
        return [i for i in self.items if i[0] == "ERROR"]

    @property
    def warnings(self):
        return [i for i in self.items if i[0] == "WARN"]


def split_document(text):
    """Return (lines, in_code flags, fence languages, headings)."""
    lines = text.splitlines()
    in_code = []
    langs = []
    headings = []  # (line_no, level, text)
    fenced = False
    fence_marker = ""
    for i, line in enumerate(lines, start=1):
        stripped = line.strip()
        marker = stripped[:3]
        if marker in ("```", "~~~"):
            if not fenced:
                fenced = True
                fence_marker = marker
                langs.append(stripped[3:].strip().lower())
                in_code.append(True)
                continue
            if marker == fence_marker:
                fenced = False
                in_code.append(True)
                continue
        in_code.append(fenced)
        if not fenced:
            m = re.match(r"^(#{1,6})\s+(.*\S)\s*$", line)
            if m:
                headings.append((i, len(m.group(1)), m.group(2)))
    return lines, in_code, langs, headings


def prose_view(line):
    """Strip inline code and URLs so they never trigger writing rules."""
    line = re.sub(r"`[^`]*`", "", line)
    line = re.sub(r"https?://\S+", "", line)
    return line


PROPER_NOUNS = {
    "chrome", "firefox", "edge", "safari", "steam", "godot", "apple", "google", "android", "ios",
    "windows", "linux", "mac", "macos", "cloudflare", "supabase", "github", "playwright", "owasp",
    "gemini", "indonesia", "indonesian", "english", "bahasa", "expo", "stripe", "phosphor",
}


def looks_title_case(heading):
    words = [w for w in re.findall(r"[A-Za-z][A-Za-z'-]*", heading) if w.lower() not in PROPER_NOUNS]
    if len(words) < 3:
        return False
    rest = words[1:]
    long_rest = [w for w in rest if len(w) > 3]
    if len(long_rest) < 2:
        return False
    caps = [w for w in long_rest if w[0].isupper() and not w.isupper()]
    return len(caps) / len(long_rest) >= 0.7


ID_PATTERN = re.compile(r"\b(?:F|R|OQ|G|E|D|S|P)-\d{1,3}\b")


def dangling_ids(lines, in_code):
    """Return IDs that are cited somewhere but never defined.

    An ID counts as defined when it opens a table row or a heading, for example
    '| R-3 | ...' or '### F-004 ...'. Anything else is a citation.
    """
    defined, cited = set(), {}
    for i, raw in enumerate(lines, start=1):
        if in_code[i - 1]:
            continue
        stripped = raw.strip()
        m = re.match(r"^\|\s*((?:F|R|OQ|G|E|D|S|P)-\d{1,3})\s*\|", stripped)
        if m:
            defined.add(m.group(1))
        h = re.match(r"^#{1,6}\s+((?:F|R|OQ|G|E|D|S|P)-\d{1,3})\b", stripped)
        if h:
            defined.add(h.group(1))
        for ref in ID_PATTERN.findall(prose_view(raw)):
            cited.setdefault(ref, []).append(i)
    return {k: v for k, v in cited.items() if k not in defined}


def section_text(headings, lines, pattern):
    """Concatenate the body text of every section whose heading matches."""
    chunks = []
    for idx, (ln, level, title) in enumerate(headings):
        if re.search(pattern, title, re.I):
            end = len(lines)
            for ln2, level2, _ in headings[idx + 1:]:
                if level2 <= level:
                    end = ln2 - 1
                    break
            chunks.append("\n".join(lines[ln:end]))
    return "\n".join(chunks)


def lint(path, profiles, lean=False):
    text = Path(path).read_text(encoding="utf-8")
    lines, in_code, langs, headings = split_document(text)
    rep = Report()
    low = text.lower()

    # ---- coverage: required sections
    required = [
        g for g in BASE
        if not all(g in PROFILE_SKIP.get(p, []) for p in profiles)
    ]
    for p in profiles:
        for g in PROFILE_EXTRA.get(p, []):
            if g not in required:
                required.append(g)
    titles = [h[2] for h in headings]
    for group in required:
        pat = SECTION_GROUPS[group]
        if not any(re.search(pat, t, re.I) for t in titles):
            rep.add("ERROR", "missing-section", f"No heading matches the '{group}' section (pattern: {pat}).")

    # ---- coverage: topics that must appear somewhere
    topic_checks = [
        ("owasp", r"owasp", "OWASP is never mentioned. Map the project to the right OWASP lists."),
        ("privacy policy", r"privacy policy", "No privacy policy plan."),
        ("terms", r"terms of (?:service|use)|\btos\b|\beula\b", "No terms of service (or EULA) plan."),
        ("consent", r"consent", "No consent design (cookies, analytics, data processing)."),
    ]
    if "web" in profiles:
        topic_checks.append(("cookie", r"cookie", "A web project needs a cookie policy and banner plan."))
    for name, pat, msg in topic_checks:
        if not re.search(pat, low):
            rep.add("ERROR", f"missing-topic-{name.replace(' ', '-')}", msg)

    soft_topics = [
        ("free option", r"\bfree\b", "No free or cheapest option appears in the doc."),
        ("ideal option", r"\bideal\b", "No ideal or best-stack option appears in the doc."),
        ("currency", r"[$\u20ac\u00a3]|\busd\b|\bidr\b|\brp\s?\d", "No prices with a currency appear in the doc."),
        ("design tokens", r"\btokens?\b", "Design section has no tokens, which makes it hard to swap the look later."),
        ("motion", r"motion|animation|transition", "No motion or animation plan."),
        ("icons", r"\bicons?\b|iconography", "No icon plan."),
        ("design swap", r"reference|screenshot|swap|override", "No note on how to change the design from a reference."),
        ("threat model", r"threat model|stride", "No threat model mentioned."),
        ("accessibility", r"wcag|accessib", "No accessibility target."),
        ("rollback", r"rollback|roll back|revert", "No rollback plan in shipping."),
        ("competitors", r"alternatives today|competitors?|comparable (?:titles|products|games)", "No competitor or alternatives analysis."),
        ("code security audit", r"security[- ]audit|code audit|security review of the (?:code|repository)", "No pre-launch code security audit planned (see the security reference)."),
        ("backup", r"backup|restore", "No backup or restore plan."),
    ]
    if profiles & {"web", "extension"}:
        soft_topics.append(("playwright", r"playwright", "Web or extension project with no Playwright testing plan."))
    for name, pat, msg in soft_topics:
        if not re.search(pat, low):
            rep.add("WARN", f"missing-topic-{name.replace(' ', '-')}", msg)

    if not re.search(r"\b20\d\d-\d\d-\d\d\b", text):
        rep.add("WARN", "no-dates", "No ISO date (YYYY-MM-DD) found. Prices, limits and laws need a 'checked on' date.")

    mermaid = sum(1 for l in langs if l == "mermaid")
    need_diagrams, min_lines = (1, 150) if lean else (2, 300)
    if mermaid < need_diagrams:
        rep.add("WARN", "few-diagrams", f"Only {mermaid} Mermaid diagram(s). At least a user flow deserves one.")

    if len(lines) < min_lines:
        rep.add("WARN", "short-doc", f"{len(lines)} lines is short for a {'lean' if lean else 'full'} PRD.")

    # ---- structure
    h1 = [h for h in headings if h[1] == 1]
    if len(h1) > 1:
        rep.add("WARN", "multiple-h1", "More than one top-level heading.", [h[0] for h in h1])
    for idx, (ln, level, title) in enumerate(headings):
        nxt = headings[idx + 1][0] if idx + 1 < len(headings) else len(lines) + 1
        body = [l for l in lines[ln:nxt - 1] if l.strip()]
        if not body and (idx + 1 >= len(headings) or headings[idx + 1][1] <= level):
            rep.add("WARN", "empty-section", f"Heading '{title}' has no content.", [ln])

    # ---- the PRD must not point at the planning tool's own files
    leak_re = re.compile(r"contrast\.py|lint_prd|check_env\.sh|SKILL\.md|project-frizzy|references/[a-z-]+\.md", re.I)
    leaks = [i for i, raw in enumerate(lines, start=1) if not in_code[i - 1] and leak_re.search(raw)]
    if leaks:
        rep.add("ERROR", "skill-leak", "The PRD names the planning skill's own scripts or files. The reader will not have them.", leaks)

    # ---- cross references
    missing_ids = dangling_ids(lines, in_code)
    if missing_ids:
        names = ", ".join(sorted(missing_ids))
        rep.add("WARN", "dangling-id", f"Cited but never defined: {names}.",
                [n for v in missing_ids.values() for n in v])

    # ---- line-level rules, outside code fences
    hits = defaultdict(list)
    bold_label_lines = []
    front_matter_end = 0
    if lines and lines[0].strip() == "---":
        for j in range(1, min(len(lines), 40)):
            if lines[j].strip() == "---":
                front_matter_end = j + 1
                break

    contrast_res = [re.compile(p, re.I) for p in CONTRAST_PATTERNS]
    staging_res = [re.compile(p, re.I) for p in STAGING_PATTERNS]
    ai_res = [(w, re.compile(r"\b" + re.escape(w) + r"\b", re.I)) for w in AI_WORDS]
    chat_re = re.compile(CHAT_RESIDUE, re.I)
    ph_re = re.compile(PLACEHOLDERS)

    for i, raw in enumerate(lines, start=1):
        if in_code[i - 1] or i <= front_matter_end:
            continue
        line = prose_view(raw)

        if DASHES.search(line):
            hits["dash"].append(i)
        if EMOJI.search(line):
            hits["emoji"].append(i)
        if CURLY.search(line):
            hits["curly"].append(i)
        if re.match(r"^\s*([-*_])\1{2,}\s*$", raw):
            hits["hr"].append(i)
        if raw.startswith("#") and "\u2192" in raw:
            hits["arrow-heading"].append(i)
        if chat_re.search(line):
            hits["chat"].append(i)
        if ph_re.search(raw):
            hits["placeholder"].append(i)
        if any(r.search(line) for r in contrast_res):
            hits["contrast"].append(i)
        if any(r.search(line) for r in staging_res):
            hits["staging"].append(i)
        for word, rx in ai_res:
            if rx.search(line):
                hits["aiword:" + word].append(i)
        if re.match(r"^\s*[-*+]\s+\*\*[^*]+?(?::\*\*|\*\*\s*[:\-])", raw):
            bold_label_lines.append(i)

    for ln, level, title in headings:
        if looks_title_case(title):
            hits["titlecase"].append(ln)

    def emit(key, level, rule, msg):
        if hits.get(key):
            rep.add(level, rule, msg, hits[key])

    emit("dash", "ERROR", "dashes", "Em dash, en dash or ' -- ' found. Use a period, comma, colon, parentheses, or the word 'to' for ranges.")
    emit("emoji", "ERROR", "emoji", "Emoji or pictograph found outside code.")
    emit("chat", "ERROR", "chat-residue", "Chatbot wrapper text found.")
    emit("placeholder", "ERROR", "placeholder", "Placeholder text found (TBD, TODO, lorem ipsum, [insert ...]). Write the content or move it to Open questions.")
    emit("contrast", "WARN", "not-x-but-y", "Staged contrast ('not just X but Y'). State the point directly.")
    emit("staging", "WARN", "staging", "Staged opener or one-line closer.")
    emit("hr", "WARN", "horizontal-rule", "Horizontal rule between sections. Remove it.")
    emit("arrow-heading", "WARN", "arrow-heading", "Arrow in a heading.")
    emit("titlecase", "WARN", "title-case-heading", "Heading looks Title Case. Use sentence case.")
    emit("curly", "WARN", "curly-quotes", "Curly quotes found. Use straight quotes.")

    ai_hits = {k[len("aiword:"):]: v for k, v in hits.items() if k.startswith("aiword:")}
    if ai_hits:
        words = ", ".join(sorted(ai_hits))
        all_lines = [n for v in ai_hits.values() for n in v]
        rep.add("WARN", "ai-words", f"Stock AI words: {words}.", all_lines)

    if len(bold_label_lines) >= 4:
        rep.add("WARN", "bold-label-list", "List items start with a bold label and colon. Use a table or plain prose.", bold_label_lines)

    return rep, len(lines), len(headings)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("prd", help="path to PRD.md")
    ap.add_argument("--profile", action="append", default=[], choices=sorted(PROFILE_EXTRA),
                    help="project type; repeat for combined projects (default: web)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--lean", action="store_true", help="lean PRD: shorter length and fewer diagrams are fine; coverage checks stay the same")
    args = ap.parse_args()

    if not Path(args.prd).is_file():
        print(f"File not found: {args.prd}", file=sys.stderr)
        return 2
    profiles = set(args.profile or ["web"])
    rep, n_lines, n_heads = lint(args.prd, profiles, lean=args.lean)

    if args.json:
        print(json.dumps({
            "file": args.prd,
            "profiles": sorted(profiles),
            "lines": n_lines,
            "headings": n_heads,
            "errors": [{"rule": r, "message": m, "lines": l} for lv, r, m, l in rep.errors],
            "warnings": [{"rule": r, "message": m, "lines": l} for lv, r, m, l in rep.warnings],
        }, indent=2))
    else:
        print(f"{args.prd}: {n_lines} lines, {n_heads} headings, profiles: {', '.join(sorted(profiles))}")
        for level, rule, msg, ls in rep.items:
            where = ""
            if ls:
                shown = ", ".join(str(n) for n in ls[:8])
                more = f" (+{len(ls) - 8} more)" if len(ls) > 8 else ""
                where = f" [lines {shown}{more}]"
            print(f"{level:5} {rule}: {msg}{where}")
        print(f"\n{len(rep.errors)} error(s), {len(rep.warnings)} warning(s)")
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main())
