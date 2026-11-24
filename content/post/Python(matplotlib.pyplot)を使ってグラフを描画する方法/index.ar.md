---
title: "رسم الرسوم البيانية باستخدام Python وMatplotlib في Google Colab"
slug: "Python(matplotlib.pyplot)を使ってرسم بيانيを描画する方法"
tags: ["Python", "رسوم بيانية", "رياضيات", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "استخدم NumPy وMatplotlib في Google Colab لرسم منحنيي الجيب وجيب التمام من 0 إلى 2π."
date: "2023-04-09T01:02:19+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

يعرض هذا المثال رسم منحنيي الجيب وجيب التمام في دفتر Google Colab باستخدام Python وNumPy وMatplotlib. قد تتغير واجهة Colab وأسماء القوائم؛ أنشئ دفتراً فارغاً من الواجهة الحالية.

## المتطلبات

تحتاج إلى حساب Google واتصال بالإنترنت. يتيح وقت التشغيل المستضاف في Colab تنفيذ التعليمات البرمجية دون إعداد بيئة Python محلية.

## تشغيل خلية الدفتر

الصق التعليمات البرمجية في خلية جديدة وشغّلها. يحتوي x على 500 قيمة متساوية التباعد من 0 إلى 2π، مع تضمين الطرفين. يرسم المخطط الجيب وجيب التمام لهذه القيم بالراديان ويعرض وسيلة إيضاح.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
plt.plot(x, np.sin(x), label="sin curve")
plt.plot(x, np.cos(x), label="cos curve")
plt.legend()
plt.show()
```

## نتيجة المثال

تعرض الخلية مخططاً لمنحنيي الجيب وجيب التمام. إذا لم تتوفر مكتبة في وقت التشغيل المستضاف، فنفّذ `%pip install numpy matplotlib` في خلية ثم أعد تشغيل المثال.

![رسم منحنيي الجيب وجيب التمام](img_1.webp)

![رسم منحنيي الجيب وجيب التمام](img.webp)

## مراجع رسمية

- [Matplotlib: pyplot](https://matplotlib.org/stable/api/pyplot_summary.html)
- [NumPy: linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
- [Google Colab: FAQ](https://research.google.com/colaboratory/faq.html?hl=en)
- [Open Google Colab](https://colab.research.google.com/)
