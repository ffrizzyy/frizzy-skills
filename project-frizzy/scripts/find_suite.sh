#!/usr/bin/env bash
# Prints where each sibling field skill is installed, or "missing".
# Read-only. Usage: bash find_suite.sh
dirs=("/mnt/skills/user" "/mnt/skills/examples" "$HOME/.claude/skills" "./.claude/skills" "$HOME/.agents/skills" "./.agents/skills")
for name in frizzy-design frizzy-stack frizzy-security frizzy-test frizzy-ship; do
  hit=""
  for d in "${dirs[@]}"; do
    [ -f "$d/$name/SKILL.md" ] && { hit="$d/$name"; break; }
  done
  echo "$name: ${hit:-missing}"
done
