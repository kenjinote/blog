import json
from pathlib import Path
import tempfile
import unittest

from internal_links import ROOT, link_text, load_rules, localizers
from extract_internal_link_terms import candidates

FM = '---\ntitle: ゴールドバッハの予想\n---\n\n'
WORD = 'ゴールドバッハの予想'
RULES = {WORD: '/p/goldbachs-conjecture/', 'Goldbach': '/p/goldbachs-conjecture/'}


class InternalLinksTest(unittest.TestCase):
    def test_plain_and_idempotent(self):
        source = FM + f'{WORD}と**{WORD}**。'
        updated, count = link_text(source, RULES)
        self.assertEqual(count, 2)
        self.assertTrue(updated.startswith(FM))
        self.assertEqual(link_text(updated, RULES), (updated, 0))

    def test_existing_links_images_references(self):
        for syntax in [f'[{WORD}](/p/a/)', f'![{WORD}](a.png)',
                       f'[{WORD}][ref]', f'[{WORD}]',
                       f'[outer [{WORD}]](/a(b)c/ "title")',
                       f'[code `]` {WORD}](/a/)',
                       f'[label](/path "a ) {WORD}")']:
            with self.subTest(syntax=syntax):
                source = FM + '本文 ' + syntax + ' ' + WORD
                updated, count = link_text(source, RULES)
                self.assertEqual(count, 1)
                self.assertIn(syntax, updated)

    def test_protected_syntax(self):
        for syntax in [f'${WORD}$', f'$${WORD}$$', f'\\({WORD}\\)', f'\\[{WORD}\\]',
                       f'`{WORD}`', f'`` a `{WORD}` ``',
                       f'```mermaid\ngraph TD\n\n A["{WORD}"]\n```',
                       f'~~~~mermaid\n{WORD}\n~~~\n{WORD}\n~~~~',
                       f'    {WORD}\n    code', f'> {WORD}\nlazy continuation',
                       f'## {WORD}', f'{WORD}\n=====',
                       f'[ref]: /{WORD}/', f'https://example.com/{WORD}',
                       f'{{#{WORD}}}']:
            with self.subTest(syntax=syntax):
                source = FM + syntax + '\n\n' + WORD
                updated, count = link_text(source, RULES)
                self.assertEqual(count, 1)
                self.assertIn(syntax, updated)

    def test_unclosed_syntax(self):
        for opening in ['$', '$$', '`', '```mermaid\n', '~~~\n', '\\(', '[', '[x](']:
            source = FM + opening + WORD + '\n\n' + WORD
            self.assertEqual(link_text(source, RULES), (source, 0))

    def test_html_shortcode_missing_frontmatter(self):
        for source in [FM + '<div>\n\n' + WORD + '\n</div>',
                       FM + '{{< example >}}\n\n' + WORD, WORD,
                       '---\ntitle: incomplete\n' + WORD]:
            self.assertEqual(link_text(source, RULES), (source, 0))

    def test_longest_match_and_word_boundary(self):
        source = FM + 'Goldbacher Goldbach ゴールドバッハの予想'
        updated, count = link_text(source, {**RULES, 'ゴールドバッハ': '/short/'})
        self.assertEqual(count, 2)
        self.assertIn('Goldbacher', updated)
        self.assertNotIn('/short/', updated)

    def test_newlines_bom_and_toml(self):
        for source in ['\ufeff' + FM.replace('\n', '\r\n') + WORD,
                       '+++\ntitle = "test"\n+++\n\n' + WORD]:
            updated, count = link_text(source, RULES)
            self.assertEqual(count, 1)
            self.assertEqual(updated.replace(f'[{WORD}]({RULES[WORD]})', WORD), source)

    def test_configuration_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            target = root / 'content/post/test/index.md'
            target.parent.mkdir(parents=True)
            target.write_text(FM, encoding='utf-8')
            config = root / 'rules.json'
            entry = {'article': 'content/post/test/index.md', 'keywords': [WORD]}
            config.write_text(json.dumps({'version': 1, 'articles': [entry]}))
            with self.assertRaises(ValueError):
                load_rules(config, root, {})
            published = {target: {'kind': 'page', 'permalink': 'https://kenji.blog/p/custom/'}}
            self.assertEqual(load_rules(config, root, published)['ja'][WORD][1], '/p/custom/')
            config.write_text(json.dumps({'version': 1, 'articles': [entry, entry]}))
            with self.assertRaises(ValueError):
                load_rules(config, root, published)

    def test_case_and_unicode_boundaries(self):
        rules = {'Conjecture de Goldbach': '/fr/p/goldbach/', 'теория': '/ru/p/theory/', 'نظرية': '/ar/p/theory/'}
        source = FM + 'conjecture de Goldbach. CONJECTURE DE GOLDBACH. теория теориятест نظرية نظريةطويلة'
        updated, count = link_text(source, rules)
        self.assertEqual(count, 4)
        self.assertIn('теориятест', updated)
        self.assertIn('نظريةطويلة', updated)
        self.assertEqual(link_text(updated, rules), (updated, 0))

    def test_acronyms_do_not_match_common_words(self):
        updated, count = link_text(FM + 'WHO who RAM ram FFT fft', {'WHO': '/who/', 'RAM': '/ram/', 'FFT': '/fft/'})
        self.assertEqual(count, 3)
        self.assertIn(' who ', updated)
        self.assertIn(' ram ', updated)

    def test_localization_uses_real_sibling_url(self):
        published = {
            ROOT / 'content/post/test/index.md': {'kind': 'page', 'permalink': 'https://kenji.blog/p/test/'},
            ROOT / 'content/post/test/index.fr.md': {'kind': 'page', 'permalink': 'https://kenji.blog/fr/p/custom-test/'},
        }
        localize = localizers(published)('fr')
        self.assertEqual(localize('/p/test/?x=1#heading'), '/fr/p/custom-test/?x=1#heading')
        self.assertEqual(localize('https://kenji.blog/p/test/'), 'https://kenji.blog/fr/p/custom-test/')
        for url in ['https://evil.example/p/test/', '/p/missing/', 'image.png']:
            self.assertEqual(localize(url), url)
        self.assertEqual(localizers(published)('de')('/p/test/'), '/p/test/')

    def test_localization_keeps_label_math_code_images(self):
        callback = lambda url: '/fr/p/test/' if url == '/p/test/' else url
        source = FM + '## [heading](/p/test/)\n\n[label](/p/test/ "title") ![image](/p/test/)\n\n`[code](/p/test/)` $[math](/p/test/)$'
        updated, count = link_text(source, {}, callback)
        self.assertEqual(count, 2)
        self.assertIn('![image](/p/test/)', updated)
        self.assertIn('`[code](/p/test/)` $[math](/p/test/)$', updated)
        self.assertIn('[label](/fr/p/test/ "title")', updated)
        self.assertEqual(link_text(updated, {}, callback), (updated, 0))

    def test_extraction_badges_and_topic(self):
        terms = candidates('[Biography] Charles Chaplin: His life', FM + '**Charles Chaplin** was an actor.')
        self.assertIn('Charles Chaplin', terms)
        self.assertNotIn('Biography', terms)
        self.assertIn('高速フーリエ変換', candidates('高速フーリエ変換（FFT）：説明', FM))
        self.assertIn('FFT', candidates('高速フーリエ変換（FFT）：説明', FM))
        self.assertTrue(candidates('Remove .DS_Store files', FM))
        self.assertTrue(candidates('Dijkstra and A* Algorithms: An introduction', FM))
        self.assertNotIn('C++', candidates('C++（WinHTTP）でSlackにメッセージを投稿する方法', FM + '**C++**'))
        self.assertNotIn('Easy', candidates('Easy! Record GIF animations', FM))
        self.assertNotIn('Physique', candidates('Physique : Le mécanisme de la supraconductivité', FM))
        self.assertNotIn('théorie des nombres', candidates('Louis Mordell : Un Géant de la Théorie des Nombres', FM + '**théorie des nombres**'))
        self.assertNotIn('TODO', candidates('Lista de películas (TODO)', FM))


if __name__ == '__main__':
    unittest.main()
