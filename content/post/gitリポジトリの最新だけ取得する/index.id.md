---
title: 'Cara mengkloning repositori Git dengan riwayat dangkal'
slug: "gitRepositoriの最新だけ取得する"
date: 2024-04-27T02:54:12+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["git", "repositori", "perintah"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Pelajari data yang diambil git clone --depth 1, cara memilih branch, dan cara mengambil riwayat tambahan.'
---

# Mengkloning repositori dengan riwayat dangkal

`git clone --depth 1` membuat shallow clone dengan kedalaman riwayat satu dari ujung branch yang dipilih. Secara default, branch yang dipilih adalah branch default remote. Cara ini mengurangi riwayat commit yang ditransfer, tetapi Git tetap mengunduh berkas saat ini dan objek yang diperlukan; jadi repositori dengan berkas besar tetap bisa berukuran besar.

```sh
git clone --depth 1 <repository-url>
```

Untuk memilih branch secara eksplisit, cantumkan namanya:

```sh
git clone --depth 1 --single-branch --branch <branch> <repository-url>
```

Anda dapat mengambil riwayat tambahan nanti, misalnya:

```sh
git -C <directory> fetch --deepen=50 origin <branch>
```

Ganti `<directory>` dan `<branch>` dengan nama yang digunakan. Dengan `--depth`, Git juga mengaktifkan `--single-branch` kecuali perilaku itu diubah. Lihat manual resmi [`git clone`](https://git-scm.com/docs/git-clone) dan [`git fetch`](https://git-scm.com/docs/git-fetch), termasuk opsi `--unshallow`.
