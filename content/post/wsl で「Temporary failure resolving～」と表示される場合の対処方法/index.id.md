---
title: "Cara mengatasi “Temporary failure resolving” di WSL"
slug: "wsl で「Temporary failure resolving～」と表示される場合のPenanggulangan"
tags: ["WSL", "DNS", "troubleshooting"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Pisahkan masalah resolusi nama di WSL dari masalah jaringan Windows, lalu periksa pembaruan WSL, DNS tunneling, VPN, dan firewall."
date: "2024-03-31T16:57:33+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Cara mengatasi “Temporary failure resolving” di WSL

Kesalahan ini berarti WSL tidak dapat menerjemahkan nama host menjadi alamat IP. Pengaturan server DNS hanyalah salah satu kemungkinan penyebab. Tentukan terlebih dahulu apakah kegagalan terjadi di Windows, WSL, atau keduanya.

## Lakukan pemeriksaan ini terlebih dahulu

1. Di Windows PowerShell, jalankan `Resolve-DnsName archive.ubuntu.com`. Jika gagal juga di Windows, periksa jaringan Windows, DNS, dan VPN terlebih dahulu.

2. Di WSL, jalankan `getent hosts archive.ubuntu.com`. Jika Windows dapat meresolusi nama tetapi WSL tidak, lanjutkan dengan langkah berikut.

Di PowerShell, jalankan `wsl --update`, lalu `wsl --shutdown`. Buka WSL kembali dan coba `getent hosts archive.ubuntu.com` serta `sudo apt update`.

Pada Windows 11 versi 22H2 ke atas, WSL versi terbaru mengaktifkan DNS tunneling secara default. Jika resolusi nama gagal saat menggunakan VPN, perbarui WSL dan pastikan `dnsTunneling=true` tidak dinonaktifkan di bagian `[wsl2]` pada `.wslconfig`. Setelah mengubah pengaturan, jalankan `wsl --shutdown` di PowerShell.

Jangan langsung menetapkan DNS publik sembarang seperti `8.8.8.8` di `/etc/resolv.conf`. Ini dapat melewati kebijakan DNS VPN atau organisasi dan berbenturan dengan pengaturan otomatis WSL. Jika lingkungan Anda memerlukan penggantian manual, ikuti petunjuk khusus VPN dari Microsoft dan tanyakan kepada administrator jaringan.

## Jika masalah berlanjut

Jika masalah berlanjut, periksa VPN, Windows Firewall, perangkat lunak keamanan, dan kebijakan jaringan organisasi. Jika resolusi nama berhasil tetapi `apt update` gagal, periksa juga proxy, mirror, dan konfigurasi repositori.

```powershell
Resolve-DnsName archive.ubuntu.com
wsl --update
wsl --shutdown
```

```bash
getent hosts archive.ubuntu.com
sudo apt update
```

## Referensi

- [Microsoft Learn: WSL troubleshooting](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting)
- [Microsoft Learn: WSL networking and DNS tunneling](https://learn.microsoft.com/en-us/windows/wsl/networking)
- [Microsoft Learn: WSL configuration](https://learn.microsoft.com/en-us/windows/wsl/wsl-config)
