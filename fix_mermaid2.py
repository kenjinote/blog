
import os
import glob
import re

# Match subgraph line
# Group 1: leading spaces
# Group 2: the rest of the line (the subgraph name/id)
pattern = re.compile(r"^(\s*)subgraph\s+(.+)$", re.MULTILINE)

count = 0
for file in glob.glob("c:/work/kenji.blog/content/post/**/*.md", recursive=True):
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = content
        def repl(match):
            indent = match.group(1)
            name = match.group(2).strip()
            
            # If it is already quoted, or if it is in the form ID ["Title"], leave it alone
            if name.startswith("\"") and name.endswith("\""):
                return match.group(0)
            if re.match(r"^\w+\s*\[.*?\]$", name):
                return match.group(0)
                
            # If it has spaces, parens, or non-alphanumeric chars (excluding CJK if we want, but simpler to just quote if it has space/parens/etc)
            # Actually, if it has a space or parenthesis, we should quote it.
            if re.search(r"[\s\(\)（）「」【】]", name):
                # Replace with: subgraph "name"
                return f"{indent}subgraph \"{name}\""
            
            return match.group(0)
            
        new_content = pattern.sub(repl, content)
        
        if new_content != content:
            with open(file, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            print(f"Fixed {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"Fixed {count} files.")

