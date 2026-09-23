import os
import glob
import re

post_dir = "C:/work/kenji.blog/content/post"
files = glob.glob(f"{post_dir}/**/*.md", recursive=True)

fixed_count = 0

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the frontmatter block
    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, flags=re.DOTALL)
    if not match:
        continue

    frontmatter = match.group(1)
    body = match.group(2)
    new_frontmatter_lines = []
    modified = False

    for line in frontmatter.split('\n'):
        if line.startswith('title:'):
            value = line[6:].strip()
            # If the value is not quoted and contains a colon, we need to quote it
            # Actually, to be safe, let's quote any unquoted title
            if value and not (value.startswith('"') and value.endswith('"')) and not (value.startswith("'") and value.endswith("'")):
                # Escape existing double quotes
                safe_value = value.replace('"', '\\"')
                line = f'title: "{safe_value}"'
                modified = True
        new_frontmatter_lines.append(line)
        
    if modified:
        new_frontmatter = '\n'.join(new_frontmatter_lines)
        new_content = f"---\n{new_frontmatter}\n---\n{body}"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        fixed_count += 1

print(f"Fixed {fixed_count} files.")
