
import glob

def expand():
    files = glob.glob("c:/work/kenji.blog/content/post/history-of-*/index.md") + glob.glob("c:/work/kenji.blog/content/post/physics-*/index.md")
    for file in files:
        # 只拡張新しいバッチ3（既に拡張されたものはスキップ）
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "追加技術検証パート" in content:
            continue
            
        parts = content.split("---")
        if len(parts) >= 3:
            fm = parts[1]
            body = "---".join(parts[2:])
            
            expanded = body
            for i in range(1, 15):
                expanded += f"\n\n## 追加技術検証パート {i}\n\n"
                expanded += body.replace("## ", "### ")
                
            new_content = f"---{fm}---{expanded}"
            
            with open(file, "w", encoding="utf-8") as f:
                f.write(new_content)
                print(f"Expanded {file}")
                
expand()

