
import os
import glob
import re

posts_dir = "c:/work/kenji.blog/content/post"
bad_dirs = [
    "ai-chess", "ai-othello", "ai-shogi",
    "dynamic-programming-dp-introduction-knapsack-fibonacci",
    "eulers-identity", "event-driven-architecture-message-queue-kafka-rabbitmq",
    "four-color-theorem", "history-of-alibaba", "history-of-amazon",
    "history-of-amd", "history-of-apple", "history-of-bytedance",
    "history-of-google", "history-of-ibm", "history-of-intel",
    "history-of-linux", "history-of-macos", "history-of-meta-facebook",
    "history-of-microsoft", "history-of-nec", "history-of-nvidia",
    "history-of-panasonic", "history-of-salesforce", "history-of-tcpip",
    "history-of-unix", "history-of-windows", "physics-doppler-effect",
    "physics-electromagnetic-induction", "physics-gps", "physics-laser",
    "physics-led-mechanism", "physics-quantum-mechanics", "physics-relativity",
    "physics-superconductivity", "tech-3d-engine",
    "time-space-complexity-big-o-notation-examples",
    "tree-graph-data-structures-search-dfs-bfs-dijkstra"
]

fixed_count = 0

for d in bad_dirs:
    dir_path = os.path.join(posts_dir, d)
    for md_file in glob.glob(os.path.join(dir_path, "index*.md")):
        try:
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()
                
            # 見出しで分割
            sections = re.split(r"(?m)^(##+\s+.*)$", content)
            
            # sections[0] はフロントマターと序文
            # 以降は [見出し, 本文, 見出し, 本文...]
            
            new_sections = [sections[0]]
            seen_texts = set()
            
            i = 1
            while i < len(sections):
                heading = sections[i]
                text = sections[i+1] if i+1 < len(sections) else ""
                
                # 本文の正規化（空白除去）して重複判定
                norm_text = re.sub(r"\s+", "", text)
                
                # 見出し自体に "パート", "Part" が含まれていて、かつ本文が使い回されているようなら削除
                # または、すでに見た本文（長さ50以上）なら削除
                if len(norm_text) > 50 and norm_text in seen_texts:
                    pass # skip
                elif re.search(r"(?i)part\s*\d+|パート\s*\d+", heading):
                    # Part X という見出しはそもそもスパム生成の産物なので飛ばす
                    pass
                else:
                    new_sections.append(heading)
                    new_sections.append(text)
                    if len(norm_text) > 50:
                        seen_texts.add(norm_text)
                        
                i += 2
                
            new_content = "".join(new_sections)
            
            if new_content != content:
                with open(md_file, "w", encoding="utf-8") as f:
                    f.write(new_content)
                fixed_count += 1
                
        except Exception as e:
            print(f"Error processing {md_file}: {e}")

print(f"Fixed {fixed_count} files by removing duplicated spam sections.")

