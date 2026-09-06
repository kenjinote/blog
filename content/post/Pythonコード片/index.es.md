---








title: "Fragmentos de código de Python"
slug: "Pythonコード片"
date: 2025-02-24T18:21:14+09:00
tags: ["Python", "Código de ejemplo"]
draft: false
image: "img.png"
categories: ["Programación"]
---









Esta es una introducción a ejemplos de código utilizando la biblioteca estándar.

# Descargar y mostrar una imagen
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

    # Guardar en un archivo temporal y mostrar
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(img_data)
        print(f"file://{tmp.name}")
        webbrowser.open(f"file://{tmp.name}")
        time.sleep(3)
except Exception as e:
    print(f"Ocurrió un error: {e}")

finally:
    if 'tmp' in locals():
        os.unlink(tmp.name)  # Eliminar archivo temporal
```
