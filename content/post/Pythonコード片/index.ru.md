---
title: 'Пример кода на Python для загрузки, временного сохранения и отображения изображения'
slug: "Pythonコード片"
date: 2025-02-24T18:21:14+09:00
tags: ["Python", "пример кода"]
draft: false
image: "img.webp"
categories: ["Программирование"]
description: 'Представлен практический пример кода, который использует только стандартные библиотеки Python для загрузки данных по URL-адресу изображения в Интернете, сохранения их во временный файл, отображения в браузере, а затем автоматического удаления.'
---

Введение в пример кода с использованием стандартной библиотеки.

# Скачивание и отображение изображения
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

    # Сохранить во временный файл и отобразить
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(img_data)
        print(f"file://{tmp.name}")
        webbrowser.open(f"file://{tmp.name}")
        time.sleep(3)
except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    if 'tmp' in locals():
        os.unlink(tmp.name)  # Удалить временный файл
```
