---
title: 'Como desenhar gráficos usando Python e matplotlib [Compatível com Google Colab]'
slug: "Como desenhar gráficos usando Python (matplotlib.pyplot)"
date: 2023-04-09T01:02:19+09:00
tags: ["Python", "Gráficos", "Matemática", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["Matemática・Criptografia・Quântica"]
description: 'Explicamos para iniciantes os passos para desenhar e exibir facilmente gráficos de ondas senoidais e cosseno usando a biblioteca matplotlib.pyplot do Python, através do Google Colaboratory. Você pode testar imediatamente sem a necessidade de configurar o ambiente.'
---

![img_1.png](img_1.webp)

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

![img.png](img.webp)

# Referências

- [matplotlib.pyplot — Matplotlib 3.5.3 documentation](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
