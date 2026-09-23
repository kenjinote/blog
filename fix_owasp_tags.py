
import glob
import re

dir_path = "c:/work/kenji.blog/content/post/web-application-vulnerability-owasp-top-10/"

with open(dir_path + "index.md", "r", encoding="utf-8") as f:
    ja_content = f.read()

categories_match = re.search(r"^categories:\s*\[.*?\]", ja_content, re.MULTILINE)
tags_match = re.search(r"^tags:\s*\[.*?\]", ja_content, re.MULTILINE)

if not categories_match or not tags_match:
    print("Could not find categories or tags in index.md")
    exit()

cat_str = categories_match.group(0)
tag_str = tags_match.group(0)

for file in glob.glob(dir_path + "*.md"):
    if file.endswith("index.md"):
        continue
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = re.sub(r"^categories:\s*\[.*?\]", cat_str, content, flags=re.MULTILINE)
    new_content = re.sub(r"^tags:\s*\[.*?\]", tag_str, new_content, flags=re.MULTILINE)
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(new_content)
    
print("Fixed tags for all translations.")

