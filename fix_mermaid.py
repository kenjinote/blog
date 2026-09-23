
import os
import glob
import re

pattern = re.compile(r"^(\s*)subgraph\s+([A-Za-z0-9_]+)\s*\((.*?)\)\s*$", re.MULTILINE)

count = 0
for file in glob.glob("c:/work/kenji.blog/content/post/**/*.md", recursive=True):
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content, num_subs = pattern.subn(r"\1subgraph \2 [\"\2 (\3)\"]", content)
        
        if num_subs > 0:
            with open(file, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            print(f"Fixed {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"Fixed {count} files.")

