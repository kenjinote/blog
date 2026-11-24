---
title: "Dibujar gráficas con Python y Matplotlib en Google Colab"
slug: "Python(matplotlib.pyplot)を使ってGráficoを描画する方法"
tags: ["Python", "Gráfico", "Matemáticas", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "Usa NumPy y Matplotlib en Google Colab para representar las curvas seno y coseno de 0 a 2π."
date: "2023-04-09T01:02:19+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Este ejemplo dibuja las curvas seno y coseno en un cuaderno de Google Colab con Python, NumPy y Matplotlib. La interfaz y los nombres de los menús de Colab pueden cambiar; crea un cuaderno vacío desde la interfaz actual.

## Requisitos

Necesitas una cuenta de Google y conexión a Internet. Con el entorno alojado de Colab puedes ejecutar el código sin configurar Python en tu equipo.

## Ejecutar la celda del cuaderno

Pega el código en una celda de un cuaderno nuevo y ejecútala. x contiene 500 valores equidistantes desde 0 hasta 2π, incluido. La gráfica calcula seno y coseno para esos valores en radianes y muestra una leyenda.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
plt.plot(x, np.sin(x), label="sin curve")
plt.plot(x, np.cos(x), label="cos curve")
plt.legend()
plt.show()
```

## Resultado de ejemplo

La celda muestra una gráfica con las curvas seno y coseno. Si falta alguna biblioteca en el entorno alojado, ejecuta `%pip install numpy matplotlib` en una celda y vuelve a ejecutar el ejemplo.

![Gráfica de seno y coseno](img_1.webp)

![Gráfica de seno y coseno](img.webp)

## Referencias oficiales

- [Matplotlib: pyplot](https://matplotlib.org/stable/api/pyplot_summary.html)
- [NumPy: linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
- [Google Colab: FAQ](https://research.google.com/colaboratory/faq.html?hl=en)
- [Open Google Colab](https://colab.research.google.com/)
