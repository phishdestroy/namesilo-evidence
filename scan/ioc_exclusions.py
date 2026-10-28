"""Apply reviewed, exact-domain corrections to derived IOC feeds."""
import csv
import io
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def excluded_domains(root=ROOT):
    path = root / 'data/ioc/exclusions.json'
    if not path.exists():
        return set()
    records = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(records, dict):
        raise ValueError('IOC exclusions must map exact domain names to review records')
    for domain, review in records.items():
        if (not re.fullmatch(r'[a-z0-9-]+(?:\.[a-z0-9-]+)+', domain)
                or not isinstance(review, dict) or not review.get('reason')):
            raise ValueError('Invalid IOC exclusion: ' + str(domain))
    return set(records)


def apply_exclusions(root=ROOT):
    """Remove excluded records without changing any other rows or raw registrations."""
    excluded = excluded_domains(root)
    changed = []
    if not excluded:
        return changed
    paths = ['data/ioc/feed_confirmed.txt', 'data/ioc/feed_high.txt',
             'data/ioc/intel_confirmed.txt']
    for folder in ('ioc', 'docs/ioc'):
        paths.extend(f'{folder}/{name}' for name in
                     ('domains_all_malicious.txt', 'domains_high.txt', 'indicators.csv'))
    for rel in paths:
        path = root / rel
        if not path.exists():
            continue
        original = path.read_bytes()
        text = original.decode('utf-8-sig')
        lines = text.splitlines(keepends=True)
        if path.suffix == '.csv':
            reader = csv.reader(io.StringIO(text, newline=''))
            header = next(reader, [])
            if 'domain' not in header:
                raise ValueError(f'{rel}: missing domain column')
            column = header.index('domain')
            end = reader.line_num
            kept = lines[:end]
            for row in reader:
                start, end = end, reader.line_num
                if row and len(row) <= column:
                    raise ValueError(f'{rel}: malformed CSV row')
                if not row or row[column].strip().lower().rstrip('.') not in excluded:
                    kept.extend(lines[start:end])
        else:
            kept = [line for line in lines
                    if line.strip().lower().rstrip('.') not in excluded]
            if len(kept) != len(lines):
                count = sum(bool(line.strip()) and not line.lstrip().startswith('#') for line in kept)
                kept = [re.sub(r' - \d+ entries', f' - {count} entries', line)
                        if line.startswith('#') else line for line in kept]
        bom = b'\xef\xbb\xbf' if original.startswith(b'\xef\xbb\xbf') else b''
        updated = bom + ''.join(kept).encode('utf-8')
        if updated != original:
            path.write_bytes(updated)
            changed.append(rel)
    return changed


if __name__ == '__main__':
    print(json.dumps({'changed': apply_exclusions()}))
