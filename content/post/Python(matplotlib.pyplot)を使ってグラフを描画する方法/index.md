---
title: 'Python(matplotlib.pyplot)を使ってグラフを描画する方法'
date: 2023-04-09T01:02:19+09:00
tags: ["Python", "グラフ", "数学", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.png"
---

![img_1.png](img_1.png)

# 必要なもの
- Google アカウント

# 手順

1. [https://colab.research.google.com/](https://colab.research.google.com/) にアクセス
2. 「ファイル」→「ノートブックを新規作成」を選択
3. 下記のコードを貼り付けて実行
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2*np.pi, 500)
plt.plot(x, np.sin(x), label="sin curve")
plt.plot(x, np.cos(x), label="cos curve")
plt.legend() # 凡例の表示
plt.show()
```

# 実行結果

![img.png](img.png)

# 参考

- [matplotlib.pyplot — Matplotlib 3.5.3 documentation](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)