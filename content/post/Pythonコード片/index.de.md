---
title: "Ein Bild mit Python herunterladen, temporär speichern und öffnen"
slug: "Pythonコード片"
tags: ["Python", "Beispielcode"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Laden Sie mit der Python-Standardbibliothek ein geprüftes PNG herunter, öffnen Sie eine temporäre Kopie im Desktop-Browser und löschen Sie sie danach."
date: "2025-02-24T18:21:14+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Dieses Beispiel verwendet nur die Python-Standardbibliothek, um ein Webbild herunterzuladen, temporär zu speichern und in einem lokalen Desktop-Browser zu öffnen. Als Beispiel dient ein PNG-Logo von Python.org. Wenn Sie die URL ändern, verwenden Sie ein vertrauenswürdiges HTTPS-Bild, auf das Sie zugreifen dürfen.

## Umgebung

Der Code ist für eine interaktive Python-Sitzung auf einem lokalen Computer gedacht. In einem Remote-Notebook wie Colab ist eine temporäre Datei der Laufzeitumgebung möglicherweise nicht direkt im lokalen Browser erreichbar.

## Bild herunterladen und öffnen

Der Code verwendet ein Netzwerk-Timeout von 15 Sekunden, prüft Content-Type und PNG-Signatur und begrenzt den Download auf 2 MiB. Wenn der Browser gestartet wurde, schließen Sie das Bild, kehren Sie zum Terminal zurück und drücken Sie die Eingabetaste, um die temporäre Datei zu löschen.

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

## Grenzen und Hinweise

Verwenden Sie eine vertrauenswürdige Bild-URL und prüfen Sie, ob Sie das Bild für Ihren Zweck nutzen dürfen. Das Beispiel akzeptiert nur PNG und weist Dateien über 2 MiB zurück. Das Starten eines Browsers hängt vom Betriebssystem und der Laufzeitumgebung ab.

## Offizielle Referenzen

- [Python: urllib.request](https://docs.python.org/3/library/urllib.request.html)
- [Python: tempfile](https://docs.python.org/3/library/tempfile.html)
- [Python: webbrowser](https://docs.python.org/3/library/webbrowser.html)
- [Python Software Foundation: Python logos](https://www.python.org/community/logos/)
