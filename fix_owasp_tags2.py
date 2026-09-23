
import glob
import re

dir_path = "c:/work/kenji.blog/content/post/web-application-vulnerability-owasp-top-10/"

with open(dir_path + "index.md", "r", encoding="utf-8") as f:
    ja_content = f.read()

# Extract frontmatter blocks
fm_match = re.search(r"^---$(.*?)^---$", ja_content, re.MULTILINE | re.DOTALL)
if not fm_match:
    print("Could not find frontmatter in index.md")
    exit()

ja_fm = fm_match.group(1)

# We just want to extract the categories and tags section completely
# It might be easier to just copy the categories and tags lines
cat_tag_str = """categories:
    - "security"
    - "web"
tags:
    - "owasp"
    - "vulnerability"
    - "xss"
    - "sql-injection"
    - "csrf"
"""

for file in glob.glob(dir_path + "*.md"):
    if file.endswith("index.md"):
        continue
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We will replace categories and tags in the translated files
    # The translated files might have them in array format [ "..." ] or multi-line
    fm_match_target = re.search(r"^---$(.*?)^---$", content, re.MULTILINE | re.DOTALL)
    if fm_match_target:
        target_fm = fm_match_target.group(1)
        # Remove existing categories and tags
        target_fm = re.sub(r"^categories:.*?(?=^[a-z0-9_]+:|\Z)", "", target_fm, flags=re.MULTILINE | re.DOTALL)
        target_fm = re.sub(r"^tags:.*?(?=^[a-z0-9_]+:|\Z)", "", target_fm, flags=re.MULTILINE | re.DOTALL)
        
        # Add English categories and tags
        target_fm = target_fm.strip() + "\n" + cat_tag_str
        
        new_content = content[:fm_match_target.start(1)] + target_fm + "\n" + content[fm_match_target.end(1):]
        
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
    
print("Fixed tags for all translations.")

