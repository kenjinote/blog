---
title: "Google ColabでPython・Matplotlibのグラフを描く"
slug: "Python(matplotlib.pyplot)を使ってグラフを描画する方法"
tags: ["Python", "グラフ", "数学", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "Google ColabでNumPyとMatplotlibを使い、0から2πまでのsin・cos曲線を描画する手順を紹介します。"
date: "2023-04-09T01:02:19+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Google Colabのノートブックで、PythonのNumPyとMatplotlibを使って正弦曲線と余弦曲線を描く例です。Colabの画面やメニュー名は更新されることがあるため、空のノートブックを現在の画面から作成してください。

## 必要なもの

Googleアカウントとインターネット接続が必要です。Colabのホスト型ランタイムを使う場合、手元のPCにPython環境を構築せずにコードを実行できます。

## ノートブックで実行する

新しいノートブックのコードセルに貼り付け、セルを実行してください。xは0から2πまでを含む500個の等間隔な値です。sinとcosはラジアン単位のxに対する値を描き、凡例を表示します。

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
plt.plot(x, np.sin(x), label="sin curve")
plt.plot(x, np.cos(x), label="cos curve")
plt.legend()
plt.show()
```

## 実行結果

実行すると、sin曲線とcos曲線を重ねたグラフが表示されます。Colabの標準ランタイムでライブラリが見つからない場合は、セルで`%pip install numpy matplotlib`を実行してからコードを再実行してください。

![sinとcosのグラフ](img_1.webp)

![sinとcosのグラフ](img.webp)

## 公式資料

- [Matplotlib: pyplot](https://matplotlib.org/stable/api/pyplot_summary.html)
- [NumPy: linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
- [Google Colab: FAQ](https://research.google.com/colaboratory/faq.html?hl=en)
- [Open Google Colab](https://colab.research.google.com/)
