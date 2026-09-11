---
title: 'Как рисовать графики с помощью Python и matplotlib [Поддержка Google Colab]'
slug: "Python(matplotlib.pyplot)を使ってグラフを描画する方法"
date: 2023-04-09T01:02:19+09:00
tags: ["Python", "график", "математика", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["Математика, криптография, квант"]
description: 'Объясняется для новичков процедура легкого рисования и отображения графиков синуса и косинуса с использованием библиотеки matplotlib.pyplot для Python в Google Colaboratory. Вы можете попробовать это сразу, без настройки среды.'
---

![img_1.png](img_1.webp)

# Требования
- Аккаунт Google

# Шаги

1. Перейдите на [https://colab.research.google.com/](https://colab.research.google.com/)
2. Выберите «Файл» → «Создать блокнот»
3. Вставьте и выполните следующий код
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2*np.pi, 500)
plt.plot(x, np.sin(x), label="sin curve")
plt.plot(x, np.cos(x), label="cos curve")
plt.legend() # отображение легенды
plt.show()
```

# Результат

![img.png](img.webp)

# Ссылки

- [matplotlib.pyplot — Matplotlib 3.5.3 documentation](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
