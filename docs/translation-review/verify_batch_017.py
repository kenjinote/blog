"""Validate explicitly selected factoring translations and minified HTML.

Independent arithmetic supplements actual prose review; this script never records
a translation review. The article has no executable blocks, only Mermaid diagrams.
Usage: python docs/translation-review/verify_batch_017.py SITE --languages ja en --output NEW.json
"""
import argparse
import json
import math
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone, timedelta
from pathlib import Path

from verify_batch_013_rendering import ArticleText, expressions

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from translation_reviews import digest

FOLDER = ROOT / "content/post/素因数分解と計算量"
SLUG = "prime-factorization-limits-big-o-notation"


def factor_by_trial(N):
    factors = []
    d = 2
    while d*d <= N:
        while N % d == 0:
            factors.append(d)
            N //= d
        d += 1
    if N > 1:
        factors.append(N)
    return factors


def independent_math():
    # Rerun the historical portable fixtures into a fresh temporary file without
    # modifying their original saved result or treating them as article code.
    with tempfile.TemporaryDirectory(prefix="kenji-factoring-") as directory:
        output = Path(directory) / "fixtures.json"
        subprocess.run([sys.executable, str(Path(__file__).with_name("verify_batch_017_source.py")),
                        "--output", str(output)], check=True, capture_output=True, text=True)
        fixtures = json.loads(output.read_text(encoding="utf-8"))
    assert fixtures["allPassed"]
    cases = 0
    # Compare direct divisor search with the complete-factorization certificates.
    for N in range(3, 301):
        factors = factor_by_trial(N)
        assert math.prod(factors) == N
        for K in range(2, N):
            yes = any(N % d == 0 for d in range(2, K+1))
            no_certificate = all(p > K for p in factors)
            assert yes != no_certificate
            cases += 1
    # Independent decision oracle followed by binary search and repeated removal.
    def decision(N, K):
        return any(N % d == 0 for d in range(2, K+1))
    def extract(N):
        result = []
        while N > 1:
            if N == 2 or not decision(N, N-1):
                result.append(N)
                break
            lo, hi = 2, N-1
            while lo < hi:
                mid = (lo+hi)//2
                if decision(N, mid):
                    hi = mid
                else:
                    lo = mid+1
            result.append(lo)
            N //= lo
        return result
    for N in range(2, 501):
        assert extract(N) == factor_by_trial(N)
    return {"priorFixturesRerun": fixtures["arithmeticReproductions"],
            "decisionVsCertificatesCases": cases, "decisionBinarySearchFactorizations": 499,
            "limitations": "Finite arithmetic examples, not proofs of asymptotic complexity, AKS, GNFS, Shor or cryptographic security."}


def verify(site, languages):
    assert languages and len(languages) == len(set(languages))
    original = (FOLDER / "index.md").read_text(encoding="utf-8-sig")
    displays = re.findall(r"^\$\$(.*?)^\$\$", original, re.M | re.S)
    assert len(displays) == 10
    external = {url for url in re.findall(r"\]\((https://[^)]+)\)", original)
                if not url.startswith("https://kenji.blog/")}
    assert len(external) == 9
    files = []
    for language in languages:
        path = FOLDER / ("index.md" if language == "ja" else f"index.{language}.md")
        text = path.read_text(encoding="utf-8-sig")
        assert re.findall(r"^\$\$(.*?)^\$\$", text, re.M | re.S) == displays
        assert len(re.findall(r"^## [1-6]\. ", text, re.M)) == 6
        fences = re.findall(r"^```([^\n]*)\n", text, re.M)
        assert fences == ["mermaid", "", "mermaid", ""]
        diagrams = re.findall(r"^```mermaid\n(.*?)^```", text, re.M | re.S)
        assert [diagram.count("-->") for diagram in diagrams] == [3, 2]
        links = re.findall(r"\]\((https://[^)]+)\)", text)
        assert {url for url in links if not url.startswith("https://kenji.blog/")} == external
        internal = "https://kenji.blog/" + ("" if language == "ja" else language+"/") + "p/modern-cryptography-public-key-hash-signature/"
        assert [url for url in links if url.startswith("https://kenji.blog/")] == [internal]
        assert (site / internal.removeprefix("https://kenji.blog/") / "index.html").is_file()
        assert 'date: "2026-09-11T23:00:00+09:00"' in text
        assert 'lastmod: "2026-10-28"' in text
        assert f'slug: "{SLUG}"' in text
        assert 'image: "img/eyecatch.jpg"' in text and (FOLDER / "img/eyecatch.jpg").is_file()
        source = re.sub(r"^```.*?^```[^\n]*", "", text, flags=re.M | re.S)
        html_path = site / ("" if language == "ja" else language) / "p" / SLUG / "index.html"
        html = html_path.read_text(encoding="utf-8")
        parser = ArticleText()
        parser.feed(html)
        rendered = "".join(parser.parts)
        expected, actual = expressions(source), expressions(rendered)
        checks = {"allTeXPreserved": expected == actual,
                  "strictBoundsPreserved": any(r"2^{b-1}\le N<2^b." in expression for expression in actual) and r"1<d<N" in actual,
                  "linksPreserved": all(url in html for url in links),
                  "mathEnabled": "katex" in html, "mermaidEnabled": "mermaid" in html,
                  "markersPreserved": all(marker in rendered for marker in ("51806", "2700", "829", "2047", "MPQS", "OAEP", "coNP")),
                  "convertedConstantPreserved": ("1,702" if language in ("fr", "de", "id", "ru") else "1.702") in rendered}
        files.append({"language": language, "path": path.relative_to(ROOT / "content").as_posix(),
                      "hash": digest(path), "displayFormulas": 10, "texExpressions": sum(expected.values()),
                      "diagrams": 2, "diagramEdges": [3, 2], "executableArticleBlocks": 0,
                      "missingMath": list((expected-actual).elements()), "unexpectedMath": list((actual-expected).elements()),
                      "checks": checks, "passed": all(checks.values())})
    return {"version": 1, "checkedAt": datetime.now(timezone(timedelta(hours=9))).isoformat(),
            "site": str(site), "scope": "Explicitly selected languages only; no automated prose-review or review-date recording.",
            "limitations": ["No executable article code; independent arithmetic only.", "No visual browser, native-speaker, full primary-paper proof or production cryptography audit."],
            "arithmetic": independent_math(), "files": files, "allPassed": all(f["passed"] for f in files)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path)
    parser.add_argument("--languages", nargs="+", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("Preserve existing evidence; use a new output path.")
    result = verify(args.site, args.languages)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"pages": len(result["files"]), "expressions": sum(f["texExpressions"] for f in result["files"]),
                      "passed": result["allPassed"], "failures": [f for f in result["files"] if not f["passed"]]}))
    sys.exit(0 if result["allPassed"] else 1)
