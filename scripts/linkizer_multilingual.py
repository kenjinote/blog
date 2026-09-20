import os
import re

blog_dir = r'c:\work\kenji.blog\content\post'

link_dict = {}

# Step 1: Extract titles and short titles from ALL markdown files across all languages
for root, dirs, files in os.walk(blog_dir):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            slug = os.path.basename(root)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                slug_match = re.search(r'^slug:\s*"?([^"\r\n]+)"?', content, re.MULTILINE)
                if slug_match:
                    slug = slug_match.group(1)
                
                title_match = re.search(r'^title:\s*"?([^"\r\n]+)"?', content, re.MULTILINE)
                if title_match:
                    title = title_match.group(1).strip()
                    if title:
                        link_dict[title] = slug
                        
                        # Extract the main concept if title has a subtitle
                        delimiters = ['：', ':', ' - ', ' – ', ' — ', '|', '｜']
                        for d in delimiters:
                            if d in title:
                                short_title = title.split(d)[0].strip()
                                # Prevent matching very short common words
                                if short_title and len(short_title) > 2:
                                    link_dict[short_title] = slug
                                break
                                
            except Exception as e:
                pass

# Add some manual English keywords just in case
manual_dict = {
    "ABC conjecture": "abc-conjecture",
    "Fermat's Last Theorem": "fermats-last-theorem",
    "Galois theory": "galois-theory",
    "Poincaré conjecture": "poincare-conjecture",
    "Riemann hypothesis": "riemann-hypothesis",
    "Benford's Law": "benfords-law",
    "Conway's Game of Life": "conways-game-of-life",
}
for k, v in manual_dict.items():
    link_dict[k] = v

sorted_keys = sorted(link_dict.keys(), key=len, reverse=True)
kw_pattern = '|'.join(map(re.escape, sorted_keys))

pattern = re.compile(r'(!?\[[^\]]*\]\([^\)]+\)|```.*?```|`[^`]+`)|(' + kw_pattern + r')', re.DOTALL)

def replacer(match):
    if match.group(1):
        return match.group(1)
    else:
        kw = match.group(2)
        slug = link_dict[kw]
        return f"[{kw}](https://kenji.blog/p/{slug}/)"

# Step 2: Replace keywords in all markdown files
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
