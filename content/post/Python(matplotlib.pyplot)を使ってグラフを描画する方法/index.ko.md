---

title: "Python(matplotlib.pyplot)을 사용하여 그래프를 그리는 방법"
date: 2023-04-09T01:02:19+09:00
tags: ["Python", "그래프", "수학", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.png"
categories: ["수학・암호・양자"]
---


![img_1.png](img_1.png)

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

![img.png](img.png)

# 참고

- [matplotlib.pyplot — Matplotlib 3.5.3 documentation](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
