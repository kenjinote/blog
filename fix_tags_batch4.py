
import glob
import re

articles = {
    "physics-noise-cancelling": {"cats": ["science", "physics"], "tags": ["physics", "sound", "noise-cancelling", "technology"]},
    "physics-bluetooth": {"cats": ["science", "technology"], "tags": ["physics", "bluetooth", "wireless", "network"]},
    "physics-wifi": {"cats": ["science", "technology"], "tags": ["physics", "wifi", "wireless", "network"]},
    "finance-fx-algo": {"cats": ["finance", "technology"], "tags": ["fx", "trading", "algorithm", "history"]},
    "history-of-winny": {"cats": ["technology", "computer-science"], "tags": ["p2p", "network", "winny", "history"]}
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

