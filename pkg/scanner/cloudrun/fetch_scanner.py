#!/usr/bin/env python3
"""Fetch scanner files from dump-srv via SSH."""
import paramiko
import sys

HOST = "[redacted]"
USER = "root"
PASS = "[redacted]"
PORT = 22

def fetch_file(sftp, remote_path):
    with sftp.open(remote_path, 'r') as f:
        return f.read().decode('utf-8')

def main():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f"Connecting to {HOST}...")
    client.connect(HOST, port=PORT, username=USER, password=PASS, timeout=30)
    print("Connected.")

    sftp = client.open_sftp()

    files = [
        '/root/scanner/handler.py',
        '/root/scanner/local_scan.py',
    ]

    results = {}
    for path in files:
        try:
            content = fetch_file(sftp, path)
            results[path] = content
            print(f"\n{'='*60}")
            print(f"FILE: {path}")
            print('='*60)
            print(content)
        except Exception as e:
            print(f"ERROR reading {path}: {e}", file=sys.stderr)
            results[path] = None

    # Also try to list the scanner directory
    try:
        items = sftp.listdir('/root/scanner')
        print(f"\n{'='*60}")
        print("Directory /root/scanner contents:")
        print('='*60)
        for item in sorted(items):
            print(f"  {item}")
    except Exception as e:
        print(f"Could not list /root/scanner: {e}", file=sys.stderr)

    sftp.close()
    client.close()
    print("\nDone fetching files.")

if __name__ == "__main__":
    main()
