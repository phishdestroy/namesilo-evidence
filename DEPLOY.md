# Deploy guide — `namesilo-xmrwallet-coverup`

Two artifacts in this directory:

- **The repo itself** — README + supporting docs + `evidence/` — ready to push to GitHub.
- **`docs/`** — fully SEO-optimized static-site mirror, ready for GitHub Pages or any other static host.

---

## 1 · Push the repo

Recommended GitHub repo name: **`namesilo-xmrwallet-coverup`** (matches the URLs already baked into the docs).

```bash
cd proof-repo
git init -b main
git add .
git commit -m "Public release: NameSilo / xmrwallet evidence package"
git remote add origin git@github.com:phishdestroy/namesilo-xmrwallet-coverup.git
git push -u origin main
```

After the push:

1. **Repo description** (GitHub UI → About):
   > "A US ICANN-accredited registrar publicly defended xmrwallet.com — a 10-year, $20M Monero drainer — denied 20+ abuse reports, offered to scrub the operator's VirusTotal record, then used X Gold Checkmark support to silence our research. Evidence package, SHA-256 fingerprinted, court-usable."

2. **Repo topics** (GitHub UI → About → settings cog → Topics):
   ```
   namesilo  xmrwallet  monero  cryptocurrency-scam  registrar-abuse
   icann-compliance  phishing  threat-intelligence  evidence
   investigation  censorship  phishdestroy
   ```

3. **Social preview** (Settings → Social preview → Upload an image):
   Use `evidence/03-namesilo-statement-mar13.png`.

4. **Pin the README sections** in the order:
   `README.md` → `CONNECTION.md` → `THE-LIES.md` → `PRESSURE.md` → `EVIDENCE_INDEX.md`

---

## 2 · Enable GitHub Pages

The `docs/` folder is a self-contained static site.

GitHub repo → **Settings → Pages**:

- **Source:** Deploy from a branch
- **Branch:** `main`, folder: `/docs`
- **Save**.

Default URL: `https://phishdestroy.github.io/namesilo-xmrwallet-coverup/`

### Custom domain

Edit `docs/CNAME` (currently `namesilo-xmrwallet.phishdestroy.io`) to whatever subdomain you want. Add a CNAME record on your DNS pointing that subdomain at `phishdestroy.github.io`. Then in GitHub Pages settings, enable HTTPS.

---

## 3 · Verify integrity from a fresh clone

```bash
git clone https://github.com/phishdestroy/namesilo-xmrwallet-coverup.git
cd namesilo-xmrwallet-coverup/evidence
sha256sum -c ../EVIDENCE_HASHES.txt
```

All ten files should report `OK`.

---

## 4 · Push to web archives (after publication)

```bash
# Wayback Machine — submit the GitHub repo
curl -X POST "https://web.archive.org/save/https://github.com/phishdestroy/namesilo-xmrwallet-coverup"

# Wayback Machine — submit the GitHub Pages mirror
curl -X POST "https://web.archive.org/save/https://phishdestroy.github.io/namesilo-xmrwallet-coverup/"

# archive.today / archive.ph — manual: paste URL on https://archive.ph/
# GhostArchive — manual: paste URL on https://ghostarchive.org/
```

Repeat for each of the four MD documents (`CONNECTION.md`, `THE-LIES.md`, `PRESSURE.md`, `EVIDENCE_INDEX.md`) so each one has its own permanent archive URL. This is part of the Hydra principle: every document has at least three independent immutable copies.

---

## 5 · Canonical URL — what's already wired up

Throughout this build the canonical URL is `https://phishdestroy.io/namesilo-killed-our-twitter`. Every mirror points back to the main site.

If you don't want the GitHub Pages mirror to defer to phishdestroy.io, edit:

- `docs/index.html` → `<link rel="canonical">`, `og:url`, JSON-LD `@id` and `mainEntityOfPage`
- `docs/sitemap.xml` → `<loc>` and `<image:loc>` entries
- `docs/feed.xml` → `<link>` and `<guid>` entries
- `docs/robots.txt` → `Sitemap:` line

A simple search-and-replace on `https://phishdestroy.io/namesilo-killed-our-twitter` does the lot.

---

## 6 · Pin to IPFS & permanent decentralized storage

They are actively delisting us from Bing and trying to erase every surface. Decentralized/immutable storage is the counter.

### 6a · IPFS via web3.storage (free, no credit card)

```bash
# Install w3 CLI
npm install -g @web3-storage/w3cli

# Login (one-time, creates a DID)
w3 login your-email@phishdestroy.io

# Create a storage space
w3 space create phishdestroy-evidence

# Upload the evidence package
cd proof-repo
w3 up evidence/ PROOFS.md README.md CONNECTION.md THE-LIES.md PRESSURE.md \
   EVIDENCE_INDEX.md XMRWALLET_TECHNICAL.md ARTICLE_FULL.md SOURCES.md \
   EVIDENCE_HASHES.txt LICENSE
# Returns a CID like: bafybeig...

# The content is now at:
#   https://<CID>.ipfs.w3s.link/
#   https://dweb.link/ipfs/<CID>/
#   ipfs://<CID>/
```

Alternative: **Pinata** (pinata.cloud) — free tier, 1 GB, web UI upload.

```bash
# Or via Pinata CLI
npm install -g pinata-cli
pinata-cli upload ./evidence/
pinata-cli upload ./PROOFS.md
```

### 6b · Arweave (permanent, pay once, stored forever)

```bash
# Install arkb
npm install -g arkb

# Fund a wallet (needs ~0.01 AR, ~$0.15)
# Get AR from a faucet or buy on exchange

# Upload entire evidence directory
arkb deploy evidence/ --wallet /path/to/arweave-key.json
# Returns TX ID

# Upload key documents
arkb deploy PROOFS.md --wallet /path/to/arweave-key.json
arkb deploy README.md --wallet /path/to/arweave-key.json

# Content is permanent at:
#   https://arweave.net/<TX_ID>
```

Alternative: **Bundlr/Irys** (irys.xyz) — can pay with ETH/SOL/MATIC, easier onramp.

### 6c · Filecoin deals (redundant alongside IPFS)

If using web3.storage, content is automatically stored on Filecoin via storage deals. No extra steps needed — w3.storage handles the deal-making.

### 6d · Update PROOFS.md with CIDs

After pinning, add the IPFS CID and Arweave TX ID to:
- `PROOFS.md` section 12 (Permanent mirrors & IPFS)
- `README.md` mirrors section
- `docs/index.html` mirrors section

```bash
# Example — replace placeholder in PROOFS.md
sed -i 's/CID to be published after pinning/bafybeigXXXXXXXXXX/' PROOFS.md
sed -i 's/TX ID to be published after upload/ARWEAVE_TX_XXXXXX/' PROOFS.md
git add PROOFS.md README.md
git commit -m "Add IPFS CID and Arweave TX ID to mirrors"
git push
```

### 6e · Git mirrors — different jurisdictions

```bash
# === Codeberg (Germany — DMCA doesn't apply) ===
# Create account at codeberg.org, then:
cd proof-repo
git remote add codeberg https://codeberg.org/phishdestroy/namesilo-xmrwallet-coverup.git
git push codeberg main

# === GitLab (Netherlands — different company, different legal) ===
git remote add gitlab https://gitlab.com/phishdestroy/namesilo-xmrwallet-coverup.git
git push gitlab main

# === SourceHut (indie, minimal, owner-operated) ===
git remote add sourcehut git@git.sr.ht:~phishdestroy/namesilo-xmrwallet-coverup
git push sourcehut main

# === Radicle (P2P git — no central server at all) ===
# Install: https://radicle.xyz
rad init
rad push
# Share the Radicle ID — anyone can clone without a server
```

### 6f · Blockchain publishing

```bash
# === Mirror.xyz (article on Ethereum — permanent, no takedowns) ===
# 1. Go to mirror.xyz
# 2. Connect wallet
# 3. Paste ARTICLE_FULL.md content
# 4. Publish — it's on-chain forever
# 5. Save the Mirror URL in PROOFS.md

# === Nostr (decentralized social — no moderation) ===
# Install a Nostr client (e.g. Damus, Amethyst, or nostril CLI)
# Publish key evidence as notes:
#   - The connection paragraph from README
#   - The 4 lies table
#   - Links to IPFS CID and GitHub
#   - Tag: #namesilo #xmrwallet #cryptoscam #phishdestroy

# === HackerNoon ===
# Submit ARTICLE_FULL.md via hackernoon.com/signup
# HackerNoon uses blockchain-backed publishing — content is persistent
```

### 6g · Publishing platforms

```bash
# === dev.to ===
# article.devto.md is ready — paste into dev.to editor
# Canonical URL already set to Medium article

# === HackerNoon ===
# Submit via hackernoon.com — they review within 24-48h
# Blockchain-backed, harder to suppress than Medium

# === Reddit ===
# Post to r/CryptoCurrency, r/Monero, r/cybersecurity, r/privacy
# Link to GitHub repo + PROOFS.md
# Reddit posts get indexed by Google fast
```

### 6h · Community mirroring instructions

Anyone can re-pin to their own IPFS node:

```bash
# Pin our CID on your own node
ipfs pin add <CID>

# Or via a pinning service
curl -X POST "https://api.pinata.cloud/pinning/pinByHash" \
  -H "Authorization: Bearer YOUR_JWT" \
  -d '{"hashToPin": "<CID>"}'
```

The more nodes pin the CID, the harder it is to take down. **Each pin is free. Each pin is permanent.**

---

## 7 · Mass archive submission (after publication)

```bash
# === Wayback Machine ===
URLS=(
  "https://github.com/phishdestroy/namesilo-xmrwallet-coverup"
  "https://github.com/phishdestroy/namesilo-xmrwallet-coverup/blob/main/PROOFS.md"
  "https://github.com/phishdestroy/namesilo-xmrwallet-coverup/blob/main/CONNECTION.md"
  "https://github.com/phishdestroy/namesilo-xmrwallet-coverup/blob/main/THE-LIES.md"
  "https://github.com/phishdestroy/namesilo-xmrwallet-coverup/blob/main/PRESSURE.md"
  "https://github.com/phishdestroy/namesilo-xmrwallet-coverup/blob/main/EVIDENCE_INDEX.md"
  "https://github.com/phishdestroy/namesilo-xmrwallet-coverup/blob/main/ARTICLE_FULL.md"
  "https://github.com/phishdestroy/namesilo-xmrwallet-coverup/blob/main/XMRWALLET_TECHNICAL.md"
  "https://phishdestroy.github.io/namesilo-xmrwallet-coverup/"
  "https://phishdestroy.io/namesilo-killed-our-twitter"
  "https://phishdestroy.io/xmrwallet-namesilo-exposed"
  "https://phishdestroy.medium.com/namesilo-lied-to-defend-a-20m-crypto-scam-then-took-down-our-twitter-4904d15d531e"
  "https://phishdestroy.medium.com/xmrwallet-com-2953f35b8a79"
)

for url in "${URLS[@]}"; do
  echo "Saving: $url"
  curl -s -o /dev/null "https://web.archive.org/save/$url"
  sleep 2
done

# === archive.today ===
# Manual: paste each URL at https://archive.ph/
# Or use the bookmarklet/API if available

# === GhostArchive ===
# Manual: paste each URL at https://ghostarchive.org/
```

---

## 8 · After-publication checklist

Once the repo is live and the GitHub Pages mirror resolves:

**Archives:**
- [ ] Run mass archive submission script (step 7)
- [ ] Submit all URLs to archive.ph (manual)
- [ ] Submit all URLs to GhostArchive (manual)

**IPFS / permanent storage:**
- [ ] Pin to IPFS via web3.storage (step 6a) — record CID
- [ ] Upload to Arweave (step 6b) — record TX ID
- [ ] Update PROOFS.md, README.md, docs/index.html with CID and TX ID
- [ ] Commit and push the CID/TX update
- [ ] Post CID on phishdestroy.io so community can re-pin

**SEO & indexing:**
- [ ] Add the GitHub repo URL to `phishdestroy.io/namesilo-killed-our-twitter` as a "GitHub mirror" link
- [ ] Add the GitHub repo URL to the Medium article (canonical_url tag pointing to phishdestroy.io)
- [ ] Verify Open Graph preview at:
  - https://opengraph.dev/?url=https://phishdestroy.github.io/namesilo-xmrwallet-coverup/
  - https://cards-dev.twitter.com/validator
  - https://www.opengraph.xyz/
- [ ] Submit the sitemap to Google Search Console: `https://phishdestroy.io/namesilo-killed-our-twitter/sitemap.xml`
- [ ] Submit the sitemap to Bing Webmaster Tools (fight the delisting)
- [ ] Submit a news-feed indexing request via Google News Publisher Center (the sitemap includes `<news:news>` markup)
- [ ] File Bing Webmaster Tools dispute if delisting requests are visible

**Community:**
- [ ] Post IPFS CID in README so anyone can re-pin
- [ ] Add "How to mirror" section to phishdestroy.io with instructions
- [ ] Share IPFS gateway links on Reddit/HN/security forums

---

## 9 · What's intentionally NOT in this repo

- Internal hosting credentials (Screenshot_12, Screenshot_13 from the working tree)
- Internal email-analysis dashboard (Screenshot_14 from the working tree)
- A low-resolution thumbnail (Screenshot_9)
- Operational data from the parent `backup/` folder (raw Wayback CDX dumps, archive.today crawler scripts) — that's tooling, not evidence.

If any of those need to go public later, do it as a separate, deliberate commit — never `git add -A` from the parent directory.

The full email thread with the operator (including the Feb 17 *"Feel free to subpoena the domain registrar"* line) is preserved in raw form, not published, and is available to ICANN Compliance and law enforcement on request.
