import os
import re

blog_dir = r'c:\work\kenji.blog\content\post'
target_slug = 'sorting-algorithms'
target_dir = os.path.join(blog_dir, target_slug)

link_dict = {}

# Extract titles from sorting-algorithms articles
if os.path.exists(target_dir):
    for file in os.listdir(target_dir):
        if file.endswith('.md'):
            file_path = os.path.join(target_dir, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                title_match = re.search(r'^title:\s*"?([^"\r\n]+)"?', content, re.MULTILINE)
                if title_match:
                    title = title_match.group(1).strip()
                    if title:
                        link_dict[title] = target_slug
                        delimiters = ['：', ':', ' - ', ' – ', ' — ', '|', '｜']
                        for d in delimiters:
                            if d in title:
                                short_title = title.split(d)[0].strip()
                                if short_title and len(short_title) > 2:
                                    link_dict[short_title] = target_slug
                                break
            except Exception:
                pass

# Add common keywords explicitly
manual_dict = {
    "ソート": target_slug,
    "ソートアルゴリズム": target_slug,
    "バブルソート": target_slug,
    "クイックソート": target_slug,
    "マージソート": target_slug,
    "ヒープソート": target_slug,
    "挿入ソート": target_slug,
    "ティムソート": target_slug,
    "Timsort": target_slug,
    "Quicksort": target_slug,
    "Mergesort": target_slug,
    "Sorting algorithm": target_slug,
    "Sorting": target_slug,
    "Sortieren": target_slug, # German
    "Algoritmo de ordenación": target_slug, # Spanish
    "Tri": target_slug, # French (e.g., Algorithme de tri)
    "Algorithme de tri": target_slug,
    "Сортировка": target_slug, # Russian
    "Алгоритм сортировки": target_slug,
    "정렬": target_slug, # Korean
    "정렬 알고리즘": target_slug,
    "排序": target_slug, # Chinese
    "排序算法": target_slug,
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
            
            # Skip the target directory itself to avoid self-linking
            if target_slug in root:
                continue

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
                        for kw in sorted_keys:
                            # Use \b to match exact words for English, but \b doesn't work well for CJK
                            # For simple replace without \b:
                            if kw in text:
                                # For short english words like "Tri", we should be careful. 
                                # Let's only replace if it's not part of another english word
                                if kw.isalpha() and len(kw) <= 4:
                                    pattern = r'(?<![a-zA-Z])' + re.escape(kw) + r'(?![a-zA-Z])'
                                    if re.search(pattern, text):
                                        link_str = f"[{kw}](https://kenji.blog{lang_prefix}/p/{target_slug}/)"
                                        text = re.sub(pattern, link_str, text)
                                        changed = True
                                else:
                                    link_str = f"[{kw}](https://kenji.blog{lang_prefix}/p/{target_slug}/)"
                                    text = text.replace(kw, link_str)
                                    changed = True
                        tokens[i] = text
                
                if changed:
                    new_body = "".join(tokens)
                    new_content = front_matter + new_body
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    count += 1
            except Exception:
                pass

print(f"Updated {count} markdown files for sorting algorithm links.")
