---
title: "Download, Temporarily Save, and Open an Image with Python"
slug: "Pythonコード片"
tags: ["Python", "Sample Code"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Use Python's standard library to validate a PNG, open a temporary copy in a desktop browser, and delete it after viewing."
date: "2025-02-24T18:21:14+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

This example uses only Python's standard library to download a web image, save it temporarily, and open it in a local desktop browser. It uses a PNG logo hosted by Python.org. If you change the URL, choose a trusted HTTPS image that you are allowed to access.

## Environment

The code is intended for an interactive Python session on a local computer. In a remote notebook such as Colab, a temporary file on the runtime may not be directly accessible to your local browser.

## Download and open the image

The code uses a 15-second network timeout, checks the PNG Content-Type and file signature, and limits the download to 2 MiB. If the browser launches, close the image, return to the terminal, and press Enter to delete the temporary file.

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

## Limits and notes

Use a trusted image URL and confirm that you have the rights needed for your use. The example accepts PNG only and rejects files larger than 2 MiB. Browser launching depends on the operating system and execution environment.

## Official references

- [Python: urllib.request](https://docs.python.org/3/library/urllib.request.html)
- [Python: tempfile](https://docs.python.org/3/library/tempfile.html)
- [Python: webbrowser](https://docs.python.org/3/library/webbrowser.html)
- [Python Software Foundation: Python logos](https://www.python.org/community/logos/)
