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
    def test_unwrap_only_reviewed_ordinary_verb(self):
        raw = '[Go](/en/p/languages/)'
        prefix = '---\ntitle: Test\n---\n\n'
        source = prefix + raw + ' is a language.\n\n' + raw + ' beyond engineering.'
        item = {'link': raw, 'context': raw + ' beyond engineering.', 'reason': 'misleading'}
        self.assertEqual(audit.unwrap_reviewed_link(source, item, {'/en/p/languages/'}),
                         prefix + raw + ' is a language.\n\nGo beyond engineering.')

    def test_unwrap_rejects_protected_or_unpublished_link(self):
        raw = '[Go](/en/p/languages/)'
        for source in ['# ' + raw, '`' + raw + '`', '$' + raw + '$',
                       '```mermaid\n' + raw + '\n```', '<div>' + raw + '</div>']:
            with self.subTest(source=source), self.assertRaises(ValueError):
                audit.unwrap_reviewed_link('---\ntitle: Test\n---\n\n' + source, {'link': raw, 'context': raw, 'reason': 'misleading'}, {'/en/p/languages/'})
        with self.assertRaises(ValueError):
            audit.unwrap_reviewed_link(raw, {'link': raw, 'context': raw, 'reason': 'misleading'}, {'/de/p/languages/'})
        with self.assertRaises(ValueError):
            audit.unwrap_reviewed_link('---\ntitle: Test\n---\n\n' + raw, {'link': raw, 'context': raw, 'reason': 'duplicate'}, {'/en/p/languages/'})
        external = '[Go](https://example.org/en/p/languages/)'
        with self.assertRaises(ValueError):
            audit.unwrap_reviewed_link('---\ntitle: Test\n---\n\n' + external,
                                       {'link': external, 'context': external, 'reason': 'misleading'}, {'/en/p/languages/'})

    def test_unwrap_retains_suffix_and_other_duplicate_link(self):
        source = '---\ntitle: Test\n---\n\n[Pipeline](/de/p/cicd/) and [Workflow](/de/p/cicd/)s.'
        item = {'link': '[Workflow](/de/p/cicd/)', 'context': 'and [Workflow](/de/p/cicd/)s.', 'reason': 'duplicate'}
        self.assertEqual(audit.unwrap_reviewed_link(source, item, {'/de/p/cicd/'}),
                         '---\ntitle: Test\n---\n\n[Pipeline](/de/p/cicd/) and Workflows.')

    def test_explicit_context_preserves_inline_html(self):
        source = '---\ntitle: Test\n---\n\nAn <strong>Introduction</strong> Euler explained waves.<br>\n'
        result, count = audit.link_reviewed_context(source, 'Euler', 'Euler explained', '/en/p/euler/')
        self.assertEqual(count, 1)
        self.assertEqual(result, source.replace('Euler', '[Euler](/en/p/euler/)'))

    def test_explicit_context_rejects_protected_spans(self):
        for source in ['# Euler\n', '`Euler`', '$Euler$', '[Euler](/existing/)', '```text\nEuler\n```', '<strong title="Euler">Title</strong>', '<div>Euler</div>']:
            with self.subTest(source=source), self.assertRaises(ValueError):
                audit.link_reviewed_context('---\ntitle: Test\n---\n\n' + source, 'Euler', 'Euler', '/en/p/euler/')

    def test_reviewed_math_literal_is_preserved_and_protected(self):
        source = '---\ntitle: Test\n---\n\nEuler calculated $2 V_0$.'
        result, _ = audit.link_reviewed_context(source, 'Euler', 'Euler', '/en/p/euler/', ['$2 V_0$'])
        self.assertEqual(result, source.replace('Euler', '[Euler](/en/p/euler/)'))
        with self.assertRaises(ValueError):
            audit.link_reviewed_context(source, 'V_0', 'V_0', '/en/p/euler/', ['$2 V_0$'])

    def test_mermaid_repair_preserves_edge_label(self):
        edge = '    A -->|Pressure (>140 dB)| B'
        self.original += '\n```mermaid\nflowchart TD\n' + edge + '\n```\n'
        self.source.write_text(self.original, encoding='utf-8')
        self.item['source_sha256'] = hashlib.sha256(self.source.read_bytes()).hexdigest()
        self.item['mermaid_edge_labels'] = [edge]
        self.run_plan()
        updated = self.source.read_text(encoding='utf-8')
        self.assertIn('    A -- "Pressure (>140 dB)" --> B', updated)
        self.assertNotIn(edge, updated)

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

    def test_multiline_categories_preserve_crlf_and_other_content(self):
        old_field = 'categories:\n  - "business"\n  - "web-marketing"'
        self.original = self.original.replace('categories: ["business", "web-marketing"]', old_field).replace('\n', '\r\n')
        self.source.write_bytes(self.original.encode('utf-8'))
        self.item['source_sha256'] = hashlib.sha256(self.source.read_bytes()).hexdigest()
        self.item['links'] = []
        self.item['categories'] = {'before': ['business', 'web-marketing'], 'after': ['business'], 'source_field': old_field}
        p = self.root / 'content/categories/business/_index.en.md'
        p.parent.mkdir(parents=True)
        p.write_text('---\ntitle: Business\n---\n', encoding='utf-8')
        self.run_plan()
        expected = self.original.replace(old_field.replace('\n', '\r\n'), 'categories: ["business"]').replace('[Subject](/en/p/source/) studied', 'Subject studied')
        self.assertEqual(self.source.read_bytes(), expected.encode('utf-8'))

    def test_existing_destination_not_nested_or_duplicated(self):
        self.original = self.original.replace('studied Euler.', 'studied [Euler](/en/p/euler/).')
        self.source.write_text(self.original, encoding='utf-8')
        self.item['source_sha256'] = hashlib.sha256(self.source.read_bytes()).hexdigest()
        self.run_plan()
        updated = self.source.read_text(encoding='utf-8')
        self.assertEqual(updated.count('[Euler](/en/p/euler/)'), 1)
        self.assertEqual(updated, self.original.replace('[Subject](/en/p/source/) studied', 'Subject studied'))

    def test_explicit_quoted_self_link_unwrap_preserves_label(self):
        broken = "['Subject](/en/p/'source'/)"
        self.original += '\n' + broken + "' explained.\n"
        self.source.write_text(self.original, encoding='utf-8')
        self.item['source_sha256'] = hashlib.sha256(self.source.read_bytes()).hexdigest()
        self.item['broken_self_links'] = [broken]
        self.run_plan()
        self.assertIn("'Subject' explained.", self.source.read_text(encoding='utf-8'))

    def test_quoted_external_link_cannot_be_unwrapped_as_self(self):
        broken = "[Subject](https://example.com/en/p/'source'/)"
        self.original += '\n' + broken + '\n'
        self.source.write_text(self.original, encoding='utf-8')
        self.item['source_sha256'] = hashlib.sha256(self.source.read_bytes()).hexdigest()
        self.item['broken_self_links'] = [broken]
        with self.assertRaisesRegex(ValueError, 'not a quoted self-link'):
            self.run_plan()
        self.assertEqual(self.source.read_text(encoding='utf-8'), self.original)


if __name__ == '__main__':
    unittest.main()
