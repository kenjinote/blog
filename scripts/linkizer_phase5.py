import os
import re

blog_dir = r'c:\work\kenji.blog\content\post'
targets = {
    'docker-container-namespace-cgroups-layers': [
        "Docker", "Namespace", "cgroups", "OverlayFS", "Container", "\u30b3\u30f3\u30c6\u30ca"
    ],
    'kubernetes-k8s-architecture-pod-service-ingress': [
        "Kubernetes", "K8s", "Pod", "Service", "Ingress", "Control Plane", "\u30b3\u30f3\u30c8\u30ed\u30fc\u30eb\u30d7\u30ec\u30fc\u30f3", "kube-apiserver"
    ],
    'serverless-architecture-aws-lambda-cold-start': [
        "Serverless", "\u30b5\u30fc\u30d0\u30fc\u30ec\u30b9", "AWS Lambda", "Lambda", "Cold Start", "\u30b3\u30fc\u30eb\u30c9\u30b9\u30bf\u30fc\u30c8", "Firecracker"
    ],
    'iac-infrastructure-as-code-terraform': [
        "IaC", "Infrastructure as Code", "Terraform", "HCL", "State"
    ],
    'cicd-pipeline-github-actions-best-practices': [
        "CI/CD", "GitHub Actions", "Workflow", "Pipeline", "\u30d1\u30a4\u30d7\u30e9\u30a4\u30f3"
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

print(f"Updated {count} markdown files for phase 5 links.")
