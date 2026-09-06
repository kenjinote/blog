---



title: "Cómo dibujar un gráfico usando Python (matplotlib.pyplot)"
slug: "Python(matplotlib.pyplot)を使ってグラフを描画する方法"
date: 2023-04-09T01:02:19+09:00
tags: ["Python", "Gráfico", "Matemáticas", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.png"
categories: ["Matemáticas, Criptografía, Cuántica"]
---




![img_1.png](img_1.png)

# Requisitos
- Cuenta de Google

# Procedimiento

1. Accede a [https://colab.research.google.com/](https://colab.research.google.com/)
2. Selecciona "Archivo" → "Nuevo cuaderno"
3. Pega y ejecuta el siguiente código:
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2*np.pi, 500)
plt.plot(x, np.sin(x), label="sin curve")
plt.plot(x, np.cos(x), label="cos curve")
plt.legend() # Muestra la leyenda
plt.show()
```

# Resultado de la ejecución

![img.png](img.png)

# Referencias

- [matplotlib.pyplot — Matplotlib 3.5.3 documentation](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
