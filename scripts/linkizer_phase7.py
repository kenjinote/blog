import os
import re

blog_dir = r'c:\work\kenji.blog\content\post'
targets = {
    'pwa-progressive-web-apps-service-worker': [
        "PWA", "Progressive Web App", "Service Worker", "offline", "\u30aa\u30d5\u30e9\u30a4\u30f3", "manifest.json", "Push Notification"
    ],
    'web-vitals-frontend-performance-optimization-lcp-fid-cls': [
        "Web Vitals", "Core Web Vitals", "LCP", "FID", "CLS", "INP", "\u30d1\u30d5\u30a9\u30fc\u30de\u30f3\u30b9\u6700\u9069\u5316", "Performance Optimization"
    ],
    'state-management-history-redux-context-recoil-zustand': [
        "State Management", "\u72b6\u614b\u7ba1\u7406", "Redux", "Recoil", "Zustand", "Context API", "Flux", "Jotai"
    ],
    'graphql-vs-rest-api-overfetching-type-safety': [
        "GraphQL", "REST API", "overfetching", "underfetching", "DataLoader", "Apollo Client", "GraphQL Code Generator"
    ],
    'micro-frontends-architecture-spa-division': [
        "Micro Frontends", "Micro Frontend", "\u30de\u30a4\u30af\u30ed\u30d5\u30ed\u30f3\u30c8\u30a8\u30f3\u30c9", "Module Federation", "Webpack 5", "SPA\u5206\u5272"
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

print(f"Updated {count} markdown files for phase 7 links.")
