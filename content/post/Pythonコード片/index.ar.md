---
title: "تنزيل صورة وحفظها مؤقتاً وفتحها باستخدام Python"
slug: "Pythonコード片"
tags: ["Python", "نموذج كود"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "تحقق من PNG باستخدام مكتبة Python القياسية، وافتح نسخة مؤقتة في متصفح سطح المكتب ثم احذفها بعد المشاهدة."
date: "2025-02-24T18:21:14+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

يستخدم هذا المثال مكتبة Python القياسية فقط لتنزيل صورة من الويب وحفظها مؤقتاً وفتحها في متصفح سطح مكتب محلي. يستخدم شعار PNG مستضافاً على Python.org. عند تغيير URL، اختر صورة HTTPS موثوقة ومسموحاً لك بالوصول إليها.

## بيئة التشغيل

هذا الرمز مخصص لجلسة Python تفاعلية على كمبيوتر محلي. في دفتر بعيد مثل Colab، قد لا يتمكن المتصفح المحلي من الوصول مباشرة إلى ملف مؤقت في بيئة التشغيل.

## تنزيل الصورة وفتحها

يحدد الرمز مهلة شبكة قدرها 15 ثانية، ويتحقق من Content-Type وتوقيع PNG، ويحد التنزيل إلى 2 MiB. إذا بدأ المتصفح، فأغلق الصورة وعد إلى الطرفية واضغط Enter لحذف الملف المؤقت.

```python
from pathlib import Path
import tempfile
import urllib.request
import webbrowser

image_url = "https://www.python.org/static/community_logos/python-logo.png"
max_bytes = 2 * 1024 * 1024
temp_path = None

try:
    request = urllib.request.Request(image_url, headers={"User-Agent": "Python image example"})
    with urllib.request.urlopen(request, timeout=15) as response:
        if response.status != 200:
            raise RuntimeError(f"Unexpected HTTP status: {response.status}")
        if response.headers.get_content_type() != "image/png":
            raise ValueError("The response is not a PNG image")
        image_data = response.read(max_bytes + 1)

    if len(image_data) > max_bytes:
        raise ValueError("The image exceeds the 2 MiB limit")
    if not image_data.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("The response does not have a PNG signature")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        temp_path = Path(temp_file.name)
        temp_file.write(image_data)

    print(temp_path.as_uri())
    if webbrowser.open(temp_path.as_uri(), new=2):
        input()
    else:
        raise RuntimeError("Could not launch a browser")
finally:
    if temp_path is not None and temp_path.exists():
        temp_path.unlink()
```

## الحدود والتنبيهات

استخدم URL صورة موثوقاً وتأكد من امتلاك حقوق الاستخدام اللازمة. يقبل المثال PNG فقط ويرفض الملفات الأكبر من 2 MiB. يعتمد تشغيل المتصفح على نظام التشغيل وبيئة التنفيذ.

## مراجع رسمية

- [Python: urllib.request](https://docs.python.org/3/library/urllib.request.html)
- [Python: tempfile](https://docs.python.org/3/library/tempfile.html)
- [Python: webbrowser](https://docs.python.org/3/library/webbrowser.html)
- [Python Software Foundation: Python logos](https://www.python.org/community/logos/)
