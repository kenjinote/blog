import os
import re

blog_dir = r'c:\work\kenji.blog\content\post'

link_dict = {
    "ABC予想": "abc-conjecture",
    "フェルマーの最終定理": "fermats-last-theorem",
    "ガロア理論": "galois-theory",
    "ポアンカレ予想": "poincare-conjecture",
    "リーマン予想": "riemann-hypothesis",
    "ゲーデルの不完全性定理": "godels-incompleteness-theorems",
    "不完全性定理": "godels-incompleteness-theorems",
    "四色定理": "four-color-theorem",
    "ABC conjecture": "abc-conjecture",
    "Fermat's Last Theorem": "fermats-last-theorem",
    "Galois theory": "galois-theory",
    "Poincaré conjecture": "poincare-conjecture",
    "Riemann hypothesis": "riemann-hypothesis",
    "Gödel's incompleteness theorems": "godels-incompleteness-theorems",
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

def add_links_to_text(text):
    # Sort keys by length descending to match longer phrases first
    sorted_keys = sorted(link_dict.keys(), key=len, reverse=True)
    
    parts = text.split('---')
    if len(parts) >= 3:
        front_matter = '---' + parts[1] + '---'
        content = '---'.join(parts[2:])
    else:
        front_matter = ''
        content = text
        
    placeholders = {}
    counter = 0
    
    # Protect code blocks
    for m in re.finditer(r'`.*?`', content, re.DOTALL):
        p = f"__P_CODE_BLOCK_{counter}__"
        placeholders[p] = m.group(0)
        content = content.replace(m.group(0), p)
        counter += 1
        
    # Protect inline code
    for m in re.finditer(r'[^]+', content):
        p = f"__P_INLINE_CODE_{counter}__"
        placeholders[p] = m.group(0)
        content = content.replace(m.group(0), p)
        counter += 1

    # Protect existing links (including images)
    for m in re.finditer(r'!?\[([^\]]*)\]\([^\)]+\)', content):
        p = f"__P_LINK_{counter}__"
        placeholders[p] = m.group(0)
        content = content.replace(m.group(0), p)
        counter += 1

    # Protect headers
    for m in re.finditer(r'^#+ .*$', content, re.MULTILINE):
        p = f"__P_HEADER_{counter}__"
        placeholders[p] = m.group(0)
        content = content.replace(m.group(0), p)
        counter += 1

    # Simple replace
    for keyword in sorted_keys:
        slug = link_dict[keyword]
        link_str = f"[{keyword}](https://kenji.blog/p/{slug}/)"
        content = content.replace(keyword, link_str)
            
    # Restore placeholders in reverse order
    for p, orig in reversed(list(placeholders.items())):
        content = content.replace(p, orig)
        
    return front_matter + content

def process_directory():
    count = 0
    for root, dirs, files in os.walk(blog_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        original_text = f.read()
                        
                    new_text = add_links_to_text(original_text)
                    
                    if new_text != original_text:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_text)
                        count += 1
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    print(f"Updated {count} markdown files.")

if __name__ == '__main__':
    process_directory()
