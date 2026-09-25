import os
import glob
import re

post_dir = "C:/work/kenji.blog/content/post"
files = glob.glob(f"{post_dir}/biography-*/**/*.md", recursive=True)

missing_count = 0
missing_files = []

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, flags=re.DOTALL)
    if not match:
        continue

    frontmatter = match.group(1)
    
    if not re.search(r'^description:\s+', frontmatter, flags=re.MULTILINE):
        missing_count += 1
        missing_files.append(file_path)

print(f"Missing description in {missing_count} files out of {len(files)} total biography files.")
if missing_count > 0:
    print("Example missing files:")
    for f in missing_files[:5]:
        print(f)
