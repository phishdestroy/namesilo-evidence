#!/usr/bin/env bash
# Submit ALL URLs to Wayback Machine + print archive.today links
# Run after GitHub push: bash tools/archive-all.sh
set -euo pipefail

echo "=== Mass Archive Submission ==="
echo ""

URLS=(
  # GitHub
  "https://github.com/phishdestroy/namesilo-xmrwallet-coverup"
  "https://github.com/phishdestroy/namesilo-xmrwallet-coverup/blob/main/PROOFS.md"
  "https://github.com/phishdestroy/namesilo-xmrwallet-coverup/blob/main/README.md"
  "https://github.com/phishdestroy/namesilo-xmrwallet-coverup/blob/main/CONNECTION.md"
  "https://github.com/phishdestroy/namesilo-xmrwallet-coverup/blob/main/THE-LIES.md"
  "https://github.com/phishdestroy/namesilo-xmrwallet-coverup/blob/main/PRESSURE.md"
  "https://github.com/phishdestroy/namesilo-xmrwallet-coverup/blob/main/ARTICLE_FULL.md"
  "https://github.com/phishdestroy/namesilo-xmrwallet-coverup/blob/main/SCAM_TECHNICAL.md"
  "https://github.com/phishdestroy/namesilo-xmrwallet-coverup/blob/main/OPERATOR_PROFILE.md"
  "https://github.com/phishdestroy/namesilo-xmrwallet-coverup/blob/main/VICTIMS.md"
  "https://github.com/phishdestroy/namesilo-xmrwallet-coverup/blob/main/XMRWALLET_TECHNICAL.md"
  "https://github.com/phishdestroy/namesilo-xmrwallet-coverup/blob/main/EVIDENCE_INDEX.md"
  # GitHub Pages
  "https://phishdestroy.github.io/namesilo-xmrwallet-coverup/"
  # PhishDestroy.io
  "https://phishdestroy.io/namesilo-killed-our-twitter"
  "https://phishdestroy.io/xmrwallet-namesilo-exposed"
  # Medium
  "https://phishdestroy.medium.com/namesilo-lied-to-defend-a-20m-crypto-scam-then-took-down-our-twitter-4904d15d531e"
  "https://phishdestroy.medium.com/xmrwallet-com-2953f35b8a79"
  # Other GitHub repo
  "https://github.com/phishdestroy/DO-NOT-USE-xmrwallet-com"
  # Git mirrors (add after creating)
  # "https://codeberg.org/phishdestroy/namesilo-xmrwallet-coverup"
  # "https://gitlab.com/phishdestroy/namesilo-xmrwallet-coverup"
)

echo "[*] Submitting ${#URLS[@]} URLs to Wayback Machine..."
echo ""

for url in "${URLS[@]}"; do
  echo "  -> $url"
  curl -s -o /dev/null -w "     HTTP %{http_code}\n" \
    "https://web.archive.org/save/$url" \
    -H 'User-Agent: PhishDestroy-Archive/1.0' \
    --max-time 30 || echo "     FAILED (timeout/error)"
  sleep 8
done

echo ""
echo "=== Wayback done ==="
echo ""
echo "=== Now manually submit to archive.today ==="
echo "Open https://archive.ph/ and paste each URL:"
echo ""
for url in "${URLS[@]}"; do
  echo "  $url"
done

echo ""
echo "=== And GhostArchive ==="
echo "Open https://ghostarchive.org/ and paste key URLs."
echo ""
echo "Done. Every URL now has at least 1 immutable copy."
