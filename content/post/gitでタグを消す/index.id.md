---
title: "Menghapus tag di git"
slug: "gitでタグを消す"
date: 2022-10-02T02:18:04+09:00
tags: ["git"]
draft: false
image: "img.png"
categories: ["Alat & Lingkungan Pengembangan"]
---
# Menghapus tag lokal

1. Periksa tag yang ada di lokal dengan `git tag`.
2. Hapus tag dengan `git tag -d v0.1.0`. (Ganti `v0.1.0` dengan tag yang ingin Anda hapus)

# Menghapus tag jarak jauh (remote)

1. Periksa tag yang ada di jarak jauh dengan `git ls-remote --tags`.
2. Hapus tag yang ada di jarak jauh dengan `git push origin --delete v0.1.0`. (Ganti `v0.1.0` dengan tag yang ingin Anda hapus)

## Referensi
[Cara menghapus tag git secara lokal dan jarak jauh!](https://qumeru.com/magazine/528)
