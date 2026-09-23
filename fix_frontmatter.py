
import glob
import re
import yaml
import io

def fix_frontmatter():
    articles = {
        "history-of-apple": {"cats": ["technology", "business"], "tags": ["apple", "history", "steve-jobs", "iphone", "innovation"]},
        "history-of-google": {"cats": ["technology", "business"], "tags": ["google", "history", "search-engine", "ai", "android"]},
        "history-of-amazon": {"cats": ["technology", "business"], "tags": ["amazon", "history", "aws", "ecommerce", "jeff-bezos"]},
        "history-of-microsoft": {"cats": ["technology", "business"], "tags": ["microsoft", "history", "windows", "azure", "ai"]},
        "history-of-meta-facebook": {"cats": ["technology", "business"], "tags": ["meta", "facebook", "history", "metaverse", "sns"]}
    }

    count = 0
    for slug, meta in articles.items():
        for file in glob.glob(f"c:/work/kenji.blog/content/post/{slug}/*.md"):
            try:
                with open(file, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Extract frontmatter
                m = re.match(r"^---\n(.*?)\n---\n(.*)", content, re.DOTALL)
                if m:
                    fm_text = m.group(1)
                    body = m.group(2)
                    
                    try:
                        # Try to parse yaml
                        # Replace categories and tags
                        fm = yaml.safe_load(fm_text)
                        if fm is None:
                            continue
                        
                        fm["categories"] = meta["cats"]
                        fm["tags"] = meta["tags"]
                        
                        # ensure title/desc don`t have unescaped quotes causing invalid yaml if dumped incorrectly
                        # Instead of yaml.dump which can reformat strings weirdly, let`s just regex replace categories and tags blocks
                    except yaml.YAMLError:
                        pass
                    
                    # Regex replacement is safer to preserve the rest of the yaml untouched
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

