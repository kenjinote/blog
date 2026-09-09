---
title: 'Cara Menghapus Tag Lokal dan Remote di Git'
slug: "gitでタグを消す"
date: 2022-10-02T02:18:04+09:00
tags: ["git"]
draft: false
image: "img.webp"
categories: ["Alat & Lingkungan Pengembangan"]
description: 'Menjelaskan dengan sederhana cara menghapus tag yang tidak diperlukan di Git. Mencakup mulai dari penghapusan tag di lingkungan lokal menggunakan ''git tag -d'' hingga penghapusan tag di repositori remote menggunakan ''git push origin --delete''.'
---
# Menghapus tag lokal

1. Periksa tag yang ada di lokal dengan `git tag`.
2. Hapus tag dengan `git tag -d v0.1.0`. (Ganti `v0.1.0` dengan tag yang ingin Anda hapus)

# Menghapus tag jarak jauh (remote)

1. Periksa tag yang ada di jarak jauh dengan `git ls-remote --tags`.
2. Hapus tag yang ada di jarak jauh dengan `git push origin --delete v0.1.0`. (Ganti `v0.1.0` dengan tag yang ingin Anda hapus)

## Referensi
[Cara menghapus tag git secara lokal dan jarak jauh!](https://qumeru.com/magazine/528)
