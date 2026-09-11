---
title: 'Python-Beispielcode zum Herunterladen, temporären Speichern und Anzeigen von Bildern'
slug: "Pythonコード片"
date: 2025-02-24T18:21:14+09:00
tags: ["Python", "Beispielcode"]
draft: false
image: "img.webp"
categories: ["Programmierung"]
description: 'Stellt einen praktischen Beispielcode vor, der nur die Standardbibliothek von Python verwendet, um Daten von einer Bild-URL aus dem Web herunterzuladen, in einer temporären Datei zu speichern, im Browser anzuzeigen und danach automatisch zu löschen.'
---

Einführung in Beispielcode mit der Standardbibliothek.

# Ein Bild herunterladen und anzeigen
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

    # In einer temporären Datei speichern und anzeigen
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(img_data)
        print(f"file://{tmp.name}")
        webbrowser.open(f"file://{tmp.name}")
        time.sleep(3)
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")

finally:
    if 'tmp' in locals():
        os.unlink(tmp.name)  # Temporäre Datei löschen
```
