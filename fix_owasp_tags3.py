
import glob
import re

dir_path = "c:/work/kenji.blog/content/post/web-application-vulnerability-owasp-top-10/"

for file in glob.glob(dir_path + "*.md"):
    if file.endswith("index.md"):
        continue
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Fix the missing newline after first ---
    new_content = re.sub(r"^---title:", "---\ntitle:", content)
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(new_content)
    
print("Fixed missing newlines.")

