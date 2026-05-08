#!/usr/bin/env bash
# Pin evidence to IPFS via web3.storage
# Run: bash tools/pin-ipfs.sh
set -euo pipefail

echo "=== IPFS Pin: namesilo-xmrwallet-coverup ==="
echo ""

# Check if w3 CLI installed
if ! command -v w3 &>/dev/null; then
  echo "[!] w3 CLI not found. Installing..."
  npm install -g @web3-storage/w3cli
fi

# Check login
echo "[*] Checking w3 auth..."
w3 whoami 2>/dev/null || {
  echo "[!] Not logged in. Run: w3 login your-email@phishdestroy.io"
  echo "[!] Then: w3 space create phishdestroy-evidence"
  exit 1
}

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "[*] Pinning evidence directory..."
EVIDENCE_CID=$(w3 up "$REPO_ROOT/evidence/" 2>&1 | tail -1)
echo "[+] evidence/ CID: $EVIDENCE_CID"

echo "[*] Pinning key documents..."
KEY_CID=$(w3 up \
  "$REPO_ROOT/PROOFS.md" \
  "$REPO_ROOT/README.md" \
  "$REPO_ROOT/ARTICLE_FULL.md" \
  "$REPO_ROOT/CONNECTION.md" \
  "$REPO_ROOT/THE-LIES.md" \
  "$REPO_ROOT/PRESSURE.md" \
  "$REPO_ROOT/SCAM_TECHNICAL.md" \
  "$REPO_ROOT/OPERATOR_PROFILE.md" \
  "$REPO_ROOT/VICTIMS.md" \
  "$REPO_ROOT/XMRWALLET_TECHNICAL.md" \
  "$REPO_ROOT/EVIDENCE_INDEX.md" \
  "$REPO_ROOT/SOURCES.md" \
  "$REPO_ROOT/EVIDENCE_HASHES.txt" \
  "$REPO_ROOT/LICENSE" \
  2>&1 | tail -1)
echo "[+] docs CID: $KEY_CID"

echo ""
echo "=== DONE ==="
echo ""
echo "Evidence: https://${EVIDENCE_CID}.ipfs.w3s.link/"
echo "Docs:     https://${KEY_CID}.ipfs.w3s.link/"
echo "IPFS:     ipfs://${EVIDENCE_CID}/"
echo "dweb:     https://dweb.link/ipfs/${EVIDENCE_CID}/"
echo ""
echo "UPDATE these in PROOFS.md section 12 and README.md mirrors section."
echo "Anyone can re-pin: ipfs pin add ${EVIDENCE_CID}"
