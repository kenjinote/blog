---
title: "Menghapus Folder Besar lewat Command Prompt Windows: Langkah dan Risiko"

slug: "大きなフォルダーを高速一括削除"
date: 2022-09-20T16:04:02+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Command Prompt"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Metode terdokumentasi Microsoft untuk menghapus folder dengan DEL dan RMDIR, termasuk risiko penghapusan rekursif senyap, pemeriksaan jalur, dan pencadangan."
---
Perintah ini menghapus file dan subfolder di dalam target secara rekursif. `/Q` meniadakan konfirmasi. Target yang keliru dapat menyebabkan kehilangan data yang tidak dapat dipulihkan; cadangkan data penting dan periksa jalur induk serta nama folder sebelum menjalankan penghapusan. Kecepatan bergantung pada jumlah file dan media penyimpanan, jadi tidak dijamin lebih cepat.

## Langkah

Dalam contoh ini, `C:\Parent` adalah folder induk dan `Large Folder` adalah folder yang akan dihapus. Tampilkan dan periksa target terlebih dahulu, lalu hapus.

```bat
cd /d "C:\Parent"
dir /a "Large Folder"
DEL /F /Q /S "Large Folder\*" > NUL
RMDIR /S /Q "Large Folder"
```

`DEL /F /Q /S` menghapus file di dalam target (`/F` mencakup file hanya-baca, `/Q` meniadakan konfirmasi, dan `/S` mencakup subfolder). Setelah itu, `RMDIR /S /Q` menghapus seluruh pohon direktori tanpa konfirmasi. Ganti `C:\Parent` dan `Large Folder` dengan nilai sebenarnya, lalu periksa hasil `dir` sebelum menjalankan perintah penghapusan.

## Microsoft documentation

- [del command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/del)
- [rmdir command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/rmdir)
