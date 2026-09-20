import os
import re

blog_dir = r'c:\work\kenji.blog\content\post'

link_dict = {}

for root, dirs, files in os.walk(blog_dir):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            slug = os.path.basename(root)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                title_match = re.search(r'^title:\s*"?([^"\r\n]+)"?', content, re.MULTILINE)
                if title_match:
                    title = title_match.group(1).strip()
                    if title:
                        link_dict[title] = slug
                        delimiters = ['：', ':', ' - ', ' – ', ' — ', '|', '｜']
                        for d in delimiters:
                            if d in title:
                                short_title = title.split(d)[0].strip()
                                if short_title and len(short_title) > 2:
                                    link_dict[short_title] = slug
                                break
            except Exception:
                pass

manual_dict = {
    "ABC conjecture": "abc-conjecture",
    "Fermat's Last Theorem": "fermats-last-theorem",
    "Galois theory": "galois-theory",
    "Poincaré conjecture": "poincare-conjecture",
    "Riemann hypothesis": "riemann-hypothesis",
    "Benford's Law": "benfords-law",
    "Conway's Game of Life": "conways-game-of-life",
    "フィボナッチ": "fibonacci",
    "バシェ": "bachet",
    "メルセンヌ": "mersenne",
    "デカルト": "descartes",
    "アルキメデス": "archimedes",
    "ユークリッド": "euclid",
    "ピタゴラス": "pythagoras",
    "Fibonacci": "fibonacci",
    "Bachet": "bachet",
    "Mersenne": "mersenne",
    "Descartes": "descartes",
    "Archimedes": "archimedes",
    "Euclid": "euclid",
    "Pythagoras": "pythagoras",
}

for k, v in manual_dict.items():
    link_dict[k] = v

sorted_keys = [k for k in link_dict.keys() if len(k) > 2 and not k.isdigit()]
sorted_keys = sorted(sorted_keys, key=len, reverse=True)

split_pattern = re.compile(r'(!?\[[^\]]*\]\([^\)]+\)|```.*?```|`[^`]+`)', re.DOTALL)

count = 0
for root, dirs, files in os.walk(blog_dir):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            
            lang_prefix = ""
            parts_file = file.split('.')
            if len(parts_file) == 3 and parts_file[2] == 'md':
                lang_prefix = "/" + parts_file[1]

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
                
                tokens = split_pattern.split(body)
                
                changed = False
                for i in range(0, len(tokens)):
                    text = tokens[i]
                    if not text: continue
                    
                    if i % 2 == 0:
                        # Unprotected text, perform keyword replacement
                        for kw in sorted_keys:
                            if kw in text:
                                slug = link_dict[kw]
                                link_str = f"[{kw}](https://kenji.blog{lang_prefix}/p/{slug}/)"
                                text = text.replace(kw, link_str)
                                changed = True
                        tokens[i] = text
                    else:
                        # Protected text (like existing links)
                        # We might need to fix old links that point to the wrong language prefix, but we already did that in the previous step.
                        # Wait, if we replace NEW keywords here, we must make sure we don't double link. The split_pattern takes care of this because new keywords are replaced in unprotected text.
                        pass
                
                if changed:
                    new_body = "".join(tokens)
                    new_content = front_matter + new_body
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    count += 1
            except Exception:
                pass

print(f"Updated {count} markdown files.")
