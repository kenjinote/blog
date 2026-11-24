---
title: "Membuat Grafik dengan Python dan Matplotlib di Google Colab"
slug: "Python(matplotlib.pyplot)を使ってGrafikを描画する方法"
tags: ["Python", "grafik", "matematika", "matplotlib", "pyplot", "Google Colaboratory"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "Gunakan NumPy dan Matplotlib di Google Colab untuk menggambar kurva sinus dan kosinus dari 0 hingga 2π."
date: "2023-04-09T01:02:19+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Contoh ini menggambar kurva sinus dan kosinus di notebook Google Colab menggunakan Python, NumPy, dan Matplotlib. Antarmuka dan nama menu Colab dapat berubah; buat notebook kosong melalui antarmuka saat ini.

## Persyaratan

Anda memerlukan Akun Google dan koneksi internet. Dengan runtime yang di-host Colab, kode dapat dijalankan tanpa menyiapkan lingkungan Python lokal.

## Jalankan sel notebook

Tempelkan kode ke sel kode di notebook baru, lalu jalankan sel tersebut. x berisi 500 nilai berjarak sama dari 0 hingga 2π, termasuk kedua ujungnya. Grafik menghitung sinus dan kosinus untuk nilai dalam radian itu serta menampilkan legenda.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
plt.plot(x, np.sin(x), label="sin curve")
plt.plot(x, np.cos(x), label="cos curve")
plt.legend()
plt.show()
```

## Contoh hasil

Sel akan menampilkan grafik kurva sinus dan kosinus. Jika pustaka tidak tersedia di runtime yang di-host, jalankan `%pip install numpy matplotlib` di sebuah sel, lalu jalankan ulang contoh.

![Grafik sinus dan kosinus](img_1.webp)

![Grafik sinus dan kosinus](img.webp)

## Referensi resmi

- [Matplotlib: pyplot](https://matplotlib.org/stable/api/pyplot_summary.html)
- [NumPy: linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
- [Google Colab: FAQ](https://research.google.com/colaboratory/faq.html?hl=en)
- [Open Google Colab](https://colab.research.google.com/)
