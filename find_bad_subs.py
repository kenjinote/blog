
import glob
import re

pattern = re.compile(r"^(\s*)subgraph\s+([^\"\[\]]+)$", re.MULTILINE)

bad_subs = []
for file in glob.glob("c:/work/kenji.blog/content/post/**/*.md", recursive=True):
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        for match in pattern.finditer(content):
            val = match.group(2).strip()
            if re.search(r"[\s\(\)]", val):
                bad_subs.append(f"{file}: {val}")
    except Exception as e:
        pass

for b in bad_subs:
    print(b)

