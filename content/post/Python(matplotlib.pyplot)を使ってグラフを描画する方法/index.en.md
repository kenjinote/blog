---
title: "Plot Graphs with Python and Matplotlib in Google Colab"
slug: "Python(matplotlib.pyplot)を使ってGraphを描画する方法"
tags: ["Python", "Graph", "Math", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "Use NumPy and Matplotlib in Google Colab to plot sine and cosine curves from 0 to 2π."
date: "2023-04-09T01:02:19+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

This example plots sine and cosine curves in a Google Colab notebook with Python, NumPy, and Matplotlib. Colab's interface and menu labels can change, so create a blank notebook using the current interface.

## Requirements

You need a Google Account and an internet connection. With Colab's hosted runtime, you can run the code without setting up a local Python environment.

## Run the notebook cell

Paste the code into a code cell in a new notebook and run the cell. x contains 500 evenly spaced values from 0 through 2π. The plot evaluates sine and cosine at those radian values and displays a legend.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
plt.plot(x, np.sin(x), label="sin curve")
plt.plot(x, np.cos(x), label="cos curve")
plt.legend()
plt.show()
```

## Example result

The cell displays a graph with the sine and cosine curves. If a library is unavailable in the hosted runtime, run `%pip install numpy matplotlib` in a cell, then rerun the example.

![Plot of sine and cosine](img_1.webp)

![Plot of sine and cosine](img.webp)

## Official references

- [Matplotlib: pyplot](https://matplotlib.org/stable/api/pyplot_summary.html)
- [NumPy: linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
- [Google Colab: FAQ](https://research.google.com/colaboratory/faq.html?hl=en)
- [Open Google Colab](https://colab.research.google.com/)
