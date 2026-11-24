---
title: "Построение графиков на Python и Matplotlib в Google Colab"
slug: "Python(matplotlib.pyplot)を使ってГрафを描画する方法"
tags: ["Python", "график", "математика", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "Используйте NumPy и Matplotlib в Google Colab, чтобы построить синус и косинус на интервале от 0 до 2π."
date: "2023-04-09T01:02:19+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

В этом примере графики синуса и косинуса строятся в блокноте Google Colab с помощью Python, NumPy и Matplotlib. Интерфейс и названия меню Colab могут меняться; создайте пустой блокнот через текущий интерфейс.

## Требования

Нужны аккаунт Google и подключение к Интернету. В облачной среде Colab код запускается без настройки локального окружения Python.

## Запуск ячейки блокнота

Вставьте код в ячейку нового блокнота и запустите её. x содержит 500 равномерно распределённых значений от 0 до 2π включительно. График вычисляет синус и косинус для этих значений в радианах и показывает легенду.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
plt.plot(x, np.sin(x), label="sin curve")
plt.plot(x, np.cos(x), label="cos curve")
plt.legend()
plt.show()
```

## Пример результата

В ячейке отобразится график синуса и косинуса. Если в облачной среде не найдётся библиотека, выполните в ячейке `%pip install numpy matplotlib`, а затем запустите пример повторно.

![График синуса и косинуса](img_1.webp)

![График синуса и косинуса](img.webp)

## Официальные материалы

- [Matplotlib: pyplot](https://matplotlib.org/stable/api/pyplot_summary.html)
- [NumPy: linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
- [Google Colab: FAQ](https://research.google.com/colaboratory/faq.html?hl=en)
- [Open Google Colab](https://colab.research.google.com/)
