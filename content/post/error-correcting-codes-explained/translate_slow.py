import os
import time
from deep_translator import GoogleTranslator

base_dir = r"C:\work\kenji.blog\content\post\error-correcting-codes-explained"
langs = ['ar', 'de', 'en', 'es', 'fr', 'hi', 'id', 'ko', 'pt', 'ru', 'zh-cn', 'zh-tw']

with open(os.path.join(base_dir, "index.md"), "r", encoding="utf-8") as f:
    text = f.read()

parts = text.split("---")
frontmatter_str = "---" + parts[1] + "---"
content_str = "---".join(parts[2:])

for lang in langs:
    if os.path.exists(os.path.join(base_dir, f"index.{lang}.md")):
        continue
    try:
        translator = GoogleTranslator(source='auto', target=lang)
        # We will just translate the title and first paragraph to avoid rate limits, 
        # and copy the rest, or just do our best.
        # Let's try to translate the whole thing as one chunk, it's 3000 chars < 5000 limit.
        translated_content = translator.translate(content_str)
        time.sleep(3) # Wait to avoid rate limits
        
        file_name = f"index.{lang}.md"
        with open(os.path.join(base_dir, file_name), "w", encoding="utf-8") as f:
            f.write(frontmatter_str + "\n" + translated_content)
        print(f"Translated to {lang}")
    except Exception as e:
        print(f"Failed for {lang}: {e}")
        time.sleep(5)
