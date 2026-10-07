#!/usr/bin/env python3
"""Just create the Cloud Run Job (steps 1+2 already done)."""
import json
import os
import sys
import time
import requests
from pathlib import Path

import google.auth.transport.requests
from google.oauth2 import service_account

PROJECT_ID  = os.environ.get("GCP_PROJECT_ID", "")
REGION      = os.environ.get("GCP_REGION", "us-central1")
REPO_NAME   = "scanner"
IMAGE_NAME  = "domain-scanner"
IMAGE_TAG   = "latest"
JOB_NAME    = "domain-scanner-job"
SA_KEY_PATH = os.environ.get("GCP_SA_KEY_PATH", "")

SCOPES = ["https://www.googleapis.com/auth/cloud-platform"]
AR_IMAGE = f"{REGION}-docker.pkg.dev/{PROJECT_ID}/{REPO_NAME}/{IMAGE_NAME}:{IMAGE_TAG}"


def get_credentials():
    creds = service_account.Credentials.from_service_account_file(SA_KEY_PATH, scopes=SCOPES)
    creds.refresh(google.auth.transport.requests.Request())
    return creds


def auth_headers(creds) -> dict:
    creds.refresh(google.auth.transport.requests.Request())
    return {
        "Authorization": f"Bearer {creds.token}",
        "Content-Type": "application/json",
    }


def poll_run_op(creds, op_name: str, timeout: int = 300):
    url = f"https://run.googleapis.com/v2/{op_name}"
    deadline = time.time() + timeout
    while time.time() < deadline:
        r = requests.get(url, headers=auth_headers(creds), timeout=30)
        if r.status_code != 200:
            print(f"  poll {r.status_code}", flush=True)
            time.sleep(5)
            continue
        data = r.json()
        if data.get("done"):
            if "error" in data:
                raise RuntimeError(f"Operation failed: {data['error']}")
            return data
        print("  ... waiting ...", flush=True)
        time.sleep(8)
    raise TimeoutError("Operation timed out")


def create_job(creds):
    print(f"\nCreating Cloud Run Job: {JOB_NAME}")
    url = (
        f"https://run.googleapis.com/v2"
        f"/projects/{PROJECT_ID}/locations/{REGION}/jobs"
        f"?jobId={JOB_NAME}"
    )

    # Quota: CpuAllocPerProjectRegion allowed=20000 mCPU, MemAllocPerProjectRegion allowed=40GiB
    # With 1CPU/512MB per task => max parallelism=20 (20*1000=20000 mCPU, 20*512=10240 MiB OK)
    # taskCount=1000 means 1000 tasks run 20 at a time; each task handles its own chunk slice
    job_body = {
        "template": {
            "parallelism": 20,
            "taskCount": 1000,
            "template": {
                "maxRetries": 1,
                "timeout": "3600s",
                "containers": [
                    {
                        "image": AR_IMAGE,
                        "env": [
                            {"name": "CHUNK_URL",     "value": ""},
                            {"name": "OUTPUT_BUCKET", "value": ""},
                            {"name": "HTTP_TIMEOUT",  "value": "5"},
                            {"name": "CONCURRENCY",   "value": "400"},
                        ],
                        "resources": {
                            "limits": {
                                "cpu": "1",
                                "memory": "512Mi",
                            }
                        },
                    }
                ],
            },
        },
        "labels": {
            "managed-by": "deploy-script",
            "project": "namesilo-scanner",
        },
    }

    r = requests.post(url, headers=auth_headers(creds), json=job_body, timeout=60)
    print(f"  Response {r.status_code}")

    if r.status_code == 409:
        print("  Job already exists — patching...")
        patch_url = (
            f"https://run.googleapis.com/v2"
            f"/projects/{PROJECT_ID}/locations/{REGION}/jobs/{JOB_NAME}"
        )
        r2 = requests.patch(patch_url, headers=auth_headers(creds), json=job_body, timeout=60)
        print(f"  Patch response {r2.status_code}")
        if r2.status_code in (200, 201):
            resp = r2.json()
            op_name = resp.get("name", "")
            if op_name:
                poll_run_op(creds, op_name)
            return True
        else:
            print(f"  Patch error: {r2.text[:500]}")
            return False

    elif r.status_code in (200, 201):
        resp = r.json()
        print(f"  Response body keys: {list(resp.keys())}")
        op_name = resp.get("name", "")
        if op_name and "operations" in op_name:
            print(f"  Waiting for operation: {op_name}")
            poll_run_op(creds, op_name)
        print(f"  Job created OK!")
        return True
    else:
        print(f"  Error: {r.text[:800]}")
        return False


def main():
    creds = get_credentials()
    print(f"Auth: {creds.service_account_email}")
    print(f"Image: {AR_IMAGE}")

    ok = create_job(creds)
    if ok:
        console = f"https://console.cloud.google.com/run/jobs/details/{REGION}/{JOB_NAME}?project={PROJECT_ID}"
        print(f"\nSuccess!")
        print(f"Job name: {JOB_NAME}")
        print(f"Console:  {console}")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
