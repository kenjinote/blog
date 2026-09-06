---
title: "Как рисовать графики с помощью Python (matplotlib.pyplot)"
slug: "как-рисовать-графики-с-помощью-python-matplotlib-pyplot"
date: 2023-04-09T01:02:19+09:00
tags: ["Python", "график", "математика", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.png"
categories: ["Математика, криптография, квант"]
---

![img_1.png](img_1.png)

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

![img.png](img.png)

# Ссылки

- [matplotlib.pyplot — Matplotlib 3.5.3 documentation](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
