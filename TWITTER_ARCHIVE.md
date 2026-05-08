# @Phish_Destroy Twitter Archive — Methodology

> **The @Phish_Destroy account is locked. The tweets are invisible from the account itself. None of them are gone.**

This document explains how the public posts of @Phish_Destroy were archived, in real time, across multiple independent services — so that the rebuttals to NameSilo's March 13 statement remain permanently retrievable even though the account that published them has been silenced.

---

## Why this archive exists

On the day NameSilo published their public defense of `xmrwallet[.]com`, we did three things in parallel:

1. **Posted the rebuttals.** Citing the operator's own emails as proof.
2. **Submitted each post to the Wayback Machine the moment it went live.** No tweet was published without being permanently archived within minutes.
3. **Notarized our prediction in GhostArchive** that NameSilo would attempt to silence us via X's paid Gold Checkmark support channel — *before* the lock dropped.

When the lock did drop, on schedule, every rebuttal was already preserved in at least two independent archives.

The same methodology is being applied to NameSilo's official Twitter feed, ICANN's compliance bulletins, and any Medium article in the case file that NameSilo or its allies might attempt to take down.

---

## Discovery sources

The reproducible tooling (in [`tools/`](tools/)) queries each of the following sources independently, then merges the results by tweet ID. Any one of them going dark does not break the archive.

### 1. Wayback Machine CDX

The Internet Archive's CDX index is the canonical source. It returns every snapshot of every Twitter URL the Archive has ever ingested.

```text
https://web.archive.org/cdx/search/cdx
  ?url=twitter.com/Phish_Destroy/status/*
  &output=json
  &fl=timestamp,original,statuscode,mimetype,digest
  &filter=statuscode:200
  &filter=mimetype:text/html
  &collapse=urlkey
```

Same query is run for `x.com/Phish_Destroy/status/*` and `mobile.twitter.com/Phish_Destroy/status/*`. Results are merged by Snowflake-decoded tweet ID.

### 2. archive.today / archive.ph

archive.today is a separately-operated archive service that has historically captured Twitter content even when Wayback was rate-limited or blocked. The discovery URL is:

```text
https://archive.ph/newest/https://x.com/Phish_Destroy
https://archive.ph/newest/https://twitter.com/Phish_Destroy
```

The HTML response contains short codes (e.g. `archive.ph/abcde`) that resolve to immutable snapshots.

### 3. GhostArchive

GhostArchive is a third independent archive specialising in social media. It is currently our highest-confidence channel for tweets that quote NameSilo, because it is the channel where NameSilo's own March 13 statement was preserved before the noise around the case forced any service to make rate-limit decisions.

### 4. DuckDuckGo HTML SERP

For tweet ID *discovery* (not preservation), the DDG HTML search-results page survives most rate limits and returns canonical Twitter URLs:

```text
https://html.duckduckgo.com/html/?q=site:x.com+Phish_Destroy
https://html.duckduckgo.com/html/?q=site:twitter.com+Phish_Destroy
```

Pagination via `&s=30, &s=60, …` until a page returns no new IDs.

### 5. Live scrape (optional, requires sock accounts)

If `twscrape` is installed and configured with sock accounts, full tweet text, like / retweet / view counts, and media URLs can be pulled directly. This step is optional — the four archive sources above are sufficient to prove existence and capture content without it.

---

## Outputs

The tooling in [`tools/inventory.py`](tools/inventory.py) produces a structure intentionally identical to the public archive published for the @CarlyGriggs13 case (a precedent reference for archive structure):

```
out/
├── webarchive.json          ["https://web.archive.org/web/0/.../<id>", …]
├── Phish_Destroy_tweets.csv tweet_id, text, language, type, like_count, …, media_urls
├── tweetfeed/               YYYY-MM-DD.jsonl per-day buckets
├── snapshots/               (reserved for direct HTML pulls)
├── domains.json             {tweet_id: {urls, domains, created_at}}
├── inventory.json           master index of every snapshot found
└── missing.txt              tweet IDs known but not yet archived anywhere
```

`missing.txt` is the work queue. [`tools/submit_missing.py`](tools/submit_missing.py) reads it and POSTs each ID to:

```
https://web.archive.org/save/https://twitter.com/Phish_Destroy/status/<ID>
https://archive.ph/?url=https%3A%2F%2Fx.com%2FPhish_Destroy%2Fstatus%2F<ID>
```

Wayback rate-limits to roughly one save per 8 seconds. archive.ph is harder to script and works best from a clean residential IP.

---

## Re-running the archive

```bash
cd proof-repo/tools
python3 inventory.py --handle Phish_Destroy --no-archive-today --ddg-pages 30
# Produces ./out/

python3 submit_missing.py < out/missing.txt
# Pushes any tweet ID we found a reference to but no archive copy of.
```

`--no-archive-today` skips the archive.ph discovery step (which gets blocked by Cloudflare a non-trivial fraction of the time); the Wayback CDX + DDG combination still covers most of the corpus.

---

## Specific tweets preserved in this repository

In addition to the algorithmic archive above, the following four tweets are preserved as **screenshots in `evidence/`** because they are central to the case and should be retrievable without dependence on any third-party archive at all:

- [`04-tweet-namesilo-is-lying.png`](evidence/04-tweet-namesilo-is-lying.png)
- [`04-tweet-press-secretary.png`](evidence/04-tweet-press-secretary.png)
- [`04-tweet-honest-question.png`](evidence/04-tweet-honest-question.png)
- [`04-tweet-cryptopus-quote.png`](evidence/04-tweet-cryptopus-quote.png)

Each is SHA-256 fingerprinted in [`EVIDENCE_HASHES.txt`](EVIDENCE_HASHES.txt). The screenshots are the canonical court-usable copies; the algorithmic archive is the breadth-first redundancy layer.

---

## Why this matters for the broader investigation

Once a registrar starts using paid platform-level access to silence security researchers, **the registrar is implicitly admitting that the silencing is more important to them than the underlying technical dispute**. NameSilo's path of least resistance, on a tweet they disagreed with, was:

- Pay nothing → use X's regular report button.
- Pay nothing extra → file an ICANN-style abuse complaint at PhishDestroy's hosting layer.
- Pay nothing extra → write a public reply contesting the technical findings.

They did none of those. They used the **paid Gold Checkmark live-support channel** that goes directly to a human moderator at X. That channel exists precisely because it bypasses the normal checks. Its weaponisation for silencing is the story.

The archive in this directory is what makes that story permanent.

---

## A note on responsible disclosure of the archive itself

The archive contains only **publicly published material** — tweets that were on a public account at the time of capture. No private DMs, no protected tweets, no scraped data from private profiles.

If at any point @Phish_Destroy is restored and the account holder asks for specific archived tweets to be redacted, requests will be honoured for posts that:

- Reveal personal information that should not have been published the first time, or
- Were drafts inadvertently posted and immediately deleted.

Posts about NameSilo and `xmrwallet[.]com` will not be redacted on request. They are part of an ongoing public-interest investigation and an ICANN compliance matter.
