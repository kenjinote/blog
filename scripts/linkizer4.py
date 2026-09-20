import os
import re

blog_dir = r'c:\work\kenji.blog\content\post'

link_dict = {
    "フェルマーの最終定理": "fermats-last-theorem",
    "Fermat's Last Theorem": "fermats-last-theorem",
    "ABC予想": "abc-conjecture",
    "ABC conjecture": "abc-conjecture",
    "ガロア理論": "galois-theory",
    "Galois theory": "galois-theory",
    "ポアンカレ予想": "poincare-conjecture",
    "Poincaré conjecture": "poincare-conjecture",
    "リーマン予想": "riemann-hypothesis",
    "Riemann hypothesis": "riemann-hypothesis",
    "ゲーデルの不完全性定理": "godels-incompleteness-theorems",
    "不完全性定理": "godels-incompleteness-theorems",
    "Gödel's incompleteness theorems": "godels-incompleteness-theorems",
    "四色定理": "four-color-theorem",
    "Four color theorem": "four-color-theorem",
    "エミー・ネーター": "noether",
    "シュリニヴァーサ・ラマヌジャン": "ramanujan",
    "ラマヌジャン": "ramanujan",
    "モーデル": "mordell",
    "ジーゲル": "siegel",
    "ハッセ": "hasse",
    "岡潔": "oka-kiyoshi",
    "ジョン・フォン・ノイマン": "von-neumann",
    "フォン・ノイマン": "von-neumann",
    "ヴェイユ": "weil",
    "クルト・ゲーデル": "godel",
    "ゲーデル": "godel",
    "アラン・チューリング": "turing",
    "チューリング": "turing",
    "小平邦彦": "kodaira-kunihiko",
    "伊藤清": "ito-kiyosi",
    "谷山豊": "taniyama-yutaka",
    "アレクサンドル・グロタンディーク": "grothendieck",
    "グロタンディーク": "grothendieck",
    "志村五郎": "shimura-goro",
    "広中平祐": "hironaka-heisuke",
    "アラン・ベーカー": "baker",
    "ベーカー": "baker",
    "アンドリュー・ワイルズ": "wiles",
    "ワイルズ": "wiles",
    "ゲルト・ファルティングス": "faltings",
    "ファルティングス": "faltings",
    "オイラー": "euler",
    "ガウス": "gauss",
    "ニュートン": "newton",
    "ライプニッツ": "leibniz",
    "ピタゴラス": "pythagoras",
    "選択公理": "axiom-of-choice-and-zorns-lemma",
    "ツォルンの補題": "axiom-of-choice-and-zorns-lemma",
    "中心極限定理": "central-limit-theorem",
    "ビュフォンの針": "buffons-needle",
    "ジップの法則": "zipfs-law",
    "カオス理論": "chaos-theory",
    "大数の法則": "law-of-large-numbers",
    "ベンフォードの法則": "benfords-law",
    "ライフゲーム": "conways-game-of-life",
    "コンウェイのライフゲーム": "conways-game-of-life",
}

sorted_keys = sorted(link_dict.keys(), key=len, reverse=True)
kw_pattern = '|'.join(map(re.escape, sorted_keys))

# Match existing links, code blocks, or inline code in group 1.
# Match keywords in group 2.
pattern = re.compile(r'(!?\[[^\]]*\]\([^\)]+\)|```.*?```|`[^`]+`)|(' + kw_pattern + r')', re.DOTALL)

def replacer(match):
    if match.group(1):
        return match.group(1)
    else:
        kw = match.group(2)
        slug = link_dict[kw]
        return f"[{kw}](https://kenji.blog/p/{slug}/)"

count = 0
for root, dirs, files in os.walk(blog_dir):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    front_matter = '---' + parts[1] + '---'
                    body = parts[2]
                else:
                    front_matter = ''
                    body = content
                
                new_body = pattern.sub(replacer, body)
                
                if new_body != body:
                    new_content = front_matter + new_body
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    count += 1
            except Exception as e:
                pass

print(f"Updated {count} markdown files.")
