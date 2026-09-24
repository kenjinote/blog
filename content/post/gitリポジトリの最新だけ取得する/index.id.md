---
title: 'Cara Hanya Mengambil Commit Terbaru dari Repositori dengan Git clone'
date: "2026-09-24T19:44:38+09:00"
slug: "gitRepositoriの最新だけ取得する"
date: 2024-04-27T02:54:12+09:00
tags: ["git", "repositori", "perintah"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Menjelaskan cara hanya mengambil commit terbaru (shallow clone) tanpa mengunduh seluruh riwayat repositori Git. Ini adalah teknik berguna untuk menghemat kapasitas disk dan mengkloning repositori dengan cepat menggunakan opsi ''--depth 1''.'
---

# Mendapatkan hanya versi terbaru dari repositori

Anda dapat mengambil hanya versi terbaru dari repositori dengan perintah berikut.
Ini berguna jika Anda ingin mengambil repositori dengan cepat untuk menghemat ruang disk.

```
git clone --depth 1 <URL repositori>
```
