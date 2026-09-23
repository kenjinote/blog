
import glob
import re

for file in glob.glob("c:/work/kenji.blog/content/post/**/*.md", recursive=True):
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        for match in re.finditer(r"\[\"(.*?)\"\]", content):
            inner = match.group(1)
            if "\"" in inner:
                print(f"{file} -> {match.group(0)}")
    except Exception as e:
        pass

