"""Check reviewed RSA/ECC overview equations and their generated HTML.

Usage: python docs/translation-review/verify_batch_016.py SITE --languages ja en --output NEW.json
Independent small mathematical fixtures supplement the prose review. The article
has no executable code; this is not an implementation or security certification.
"""

import argparse
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

SLUG = "public-key-cryptography-rsa-ecc"
FOLDER = ROOT / "content/post" / SLUG


def arithmetic():
    # Public tiny fixtures; never suitable for protecting real data.
    p, q, g = 23, 11, 2
    subgroup = {pow(g, a, p) for a in range(q)}
    assert len(subgroup) == q and pow(g, q, p) == 1
    accepted = {y for y in range(p) if 1 < y < p and pow(y, q, p) == 1}
    assert accepted == subgroup - {1}
    assert {y for y in range(1, p) if pow(y, q, p) == 1} == subgroup
    for a in range(1, q):
        for b in range(1, q):
            assert pow(pow(g, b, p), a, p) == pow(pow(g, a, p), b, p)
    a, b, x, y = 6, 7, 3, 4
    alice = pow(pow(g, x, p), a, p)
    bob = pow(pow(g, y, p), b, p)
    assert alice == pow(pow(g, a, p), x, p) == 13
    assert bob == pow(pow(g, b, p), y, p) == 18
    assert all(pow(1, a, p) == 1 for a in range(1, q))
    N, phi, e = 143, 120, 7
    d = pow(e, -1, phi)
    for m in range(N):
        assert pow(pow(m, e, N), d, N) == m
        for prime in (11, 13):
            assert (e*d-1) % (prime-1) == 0
            assert pow(m, e*d, prime) == m % prime
        if math.gcd(m, N) == 1:
            assert pow(m, phi, N) == 1
    assert math.gcd(1, phi) == 1
    assert all(pow(m, 1, N) == m for m in range(N))
    assert math.lcm(10, 12) == 60 and (e*d-1) % 60 == 0
    points = [None]+[(x,y) for x in range(17) for y in range(17) if (y*y-x*x*x-2*x) % 17 == 0]

    def add(P, Q):
        if P is None:
            return Q
        if Q is None:
            return P
        x1, y1 = P
        x2, y2 = Q
        if x1 == x2 and (y1+y2) % 17 == 0:
            return None
        slope = ((3*x1*x1+2)*pow(2*y1, -1, 17) if P == Q
                 else (y2-y1)*pow(x2-x1, -1, 17)) % 17
        x3 = (slope*slope-x1-x2) % 17
        return x3, (slope*(x1-x3)-y1) % 17

    assert len(points) == 20
    zero = [P for P in points if P is not None and P[1] == 0]
    assert len(zero) == 3 and all(add(P, P) is None for P in zero)
    for P in points:
        assert add(P, None) == P == add(None, P)
        neg = None if P is None else (P[0], -P[1] % 17)
        assert add(P, neg) is None
        for Q in points:
            assert add(P, Q) in points and add(P, Q) == add(Q, P)
            for R in points:
                assert add(add(P, Q), R) == add(P, add(Q, R))
    assert 27*5**2 == 675 and (27*5**2) % 5 == 0
    return {"scope":"Independent mathematical fixtures, not executable article blocks or a security proof.",
            "dhMatchingPairs":100, "dhSubgroupNonidentityMembers":10,
            "dhIdentityForcesOne":True, "mitmSharedValues":[alice,bob],
            "rsaRepresentatives":143, "rsaNonCoprimeRepresentatives":23,
            "rsaPrimewiseCases":286, "e1RejectedByRevisedCondition":True,
            "curvePointsIncludingInfinity":20,"pointPairs":400,"associativityTriples":8000,
            "y0DoublingsToInfinity":3,"singularIntegerVsFieldCounterexample":True}


def verify(site, languages):
    assert len(languages) == len(set(languages))
    baseline = (FOLDER/"index.md").read_text(encoding="utf-8")
    display = re.findall(r"^\$\$(.*?)^\$\$", baseline, re.M|re.S)
    links = re.findall(r"\]\((https://[^)]+)\)", baseline)
    assert len(display) == 9 and len(links) == 6
    files=[]
    for language in languages:
        path=FOLDER/("index.md" if language=="ja" else f"index.{language}.md")
        text=path.read_text(encoding="utf-8")
        graphs=re.findall(r"^```mermaid\n(.*?)^```",text,re.M|re.S)
        assert re.findall(r"^```([^\n]*)\n",text,re.M)==["mermaid","","mermaid",""]
        assert [graph.count("->>")+graph.count("-->") for graph in graphs]==[8,2]
        assert re.findall(r"^\$\$(.*?)^\$\$",text,re.M|re.S)==display
        assert re.findall(r"\]\((https://[^)]+)\)",text)==links
        assert len(re.findall(r"^## [1-6]\. ",text,re.M))==6
        assert "date: 2026-09-27T23:50:00+09:00" in text and "lastmod: 2026-10-28" in text
        assert "image: eyecatch.jpg" in text and (FOLDER/"eyecatch.jpg").is_file()
        assert f"slug: {SLUG}" in text
        assert not re.search(r"[\u0980-\u09ff]",text), "Unexpected Bengali corruption"
        source=re.sub(r"^```.*?^```[^\n]*","",text,flags=re.M|re.S)
        html_path=site/("" if language=="ja" else language)/"p"/SLUG/"index.html"
        parser=ArticleText(); html=html_path.read_text(encoding="utf-8");parser.feed(html)
        rendered="".join(parser.parts)
        expected,actual=expressions(source),expressions(rendered)
        checks={"allTeXPreserved":expected==actual,"rsaRangePreserved":r"1<e<\phi(N)" in actual,
                "linksPreserved":all(link in html for link in links),
                "mermaidEnabled":"mermaid" in html,"mathEnabled":"katex" in html,
                "markersPreserved":all(marker in rendered for marker in ("CDH","HKDF","RSAES-OAEP","RSASSA-PSS","Pollard","112","128","256"))}
        files.append({"language":language,"path":path.relative_to(ROOT/"content").as_posix(),"hash":digest(path),
                      "displayFormulas":len(display),"texExpressions":sum(expected.values()),"diagrams":2,"diagramEdges":[8,2],
                      "executableArticleBlocks":0,"missingMath":list((expected-actual).elements()),
                      "unexpectedMath":list((actual-expected).elements()),"checks":checks,"passed":all(checks.values())})
    return {"version":1,"checkedAt":datetime.now(timezone(timedelta(hours=9))).isoformat(),"site":str(site),
            "scope":"Explicitly selected reviewed languages only. Automated checks do not record prose reviews.",
            "limitations":["No executable article code; independent arithmetic only.","Not a visual browser/KaTeX/Mermaid or native-speaker audit.","Finite examples do not prove cryptographic security."],
            "arithmetic":arithmetic(),"files":files,"allPassed":all(f["passed"] for f in files)}


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site",type=Path)
    parser.add_argument("--languages",nargs="+",required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():
        parser.error("Preserve existing evidence; use a new output path.")
    result=verify(args.site,args.languages)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"pages":len(result["files"]),"expressions":sum(f["texExpressions"] for f in result["files"]),
                      "passed":result["allPassed"],"failures":[f for f in result["files"] if not f["passed"]]}))
    sys.exit(0 if result["allPassed"] else 1)
