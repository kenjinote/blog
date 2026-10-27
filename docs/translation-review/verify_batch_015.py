"""Run extracted RSA teaching examples and compare their math with built HTML.

Example: python docs/translation-review/verify_batch_015.py SITE --languages ja en --output NEW.json
The language selection is explicit: running a fixture does not record a review.
No generated secret keys, OAEP/PSS implementation or security certification.
"""

import argparse
import contextlib
import io
import json
import math
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

from verify_batch_013_rendering import ArticleText, expressions

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from translation_reviews import digest

FOLDER = ROOT / "content/post/rsa暗号の仕組みを高校生でもわかるように説明する"
SLUG = "rsa-encryption-math-explained-for-beginners"


def check_rejection(function, arguments, exception):
    try:
        function(*arguments)
    except exception:
        return
    raise AssertionError((function.__name__, arguments, exception.__name__))


def verify(site, languages):
    assert len(languages) == len(set(languages))
    baseline = (FOLDER/"index.md").read_text(encoding="utf-8")
    baseline_blocks = re.findall(r"^```python\n(.*?)^```", baseline, re.M | re.S)
    baseline_math = re.findall(r"^\$\$(.*?)\$\$$", baseline, re.M | re.S)
    baseline_links = re.findall(r"\]\((https://[^)]+)\)", baseline)
    files = []
    for language in languages:
        path = FOLDER/("index.md" if language == "ja" else f"index.{language}.md")
        text = path.read_text(encoding="utf-8")
        blocks = re.findall(r"^```python\n(.*?)^```", text, re.M | re.S)
        assert len(blocks) == 1 and blocks == baseline_blocks
        assert re.findall(r"^\$\$(.*?)\$\$$", text, re.M | re.S) == baseline_math
        assert re.findall(r"\]\((https://[^)]+)\)", text) == baseline_links
        assert len(baseline_links) == 4
        graphs = re.findall(r"^```mermaid\n(.*?)^```", text, re.M | re.S)
        assert [g.count("-->")+g.count("-.->") for g in graphs] == [8, 14, 5]
        namespace, stdout = {}, io.StringIO()
        with contextlib.redirect_stdout(stdout):
            exec(compile(blocks[0], str(path), "exec"), namespace)
        n, e, d = namespace["N"], namespace["e"], namespace["d"]
        assert (n, e, d, namespace["ciphertext"], namespace["decrypted_message"]) == (143, 7, 103, 48, 9)
        primitive, inverse = namespace["rsa_primitive_demo"], namespace["mod_inverse"]
        assert sum(math.gcd(m, n) != 1 for m in range(n)) == 23
        for value in range(n):
            assert primitive(primitive(value, e, n), d, n) == value
            assert primitive(primitive(value, d, n), e, n) == value
        rejects = [
            (inverse, (1, 120), ValueError), (inverse, (7, 1), ValueError),
            (inverse, (6, 120), ValueError), (inverse, (121, 120), ValueError),
            (inverse, (-7, 120), ValueError), (inverse, (True, 120), TypeError),
            (inverse, (7, 120.0), TypeError),
            (primitive, (-1, 7, 143), ValueError), (primitive, (143, 7, 143), ValueError),
            (primitive, (144, 7, 143), ValueError), (primitive, (1, 0, 143), ValueError),
            (primitive, (1, -7, 143), ValueError), (primitive, (1, 7, 0), ValueError),
            (primitive, (1, 7, 1), ValueError), (primitive, (True, 7, 143), TypeError),
            (primitive, (1, 7.0, 143), TypeError), (primitive, (1, 7, 143.0), TypeError),
            (primitive, (1.5, 7, 143), TypeError),
        ]
        for function, arguments, exception in rejects:
            check_rejection(function, arguments, exception)
        assert len(rejects) == 18
        assert len(str(2**2047)) == len(str(2**2048-1)) == 617
        assert sum(math.gcd(a, n) == 1 for a in range(1, n+1)) == 120
        total = n-120+1
        discriminant = total*total-4*n
        assert math.isqrt(discriminant)**2 == discriminant
        assert {(total+math.isqrt(discriminant))//2, (total-math.isqrt(discriminant))//2} == {11, 13}
        dictionary = {pow(m, e, n): m for m in range(n)}
        assert len(dictionary) == n and dictionary[48] == 9
        for m in range(n):
            for r in (1, 2, 11, 13):
                changed = (pow(m, e, n)*pow(r, e, n)) % n
                assert pow(changed, d, n) == (m*r) % n
        assert pow(2, e, n) == 128
        html = (site/("" if language == "ja" else language)/"p"/SLUG/"index.html").read_text(encoding="utf-8")
        parser = ArticleText()
        parser.feed(html)
        expected = expressions(re.sub(r"^```.*?^```[^\n]*", "", text, flags=re.M | re.S))
        assert expected == expressions("".join(parser.parts)), language
        assert len(re.findall(r'<pre class=(?:"mermaid"|mermaid)>', html)) == 3
        for marker in ["rsa_primitive_demo", "All 143 representatives round-trip", "RSASSA-PSS", "RSAES-OAEP", "617", "190"]:
            assert marker in html, (language, marker)
        for marker in ['slug: "'+SLUG+'"', 'date: "2026-09-11T13:00:00+09:00"', 'image: "img/eyecatch.jpg"']:
            assert marker in text
        assert (FOLDER/"img/eyecatch.jpg").is_file()
        modern_link = ("" if language == "ja" else "/"+language)+"/p/modern-cryptography-public-key-hash-signature/"
        assert modern_link in text and modern_link in html
        files.append({"language": language, "path": path.relative_to(ROOT/"content").as_posix(),
                      "hash": digest(path), "standalonePythonBlocks": 1,
                      "stdout": stdout.getvalue(), "roundTripRepresentativesEachDirection": 143,
                      "nonCoprimeRepresentatives": 23, "invalidCasesRejected": len(rejects),
                      "rawRsaMalleabilityCases": 572, "rawSignatureForgery": {"s": 2, "m": 128},
                      "displayMath": len(baseline_math), "mermaidEdges": [8, 14, 5],
                      "renderedTeXExpressions": sum(expected.values()), "passed": True})
    return {"version": 1, "checkedAt": datetime.now(timezone(timedelta(hours=9))).isoformat(),
            "python": sys.version.split()[0], "files": files, "site": str(site), "allPassed": True,
            "scope": "Only selected article versions; extracted code execution, public toy arithmetic, exact math and generated markers/links.",
            "limitations": "Does not record semantic reviews or certify OAEP/PSS, general RSA security, constant-time behavior, native-language quality or visual rendering."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path)
    parser.add_argument("--languages", nargs="+", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("Preserve prior evidence; choose a new output path.")
    result = verify(args.site, args.languages)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"languages": args.languages, "allPassed": result["allPassed"], "TeXExpressions": sum(f["renderedTeXExpressions"] for f in result["files"])}))
