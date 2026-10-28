"""Regression checks for appeal corrections surviving feed rebuilds."""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from ioc_exclusions import apply_exclusions


class AppealCorrectionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for folder in ('ioc', 'data/ioc', 'docs/ioc', 'scan', 'data/new'):
            (self.root / folder).mkdir(parents=True)
        self.write('data/ioc/exclusions.json', json.dumps({
            'appealed.example': {'reason': 'Reviewed correction'}
        }))

    def write(self, path, value):
        (self.root / path).write_bytes(value.encode('utf-8'))

    def test_exact_domain_only_preserves_registration_and_csv_bytes(self):
        self.write('ioc/domains_all_malicious.txt',
                   '# IOC - 3 entries\r\nappealed.example\r\nx.appealed.example\r\nother.example\r\n')
        source = '\ufeffdomain,category,severity,threat_sources\r\n'
        keep = 'other.example,MALWARE,HIGH,"source one\r\nsource two"\r\n'
        self.write('ioc/indicators.csv', source + 'appealed.example,MALWARE,MEDIUM,\r\n' + keep)
        self.write('data/new/registration.txt', 'appealed.example\n')
        changed = apply_exclusions(self.root)
        self.assertEqual(set(changed), {'ioc/domains_all_malicious.txt', 'ioc/indicators.csv'})
        self.assertEqual((self.root / 'ioc/indicators.csv').read_bytes(), (source + keep).encode('utf-8'))
        self.assertEqual((self.root / 'ioc/domains_all_malicious.txt').read_bytes(),
                         b'# IOC - 2 entries\r\nx.appealed.example\r\nother.example\r\n')
        self.assertEqual((self.root / 'data/new/registration.txt').read_bytes(), b'appealed.example\n')
        self.assertEqual(apply_exclusions(self.root), [])

    def test_rebuild_does_not_reintroduce_domain_from_legacy_or_brand_inputs(self):
        source = Path(__file__).parent
        for name in ('ioc_exclusions.py', 'build_ioc_simple.py', 'build_feed_ioc.py'):
            shutil.copyfile(source / name, self.root / 'scan' / name)
        self.write('data/ioc/brand_domains.json', json.dumps({
            'keywords': {'wallet': ['appealed.example', 'retained.example']}
        }))
        self.write('data/ioc/serial_registrants.json', json.dumps({
            'registrants': [{'count': 10, 'domains': ['appealed.example', 'serial.example']}] 
        }))
        for path in ('data/ioc/feed_confirmed.txt', 'data/ioc/feed_high.txt',
                     'ioc/domains_all_malicious.txt', 'ioc/domains_high.txt'):
            self.write(path, 'appealed.example\nretained.example\n')
        self.write('ioc/indicators.csv',
                   'domain,category,severity,threat_sources\nappealed.example,MALWARE,MEDIUM,\n')
        for script in ('build_ioc_simple.py', 'build_feed_ioc.py'):
            subprocess.run([sys.executable, str(self.root / 'scan' / script)],
                           cwd=self.root, check=True, capture_output=True)
        for folder in ('ioc', 'docs/ioc'):
            for path in (self.root / folder).glob('*'):
                self.assertNotIn('appealed.example', path.read_text(encoding='utf-8-sig'))
        feed = json.loads((self.root / 'docs/feed-ioc.json').read_text())
        self.assertEqual({r['domain'] for r in feed['domains']}, {'retained.example', 'serial.example'})
        self.assertEqual(feed['total'], 2)

    def test_missing_file_is_noop_and_invalid_config_fails_before_writes(self):
        path = self.root / 'data/ioc/exclusions.json'
        path.unlink()
        self.assertEqual(apply_exclusions(self.root), [])
        self.write('ioc/domains_high.txt', 'retained.example\n')
        self.write('data/ioc/exclusions.json', '{"*.example": {"reason": "Invalid wildcard"}}')
        with self.assertRaises(ValueError):
            apply_exclusions(self.root)
        self.assertEqual((self.root / 'ioc/domains_high.txt').read_bytes(), b'retained.example\n')


if __name__ == '__main__':
    unittest.main()
