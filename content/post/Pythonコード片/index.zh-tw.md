---
title: "Python 程式碼片段"
slug: "Pythonコード片"
date: 2025-02-24T18:21:14+09:00
tags: ["Python", "範例程式碼"]
draft: false
image: "img.png"
categories: ["程式設計"]
---

介紹使用標準函式庫的範例程式碼。

# 下載並顯示圖片
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

    # 儲存至暫存檔案並顯示
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(img_data)
        print(f"file://{tmp.name}")
        webbrowser.open(f"file://{tmp.name}")
        time.sleep(3)
except Exception as e:
    print(f"發生錯誤： {e}")

finally:
    if 'tmp' in locals():
        os.unlink(tmp.name)  # 刪除暫存檔案
```
