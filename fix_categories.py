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
            # Determine language
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
                    
                    # Regex to find categories: [...] or categories: \n - ...
                    # A simpler approach is just to replace the specific words inside the front matter block.
                    # We only replace if they are bounded by quotes or brackets or spaces.
                    # e.g., "biography" or "Biography"
                    for eng, localized in replacements.items():
                        # replace case-insensitive, but only whole words
                        pattern = re.compile(r'\b' + eng + r'\b', re.IGNORECASE)
                        new_fm = pattern.sub(localized, fm)
                        if new_fm != fm:
                            fm = new_fm
                            changed = True
                    
                    if changed:
                        new_content = '---' + fm + '---' + parts_content[2]
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        count += 1

            except Exception as e:
                print(f"Error in {file_path}: {e}")

print(f"Updated categories in {count} files.")
