---
title: "Menghapus File .DS_Store dengan Aman Secara Massal menggunakan PowerShell"
slug: "PowerShellで.DS_Storeを一括削除する"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Tentukan folder root secara eksplisit, tinjau file tersembunyi yang cocok, dan pratinjau penghapusan dengan WhatIf sebelum menghapusnya."
date: "2022-09-12T10:11:42+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Jika file `.DS_Store` buatan macOS tertinggal di folder Windows, Anda dapat menghapusnya dengan PowerShell. Agar cakupannya terkendali, tentukan folder target, periksa jalur lengkap yang cocok, lalu pratinjau operasi menggunakan `-WhatIf` sebelum menghapus apa pun.

## Daftarkan kecocokan dan pratinjau tindakan

Ganti `$root` dengan jalur absolut folder yang ingin dibersihkan. `-LiteralPath` mencegah karakter pada jalur root ditafsirkan sebagai wildcard; `-Filter` memilih item bernama `.DS_Store`. `-File` mengecualikan folder dengan nama tersebut. `-Recurse` mencari subfolder, sedangkan `-Force` menyertakan item tersembunyi.

```powershell
$root = 'C:\path\to\target-folder'

$files = @(
    Get-ChildItem -LiteralPath $root -Filter '.DS_Store' -File -Recurse -Force -ErrorAction Stop
)

# Review the exact files that matched.
$files | Select-Object -ExpandProperty FullName

# Preview the deletion; this does not remove files.
$files | ForEach-Object {
    Remove-Item -LiteralPath $_.FullName -Force -WhatIf
}
```

## Hapus hanya setelah diperiksa

Keluaran pertama mencantumkan jalur lengkap file kandidat. `-WhatIf` berikutnya menampilkan rencana penghapusan tanpa menjalankannya. Setelah daftar dan pratinjau dipastikan benar, hapus `-WhatIf` dari baris `Remove-Item` yang sama lalu jalankan.

## Cakupan dan izin

Contoh ini menargetkan file bernama `.DS_Store` di bawah root yang dipilih. Root yang keliru dapat membuat file di seluruh cakupan tersebut ikut terpilih. `-Force` tidak melewati izin akses. Jika akses ditolak, periksa jalur dan izin Anda.

## Referensi Microsoft

- [Microsoft: Get-ChildItem](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem)
- [Microsoft: Remove-Item](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/remove-item)
- [Microsoft: PowerShell common parameters, including WhatIf](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_commonparameters)
