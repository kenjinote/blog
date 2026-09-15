"""Build standalone localized plotting scripts and their SVG figures.

Run from any directory: python scripts/localize_coupon_graphs.py [language ...]
Requires matplotlib and fonts supporting the selected languages.
SVG keeps text as Unicode so browsers shape Arabic and Indic scripts correctly.
"""

import ast
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
ARTICLE = ROOT / 'content/post/coupon-collector-problem'
LABELS = json.loads((Path(__file__).parent / 'coupon-graph-labels.json').read_text(encoding='utf-8'))
TEMPLATE = (ARTICLE / 'generate_graphs.py').read_text(encoding='utf-8')


def localized_script(lang, words):
    # Translate text literals without changing the numerical model.
    src = TEMPLATE
    literals = {
        '最後の1種類を待つだけで、平均10回': words['stage_title'],
        'すでに持っている種類数（全10種類）': words['stage_x'],
        '次の新しい種類までの平均回数': words['stage_y'],
        '30回引いても、そろう確率は約63％': words['completion_title'],
        '抽選回数 m（全10種類）': words['completion_x'],
        'm 回以内に全種類がそろう確率': words['completion_y'],
        '早くそろうことも、長く待つこともある': words['simulation_title'],
        '全種類がそろうまでの回数（5回幅・最後は100回以上）': words['simulation_x'],
        '各区間に入る割合': words['simulation_y'],
        '乱数実験（1万回）': words['empirical'],
        '同じ区間の理論確率': words['theory'],
        '100以上': words['overflow'],
        'Install a Japanese font such as Noto Sans CJK JP first.': words['font_error'],
        'independent uniform draws with replacement': words['model'],
    }
    for old, new in literals.items():
        assert f'"{old}"' in src, old
        src = src.replace(f'"{old}"', json.dumps(new, ensure_ascii=False))
    src = re.sub(r'    candidates = .*', '    candidates = '+repr([words['font']]), src)
    src = src.replace('from matplotlib.ticker import PercentFormatter', 'from matplotlib.ticker import FuncFormatter')
    src = src.replace('f"{m}回：{cdf[m]:.1%}"', repr(words['point'])+'.format(m=m, p=number(cdf[m] * 100, 1) + "%")')
    src = src.replace('f"平均回数 {mean:.2f}回"', repr(words['mean'])+'.format(v=number(mean, 2))')
    src = src.replace('f"{w:.2f}".rstrip("0").rstrip(".")', 'number(w, 2).rstrip("0").rstrip(".,")')
    src = src.replace('PercentFormatter(1)', 'FuncFormatter(lambda value, _: number(value * 100, 0) + "%")')
    src = src.replace('"axes.titlesize": 20', '"axes.titlesize": 17,\n        "svg.fonttype": "none",\n        "figure.constrained_layout.h_pad": 0.2,\n        "figure.constrained_layout.w_pad": 0.2')
    for name in ['stage-waiting', 'completion-probability', 'simulation-distribution']:
        src = src.replace(f'"{name}.png"', f'"{name}.{lang}.svg"')
    src = src.replace('(OUT / "calculation-results.json").write_text', f'(OUT / "calculation-results.{lang}.json").write_text')
    # Remove template prose from the downloadable scripts; all displayed text is localized.
    src = re.sub(r'""".*?"""', '', src, flags=re.S)
    src = re.sub(r'^\s*#.*\n', '\n', src, flags=re.M)
    helper = '\n\ndef number(value, digits):\n    value = f"{value:.{digits}f}"\n'
    helper += '    return value.replace(".", ",")\n' if lang in ['es','fr','de','pt','id','ru'] else '    return value\n'
    # SVG text is shaped by the viewer. Flip logical anchors for RTL labels so
    # their occupied area stays aligned with Matplotlib's original placement.
    helper += '''

def finish_svg(path):
    import xml.etree.ElementTree as ET
    svg_ns = "http://www.w3.org/2000/svg"
    ET.register_namespace("", svg_ns)
    ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")
    tree = ET.parse(path)
    root = tree.getroot()
    root.set("{http://www.w3.org/XML/1998/namespace}lang", LANGUAGE)
    for element in root.iter("{" + svg_ns + "}text"):
        text = "".join(element.itertext())
        style = element.get("style", "")
        if LANGUAGE == "ar" and any("\\u0600" <= c <= "\\u06ff" for c in text):
            if "text-anchor: start" in style:
                style = style.replace("text-anchor: start", "text-anchor: end")
            elif "text-anchor: end" in style:
                style = style.replace("text-anchor: end", "text-anchor: start")
            elif "text-anchor:" not in style:
                style += "; text-anchor: end"
            style += "; direction: rtl; unicode-bidi: plaintext"
        element.set("style", style)
    tree.write(path, encoding="utf-8", xml_declaration=True)
'''
    src = src.replace('\n\ndef main():', helper+'\n\ndef main():')
    src = src.replace('SEED = 20260915', 'SEED = 20260915\nLANGUAGE = '+repr(lang))
    src = re.sub(r'(    fig.savefig\(OUT / ("[^"]+\.svg"), dpi=160\))', r'\1\n    finish_svg(OUT / \2)', src)
    assert not re.search(r'[\u3040-\u30ff]', src)
    ast.parse(src)
    return '\n'.join(line.rstrip() for line in src.lstrip().splitlines()) + '\n'


def main():
    for lang in sys.argv[1:] or LABELS:
        path = ARTICLE / f'generate_graphs.{lang}.py'
        path.write_text(localized_script(lang, LABELS[lang]), encoding='utf-8')
        result = subprocess.run([sys.executable, '-B', '-X', 'utf8', str(path)], capture_output=True, text=True, encoding='utf-8')
        if result.returncode:
            raise RuntimeError(result.stderr)
        if result.stderr:
            print(lang, result.stderr.strip())
        print(lang, '3 SVG figures generated')


if __name__ == '__main__':
    main()
