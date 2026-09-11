---
title: 'كيفية رسم الرسوم البيانية باستخدام Python و matplotlib 【متوافق مع Google Colab】'
slug: "Python(matplotlib.pyplot)を使ってグラフを描画する方法"
date: 2023-04-09T01:02:19+09:00
tags: ["Python", "رسوم بيانية", "رياضيات", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["الرياضيات، التشفير، الكم"]
description: 'نشرح للمبتدئين خطوات رسم وعرض رسوم الموجة الجيبية (Sine) وجيب التمام (Cosine) بسهولة باستخدام مكتبة matplotlib.pyplot في Python عبر Google Colaboratory. يمكنك تجربتها فوراً دون الحاجة لإعداد بيئة العمل.'
---

![img_1.png](img_1.webp)

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

![img.png](img.webp)

# المراجع

- [matplotlib.pyplot — Matplotlib 3.5.3 documentation](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
