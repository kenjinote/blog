import os
import yaml

i18n_path = r"c:\work\kenji.blog\i18n\ja.yaml"
try:
    with open(i18n_path, 'r', encoding='utf-8') as f:
        print("--- i18n/ja.yaml ---")
        lines = f.readlines()
        print("".join(lines[:30]))
except Exception as e:
    print(e)

cat_path = r"c:\work\kenji.blog\content\categories"
if os.path.exists(cat_path):
    print("\n--- content/categories ---")
    for root, dirs, files in os.walk(cat_path):
        for d in dirs:
            print(os.path.join(root, d))
else:
    print("\nNo content/categories directory.")

