
import glob
import re

articles = {
    "game-othello-rules": {"cats": ["entertainment", "game"], "tags": ["othello", "strategy", "board-game", "theory"]},
    "game-chess-rules": {"cats": ["entertainment", "game"], "tags": ["chess", "strategy", "board-game", "theory"]},
    "game-poker-rules": {"cats": ["entertainment", "game"], "tags": ["poker", "strategy", "math", "probability"]},
    "game-mahjong-rules": {"cats": ["entertainment", "game"], "tags": ["mahjong", "strategy", "board-game"]},
    "game-rubiks-cube": {"cats": ["entertainment", "game"], "tags": ["puzzle", "rubiks-cube", "algorithm", "math"]},
    "history-of-iphone": {"cats": ["technology", "history"], "tags": ["apple", "iphone", "smartphone", "mobile"]}
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

