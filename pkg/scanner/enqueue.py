"""
Step 2: Read domains_to_scan.jsonl → push in batches to SQS.
SQS batch = 10 messages, each message = 10 domains → 100 domains/call.
"""
import json
import sys
import time
import boto3
from config import SQS_QUEUE_URL, AWS_REGION, DOMAINS_FILE, SQS_BATCH_SIZE

sqs = boto3.client("sqs", region_name=AWS_REGION)

def chunked(iterable, n):
    buf = []
    for item in iterable:
        buf.append(item)
        if len(buf) == n:
            yield buf
            buf = []
    if buf:
        yield buf


SQS_MSG_PER_CALL = 10  # SQS max per send_message_batch


def run(start_line: int = 0):
    sent = 0
    domain_buf = []   # current message (SQS_BATCH_SIZE domains)
    msg_buf = []      # message queue for one batch call

    with open(DOMAINS_FILE, encoding="utf-8") as f:
        for lineno, line in enumerate(f):
            if lineno < start_line:
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                continue

            domain_buf.append(item)
            if len(domain_buf) < SQS_BATCH_SIZE:
                continue

            msg_buf.append(domain_buf)
            domain_buf = []

            if len(msg_buf) < SQS_MSG_PER_CALL:
                continue

            # One call = 10 messages × 10 domains = 100 domains
            _send_messages(msg_buf)
            sent += sum(len(m) for m in msg_buf)
            msg_buf = []

            if sent % 50_000 == 0:
                print(f"  Enqueued: {sent:,} | line: {lineno:,}", flush=True)
                time.sleep(0.05)

    # Flush remaining items
    if domain_buf:
        msg_buf.append(domain_buf)
    if msg_buf:
        _send_messages(msg_buf)
        sent += sum(len(m) for m in msg_buf)

    print(f"\nDone. Enqueued: {sent:,}")


def _send_messages(batches: list):
    entries = []
    for i, batch in enumerate(batches):
        entries.append({
            "Id": str(i),
            "MessageBody": json.dumps(batch),
        })
    try:
        resp = sqs.send_message_batch(QueueUrl=SQS_QUEUE_URL, Entries=entries)
        if resp.get("Failed"):
            print(f"  WARNING: {len(resp['Failed'])} failed messages", file=sys.stderr)
    except Exception as e:
        print(f"  SQS error: {e}", file=sys.stderr)


if __name__ == "__main__":
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    run(start)
