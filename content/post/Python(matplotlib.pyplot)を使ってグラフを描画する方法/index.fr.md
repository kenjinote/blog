---
title: "Tracer des graphiques avec Python et Matplotlib dans Google Colab"
slug: "Python(matplotlib.pyplot)を使ってGrapheを描画する方法"
tags: ["Python", "Graphiques", "Mathématiques", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "Utilisez NumPy et Matplotlib dans Google Colab pour tracer les courbes sinus et cosinus de 0 à 2π."
date: "2023-04-09T01:02:19+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Cet exemple trace des courbes sinus et cosinus dans un notebook Google Colab avec Python, NumPy et Matplotlib. L’interface et les noms de menus de Colab peuvent changer ; créez un notebook vierge à partir de l’interface actuelle.

## Prérequis

Vous avez besoin d’un compte Google et d’une connexion Internet. L’environnement hébergé de Colab permet d’exécuter le code sans configurer Python sur votre ordinateur.

## Exécuter la cellule du notebook

Collez le code dans une cellule d’un nouveau notebook et exécutez-la. x contient 500 valeurs régulièrement espacées de 0 à 2π inclus. Le graphique calcule sinus et cosinus pour ces valeurs en radians et affiche une légende.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
plt.plot(x, np.sin(x), label="sin curve")
plt.plot(x, np.cos(x), label="cos curve")
plt.legend()
plt.show()
```

## Résultat d’exemple

La cellule affiche un graphique avec les courbes sinus et cosinus. Si une bibliothèque est absente de l’environnement hébergé, exécutez `%pip install numpy matplotlib` dans une cellule, puis relancez l’exemple.

![Graphique du sinus et du cosinus](img_1.webp)

![Graphique du sinus et du cosinus](img.webp)

## Références officielles

- [Matplotlib: pyplot](https://matplotlib.org/stable/api/pyplot_summary.html)
- [NumPy: linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
- [Google Colab: FAQ](https://research.google.com/colaboratory/faq.html?hl=en)
- [Open Google Colab](https://colab.research.google.com/)
