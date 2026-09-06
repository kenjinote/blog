---
title: "LoadIcon tidak perlu memanggil DestroyIcon"
slug: "LoadIconはDestroyIconを呼び出す必要はない"
date: 2024-04-19T01:55:17+09:00
tags: ["ikon", "LoadIcon", "DestroyIcon", "pemrograman Windows"]
draft: false
categories: ["Pemrograman"]
---

# Tentang kebutuhan untuk memanggil DestroyIcon

Memanggil DestroyIcon diperlukan dalam kasus berikut:
 
- CreateIconFromResourceEx (jika dipanggil tanpa flag LR_SHARED)
- CreateIconIndirect 
- CopyIcon

Jika dibuat oleh fungsi-fungsi di atas.

- LoadIcon
- LoadImage (jika menggunakan flag LR_SHARED)
- CopyImage (jika menggunakan flag LR_COPYRETURNORG dan parameter hImage adalah ikon bersama)
- CreateIconFromResource
- CreateIconFromResourceEx (jika menggunakan flag LR_SHARED)

Ikon yang dibuat dan dimuat dalam kasus di atas tidak boleh memanggil DestroyIcon.

### Referensi
- [Fungsi DestroyIcon (winuser.h)](https://learn.microsoft.com/ja-JP/windows/win32/api/winuser/nf-winuser-destroyicon)
