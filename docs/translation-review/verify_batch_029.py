"""Selected source/decoded HTML and exact arithmetic, not prose approval."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone, timedelta
from html import unescape
import argparse, hashlib, importlib.util, json, re, subprocess

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "docs/translation-review"
spec = importlib.util.spec_from_file_location("monty_checks", D / "verify_batch_028.py")
shared = importlib.util.module_from_spec(spec)
spec.loader.exec_module(shared)


def auxiliary():
    result = shared.auxiliary()
    diagnostic_cases = 0
    for p in [F(0), F(1, 10000), F(1, 100), F(1, 2), F(99, 100), F(1)]:
        for s in [F(0), F(1, 100), F(1, 2), F(99, 100), F(1)]:
            for t in [F(0), F(1, 100), F(1, 2), F(99, 100), F(1)]:
                cells = {(True, True): p*s, (True, False): p*(1-s),
                         (False, True): (1-p)*(1-t), (False, False): (1-p)*t}
                assert sum(cells.values()) == 1
                positive = sum(w for (_, test), w in cells.items() if test)
                if positive:
                    assert cells[(True, True)]/positive == s*p/(s*p+(1-t)*(1-p))
                    diagnostic_cases += 1
    p, s, t = F(1, 10000), F(99, 100), F(99, 100)
    assert s*p/(s*p+(1-t)*(1-p)) == F(1, 102)
    assert 10000*s*p == F(99, 100)
    assert 10000*(1-t)*(1-p) == F(9999, 100)
    utility_cases = 0
    for car in [-10, 0, 1, 10, 100]:
        for goat in [-10, 0, 1, 10, 100]:
            for cost in [F(0), F(1, 3), F(1), F(10), F(100)]:
                # Average the actual three equiprobable car placements.
                stay = (car + goat + goat)/F(3)
                switch = (goat + car + car)/F(3) - cost
                assert switch-stay == (car-goat)/F(3)-cost
                utility_cases += 1
    result.update(diagnosticJointTableCases=diagnostic_cases,
                  diagnosticExamplePosterior="1/102",
                  utilityPlacementCases=utility_cases,
                  additionalScope="Exact hypothetical arithmetic/utility units only;not clinical accuracy,individual risk,psychological experiment or business-success evidence.")
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("site", type=Path)
    ap.add_argument("--languages", nargs="+", required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--expected-modified", action="append", default=[])
    args = ap.parse_args()
    assert not args.output.exists()
    audit_path = D / "batch-029-source-audit.json"
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    source = ROOT / audit["versions"]["ja"]["path"]
    source_text = source.read_text(encoding="utf-8")
    tex = shared.render.expressions(shared.strip(source_text))
    assert sum(tex.values()) == 15
    urls = {l: v["canonical"] for l, v in audit["versions"].items()}
    dates = dict.fromkeys(urls, "2026-11-11")
    for value in args.expected_modified:
        lang, day = value.split("=", 1)
        assert lang in args.languages
        datetime.strptime(day, "%Y-%m-%d")
        assert "2026-11-11" <= day <= datetime.now(timezone(timedelta(hours=9))).date().isoformat()
        dates[lang] = day
    external = {"https://pub.math.leidenuniv.nl/~gillrd/montyhall3.pdf",
                "https://probability.ca/jeff/writing/montyfall.pdf",
                "https://pmc.ncbi.nlm.nih.gov/articles/PMC3435463/"}
    versions = []
    for lang in args.languages:
        v = audit["versions"][lang]
        p = ROOT / v["path"]
        text = p.read_text(encoding="utf-8")
        original = subprocess.run(["git", "show", audit["baselineCommit"]+":"+v["path"]],
                                  cwd=ROOT, capture_output=True, text=True, encoding="utf-8", check=True).stdout
        assert hashlib.sha256(original.replace("\r\n", "\n").encode()).hexdigest() == v["sha256"]
        assert shared.taxonomy(text) == shared.taxonomy(original)
        header = text.split("---", 2)[1]
        assert re.findall(r"^date:.*$", header, re.M) == v["headerDateLines"]
        assert re.findall(r"^lastmod:.*$", header, re.M) == ['lastmod: "'+dates[lang]+'"']
        for key in ("slug", "image"):
            assert re.findall(r"^"+key+r":.*$", header, re.M) == re.findall(r"^"+key+r":.*$", original.split("---", 2)[1], re.M)
        assert re.findall(r"^(?:math|mermaid): true$", header, re.M) == ["math: true", "mermaid: true"]
        assert re.findall(r"^## (\d+)\.", text, re.M) == list(map(str, range(1, 7)))
        assert re.findall(r"^"+shared.FENCE+r"(\w+)\n", text, re.M) == ["mermaid", "mermaid"]
        graphs = shared.graphs(text)
        assert len(graphs) == 2
        assert [g.count("-->") for g in graphs] == [13, 5]
        assert [re.sub(r'"[^"\n]*"', '""', g) for g in graphs] == [
            re.sub(r'"[^"\n]*"', '""', g) for g in shared.graphs(source_text)]
        assert shared.render.expressions(shared.strip(text)) == tex
        html = (args.site / urls[lang].removeprefix("https://kenji.blog/") / "index.html").read_text(encoding="utf-8")
        parser = shared.PageParser()
        parser.feed(html.split("</aside>", 1)[0]+"</aside>")
        assert parser.canonical == urls[lang] and parser.language == lang
        assert parser.alternates == dict(urls, **{"x-default": urls["ja"]})
        assert parser.options == urls
        article = shared.render.ArticleText()
        article.feed(html)
        assert shared.render.expressions("".join(article.parts)) == tex
        assert all(g.strip() in unescape(html) for g in graphs)
        prefix = "" if lang == "ja" else lang+"/"
        internal = {"https://kenji.blog/"+prefix+"p/"+slug+"/" for slug in ("monty-hall-problem", "bayes-theorem")}
        refs = set(re.findall(r"\]\((https://[^)]+)\)", text))
        assert refs == external | internal and all(u in html for u in refs)
        assert all((args.site / u.removeprefix("https://kenji.blog/") / "index.html").is_file() for u in internal)
        assert '"datePublished":"'+v["datePublished"]+'"' in html
        assert '"dateModified":"'+dates[lang] in html
        assert "katex.min.js" in html and "mermaid" in html
        title = json.loads(re.search(r"^title: (.*)$", header, re.M)[1])
        assert title in unescape(html)
        for asset in audit["assets"]:
            assert hashlib.sha256((ROOT / asset["path"]).read_bytes()).hexdigest() == asset["sha256"]
        versions.append({"language": lang, "path": v["path"], "sha256": shared.digest(p),
                         "sourceSha256": shared.digest(source), "texExpressions": 15,
                         "diagrams": 2, "diagramEdges": [13, 5], "articleExecutablePrograms": 0,
                         "references": 5, "datePublished": v["datePublished"],
                         "dateModified": dates[lang], "passed": True})
    result = {"version": 1, "checkedAt": datetime.now(timezone(timedelta(hours=9))).isoformat(),
              "allPassed": True, "versions": versions, "sharedAuxiliaryChecks": auxiliary(),
              "sourceAuditSha256": hashlib.sha256(audit_path.read_bytes()).hexdigest(),
              "reviewedTranslationsAdded": 0,
              "limitations": ["Selected source/decodedHTML/finite arithmetic only;not full prose approval or ledger record.",
                              "Article programs0;auxiliary checks separate. No native/browser/clinical/psychological/general-policy certification.",
                              "Source flags now explicit;baseline already included runtime libraries.",
                              "Other languages/publication pending;full article goal active."]}
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"passed": True, "versions": len(versions), "texEach": 15,
                      "diagramEdges": [13, 5], "auxiliary": result["sharedAuxiliaryChecks"]}))


if __name__ == "__main__":
    main()
