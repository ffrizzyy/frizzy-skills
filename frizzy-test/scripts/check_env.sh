#!/usr/bin/env bash
# project-frizzy environment check.
# Prints "key: value" lines. Read-only: it never installs or changes anything.
# Usage: bash check_env.sh

set -u

have() { command -v "$1" >/dev/null 2>&1; }
first_line() { head -n1 | tr -d '\r'; }

echo "date: $(date +%F)"
echo "os: $(uname -s 2>/dev/null) $(uname -m 2>/dev/null)"

# A claude.ai container is not the person's machine. Installing here helps nobody.
if [ -d /mnt/user-data ]; then
  echo "sandbox: yes (claude.ai container; installs here do not reach the person's machine)"
else
  echo "sandbox: no"
fi

# Core tooling
for tool in node npm pnpm git python3; do
  if have "$tool"; then
    echo "$tool: $("$tool" --version 2>/dev/null | first_line)"
  else
    echo "$tool: missing"
  fi
done

if have node; then
  major=$(node -v 2>/dev/null | sed 's/^v//' | cut -d. -f1)
  if [ -n "${major:-}" ] && [ "$major" -ge 18 ] 2>/dev/null; then
    echo "node_ok_for_playwright_cli: yes (needs 18 or newer)"
  else
    echo "node_ok_for_playwright_cli: no (needs 18 or newer)"
  fi
fi

# Network reachability decides whether an install is even possible.
if have curl; then
  if timeout 4 curl -sS -o /dev/null -I https://registry.npmjs.org 2>/dev/null; then
    echo "network_npm_registry: reachable"
  else
    echo "network_npm_registry: blocked or offline"
  fi
else
  echo "network_npm_registry: unknown (curl missing)"
fi

# playwright-cli (github.com/microsoft/playwright-cli, package @playwright/cli)
if have playwright-cli; then
  v=$(playwright-cli --version 2>/dev/null | first_line)
  echo "playwright-cli: installed (${v:-version unknown})"
elif have npx && timeout 20 npx --no-install playwright --version >/dev/null 2>&1; then
  v=$(timeout 20 npx --no-install playwright --version 2>/dev/null | first_line)
  # Older Playwright releases have no "cli" subcommand and print generic help instead.
  if timeout 20 npx --no-install playwright cli --help 2>&1 | grep -qi "snapshot"; then
    echo "playwright-cli: available through local playwright (${v:-version unknown}); run 'npx playwright cli ...'"
  else
    echo "playwright-cli: missing (a Playwright library exists, ${v:-version unknown}, but it has no cli subcommand)"
  fi
else
  echo "playwright-cli: missing"
fi

# Skills this workflow can lean on. Search the usual locations.
dirs=(
  "$HOME/.claude/skills" "./.claude/skills"
  "$HOME/.agents/skills" "./.agents/skills"
  "/mnt/skills/public" "/mnt/skills/examples" "/mnt/skills/plugins"
)

find_skill() {
  local name="$1" d hit
  for d in "${dirs[@]}"; do
    [ -d "$d" ] || continue
    hit=$(find "$d" -maxdepth 2 -type d \( -name "$name" -o -name "*:$name" \) 2>/dev/null | head -n1)
    if [ -n "$hit" ]; then echo "$hit"; return 0; fi
  done
  return 1
}

for s in humanizer design-taste-frontend emil-design-eng animate pick-ui-library playwright-cli security-audit ponytail caveman superpowers graphify; do
  if path=$(find_skill "$s"); then
    echo "skill $s: found ($path)"
  else
    echo "skill $s: missing"
  fi
done

if have graphify; then echo "graphify cli: installed"; fi
echo "install hints:"
echo "  playwright-cli: npm install -g @playwright/cli@latest && playwright-cli install --skills"
echo "  emil skills:    npx skills@latest add emilkowalski/skills"
echo "  taste skill:    npx skills add https://github.com/Leonxlnx/taste-skill --skill \"design-taste-frontend\""
echo "  build kit:      see references/ecosystem.md (ponytail, caveman, superpowers, graphify). Ask before installing; official sources only."
echo "  security audit: npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit   (needs parallel sub-agents, Node.js, and a sandbox; token-heavy, so ask first)"
