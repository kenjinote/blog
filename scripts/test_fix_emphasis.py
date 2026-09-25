import unittest
from pathlib import Path

from fix_emphasis import candidates, replace, validate


def document(body):
    return '---\ntitle: "**metadata**"\n---\n' + body


class EmphasisTests(unittest.TestCase):
    def test_cjk_punctuation(self):
        text = document('には**CDN (Content Delivery Network)**という。**正常**です。')
        self.assertEqual(replace(text, candidates(text)),
                         document('には<strong>CDN (Content Delivery Network)</strong>という。**正常**です。'))

    def test_protected_syntax(self):
        for body in [
            '```mermaid\ngraph TD\n A[前**CDN (x)**後]\n```',
            '~~~python\n前**CDN (x)**後\n~~~',
            '`前**CDN (x)**後`', '$前**CDN (x)**後$',
            '$$前**CDN (x)**後$$', r'\(前**CDN (x)**後\)',
            r'\[前**CDN (x)**後\]',
            '[前**CDN (x)**後](/p/example/)',
            '[link](https://example.com/**CDN(x)**)',
            '![前**CDN (x)**後](image.png)',
            '# 前**CDN (x)**後', '    前**CDN (x)**後',
            '<div>前**CDN (x)**後</div>', '{{< example >}}前**CDN (x)**後',
            r'前\*\*CDN (x)\*\*後',
            '前**CDN `code` (x)**後', '前**CDN [link](url) (x)**後',
        ]:
            with self.subTest(body=body):
                self.assertEqual(candidates(document(body)), [])

    def test_valid_emphasis_unchanged(self):
        self.assertEqual(candidates(document('**正常**です。 **CDN (x)** works. ***bold italic***')), [])

    def test_preserves_crlf_and_bom(self):
        text = '\ufeff' + document('前**CDN (x)**後\n').replace('\n', '\r\n')
        self.assertEqual(replace(text, candidates(text)), text.replace('**CDN (x)**', '<strong>CDN (x)</strong>'))

    def test_repeat(self):
        text = document('前**CDN (x)**後')
        fixed = replace(text, candidates(text))
        self.assertEqual(replace(fixed, candidates(fixed)), fixed)

    def test_actual_hugo_validation(self):
        good = document('前**CDN (x)**後\n\n```mermaid\ngraph TD\n A --> B\n```\n\n$e=mc^2$')
        # Equal strings in code must not be transformed by the expected-HTML check.
        ambiguous = document('前**CDN (x)**後\n\n`**CDN (x)**`')
        pages = [(Path(name), t, replace(t, candidates(t)), candidates(t))
                 for name, t in [('good.md', good), ('ambiguous.md', ambiguous)]]
        accepted, rejected = validate(pages)
        self.assertEqual([p[0].name for p in accepted], ['good.md'])
        self.assertEqual([p[0].name for p in rejected], ['ambiguous.md'])

    def test_partial_repair_keeps_typographic_quotes(self):
        text = document('前**CDN (x)**後。\n\n前**"quoted"**後。')
        spans = candidates(text)
        accepted, rejected = validate([(Path('mixed.md'), text, replace(text, spans), spans)])
        self.assertEqual(len(accepted), 1)
        self.assertEqual(len(rejected), 1)
        self.assertEqual(accepted[0][2], document('前<strong>CDN (x)</strong>後。\n\n前**"quoted"**後。'))


if __name__ == '__main__':
    unittest.main()
