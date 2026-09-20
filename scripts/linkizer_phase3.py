import os
import re

blog_dir = r'c:\work\kenji.blog\content\post'
targets = {
    'oop-vs-fp-vs-dop': [
        "Object-Oriented", "\u30aa\u30d6\u30b8\u30a7\u30af\u30c8\u6307\u5411", "Functional Programming", "\u95a2\u6570\u578b\u30d7\u30ed\u30b0\u30e9\u30df\u30f3\u30b0",
        "Data-Oriented", "\u30c7\u30fc\u30bf\u6307\u5411"
    ],
    'state-management-history-future': [
        "State Management", "\u72b6\u614b\u7ba1\u7406", "Redux", "Signals", "Reactivity", "\u30ea\u30a2\u30af\u30c6\u30a3\u30d3\u30c6\u30a3"
    ],
    'memory-management-garbage-collection': [
        "Memory Management", "\u30e1\u30e2\u30ea\u7ba1\u7406", "Garbage Collection", "\u30ac\u30d9\u30fc\u30b8\u30b3\u30ec\u30af\u30b7\u30e7\u30f3",
        "Borrow Checker", "\u501f\u7528\u30c1\u30a7\u30c3\u30ab\u30fc"
    ],
    'design-patterns-modern-practices': [
        "Design Patterns", "\u30c7\u30b6\u30a4\u30f3\u30d1\u30bf\u30fc\u30f3", "GoF", "Dependency Injection", "DI\u30b3\u30f3\u30c6\u30ca"
    ],
    'event-driven-architecture-async': [
        "Event-Driven", "\u30a4\u30d9\u30f3\u30c8\u99c6\u52d5", "Asynchronous", "\u975e\u540c\u671f\u51e6\u7406",
        "Event Loop", "\u30a4\u30d9\u30f3\u30c8\u30eb\u30fc\u30d7", "Actor Model", "\u30a2\u30af\u30bf\u30fc\u30e2\u30c7\u30eb", "CQRS"
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

print(f"Updated {count} markdown files for phase 3 links.")
