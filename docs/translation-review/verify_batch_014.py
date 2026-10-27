"""Reproduce ECC teaching-code, public-value and rendered-math checks.

Requires Python cryptography, a C++17 compiler and Boost headers. Example:
  python docs/translation-review/verify_batch_014.py SITE --output NEW.json
Windows may pass --wsl Ubuntu and a Windows --boost-include directory.
Identical code across all thirteen versions is compiled once in this final
aggregate check; individual language compilation is retained in stage evidence.
This checks finite examples and decoded HTML, not security or browser layout.
"""

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone, timedelta
from pathlib import Path

from cryptography.hazmat.primitives.asymmetric import ec

from verify_batch_013_rendering import ArticleText, expressions

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from translation_reviews import digest

SLUG = "elliptic-curve-cryptography-math-cpp"
FOLDER = ROOT / "content/post/楕円曲線暗号の数学的基礎とcppでの実装"
N = int("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141", 16)
VALUES = [0, 1, 2, 3, 7, 42, 65537, 2**128, 2**255, 2**256-1, N-1, N, N+1]


def native_path(path, wsl):
    resolved = path.resolve()
    if not wsl:
        return str(resolved)
    assert resolved.drive and resolved.drive.endswith(":"), "Use a local drive with WSL."
    return "/mnt/" + resolved.drive[0].lower() + resolved.as_posix()[2:]


def run(command, wsl):
    if wsl:
        command = ["wsl", "-d", wsl, "--exec", *command]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    assert not result.stderr.strip(), result.stderr
    return result.stdout


def compile_run(core, main, name, directory, args):
    source = directory / (name + ".cpp")
    binary = directory / name
    source.write_text(core + main, encoding="utf-8")
    command = [args.compiler, "-std=c++17", "-O2", "-Wall", "-Wextra"]
    if args.boost_include:
        command += ["-I" + native_path(args.boost_include, args.wsl)]
    command += [native_path(source, args.wsl), "-o", native_path(binary, args.wsl)]
    run(command, args.wsl)
    return run([native_path(binary, args.wsl)], args.wsl)


def add_toy(left, right):
    if left is None:
        return right
    if right is None:
        return left
    x, y = left
    u, v = right
    if x == u and (y + v) % 17 == 0:
        return None
    slope = ((v-y) * pow(u-x, -1, 17) if x != u else
             (3*x*x+2) * pow(2*y, -1, 17)) % 17
    a = (slope*slope-x-u) % 17
    return a, (slope*(x-a)-y) % 17


def verify(args):
    paths = sorted(FOLDER.glob("index*.md"))
    assert len(paths) == 13
    baseline = (FOLDER / "index.md").read_text(encoding="utf-8")
    blocks = re.findall(r"^```cpp\n(.*?)^```", baseline, re.M | re.S)
    assert len(blocks) == 5
    files = []
    references = re.findall(r"\]\((https://[^)]+)\)", baseline)
    assert len(references) == 6
    for path in paths:
        lang = "ja" if path.name == "index.md" else path.name[6:-3]
        text = path.read_text(encoding="utf-8")
        assert re.findall(r"^```cpp\n(.*?)^```", text, re.M | re.S) == blocks
        assert re.findall(r"^\$\$(.*?)\$\$$", text, re.M | re.S) == re.findall(r"^\$\$(.*?)\$\$$", baseline, re.M | re.S)
        assert len(re.findall(r"^\$\$(.*?)\$\$$", text, re.M | re.S)) == 11
        assert re.findall(r"\]\((https://[^)]+)\)", text) == references
        graphs = re.findall(r"^```mermaid\n(.*?)^```", text, re.M | re.S)
        assert [g.count("-->")+g.count("-.->")+g.count("->>") for g in graphs] == [3, 6, 6]
        html_path = args.site / ("" if lang == "ja" else lang) / "p" / SLUG / "index.html"
        html = html_path.read_text(encoding="utf-8")
        parser = ArticleText()
        parser.feed(html)
        expected = expressions(re.sub(r"^```.*?^```[^\n]*", "", text, flags=re.M | re.S))
        assert expected == expressions("".join(parser.parts)), lang
        assert len(re.findall(r'<pre class=(?:"mermaid"|mermaid)>', html)) == 3
        for marker in ["conditionalSwapDemo", "Zero has no inverse", "Scalar outside demo range", "nG = infinity", "Pollard", "HKDF", "SEC 2"]:
            assert marker in html, (lang, marker)
        modern_link = ("" if lang == "ja" else "/"+lang) + "/p/modern-cryptography-public-key-hash-signature/"
        assert modern_link in html
        files.append({"language": lang, "path": path.relative_to(ROOT/"content").as_posix(),
                      "hash": digest(path), "cppBlocksIdenticalToSharedCompiledProgram": 5,
                      "displayMath": 11, "mermaidEdges": [3, 6, 6],
                      "renderedTeXExpressions": sum(expected.values()), "passed": True})
    core = "\n".join(blocks[:4])
    fixtures = Path(__file__).parent
    with tempfile.TemporaryDirectory(prefix="kenji-ecc-verify-") as temporary:
        directory = Path(temporary)
        main = compile_run("\n".join(blocks), "", "demo", directory, args)
        assert "nG = infinity" in main
        output = compile_run(core, (fixtures/"batch-014-scalar-fixture.cpp").read_text(encoding="utf-8"), "scalar", directory, args)
        lines = output.splitlines()
        assert lines[-1] == "rejections=13" and len(lines) == 14
        for index, line in enumerate(lines[:-1]):
            number, infinity, x, y = line.split(":")
            assert int(number) == index
            value = VALUES[index] % N
            if not value:
                assert infinity == "1"
            else:
                point = ec.derive_private_key(value, ec.SECP256K1()).public_key().public_numbers()
                assert infinity == "0" and (int(x, 16), int(y, 16)) == (point.x, point.y)
        toy_core = re.sub(r"const cpp_int p\([^\n]+", "const cpp_int p(17);", core)
        toy_core = toy_core.replace("const cpp_int a = 0;", "const cpp_int a = 2;").replace("const cpp_int b = 7;", "const cpp_int b = 0;")
        assert "const cpp_int p(17);" in toy_core and "const cpp_int a = 2;" in toy_core and "const cpp_int b = 0;" in toy_core
        toy = compile_run(toy_core, (fixtures/"batch-014-toy-fixture.cpp").read_text(encoding="utf-8"), "toy", directory, args)
        points = [None] + [(x, y) for x in range(17) for y in range(17) if (y*y-x*x*x-2*x) % 17 == 0]
        assert len(points) == 20
        toy_lines = toy.splitlines()
        assert len(toy_lines) == 401 and toy_lines[-1] == "counts=20,400,8000,820,3"
        seen = set()
        for line in toy_lines[:-1]:
            i, j, infinity, x, y = map(int, line.removeprefix("pair=").split(","))
            assert (i, j) not in seen
            seen.add((i, j))
            assert add_toy(points[i], points[j]) == (None if infinity else (x, y))
        assert len(seen) == 400
    return {"version": 1, "checkedAt": datetime.now(timezone(timedelta(hours=9))).isoformat(),
            "scope": "All thirteen ECC versions; shared exact C++ recompiled once with scalar and toy fixtures.",
            "files": files, "sharedCodeSHA256": hashlib.sha256(core.encode()).hexdigest(),
            "mainStdout": main, "scalarDifferentialCases": 13, "invalidCasesRejected": 13,
            "toyCurve": {"points": 20, "independentAdditionPairs": 400, "associativityTriples": 8000,
                         "ladderRepeatedAdditionCases": 820, "zeroYDoublingCases": 3},
            "compiler": args.compiler, "wsl": args.wsl, "site": str(args.site), "allPassed": True,
            "limitations": "AI review recorded separately. Finite functional checks only; no constant-time/security proof, native-speaker certification or visual browser audit."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--compiler", default="g++")
    parser.add_argument("--boost-include", type=Path)
    parser.add_argument("--wsl")
    args = parser.parse_args()
    if args.output.exists():
        parser.error("Preserve prior evidence; choose a new output path.")
    result = verify(args)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"files": len(result["files"]), "TeXExpressions": sum(f["renderedTeXExpressions"] for f in result["files"]), "allPassed": result["allPassed"]}))
