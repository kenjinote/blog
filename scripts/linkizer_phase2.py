import os
import re

blog_dir = r'c:\work\kenji.blog\content\post'
targets = {
    'b-tree-database-index-theory': [
        "B-Tree", "B\u6728", "B+\u6728", "Database Index", "\u30c7\u30fc\u30bf\u30d9\u30fc\u30b9\u30a4\u30f3\u30c7\u30c3\u30af\u30b9",
        "Arbol B"
    ],
    'graph-theory-dijkstra-a-star': [
        "Graph Theory", "\u30b0\u30e9\u30d5\u7406\u8ad6", "Dijkstra", "\u30c0\u30a4\u30af\u30b9\u30c8\u30e9\u6cd5",
        "A* Algorithm", "A*\u30a2\u30eb\u30b4\u30ea\u30ba\u30e0", "Pathfinding", "\u7d4c\u8def\u63a2\u7d22"
    ],
    'cap-theorem-distributed-systems': [
        "CAP Theorem", "CAP\u5b9a\u7406", "Distributed System", "\u5206\u6563\u30b7\u30b9\u30c6\u30e0",
        "Partition Tolerance", "\u5206\u6563\u30c7\u30fc\u30bf\u30d9\u30fc\u30b9"
    ],
    'byzantine-generals-problem-consensus': [
        "Byzantine Generals", "\u30d3\u30b6\u30f3\u30c1\u30f3\u5c06\u8ecd", "Consensus Algorithm", "\u30b3\u30f3\u30bb\u30f3\u30b5\u30b9\u30a2\u30eb\u30b4\u30ea\u30ba\u30e0",
        "Paxos", "Raft"
    ],
    'information-theory-shannon-entropy': [
        "Information Theory", "\u60c5\u5831\u7406\u8ad6", "Shannon Entropy", "\u30b7\u30e3\u30ce\u30f3\u30a8\u30f3\u30c8\u30ed\u30d4\u30fc",
        "Data Compression", "\u30c7\u30fc\u30bf\u5727\u7e2e"
    ]
}

split_pattern = re.compile(r'(!?\[[^\]]*\]\([^\)]+\)|```.*?```|`[^`]+`)', re.DOTALL)

count = 0
for root, dirs, files in os.walk(blog_dir):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            
            # Determine lang prefix
            lang_prefix = ""
            parts_file = file.split('.')
            if len(parts_file) == 3 and parts_file[2] == 'md':
                lang_prefix = "/" + parts_file[1]
                
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    front_matter = '---' + parts[1] + '---'
                    body = parts[2]
                else:
                    front_matter = ''
                    body = content
                
                tokens = split_pattern.split(body)
                changed = False
                
                for target_slug, keywords in targets.items():
                    # Skip self linking
                    if target_slug in root:
                        continue
                        
                    for i in range(0, len(tokens)):
                        text = tokens[i]
                        if not text: continue
                        
                        if i % 2 == 0:
                            for kw in keywords:
                                if kw in text:
                                    if kw.isalpha() and len(kw) <= 5:
                                        pattern = r'(?<![a-zA-Z])' + re.escape(kw) + r'(?![a-zA-Z])'
                                        if re.search(pattern, text):
                                            link_str = f"[{kw}](https://kenji.blog{lang_prefix}/p/{target_slug}/)"
                                            text = re.sub(pattern, link_str, text, count=1)
                                            changed = True
                                    else:
                                        link_str = f"[{kw}](https://kenji.blog{lang_prefix}/p/{target_slug}/)"
                                        text = text.replace(kw, link_str, 1)
                                        changed = True
                            tokens[i] = text
                
                if changed:
                    new_body = "".join(tokens)
                    new_content = front_matter + new_body
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    count += 1
            except Exception as e:
                pass

print(f"Updated {count} markdown files for phase 2 links.")
