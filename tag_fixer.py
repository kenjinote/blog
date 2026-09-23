import os
import sys
import re

def fix_tags(original_path, translated_path):
    with open(original_path, 'r', encoding='utf-8') as f:
        orig = f.read()
    
    orig_match = re.match(r'^---\n(.*?)\n---\n', orig, re.DOTALL)
    if not orig_match:
        return
    orig_fm = orig_match.group(1)
    
    cat_match = re.search(r'^categories:\s*\[.*?\]', orig_fm, re.DOTALL | re.MULTILINE)
    tag_match = re.search(r'^tags:\s*\[.*?\]', orig_fm, re.DOTALL | re.MULTILINE)
    
    orig_cat = cat_match.group(0) if cat_match else "categories: []"
    orig_tag = tag_match.group(0) if tag_match else "tags: []"
    
    with open(translated_path, 'r', encoding='utf-8') as f:
        trans = f.read()
        
    trans_match = re.match(r'^---\n(.*?)\n---\n', trans, re.DOTALL)
    if not trans_match:
        return
    
    trans_fm = trans_match.group(1)
    
    if re.search(r'^categories:\s*\[.*?\]', trans_fm, re.DOTALL | re.MULTILINE):
        trans_fm = re.sub(r'^categories:\s*\[.*?\]', orig_cat, trans_fm, flags=re.DOTALL | re.MULTILINE)
    else:
        trans_fm += "\n" + orig_cat
        
    if re.search(r'^tags:\s*\[.*?\]', trans_fm, re.DOTALL | re.MULTILINE):
        trans_fm = re.sub(r'^tags:\s*\[.*?\]', orig_tag, trans_fm, flags=re.DOTALL | re.MULTILINE)
    else:
        trans_fm += "\n" + orig_tag
        
    new_trans = f"---\n{trans_fm}\n---" + trans[trans_match.end()-1:]
    
    with open(translated_path, 'w', encoding='utf-8') as f:
        f.write(new_trans)

def process_dir(post_dir):
    orig_path = os.path.join(post_dir, 'index.md')
    if not os.path.exists(orig_path):
        return
        
    for f in os.listdir(post_dir):
        if f != 'index.md' and f.endswith('.md'):
            fix_tags(orig_path, os.path.join(post_dir, f))

if __name__ == '__main__':
    process_dir(sys.argv[1])
