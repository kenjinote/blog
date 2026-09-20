import os
import re

blog_dir = r'c:\work\kenji.blog\content\post'
targets = {
    'p-vs-np-problem': [
        "P vs NP", "P=NP", "NP-Complete", "NP-Completo", "NP-complet", 
        "P\u5bfeNP", "NP\u5b8c\u5168", "NP\u56f0\u96e3"
    ],
    'turing-machine-computability': [
        "Turing Machine", "Turing-Maschine", "Machine de Turing", "Maquina de Turing",
        "\u30c1\u30e5\u30fc\u30ea\u30f3\u30b0\u30de\u30b7\u30f3", "Halting Problem", "Halteproblem", "\u505c\u6b62\u6027\u554f\u984c"
    ],
    'quantum-computing-shors-algorithm': [
        "Quantum Computing", "Shor's Algorithm", "Shor-Algorithmus", "Algorithme de Shor",
        "Algoritmo de Shor", "\u91cf\u5b50\u30b3\u30f3\u30d4\u30e5\u30fc\u30bf", "\u30b7\u30e7\u30a2\u306e\u30a2\u30eb\u30b4\u30ea\u30ba\u30e0"
    ],
    'lambda-calculus-functional-programming': [
        "Lambda Calculus", "Lambda-Kalkul", "Calcul lambda", "Calculo lambda",
        "\u30e9\u30e0\u30c0\u8a08\u7b97", "Functional Programming", "\u95a2\u6570\u578b\u30d7\u30ed\u30b0\u30e9\u30df\u30f3\u30b0"
    ],
    'automata-formal-language-theory': [
        "Automata", "Finite State Machine", "Automaten", "Automate",
        "\u30aa\u30fc\u30c8\u30de\u30c8\u30f3", "Formal Language", "\u5f62\u5f0f\u8a00\u8a9e"
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
                print(f"Error processing {file_path}: {e}")

print(f"Updated {count} markdown files for phase 1 links.")
