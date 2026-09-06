---
title: "如何使用 Python (matplotlib.pyplot) 繪製圖表"
slug: "如何使用 Python (matplotlib.pyplot) 繪製圖表"
date: 2023-04-09T01:02:19+09:00
tags: ["Python", "圖表", "數學", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.png"
categories: ["數學・密碼學・量子"]
---

![img_1.png](img_1.png)

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

![img.png](img.png)

# 參考資料

- [matplotlib.pyplot — Matplotlib 3.5.3 documentation](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
