---
title: 'Pythonで画像をダウンロードして一時保存・表示するサンプルコード'
slug: "Pythonコード片"
date: 2025-02-24T18:21:14+09:00
tags: ["Python", "サンプルコード"]
draft: false
image: "img.webp"
categories: ["プログラミング"]
description: 'Pythonの標準ライブラリのみを使用し、Web上の画像URLからデータをダウンロードして一時ファイルに保存、ブラウザで表示した後に自動削除する一連の実用的なサンプルコードを紹介します。'
---

標準ライブラリを使ったサンプルコードの紹介です。

# 画像をダウンロードして表示する
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

    # 一時ファイルに保存して表示
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(img_data)
        print(f"file://{tmp.name}")
        webbrowser.open(f"file://{tmp.name}")
        time.sleep(3)
except Exception as e:
    print(f"エラーが発生しました: {e}")

finally:
    if 'tmp' in locals():
        os.unlink(tmp.name)  # 一時ファイル削除
```
