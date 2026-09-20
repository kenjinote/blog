import os

base_dir = r"c:\work\kenji.blog\content\categories"
categories_to_translate = {
    "biography": {
        "": "人物伝",
        "ja": "人物伝",
        "ar": "سيرة شخصية",
        "de": "Biografie",
        "en": "Biography",
        "es": "Biografía",
        "fr": "Biographie",
        "hi": "जीवनी",
        "id": "Biografi",
        "ko": "전기",
        "pt": "Biografia",
        "ru": "Биография",
        "zh-cn": "传记",
        "zh-tw": "傳記"
    },
    "mathematics": {
        "": "数学",
        "ja": "数学",
        "ar": "رياضيات",
        "de": "Mathematik",
        "en": "Mathematics",
        "es": "Matemáticas",
        "fr": "Mathématiques",
        "hi": "गणित",
        "id": "Matematika",
        "ko": "수학",
        "pt": "Matemática",
        "ru": "Математика",
        "zh-cn": "数学",
        "zh-tw": "數學"
    }
}

for cat, langs in categories_to_translate.items():
    cat_dir = os.path.join(base_dir, cat)
    os.makedirs(cat_dir, exist_ok=True)
    
    for lang, title in langs.items():
        if lang == "" or lang == "ja":
            # Default or explicit Japanese
            # Usually _index.md is default/Japanese in this setup
            filename = "_index.md" if lang == "" else f"_index.{lang}.md"
        else:
            filename = f"_index.{lang}.md"
            
        filepath = os.path.join(cat_dir, filename)
        content = f"---\ntitle: \"{title}\"\n---\n"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
print("Taxonomy _index files created.")
