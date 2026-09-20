import os
import re

blog_dir = r'c:\work\kenji.blog\content\post'

link_dict = {}

manual_dict = {
    "フェルマー": "fermat",
    "Fermat": "fermat",
    "ロベルヴァル": "roberval",
    "Roberval": "roberval",
    "ウォリス": "wallis",
    "Wallis": "wallis",
    "ブランカー": "brouncker",
    "Brouncker": "brouncker",
    "パスカル": "pascal",
    "Pascal": "pascal",
    "ラグランジュ": "lagrange",
    "Lagrange": "lagrange",
    "ルジャンドル": "legendre",
    "Legendre": "legendre",
    "コーシー": "cauchy",
    "Cauchy": "cauchy",
    "ラメ": "lame",
    "Lamé": "lame",
    "アーベル": "abel",
    "Abel": "abel",
    "ヤコビ": "jacobi",
    "Jacobi": "jacobi",
    "リューヴィル": "liouville",
    "Liouville": "liouville",
    "クンマー": "kummer",
    "Kummer": "kummer",
    "ガロア": "galois",
    "Galois": "galois",
    "クロネッカー": "kronecker",
    "Kronecker": "kronecker",
    "リーマン": "riemann",
    "Riemann": "riemann",
    "ポアンカレ": "poincare",
    "Poincaré": "poincare",
    "Poincare": "poincare",
    "ヘンゼル": "hensel",
    "Hensel": "hensel",
    "ヒルベルト": "hilbert",
    "Hilbert": "hilbert",
    "高木貞治": "takagi-teiji",
    "Takagi": "takagi-teiji"
}

for k, v in manual_dict.items():
    link_dict[k] = v

sorted_keys = [k for k in link_dict.keys() if len(k) > 2 and not k.isdigit()]
sorted_keys = sorted(sorted_keys, key=len, reverse=True)

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
                for i in range(0, len(tokens)):
                    text = tokens[i]
                    if not text: continue
                    
                    if i % 2 == 0:
                        for kw in sorted_keys:
                            if kw in text:
                                slug = link_dict[kw]
                                link_str = f"[{kw}](https://kenji.blog{lang_prefix}/p/{slug}/)"
                                text = text.replace(kw, link_str)
                                changed = True
                        tokens[i] = text
                
                if changed:
                    new_body = "".join(tokens)
                    new_content = front_matter + new_body
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    count += 1
            except Exception:
                pass

print(f"Updated {count} markdown files.")
