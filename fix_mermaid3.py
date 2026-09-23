
import glob
import re

count = 0
for file in glob.glob("c:/work/kenji.blog/content/post/**/*.md", recursive=True):
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = content.replace(r"[\\\"", "[\"").replace(r"\\\"]", "\"]")
        # Also fix subgraph \"Name\"
        new_content = new_content.replace(r"subgraph \"", "subgraph \"").replace(r"subgraph \\\"", "subgraph \"")
        
        if new_content != content:
            with open(file, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            print(f"Fixed {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"Fixed {count} files.")

