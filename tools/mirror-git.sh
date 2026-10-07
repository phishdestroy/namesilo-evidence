#!/usr/bin/env bash
# Push repo to all git mirrors (different jurisdictions)
# Run after initial GitHub push: bash tools/mirror-git.sh
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

echo "=== Git Mirror Push ==="
echo ""

# Codeberg (Germany)
echo "[*] Codeberg (Germany — DMCA doesn't apply)..."
if git remote get-url codeberg &>/dev/null; then
  git push codeberg main
else
  echo "    Add remote first:"
  echo "    1. Create repo at https://codeberg.org/new"
  echo "    2. git remote add codeberg https://codeberg.org/phishdestroy/namesilo-xmrwallet-coverup.git"
  echo "    3. git push codeberg main"
fi
echo ""

# GitLab (Netherlands)
echo "[*] GitLab (Netherlands — different company)..."
if git remote get-url gitlab &>/dev/null; then
  git push gitlab main
else
  echo "    Add remote first:"
  echo "    1. Create repo at https://gitlab.com/projects/new"
  echo "    2. git remote add gitlab https://gitlab.com/phishdestroy/namesilo-xmrwallet-coverup.git"
  echo "    3. git push gitlab main"
fi
echo ""

# SourceHut
echo "[*] SourceHut (indie, owner-operated)..."
if git remote get-url sourcehut &>/dev/null; then
  git push sourcehut main
else
  echo "    Add remote first:"
  echo "    1. Create repo at https://sr.ht/projects/create"
  echo "    2. git remote add sourcehut git@git.sr.ht:~phishdestroy/namesilo-xmrwallet-coverup"
  echo "    3. git push sourcehut main"
fi
echo ""

echo "=== Done ==="
echo "Repo now exists in multiple jurisdictions."
echo "They'd need separate legal actions in US, Germany, Netherlands to take down all copies."
