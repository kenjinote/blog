---
title: 'Cara Menghapus Folder Besar Secara Masal dan Cepat di Windows [Command Prompt]'
slug: "大きなフォルダーを高速一括削除"
date: 2022-09-20T16:04:02+09:00
tags: ["Command Prompt"]
draft: false
image: "img.webp"
categories: ["TI dan Teknologi"]
description: 'Kami akan menjelaskan cara menghapus folder berukuran besar secara cepat dan masal di lingkungan Windows. Pekerjaan penghapusan yang memakan waktu di File Explorer dapat dipercepat secara drastis dengan memanfaatkan perintah DEL dan RMDIR di Command Prompt.'
---
## Penghapusan Massal Cepat untuk Folder Besar
Saat menghapus folder besar di File Explorer, kecepatannya lambat karena isi folder dipindai sepenuhnya terlebih dahulu sebelum penghapusan dijalankan.
Jika Anda menghapus dengan menggunakan perintah seperti di bawah ini, pemindaian dan penghapusan akan dijalankan secara bersamaan, sehingga Anda dapat menghapus folder besar dengan cepat.

1. Di Command Prompt, arahkan ke hierarki folder target.
2. Jalankan `DEL /F /Q /S NamaFolder > NUL`.
3. Jalankan `RMDIR /Q /S NamaFolder`.
