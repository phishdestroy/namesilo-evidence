# NameSilo Domain Registration Anomaly Analysis

> **Analysis date:** 2026-05-08 | **Dataset:** 130.4M domains across 8 registrars | **Full domain list:** [namesilo-domains-5.1M.csv.gz](namesilo-domains-5.1M.csv.gz) (54MB compressed, 5,179,405 domains)

## Executive Summary

Analysis of 130+ million domains across 8 major registrars reveals that **NameSilo, LLC (IANA ID 1479)** exhibits statistically anomalous patterns in domain registration activity. Approximately **32% of NameSilo-managed domains show zero signs of ever being used** — no IP address, no email, no phone, no web presence — compared to a **15–21% baseline** observed at legitimate large-scale registrars. Combined with bulk registration patterns (10,000–17,000 domains/day), heavy use of cheap/abuse-prone TLDs, and an estimated **$12M spent on never-activated domains**, these findings are consistent with **registrar-facilitated money laundering, self-dealing, or systematic revenue inflation**.

---

## Methodology

- **Data source:** Full registrar domain datasets (CSV) containing: domain URL, registration/expiry dates, Majestic rank, contact email/phone, IP address, IP geolocation
- **"Dead" domain definition:** No IP + no email + no phone + no Majestic rank = domain was never configured or used
- **Cost estimation:** Based on publicly listed industry registration prices per TLD
- **Comparison group:** 8 registrars ranging from the world's largest (GoDaddy, 65M domains) to small niche operators

---

## Comparative Results — 8 Registrars

| Registrar | IANA ID | Total Domains | Dead % | No Email % | Est. Total Cost | Est. Dead Cost | Waste % |
|---|---|---|---|---|---|---|---|
| Hostinger | 1636 | 6,605,830 | **14.7%** | 81.3% | $56.3M | $8.2M | 14.5% |
| GoDaddy | 146 | 65,374,073 | **16.0%** | 89.8% | $672.6M | $107.5M | 16.0% |
| Tucows | 69 | 10,109,244 | **20.1%** | 85.0% | $105.7M | $21.6M | 20.4% |
| Network Solutions | 2 | 5,033,191 | **21.4%** | 91.5% | $52.1M | $11.2M | 21.4% |
| Namecheap | 1068 | 24,056,032 | **22.8%** | 93.5% | $205.8M | $49.0M | 23.8% |
| Gname.com | 1923 | 5,995,317 | **31.4%** | 95.2% | $56.5M | $15.9M | 28.1% |
| **NameSilo** | **1479** | **5,179,405** | **32.2%** | **95.9%** | **$37.0M** | **$12.0M** | **32.6%** |
| Dynadot | 472 | 8,026,951 | **39.5%** | 96.3% | $58.5M | $23.4M | 40.1% |

**Baseline:** The four largest/most established registrars (GoDaddy, Hostinger, Tucows, Network Solutions) cluster at 14.7%–21.4% dead domains.

**NameSilo (32.2%)** is **1.5x–2x above baseline**. This gap cannot be explained by pricing alone — Namecheap is similarly cheap and bulk-friendly, yet sits at only 22.8%.

---

## NameSilo — Detailed Findings

### 1. Scale of Dead Domains

- **1,668,355 domains (32.2%)** have never been activated
- 95.9% of all NameSilo domains have no associated email address
- 97.9% have no phone number
- 99.9% have no Majestic rank (never indexed by search engines)

### 2. Exponential Growth of Dead Registrations

| Year | Dead Domains Registered | Est. Cost |
|---|---|---|
| 2020 | 39,115 | $395K |
| 2021 | 41,477 | $424K |
| 2022 | 46,442 | $464K |
| 2023 | 67,905 | $654K |
| **2024** | **485,859** | **$3.34M** |
| **2025** | **585,595** | **$3.08M** |
| 2026 (partial) | 145,298 | $912K |

Dead domain registrations increased **7x between 2023 and 2024**, and continued accelerating into 2025.

### 3. Bulk Registration Patterns

| Date | Domains Registered |
|---|---|
| 2025-07-19 | 17,180 |
| 2025-12-01 | 14,147 |
| 2025-05-09 | 12,336 |
| 2025-12-08 | 12,142 |
| 2025-12-11 | 12,090 |

Sustained volume of **10,000+ domains/day** throughout 2025, consistent with automated bulk purchasing.

### 4. Abuse-Prone TLD Profile

| TLD | NameSilo | GoDaddy (baseline) |
|---|---|---|
| .com | 41% | 77% |
| .sbs | 7% | <0.1% |
| .xyz | 7% | <1% |
| .cfd | 4% | <0.1% |
| .top | 4% | <1% |

NameSilo has a **disproportionately high share of cheap, abuse-associated TLDs**. These cost $1–3 to register and are widely documented as preferred by spam/fraud operations.

### 5. IP Concentration — Parking Infrastructure

| IP Address | Domains | Owner |
|---|---|---|
| 91.195.240.123 | 522,466 | Sedo (domain parking) |
| 188.114.96.3 | 242,441 | Cloudflare (default/unresolved) |
| 188.114.97.3 | 242,278 | Cloudflare (default/unresolved) |
| 23.227.38.65 | 82,563 | Shopify (default page) |
| 64.190.62.22 | 63,532 | NameSilo parking |

Top 10 IP addresses account for **36.7% of all NameSilo domains with DNS** (1.29M domains). An additional **646,381 domains (12.5%)** sit on known parking IPs with no real use.

### 6. Financial Summary

| Metric | Amount |
|---|---|
| Total estimated registration cost | ~$37.0M |
| Estimated cost of dead domains | ~$12.0M |
| Waste percentage | 32.6% |
| Annual burn rate on dead domains (2024–2025) | ~$3.2M/year |
| Dead domains pre-paid through 2026 | 1.13M domains (~$8.1M) |
| Dead domains pre-paid through 2027 | 518K domains (~$3.8M) |

---

## NameSilo vs Namecheap — Direct Competitor Comparison

Both are US-based, low-cost, bulk-friendly registrars. Namecheap has 4.6x more domains.

| Metric | Namecheap | NameSilo | Delta |
|---|---|---|---|
| Total domains | 24.1M | 5.2M | — |
| Dead % | 22.8% | 32.2% | **+41% higher** |
| No email % | 93.5% | 95.9% | +2.6% |
| .com share | 54% | 41% | NameSilo skews junk TLDs |
| Waste % | 23.8% | 32.6% | **+37% higher** |

**NameSilo is 10 percentage points dirtier than its closest market peer.** This differential is not explained by business model or pricing.

---

## Possible Explanations

1. **Money Laundering via Domain Registration** — Funds are converted to "domain purchases" at scale. The registrar receives legitimate business revenue. Domains are never used — the transaction itself is the purpose. Estimated throughput: ~$3.2M/year.

2. **Revenue Inflation / Self-Dealing** — The registrar or affiliated entities register domains through their own platform to inflate revenue metrics for valuation, acquisition, or investor purposes.

3. **Affiliate/Reseller Abuse** — Third-party resellers conduct bulk registrations to collect referral commissions or exploit promotional pricing, with no intent to use domains.

4. **Speculative Domain Investment** (least likely) — The TLD profile (.sbs, .cfd, .xyz) and total absence of activation make pure speculation an unlikely explanation for the full volume.

---

## Key Anomaly Indicators

1. Dead domain rate **2x industry baseline** (32% vs 15–21%)
2. **7x year-over-year spike** in dead registrations (2023 → 2024)
3. Sustained **10K+/day** bulk registration throughout 2025
4. **$12M+** spent on domains with zero activation
5. Disproportionate junk TLD usage (.sbs/.cfd/.xyz = 18% vs <2% at GoDaddy)
6. Extreme IP concentration — 12 IPs serve 37% of all resolved domains (parking)
7. **96% of domains have no contact email** (vs 81–90% at baseline registrars)
8. Registrations accelerating with no corresponding increase in active domains

---

## Recommendations for Further Investigation

1. **WHOIS/RDAP analysis** — Identify registrant patterns among dead domains (same privacy service, same org, same address)
2. **Financial flow tracing** — Payment methods used for bulk dead registrations (prepaid cards, crypto, wire transfers)
3. **Cross-registrar actor matching** — Shared IPs/emails between NameSilo, Gname, and Dynadot dead domains
4. **Temporal correlation** — Map bulk registration dates against known laundering operations or crypto market events
5. **Reseller/affiliate audit** — Identify which accounts generate the highest volume of never-activated registrations

---

## Data Download

The complete NameSilo domain dataset (5,179,405 domains) is available for download:

**[namesilo-domains-5.1M.csv.gz](namesilo-domains-5.1M.csv.gz)** (54MB gzipped)

Contains: domain URL, registration date, expiry date, Majestic rank, contact email, phone, IP address, IP geolocation.

---

*PhishDestroy Research · [phishdestroy.eth.limo](https://phishdestroy.eth.limo/) · [abuse@phishdestroy.io](mailto:abuse@phishdestroy.io)*
