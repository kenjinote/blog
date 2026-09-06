---
title: "Mendapatkan hanya versi terbaru dari repositori git"
slug: "gitリポジトリの最新だけ取得する"
date: 2024-04-27T02:54:12+09:00
tags: ["git", "repositori", "perintah"]
draft: false
image: "img.png"
categories: ["Alat & Lingkungan Pengembangan"]
---

# Mendapatkan hanya versi terbaru dari repositori

Anda dapat mengambil hanya versi terbaru dari repositori dengan perintah berikut.
Ini berguna jika Anda ingin mengambil repositori dengan cepat untuk menghemat ruang disk.

```
git clone --depth 1 <URL repositori>
```
