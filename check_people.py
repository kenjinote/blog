import re
import os
import glob

# 名言集ファイルのパス
post_dir = r"C:\work\kenji.blog\content\post"
quotes_file = os.path.join(post_dir, "名言集", "index.md")

people_in_quotes = set()
with open(quotes_file, "r", encoding="utf-8") as f:
    for line in f:
        # > 引用文 (人物名) のパターン
        # あるいは (人物名『作品名』) などのパターン
        line = line.strip()
        if line.startswith(">"):
            m = re.search(r"\(([^)]+)\)$", line)
            if m:
                person_info = m.group(1).split("『")[0].strip()
                # " 等" などの不要な部分を削除
                person_info = person_info.replace(" 等", "").strip()
                people_in_quotes.add(person_info)

# 記事のタイトルやフォルダ名を収集
existing_topics = set()
for dir_path in glob.glob(os.path.join(post_dir, "*")):
    if os.path.isdir(dir_path):
        dir_name = os.path.basename(dir_path)
        existing_topics.add(dir_name.lower())
        
        # 念のため index.md の title もチェック
        index_file = os.path.join(dir_path, "index.md")
        if os.path.exists(index_file):
            with open(index_file, "r", encoding="utf-8") as f:
                content = f.read()
                m = re.search(r"^title:\s*['\"]?(.*?)['\"]?$", content, re.MULTILINE)
                if m:
                    existing_topics.add(m.group(1).lower())

print("--- 人物リスト ---")
not_written = []
for person in sorted(people_in_quotes):
    # 人物名がタイトルやフォルダ名に含まれているかざっくりチェック
    # (例: "アインシュタイン" が "アインシュタインの名言" に含まれるか)
    found = False
    for topic in existing_topics:
        if person.lower() in topic or person.replace("・", "").lower() in topic.replace("・", ""):
            found = True
            break
            
    # さらに、英語名での記事もあるかもしれないので、簡単なマッピングがあれば。
    # 例えば「プラトン」->「plato」、「ソクラテス」->「socrates」、「アリストテレス」->「aristotle」
    
    if not found:
        not_written.append(person)

for p in not_written:
    print(p)

