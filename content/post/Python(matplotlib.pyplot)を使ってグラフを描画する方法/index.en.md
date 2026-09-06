---
title: 'How to draw graphs using Python (matplotlib.pyplot)'
slug: "Python(matplotlib.pyplot)を使ってグラフを描画する方法"
date: 2023-04-09T01:02:19+09:00
tags: ["Python", "Graph", "Math", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.png"
categories: ["Math/Cryptography/Quantum"]
---

![img_1.png](img_1.png)

# Requirements
- Google Account

# Steps

1. Access [https://colab.research.google.com/](https://colab.research.google.com/)
2. Select "File" -> "New notebook"
3. Paste and run the following code
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2*np.pi, 500)
plt.plot(x, np.sin(x), label="sin curve")
plt.plot(x, np.cos(x), label="cos curve")
plt.legend() # Show legend
plt.show()
```

# Execution Result

![img.png](img.png)

# References

- [matplotlib.pyplot — Matplotlib 3.5.3 documentation](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
