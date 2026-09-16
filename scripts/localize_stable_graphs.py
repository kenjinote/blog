"""Generate standalone localized stable-matching scripts, figures and results.

Usage: python scripts/localize_stable_graphs.py [language ...]
Requires matplotlib and fonts for the selected languages.
"""
import ast
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
ARTICLE = ROOT / 'content/post/stable-marriage-problem'
LABELS = json.loads((Path(__file__).parent / 'stable-matching-labels.json').read_text(encoding='utf-8'))

def localized_script(lang, words):
    src = (ARTICLE / 'generate_graphs.py').read_text(encoding='utf-8')
    src = re.sub(r'""".*?"""\n', '', src, flags=re.S)
    replacements = {
        '安定': words['stable'],
        '全6人の希望順位の合計（小さいほど上位）': words['rank_axis'],
        '順位の合計が最小でも、安定とは限らない': words['rank_title'],
        'AとXは、互いに今の相手より好ましい': words['block_note'],
        'L側': words['side'][0], 'R側': words['side'][1],
        '実線：現在の組　　破線：ブロッキングペア': words['block_legend'],
        'この組み合わせが不安定な理由': words['block_title'],
        'L側の平均順位': words['means'][0], 'R側の平均順位': words['means'][1],
        'L側が申し込む\nA–X、B–Y': words['proposes'][0]+'\nA–X, B–Y',
        'R側が申し込む\nA–Y、B–X': words['proposes'][1]+'\nA–Y, B–X',
        '平均希望順位（小さいほど上位）': words['proposer_axis'],
        '2人ずつの別例：どちらの結果も安定': words['proposer_title'],
    }
    for old, new in replacements.items():
        old_literal = json.dumps(old, ensure_ascii=False)
        assert old_literal in src, old
        src = src.replace(old_literal, json.dumps(new, ensure_ascii=False))
    src = src.replace('f"不安定：{len(row[\'blocking_pairs\'])}組"', repr(words['unstable'])+'.format(n=len(row["blocking_pairs"]))')
    src = src.replace('"、".join', '", ".join')
    src = src.replace('["Meiryo", "DejaVu Sans"]', repr([words['font'], 'DejaVu Sans']))
    src = src.replace('"font.size": 13', '"font.size": 12, "axes.titlesize": 13')
    src = src.replace('figsize=(9, 6)', 'figsize=(12, 6)').replace('figsize=(9, 5)', 'figsize=(12, 5)').replace('figsize=(10, 6)', 'figsize=(12, 6)')
    src = src.replace('ha="center", color="#c2410c"', 'ha="center", color="#c2410c", fontsize=11')
    for name in ['blocking-pair', 'rank-comparison', 'proposer-comparison']:
        src = src.replace(name+'.svg', name+'.'+lang+'.svg')
    src = src.replace('calculation-results.json', 'calculation-results.'+lang+'.json')
    helper = '''
def finish_svg(path):
    import xml.etree.ElementTree as ET
    ns = "http://www.w3.org/2000/svg"
    ET.register_namespace("", ns)
    ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")
    tree = ET.parse(path)
    tree.getroot().set("{http://www.w3.org/XML/1998/namespace}lang", LANGUAGE)
    for element in tree.getroot().iter("{"+ns+"}text"):
        text = "".join(element.itertext())
        if LANGUAGE == "ar" and any("\\u0600" <= c <= "\\u06ff" for c in text):
            style = element.get("style", "")
            if "text-anchor: start" in style:
                style = style.replace("text-anchor: start", "text-anchor: end")
            elif "text-anchor: end" in style:
                style = style.replace("text-anchor: end", "text-anchor: start")
            elif "text-anchor:" not in style:
                style += "; text-anchor: end"
            element.set("style", style+"; direction: rtl; unicode-bidi: plaintext")
    tree.write(path, encoding="utf-8", xml_declaration=True)

'''
    src = src.replace('def save(fig, name):', 'LANGUAGE = '+repr(lang)+'\n'+helper+'def save(fig, name):')
    src = src.replace('    plt.close(fig)', '    finish_svg(path)\n    plt.close(fig)')
    assert not re.search(r'[\u3040-\u30ff]', src)
    ast.parse(src)
    return src

for lang in sys.argv[1:] or LABELS:
    target = ARTICLE / f'generate_graphs.{lang}.py'
    target.write_text(localized_script(lang, LABELS[lang]), encoding='utf-8')
    run = subprocess.run([sys.executable, '-B', '-X', 'utf8', str(target)], capture_output=True, encoding='utf-8')
    if run.returncode:
        raise RuntimeError(run.stderr)
    print(lang, 'OK', run.stderr[:250])
