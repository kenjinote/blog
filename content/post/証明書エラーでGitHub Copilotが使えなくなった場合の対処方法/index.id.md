---
title: "Mendiagnosis Error Sertifikat GitHub Copilot dengan Aman"
slug: "証明書エラーでGitHub Copilotが使えなくなった場合のPenanggulangan"
tags: ["GitHub Copilot", "certificates"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Periksa error sertifikat, proxy, dan ESET dengan aman tanpa melemahkan perlindungan TLS."
date: "2024-04-21T18:47:26+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Mendiagnosis Error Sertifikat GitHub Copilot dengan Aman

Error ini saja tidak membuktikan bahwa penyebabnya adalah ESET. Menurut GitHub, error semacam ini sering terkait proxy yang memeriksa TLS atau sertifikat khusus.

## Log berikut dicatat pada 21 April 2024. Teks lisensi menggambarkan insiden saat itu; lihat dokumentasi GitHub terkini untuk pengaturan jaringan saat ini.

Coba IDE yang sama di jaringan lain untuk mengetahui apakah masalah bergantung pada proxy atau VPN. Jika proxy perusahaan memeriksa TLS, minta administrator memeriksa rantai sertifikat dan memasang sertifikat CA resmi organisasi ke penyimpanan tepercaya OS. Jika memakai ESET, perbarui produk dan ikuti panduan perbaikan sertifikat. Aturan khusus aplikasi hanya dipertimbangkan jika pemeriksaan aplikasi itu dipastikan sebagai penyebab dan diizinkan kebijakan.

```text
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

## Jangan biarkan pemeriksaan SSL/TLS ESET dinonaktifkan dan jangan abaikan error sertifikat secara permanen. ESET menjelaskan bahwa penonaktifan mengurangi pemeriksaan ancaman pada lalu lintas terenkripsi; GitHub juga memperingatkan risiko keamanan jika error sertifikat diabaikan.

Error yang tercatat

## Pemeriksaan konektivitas

```powershell
curl.exe --verbose -i -L https://copilot-proxy.githubusercontent.com/_ping
```

Untuk menguji melalui proxy, ikuti sintaks GitHub dan tambahkan `-x http://HOST:PORT`.

## Tentang ESET

Pemeriksaan aman

> Sebelum membagikan log, hapus kredensial, nama pengguna dan kata sandi proxy, serta informasi pribadi.

## Referensi

- [GitHub Docs: Troubleshooting network errors](https://docs.github.com/en/copilot/how-tos/troubleshoot-copilot/troubleshoot-network-errors)
- [GitHub Docs: Copilot network settings](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/network-settings)
- [GitHub Docs: Configure network settings for JetBrains IDEs](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/configure-network-settings?tool=jetbrains)
- [ESET: Manage SSL/TLS protocol filtering](https://support.eset.com/en/kb3126-disable-ssl-filtering-in-eset-windows-products)
