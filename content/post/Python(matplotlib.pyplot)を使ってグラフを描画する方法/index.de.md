---
title: "Diagramme mit Python und Matplotlib in Google Colab zeichnen"
slug: "Python(matplotlib.pyplot)を使ってGraphを描画する方法"
tags: ["Python", "Diagramme", "Mathematik", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "Zeichnen Sie mit NumPy und Matplotlib in Google Colab Sinus- und Kosinuskurven von 0 bis 2π."
date: "2023-04-09T01:02:19+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Dieses Beispiel zeichnet Sinus- und Kosinuskurven in einem Google-Colab-Notebook mit Python, NumPy und Matplotlib. Die Oberfläche und Menünamen von Colab können sich ändern; erstellen Sie ein leeres Notebook über die aktuelle Oberfläche.

## Voraussetzungen

Sie benötigen ein Google-Konto und eine Internetverbindung. Mit der gehosteten Colab-Laufzeit können Sie den Code ohne lokale Python-Umgebung ausführen.

## Die Notebookzelle ausführen

Fügen Sie den Code in eine Codezelle eines neuen Notebooks ein und führen Sie sie aus. x enthält 500 gleichmäßig verteilte Werte von 0 bis einschließlich 2π. Für diese Werte im Bogenmaß werden Sinus und Kosinus gezeichnet und eine Legende angezeigt.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
plt.plot(x, np.sin(x), label="sin curve")
plt.plot(x, np.cos(x), label="cos curve")
plt.legend()
plt.show()
```

## Beispielergebnis

Die Zelle zeigt ein Diagramm mit Sinus- und Kosinuskurve. Falls eine Bibliothek in der gehosteten Laufzeit fehlt, führen Sie `%pip install numpy matplotlib` in einer Zelle aus und starten Sie das Beispiel erneut.

![Diagramm mit Sinus und Kosinus](img_1.webp)

![Diagramm mit Sinus und Kosinus](img.webp)

## Offizielle Referenzen

- [Matplotlib: pyplot](https://matplotlib.org/stable/api/pyplot_summary.html)
- [NumPy: linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
- [Google Colab: FAQ](https://research.google.com/colaboratory/faq.html?hl=en)
- [Open Google Colab](https://colab.research.google.com/)
