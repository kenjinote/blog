---
title: "【HUGO】Pratinjau Tampilan di Lingkungan Lokal"
slug: "【HUGO】ローカルで環境で表示プレビュー"
date: 2022-09-05T12:28:01+09:00
tags: ["HUGO"]
draft: false
image: "img.png"
categories: ["ブログ運営"]
---
# Instalasi HUGO

## Unduhan
[Unduh HUGO](https://github.com/gohugoio/hugo/releases)

Dari situs web di atas, unduh dan ekstrak modul Windows yang sesuai dengan lingkungan Anda.
Dalam kasus saya, saya mengunduh "hugo_0.102.3_Windows-64bit.zip".

## Ekstrak
Ekstrak file zip yang diunduh dan salin hugo.exe di dalamnya ke direktori yang Anda buat, misalnya C:\bin.

## Daftarkan ke Variabel Lingkungan
Daftarkan ke variabel lingkungan untuk menjalankan hugo.exe dari lokasi mana pun.
Ini adalah operasi di Windows 11, tetapi Anda dapat mendaftarkannya dengan prosedur berikut.

1. Tekan tombol Win+Pause untuk membuka Tentang.
2. Klik Pengaturan sistem lanjutan.
3. Klik Variabel Lingkungan.
4. Pilih Path dan klik Edit.
5. Klik Baru, masukkan "C:\bin" di baris baru, dan klik OK untuk menutup dialog.
 
# Pratinjau Blog
Pergi ke folder blog HUGO di Command Prompt dan jalankan perintah berikut.

`hugo server -D`

Hasil eksekusinya ada di bawah. (-D adalah opsi untuk menampilkan artikel draf.)

```
C:\Users\win11\IdeaProjects\kenji.blog>hugo server -D
Start building sites …
hugo v0.102.3-b76146b129d7caa52417f8e914fc5b9271bf56fc windows/amd64 BuildDate=2022-09-01T10:16:19Z VendorInfo=gohugoio

                   | JA
-------------------+-----
  Pages            | 39
  Paginator pages  |  0
  Non-page files   |  7
  Static files     |  0
  Processed images |  0
  Aliases          | 13
  Sitemaps         |  1
  Cleaned          |  0

Built in 161 ms
Watching for changes in C:\Users\win11\IdeaProjects\kenji.blog\{archetypes,content,themes}
Watching for config changes in C:\Users\win11\IdeaProjects\kenji.blog\config.toml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```

Alamat akan ditampilkan pada saat eksekusi (dalam contoh di atas, `http://localhost:1313/`), jadi salin alamat tersebut ke browser Anda.
Pratinjau akan diperbarui secara otomatis setiap kali file disimpan.
Untuk mengakhiri pratinjau, masukkan Ctrl+C di command prompt.
