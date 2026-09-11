---
title: 'Código de exemplo em Python para baixar imagens, salvar temporariamente e exibi-las'
slug: "Pythonコード片"
date: 2025-02-24T18:21:14+09:00
tags: ["Python", "Código de exemplo"]
draft: false
image: "img.webp"
categories: ["Programação"]
description: 'Apresentamos uma série de códigos de exemplo práticos que usam apenas a biblioteca padrão do Python para baixar dados da URL de uma imagem da web, salvá-la em um arquivo temporário, exibi-la no navegador e, em seguida, excluí-la automaticamente.'
---

Apresentação de códigos de exemplo usando a biblioteca padrão.

# Baixar e exibir uma imagem
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

    # Salvar em um arquivo temporário e exibir
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(img_data)
        print(f"file://{tmp.name}")
        webbrowser.open(f"file://{tmp.name}")
        time.sleep(3)
except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    if 'tmp' in locals():
        os.unlink(tmp.name)  # Excluir arquivo temporário
```
