---
title: "使用 Python 下载、临时保存并打开图像"
slug: "Pythonコード片"
tags: ["Python", "示例代码"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "使用 Python 标准库验证 PNG，在桌面浏览器中打开临时副本，并在查看后删除。"
date: "2025-02-24T18:21:14+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

本示例仅使用 Python 标准库下载网络图像、临时保存并在本地桌面浏览器中打开。示例使用托管在 Python.org 的 PNG 标志。若要更换 URL，请选择可信且有权访问的 HTTPS 图像。

## 运行环境

此代码面向本地电脑上的交互式 Python 会话。在 Colab 等远程笔记本中，本地浏览器可能无法直接访问运行时中的临时文件。

## 下载并打开图像

代码设置 15 秒网络超时，检查 Content-Type 和 PNG 文件签名，并将下载大小限制为 2 MiB。如果浏览器成功启动，请关闭图像、返回终端并按 Enter 删除临时文件。

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

## 限制与注意事项

请使用可信的图像 URL，并确认拥有所需使用权限。示例仅接受 PNG，并拒绝超过 2 MiB 的文件。浏览器能否启动取决于操作系统和运行环境。

## 官方资料

- [Python: urllib.request](https://docs.python.org/3/library/urllib.request.html)
- [Python: tempfile](https://docs.python.org/3/library/tempfile.html)
- [Python: webbrowser](https://docs.python.org/3/library/webbrowser.html)
- [Python Software Foundation: Python logos](https://www.python.org/community/logos/)
