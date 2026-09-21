import os
import re

blog_dir = r'c:\work\kenji.blog\content\post'
targets = {
    'modern-cryptography-public-key-hash-signature': [
        "Cryptography", "Public Key", "Hash Function", "Digital Signature", "RSA", "\u6697\u53f7\u5316", "\u516c\u958b\u9375", "\u96fb\u5b50\u7f72\u540d"
    ],
    'oauth2-oidc-authentication-authorization-difference': [
        "OAuth 2.0", "OAuth", "OIDC", "OpenID Connect", "Authentication", "Authorization", "\u8a8d\u8a3c", "\u8a8d\u53ef", "JWT"
    ],
    'zero-trust-network-architecture-beyond-corp': [
        "Zero Trust", "\u30bc\u30ed\u30c8\u30e9\u30b9\u30c8", "BeyondCorp", "Access Proxy", "Microsegmentation"
    ],
    'web-application-vulnerability-owasp-top-10': [
        "Vulnerability", "\u8106\u5f31\u6027", "OWASP", "XSS", "CSRF", "SQL Injection", "SQL\u30a4\u30f3\u30b8\u30a7\u30af\u30b7\u30e7\u30f3"
    ],
    'blockchain-technology-smart-contract-distributed-ledger': [
        "Blockchain", "\u30d6\u30ed\u30c3\u30af\u30c1\u30a7\u30fc\u30f3", "Smart Contract", "\u30b9\u30de\u30fc\u30c8\u30b3\u30f3\u30c8\u30e9\u30af\u30c8", "Distributed Ledger", "PoW", "PoS", "Consensus"
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

print(f"Updated {count} markdown files for phase 6 links.")
