#!/usr/bin/env python3
"""Print only the parts of a reference file you need, to save tokens.

Usage:
  python3 section.py --list references/project-types.md
  python3 section.py references/project-types.md "Mobile apps" "Browser and editor"
  python3 section.py references/project-types.md::"Games" references/design-system.md::"Style flavors"

Each pattern is a case-insensitive substring of a heading. A match prints the heading and
everything under it until the next heading of the same or a higher level. Several files and
patterns can be requested in one call, which is one tool call instead of several file reads.
"""
import re
import sys
from pathlib import Path

HEAD = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")


def sections(path):
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    heads, fenced = [], False
    for i, line in enumerate(lines):
        if line.strip().startswith("```"):
            fenced = not fenced
        m = None if fenced else HEAD.match(line)
        if m:
            heads.append((i, len(m.group(1)), m.group(2)))
    return lines, heads


def pull(path, pattern):
    lines, heads = sections(path)
    out = []
    for idx, (start, level, title) in enumerate(heads):
        if pattern.lower() in title.lower():
            end = len(lines)
            for s2, l2, _ in heads[idx + 1:]:
                if l2 <= level:
                    end = s2
                    break
            out.append("\n".join(lines[start:end]).rstrip())
    return out


def main(argv):
    if len(argv) >= 2 and argv[0] == "--list":
        _, heads = sections(argv[1])
        for _, level, title in heads:
            print("  " * (level - 1) + title)
        return 0
    if not argv:
        print(__doc__)
        return 2
    current = None
    status = 0
    for arg in argv:
        if "::" in arg:
            current, pat = arg.split("::", 1)
        elif current is None and Path(arg).is_file():
            current = arg
            continue
        else:
            pat = arg
        if current is None:
            print(f"No file given before pattern '{pat}'.", file=sys.stderr)
            return 2
        found = pull(current, pat.strip('"'))
        if not found:
            print(f"[no heading matching '{pat}' in {current}]", file=sys.stderr)
            status = 1
        for block in found:
            print(block + "\n")
    return status


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except BrokenPipeError:
        sys.exit(0)
