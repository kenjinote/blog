---
title: "Pythonで画像をダウンロードして一時保存し、表示する"
slug: "Pythonコード片"
tags: ["Python", "サンプルコード"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Python標準ライブラリでPNG画像を安全に取得し、一時ファイルをデスクトップのブラウザーで開いて、閲覧後に削除する例です。"
date: "2025-02-24T18:21:14+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Python標準ライブラリだけで、Web上の画像を取得して一時ファイルに保存し、ローカルのデスクトップブラウザーで開く例です。サンプルはPython.orgのPNGロゴを使います。URLを置き換える場合は、アクセス権のある信頼できるHTTPS画像を指定してください。

## 実行環境

このコードはローカルPCの対話型Python環境を想定しています。Colabなどのリモートノートブックでは、ランタイム側の一時ファイルを手元のブラウザーから直接開けないことがあります。

## ダウンロードして開く

次のコードは応答を15秒でタイムアウトし、PNGのContent-Typeとファイル署名を確認します。読み込みは2 MiBに制限します。ブラウザー起動に成功した場合、画像を閉じてターミナルに戻り、Enterを押すと一時ファイルを削除します。

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

## 制限と注意点

URL先の応答は信頼できるものに限り、画像URLと用途に必要な権利を確認してください。コードはPNGだけを受け付け、サイズが2 MiBを超える画像を拒否します。ブラウザー起動はOSや実行環境に依存します。

## 公式資料

- [Python: urllib.request](https://docs.python.org/3/library/urllib.request.html)
- [Python: tempfile](https://docs.python.org/3/library/tempfile.html)
- [Python: webbrowser](https://docs.python.org/3/library/webbrowser.html)
- [Python Software Foundation: Python logos](https://www.python.org/community/logos/)
