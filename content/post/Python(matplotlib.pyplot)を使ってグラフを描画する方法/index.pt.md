---
title: "Como desenhar gráficos usando Python (matplotlib.pyplot)"
slug: "Como desenhar gráficos usando Python (matplotlib.pyplot)"
date: 2023-04-09T01:02:19+09:00
tags: ["Python", "Gráficos", "Matemática", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.png"
categories: ["Matemática・Criptografia・Quântica"]
---

![img_1.png](img_1.png)

# O que você precisa
- Conta do Google

# Passos

1. Acesse [https://colab.research.google.com/](https://colab.research.google.com/)
2. Selecione "Arquivo" -> "Novo notebook"
3. Cole e execute o código abaixo
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2*np.pi, 500)
plt.plot(x, np.sin(x), label="sin curve")
plt.plot(x, np.cos(x), label="cos curve")
plt.legend() # Mostrar legenda
plt.show()
```

# Resultado da execução

![img.png](img.png)

# Referências

- [matplotlib.pyplot — Matplotlib 3.5.3 documentation](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
