---
title: "Comment dessiner des graphiques avec Python (matplotlib.pyplot)"
slug: "Comment dessiner des graphiques avec Python (matplotlib.pyplot)"
date: 2023-04-09T01:02:19+09:00
tags: ["Python", "Graphiques", "Mathématiques", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.png"
categories: ["Mathématiques・Cryptographie・Quantique"]
---

![img_1.png](img_1.png)

# Ce dont vous avez besoin
- Compte Google

# Étapes

1. Accédez à [https://colab.research.google.com/](https://colab.research.google.com/)
2. Sélectionnez "Fichier" -> "Nouveau notebook"
3. Collez et exécutez le code ci-dessous
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2*np.pi, 500)
plt.plot(x, np.sin(x), label="sin curve")
plt.plot(x, np.cos(x), label="cos curve")
plt.legend() # Afficher la légende
plt.show()
```

# Résultat de l'exécution

![img.png](img.png)

# Références

- [matplotlib.pyplot — Matplotlib 3.5.3 documentation](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
