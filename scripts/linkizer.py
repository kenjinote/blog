import os
import json
import re

blog_dir = r'c:\work\kenji.blog\content\post'

# Dictionary of keywords to slugs
# Format: "Keyword in text": "slug"
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
    
    # Mathematicians
    "エミー・ネーター": "noether",
    "ラマヌジャン": "ramanujan",
    "シュリニヴァーサ・ラマヌジャン": "ramanujan",
    "モーデル": "mordell",
    "ジーゲル": "siegel",
    "ハッセ": "hasse",
    "岡潔": "oka-kiyoshi",
    "フォン・ノイマン": "von-neumann",
    "ジョン・フォン・ノイマン": "von-neumann",
    "ヴェイユ": "weil",
    "ゲーデル": "godel",
    "クルト・ゲーデル": "godel",
    "チューリング": "turing",
    "アラン・チューリング": "turing",
    "小平邦彦": "kodaira-kunihiko",
    "伊藤清": "ito-kiyosi",
    "谷山豊": "taniyama-yutaka",
    "グロタンディーク": "grothendieck",
    "アレクサンドル・グロタンディーク": "grothendieck",
    "志村五郎": "shimura-goro",
    "広中平祐": "hironaka-heisuke",
    "ベーカー": "baker",
    "アラン・ベーカー": "baker",
    "ワイルズ": "wiles",
    "アンドリュー・ワイルズ": "wiles",
    "ファルティングス": "faltings",
    "ゲルト・ファルティングス": "faltings",
    "オイラー": "euler",
    "ガウス": "gauss",
    "ニュートン": "newton",
    "ライプニッツ": "leibniz",
    "ピタゴラス": "pythagoras",
    
    # Mathematical concepts
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
    
    # We need to avoid replacing text that is already inside a markdown link: [text](link)
    # or inside html tags, or front matter.
    
    # Split text into front matter and content
    parts = text.split('---')
    if len(parts) >= 3:
        front_matter = '---' + parts[1] + '---'
        content = '---'.join(parts[2:])
    else:
        front_matter = ''
        content = text
        
    # We will use a regex to find all existing links and code blocks to avoid replacing inside them.
    # Placeholder approach:
    placeholders = {}
    counter = 0
    
    # Protect code blocks
    code_block_pattern = re.compile(r'`.*?`', re.DOTALL)
    for m in code_block_pattern.finditer(content):
        placeholder = f"__CODE_BLOCK_{counter}__"
        placeholders[placeholder] = m.group(0)
        content = content.replace(m.group(0), placeholder)
        counter += 1
        
    # Protect inline code
    inline_code_pattern = re.compile(r'[^]+')
    for m in inline_code_pattern.finditer(content):
        placeholder = f"__INLINE_CODE_{counter}__"
        placeholders[placeholder] = m.group(0)
        content = content.replace(m.group(0), placeholder)
        counter += 1

    # Protect existing links
    link_pattern = re.compile(r'\[([^\]]+)\]\([^\)]+\)')
    for m in link_pattern.finditer(content):
        placeholder = f"__LINK_{counter}__"
        placeholders[placeholder] = m.group(0)
        content = content.replace(m.group(0), placeholder)
        counter += 1
        
    # Protect image links
    img_pattern = re.compile(r'!\[([^\]]*)\]\([^\)]+\)')
    for m in img_pattern.finditer(content):
        placeholder = f"__IMG_{counter}__"
        placeholders[placeholder] = m.group(0)
        content = content.replace(m.group(0), placeholder)
        counter += 1

    # Protect headers (so we don't link inside headers)
    header_pattern = re.compile(r'^#+ .*$', re.MULTILINE)
    for m in header_pattern.finditer(content):
        placeholder = f"__HEADER_{counter}__"
        placeholders[placeholder] = m.group(0)
        content = content.replace(m.group(0), placeholder)
        counter += 1

    # Now replace keywords
    for keyword in sorted_keys:
        slug = link_dict[keyword]
        link_str = f"[{keyword}](https://kenji.blog/p/{slug}/)"
        
        # Word boundary for English words, simple replace for Japanese
        if re.match(r'^[A-Za-z0-9 ]+$', keyword):
            # English keyword, use word boundaries
            pattern = re.compile(r'\b' + re.escape(keyword) + r'\b')
            content = pattern.sub(link_str, content)
        else:
            # Japanese keyword, simple replace
            content = content.replace(keyword, link_str)
            
    # Restore placeholders
    # Do this in reverse order of creation just in case
    for placeholder, original in reversed(placeholders.items()):
        content = content.replace(placeholder, original)
        
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
