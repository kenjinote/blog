import os
import glob
import re

directories = [
    r"c:\work\kenji.blog\content\post\time-space-complexity-big-o-notation-examples",
    r"c:\work\kenji.blog\content\post\sorting-algorithms-visualized-bubble-quick-merge",
    r"c:\work\kenji.blog\content\post\search-algorithms-linear-binary-hash-table-principles",
    r"c:\work\kenji.blog\content\post\tree-graph-data-structures-search-dfs-bfs-dijkstra",
    r"c:\work\kenji.blog\content\post\dynamic-programming-dp-introduction-knapsack-fibonacci"
]

def extract_fm(content):
    match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    return match.group(1) if match else None

def get_categories_tags(fm):
    categories = re.search(r'^categories:\s*(\[.*?\])', fm, re.MULTILINE)
    tags = re.search(r'^tags:\s*(\[.*?\])', fm, re.MULTILINE)
    
    cat_res = categories.group(1) if categories else None
    tag_res = tags.group(1) if tags else None
    
    if not cat_res:
        categories = re.search(r'^categories:\n((?:\s+- .*\n?)+)', fm, re.MULTILINE)
        cat_res = "\n" + categories.group(1).rstrip() if categories else None
    if not tag_res:
        tags = re.search(r'^tags:\n((?:\s+- .*\n?)+)', fm, re.MULTILINE)
        tag_res = "\n" + tags.group(1).rstrip() if tags else None
        
    return (cat_res, tag_res)

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
            new_fm = re.sub(r'^categories:\n(?:\s+- .*\n?)+', f'categories:{c_match}\n', new_fm, flags=re.MULTILINE)
        if t_match:
            new_fm = re.sub(r'^tags:\s*\[.*?\]', f'tags: {t_match}', new_fm, flags=re.MULTILINE)
            new_fm = re.sub(r'^tags:\n(?:\s+- .*\n?)+', f'tags:{t_match}\n', new_fm, flags=re.MULTILINE)
            
        body = content[fm_match.end():]
        body = re.sub(r'(?<!\$)\$\$(?!\$)(.*?)(?<!\$)\$\$(?!\$)', lambda m: f"${m.group(1)}$" if '\n' not in m.group(1) else f"$${m.group(1)}$$", body)
        
        new_content = f"---\n{new_fm}\n---{body}"
        
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(new_content)
            
print("Fixed front matter and inline math for phase 8.")
