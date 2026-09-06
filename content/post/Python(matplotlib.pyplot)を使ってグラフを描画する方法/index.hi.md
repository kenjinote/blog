---
title: "Python (matplotlib.pyplot) का उपयोग करके ग्राफ़ कैसे बनाएं"
slug: "Python (matplotlib.pyplot) का उपयोग करके ग्राफ़ कैसे बनाएं"
date: 2023-04-09T01:02:19+09:00
tags: ["Python", "ग्राफ़", "गणित", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.png"
categories: ["गणित・क्रिप्टोग्राफी・क्वांटम"]
---

![img_1.png](img_1.png)

# आपको क्या चाहिए
- Google खाता

# चरण

1. [https://colab.research.google.com/](https://colab.research.google.com/) पर जाएं
2. "फ़ाइल" -> "नई नोटबुक" चुनें
3. नीचे दिए गए कोड को पेस्ट करें और चलाएं
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2*np.pi, 500)
plt.plot(x, np.sin(x), label="sin curve")
plt.plot(x, np.cos(x), label="cos curve")
plt.legend() # लीजेंड दिखाएं
plt.show()
```

# निष्पादन परिणाम

![img.png](img.png)

# संदर्भ

- [matplotlib.pyplot — Matplotlib 3.5.3 documentation](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
