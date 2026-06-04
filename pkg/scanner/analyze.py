"""
Analysis of scan results.
Produces concrete counts: how many dead, parking, duplicates, and placeholder pages.
"""
import json
import sys
import gzip
from collections import Counter, defaultdict
from pathlib import Path

import boto3
from config import S3_BUCKET, AWS_REGION

s3 = boto3.client("s3", region_name=AWS_REGION)
LOCAL_CACHE = Path("E:/namesilo-scanner/results_cache")
LOCAL_CACHE.mkdir(exist_ok=True)


def download_results(prefix="scans/") -> list[Path]:
    paginator = s3.get_paginator("list_objects_v2")
    files = []
    for page in paginator.paginate(Bucket=S3_BUCKET, Prefix=prefix):
        for obj in page.get("Contents", []):
            key = obj["Key"]
            local = LOCAL_CACHE / key.replace("/", "_")
            if not local.exists():
                print(f"  ↓ {key} ({obj['Size']//1024}KB)")
                s3.download_file(S3_BUCKET, key, str(local))
            files.append(local)
    return files


def load_records(files: list[Path]):
    for f in files:
        opener = gzip.open if str(f).endswith(".gz") else open
        with opener(f, "rt", encoding="utf-8", errors="replace") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    try:
                        yield json.loads(line)
                    except json.JSONDecodeError:
                        pass


def analyze(files: list[Path] = None):
    if files is None:
        print("Downloading from S3...")
        files = download_results()

    print(f"Analyzing {len(files)} result files...\n")

    # Counters
    page_types          = Counter()
    parking_services    = Counter()
    error_types         = Counter()
    redirect_targets    = Counter()
    favicon_clusters    = Counter()
    simhash_clusters    = Counter()
    title_clusters      = Counter()
    server_fp_clusters  = Counter()
    word_count_buckets  = Counter()
    body_size_buckets   = Counter()
    tls_cn_counter      = Counter()
    generator_counter   = Counter()
    cloudflare_count    = 0
    cookie_count        = 0

    domains_by_favicon  = defaultdict(list)
    domains_by_simhash  = defaultdict(list)
    domains_by_title    = defaultdict(list)   # title_md5 → examples
    title_text          = {}                  # title_md5 → the title string itself
    for_sale_examples   = []
    parking_examples    = defaultdict(list)
    redirect_examples   = []

    total = scanned = errors = 0

    for rec in load_records(files):
        total += 1

        if rec.get("error"):
            errors += 1
            err = rec["error"]
            # Normalize error type
            if "timed out" in err or "timeout" in err.lower():
                error_types["timeout"] += 1
            elif "refused" in err:
                error_types["connection_refused"] += 1
            elif "Name or service" in err or "NXDOMAIN" in err:
                error_types["dns_fail"] += 1
            elif "SSL" in err or "certificate" in err.lower():
                error_types["ssl_error"] += 1
            else:
                error_types["other"] += 1
            continue

        scanned += 1
        pt = rec.get("page_type", "unknown")
        page_types[pt] += 1

        # Parking service
        ps = rec.get("parking_service", "")
        if ps:
            parking_services[ps] += 1

        # Parking examples
        if pt == "parking" and len(parking_examples[ps]) < 5:
            parking_examples[ps].append(f"{rec['domain']} | {rec.get('title','')[:60]}")

        # For-sale examples
        if pt == "for_sale" and len(for_sale_examples) < 20:
            for_sale_examples.append(f"{rec['domain']} | {rec.get('title','')[:60]}")

        # Redirects
        if rec.get("redirected_away"):
            fd = rec.get("final_domain", "")
            redirect_targets[fd] += 1
            if len(redirect_examples) < 50:
                redirect_examples.append(f"{rec['domain']} → {rec.get('final_url','')[:80]}")

        # Favicon clusters (non-standard favicons only)
        mmh3 = rec.get("favicon_mmh3")
        if mmh3 and mmh3 not in (0, -1, None):
            favicon_clusters[mmh3] += 1
            if len(domains_by_favicon[mmh3]) < 5:
                domains_by_favicon[mmh3].append(rec["domain"])

        # SimHash clusters
        sh = rec.get("body_simhash", "")
        if sh and sh != "0" * 16:
            simhash_clusters[sh] += 1
            if len(domains_by_simhash[sh]) < 5:
                domains_by_simhash[sh].append(rec["domain"])

        # Title clusters (exact duplicates by page title)
        tm = rec.get("title_md5", "")
        t  = rec.get("title", "")
        if tm and t and t.lower() not in ("", "untitled"):
            title_clusters[tm] += 1
            title_text[tm] = t
            if len(domains_by_title[tm]) < 5:
                domains_by_title[tm].append(rec["domain"])

        # Server fingerprint
        sfp = rec.get("server_fp", "")
        if sfp:
            server_fp_clusters[sfp] += 1

        # Cloudflare / cookies
        if rec.get("is_cloudflare"):
            cloudflare_count += 1
        if rec.get("has_set_cookie"):
            cookie_count += 1

        # Word count
        wc = rec.get("word_count", 0)
        if wc == 0:          word_count_buckets["0 words"] += 1
        elif wc < 20:        word_count_buckets["1-19 words"] += 1
        elif wc < 50:        word_count_buckets["20-49 words"] += 1
        elif wc < 200:       word_count_buckets["50-199 words"] += 1
        else:                word_count_buckets["200+ words"] += 1

        # Body size
        bs = rec.get("body_size", 0)
        if bs < 500:         body_size_buckets["<500B"] += 1
        elif bs < 2048:      body_size_buckets["<2KB"] += 1
        elif bs < 10240:     body_size_buckets["<10KB"] += 1
        else:                body_size_buckets["10KB+"] += 1

        # TLS
        cn = rec.get("tls_cn", "")
        if cn:
            tls_cn_counter[cn] += 1

        gen = rec.get("meta_generator", "")
        if gen:
            generator_counter[gen[:50]] += 1

        if total % 200_000 == 0:
            print(f"  {total:,} processed...", flush=True)

    # --- Compute aggregate categories ---
    # "Garbage" = parking + for_sale + default_server + coming_soon + empty + low_content
    garbage_types = {"parking", "for_sale", "default_server", "coming_soon", "empty", "low_content"}
    garbage_count = sum(page_types[t] for t in garbage_types)
    dead_count = errors  # no HTTP response at all

    # Duplicates by favicon (top clusters)
    top_favicon = [(cnt, mmh3) for mmh3, cnt in favicon_clusters.most_common(20) if cnt >= 5]
    favicon_dupes = sum(cnt for cnt, _ in top_favicon if cnt >= 100)

    # Duplicates by simhash
    top_simhash = [(cnt, sh) for sh, cnt in simhash_clusters.most_common(20) if cnt >= 5]
    simhash_dupes = sum(cnt for cnt, _ in top_simhash if cnt >= 100)

    # -------------------------------------------------------------------
    # Report output
    # -------------------------------------------------------------------
    out = Path("E:/namesilo-scanner/report.txt")
    with open(out, "w", encoding="utf-8") as f:
        def w(s=""): f.write(s + "\n"); print(s)

        w("=" * 68)
        w("  NAMESILO DOMAINS — GARBAGE ANALYSIS REPORT")
        w("=" * 68)
        w(f"  Total domains attempted:    {total:>10,}")
        w(f"  Failed to connect (dead):   {dead_count:>10,}  ({dead_count/total*100:.1f}%)")
        w(f"  Successfully fetched:       {scanned:>10,}  ({scanned/total*100:.1f}%)")
        w()

        pct = lambda n: f"{n:>10,}  ({n/total*100:5.1f}%)" if total else f"{n:>10,}"

        w("─" * 68)
        w("  PAGE TYPE BREAKDOWN")
        w("─" * 68)
        labels = {
            "parking":           "Parking pages (registrar placeholder)",
            "for_sale":          "Domain for sale (for sale)",
            "default_server":    "Default server page (Apache/nginx/cPanel)",
            "coming_soon":       "Coming soon / Under construction",
            "empty":             "Empty page (< 2KB / < 20 words)",
            "low_content":       "Low content (20-199 words)",
            "redirect_external": "Redirect to external domain",
            "not_found":         "404 Not Found",
            "server_error":      "5xx Server Error",
            "active_with_forms": "Active page with forms (potential phishing)",
            "active_content":    "Active content (200+ words)",
            "unknown":           "Unknown",
        }
        for pt, label in labels.items():
            cnt = page_types.get(pt, 0)
            if cnt:
                w(f"  {label:<45} {pct(cnt)}")

        w()
        w(f"  {'TOTAL GARBAGE (parking+empty+default+sale+soon):':<45} {pct(garbage_count)}")
        w(f"  {'TOTAL DEAD (no HTTP response):':<45} {pct(dead_count)}")
        w(f"  {'TOTAL JUNK (garbage + dead):':<45}")
        total_junk = garbage_count + dead_count
        w(f"  → {total_junk:,} of {total:,} = {total_junk/total*100:.1f}%")

        w()
        w("─" * 68)
        w("  PARKING SERVICES")
        w("─" * 68)
        for svc, cnt in parking_services.most_common():
            w(f"  {svc:<20} {pct(cnt)}")
            for ex in parking_examples.get(svc, []):
                w(f"    → {ex}")

        w()
        w("─" * 68)
        w("  DUPLICATES — FAVICON HASH CLUSTERS")
        w("  (single hash = thousands of domains sharing one template)")
        w("─" * 68)
        for cnt, mmh3 in top_favicon[:15]:
            examples = ", ".join(domains_by_favicon[mmh3][:3])
            w(f"  {cnt:>8,} domains  mmh3={mmh3:<12}  e.g.: {examples}")
        w(f"  → Total domains in top clusters: {favicon_dupes:,}")

        w()
        w("─" * 68)
        w("  DUPLICATES — BODY SIMHASH CLUSTERS")
        w("  (identical or near-identical content)")
        w("─" * 68)
        for cnt, sh in top_simhash[:15]:
            examples = ", ".join(domains_by_simhash[sh][:3])
            w(f"  {cnt:>8,} domains  sh={sh}  e.g.: {examples}")
        w(f"  → Total domains in top clusters: {simhash_dupes:,}")

        w()
        w("─" * 68)
        w("  DUPLICATES — TITLE CLUSTERS")
        w("  (thousands of domains with the same page title = one placeholder template)")
        w("─" * 68)
        top_titles = [(cnt, tm) for tm, cnt in title_clusters.most_common(20) if cnt >= 5]
        for cnt, tm in top_titles[:15]:
            examples = ", ".join(domains_by_title[tm][:3])
            t_str = title_text.get(tm, "")[:50]
            w(f"  {cnt:>8,} domains  title=\"{t_str}\"  e.g.: {examples}")
        title_dupes = sum(cnt for cnt, _ in top_titles if cnt >= 100)
        w(f"  → Total domains in top clusters: {title_dupes:,}")

        w()
        w("─" * 68)
        w("  INFRASTRUCTURE")
        w("─" * 68)
        uniq_server_fp = len(server_fp_clusters)
        w(f"  Unique server fingerprints:     {uniq_server_fp:>8,}")
        w(f"  Cloudflare domains:             {cloudflare_count:>8,}  ({cloudflare_count/scanned*100:.1f}% of responding)" if scanned else "")
        w(f"  Domains with Set-Cookie:        {cookie_count:>8,}  ({cookie_count/scanned*100:.1f}%)" if scanned else "")

        w()
        w("─" * 68)
        w("  CONTENT — WORD COUNT DISTRIBUTION")
        w("─" * 68)
        for bucket in ["0 words", "1-19 words", "20-49 words", "50-199 words", "200+ words"]:
            cnt = word_count_buckets.get(bucket, 0)
            bar = "█" * min(40, int(cnt / max(scanned, 1) * 40 * 5))
            w(f"  {bucket:<15} {pct(cnt)}  {bar}")

        w()
        w("─" * 68)
        w("  TOP REDIRECT DESTINATIONS")
        w("─" * 68)
        for target, cnt in redirect_targets.most_common(20):
            w(f"  {cnt:>8,}  → {target}")

        w()
        w("─" * 68)
        w("  ERROR BREAKDOWN (domains that did not respond)")
        w("─" * 68)
        for err, cnt in error_types.most_common():
            w(f"  {err:<25} {cnt:>8,}")

        w()
        w("─" * 68)
        w("  TLS CN — WILDCARD CERTIFICATES (shared hosting)")
        w("─" * 68)
        for cn, cnt in tls_cn_counter.most_common(15):
            w(f"  {cnt:>8,}  {cn}")

        w()
        w("─" * 68)
        w("  META GENERATOR")
        w("─" * 68)
        for gen, cnt in generator_counter.most_common(15):
            w(f"  {cnt:>8,}  {gen}")

    print(f"\n→ Report: {out}")

    # Export parking and for_sale domains for blocklist
    bl = Path("E:/namesilo-scanner/garbage_domains.jsonl")
    with open(bl, "w") as bf:
        for f2 in files:
            opener = gzip.open if str(f2).endswith(".gz") else open
            with opener(f2, "rt", encoding="utf-8", errors="replace") as fh:
                for line in fh:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        rec = json.loads(line)
                        if rec.get("page_type") in garbage_types or rec.get("error"):
                            bf.write(json.dumps({
                                "domain": rec.get("domain"),
                                "page_type": rec.get("page_type", "dead"),
                                "parking_service": rec.get("parking_service", ""),
                                "title": rec.get("title", ""),
                                "word_count": rec.get("word_count", 0),
                                "favicon_mmh3": rec.get("favicon_mmh3"),
                            }) + "\n")
                    except Exception:
                        pass

    print(f"→ Garbage domains export: {bl}")


if __name__ == "__main__":
    local_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    if local_dir:
        files = list(local_dir.glob("*.jsonl")) + list(local_dir.glob("*.jsonl.gz"))
        analyze(files)
    else:
        analyze()
