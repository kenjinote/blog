import os
import glob
import re

posts_dir = "c:/work/kenji.blog/content/post"
fixed_count = 0

replacements = {
    "AI": "ai",
    "Business": "business",
    "Gaming": "gaming",
    "Networking": "networking",
    "Space": "space",
    "数学": "mathematics",
    "伝記": "biography"
}

def fix_cats_in_match(match):
    cat_str = match.group(1)
    for old, new in replacements.items():
        cat_str = re.sub(r"(['" + '"' + r"])" + old + r"(['" + '"' + r"])", r"\g<1>" + new + r"\g<2>", cat_str)
    return "categories: [" + cat_str + "]"

for md_file in glob.glob(os.path.join(posts_dir, "*", "*.md")):
    try:
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        # 1行配列パターン: categories: ["AI", "Gaming"]
        new_content = re.sub(r"categories\s*:\s*\[(.*?)\]", fix_cats_in_match, content)
        
        # 複数行パターン: categories:\n  - "AI"
        for old, new in replacements.items():
            new_content = re.sub(r"(categories:\s*\n(?:\s+-\s+.*\n)*\s+-\s+['" + '"' + r"]?)" + old + r"(['" + '"' + r"]?\s*\n)", r"\g<1>" + new + r"\g<2>", new_content)
            
        if new_content != content:
            with open(md_file, "w", encoding="utf-8") as f:
                f.write(new_content)
            fixed_count += 1
            print(f"Fixed: {md_file}")
            
    except Exception as e:
        print(f"Error {md_file}: {e}")

print(f"Fixed categories in {fixed_count} files.")
