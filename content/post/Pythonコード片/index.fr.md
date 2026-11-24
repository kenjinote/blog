---
title: "Télécharger, enregistrer temporairement et ouvrir une image avec Python"
slug: "Pythonコード片"
tags: ["Python", "Code d'exemple"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Validez un PNG avec la bibliothèque standard de Python, ouvrez une copie temporaire dans un navigateur de bureau, puis supprimez-la."
date: "2025-02-24T18:21:14+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Cet exemple utilise uniquement la bibliothèque standard de Python pour télécharger une image Web, l’enregistrer temporairement et l’ouvrir dans un navigateur de bureau local. Il utilise un logo PNG hébergé sur Python.org. Si vous changez l’URL, choisissez une image HTTPS fiable à laquelle vous êtes autorisé à accéder.

## Environnement

Le code est destiné à une session Python interactive sur un ordinateur local. Dans un notebook distant comme Colab, le navigateur local ne peut pas toujours accéder directement à un fichier temporaire de l’environnement d’exécution.

## Télécharger et ouvrir l’image

Le code définit un délai réseau de 15 secondes, vérifie le type de contenu et la signature PNG, et limite le téléchargement à 2 Mio. Si le navigateur s’ouvre, fermez l’image, revenez au terminal et appuyez sur Entrée pour supprimer le fichier temporaire.

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

## Limites et remarques

Utilisez une URL d’image fiable et vérifiez que vous disposez des droits nécessaires. L’exemple accepte uniquement les PNG et refuse les fichiers de plus de 2 Mio. Le lancement du navigateur dépend du système et de l’environnement d’exécution.

## Références officielles

- [Python: urllib.request](https://docs.python.org/3/library/urllib.request.html)
- [Python: tempfile](https://docs.python.org/3/library/tempfile.html)
- [Python: webbrowser](https://docs.python.org/3/library/webbrowser.html)
- [Python Software Foundation: Python logos](https://www.python.org/community/logos/)
