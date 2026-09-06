---
title: "Cara Menghasilkan Gambar Ilustrasi Menggunakan AI (StableDiffusion)"
slug: "cara-menghasilkan-gambar-ilustrasi-menggunakan-ai-stablediffusion"
date: 2023-04-06T00:43:19+09:00
tags: ["AI", "Stable Diffusion", "ilustrasi", "generasi gambar", "Google Colaboratory"]
draft: false
image: "img.png"
categories: ["Pemrograman"]
---

# Apa itu Stable diffusion
Stable diffusion adalah AI yang menghasilkan gambar dari informasi teks yang dimasukkan, dikembangkan oleh tim peneliti di Universitas Munich di Jerman.
Dengan melatihnya pada berbagai gambar, ia dapat menghasilkan berbagai gambar mulai dari foto realistis hingga ilustrasi.

Kali ini, saya akan memperkenalkan cara menghasilkan gambar ilustrasi menggunakan data pra-terlatih dari Stable diffusion.

# Yang perlu disiapkan

- Akun Google

Hanya itu

# Langkah-langkah pembuatan

1. Buka https://colab.research.google.com
2. Dari menu `File` di kiri atas, pilih `Buku catatan baru`
3. Dari menu `Edit`, pilih `Setelan buku catatan`
4. Ubah `Akselerator hardware` menjadi `GPU`
![img_2.png](img_2.png)
5. Tempelkan kode berikut dan jalankan
```
!pip install diffusers==0.8.0 transformers
```
6. Tempelkan kode berikut dan jalankan
```
from diffusers import StableDiffusionPipeline
```
7. Tempelkan kode berikut dan jalankan
```
pipe = StableDiffusionPipeline.from_pretrained("gsdf/Counterfeit-V2.5")
pipe.to("cuda")
```
8. Tempelkan kode berikut dan jalankan
```
prompt = "((masterpiece,best quality)),1girl, solo, animal ears, rabbit, barefoot, knees up, dress, sitting, rabbit ears, short sleeves, looking at viewer, grass, short hair, smile, white hair, puffy sleeves, outdoors, puffy short sleeves, bangs, on ground, full body, animal, white dress, sunlight, brown eyes, dappled sunlight, day, depth of field"
n_prompt = "EasyNegative, extra fingers,fewer fingers"

image = pipe(prompt, negative_prompt = n_prompt).images[0]
image
```

`Prompt` yang digunakan di sini didasarkan pada `Prompt` dari [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5).

## Hasil pembuatan (beberapa)
![img_1.png](img_1.png)

![img_3.png](img_3.png)

![img_4.png](img_4.png)

## Referensi

- [https://huggingface.co/gsdf/Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5)
- [Saya mencoba membuat program penghasil gambar menggunakan Kecerdasan Buatan (AI) dalam 15 menit 【Pemrograman Langsung】](https://www.youtube.com/watch?v=l8-fVSM2PVQ)
