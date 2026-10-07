#!/usr/bin/env python3
"""Fetch fingerprint.py from dump-srv via SSH."""
import paramiko

HOST = "[redacted]"
USER = "root"
PASS = "[redacted]"
PORT = 22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(HOST, port=PORT, username=USER, password=PASS, timeout=30)

sftp = client.open_sftp()
with sftp.open('/root/scanner/fingerprint.py', 'r') as f:
    content = f.read().decode('utf-8')

print(content)
sftp.close()
client.close()
