---
title: "使用 Python 下載、暫存並開啟圖片"
slug: "Pythonコード片"
tags: ["Python", "範例程式碼"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "使用 Python 標準程式庫驗證 PNG，在桌面瀏覽器開啟暫存副本，並於檢視後刪除。"
date: "2025-02-24T18:21:14+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

本範例只使用 Python 標準程式庫下載網路圖片、暫存並在本機桌面瀏覽器開啟。範例使用託管於 Python.org 的 PNG 標誌。若要更換 URL，請選擇可信且有權存取的 HTTPS 圖片。

## 執行環境

此程式碼適用於本機電腦上的互動式 Python 工作階段。在 Colab 等遠端筆記本中，本機瀏覽器可能無法直接存取執行階段中的暫存檔案。

## 下載並開啟圖片

程式碼設定 15 秒網路逾時、檢查 Content-Type 和 PNG 檔案簽章，並將下載大小限制為 2 MiB。若瀏覽器成功啟動，請關閉圖片、返回終端機並按 Enter 刪除暫存檔案。

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

## 限制與注意事項

請使用可信的圖片 URL，並確認具備必要的使用權利。範例只接受 PNG，並拒絕超過 2 MiB 的檔案。瀏覽器能否啟動取決於作業系統與執行環境。

## 官方資料

- [Python: urllib.request](https://docs.python.org/3/library/urllib.request.html)
- [Python: tempfile](https://docs.python.org/3/library/tempfile.html)
- [Python: webbrowser](https://docs.python.org/3/library/webbrowser.html)
- [Python Software Foundation: Python logos](https://www.python.org/community/logos/)
