
import glob
import re

articles = {
    "network-vpn": {"cats": ["technology", "computer-science"], "tags": ["network", "vpn", "security", "remote"]},
    "network-ssl-tls": {"cats": ["technology", "computer-science"], "tags": ["network", "security", "ssl", "tls"]},
    "technology-cloud-computing": {"cats": ["technology", "computer-science"], "tags": ["cloud", "aws", "infrastructure", "virtualization"]},
    "technology-iot": {"cats": ["technology", "computer-science"], "tags": ["iot", "hardware", "sensor", "network"]},
    "history-of-ipv4": {"cats": ["technology", "history"], "tags": ["network", "internet", "ipv4", "ipv6"]}
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

