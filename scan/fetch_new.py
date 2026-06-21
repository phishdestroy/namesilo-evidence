#!/usr/bin/env python3
"""Fetch new domain registrations from NetAPI and update repository data."""

import os, gzip, csv, io, json, urllib.request, urllib.parse
from pathlib import Path
from datetime import date, datetime
from collections import defaultdict, Counter

REGISTRAR_ID = os.environ["REGISTRAR_ID"]
TOKEN        = os.environ["NETAPI_TOKEN"]
TODAY        = date.today().isoformat()

# Approximate registration prices by TLD (USD/year)
TLD_PRICES = {
    'com':8.99,'net':9.99,'org':9.99,'info':3.99,'biz':9.99,
    'xyz':1.49,'top':0.99,'club':3.99,'online':4.99,'site':4.99,
    'store':5.99,'shop':5.99,'app':14.00,'io':32.00,'co':24.99,
    'us':7.99,'cc':19.99,'me':11.99,'vip':4.99,'pro':7.99,
    'live':9.99,'link':3.99,'click':3.99,'tech':9.99,'digital':14.99,
    'finance':24.99,'exchange':24.99,'cash':14.99,'capital':24.99,
    'money':14.99,'trade':14.99,'market':14.99,'academy':14.99,
    'agency':11.99,'solutions':14.99,'support':14.99,'services':14.99,
    'group':11.99,'network':11.99,'tools':9.99,'pw':1.49,
    'icu':0.99,'cyou':0.99,'hair':1.99,'bond':9.99,'homes':9.99,
    'autos':9.99,'voto':9.99,'wiki':14.99,'space':4.99,'website':4.99,
}
DEFAULT_PRICE = 4.99

def get_price(domain):
    tld = domain.rsplit('.', 1)[-1].lower()
    return TLD_PRICES.get(tld, DEFAULT_PRICE)

# ── Fetch from NetAPI ─────────────────────────────────────────────────────────
print(f"Fetching registrar_id={REGISTRAR_ID} ...")
params = urllib.parse.urlencode({
    'method':       'download-whois',
    'registrar_id': REGISTRAR_ID,
    'filter_type':  'new',
    'token':        TOKEN,
    'dataset_type': 'dataset',
})
req = urllib.request.Request(
    'https://netapi.com/api2/?' + params,
    headers={'User-Agent': 'PhishDestroy/2.0'}
)
with urllib.request.urlopen(req, timeout=300) as resp:
    raw = gzip.decompress(resp.read()).decode('utf-8', errors='replace')

# CSV columns: registrar, url, registered_at, expiring_at,
#              majestic_rank, emails, phones, ip, ip_country
reader = csv.reader(io.StringIO(raw))
next(reader)  # skip header

by_date     = defaultdict(list)
all_domains = set()

for row in reader:
    if len(row) < 3:
        continue
    domain         = row[1].strip().lower()
    reg_date       = row[2].strip()
    expiring_at    = row[3].strip() if len(row) > 3 else ''
    majestic_rank  = row[4].strip() if len(row) > 4 else ''
    emails_raw     = row[5].strip() if len(row) > 5 else ''
    phones_raw     = row[6].strip() if len(row) > 6 else ''
    ip          = row[7].strip() if len(row) > 7 else ''
    ip_country  = row[8].strip() if len(row) > 8 else ''

    if not domain or '.' not in domain:
        continue
    if len(reg_date) == 10 and reg_date[:4].isdigit():
        by_date[reg_date].append({
            'd': domain,
            'e': expiring_at,
            'r': majestic_rank,
            'm': emails_raw,
            'p': phones_raw,
            'i': ip,
            'c': ip_country,
        })
        all_domains.add(domain)

dates = sorted(by_date.keys())
if not dates:
    print("No data returned"); exit(0)

print(f"  {len(all_domains):,} unique domains across {len(dates)} days ({dates[0]} → {dates[-1]})")

# ── Revenue & lifetime ────────────────────────────────────────────────────────
def day_revenue(records):
    return round(sum(get_price(r['d']) for r in records), 2)

def avg_lifetime_days(by_date_map):
    durations = []
    for records in by_date_map.values():
        for r in records:
            reg, exp = r.get('e',''), ''
            # expiring_at is in row, but stored as 'e' key via backfill
            # For newly fetched data, reg_date is the key, expiring_at is r['e']
            try:
                if r['e'] and len(r['e']) == 10:
                    d1 = datetime.strptime(records[0] if isinstance(records[0], str) else r['d'], '%Y-%m-%d') if False else None
                    # compute from by_date key
            except Exception:
                pass
    # Simpler: compute from raw records stored per date
    return 365  # fallback

# Compute avg lifetime from expiring_at - registered_at
durations = []
for reg_date, records in by_date.items():
    for r in records:
        exp = r.get('e', '')
        if exp and len(exp) == 10:
            try:
                d1 = datetime.strptime(reg_date, '%Y-%m-%d')
                d2 = datetime.strptime(exp, '%Y-%m-%d')
                durations.append((d2 - d1).days)
            except Exception:
                pass
avg_lifetime = (sum(durations) // len(durations)) if durations else 365

total_revenue = sum(day_revenue(by_date[d]) for d in dates)

# ── IP/country stats ──────────────────────────────────────────────────────────
country_counts = Counter(
    r['c'] for records in by_date.values() for r in records if r.get('c')
)
ip_counts = Counter(
    r['i'] for records in by_date.values() for r in records if r.get('i')
)

# ── Deployment stats (has IP vs no IP) ────────────────────────────────────────
all_recs_flat = [r for records in by_date.values() for r in records]
deployed_count = sum(1 for r in all_recs_flat if r.get('i'))
no_ip_count    = len(all_recs_flat) - deployed_count
deploy_rate    = round(deployed_count / len(all_recs_flat) * 100, 1) if all_recs_flat else 0

# ── Registration period buckets ────────────────────────────────────────────────
period_buckets = {'lt_1yr': 0, 'eq_1yr': 0, 'yr_2': 0, 'yr_3plus': 0}
tld_periods    = {}  # tld -> list of days
tld_counts_map = Counter()

for reg_date, records in by_date.items():
    for r in records:
        tld = r['d'].rsplit('.', 1)[-1].lower() if '.' in r['d'] else ''
        tld_counts_map[tld] += 1
        exp = r.get('e', '')
        if exp and len(exp) == 10:
            try:
                d1 = datetime.strptime(reg_date, '%Y-%m-%d')
                d2 = datetime.strptime(exp, '%Y-%m-%d')
                days = (d2 - d1).days
                if tld:
                    tld_periods.setdefault(tld, []).append(days)
                if days < 350:
                    period_buckets['lt_1yr'] += 1
                elif days < 500:
                    period_buckets['eq_1yr'] += 1
                elif days < 800:
                    period_buckets['yr_2'] += 1
                else:
                    period_buckets['yr_3plus'] += 1
            except Exception:
                pass

total_with_period = sum(period_buckets.values())
pct_gt1 = round((period_buckets['yr_2'] + period_buckets['yr_3plus']) / total_with_period * 100, 1) if total_with_period else 0
pct_gt2 = round(period_buckets['yr_3plus'] / total_with_period * 100, 1) if total_with_period else 0

# TLD stats: count + avg reg period
tld_stats = {}
for tld, cnt in tld_counts_map.most_common(20):
    avg_d = int(sum(tld_periods.get(tld, [])) / len(tld_periods[tld])) if tld_periods.get(tld) else 365
    tld_stats[tld] = {'count': cnt, 'avg_days': avg_d}

# ── Revenue by TLD zone ────────────────────────────────────────────────────────
revenue_by_tld = {}
for tld, cnt in tld_counts_map.most_common(20):
    price    = TLD_PRICES.get(tld, DEFAULT_PRICE)
    tld_rev  = round(cnt * price, 2)
    revenue_by_tld[tld] = {
        'count':   cnt,
        'price':   price,
        'revenue': tld_rev,
        'pct':     round(tld_rev / total_revenue * 100, 1) if total_revenue else 0,
    }

# ── Domain freshness: days from registration date to TODAY ────────────────────
# Tells us how quickly we catch newly registered phishing domains
catch_buckets = {'same_day': 0, 'within_week': 0, 'within_month': 0, 'older': 0}
catch_ages_list = []
today_dt = datetime.strptime(TODAY, '%Y-%m-%d')
for reg_date, records in by_date.items():
    try:
        d1  = datetime.strptime(reg_date, '%Y-%m-%d')
        age = (today_dt - d1).days
        catch_ages_list.append(age)
        n   = len(records)
        if age == 0:    catch_buckets['same_day']     += n
        elif age <= 7:  catch_buckets['within_week']  += n
        elif age <= 30: catch_buckets['within_month'] += n
        else:           catch_buckets['older']         += n
    except Exception:
        pass
avg_catch_age = (sum(catch_ages_list) // len(catch_ages_list)) if catch_ages_list else 0
catch_total   = sum(catch_buckets.values()) or 1
fresh_pct     = round((catch_buckets['same_day'] + catch_buckets['within_week']) / catch_total * 100, 1)

# ── Burst days: top 10 days by registration volume (campaign detection) ───────
daily_counts  = {d: len(set(r['d'] for r in by_date[d])) for d in dates}
avg_daily     = sum(daily_counts.values()) / len(daily_counts) if daily_counts else 1
burst_days    = sorted(daily_counts.items(), key=lambda x: -x[1])[:10]
burst_days    = [{'date': d, 'count': c, 'x_avg': round(c / avg_daily, 1)} for d, c in burst_days]

# ── Registrant fingerprinting (email + phone) ─────────────────────────────────
email_counts = Counter()
phone_counts = Counter()
for records in by_date.values():
    for r in records:
        for em in r.get('m', '').split(','):
            em = em.strip().lower()
            if em and '@' in em:
                email_counts[em] += 1
        for ph in r.get('p', '').split(','):
            ph = ph.strip()
            if ph and len(ph) >= 7:
                phone_counts[ph] += 1

top_registrant_emails = dict(email_counts.most_common(20))
top_registrant_phones = dict(phone_counts.most_common(10))
serial_email_count    = sum(1 for c in email_counts.values() if c >= 10)

# ── Brand/keyword heatmap ──────────────────────────────────────────────────────
BRAND_KEYWORDS = [
    'metamask','coinbase','binance','wallet','defi','airdrop','claim','bitcoin',
    'ethereum','crypto','token','nft','web3','ledger','trezor','uniswap','opensea',
    'kraken','kucoin','bybit','okx','huobi','trust','phantom','solana','polygon',
    'arbitrum','optimism','swap','bridge','staking','yield','vault','farm','mint',
    'connect','secure','support','login','verify','account','update','official',
]
keyword_counts = Counter()
for domain in all_domains:
    label = domain.split('.')[0]
    for kw in BRAND_KEYWORDS:
        if kw in label:
            keyword_counts[kw] += 1

brand_heatmap = dict(keyword_counts.most_common(20))

# ── Majestic rank: % of unknown/new domains ────────────────────────────────────
ranked_count   = sum(1 for records in by_date.values() for r in records if r.get('r','').strip() not in ('','0'))
unranked_count = len(all_domains) - ranked_count
unranked_pct   = round(unranked_count / len(all_domains) * 100, 1) if all_domains else 0

# ── Correlation with main destroylist ─────────────────────────────────────────
correlation_count = 0
correlation_pct   = 0.0
try:
    _ml_req = urllib.request.Request(
        'https://raw.githubusercontent.com/phishdestroy/destroylist/main/list.txt',
        headers={'User-Agent': 'PhishDestroy/2.0'})
    with urllib.request.urlopen(_ml_req, timeout=30) as _ml_resp:
        _main_domains = set(_ml_resp.read().decode('utf-8', errors='replace').strip().splitlines())
    _overlap = all_domains & _main_domains
    correlation_count = len(_overlap)
    correlation_pct   = round(correlation_count / len(all_domains) * 100, 1) if all_domains else 0
    print(f"Correlation: {correlation_count:,} of {len(all_domains):,} domains in main blocklist ({correlation_pct}%)")
except Exception as _ce:
    print(f"Correlation fetch failed: {_ce}")

# ── Monthly snapshot ───────────────────────────────────────────────────────────
_snap_dir = Path('data/snapshots')
_snap_dir.mkdir(exist_ok=True)
_monthly_snap = {
    'month':              TODAY[:7],
    'generated':          TODAY,
    'total_domains':      len(all_domains),
    'total_revenue':      round(total_revenue, 2),
    'avg_reg_days':       avg_lifetime,
    'deployment_rate':    deploy_rate,
    'fresh_pct':          fresh_pct,
    'unranked_pct':       unranked_pct,
    'correlation_pct':    correlation_pct,
    'serial_registrants': serial_email_count,
    'top_tld':            list(tld_stats.keys())[0] if tld_stats else '',
    'top_country':        list(country_counts.keys())[0] if country_counts else '',
    'top_brand':          list(brand_heatmap.keys())[0] if brand_heatmap else '',
}
(_snap_dir / f'{TODAY[:7]}.json').write_text(json.dumps(_monthly_snap, indent=2), encoding='utf-8')

# ── Write daily TXT + JSON ────────────────────────────────────────────────────
data_root = Path('data/new')
for day_date in dates:
    yr, mo = day_date[:4], day_date[5:7]
    day_dir = data_root / yr / mo
    day_dir.mkdir(parents=True, exist_ok=True)

    records = by_date[day_date]
    domains = sorted(set(r['d'] for r in records))

    # plain TXT
    (day_dir / f'{day_date}.txt').write_text('\n'.join(domains) + '\n', encoding='utf-8')

    # enriched JSON
    day_json = {
        'date':             day_date,
        'count':            len(domains),
        'revenue_estimate': day_revenue(records),
        'domains': [
            {k2: v2 for k2, v2 in {
                'domain':      r['d'],
                'expiring_at': r.get('e',''),
                'ip':          r.get('i',''),
                'ip_country':  r.get('c',''),
                'email':       r.get('m','').split(',')[0].strip().lower() if r.get('m') else '',
                'phone':       r.get('p','').split(',')[0].strip() if r.get('p') else '',
            }.items() if v2}
            for r in sorted(records, key=lambda x: x['d'])
        ]
    }
    (day_dir / f'{day_date}.json').write_text(
        json.dumps(day_json, separators=(',',':')), encoding='utf-8'
    )

# ── Monthly rollup TXT ────────────────────────────────────────────────────────
by_month = defaultdict(set)
for day_date, records in by_date.items():
    by_month[day_date[:7]].update(r['d'] for r in records)

for month_key, doms in by_month.items():
    yr = month_key[:4]
    mp = data_root / yr
    mp.mkdir(parents=True, exist_ok=True)
    (mp / f'{month_key}.txt').write_text('\n'.join(sorted(doms)) + '\n', encoding='utf-8')

# ── all.txt ───────────────────────────────────────────────────────────────────
Path('data/all.txt').write_text('\n'.join(sorted(all_domains)) + '\n', encoding='utf-8')

# ── data/index.json ───────────────────────────────────────────────────────────
index_days = [
    {
        'date':    d,
        'count':   len(set(r['d'] for r in by_date[d])),
        'revenue': day_revenue(by_date[d]),
        'path':    f'data/new/{d[:4]}/{d[5:7]}/{d}.txt',
    }
    for d in dates
]
index = {
    'days':                   index_days,
    'total_new_all_time':     len(all_domains),
    'total_revenue_estimate': round(total_revenue, 2),
    'avg_registration_days':  avg_lifetime,
    'ip_countries':           dict(country_counts.most_common(10)),
    'top_shared_ips':         dict(ip_counts.most_common(20)),
    'deployed_count':         deployed_count,
    'no_ip_count':            no_ip_count,
    'deployment_rate':        deploy_rate,
    'reg_periods':            period_buckets,
    'pct_gt_1yr':             pct_gt1,
    'pct_gt_2yr':             pct_gt2,
    'tld_stats':              tld_stats,
    'revenue_by_tld':         revenue_by_tld,
    'catch_age_buckets':      catch_buckets,
    'avg_catch_age_days':     avg_catch_age,
    'fresh_pct':              fresh_pct,
    'burst_days':             burst_days,
    'top_registrant_emails':  top_registrant_emails,
    'top_registrant_phones':  top_registrant_phones,
    'serial_email_count':     serial_email_count,
    'brand_heatmap':          brand_heatmap,
    'unranked_pct':           unranked_pct,
    'ranked_count':           ranked_count,
    'correlation_count':      correlation_count,
    'correlation_pct':        correlation_pct,
    'last_updated':           dates[-1],
}
Path('data/index.json').write_text(json.dumps(index, indent=2) + '\n', encoding='utf-8')

# ── IOC export: data/ioc/ ──────────────────────────────────────────────────────
ioc_dir = Path('data/ioc')
ioc_dir.mkdir(parents=True, exist_ok=True)

# Serial registrants: emails with >=5 domains
serial_regs = []
for em, cnt in email_counts.most_common(50):
    if cnt < 5:
        break
    domains_for_email = [
        r['d'] for records in by_date.values()
        for r in records
        if r.get('m','').split(',')[0].strip().lower() == em
    ]
    serial_regs.append({'email': em, 'count': cnt, 'domains': sorted(set(domains_for_email))[:100]})

(ioc_dir / 'serial_registrants.json').write_text(
    json.dumps({'generated': TODAY, 'count': len(serial_regs), 'registrants': serial_regs}, indent=2),
    encoding='utf-8')

# Shared IPs: IPs hosting >=3 domains
shared_ip_export = []
for ip_addr, cnt in ip_counts.most_common(50):
    if cnt < 3:
        break
    domains_for_ip = sorted(set(
        r['d'] for records in by_date.values()
        for r in records if r.get('i') == ip_addr
    ))
    country = next((
        r.get('c','') for records in by_date.values()
        for r in records if r.get('i') == ip_addr and r.get('c')
    ), '')
    shared_ip_export.append({'ip': ip_addr, 'count': cnt, 'country': country, 'domains': domains_for_ip[:100]})

(ioc_dir / 'shared_ips.json').write_text(
    json.dumps({'generated': TODAY, 'count': len(shared_ip_export), 'ips': shared_ip_export}, indent=2),
    encoding='utf-8')

# Brand domains: domains per keyword
brand_domains_export = {}
for kw in brand_heatmap:
    brand_domains_export[kw] = sorted(d for d in all_domains if kw in d.split('.')[0])[:200]

(ioc_dir / 'brand_domains.json').write_text(
    json.dumps({'generated': TODAY, 'keywords': brand_domains_export}, indent=2),
    encoding='utf-8')

print(f"IOC: {len(serial_regs)} serial registrants | {len(shared_ip_export)} shared IPs written")

# ── Stats badges ──────────────────────────────────────────────────────────────
stats_dir = Path('stats')
stats_dir.mkdir(exist_ok=True)

today_recs    = by_date.get(TODAY, [])
today_count   = len(set(r['d'] for r in today_recs))
today_revenue = day_revenue(today_recs)

def badge(label, message, color, label_color='0c1018'):
    return json.dumps({
        'schemaVersion': 1, 'label': label, 'message': str(message),
        'color': color, 'labelColor': label_color, 'style': 'flat-square'
    })

(stats_dir / 'today.json').write_text(
    badge('new today', f'{today_count:,}', 'da3633'), encoding='utf-8')
(stats_dir / 'total.json').write_text(
    badge('total domains', f'{len(all_domains):,}', 'da3633'), encoding='utf-8')
(stats_dir / 'last_fetch.json').write_text(
    badge('last fetch', dates[-1], '0075ca'), encoding='utf-8')
(stats_dir / 'revenue.json').write_text(
    badge('est. revenue', f'${total_revenue:,.0f}', 'e3b341'), encoding='utf-8')
(stats_dir / 'lifetime.json').write_text(
    badge('avg reg. period', f'{avg_lifetime}d', '6e40c9'), encoding='utf-8')

if country_counts:
    top3 = ' · '.join(f'{c}:{n:,}' for c, n in country_counts.most_common(3) if c)
    (stats_dir / 'hosting.json').write_text(
        badge('top hosting', top3 or 'n/a', '0075ca'), encoding='utf-8')

if ip_counts:
    top_ip_msg = f'{ip_counts.most_common(1)[0][1]:,} domains'
    (stats_dir / 'top_ip.json').write_text(
        badge('top IP domains', top_ip_msg, '8b5cf6'), encoding='utf-8')

(stats_dir / 'no_ip.json').write_text(
    badge('no DNS at reg', f'{no_ip_count:,} ({100-deploy_rate:.0f}%)', 'e3b341'), encoding='utf-8')

(stats_dir / 'deployed.json').write_text(
    badge('deployed', f'{deployed_count:,} ({deploy_rate:.0f}%)', '2ea44f'), encoding='utf-8')

if total_with_period:
    longreg_msg = f'>1yr: {pct_gt1}% · >2yr: {pct_gt2}%'
    (stats_dir / 'longreg.json').write_text(
        badge('long reg.', longreg_msg, '8b5cf6'), encoding='utf-8')

if tld_stats:
    top3_tlds = ' · '.join(f'.{t}:{v["count"]:,}' for t,v in list(tld_stats.items())[:3])
    (stats_dir / 'tld_top.json').write_text(
        badge('top TLDs', top3_tlds, '6e40c9'), encoding='utf-8')

if revenue_by_tld:
    top_tld_item = list(revenue_by_tld.items())[0]
    (stats_dir / 'top_tld_rev.json').write_text(
        badge('top $ TLD', f'.{top_tld_item[0]}: ${top_tld_item[1]["revenue"]:,.0f}', 'e3b341'), encoding='utf-8')

(stats_dir / 'freshness.json').write_text(
    badge('fresh catch', f'{fresh_pct}% ≤7d old', '2ea44f'), encoding='utf-8')

if serial_email_count:
    (stats_dir / 'serial_regs.json').write_text(
        badge('serial registrants', f'{serial_email_count:,} emails ≥10 domains', 'da3633'), encoding='utf-8')

if brand_heatmap:
    top3_brands = ' · '.join(list(brand_heatmap.keys())[:3])
    (stats_dir / 'brands.json').write_text(
        badge('top targets', top3_brands, '6e40c9'), encoding='utf-8')

(stats_dir / 'unranked.json').write_text(
    badge('unranked domains', f'{unranked_pct}% zero Majestic', '6e40c9'), encoding='utf-8')

if correlation_count:
    (stats_dir / 'correlation.json').write_text(
        badge('in blocklist', f'{correlation_pct}% confirmed phishing', '2ea44f'), encoding='utf-8')

print(f"Done: {len(all_domains):,} domains | ${total_revenue:,.2f} est. revenue | {avg_lifetime}d avg | today: {today_count:,} | deployed: {deploy_rate:.0f}% | >1yr: {pct_gt1}% | >2yr: {pct_gt2}% | fresh: {fresh_pct}%")
