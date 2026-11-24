---
title: "Mengunduh, Menyimpan Sementara, dan Membuka Gambar dengan Python"
slug: "Pythonコード片"
tags: ["Python", "kode sampel"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Validasi PNG dengan pustaka standar Python, buka salinan sementara di browser desktop, lalu hapus setelah dilihat."
date: "2025-02-24T18:21:14+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Contoh ini hanya menggunakan pustaka standar Python untuk mengunduh gambar web, menyimpannya sementara, lalu membukanya di browser desktop lokal. Contoh memakai logo PNG yang di-host di Python.org. Jika URL diganti, pilih gambar HTTPS tepercaya yang boleh Anda akses.

## Lingkungan

Kode ini ditujukan untuk sesi Python interaktif di komputer lokal. Di notebook jarak jauh seperti Colab, file sementara pada runtime mungkin tidak dapat langsung diakses oleh browser lokal.

## Unduh dan buka gambar

Kode menetapkan timeout jaringan 15 detik, memeriksa Content-Type dan tanda tangan PNG, serta membatasi unduhan hingga 2 MiB. Jika browser berhasil dibuka, tutup gambar, kembali ke terminal, lalu tekan Enter untuk menghapus file sementara.

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

## Batasan dan catatan

Gunakan URL gambar tepercaya dan pastikan Anda memiliki hak yang diperlukan. Contoh hanya menerima PNG dan menolak file berukuran lebih dari 2 MiB. Peluncuran browser bergantung pada OS dan lingkungan eksekusi.

## Referensi resmi

- [Python: urllib.request](https://docs.python.org/3/library/urllib.request.html)
- [Python: tempfile](https://docs.python.org/3/library/tempfile.html)
- [Python: webbrowser](https://docs.python.org/3/library/webbrowser.html)
- [Python Software Foundation: Python logos](https://www.python.org/community/logos/)
