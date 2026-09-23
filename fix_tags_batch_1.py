import os
import glob
import re

targets = [
    "biography-steve-jobs", "biography-bill-gates", "biography-linus-torvalds",
    "biography-dennis-ritchie", "biography-alan-kay", "biography-edsger-dijkstra",
    "biography-donald-knuth", "biography-guido-van-rossum", "biography-mark-zuckerberg",
    "biography-marc-andreessen", "biography-frederick-brooks", "biography-martin-fowler",
    "biography-steve-mcconnell", "biography-car-hoare", "biography-harold-abelson"
]

post_dir = "C:/work/kenji.blog/content/post"

for target in targets:
    # 対象ディレクトリの index.*.md を取得
    files = glob.glob(f"{post_dir}/{target}/index.*.md")
    
    # オリジナルのタグを取得 (index.md)
    base_file = f"{post_dir}/{target}/index.md"
    orig_tags = "[]"
    if os.path.exists(base_file):
        with open(base_file, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("tags:"):
                    orig_tags = line.strip()
                    break
    
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        # categoriesを強制修復
        content = re.sub(r'^categories:\s*\[?.*?\]?\r?\n', 'categories: ["biography"]\n', content, flags=re.MULTILINE)
        
        # tagsをオリジナルで置換
        if orig_tags != "[]":
            content = re.sub(r'^tags:\s*\[?.*?\]?\r?\n', f'{orig_tags}\n', content, flags=re.MULTILINE)
            
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)

print("Tag and Category restoration complete for Batch 1.")
