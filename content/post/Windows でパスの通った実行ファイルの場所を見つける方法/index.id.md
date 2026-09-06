---
title: "Cara Menemukan Lokasi File Executable di Path Windows"
slug: "Windows でパスの通った実行ファイルの場所を見つける方法"
date: 2023-04-03T00:02:55+09:00
tags: ["Windows", "path", "file executable", "command prompt"]
draft: false
image: "img.png"
categories: ["PC & Gadget"]
---

# Cara Menemukan Lokasi File Executable di Path Windows

Saat menjalankan perintah dengan menentukan file executable, kadang-kadang Anda ingin tahu di mana file executable itu berada. Dalam kasus seperti itu, Anda dapat menggunakan perintah di bawah ini untuk memeriksa lokasi file executable.

```powershell
where <nama file executable>
```

Misalnya, jika Anda ingin mengetahui lokasi Paint (mspaint.exe), lakukan hal berikut:

```powershell
where mspaint.exe
```

# Referensi

- [How do I find the location of an executable in Windows?](https://superuser.com/questions/49104/how-do-i-find-the-location-of-an-executable-in-windows)
