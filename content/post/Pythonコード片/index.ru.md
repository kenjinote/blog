---
title: "Загрузка, временное сохранение и открытие изображения в Python"
slug: "Pythonコード片"
tags: ["Python", "пример кода"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Проверьте PNG средствами стандартной библиотеки Python, откройте временную копию в браузере и удалите её после просмотра."
date: "2025-02-24T18:21:14+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

В этом примере стандартная библиотека Python загружает веб-изображение, временно сохраняет его и открывает в локальном настольном браузере. Используется PNG-логотип с сайта Python.org. При замене URL укажите доверенное изображение HTTPS, к которому у вас есть доступ.

## Среда выполнения

Код рассчитан на интерактивный сеанс Python на локальном компьютере. В удалённом блокноте, например Colab, локальный браузер может не иметь прямого доступа к временному файлу среды выполнения.

## Загрузка и открытие изображения

Код задаёт тайм-аут сети 15 секунд, проверяет Content-Type и сигнатуру PNG, а также ограничивает загрузку размером 2 МиБ. Если браузер открылся, закройте изображение, вернитесь в терминал и нажмите Enter, чтобы удалить временный файл.

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

## Ограничения и примечания

Используйте доверенный URL изображения и убедитесь в наличии необходимых прав. Пример принимает только PNG и отклоняет файлы больше 2 МиБ. Запуск браузера зависит от ОС и среды выполнения.

## Официальная документация

- [Python: urllib.request](https://docs.python.org/3/library/urllib.request.html)
- [Python: tempfile](https://docs.python.org/3/library/tempfile.html)
- [Python: webbrowser](https://docs.python.org/3/library/webbrowser.html)
- [Python Software Foundation: Python logos](https://www.python.org/community/logos/)
