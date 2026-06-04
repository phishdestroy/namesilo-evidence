# NameSilo Domain Scanner — Technical Overview

Scans all ~3.4M active NameSilo domains, collects HTTP/TLS fingerprints to identify phishing, gambling, and piracy infrastructure.

## Pipeline

```
1479_full.csv (5.27M domains — complete NameSilo zone export)
    ↓ prepare.py  (filter by IP/DNS presence)
domains_to_scan.jsonl (3.4M domains with DNS)
    ↓ enqueue.py  (push to SQS queue)
AWS Lambda ×400 concurrent  +  GCP Cloud Run ×20 containers
    ↓
S3: scans/YYYY/MM/DD/HH/*.jsonl
    ↓ analyze.py
report_stats.json  +  evidence_data.json
```

## Evidence Collected Per Domain

| Field | Forensic Value |
|---|---|
| `favicon_mmh3` | MurmurHash3 of favicon — identical hash = same operator |
| `body_simhash` | Identical pages across domains = mass-generated infrastructure |
| `redirect_chain` | Redirect targets reveal casino / crypto scam networks |
| `form_actions` | Login form presence = credential phishing |
| `keywords_hit` | Direct abuse markers: paypal, casino, prize, wallet |
| `tls_cn` | Wildcard `*.namesilo-parking.com` = shared scam infrastructure |
| `server_fp` | SHA-256(Server + X-Powered-By + ETag) — identifies shared servers |

## Running the Scanner

### 1. Dependencies
```bash
pip install boto3 aiohttp mmh3
aws configure   # set AWS credentials
```

### 2. Filter domains with DNS
```bash
python scanner/prepare.py
# → domains_to_scan.jsonl (3.4M entries)
```

### 3. Deploy AWS Lambda
```bash
export LAMBDA_ROLE_ARN="arn:aws:iam::ACCOUNT:role/namesilo-lambda-role"
export S3_BUCKET_NAME="namesilo-scan-results"
export SQS_QUEUE_ARN="arn:aws:sqs:us-east-1:ACCOUNT:namesilo-scan-queue"
bash deploy.sh
```

### 4. Enqueue and scan
```bash
python scanner/enqueue.py
# Pushes 3.4M SQS messages → Lambda auto-scales to 400 concurrent executions
```

### 5. Monitor
```bash
aws sqs get-queue-attributes --queue-url $SQS_QUEUE_URL \
  --attribute-names ApproximateNumberOfMessages

aws logs tail /aws/lambda/namesilo-scanner --follow
```

### 6. Analyze results
```bash
python scanner/analyze.py
# → report_stats.json  (clusters, fingerprints, page types)
# → evidence_data.json (full domain lists per abuse category)
```

## Estimated Cost (~3.4M domains)

| Service | Cost |
|---|---|
| AWS Lambda | ~$25 |
| SQS | ~$0.15 |
| S3 (~10 GB JSONL) | ~$1 |
| **Total** | **~$27** |
| **Runtime** | **~1.5–2 hours** |
