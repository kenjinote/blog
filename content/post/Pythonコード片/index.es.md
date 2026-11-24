---
title: "Descargar, guardar temporalmente y abrir una imagen con Python"
slug: "Pythonコード片"
tags: ["Python", "Código de ejemplo"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Valida un PNG con la biblioteca estándar de Python, abre una copia temporal en un navegador de escritorio y elimínala después."
date: "2025-02-24T18:21:14+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Este ejemplo solo usa la biblioteca estándar de Python para descargar una imagen web, guardarla temporalmente y abrirla en un navegador de escritorio local. Utiliza un logotipo PNG alojado en Python.org. Si cambias la URL, elige una imagen HTTPS de confianza a la que tengas permiso para acceder.

## Entorno

El código está pensado para una sesión interactiva de Python en un equipo local. En un cuaderno remoto como Colab, es posible que el navegador local no pueda acceder directamente a un archivo temporal del entorno de ejecución.

## Descargar y abrir la imagen

El código establece un tiempo de espera de red de 15 segundos, comprueba el Content-Type y la firma PNG, y limita la descarga a 2 MiB. Si se abre el navegador, cierra la imagen, vuelve al terminal y pulsa Intro para eliminar el archivo temporal.

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

## Límites y notas

Usa una URL de imagen de confianza y confirma que tienes los derechos necesarios para utilizarla. El ejemplo solo acepta PNG y rechaza archivos de más de 2 MiB. El inicio del navegador depende del sistema operativo y del entorno de ejecución.

## Referencias oficiales

- [Python: urllib.request](https://docs.python.org/3/library/urllib.request.html)
- [Python: tempfile](https://docs.python.org/3/library/tempfile.html)
- [Python: webbrowser](https://docs.python.org/3/library/webbrowser.html)
- [Python Software Foundation: Python logos](https://www.python.org/community/logos/)
