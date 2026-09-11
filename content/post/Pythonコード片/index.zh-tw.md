---
title: '使用 Python 下載圖片並暫存、顯示的範例程式碼'
slug: "Pythonコード片"
date: 2025-02-24T18:21:14+09:00
tags: ["Python", "範例程式碼"]
draft: false
image: "img.webp"
categories: ["程式設計"]
description: '介紹僅使用 Python 標準函式庫，從網頁上的圖片 URL 下載資料並儲存至暫存檔，在瀏覽器顯示後自動刪除的一系列實用範例程式碼。'
---

介紹使用標準函式庫的範例程式碼。

# 下載並顯示圖片
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
