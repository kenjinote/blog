---
title: "Google Colab에서 Python과 Matplotlib으로 그래프 그리기"
slug: "Python(matplotlib.pyplot)を使って그래프を描画する方法"
tags: ["Python", "그래프", "수학", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "Google Colab에서 NumPy와 Matplotlib을 사용해 0부터 2π까지의 사인·코사인 곡선을 그립니다."
date: "2023-04-09T01:02:19+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

이 예제는 Python, NumPy, Matplotlib을 사용해 Google Colab 노트북에서 사인 및 코사인 곡선을 그립니다. Colab의 인터페이스와 메뉴 이름은 바뀔 수 있으므로 현재 화면에서 빈 노트북을 만드세요.

## 필요 항목

Google 계정과 인터넷 연결이 필요합니다. Colab 호스팅 런타임을 이용하면 로컬 PC에 Python 환경을 구성하지 않고 코드를 실행할 수 있습니다.

## 노트북 셀 실행

새 노트북의 코드 셀에 코드를 붙여넣고 실행하세요. x에는 0부터 2π까지 양 끝을 포함해 균등 간격으로 배치한 값 500개가 들어갑니다. 그래프는 라디안 값의 사인과 코사인을 그려 범례를 표시합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
plt.plot(x, np.sin(x), label="sin curve")
plt.plot(x, np.cos(x), label="cos curve")
plt.legend()
plt.show()
```

## 실행 예시

셀을 실행하면 사인과 코사인 곡선이 함께 표시됩니다. 호스팅 런타임에서 라이브러리를 찾을 수 없으면 셀에서 `%pip install numpy matplotlib`을 실행한 뒤 예제를 다시 실행하세요.

![사인과 코사인 그래프](img_1.webp)

![사인과 코사인 그래프](img.webp)

## 공식 참고 자료

- [Matplotlib: pyplot](https://matplotlib.org/stable/api/pyplot_summary.html)
- [NumPy: linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
- [Google Colab: FAQ](https://research.google.com/colaboratory/faq.html?hl=en)
- [Open Google Colab](https://colab.research.google.com/)
