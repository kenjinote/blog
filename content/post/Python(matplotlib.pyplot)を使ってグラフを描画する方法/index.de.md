---
title: "Wie man Diagramme mit Python (matplotlib.pyplot) zeichnet"
slug: "Wie man Diagramme mit Python (matplotlib.pyplot) zeichnet"
date: 2023-04-09T01:02:19+09:00
tags: ["Python", "Diagramme", "Mathematik", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.png"
categories: ["Mathematik・Kryptographie・Quanten"]
---

![img_1.png](img_1.png)

# Was Sie brauchen
- Google-Konto

# Schritte

1. Gehen Sie auf [https://colab.research.google.com/](https://colab.research.google.com/)
2. Wählen Sie "Datei" -> "Neues Notizbuch"
3. Fügen Sie den folgenden Code ein und führen Sie ihn aus
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2*np.pi, 500)
plt.plot(x, np.sin(x), label="sin curve")
plt.plot(x, np.cos(x), label="cos curve")
plt.legend() # Legende anzeigen
plt.show()
```

# Ausführungsergebnis

![img.png](img.png)

# Referenzen

- [matplotlib.pyplot — Matplotlib 3.5.3 documentation](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
