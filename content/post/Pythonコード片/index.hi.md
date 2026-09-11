---
title: 'Python में छवियों को डाउनलोड करने, अस्थायी रूप से सहेजने और प्रदर्शित करने के लिए नमूना कोड'
slug: "Pythonコード片"
date: 2025-02-24T18:21:14+09:00
tags: ["Python", "नमूना कोड"]
draft: false
image: "img.webp"
categories: ["प्रोग्रामिंग"]
description: 'हम केवल Python की मानक लाइब्रेरी का उपयोग करके वेब पर छवि URL से डेटा डाउनलोड करने, इसे एक अस्थायी फ़ाइल में सहेजने, इसे ब्राउज़र में प्रदर्शित करने और फिर इसे स्वचालित रूप से हटाने के लिए व्यावहारिक नमूना कोड की एक श्रृंखला प्रस्तुत करते हैं।'
---

मानक लाइब्रेरी का उपयोग करके नमूना कोड का परिचय।

# एक छवि डाउनलोड करें और प्रदर्शित करें
```python
import urllib.request
import tempfile
import os
import webbrowser
import time

url = "https://www.aomori-ringo.or.jp/kids/wp-content/uploads/2021/11/apple.webp"

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
