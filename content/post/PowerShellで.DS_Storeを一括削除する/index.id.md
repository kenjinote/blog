---
title: "Menghapus massal .DS_Store dengan PowerShell"
slug: "PowerShellで.DS_Storeを一括削除する"
date: 2022-09-12T10:11:42+09:00
tags: ["PowerShell"]
draft: false
image: "img.png"
categories: ["Pemrograman"]
---

Pindahkan direktori saat ini ke folder target dan jalankan perintah berikut untuk menghapus file .DS_Store secara massal, termasuk dalam subfolder.

```powershell
Get-ChildItem . -include '.DS_Store' -Recurse -Force | Remove-Item -Force
```
