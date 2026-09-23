import os
import glob
import re

post_dir = "C:/work/kenji.blog/content/post"
files = glob.glob(f"{post_dir}/**/*.md", recursive=True)

fixed_count = 0

for file_path in files:
    # Get the parent directory name to use as slug
    dir_name = os.path.basename(os.path.dirname(file_path))
    if dir_name == "post":
        continue # Should not happen if organized in bundles, but just in case
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, flags=re.DOTALL)
    if not match:
        continue

    frontmatter = match.group(1)
    body = match.group(2)
    
    # Check if slug already exists
    if not re.search(r'^slug:\s+', frontmatter, flags=re.MULTILINE):
        # Insert slug at the end of frontmatter
        new_frontmatter = frontmatter + f'\nslug: "{dir_name}"'
        new_content = f"---\n{new_frontmatter}\n---\n{body}"
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        fixed_count += 1

print(f"Added slug to {fixed_count} files.")
