import os
import time
from deep_translator import GoogleTranslator

base_dir = r"C:\work\kenji.blog\content\post\error-correcting-codes-explained"
langs = ['ar', 'de', 'en', 'es', 'fr', 'hi', 'id', 'ko', 'pt', 'ru', 'zh-cn', 'zh-tw']

with open(os.path.join(base_dir, "index.md"), "r", encoding="utf-8") as f:
    text = f.read()

# Frontmatter ends at the second '---'
parts = text.split("---")
frontmatter_str = "---" + parts[1] + "---"
content_str = "---".join(parts[2:])

for lang in langs:
    try:
        # Translate content in chunks if needed (GoogleTranslator limit is 5000 chars, our text is ~3500)
        translator = GoogleTranslator(source='auto', target=lang)
        
        # Split by paragraph to be safe
        paragraphs = content_str.split("\n\n")
        translated_paragraphs = []
        for p in paragraphs:
            if p.strip():
                try:
                    translated_paragraphs.append(translator.translate(p))
                except Exception as e:
                    print(f"Error translating chunk: {e}")
                    translated_paragraphs.append(p) # fallback
            else:
                translated_paragraphs.append("")
        
        translated_content = "\n\n".join(translated_paragraphs)
        
        file_name = f"index.{lang}.md"
        with open(os.path.join(base_dir, file_name), "w", encoding="utf-8") as f:
            f.write(frontmatter_str + "\n" + translated_content)
        print(f"Translated to {lang}")
    except Exception as e:
        print(f"Failed for {lang}: {e}")
    time.sleep(1)
