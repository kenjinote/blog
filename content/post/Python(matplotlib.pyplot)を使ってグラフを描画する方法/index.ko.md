---




title: 'Python과 matplotlib로 그래프를 그리는 방법 [Google Colab 대응]'
slug: "Python(matplotlib.pyplot)を使ってグラフを描画する方法"
date: 2023-04-09T01:02:19+09:00
tags: ["Python", "그래프", "수학", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["수학・암호・양자"]
description: 'Google Colaboratory를 사용하여 Python의 matplotlib.pyplot 라이브러리로 사인파 및 코사인파 그래프를 간단히 그리고 표시하는 절차를 초보자를 위해 설명합니다. 환경 구축 없이 바로 테스트해 볼 수 있습니다.'
---





![img_1.png](img_1.webp)

# 필요한 것
- Google 계정

# 순서

1. [https://colab.research.google.com/](https://colab.research.google.com/) 에 접속
2. '파일' → '새 노트' 선택
3. 아래의 코드를 붙여넣고 실행
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2*np.pi, 500)
plt.plot(x, np.sin(x), label="sin curve")
plt.plot(x, np.cos(x), label="cos curve")
plt.legend() # 범례 표시
plt.show()
```

# 실행 결과

![img.png](img.webp)

# 참고

- [matplotlib.pyplot — Matplotlib 3.5.3 documentation](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
