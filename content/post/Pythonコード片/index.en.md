---
title: 'Sample Code to Download, Temporarily Save, and Display an Image in Python'
slug: "Pythonコード片"
date: 2025-02-24T18:21:14+09:00
tags: ["Python", "Sample Code"]
draft: false
image: "img.webp"
categories: ["Programming"]
description: 'Introduces a series of practical sample codes using only Python''s standard libraries to download data from an image URL on the web, save it to a temporary file, display it in a browser, and then automatically delete it.'
---

Introduction of sample code using standard libraries.

# Download and display an image
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

    # Save to a temporary file and display
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(img_data)
        print(f"file://{tmp.name}")
        webbrowser.open(f"file://{tmp.name}")
        time.sleep(3)
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'tmp' in locals():
        os.unlink(tmp.name)  # Delete temporary file
```
