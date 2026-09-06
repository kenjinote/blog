---
title: "كيفية رسم الرسوم البيانية باستخدام Python (matplotlib.pyplot)"
slug: "كيفية-رسم-الرسوم-البيانية-باستخدام-python-matplotlib-pyplot"
date: 2023-04-09T01:02:19+09:00
tags: ["Python", "رسوم بيانية", "رياضيات", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.png"
categories: ["الرياضيات، التشفير، الكم"]
---

![img_1.png](img_1.png)

# المتطلبات
- حساب جوجل

# الخطوات

1. اذهب إلى [https://colab.research.google.com/](https://colab.research.google.com/)
2. اختر "ملف" -> "دفتر ملاحظات جديد"
3. الصق الكود التالي وقم بتشغيله
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2*np.pi, 500)
plt.plot(x, np.sin(x), label="sin curve")
plt.plot(x, np.cos(x), label="cos curve")
plt.legend() # إظهار وسيلة الإيضاح
plt.show()
```

# النتيجة

![img.png](img.png)

# المراجع

- [matplotlib.pyplot — Matplotlib 3.5.3 documentation](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
