import os
import re

blog_dir = r'c:\work\kenji.blog\content\post'
targets = {
    'programming-languages-history-paradigm-evolution': [
        "プログラミング言語", "アセンブリ", "Java", "Rust", "Go", "Programming Language"
    ],
    'c-language-pointers-memory-management-stack-heap': [
        "ポインタ", "メモリ管理", "アドレス", "ヒープ", "スタック", "C言語", "Pointer", "Memory Management", "Stack", "Heap"
    ],
    'object-oriented-programming-oop-solid-principles': [
        "オブジェクト指向", "OOP", "SOLID原則", "デザインパターン", "Object-Oriented", "SOLID Principles"
    ],
    'functional-programming-concepts-pure-functions-monads': [
        "関数型プログラミング", "純粋関数", "不変性", "モナド", "Functional Programming", "Monad"
    ],
    'large-language-models-llm-transformer-prompt-engineering': [
        "大規模言語モデル", "LLM", "Transformer", "プロンプトエンジニアリング", "Prompt Engineering", "Large Language Models"
    ]
}

split_pattern = re.compile(r'(!?\[[^\]]*\]\([^\)]+\)|```.*?```|`[^`]+`)', re.DOTALL)

count = 0
for root, dirs, files in os.walk(blog_dir):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            
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

print(f"Updated {count} markdown files for phase 8 links.")
