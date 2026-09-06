---
title: "Penghapusan Massal Cepat untuk Folder Besar"
slug: "penghapusan-massal-cepat-untuk-folder-besar"
date: 2022-09-20T16:04:02+09:00
tags: ["Command Prompt"]
draft: false
image: "img.png"
categories: ["TI dan Teknologi"]
---
## Penghapusan Massal Cepat untuk Folder Besar
Saat menghapus folder besar di File Explorer, kecepatannya lambat karena isi folder dipindai sepenuhnya terlebih dahulu sebelum penghapusan dijalankan.
Jika Anda menghapus dengan menggunakan perintah seperti di bawah ini, pemindaian dan penghapusan akan dijalankan secara bersamaan, sehingga Anda dapat menghapus folder besar dengan cepat.

1. Di Command Prompt, arahkan ke hierarki folder target.
2. Jalankan `DEL /F /Q /S NamaFolder > NUL`.
3. Jalankan `RMDIR /Q /S NamaFolder`.
