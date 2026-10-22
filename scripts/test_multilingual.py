"""Small Hugo integration fixtures plus regression tests for translation review states."""

import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

import check_multilingual
import translation_reviews

ROOT = Path(__file__).resolve().parents[1]


class MultilingualTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix="kenji-multilingual-")
        cls.fixture = Path(cls.temp.name)
        files = {
            "hugo.json": json.dumps({
                "baseURL": "https://example.org/", "defaultContentLanguage": "ja",
                "languages": {code: {"languageName": name, "weight": weight} for code, name, weight in
                              [("ja", "日本語", 1), ("en", "English", 2), ("fr", "Français", 3)]},
            }),
            "layouts/_default/baseof.html": '''<!doctype html><html lang="{{ .Language.Lang }}"><head>
<link rel="canonical" href="{{ .Permalink }}">{{ partial "head/hreflang.html" . }}</head>
<body><aside><ol>{{ partial "sidebar/language-switch.html" . }}</ol></aside><main>{{ .Content }}</main>
{{ $js := resources.Get "ts/language.ts" | js.Build }}<script defer src="{{ $js.RelPermalink }}"></script></body></html>''',
            "layouts/_default/single.html": '{{ define "main" }}{{ end }}',
            "layouts/_default/list.html": '{{ define "main" }}{{ end }}',
            "layouts/partials/helper/icon.html": "",
            "content/post/shared/index.md": '---\ntitle: 日本語記事\nslug: japanese-slug\n---\n日本語本文',
            "content/post/shared/index.en.md": '---\ntitle: English article\nslug: english-slug\n---\nEnglish body',
            "content/post/only-ja/index.md": '---\ntitle: 未翻訳記事\n---\n日本語のみ',
            "content/post/no-ja/index.en.md": '---\ntitle: Original English\n---\nEnglish',
            "content/post/no-ja/index.fr.md": '---\ntitle: Français\n---\nFrançais',
        }
        for path, text in files.items():
            target = cls.fixture / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text, encoding="utf-8")
        for path in ("layouts/partials/head/hreflang.html", "layouts/partials/sidebar/language-switch.html",
                     "data/languages.yaml", "assets/ts/language.ts"):
            target = cls.fixture / path
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / path, target)
        subprocess.run(["hugo", "--source", str(cls.fixture), "--quiet"], check=True)
        cls.public = cls.fixture / "public"

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def page(self, path):
        parser = check_multilingual.PageParser()
        parser.feed((self.public / path / "index.html").read_text(encoding="utf-8"))
        return parser

    def test_all_reciprocal(self):
        check_multilingual.validate(self.public)

    def test_translated_slug_and_missing_language(self):
        page = self.page("post/japanese-slug")
        self.assertEqual(page.options["en"], "https://example.org/en/post/english-slug/")
        self.assertEqual(page.options["fr"], "")
        self.assertTrue(page.status)

    def test_untranslated_page_does_not_link_to_home(self):
        page = self.page("post/only-ja")
        self.assertEqual(page.options["en"], "")
        self.assertEqual(page.alternates, {"ja": page.canonical, "x-default": page.canonical})

    def test_no_japanese_counterpart_has_no_x_default(self):
        self.assertNotIn("x-default", self.page("en/post/no-ja").alternates)

    def test_duplicate_rejected(self):
        parser = check_multilingual.PageParser()
        with self.assertRaisesRegex(AssertionError, "Duplicate hreflang"):
            parser.feed('<link rel="alternate" hreflang="en" href="https://example.org/">' * 2)

    def test_wrong_sidebar_destination_rejected(self):
        target = self.public / "post/japanese-slug/index.html"
        original = target.read_text(encoding="utf-8")
        try:
            target.write_text(original.replace('value="https://example.org/en/post/english-slug/"', 'value="https://example.org/en/"'), encoding="utf-8")
            with self.assertRaisesRegex(AssertionError, "Sidebar differs"):
                check_multilingual.validate(self.public)
        finally:
            target.write_text(original, encoding="utf-8")

    def test_non_reciprocal_translation_rejected(self):
        target = self.public / "en/post/english-slug/index.html"
        original = target.read_text(encoding="utf-8")
        # Remove a counterpart from one version only, including its selector option.
        import re
        broken = re.sub(r'<link rel="alternate" hreflang="ja"[^>]*>', "", original)
        broken = re.sub(r'<link rel="alternate" hreflang="x-default"[^>]*>', "", broken)
        broken = broken.replace('value="https://example.org/post/japanese-slug/"', 'value=""')
        try:
            target.write_text(broken, encoding="utf-8")
            with self.assertRaisesRegex(AssertionError, "Non-reciprocal"):
                check_multilingual.validate(self.public)
        finally:
            target.write_text(original, encoding="utf-8")

    def test_review_invalidated_by_either_file(self):
        original_root = translation_reviews.ROOT
        translation_reviews.ROOT = self.fixture
        source, target = "post/shared/index.md", "post/shared/index.en.md"
        try:
            self.assertEqual(translation_reviews.status(target, source, {"reviews": {}}), "unreviewed")
            record = {"source": source, "sourceHash": translation_reviews.digest(self.fixture / "content" / source),
                      "translationHash": translation_reviews.digest(self.fixture / "content" / target)}
            ledger = {"reviews": {target: record}}
            self.assertEqual(translation_reviews.status(target, source, ledger), "current")
            record["translationHash"] = "0" * 64
            self.assertEqual(translation_reviews.status(target, source, ledger), "translation_changed")
            record["sourceHash"] = "0" * 64
            self.assertEqual(translation_reviews.status(target, source, ledger), "source_changed")
        finally:
            translation_reviews.ROOT = original_root


if __name__ == "__main__":
    unittest.main()
