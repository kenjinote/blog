import os
import glob
import re
from collections import Counter

posts_dir = "c:/work/kenji.blog/content/post"
cats = Counter()

for md_file in glob.glob(os.path.join(posts_dir, "*", "index.md")):
    try:
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        m = re.search(r"^(?:---|+++)\n(.*?)\n(?:---|+++)", content, re.DOTALL)
        frontmatter = content
        if m:
            frontmatter = m.group(1)
            
        # 1行形式
        m1 = re.search(r"categories\s*[:=]\s*\[(.*?)\]", frontmatter)
        if m1:
            items = m1.group(1).split(",")
            for item in items:
                cat = item.strip().strip("\"'")
                if cat:
                    cats[cat] += 1
                    
        # 複数行形式
        m2 = re.search(r"^categories:\s*\n((?:\s+-\s+.*(?:\n|$))+)", frontmatter, re.MULTILINE)
        if m2:
            lines = m2.group(1).strip().split("\n")
            for line in lines:
                mm = re.match(r"\s+-\s+[\"']?(.*?)[\"']?\s*$", line)
                if mm:
                    cat = mm.group(1).strip()
                    cats[cat] += 1

    except Exception as e:
        pass

for k in sorted(cats.keys()):
    print(f"{k}: {cats[k]}")
