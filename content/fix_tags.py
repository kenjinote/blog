import os
import sys

base_dir = r"c:\work\kenji.blog\content\post"

def get_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if not lines or lines[0].strip() != '---':
        return None, lines
    end_idx = -1
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end_idx = i
            break
    if end_idx != -1:
        return lines[1:end_idx], lines[end_idx+1:]
    return None, lines

for slug in os.listdir(base_dir):
    dir_path = os.path.join(base_dir, slug)
    if not os.path.isdir(dir_path):
        continue
    index_path = os.path.join(dir_path, "index.md")
    if not os.path.exists(index_path):
        continue
        
    fm, _ = get_frontmatter(index_path)
    if not fm:
        continue
        
    cats = []
    tags = []
    in_cat = False
    in_tag = False
    for line in fm:
        if line.startswith('categories:'):
            in_cat = True
            in_tag = False
        elif line.startswith('tags:'):
            in_tag = True
            in_cat = False
        elif line.startswith('slug:') or line.startswith('image:') or line.startswith('title:') or line.startswith('date:'):
            in_cat = False
            in_tag = False
        elif in_cat and line.strip().startswith('-'):
            cats.append(line.strip('\n'))
        elif in_tag and line.strip().startswith('-'):
            tags.append(line.strip('\n'))
            
    cat_str = "categories:\n" + "\n".join(cats) + "\n" if cats else ""
    tag_str = "tags:\n" + "\n".join(tags) + "\n" if tags else ""
    
    for filename in os.listdir(dir_path):
        if filename.endswith('.md') and filename != 'index.md':
            filepath = os.path.join(dir_path, filename)
            trans_fm, trans_content = get_frontmatter(filepath)
            if not trans_fm:
                continue
            
            new_fm_lines = []
            skip = False
            for line in trans_fm:
                if line.startswith('categories:') or line.startswith('tags:'):
                    skip = True
                elif line.startswith('slug:') or line.startswith('image:') or line.startswith('title:') or line.startswith('date:'):
                    skip = False
                
                if not skip:
                    new_fm_lines.append(line)
            
            new_fm = "---\n" + "".join(new_fm_lines).strip() + "\n\n" + cat_str + tag_str + "---\n"
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_fm + "".join(trans_content))

print("Tags fixed for all files.")
