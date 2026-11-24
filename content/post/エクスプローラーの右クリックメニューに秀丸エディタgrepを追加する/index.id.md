---
title: 'Cara Menambahkan Fitur grep Hidemaru Editor ke Menu Klik Kanan di Windows'
date: 2024-04-03T00:00:46+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "PenjelajahのMenu Klik KananにEditor Hidemarugrepを追加する"
tags: ["Hidemaru Editor", "File Explorer", "Menu klik kanan", "grep", "Registry"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Memperkenalkan langkah pengaturan yang berguna untuk menambahkan fitur grep Hidemaru Editor ke menu klik kanan di Explorer pada Windows 10/11. Menjelaskan cara mudahnya dengan jelas, menggunakan file pendaftaran registri.'
---
Kami akan menunjukkan cara menambahkan fungsi grep dari Hidemaru Editor ke menu klik kanan di File Explorer pada Windows 10/11.

**※ Harap perhatikan bahwa langkah-langkah berikut melibatkan modifikasi registry, jadi lakukan dengan risiko Anda sendiri.**

File ini hanya menambahkan perintah menu folder untuk pengguna saat ini; tidak menambahkan “Buka dengan Hidemaru” ke semua file atau mengubah pengaturan seluruh komputer. Sebelum mengimpornya, buka dengan Notepad dan periksa atau sesuaikan jalur program. Jika kunci tujuan sudah ada, ekspor dahulu melalui Registry Editor (File > Export). Di Windows 11, perintah lama mungkin berada di “Show more options”. Dukungan Windows 10 berakhir pada 14 Oktober 2025. File penghapusan yang disertakan hanya menghapus entri pengguna saat ini; file ini tidak membatalkan pendaftaran lama untuk seluruh komputer. Jika Anda mengimpor file sebelumnya, periksa dan hapus kuncinya secara terpisah di Registry Editor.
## Langkah-langkah

1. Buka tautan di bawah ini dan simpan ke folder mana saja.

[Registrasi_Registry_Hidemaru.reg](秀丸レジストリ登録.reg)

[Hapus entri registry Hidemaru](秀丸レジストリ解除.reg)

2. Klik ganda file `Registrasi_Registry_Hidemaru.reg` untuk menambahkannya ke dalam registry.

## Referensi

- [Menjalankan grep Hidemaru dari menu klik kanan folder](https://aimek-developer.blogspot.com/2019/02/grep.html)

## Referensi resmi

- [Hidemaru startup options](https://help.maruo.co.jp/hidemaru/html/230_Option.html)
- [Microsoft: Back up and restore the registry](https://support.microsoft.com/en-us/windows/experience/backup-recovery/how-to-back-up-and-restore-the-registry-in-windows)
- [Microsoft: File Explorer context menu](https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows)
- [Microsoft: Windows 10 end of support](https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/windows-10-support-has-ended-on-october-14-2025)
- [Microsoft: reg import](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg-import)
