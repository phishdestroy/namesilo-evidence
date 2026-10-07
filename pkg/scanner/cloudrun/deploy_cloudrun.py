#!/usr/bin/env python3
"""
Deploy domain scanner to GCP Cloud Run Jobs.

Steps:
1. Create Artifact Registry Docker repository "scanner" in us-central1
2. Build Docker image via Cloud Build (source tarball upload)
3. Create Cloud Run Job

Uses service account key for authentication.
"""
import json
import os
import sys
import tarfile
import io
import time
import requests
from pathlib import Path

import google.auth
import google.auth.transport.requests
from google.oauth2 import service_account

# ── Config ─────────────────────────────────────────────────────────────────

PROJECT_ID   = os.environ.get("GCP_PROJECT_ID", "")
REGION       = os.environ.get("GCP_REGION", "us-central1")
REPO_NAME    = "scanner"
IMAGE_NAME   = "domain-scanner"
IMAGE_TAG    = "latest"
JOB_NAME     = "domain-scanner-job"
SA_KEY_PATH  = os.environ.get("GCP_SA_KEY_PATH", "")
SOURCE_DIR   = Path(__file__).parent / "scanner"

SCOPES = [
    "https://www.googleapis.com/auth/cloud-platform",
]

AR_IMAGE = (
    f"{REGION}-docker.pkg.dev/{PROJECT_ID}/{REPO_NAME}/{IMAGE_NAME}:{IMAGE_TAG}"
)


# ── Auth ───────────────────────────────────────────────────────────────────

def get_credentials():
    creds = service_account.Credentials.from_service_account_file(
        SA_KEY_PATH, scopes=SCOPES
    )
    req = google.auth.transport.requests.Request()
    creds.refresh(req)
    return creds


def auth_headers(creds) -> dict:
    req = google.auth.transport.requests.Request()
    creds.refresh(req)
    return {
        "Authorization": f"Bearer {creds.token}",
        "Content-Type": "application/json",
    }


# ── Step 1: Create Artifact Registry Repository ───────────────────────────

def create_artifact_registry_repo(creds):
    print("\n[1] Creating Artifact Registry repository...")
    url = (
        f"https://artifactregistry.googleapis.com/v1"
        f"/projects/{PROJECT_ID}/locations/{REGION}/repositories"
        f"?repositoryId={REPO_NAME}"
    )
    body = {
        "format": "DOCKER",
        "description": "Domain scanner Docker images",
    }
    headers = auth_headers(creds)
    headers["Content-Type"] = "application/json"

    r = requests.post(url, headers=headers, json=body, timeout=30)

    if r.status_code == 409:
        print(f"  Repository already exists — OK")
        return True
    elif r.status_code in (200, 201):
        resp = r.json()
        op_name = resp.get("name", "")
        print(f"  Repository creation started: {op_name}")
        if op_name:
            wait_for_operation(creds, op_name, "artifactregistry")
        print(f"  Repository created: {REPO_NAME}")
        return True
    else:
        print(f"  ERROR {r.status_code}: {r.text[:500]}")
        return False


def wait_for_operation(creds, op_name: str, api: str, timeout: int = 300):
    """Poll a long-running operation until done."""
    if api == "artifactregistry":
        base = "https://artifactregistry.googleapis.com/v1"
    elif api == "run":
        base = f"https://run.googleapis.com/v2"
    else:
        base = f"https://{api}.googleapis.com/v1"

    url = f"{base}/{op_name}"
    deadline = time.time() + timeout
    while time.time() < deadline:
        r = requests.get(url, headers=auth_headers(creds), timeout=30)
        if r.status_code != 200:
            print(f"  Operation poll error {r.status_code}: {r.text[:200]}")
            time.sleep(5)
            continue
        data = r.json()
        if data.get("done"):
            if "error" in data:
                raise RuntimeError(f"Operation failed: {data['error']}")
            return data
        pct = data.get("metadata", {}).get("progressPercent", "?")
        print(f"  ... waiting (progress={pct}%))", flush=True)
        time.sleep(10)
    raise TimeoutError(f"Operation {op_name} did not complete in {timeout}s")


# ── Step 2: Cloud Build — upload source tarball ───────────────────────────

def build_docker_image(creds):
    print("\n[2] Building Docker image via Cloud Build...")

    # 2a. Upload source tarball to GCS staging bucket
    tarball = _make_source_tarball()
    staging_bucket = f"{PROJECT_ID}_cloudbuild"
    object_name = f"source/domain-scanner-{int(time.time())}.tar.gz"

    print(f"  Uploading source tarball ({len(tarball)} bytes) to gs://{staging_bucket}/{object_name}...")
    gcs_url = f"https://storage.googleapis.com/upload/storage/v1/b/{staging_bucket}/o?uploadType=media&name={object_name}"
    headers = auth_headers(creds)
    headers["Content-Type"] = "application/gzip"
    r = requests.post(gcs_url, headers=headers, data=tarball, timeout=120)
    if r.status_code not in (200, 201):
        # Try creating the bucket first
        print(f"  Upload failed ({r.status_code}), trying to create staging bucket...")
        _create_gcs_bucket(creds, staging_bucket)
        r = requests.post(gcs_url, headers=headers, data=tarball, timeout=120)
        if r.status_code not in (200, 201):
            print(f"  ERROR uploading source: {r.status_code} {r.text[:400]}")
            return False
    print(f"  Source uploaded OK")

    # 2b. Submit Cloud Build
    build_body = {
        "source": {
            "storageSource": {
                "bucket": staging_bucket,
                "object": object_name,
            }
        },
        "steps": [
            {
                "name": "gcr.io/cloud-builders/docker",
                "args": [
                    "build",
                    "-t", AR_IMAGE,
                    ".",
                ],
            }
        ],
        "images": [AR_IMAGE],
        "options": {
            "machineType": "E2_MEDIUM",
            "logging": "CLOUD_LOGGING_ONLY",
        },
        "timeout": "1200s",
    }

    build_url = f"https://cloudbuild.googleapis.com/v1/projects/{PROJECT_ID}/builds"
    headers = auth_headers(creds)
    headers["Content-Type"] = "application/json"

    print(f"  Submitting Cloud Build for image: {AR_IMAGE}")
    r = requests.post(build_url, headers=headers, json=build_body, timeout=60)
    if r.status_code not in (200, 201):
        print(f"  ERROR submitting build: {r.status_code} {r.text[:600]}")
        return False

    op = r.json()
    op_name = op.get("name", "")
    build_id = op.get("metadata", {}).get("build", {}).get("id", "")
    print(f"  Build started: {build_id or op_name}")
    print(f"  Waiting for build to complete (may take 3-10 min)...")

    # Poll the build directly
    if build_id:
        return _wait_for_build(creds, build_id)
    else:
        # Fall back to operation polling
        try:
            _poll_operation_cloudbuild(creds, op_name)
            return True
        except Exception as e:
            print(f"  Build wait error: {e}")
            return False


def _poll_operation_cloudbuild(creds, op_name: str, timeout: int = 900):
    url = f"https://cloudbuild.googleapis.com/v1/{op_name}"
    deadline = time.time() + timeout
    while time.time() < deadline:
        r = requests.get(url, headers=auth_headers(creds), timeout=30)
        if r.status_code != 200:
            time.sleep(10)
            continue
        data = r.json()
        if data.get("done"):
            if "error" in data:
                raise RuntimeError(f"Build operation failed: {data['error']}")
            return data
        print(f"  ... waiting for build ...", flush=True)
        time.sleep(20)
    raise TimeoutError("Cloud Build timed out")


def _wait_for_build(creds, build_id: str, timeout: int = 900) -> bool:
    url = f"https://cloudbuild.googleapis.com/v1/projects/{PROJECT_ID}/builds/{build_id}"
    deadline = time.time() + timeout
    last_status = ""
    while time.time() < deadline:
        r = requests.get(url, headers=auth_headers(creds), timeout=30)
        if r.status_code != 200:
            time.sleep(10)
            continue
        data = r.json()
        status = data.get("status", "")
        if status != last_status:
            print(f"  Build status: {status}", flush=True)
            last_status = status
        if status == "SUCCESS":
            print(f"  Build completed successfully!")
            return True
        elif status in ("FAILURE", "INTERNAL_ERROR", "TIMEOUT", "CANCELLED"):
            print(f"  Build failed with status: {status}")
            # Print build log URL
            log_url = data.get("logUrl", "")
            if log_url:
                print(f"  Build log: {log_url}")
            steps = data.get("steps", [])
            for step in steps:
                if step.get("status") in ("FAILURE",):
                    print(f"  Failed step: {step.get('name')} — {step.get('status')}")
            return False
        time.sleep(20)
    print("  Build timed out waiting")
    return False


def _create_gcs_bucket(creds, bucket_name: str):
    url = f"https://storage.googleapis.com/storage/v1/b?project={PROJECT_ID}"
    body = {
        "name": bucket_name,
        "location": REGION,
        "storageClass": "STANDARD",
    }
    headers = auth_headers(creds)
    headers["Content-Type"] = "application/json"
    r = requests.post(url, headers=headers, json=body, timeout=30)
    if r.status_code in (200, 201):
        print(f"  Created GCS bucket: {bucket_name}")
    elif r.status_code == 409:
        print(f"  GCS bucket already exists: {bucket_name}")
    else:
        print(f"  WARNING: could not create bucket {bucket_name}: {r.status_code} {r.text[:200]}")


def _make_source_tarball() -> bytes:
    """Create a tar.gz of the scanner/ directory."""
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as tar:
        for fpath in SOURCE_DIR.iterdir():
            if fpath.name.startswith(".") or fpath.name == "__pycache__":
                continue
            tar.add(str(fpath), arcname=fpath.name)
    return buf.getvalue()


# ── Step 3: Create Cloud Run Job ──────────────────────────────────────────

def create_cloud_run_job(creds):
    print("\n[3] Creating Cloud Run Job...")

    # Cloud Run Jobs API v2
    url = (
        f"https://run.googleapis.com/v2"
        f"/projects/{PROJECT_ID}/locations/{REGION}/jobs"
        f"?jobId={JOB_NAME}"
    )

    # Quota: CpuAllocPerProjectRegion = 20000 mCPU, so max parallelism with 1CPU/task = 20
    # 1000 tasks run 20 at a time sequentially; each handles its own chunk via CLOUD_RUN_TASK_INDEX
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
                            # CHUNK_URL and OUTPUT_BUCKET are set at execution time via --update-env-vars
                            {"name": "CHUNK_URL",     "value": ""},
                            {"name": "OUTPUT_BUCKET", "value": ""},
                            # CLOUD_RUN_TASK_INDEX is automatically injected by Cloud Run Jobs
                            # Map it to TASK_INDEX for our script
                            {"name": "TASK_INDEX",    "value": "0"},
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

    headers = auth_headers(creds)
    headers["Content-Type"] = "application/json"

    r = requests.post(url, headers=headers, json=job_body, timeout=60)

    if r.status_code == 409:
        print(f"  Job already exists — updating...")
        return _update_cloud_run_job(creds, job_body)
    elif r.status_code in (200, 201):
        resp = r.json()
        op_name = resp.get("name", "")
        print(f"  Job creation started (operation: {op_name})")
        if op_name:
            try:
                _poll_run_operation(creds, op_name)
            except Exception as e:
                print(f"  Operation polling error: {e}")
        print(f"  Job created: {JOB_NAME}")
        job_url = (
            f"https://console.cloud.google.com/run/jobs/details/"
            f"{REGION}/{JOB_NAME}?project={PROJECT_ID}"
        )
        print(f"  Console URL: {job_url}")
        return True
    else:
        print(f"  ERROR {r.status_code}: {r.text[:600]}")
        return False


def _update_cloud_run_job(creds, job_body: dict) -> bool:
    url = (
        f"https://run.googleapis.com/v2"
        f"/projects/{PROJECT_ID}/locations/{REGION}/jobs/{JOB_NAME}"
    )
    headers = auth_headers(creds)
    headers["Content-Type"] = "application/json"
    r = requests.patch(url, headers=headers, json=job_body, timeout=60)
    if r.status_code in (200, 201):
        resp = r.json()
        op_name = resp.get("name", "")
        if op_name:
            try:
                _poll_run_operation(creds, op_name)
            except Exception as e:
                print(f"  Operation polling error: {e}")
        print(f"  Job updated: {JOB_NAME}")
        return True
    else:
        print(f"  Update ERROR {r.status_code}: {r.text[:400]}")
        return False


def _poll_run_operation(creds, op_name: str, timeout: int = 300):
    url = f"https://run.googleapis.com/v2/{op_name}"
    deadline = time.time() + timeout
    while time.time() < deadline:
        r = requests.get(url, headers=auth_headers(creds), timeout=30)
        if r.status_code != 200:
            time.sleep(5)
            continue
        data = r.json()
        if data.get("done"):
            if "error" in data:
                raise RuntimeError(f"Operation failed: {data['error']}")
            return data
        print(f"  ... waiting for job operation ...", flush=True)
        time.sleep(10)
    raise TimeoutError(f"Cloud Run operation timed out")


# ── Main ───────────────────────────────────────────────────────────────────

def main():
    print("=== Cloud Run Job Deployment ===")
    print(f"Project:  {PROJECT_ID}")
    print(f"Region:   {REGION}")
    print(f"Image:    {AR_IMAGE}")
    print(f"Job:      {JOB_NAME}")

    creds = get_credentials()
    print(f"Auth OK: service account = {creds.service_account_email}")

    ok1 = create_artifact_registry_repo(creds)
    if not ok1:
        print("\nArtifact Registry step failed — aborting.")
        sys.exit(1)

    ok2 = build_docker_image(creds)
    if not ok2:
        print("\nDocker build failed — aborting.")
        sys.exit(1)

    ok3 = create_cloud_run_job(creds)
    if not ok3:
        print("\nCloud Run Job creation failed.")
        sys.exit(1)

    print("\n=== Deployment complete ===")
    print(f"Job name:  {JOB_NAME}")
    print(f"Image:     {AR_IMAGE}")
    print(f"Console:   https://console.cloud.google.com/run/jobs/details/{REGION}/{JOB_NAME}?project={PROJECT_ID}")
    print()
    print("To run the job:")
    print(f"  Set CHUNK_URL and OUTPUT_BUCKET, then execute the job via Cloud Console or:")
    print(f"  gcloud run jobs execute {JOB_NAME} --region={REGION} \\")
    print(f"    --update-env-vars CHUNK_URL=gs://BUCKET/chunk.jsonl,OUTPUT_BUCKET=gs://BUCKET \\")
    print(f"    --project={PROJECT_ID}")


if __name__ == "__main__":
    main()
