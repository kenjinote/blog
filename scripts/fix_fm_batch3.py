import os
import glob
import re

directories = [
    r"c:\work\kenji.blog\content\post\oop-vs-fp-vs-dop",
    r"c:\work\kenji.blog\content\post\state-management-history-future",
    r"c:\work\kenji.blog\content\post\memory-management-garbage-collection",
    r"c:\work\kenji.blog\content\post\design-patterns-modern-practices",
    r"c:\work\kenji.blog\content\post\event-driven-architecture-async"
]

def extract_fm(content):
    match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    return match.group(1) if match else None

def get_categories_tags(fm):
    categories = re.search(r'^categories:\s*(\[.*?\])', fm, re.MULTILINE)
    tags = re.search(r'^tags:\s*(\[.*?\])', fm, re.MULTILINE)
    return (categories.group(1) if categories else None, tags.group(1) if tags else None)

for d in directories:
    ja_file = os.path.join(d, "index.md")
    if not os.path.exists(ja_file):
        continue
    
    with open(ja_file, "r", encoding="utf-8") as f:
        ja_content = f.read()
    
    ja_fm = extract_fm(ja_content)
    if not ja_fm:
        continue
        
    c_match, t_match = get_categories_tags(ja_fm)
    
    for md_file in glob.glob(os.path.join(d, "index.*.md")):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not fm_match:
            continue
            
        new_fm = fm_match.group(1)
        if c_match:
            new_fm = re.sub(r'^categories:\s*\[.*?\]', f'categories: {c_match}', new_fm, flags=re.MULTILINE)
        if t_match:
            new_fm = re.sub(r'^tags:\s*\[.*?\]', f'tags: {t_match}', new_fm, flags=re.MULTILINE)
            
        body = content[fm_match.end():]
        body = re.sub(r'(?<!\$)\$\$(?!\$)(.*?)(?<!\$)\$\$(?!\$)', lambda m: f"${m.group(1)}$" if '\n' not in m.group(1) else f"$${m.group(1)}$$", body)
        
        new_content = f"---\n{new_fm}\n---{body}"
        
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(new_content)
            
print("Fixed front matter and inline math for phase 3.")
