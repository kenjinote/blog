import os
import re

blog_dir = r'c:\work\kenji.blog\content\post'
target_slug = 'cryptocurrency-and-bitcoin'
target_dir = os.path.join(blog_dir, target_slug)

link_dict = {}

# Extract titles from cryptocurrency-and-bitcoin articles
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
    "仮想通貨": target_slug,
    "暗号資産": target_slug,
    "ビットコイン": target_slug,
    "Bitcoin": target_slug,
    "Cryptocurrency": target_slug,
    "Crypto": target_slug,
    "Crypto-monnaie": target_slug,
    "Criptomoneda": target_slug,
    "Criptomoeda": target_slug,
    "Kryptowährung": target_slug,
    "암호화폐": target_slug,
    "가상화폐": target_slug,
    "비트코인": target_slug,
    "加密货币": target_slug,
    "比特币": target_slug,
    "加密貨幣": target_slug,
    "比特幣": target_slug,
    "Mata uang kripto": target_slug,
    "Криптовалюта": target_slug,
    "Биткойн": target_slug,
    "Биткоин": target_slug,
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
            
            # Skip the target directory itself to avoid self-linking too much, though it's optional
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
                            if kw in text:
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

print(f"Updated {count} markdown files for cryptocurrency links.")
