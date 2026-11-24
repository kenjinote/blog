---
title: "在 Google Colab 中使用 Python 和 Matplotlib 绘图"
slug: "Python(matplotlib.pyplot)を使って图を描画する方法"
tags: ["Python", "图表", "数学", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "在 Google Colab 中使用 NumPy 和 Matplotlib 绘制从 0 到 2π 的正弦与余弦曲线。"
date: "2023-04-09T01:02:19+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

本示例使用 Python、NumPy 和 Matplotlib，在 Google Colab 笔记本中绘制正弦与余弦曲线。Colab 的界面和菜单名称可能变化，请通过当前界面创建空白笔记本。

## 所需条件

需要 Google 账号和互联网连接。使用 Colab 托管运行时，无需在本地电脑配置 Python 环境即可运行代码。

## 运行笔记本单元格

将代码粘贴到新笔记本的代码单元格并运行。x 包含从 0 到 2π（含两端）等间隔的 500 个值。图表以弧度计算这些值的正弦和余弦，并显示图例。

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
plt.plot(x, np.sin(x), label="sin curve")
plt.plot(x, np.cos(x), label="cos curve")
plt.legend()
plt.show()
```

## 运行结果示例

运行后会显示包含正弦和余弦曲线的图表。如果托管运行时缺少库，请在单元格中运行 `%pip install numpy matplotlib`，然后重新运行示例。

![正弦和余弦曲线图](img_1.webp)

![正弦和余弦曲线图](img.webp)

## 官方资料

- [Matplotlib: pyplot](https://matplotlib.org/stable/api/pyplot_summary.html)
- [NumPy: linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
- [Google Colab: FAQ](https://research.google.com/colaboratory/faq.html?hl=en)
- [Open Google Colab](https://colab.research.google.com/)
