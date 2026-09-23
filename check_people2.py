import re
import os
import glob

post_dir = r"C:\work\kenji.blog\content\post"
quotes_file = os.path.join(post_dir, "名言集", "index.md")

# 名言集に登場する人物を抽出
people = set()
with open(quotes_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            m = re.search(r"\(([^)]+)\)$", line)
            if m:
                person = m.group(1).split("『")[0].strip().replace(" 等", "")
                people.add(person)
                
# 全記事のタイトルを抽出
existing_titles = []
for dir_path in glob.glob(os.path.join(post_dir, "*")):
    if os.path.isdir(dir_path):
        index_file = os.path.join(dir_path, "index.md")
        if os.path.exists(index_file):
            with open(index_file, "r", encoding="utf-8") as f:
                content = f.read()
                m = re.search(r"^title:\s*['\"]?(.*?)['\"]?$", content, re.MULTILINE)
                if m:
                    existing_titles.append(m.group(1))

# 人物名（フルネーム、またはスペースや「・」で区切られた最後の単語＝名字）でマッチング
not_written = []
for person in sorted(people):
    # 名前のパーツに分割
    parts = re.split(r"[\s・＝=]", person)
    last_name = parts[-1]
    
    found = False
    for title in existing_titles:
        # フルネームまたは名字がタイトルに含まれていれば、記事化されているとみなす
        if person in title or last_name in title:
            found = True
            break
            
    if not found:
        not_written.append(person)

print("--- 記事化されていない可能性のある人物 ---")
for p in not_written:
    print(p)
