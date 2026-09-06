---
title: "مقتطفات كود بايثون"
slug: "Pythonコード片"
date: 2025-02-24T18:21:14+09:00
tags: ["Python", "نموذج كود"]
draft: false
image: "img.png"
categories: ["برمجة"]
---

مقدمة لنموذج كود باستخدام المكتبة القياسية.

# تنزيل وعرض صورة
```python
import urllib.request
import tempfile
import os
import webbrowser
import time

url = "https://www.aomori-ringo.or.jp/kids/wp-content/uploads/2021/11/apple.png"

try:
    with urllib.request.urlopen(url) as response:
        img_data = response.read()

    # حفظ في ملف مؤقت وعرضه
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(img_data)
        print(f"file://{tmp.name}")
        webbrowser.open(f"file://{tmp.name}")
        time.sleep(3)
except Exception as e:
    print(f"حدث خطأ: {e}")

finally:
    if 'tmp' in locals():
        os.unlink(tmp.name)  # حذف الملف المؤقت
```
