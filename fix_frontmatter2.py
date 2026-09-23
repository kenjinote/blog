
import glob
import re
import yaml

def fix_frontmatter():
    articles = {
        "history-of-nvidia": {"cats": ["technology", "business"], "tags": ["nvidia", "gpu", "ai", "history", "jensen-huang"]},
        "history-of-alibaba": {"cats": ["technology", "business"], "tags": ["alibaba", "ecommerce", "china", "jack-ma", "alipay"]},
        "history-of-nec": {"cats": ["technology", "business"], "tags": ["nec", "history", "japan", "pc98"]},
        "history-of-panasonic": {"cats": ["technology", "business"], "tags": ["panasonic", "history", "japan", "ev"]},
        "history-of-ibm": {"cats": ["technology", "business"], "tags": ["ibm", "history", "mainframe", "quantum"]}
    }

    count = 0
    for slug, meta in articles.items():
        for file in glob.glob(f"c:/work/kenji.blog/content/post/{slug}/*.md"):
            try:
                with open(file, "r", encoding="utf-8") as f:
                    content = f.read()
                
                m = re.match(r"^---\n(.*?)\n---\n(.*)", content, re.DOTALL)
                if m:
                    fm_text = m.group(1)
                    body = m.group(2)
                    
                    new_fm_text = re.sub(r"categories:\n(?:[ ]+- .*\n)+", "categories:\n" + "".join([f"    - \"{c}\"\n" for c in meta["cats"]]), fm_text)
                    new_fm_text = re.sub(r"tags:\n(?:[ ]+- .*\n)+", "tags:\n" + "".join([f"    - \"{t}\"\n" for t in meta["tags"]]), new_fm_text)
                    
                    new_content = f"---\n{new_fm_text}\n---\n{body}"
                    
                    if new_content != content:
                        with open(file, "w", encoding="utf-8") as f:
                            f.write(new_content)
                        count += 1
            except Exception as e:
                print(f"Error {file}: {e}")
    print(f"Fixed {count} files.")

fix_frontmatter()

