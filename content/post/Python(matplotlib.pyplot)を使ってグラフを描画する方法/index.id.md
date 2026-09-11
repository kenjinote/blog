---
title: 'Cara Menggambar Grafik dengan Python dan matplotlib [Sesuai dengan Google Colab]'
slug: "Python(matplotlib.pyplot)を使ってグラフを描画する方法"
date: 2023-04-09T01:02:19+09:00
tags: ["Python", "grafik", "matematika", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["Matematika, Kriptografi, Kuantum"]
description: 'Menjelaskan prosedur untuk pemula tentang cara dengan mudah menggambar dan menampilkan grafik gelombang sinus dan kosinus dengan pustaka matplotlib.pyplot milik Python menggunakan Google Colaboratory. Anda dapat langsung mencobanya tanpa perlu menyiapkan lingkungan.'
---

![img_1.png](img_1.webp)

# Prasyarat
- Akun Google

# Langkah-langkah

1. Akses [https://colab.research.google.com/](https://colab.research.google.com/)
2. Pilih "File" -> "Notebook baru"
3. Tempel dan jalankan kode berikut
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2*np.pi, 500)
plt.plot(x, np.sin(x), label="sin curve")
plt.plot(x, np.cos(x), label="cos curve")
plt.legend() # tampilkan legenda
plt.show()
```

# Hasil

![img.png](img.webp)

# Referensi

- [matplotlib.pyplot — Matplotlib 3.5.3 documentation](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
