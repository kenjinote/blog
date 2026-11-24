---
title: "Google Colab में Python और Matplotlib से ग्राफ़ बनाएँ"
slug: "Python(matplotlib.pyplot)を使ってग्राफを描画する方法"
tags: ["Python", "ग्राफ़", "गणित", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "Google Colab में NumPy और Matplotlib से 0 से 2π तक sine और cosine वक्र बनाएँ।"
date: "2023-04-09T01:02:19+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

यह उदाहरण Python, NumPy और Matplotlib के साथ Google Colab notebook में sine और cosine वक्र बनाता है। Colab का इंटरफ़ेस और menu नाम बदल सकते हैं, इसलिए मौजूदा इंटरफ़ेस से खाली notebook बनाएँ।

## आवश्यकताएँ

आपको Google Account और इंटरनेट कनेक्शन चाहिए। Colab के hosted runtime में स्थानीय कंप्यूटर पर Python environment सेट किए बिना code चलाया जा सकता है।

## Notebook cell चलाएँ

कोड को नए notebook के code cell में paste करके चलाएँ। x में 0 से 2π तक, दोनों सिरों सहित, समान दूरी वाले 500 मान हैं। ग्राफ़ radians में इन मानों के लिए sine और cosine दिखाता है और legend जोड़ता है।

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
plt.plot(x, np.sin(x), label="sin curve")
plt.plot(x, np.cos(x), label="cos curve")
plt.legend()
plt.show()
```

## उदाहरण परिणाम

Cell में sine और cosine वक्रों का ग्राफ़ दिखता है। यदि hosted runtime में कोई library उपलब्ध न हो, तो cell में `%pip install numpy matplotlib` चलाकर उदाहरण फिर चलाएँ।

![sine और cosine का ग्राफ़](img_1.webp)

![sine और cosine का ग्राफ़](img.webp)

## आधिकारिक संदर्भ

- [Matplotlib: pyplot](https://matplotlib.org/stable/api/pyplot_summary.html)
- [NumPy: linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
- [Google Colab: FAQ](https://research.google.com/colaboratory/faq.html?hl=en)
- [Open Google Colab](https://colab.research.google.com/)
