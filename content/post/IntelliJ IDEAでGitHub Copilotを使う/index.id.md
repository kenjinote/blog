---
title: 'Cara Menginstal dan Mengaktifkan GitHub Copilot di IntelliJ IDEA'
slug: "IntelliJ IDEAでGitHub Copilotを使う"
date: 2022-09-10T09:44:55+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA","GitHub Copilot"]
draft: false
image: "images/img.webp"
categories: ["tools-development-environment"]
description: 'Pelajari cara memasang plugin GitHub Copilot di IntelliJ IDEA, masuk dengan GitHub, dan menggunakan saran kode inline. Panduan ini menjelaskan persyaratan akses serta alur autentikasi saat ini, dan menyertakan tautan ke petunjuk resmi.'
---
# Pendahuluan

Plugin GitHub Copilot menambahkan saran kode inline dan Copilot Chat ke IDE JetBrains. Panduan ini menjelaskan instalasi dasar dan proses masuk di IntelliJ IDEA. Nama menu dan tampilannya dapat berbeda menurut versi IDE dan plugin.

## Sebelum memulai

Anda memerlukan akun GitHub yang memiliki akses ke Copilot dan versi IntelliJ IDEA yang kompatibel. Copilot Free memiliki batas penggunaan; paket berbayar menyediakan akses lebih luas. Paket dan kompatibilitas dapat berubah, jadi periksa dokumentasi resmi terbaru.

## Memasang plugin

1. Buka pengaturan Plugins. Di Windows atau Linux, pilih **File > Settings > Plugins**. Di macOS, pilih **IntelliJ IDEA > Settings > Plugins**.
2. Di Marketplace, cari **GitHub Copilot**, lalu klik **Install** pada plugin yang disediakan GitHub.
3. Mulai ulang IDE setelah instalasi selesai.

## Masuk ke GitHub

1. Buka **Tools > GitHub Copilot > Login to GitHub**.
2. Pada dialog masuk, klik **Copy and Open**. Browser akan terbuka.
3. Masuk ke GitHub di browser, tempel kode perangkat yang ditampilkan IDE, lalu klik **Continue**.
4. Tinjau izin yang diminta dan pilih **Authorize GitHub Copilot Plugin**. Kembali ke IDE dan klik **OK** pada layar konfirmasi.

## Menggunakan saran kode

Mulailah mengetik di editor. Copilot menampilkan saran dengan teks berwarna abu-abu; tekan **Tab** untuk menerimanya. Periksa saran sebelum digunakan karena saran dibuat berdasarkan konteks dan mungkin perlu diubah. Buka ikon GitHub Copilot Chat di sisi kanan IDE untuk memulai percakapan.

Menu dan fitur dapat berubah. Lihat dokumentasi resmi untuk langkah dan informasi kompatibilitas terbaru.

## Referensi

- [Memasang plugin dan masuk](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [Mendapatkan saran kode di JetBrains](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [Plugin GitHub Copilot di JetBrains Marketplace](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
