"""Join preserved finite code executions to fresh all-language HTML; no prose approval."""
from pathlib import Path
import argparse, json, re, importlib.util
from datetime import datetime, timezone, timedelta

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('fermat_checks', Path(__file__).with_name('verify_batch_022.py'))
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('site', type=Path)
    ap.add_argument('--output', type=Path, required=True)
    a = ap.parse_args()
    assert not a.output.exists(), 'Preserve earlier evidence'
    audit = json.loads((ROOT/'docs/translation-review/batch-022-source-audit.json').read_text(encoding='utf-8'))
    reviews = json.loads((ROOT/'docs/translation-review/batch-022.json').read_text(encoding='utf-8'))['reviews']
    proofs = {}
    for suffix in ['ja-en', 'cn', 'tw', 'es', 'ko', 'pt', 'fr', 'de', 'id', 'hi', 'ru', 'ar']:
        p = ROOT/f'docs/translation-review/batch-022-{suffix}-validation.json'
        for v in json.loads(p.read_text(encoding='utf-8'))['versions']:
            assert v['language'] not in proofs
            proofs[v['language']] = (p, v)
    assert set(proofs) == set(audit['versions']) and len(proofs) == 13 and len(reviews) == 12
    urls = {l: 'https://kenji.blog/'+('' if l == 'ja' else l+'/')+'p/'+check.SLUG+'/' for l in proofs}
    fence = chr(96)*3
    ja = (check.FOLDER/'index.md').read_text(encoding='utf-8')
    codes_ja = re.findall(r'^'+fence+r'(cpp|python)\n(.*?)^'+fence, ja, re.M|re.S)
    graphs_ja = re.findall(r'^'+fence+r'mermaid\n(.*?)^'+fence, ja, re.M|re.S)
    strip_code = lambda s: re.sub(r'^'+fence+r'.*?^'+fence+r'[^\n]*', '', s, flags=re.M|re.S)
    math_ja = check.cpp.rendering.expressions(strip_code(ja))
    assert sum(math_ja.values()) == 82
    external = {'https://dlmf.nist.gov/27.2#E8', 'https://cacr.uwaterloo.ca/hac/about/chap4.pdf', 'https://docs.openssl.org/master/man3/BN_generate_prime/', 'https://www.rfc-editor.org/rfc/rfc8017.html', 'https://docs.python.org/3/library/random.html', 'https://gcc.gnu.org/onlinedocs/gcc/_005f_005fint128.html'}
    results = []
    for lang, (p, v) in proofs.items():
        source = ROOT/audit['versions'][lang]['path']
        text = source.read_text(encoding='utf-8-sig')
        sha = check.digest(source)
        assert sha == v['sha256'] and v['passed']
        if lang != 'ja':
            e = reviews[source.relative_to(ROOT/'content').as_posix()]
            assert e['translationHash'] == sha and e['sourceHash'] == check.digest(check.FOLDER/'index.md')
        url = urls[lang]
        html = (a.site/url.removeprefix('https://kenji.blog/')/'index.html').read_text(encoding='utf-8')
        parser = check.PageParser()
        parser.feed(html.split('</aside>', 1)[0]+'</aside>')
        assert parser.canonical == url and parser.language == lang
        assert parser.alternates == dict(urls, **{'x-default': urls['ja']}) and parser.options == urls
        codes = re.findall(r'^'+fence+r'(cpp|python)\n(.*?)^'+fence, text, re.M|re.S)
        assert codes == codes_ja and len(codes) == 3
        rendered = check.CodeParser()
        rendered.feed(html)
        assert [(l, c.strip()) for l, c in rendered.blocks] == [(l, c.strip()) for l, c in codes]
        graphs = re.findall(r'^'+fence+r'mermaid\n(.*?)^'+fence, text, re.M|re.S)
        assert len(graphs) == 2 and check.graph_edges(graphs[0]) == check.graph_edges(graphs_ja[0]) and check.sequence_edges(graphs[1]) == check.sequence_edges(graphs_ja[1])
        # Hugo retains Mermaid diagram source inside pre blocks, HTML-escaped.
        from html import unescape
        decoded = unescape(html)
        assert all(g.strip() in decoded for g in graphs)
        assert check.cpp.rendering.expressions(strip_code(text)) == math_ja
        article = check.cpp.rendering.ArticleText()
        article.feed(html)
        assert check.cpp.rendering.expressions(''.join(article.parts)) == math_ja
        internal = {'https://kenji.blog/'+('' if lang == 'ja' else lang+'/')+'p/'+s+'/' for s in ['rsa-encryption-math-explained-for-beginners', 'cpp-fast-prime-testing-miller-rabin']}
        refs = set(re.findall(r'\]\((https://[^)]+)\)', text))
        assert refs == external | internal and all(u in html for u in refs)
        assert all((a.site/u.removeprefix('https://kenji.blog/')/'index.html').is_file() for u in internal)
        assert len(re.findall(r'^## [1-9]\. ', text, re.M)) == 9
        assert 'date: "2026-09-11T22:00:00+09:00"' in text and 'lastmod: 2026-10-29' in text
        assert 'slug: "'+check.SLUG+'"' in text and 'image: "img/eyecatch.jpg"' in text
        assert '"datePublished":"2026-09-11T22:00:00+09:00"' in html and '"dateModified":"2026-10-29' in html
        assert 'katex' in html and 'mermaid' in html
        assert len(v['cppBuilds']) == 2 and {b['mode'] for b in v['cppBuilds']} == {'optimized', 'ubsan'}
        for b in v['cppBuilds']:
            assert b['cases'] == 7480 and b['kindCounts'] == {'M':2696,'P':2696,'F':2080,'invalid':8}
            assert b['completeProgramOutputExact'] and b['allArithmeticAndFermatCasesExact']
        assert v['pythonCompleteProgramsExact'] == 2 and v['pythonFermatCases'] == 2078 and v['pythonExtendedGcdAndInverseCases'] == 9999 and v['rsaRepresentativesRoundTrip'] == 3233
        assert (v['pythonInvalidFermatCases'], v['pythonInvalidInverseCases'], v['pythonInvalidRsaCases']) == (11,5,9)
        results.append({'language':lang, 'sha256':sha, 'canonical':url, 'executionEvidence':p.relative_to(ROOT).as_posix(), 'cppBuilds':v['cppBuilds'], 'pythonCompleteProgramsExact':2, 'rsaRepresentativesRoundTrip':3233, 'codeBlocksExact':3, 'texExpressionsExact':82, 'diagramEdgesExact':[13,6], 'all14HreflangAnd13SidebarUrlsExact':True, 'referencesAndMetadataExact':True})
    output = {'version':1, 'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(), 'scope':'Fresh all13version HTML/metadata/exactcode/TeX/diagram/reference/language-map checks joined to preserved actual per-language executions. No duplicate new executable runs or automatic prose approval.', 'versions':results, 'codeBlocksExact':39, 'texExpressionsExact':1066, 'diagramsExact':26, 'diagramEdgesExact':247, 'preservedCppCasesAllModes':194480, 'preservedCppCompleteProgramRuns':26, 'preservedPythonCompleteProgramRuns':26, 'publicationPending':True, 'limitations':['AI review,not human/native-language certification.', 'Finite C++/Python cases,not exhaustive uint64 proof,production cryptographic audit or performance/constant-time assessment.', 'HTML/source checked;no visualbrowser,RTL,KaTeX or Mermaid runtime-rendering certification.']}
    a.output.write_text(json.dumps(output, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k:output[k] for k in ['codeBlocksExact','texExpressionsExact','diagramsExact','preservedCppCasesAllModes']}))


if __name__ == '__main__':
    main()
