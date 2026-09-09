---
title: '使用Python下载图片并临时保存、显示的示例代码'
slug: "Pythonコード片"
date: 2025-02-24T18:21:14+09:00
tags: ["Python", "示例代码"]
draft: false
image: "img.webp"
categories: ["编程"]
description: '介绍一套实用的示例代码：仅使用Python标准库，从网络图片URL下载数据并保存到临时文件，在浏览器中显示后自动删除。'
---

介绍使用标准库的示例代码。

# 下载并显示图片
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

    # 保存到临时文件并显示
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(img_data)
        print(f"file://{tmp.name}")
        webbrowser.open(f"file://{tmp.name}")
        time.sleep(3)
except Exception as e:
    print(f"发生错误: {e}")

finally:
    if 'tmp' in locals():
        os.unlink(tmp.name)  # 删除临时文件
```
