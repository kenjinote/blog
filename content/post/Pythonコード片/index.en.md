---
title: 'Python Code Snippets'
date: 2025-02-24T18:21:14+09:00
tags: ["Python", "Sample Code"]
draft: false
image: "img.png"
categories: ["Programming"]
---

Introduction of sample code using standard libraries.

# Download and display an image
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
