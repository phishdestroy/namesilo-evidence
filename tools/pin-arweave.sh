#!/usr/bin/env bash
# Upload evidence to Arweave (permanent, pay once, no takedowns)
# Run: bash tools/pin-arweave.sh
set -euo pipefail

echo "=== Arweave Upload: namesilo-xmrwallet-coverup ==="
echo ""

# Check arkb
if ! command -v arkb &>/dev/null; then
  echo "[!] arkb not found. Installing..."
  npm install -g arkb
fi

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WALLET="${ARWEAVE_WALLET:-$HOME/.arweave/wallet.json}"

if [ ! -f "$WALLET" ]; then
  echo "[!] Arweave wallet not found at $WALLET"
  echo "[!] Get one at: https://arweave.app or https://faucet.arweave.net"
  echo "[!] Set ARWEAVE_WALLET=/path/to/key.json and re-run"
  exit 1
fi

echo "[*] Uploading evidence/..."
arkb deploy "$REPO_ROOT/evidence/" --wallet "$WALLET" --tag-name "App-Name" --tag-value "PhishDestroy-Evidence"
echo ""

echo "[*] Uploading PROOFS.md..."
arkb deploy "$REPO_ROOT/PROOFS.md" --wallet "$WALLET" --tag-name "Content-Type" --tag-value "text/markdown"

echo "[*] Uploading README.md..."
arkb deploy "$REPO_ROOT/README.md" --wallet "$WALLET" --tag-name "Content-Type" --tag-value "text/markdown"

echo "[*] Uploading OPERATOR_PROFILE.md..."
arkb deploy "$REPO_ROOT/OPERATOR_PROFILE.md" --wallet "$WALLET" --tag-name "Content-Type" --tag-value "text/markdown"

echo "[*] Uploading SCAM_TECHNICAL.md..."
arkb deploy "$REPO_ROOT/SCAM_TECHNICAL.md" --wallet "$WALLET" --tag-name "Content-Type" --tag-value "text/markdown"

echo "[*] Uploading VICTIMS.md..."
arkb deploy "$REPO_ROOT/VICTIMS.md" --wallet "$WALLET" --tag-name "Content-Type" --tag-value "text/markdown"

echo ""
echo "=== DONE ==="
echo "TX IDs above. Content at: https://arweave.net/<TX_ID>"
echo "UPDATE PROOFS.md section 12 with TX IDs."
echo "This is PERMANENT. No takedowns. No deletions. Ever."
