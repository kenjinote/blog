
import os
import glob
import re

posts_dir = "c:/work/kenji.blog/content/post"
bad_dirs = []

for index_file in glob.glob(os.path.join(posts_dir, "*/index.md")):
    try:
        with open(index_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        # 見出し(##など)で分割
        sections = re.split(r"(?m)^##+\s+.*$", content)
        
        # 最初の要素(フロントマターと序文)を除外
        sections = sections[1:]
        
        # 本文部分を正規化（空白除去）して比較
        norm_sections = [re.sub(r"\s+", "", s) for s in sections]
        
        # 重複をカウント
        duplicates = False
        for i, s1 in enumerate(norm_sections):
            if len(s1) < 50: # 短すぎるものは無視
                continue
            count = 0
            for j, s2 in enumerate(norm_sections):
                if s1 == s2:
                    count += 1
            if count >= 3: # 完全に同じセクションが3回以上出現したらスパム
                duplicates = True
                break
                
        if duplicates:
            bad_dirs.append(os.path.basename(os.path.dirname(index_file)))
            
    except Exception as e:
        pass

print("Spam directories:")
for d in bad_dirs:
    print(d)

