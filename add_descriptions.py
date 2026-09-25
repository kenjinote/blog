#!/usr/bin/env python3
"""
Add description to biography article frontmatter.
For index.md (Japanese): extract first meaningful paragraph and trim to ~150 chars.
For index.*.md (translations): extract first meaningful paragraph and trim to ~150 chars.
"""
import os
import glob
import re

post_dir = "C:/work/kenji.blog/content/post"
dirs = sorted(glob.glob(f"{post_dir}/biography-*/"))

added = 0
skipped = 0

for d in dirs:
    files = glob.glob(os.path.join(d, "index*.md"))
    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        match = re.match(r'^---\n(.*?)\n---\n(.*)', content, flags=re.DOTALL)
        if not match:
            continue

        frontmatter = match.group(1)
        body = match.group(2)

        # Skip if description already exists
        if re.search(r'^description:\s+', frontmatter, flags=re.MULTILINE):
            skipped += 1
            continue

        # Extract first meaningful paragraph from body
        # Skip empty lines, headings, mermaid blocks, images
        paragraphs = body.strip().split('\n\n')
        desc_text = ""
        for para in paragraphs:
            para = para.strip()
            # Skip empty, headings, code blocks, images, mermaid
            if not para:
                continue
            if para.startswith('#'):
                continue
            if para.startswith('```'):
                continue
            if para.startswith('!['):
                continue
            if para.startswith('{{'):
                continue
            # Clean markdown formatting
            clean = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', para)  # links
            clean = re.sub(r'\*\*([^*]+)\*\*', r'\1', clean)  # bold
            clean = re.sub(r'\*([^*]+)\*', r'\1', clean)  # italic
            clean = re.sub(r'`([^`]+)`', r'\1', clean)  # inline code
            clean = re.sub(r'\$[^$]+\$', '', clean)  # inline math
            clean = clean.replace('\r', '').replace('\n', ' ').strip()
            if len(clean) > 30:  # meaningful content
                desc_text = clean
                break

        if not desc_text:
            continue

        # Trim to ~150 chars at sentence boundary
        if len(desc_text) > 160:
            # Try to cut at a sentence boundary (。or . or 、)
            cut_pos = -1
            for sep in ['。', '. ', '、']:
                pos = desc_text.find(sep, 80)
                if pos != -1 and pos < 160:
                    cut_pos = pos + len(sep)
                    break
            if cut_pos == -1:
                cut_pos = 155
            desc_text = desc_text[:cut_pos].rstrip()

        # Escape double quotes in description
        safe_desc = desc_text.replace('"', '\\"')
        
        # Add description to frontmatter (before the last line or after title)
        new_frontmatter = frontmatter + f'\ndescription: "{safe_desc}"'
        new_content = f"---\n{new_frontmatter}\n---\n{body}"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        added += 1

print(f"Added description to {added} files. Skipped {skipped} (already had description).")
