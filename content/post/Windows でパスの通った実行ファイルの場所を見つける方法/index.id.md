---
title: "Menemukan File Eksekusi Windows dengan where.exe dan PowerShell"
date: 2023-04-03T00:02:55+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Windows でJalurの通ったFile Eksekusiの場所を見つける方法"
tags: ["Windows", "path", "file executable", "command prompt"]
draft: false
image: "img.webp"
categories: ["windows", "terminal"]
description: "Cara mencari executable di PATH dengan where di Command Prompt atau where.exe dan Get-Command di PowerShell, termasuk alias dan cakupan pencarian."
---
## Command Prompt

Untuk menemukan lokasi executable yang dapat dipanggil sebagai perintah, gunakan `where` di Command Prompt. Di PowerShell, `where` adalah alias `Where-Object`; tulis `where.exe` untuk memanggil program eksternal secara eksplisit.

```cmd
where mspaint.exe
```

`where` mencari folder saat ini dan folder yang tercantum dalam variabel lingkungan `PATH`, lalu menampilkan lokasi yang cocok. Hasilnya bisa lebih dari satu. Perintah ini tidak mencari seluruh folder komputer atau aplikasi di luar lokasi tersebut.

## PowerShell

```powershell
where.exe mspaint.exe
Get-Command mspaint.exe -All
```

Di PowerShell, `Get-Command` menampilkan perintah yang akan dijalankan PowerShell beserta jalur executable-nya.

## Referensi resmi

- [Windows `where` command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/where)
- [PowerShell `Get-Command`](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-command?view=powershell-7.5)
- [PowerShell `Where-Object` (the `where` alias)](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-7.5)
