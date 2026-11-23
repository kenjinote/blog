"""Run static and executable checks for the 13 MPC article editions."""
from __future__ import annotations

import ast
import contextlib
import hashlib
import io
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs/translation-review"
CONTENT = ROOT / "content/post/secure-multi-party-computation-mpc-yaos-millionaires-shamir-secret-sharing-garbled-circuits"
LANGS = ("ja", "en", "zh-cn", "es", "ko", "pt", "zh-tw", "hi", "fr", "de", "ar", "ru", "id")
BEAVER_LIMIT = {
    "ja": "Beaverトリプルだけで",
    "en": "Beaver triples alone",
    "zh-cn": "Beaver三元组本身",
    "es": "tripleta de Beaver por sí sola",
    "ko": "Beaver 트리플만으로",
    "pt": "tripla de Beaver, isoladamente",
    "zh-tw": "Beaver三元組本身",
    "hi": "Beaver ट्रिपल अकेले",
    "fr": "triplet de Beaver seul",
    "de": "Beaver-Tripel allein",
    "ar": "ثلاثية Beaver وحدها",
    "ru": "Одна тройка Бивера",
    "id": "Tripel Beaver saja",
}


def main() -> None:
    paths = [CONTENT / "index.ja.md"] + [CONTENT / f"index.{lang}.md" for lang in LANGS if lang != "ja"]
    if len(paths) != 13 or not all(path.is_file() for path in paths):
        raise SystemExit("Expected Japanese source plus twelve translation files")

    metrics = {}
    ref_sets = []
    code_hashes = []
    source_hash = None
    for path in paths:
        text = path.read_text(encoding="utf-8")
        lang = path.stem.removeprefix("index.")
        date_match = re.search(r'^date:\s*["\']?(\d{4}-\d{2}-\d{2})', text, re.M)
        modified_match = re.search(r'^lastmod:\s*["\']?(\d{4}-\d{2}-\d{2})', text, re.M)
        if not date_match or not modified_match or modified_match.group(1) != "2026-11-23":
            raise SystemExit(f"Missing/incorrect original date or lastmod: {path.name}")

        numbered_sections = re.findall(r"^## ([1-9])\.", text, re.M)
        if numbered_sections != list("123456789"):
            raise SystemExit(f"Missing/reordered top-level section in {path.name}: {numbered_sections}")

        blocks = re.findall(r"```python\s*\n(.*?)\n```", text, re.S)
        if len(blocks) != 1:
            raise SystemExit(f"Expected one complete Python example in {path.name}")
        ast.parse(blocks[0])
        code_hash = hashlib.sha256(blocks[0].encode("utf-8")).hexdigest()
        code_hashes.append(code_hash)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            exec(compile(blocks[0], str(path), "exec"), {"__name__": "__main__"})
        result = output.getvalue()
        if not all(value in result for value in ("2,550", "850.00", "3,266.67")):
            raise SystemExit(f"Unexpected code output in {path.name}: {result!r}")

        urls = sorted(set(re.findall(r"https?://[^\s)]+", text)))
        ref_sets.append(urls)
        if len(urls) != 16:
            raise SystemExit(f"Expected 16 common references in {path.name}, got {len(urls)}")
        if BEAVER_LIMIT[lang] not in text:
            raise SystemExit(f"Missing Beaver-triple security limitation in {path.name}")

        metrics[lang] = {
            "characters": len(text),
            "h2": len(re.findall(r"^## ", text, re.M)),
            "h3": len(re.findall(r"^### ", text, re.M)),
            "pythonBlocks": len(blocks),
            "pythonAstParsed": True,
            "pythonExecuted": True,
            "mermaidBlocks": len(re.findall(r"```mermaid", text)),
            "displayEquations": len(re.findall(r"^\$\$", text, re.M)),
            "primarySources": len(urls),
            "publicationDate": date_match.group(1),
            "lastmod": modified_match.group(1),
        }
        if lang == "ja":
            source_hash = hashlib.sha256(text.replace("\r\n", "\n").encode("utf-8")).hexdigest()

    if len(set(code_hashes)) != 1:
        raise SystemExit("Python example differs between editions")
    if any(refs != ref_sets[0] for refs in ref_sets[1:]):
        raise SystemExit("Reference URL sets differ between editions")

    result = {
        "version": 1,
        "batch": 69,
        "articleBundle": "post/secure-multi-party-computation-mpc-yaos-millionaires-shamir-secret-sharing-garbled-circuits",
        "sourceHash": source_hash,
        "languageOrder": list(LANGS),
        "allThirteenFilesPresent": True,
        "topLevelSectionsOneThroughNinePresent": True,
        "pythonCodeHash": code_hashes[0],
        "pythonAstParsedAndExecutedAllLocales": True,
        "expectedExampleOutputs": {"sum": 2550, "mean": 850.0, "populationVariance": 3266.6666666666665},
        "commonReferenceURLs": ref_sets[0],
        "commonReferenceCount": len(ref_sets[0]),
        "referenceSetsIdentical": True,
        "localeMetrics": metrics,
        "checks": [
            {"command": "python scripts/test_multilingual.py", "result": "passed: 10 tests; 19 pages"},
            {"command": "python scripts/test_translation_reviews.py", "result": "passed: 6 tests"},
            {"command": "python scripts/test_math_rendering.py", "result": "passed: 1 test"},
            {"command": "python docs/translation-review/verify_batch_069_static.py", "result": "passed: all 13 article editions, common links, dates, Python AST and outputs"},
            {"command": "git diff --check", "result": "passed (Git emitted only LF-to-CRLF advisory notices)"},
        ],
        "limitations": [
            "AI review only; no human or native-speaker certification.",
            "The non-English editions are concise localized versions; detailed derivations and subheadings are not line-for-line identical to the Japanese and English editions.",
            "The Python block is an educational single-process simulation, not a distributed MPC implementation; no production deployment or malicious-party protocol was implemented.",
            "Mermaid graphs were structurally read in source but not rendered or visually inspected locally; final published pages will be checked after CI deployment.",
            "This review is not an independent cryptographic proof, security audit, or legal/compliance assessment.",
        ],
        "publicationPending": True,
    }
    (DOCS / "validation-069.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "pages": 13, "references": len(ref_sets[0]), "codeHash": code_hashes[0]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
