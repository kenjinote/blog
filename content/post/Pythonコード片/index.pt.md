---
title: "Baixar, salvar temporariamente e abrir uma imagem com Python"
slug: "Pythonコード片"
tags: ["Python", "Código de exemplo"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Valide um PNG com a biblioteca padrão do Python, abra uma cópia temporária no navegador do computador e exclua-a depois."
date: "2025-02-24T18:21:14+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Este exemplo usa apenas a biblioteca padrão do Python para baixar uma imagem da Web, salvá-la temporariamente e abri-la em um navegador de desktop local. Ele usa um logotipo PNG hospedado no Python.org. Se você trocar a URL, escolha uma imagem HTTPS confiável que tenha permissão para acessar.

## Ambiente

O código foi feito para uma sessão interativa de Python em um computador local. Em um notebook remoto como o Colab, o navegador local talvez não consiga acessar diretamente um arquivo temporário do ambiente de execução.

## Baixar e abrir a imagem

O código define um tempo limite de rede de 15 segundos, verifica o Content-Type e a assinatura PNG e limita o download a 2 MiB. Se o navegador abrir, feche a imagem, volte ao terminal e pressione Enter para excluir o arquivo temporário.

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

## Limites e observações

Use uma URL de imagem confiável e confirme que tem os direitos necessários para usá-la. O exemplo aceita apenas PNG e rejeita arquivos maiores que 2 MiB. A abertura do navegador depende do sistema operacional e do ambiente de execução.

## Referências oficiais

- [Python: urllib.request](https://docs.python.org/3/library/urllib.request.html)
- [Python: tempfile](https://docs.python.org/3/library/tempfile.html)
- [Python: webbrowser](https://docs.python.org/3/library/webbrowser.html)
- [Python Software Foundation: Python logos](https://www.python.org/community/logos/)
