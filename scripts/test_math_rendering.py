"""Check TeX survives both Goldmark and HTML minification as DOM text."""

import json
import shutil
import subprocess
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TextParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.tags = []

    def handle_data(self, data):
        self.parts.append(data)

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)


class MathRenderingTest(unittest.TestCase):
    def test_math_is_text_in_minified_and_unminified_html(self):
        inline = r"1<e<\phi(N)"
        block = r"\begin{aligned}M<N &\quad p>3\\ A&B\end{aligned}"
        body = (
            f"Choose ${inline}$. The implementation uses $e=65537$.\n\n"
            f"$$\n{block}\n$$\n\n"
            r"Other delimiters: \(x_i<Y\) and" + "\n\n"
            r"\[a&b<c\]" + "\n\n"
            "```text\n$literal<CODE$\n```\n\n"
            "[Following LINK](https://example.org/next/)\n"
        )
        with tempfile.TemporaryDirectory(prefix="kenji-math-") as directory:
            fixture = Path(directory)
            config = {
                "baseURL": "https://example.org/",
                "markup": {"goldmark": {"extensions": {"passthrough": {
                    "enable": True,
                    "delimiters": {
                        "inline": [["$", "$"], [r"\(", r"\)"]],
                        "block": [["$$", "$$"], [r"\[", r"\]"]],
                    },
                }}, "renderer": {"unsafe": True}}},
            }
            files = {
                "hugo.json": json.dumps(config),
                "layouts/_default/single.html": "<!doctype html><html><body>{{ .Content }}</body></html>",
                "layouts/_default/list.html": "<!doctype html><html><body></body></html>",
                "content/test.md": "---\ntitle: Math\n---\n" + body,
            }
            for name, text in files.items():
                path = fixture / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8")
            hook = Path("layouts/_default/_markup/render-passthrough.html")
            (fixture / hook).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / hook, fixture / hook)
            for minify in (False, True):
                with self.subTest(minify=minify):
                    destination = fixture / ("minified" if minify else "plain")
                    command = ["hugo", "--source", str(fixture), "--destination", str(destination)]
                    if minify:
                        command.append("--minify")
                    result = subprocess.run(command, capture_output=True, encoding="utf-8")
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                    parser = TextParser()
                    html = (destination / "test/index.html").read_text(encoding="utf-8")
                    parser.feed(html)
                    text = "".join(parser.parts)
                    for expected in (rf"\({inline}\)", "\\[\n" + block + "\n\\]", r"\(x_i<Y\)",
                                     r"\[a&b<c\]", "The implementation uses", r"\(e=65537\)",
                                     "$literal<CODE$", "Following LINK"):
                        self.assertIn(expected, text)
                    self.assertNotIn("e", parser.tags)
                    self.assertIn("https://example.org/next/", html)


if __name__ == "__main__":
    unittest.main()
