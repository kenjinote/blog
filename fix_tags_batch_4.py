import os
import glob
import re

targets = [
    "biography-william-shakespeare", "biography-pablo-picasso", "biography-michelangelo",
    "biography-walt-disney", "biography-charles-chaplin", "biography-oscar-wilde",
    "biography-jean-jacques-rousseau", "biography-j-r-r-tolkien", "biography-lewis-carroll",
    "biography-neil-armstrong"
]

post_dir = "C:/work/kenji.blog/content/post"

for target in targets:
    files = glob.glob(f"{post_dir}/{target}/index.*.md")
    
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
            
        content = re.sub(r'^categories:\s*\[?.*?\]?\r?\n', 'categories: ["biography"]\n', content, flags=re.MULTILINE)
        if orig_tags != "[]":
            content = re.sub(r'^tags:\s*\[?.*?\]?\r?\n', f'{orig_tags}\n', content, flags=re.MULTILINE)
            
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)

    all_files = glob.glob(f"{post_dir}/{target}/*")
    for file in all_files:
        basename = os.path.basename(file)
        if not re.match(r'^index(\.[a-z]{2}(-[a-z]{2})?)?\.md$', basename) and not basename.endswith(('.jpg', '.png', '.webp', '.jpeg', '.gif')):
            if os.path.isfile(file):
                os.remove(file)

print("Tag and Category restoration & Cleanup complete for Batch 4.")
