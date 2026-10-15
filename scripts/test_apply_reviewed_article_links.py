"""Regression checks for explicitly reviewed source-preserving edits."""
import contextlib
import hashlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import apply_reviewed_article_links as audit


class ReviewedEditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / 'content/post/source/index.en.md'
        self.target = self.root / 'content/post/euler/index.en.md'
        self.source.parent.mkdir(parents=True)
        self.target.parent.mkdir(parents=True)
        self.target.write_text('target', encoding='utf-8')
        self.original = ('---\ntitle: "Subject"\ncategories: ["business", "web-marketing"]\n---\n'
                         '# [Subject](/en/p/source/)\n\n'
                         '[Subject](/en/p/source/) studied Euler.\n\n'
                         '```text\nEuler [Subject](/en/p/source/)\n```\n\n'
                         '`Euler` and $Euler$.\n')
        self.source.write_text(self.original, encoding='utf-8')
        self.item = {'path': self.source.relative_to(self.root).as_posix(),
                     'source_sha256': hashlib.sha256(self.source.read_bytes()).hexdigest(),
                     'links': [{'term': 'Euler', 'target': self.target.relative_to(self.root).as_posix()}],
                     'category_decision': 'Reviewed fixture'}

    def run_plan(self):
        plan = self.root / 'plan.json'
        plan.write_text(json.dumps({'articles': [self.item]}), encoding='utf-8')
        pages = {self.source.resolve(): {'permalink': 'https://kenji.blog/en/p/source/'},
                 self.target.resolve(): {'permalink': 'https://kenji.blog/en/p/euler/'}}
        with patch.object(audit, 'ROOT', self.root), patch.object(audit, 'published_pages', return_value=pages), \
             patch.object(sys, 'argv', ['apply', str(plan), '--write']), contextlib.redirect_stdout(io.StringIO()):
            audit.main()

    def test_preserves_heading_code_math_and_adds_contextual_link(self):
        self.run_plan()
        updated = self.source.read_text(encoding='utf-8')
        expected = self.original.replace('[Subject](/en/p/source/) studied Euler.', 'Subject studied [Euler](/en/p/euler/).')
        self.assertEqual(updated, expected)
        with self.assertRaisesRegex(ValueError, 'Source changed'):
            self.run_plan()
        self.assertEqual(self.source.read_text(encoding='utf-8'), expected)

    def test_category_change_requires_existing_localized_definitions(self):
        self.item['categories'] = {'before': ['business', 'web-marketing'], 'after': ['business', 'marketing']}
        with self.assertRaisesRegex(ValueError, 'Missing localized category'):
            self.run_plan()
        self.assertEqual(self.source.read_text(encoding='utf-8'), self.original)
        for name in ['business', 'marketing']:
            p = self.root / 'content/categories' / name / '_index.en.md'
            p.parent.mkdir(parents=True)
            p.write_text('---\ntitle: "Category"\n---\n', encoding='utf-8')
        self.run_plan()
        expected = self.original.replace('[Subject](/en/p/source/) studied Euler.', 'Subject studied [Euler](/en/p/euler/).').replace('"web-marketing"', '"marketing"')
        self.assertEqual(self.source.read_text(encoding='utf-8'), expected)

    def test_cross_language_target_rejected_before_write(self):
        self.target = self.target.with_name('index.ja.md')
        self.item['links'][0]['target'] = self.target.relative_to(self.root).as_posix()
        with self.assertRaisesRegex(ValueError, 'Invalid target'):
            self.run_plan()
        self.assertEqual(self.source.read_text(encoding='utf-8'), self.original)

    def test_existing_destination_not_nested_or_duplicated(self):
        self.original = self.original.replace('studied Euler.', 'studied [Euler](/en/p/euler/).')
        self.source.write_text(self.original, encoding='utf-8')
        self.item['source_sha256'] = hashlib.sha256(self.source.read_bytes()).hexdigest()
        self.run_plan()
        updated = self.source.read_text(encoding='utf-8')
        self.assertEqual(updated.count('[Euler](/en/p/euler/)'), 1)
        self.assertEqual(updated, self.original.replace('[Subject](/en/p/source/) studied', 'Subject studied'))


if __name__ == '__main__':
    unittest.main()
