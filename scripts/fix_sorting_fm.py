import os
import re

dir_path = r"c:\work\kenji.blog\content\post\sorting-algorithms"

# Target values we want to ensure
target_categories = 'categories: ["programming", "algorithms", "computer-science"]'
target_tags = 'tags: ["sort", "python", "algorithm", "big-o"]'

count = 0
for file in os.listdir(dir_path):
    if file.endswith('.md'):
        file_path = os.path.join(dir_path, file)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Use regex to replace the lines
            new_content = re.sub(r'^categories\s*:\s*\[.*?\]', target_categories, content, flags=re.MULTILINE)
            new_content = re.sub(r'^tags\s*:\s*\[.*?\]', target_tags, new_content, flags=re.MULTILINE)
            
            # Handle TOML format +++ as seen in the output
            new_content = re.sub(r'^categories\s*=\s*\[.*?\]', 'categories = ["programming", "algorithms", "computer-science"]', new_content, flags=re.MULTILINE)
            new_content = re.sub(r'^tags\s*=\s*\[.*?\]', 'tags = ["sort", "python", "algorithm", "big-o"]', new_content, flags=re.MULTILINE)

            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
        except Exception:
            pass

print(f"Fixed front matter in {count} files.")
