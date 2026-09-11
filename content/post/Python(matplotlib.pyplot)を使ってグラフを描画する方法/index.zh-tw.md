---
title: '使用 Python 與 matplotlib 繪製圖表的方法【支援 Google Colab】'
slug: "Python(matplotlib.pyplot)を使ってグラフを描画する方法"
date: 2023-04-09T01:02:19+09:00
tags: ["Python", "圖表", "數學", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["數學・密碼學・量子"]
description: '為初學者說明如何使用 Google Colaboratory，透過 Python 的 matplotlib.pyplot 函式庫輕鬆繪製並顯示正弦波與餘弦波圖表的步驟。無須建置環境即可立即測試。'
---

![img_1.png](img_1.webp)

# 需要的東西
- Google 帳號

# 步驟

1. 進入 [https://colab.research.google.com/](https://colab.research.google.com/)
2. 選擇「檔案」→「新增筆記本」
3. 貼上並執行以下程式碼
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2*np.pi, 500)
plt.plot(x, np.sin(x), label="sin curve")
plt.plot(x, np.cos(x), label="cos curve")
plt.legend() # 顯示圖例
plt.show()
```

# 執行結果

![img.png](img.webp)

# 參考資料

- [matplotlib.pyplot — Matplotlib 3.5.3 documentation](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
