"""
Lambda handler: asyncio + aiohttp — processes the entire SQS batch concurrently.
100 domains concurrently in ~8-10 seconds instead of 600.
"""
import asyncio
import json
import os
import time
import ssl
import hashlib
import re
from datetime import datetime, timezone
from urllib.parse import urlparse

import aiohttp
import boto3

import fingerprint as fp

S3_BUCKET      = os.environ["S3_BUCKET"]
HTTP_TIMEOUT   = int(os.environ.get("HTTP_TIMEOUT", "6"))
MAX_REDIRECTS  = int(os.environ.get("MAX_REDIRECTS", "3"))
CONCUR_PER_INV = int(os.environ.get("CONCUR_PER_INV", "50"))  # concurrent requests within a single Lambda invocation

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36")

s3 = boto3.client("s3")


def _ssl_ctx():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


async def _fetch(session: aiohttp.ClientSession, domain: str) -> dict:
    redirect_chain = []
    result_url = ""
    status = 0

    for scheme in ("https", "http"):
        url = f"{scheme}://{domain}"
        try:
            async with session.get(
                url,
                timeout=aiohttp.ClientTimeout(total=HTTP_TIMEOUT),
                max_redirects=MAX_REDIRECTS,
                ssl=_ssl_ctx(),
                allow_redirects=True,
            ) as resp:
                status = resp.status
                result_url = str(resp.url)
                headers = {k.lower(): v for k, v in resp.headers.items()}
                body = await resp.read()
                body = body[:512_000]

                # Redirect chain
                if resp.history:
                    redirect_chain = [str(h.url) for h in resp.history]

                tls_info = {}  # aiohttp does not expose the cert directly without an SSL hook — skip
                extracted = fp.extract(
                    domain, result_url, status, headers,
                    body, redirect_chain, tls_info
                )
                return {"error": None, **extracted}

        except aiohttp.TooManyRedirects:
            return {"domain": domain, "error": "too_many_redirects", "page_type": "redirect_loop"}
        except asyncio.TimeoutError:
            if scheme == "https":
                continue  # try http
            return {"domain": domain, "error": "timeout", "page_type": "dead"}
        except aiohttp.ClientConnectorError:
            if scheme == "https":
                continue
            return {"domain": domain, "error": "connection_refused", "page_type": "dead"}
        except Exception as e:
            err = str(e)[:80]
            if scheme == "https":
                continue
            return {"domain": domain, "error": err, "page_type": "dead"}

    return {"domain": domain, "error": "no_response", "page_type": "dead"}


async def _fetch_favicon(session: aiohttp.ClientSession, url: str) -> dict:
    try:
        async with session.get(
            url,
            timeout=aiohttp.ClientTimeout(total=4),
            ssl=_ssl_ctx(),
        ) as resp:
            if resp.status == 200:
                raw = await resp.read()
                raw = raw[:32_768]
                return {
                    "favicon_md5": hashlib.md5(raw).hexdigest(),
                    "favicon_mmh3": fp.favicon_mmh3(raw),
                }
    except Exception:
        pass
    return {}


async def _scan_item(session: aiohttp.ClientSession, item: dict) -> dict:
    domain = item["domain"]
    ts = int(time.time())

    result = await _fetch(session, domain)
    result["domain"] = domain
    result["ip"] = item.get("ip", "")
    result["ip_country"] = item.get("ip_country", "")
    result["scan_ts"] = ts

    # Favicon (only if the domain responded)
    if not result.get("error"):
        favicon_hint = result.get("favicon_hint", "")
        scheme = "https" if result.get("final_url", "").startswith("https") else "http"
        if favicon_hint:
            fav_url = favicon_hint if favicon_hint.startswith("http") \
                else f"{scheme}://{domain}/{favicon_hint.lstrip('/')}"
        else:
            fav_url = f"{scheme}://{domain}/favicon.ico"
        result.update(await _fetch_favicon(session, fav_url))
        result["favicon_url"] = fav_url

    return result


async def _process_batch(items: list[dict]) -> list[dict]:
    connector = aiohttp.TCPConnector(
        limit=CONCUR_PER_INV,
        ssl=False,
        enable_cleanup_closed=True,
    )
    headers = {
        "User-Agent": UA,
        "Accept": "text/html,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
    }
    async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
        tasks = [_scan_item(session, item) for item in items]
        return await asyncio.gather(*tasks, return_exceptions=False)


def _write_s3(records: list, batch_id: str) -> str:
    ts = datetime.now(timezone.utc).strftime("%Y%m%d/%H")
    key = f"scans/{ts}/{batch_id}.jsonl"
    body = "\n".join(json.dumps(r, ensure_ascii=False) for r in records)
    s3.put_object(
        Bucket=S3_BUCKET,
        Key=key,
        Body=body.encode("utf-8"),
        ContentType="application/x-ndjson",
    )
    return key


def lambda_handler(event, context):
    # Collect all domains from all SQS messages in the batch
    items = []
    for sqs_record in event.get("Records", []):
        batch = json.loads(sqs_record["body"])
        if isinstance(batch, list):
            items.extend(batch)
        else:
            items.append(batch)

    if not items:
        return {"statusCode": 200, "count": 0}

    results = asyncio.run(_process_batch(items))

    key = _write_s3(results, context.aws_request_id)

    ok  = sum(1 for r in results if not r.get("error"))
    err = len(results) - ok
    print(f"Batch={len(items)} ok={ok} err={err} → s3://{S3_BUCKET}/{key}")

    return {"statusCode": 200, "count": len(results)}
