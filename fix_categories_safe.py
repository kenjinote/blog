import os
import re

dir_path = r"c:\work\kenji.blog\content\post"

lang_dict = {
    "": {"biography": "人物伝", "mathematics": "数学"},
    "ja": {"biography": "人物伝", "mathematics": "数学"},
    "ar": {"biography": "سيرة شخصية", "mathematics": "رياضيات"},
    "de": {"biography": "Biografie", "mathematics": "Mathematik"},
    "en": {"biography": "Biography", "mathematics": "Mathematics"},
    "es": {"biography": "Biografía", "mathematics": "Matemáticas"},
    "fr": {"biography": "Biographie", "mathematics": "Mathématiques"},
    "hi": {"biography": "जीवनी", "mathematics": "गणित"},
    "id": {"biography": "Biografi", "mathematics": "Matematika"},
    "ko": {"biography": "전기", "mathematics": "수학"},
    "pt": {"biography": "Biografia", "mathematics": "Matemática"},
    "ru": {"biography": "Биография", "mathematics": "Математика"},
    "zh-cn": {"biography": "传记", "mathematics": "数学"},
    "zh-tw": {"biography": "傳記", "mathematics": "數學"},
}

count = 0
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.md'):
            parts = file.split('.')
            if len(parts) == 3 and parts[2] == 'md':
                lang = parts[1]
            else:
                lang = ""

            if lang not in lang_dict:
                lang = ""
            
            replacements = lang_dict[lang]
            
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                parts_content = content.split('---', 2)
                if len(parts_content) >= 3:
                    fm = parts_content[1]
                    
                    changed = False
                    new_fm_lines = []
                    
                    for line in fm.splitlines():
                        if re.match(r'^(categories|tags):', line.strip()) or re.match(r'^\s*-\s+', line):
                            new_line = line
                            for eng, localized in replacements.items():
                                pattern = re.compile(r'\b' + eng + r'\b', re.IGNORECASE)
                                new_line = pattern.sub(localized, new_line)
                            
                            if new_line != line:
                                changed = True
                            new_fm_lines.append(new_line)
                        else:
                            new_fm_lines.append(line)
                            
                    if changed:
                        # parts_content[1] actually doesn't include the '---'
                        # but parts_content[0] is usually empty string or newline
                        # to safely reconstruct, we can just replace the fm part
                        new_fm = '\n'.join(new_fm_lines)
                        new_content = parts_content[0] + '---' + new_fm + '\n---' + parts_content[2]
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        count += 1

            except Exception as e:
                print(f"Error in {file_path}: {e}")

print(f"Updated categories safely in {count} files.")
