import os
import glob
import re
import shutil

targets = [
    "biography-abraham-lincoln", "biography-winston-churchill", "biography-john-f-kennedy",
    "biography-franklin-d-roosevelt", "biography-martin-luther-king-jr", "biography-mahatma-gandhi",
    "biography-nelson-mandela", "biography-napoleon-bonaparte", "biography-julius-caesar",
    "biography-otto-von-bismarck", "biography-benjamin-franklin", "biography-mother-teresa"
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

    # ゴミファイル削除
    all_files = glob.glob(f"{post_dir}/{target}/*")
    for file in all_files:
        basename = os.path.basename(file)
        if not re.match(r'^index(\.[a-z]{2}(-[a-z]{2})?)?\.md$', basename) and not basename.endswith(('.jpg', '.png', '.webp', '.jpeg', '.gif')):
            if os.path.isfile(file):
                os.remove(file)

print("Tag and Category restoration & Cleanup complete for Batch 2.")
