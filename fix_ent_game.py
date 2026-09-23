import os
import glob
import re

posts_dir = "c:/work/kenji.blog/content/post"
fixed_count = 0

replacements = {
    "Entertainment": "entertainment",
    "Game": "gaming",
    "Games": "gaming",
    "Gaming": "gaming"
}

for md_file in glob.glob(os.path.join(posts_dir, "*", "index*.md")):
    try:
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        # フロントマターを抽出 (YAMLの --- または TOMLの +++)
        m = re.match(r"^(---|(?:\+\+\+))\n(.*?)\n\1\n(.*)", content, re.DOTALL)
        if m:
            sep = m.group(1)
            frontmatter = m.group(2)
            body = m.group(3)
            
            new_frontmatter = frontmatter
            for old, new in replacements.items():
                # 単語境界で置換
                new_frontmatter = re.sub(rf"\b{old}\b", new, new_frontmatter)
                
            if new_frontmatter != frontmatter:
                new_content = f"{sep}\n{new_frontmatter}\n{sep}\n{body}"
                with open(md_file, "w", encoding="utf-8") as f:
                    f.write(new_content)
                fixed_count += 1
                
    except Exception as e:
        pass

print(f"Fixed {fixed_count} files.")
