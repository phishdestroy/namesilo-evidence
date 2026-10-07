"""
Phish_Destroy archive — same structure as
github.com/phishdestroy/x-twitter-archive-CarlyGriggs13

Outputs (in ./out):
  webarchive.json          -- ["https://web.archive.org/web/0/https://twitter.com/Phish_Destroy/status/<ID>", ...]
  Phish_Destroy_tweets.csv -- tweet_id,text,language,type,bookmark_count,...,media_urls
  tweetfeed/               -- per-day JSON-Lines (tweetfeed/YYYY-MM-DD.jsonl)
  domains.json             -- extracted URLs/domains keyed by tweet_id
  inventory.json           -- master index of every archived snapshot we found
  missing.txt              -- tweet IDs that exist in inventory but no archive copy

Two-stage:
  Stage A (any IP) -- discovery via Wayback CDX, archive.today, GhostArchive, DDG
  Stage B (optional) -- live scrape via twscrape / snscrape if you have sock accounts
                        controlled with --live flag

Run from a clean IP. Wayback rate-limits aggressively; sleep_wayback is set to 8s.
"""
from __future__ import annotations
import argparse
import csv
import json
import re
import sys
import time
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

HANDLE = "Phish_Destroy"
OUT = Path(__file__).parent / "out"
OUT.mkdir(exist_ok=True)
(OUT / "tweetfeed").mkdir(exist_ok=True)
(OUT / "snapshots").mkdir(exist_ok=True)

UA = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/121.0 Safari/537.36"
    )
}
SLEEP_WAYBACK = 8.0
SLEEP_ARCHIVE = 4.0
SLEEP_DDG = 2.0


# --- helpers --------------------------------------------------------------

def http_get(url: str, sleep: float = 2.0, timeout: int = 60) -> bytes | None:
    time.sleep(sleep)
    try:
        with urlopen(Request(url, headers=UA), timeout=timeout) as r:
            return r.read()
    except HTTPError as e:
        print(f"  HTTP {e.code} on {url[:100]}")
    except URLError as e:
        print(f"  URLERR {e.reason} on {url[:100]}")
    except Exception as e:
        print(f"  ERR {e} on {url[:100]}")
    return None


def snowflake_to_iso(tweet_id: int) -> str:
    ms = (tweet_id >> 22) + 1288834974657
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).isoformat()


def extract_tweet_id(url: str | None) -> str | None:
    if not url:
        return None
    m = re.search(r'/status(?:es)?/(\d{15,20})', url)
    return m.group(1) if m else None


# --- discovery ------------------------------------------------------------

def discover_wayback(handle: str) -> list[dict]:
    found: dict[str, dict] = {}
    targets = [
        f"twitter.com/{handle}/status/*",
        f"x.com/{handle}/status/*",
        f"mobile.twitter.com/{handle}/status/*",
    ]
    for tgt in targets:
        url = (
            "https://web.archive.org/cdx/search/cdx?"
            f"url={urllib.parse.quote(tgt)}"
            "&output=json&fl=timestamp,original,statuscode,mimetype,digest"
            "&filter=statuscode:200&filter=mimetype:text/html&collapse=urlkey"
        )
        print(f"[wayback] {tgt}")
        body = http_get(url, sleep=SLEEP_WAYBACK, timeout=180)
        if not body:
            continue
        try:
            rows = json.loads(body)
        except Exception:
            print(f"  cdx not json: {body[:120]!r}")
            continue
        for ts, original, status, mime, digest in rows[1:]:
            tid = extract_tweet_id(original)
            if not tid:
                continue
            found.setdefault(tid, {
                "tweet_id": tid,
                "wayback_ts": ts,
                "wayback_url": f"https://web.archive.org/web/0/https://twitter.com/{handle}/status/{tid}",
                "wayback_snapshot": f"https://web.archive.org/web/{ts}id_/{original}",
                "original": original,
            })
    print(f"[wayback] {len(found)} tweet ids")
    return list(found.values())


def discover_archive_today(handle: str) -> list[dict]:
    """Best-effort. Will fail if Cloudflare blocks."""
    found: dict[str, dict] = {}
    for host in ("twitter.com", "x.com"):
        url = f"https://archive.ph/newest/https://{host}/{handle}"
        body = http_get(url, sleep=SLEEP_ARCHIVE, timeout=60)
        if not body:
            continue
        text = body.decode("utf-8", errors="ignore")
        if "One more step" in text or "challenge" in text.lower():
            print(f"[archive.today] {host}: cloudflare wall — skipping")
            continue
        for m in re.finditer(
            r'href="(https?://archive\.(?:ph|today|fo|li|md)/([A-Za-z0-9]{4,8}))"',
            text,
        ):
            full, code = m.group(1), m.group(2)
            window = text[max(0, m.start() - 200): m.end() + 200]
            orig_m = re.search(r'(https?://(?:twitter|x)\.com/\S+/status/\d+)', window)
            orig = orig_m.group(1) if orig_m else ""
            tid = extract_tweet_id(orig)
            if not tid:
                continue
            found.setdefault(tid, {
                "tweet_id": tid,
                "archive_today_code": code,
                "archive_today_url": full,
                "original": orig,
            })
    print(f"[archive.today] {len(found)} tweet ids")
    return list(found.values())


def discover_ddg(handle: str, max_pages: int = 20) -> list[dict]:
    """DDG HTML SERP — survives most rate limits."""
    found: dict[str, dict] = {}
    for q in (f"site:x.com {handle}", f"site:twitter.com {handle}"):
        for s in range(0, max_pages * 30, 30):
            url = (
                "https://html.duckduckgo.com/html/?"
                f"q={urllib.parse.quote(q)}&s={s}"
            )
            body = http_get(url, sleep=SLEEP_DDG, timeout=30)
            if not body:
                break
            text = body.decode("utf-8", errors="ignore")
            ids = re.findall(rf'{handle}[/%]2F?status[/%]2F?(\d{{15,20}})', text, flags=re.I)
            new = 0
            for tid in ids:
                if tid not in found:
                    found[tid] = {
                        "tweet_id": tid,
                        "ddg_seen": True,
                        "original": f"https://x.com/{handle}/status/{tid}",
                    }
                    new += 1
            print(f"[ddg] {q} s={s} -> +{new} (total {len(found)})")
            if new == 0:
                break
    print(f"[ddg] {len(found)} unique ids")
    return list(found.values())


# --- live scrape (optional, requires twscrape with sock accounts) --------

def live_scrape_twscrape(handle: str) -> list[dict] | None:
    """If twscrape is installed and configured, pull live profile."""
    try:
        import asyncio
        from twscrape import API  # type: ignore
    except ImportError:
        print("[live] twscrape not installed — skipping live scrape")
        print("       pip install twscrape  (and configure sock accounts)")
        return None

    async def run():
        api = API()
        out = []
        user = await api.user_by_login(handle)
        if not user:
            print(f"[live] cannot resolve user {handle}")
            return None
        async for t in api.user_tweets_and_replies(user.id, limit=10000):
            out.append({
                "tweet_id": str(t.id),
                "text": t.rawContent,
                "language": t.lang,
                "type": "Reply" if t.inReplyToTweetId else "Tweet",
                "bookmark_count": t.bookmarkCount or 0,
                "favorite_count": t.likeCount or 0,
                "retweet_count": t.retweetCount or 0,
                "reply_count": t.replyCount or 0,
                "view_count": t.viewCount or 0,
                "created_at": t.date.isoformat() if t.date else "",
                "client": t.sourceLabel or "",
                "hashtags": ",".join(f"#{h}" for h in (t.hashtags or [])),
                "urls": ",".join(u.expandedUrl for u in (t.urls or [])),
                "media_type": (t.media[0].type if t.media else ""),
                "media_urls": ",".join(getattr(m, "url", "") or getattr(m, "thumbnailUrl", "")
                                       for m in (t.media or [])),
            })
        return out

    try:
        return asyncio.run(run())
    except Exception as e:
        print(f"[live] twscrape failed: {e}")
        return None


# --- output writers -------------------------------------------------------

CSV_FIELDS = [
    "tweet_id", "text", "language", "type",
    "bookmark_count", "favorite_count", "retweet_count", "reply_count", "view_count",
    "created_at", "client", "hashtags", "urls", "media_type", "media_urls",
]


def write_csv(rows: list[dict], path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CSV_FIELDS, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        for r in rows:
            r2 = {k: r.get(k, "") for k in CSV_FIELDS}
            r2["tweet_id"] = f"'{r2['tweet_id']}'" if r2["tweet_id"] and not str(r2["tweet_id"]).startswith("'") else r2["tweet_id"]
            w.writerow(r2)
    print(f"[csv] {len(rows)} rows -> {path}")


def write_tweetfeed(rows: list[dict], dirpath: Path) -> None:
    by_day: dict[str, list[dict]] = {}
    for r in rows:
        ca = r.get("created_at", "")
        day = ca[:10] if ca else "unknown"
        by_day.setdefault(day, []).append(r)
    for day, items in by_day.items():
        with (dirpath / f"{day}.jsonl").open("w", encoding="utf-8") as f:
            for it in items:
                f.write(json.dumps(it, ensure_ascii=False) + "\n")
    print(f"[tweetfeed] {len(by_day)} day buckets -> {dirpath}")


def write_webarchive_json(tweet_ids: list[str], handle: str, path: Path) -> None:
    urls = [
        f"https://web.archive.org/web/0/https://twitter.com/{handle}/status/{tid}"
        for tid in sorted(tweet_ids)
    ]
    path.write_text(json.dumps(urls, indent=0))
    print(f"[webarchive.json] {len(urls)} urls -> {path}")


URL_RE = re.compile(r'https?://[^\s<>"]+')

def extract_domains_json(rows: list[dict], path: Path) -> None:
    dom = {}
    for r in rows:
        tid = r.get("tweet_id", "").strip("'")
        urls = URL_RE.findall(r.get("text", "") or "")
        urls += [u for u in (r.get("urls") or "").split(",") if u]
        if not urls:
            continue
        domains = []
        for u in urls:
            try:
                host = urllib.parse.urlparse(u).hostname or ""
                if host:
                    domains.append(host)
            except Exception:
                pass
        dom[tid] = {
            "tweet_id": tid,
            "urls": list(dict.fromkeys(urls)),
            "domains": list(dict.fromkeys(domains)),
            "created_at": r.get("created_at", ""),
        }
    path.write_text(json.dumps(dom, indent=2, ensure_ascii=False))
    print(f"[domains.json] {len(dom)} entries -> {path}")


# --- main -----------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--handle", default=HANDLE)
    ap.add_argument("--live", action="store_true",
                    help="also try live scrape via twscrape (needs sock accounts)")
    ap.add_argument("--no-archive-today", action="store_true",
                    help="skip archive.today (avoids Cloudflare delays)")
    ap.add_argument("--ddg-pages", type=int, default=20)
    args = ap.parse_args()

    # --- discovery ---
    rows: list[dict] = []
    rows += discover_wayback(args.handle)
    if not args.no_archive_today:
        rows += discover_archive_today(args.handle)
    rows += discover_ddg(args.handle, max_pages=args.ddg_pages)

    # merge by tweet_id, keep all source fields
    by_tweet: dict[str, dict] = {}
    for r in rows:
        tid = r.get("tweet_id")
        if not tid:
            continue
        if tid in by_tweet:
            by_tweet[tid].update({k: v for k, v in r.items() if v})
        else:
            by_tweet[tid] = dict(r)

    # add snowflake timestamps
    for tid, rec in by_tweet.items():
        try:
            rec["created_at_inferred"] = snowflake_to_iso(int(tid))
        except Exception:
            pass

    print(f"\n[stage A] {len(by_tweet)} unique tweet ids discovered")

    # --- live scrape if asked ---
    live_rows: list[dict] = []
    if args.live:
        scraped = live_scrape_twscrape(args.handle)
        if scraped:
            live_rows = scraped
            for r in live_rows:
                tid = r["tweet_id"]
                if tid in by_tweet:
                    by_tweet[tid].update(r)
                else:
                    by_tweet[tid] = dict(r)
            print(f"[stage B] +{len(live_rows)} live tweets")

    # --- write outputs ---
    all_rows = list(by_tweet.values())

    write_webarchive_json(list(by_tweet.keys()), args.handle, OUT / "webarchive.json")
    write_csv(all_rows, OUT / f"{args.handle}_tweets.csv")
    write_tweetfeed(all_rows, OUT / "tweetfeed")
    extract_domains_json(all_rows, OUT / "domains.json")

    # master inventory
    (OUT / "inventory.json").write_text(json.dumps({
        "handle": args.handle,
        "total_unique_tweets": len(by_tweet),
        "tweet_ids": sorted(by_tweet.keys()),
        "by_tweet": by_tweet,
    }, indent=2))
    print(f"[inventory.json] -> {OUT / 'inventory.json'}")

    missing = [
        tid for tid, r in by_tweet.items()
        if not r.get("wayback_snapshot") and not r.get("archive_today_url")
    ]
    if missing:
        (OUT / "missing.txt").write_text("\n".join(missing))
        print(f"[missing] {len(missing)} ids known but not archived anywhere")
        print(f"          run submit_missing.py to push them to Wayback + archive.ph")

    print("\ndone.")


if __name__ == "__main__":
    main()
