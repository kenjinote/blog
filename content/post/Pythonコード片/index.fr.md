---
title: "Extraits de code Python"
slug: "Pythonコード片"
date: 2025-02-24T18:21:14+09:00
tags: ["Python", "Code d'exemple"]
draft: false
image: "img.png"
categories: ["Programmation"]
---

Présentation d'exemples de code utilisant la bibliothèque standard.

# Télécharger et afficher une image
```python
import urllib.request
import tempfile
import os
import webbrowser
import time

url = "https://www.aomori-ringo.or.jp/kids/wp-content/uploads/2021/11/apple.png"

try:
    with urllib.request.urlopen(url) as response:
        img_data = response.read()

    # Enregistrer dans un fichier temporaire et afficher
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(img_data)
        print(f"file://{tmp.name}")
        webbrowser.open(f"file://{tmp.name}")
        time.sleep(3)
except Exception as e:
    print(f"Une erreur s'est produite : {e}")

finally:
    if 'tmp' in locals():
        os.unlink(tmp.name)  # Supprimer le fichier temporaire
```
