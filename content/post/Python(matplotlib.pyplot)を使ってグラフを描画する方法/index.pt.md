---
title: "Criar gráficos com Python e Matplotlib no Google Colab"
slug: "Python(matplotlib.pyplot)を使ってGrafoを描画する方法"
tags: ["Python", "Gráficos", "Matemática", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "Use NumPy e Matplotlib no Google Colab para desenhar as curvas de seno e cosseno de 0 a 2π."
date: "2023-04-09T01:02:19+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Este exemplo desenha curvas de seno e cosseno em um notebook do Google Colab com Python, NumPy e Matplotlib. A interface e os nomes dos menus do Colab podem mudar; crie um notebook vazio pela interface atual.

## Requisitos

Você precisa de uma Conta do Google e de conexão à internet. Com o ambiente hospedado do Colab, é possível executar o código sem configurar o Python no computador local.

## Executar a célula do notebook

Cole o código em uma célula de um novo notebook e execute-a. x contém 500 valores igualmente espaçados de 0 até 2π, incluindo as extremidades. O gráfico calcula seno e cosseno para esses valores em radianos e exibe uma legenda.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
plt.plot(x, np.sin(x), label="sin curve")
plt.plot(x, np.cos(x), label="cos curve")
plt.legend()
plt.show()
```

## Resultado de exemplo

A célula mostra um gráfico com as curvas de seno e cosseno. Se alguma biblioteca não estiver disponível no ambiente hospedado, execute `%pip install numpy matplotlib` em uma célula e rode o exemplo novamente.

![Gráfico de seno e cosseno](img_1.webp)

![Gráfico de seno e cosseno](img.webp)

## Referências oficiais

- [Matplotlib: pyplot](https://matplotlib.org/stable/api/pyplot_summary.html)
- [NumPy: linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
- [Google Colab: FAQ](https://research.google.com/colaboratory/faq.html?hl=en)
- [Open Google Colab](https://colab.research.google.com/)
