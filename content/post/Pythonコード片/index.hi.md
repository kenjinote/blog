---
title: "पायथन कोड स्निपेट्स"
slug: "Pythonコード片"
date: 2025-02-24T18:21:14+09:00
tags: ["Python", "नमूना कोड"]
draft: false
image: "img.png"
categories: ["प्रोग्रामिंग"]
---

मानक लाइब्रेरी का उपयोग करके नमूना कोड का परिचय।

# एक छवि डाउनलोड करें और प्रदर्शित करें
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

    # एक अस्थायी फ़ाइल में सहेजें और प्रदर्शित करें
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(img_data)
        print(f"file://{tmp.name}")
        webbrowser.open(f"file://{tmp.name}")
        time.sleep(3)
except Exception as e:
    print(f"एक त्रुटि उत्पन्न हुई: {e}")

finally:
    if 'tmp' in locals():
        os.unlink(tmp.name)  # अस्थायी फ़ाइल हटाएँ
```
