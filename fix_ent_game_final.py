import os
import glob
import re

posts_dir = "c:/work/kenji.blog/content/post"
fixed_count = 0

# カテゴリの本来あるべき統合ルール
replacements = {
    '"entertainment"': '"lifestyle-miscellaneous"',
    "'entertainment'": "'lifestyle-miscellaneous'",
    " entertainment": " lifestyle-miscellaneous",
    
    '"game"': '"gaming"',
    "'game'": "'gaming'",
    " game": " gaming",
    
    '"Entertainment"': '"lifestyle-miscellaneous"',
    "'Entertainment'": "'lifestyle-miscellaneous'",
    " Entertainment": " lifestyle-miscellaneous",
    
    '"Game"': '"gaming"',
    "'Game'": "'gaming'",
    " Game": " gaming"
}

for md_file in glob.glob(os.path.join(posts_dir, "*", "index*.md")):
    try:
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        # フロントマターを抽出
        m = re.match(r"^(---|(?:\+\+\+))\n(.*?)\n\1\n(.*)", content, re.DOTALL)
        if m:
            sep = m.group(1)
            frontmatter = m.group(2)
            body = m.group(3)
            
            new_frontmatter = frontmatter
            # categories ブロックだけを置換するように、行ごとに処理
            lines = new_frontmatter.split("\n")
            in_categories = False
            for i, line in enumerate(lines):
                if line.startswith("categories:"):
                    # 行内の配列パターンの置換: categories: ["game"]
                    for old, new in replacements.items():
                        line = line.replace(old, new)
                    lines[i] = line
                    in_categories = True
                elif in_categories and line.strip().startswith("-"):
                    # リストパターンの置換: - "game"
                    for old, new in replacements.items():
                        line = line.replace(old, new)
                    lines[i] = line
                elif in_categories and not line.strip().startswith("-") and line.strip() != "":
                    in_categories = False
            
            new_frontmatter = "\n".join(lines)
                
            if new_frontmatter != frontmatter:
                new_content = f"{sep}\n{new_frontmatter}\n{sep}\n{body}"
                with open(md_file, "w", encoding="utf-8") as f:
                    f.write(new_content)
                fixed_count += 1
                
    except Exception as e:
        pass

print(f"Fixed {fixed_count} files.")
