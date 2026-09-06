---
title: "Kumpulan Pintasan dan Trik Kecil Windows"
slug: "Windows のショートカット・小技集"
date: 2022-09-18T23:49:29+09:00
tags: ["Windows", "Trik", "Pintasan"]
draft: false
image: "img.png"
categories: ["PC・Gadget"]
---
Berikut adalah kumpulan trik kecil yang biasa digunakan di Windows. Saya akan sangat senang jika pengguna baru Windows membacanya.
Meskipun ini ditujukan untuk Windows 11, banyak di antaranya yang mungkin juga bisa digunakan di Windows 10.

## Menutup Jendela
- `Alt + F4` saat jendela aktif
- `Ctrl + W` saat jendela aktif. Menutup tab atau jendela (hanya aplikasi yang didukung)
- Klik ganda ikon di sebelah kiri bilah judul jendela
- Klik `×` pada bilah judul jendela

## Menampilkan Desktop
- `Win + D`. Menekannya dua kali akan mengembalikan jendela ke keadaan semula. Berguna ketika Anda ingin menampilkan desktop hanya untuk sesaat.
- `Win + M`. Meminimalkan semua aplikasi. Menekannya dua kali tidak akan mengembalikannya.

## Input Suara
- `Win + H`. Memulai input suara. Untuk mengakhiri input suara, tekan `Esc` atau `Win + H` lagi.

## Menampilkan Menu Klik Kanan Klasik di Explorer
- Tekan `Shift + F10` atau tombol aplikasi. Tombol aplikasi adalah tombol yang terletak di bagian kanan bawah keyboard.

## Memilih Area dan Menangkap Layar
- Anda dapat memilih area dan menangkap layar dengan `Win + Shift + S`.
- Anda dapat menangkap seluruh layar dengan `Win + Print Screen` atau hanya `Print Screen`.
(Jika Anda menambahkan `Win`, gambar tangkapan akan disimpan di `C:\Users\NamaPengguna\Pictures\Screenshots`.)
- Anda dapat menangkap jendela saat ini dengan `Alt + Print Screen`.

## Menjalankan Aplikasi yang Terdaftar di Taskbar
- Anda dapat menjalankan aplikasi yang terdaftar di taskbar dengan `Win + Tombol Angka`.  
  Misalnya, menekan `Win + 1` akan menjalankan aplikasi pertama dari kiri di taskbar.
- Anda dapat memindahkan fokus ke ikon taskbar dengan `Win + T`, dan menekan `Win + T` beberapa kali berturut-turut,
  atau menggunakan `←` atau `→` untuk memindahkan pilihan, lalu tekan `Enter` untuk menjalankan aplikasi yang dipilih.

## Memperbesar / Memperkecil
- `Win + +` akan meluncurkan Kaca Pembesar Windows. Kemudian `Win + + atau -` dapat memperbesar/memperkecil layar.
- Di Notepad atau browser, Anda dapat memperbesar/memperkecil dengan `Ctrl + + atau -` (hanya aplikasi yang didukung).

## Mengunci Windows
- `Win + L`
- `Ctrl + Alt + Del` → `Space` atau `Enter`

## Mematikan Windows (Shutdown)
- Saat desktop ditampilkan dengan `Win + M` atau `Win + D`, atau saat taskbar aktif dengan `Win + T` atau `Win + B`, tekan `Alt + F4`. Dialog berikut akan muncul, pastikan "Shut down" dipilih, lalu tekan `Enter`.
  Bisa juga dengan `Win + R` → `Alt + F4` → `Alt + F4`.
  ![img_20.png](img_20.png)
- Anda bisa mematikan dengan `Win + X` → `U` → `U`.
- Memasukkan `shutdown /s /t 0` di Command Prompt atau "Run" (`Win + R`) akan mematikan komputer. Menambahkan `/f` akan memaksanya mati (force shutdown).

## Memulai Ulang Windows (Restart)
- Saat desktop ditampilkan dengan `Win + M` atau `Win + D`, atau saat taskbar aktif dengan `Win + T` atau `Win + B`, tekan `Alt + F4`. Dialog berikut akan muncul, tekan `↓` satu kali untuk memilih "Restart", lalu tekan `Enter`.
  Bisa juga dengan `Win + R` → `Alt + F4` → `Alt + F4`.
  ![img_21.png](img_21.png)
- Anda bisa memulai ulang dengan `Win + X` → `U` → `R`.
- Anda bisa memulai ulang dengan `shutdown /r /t 0`. Menambahkan `/f` akan memaksanya memulai ulang (force restart).

## Mode Tidur Windows (Sleep)
- Saat desktop ditampilkan dengan `Win + M` atau `Win + D`, atau saat taskbar aktif dengan `Win + T` atau `Win + B`, tekan `Alt + F4`. Dialog berikut akan muncul, tekan `↑` satu kali untuk memilih "Sleep", lalu tekan `Enter`.
  Bisa juga dengan `Win + R` → `Alt + F4` → `Alt + F4`.
  ![img_23.png](img_23.png)
- Anda dapat mengubah ke status hibernasi (Hibernate) dengan memasukkan `rundll32.exe powrprof.dll,SetSuspendState` di `Win + R` atau Command Prompt.

## Keluar dari Windows (Sign out / Log off)
- Saat desktop ditampilkan dengan `Win + M` atau `Win + D`, atau saat taskbar aktif dengan `Win + T` atau `Win + B`, tekan `Alt + F4`. Dialog berikut akan muncul, tekan `↑` dua kali untuk memilih "Sign out", lalu tekan `Enter`.
  Bisa juga dengan `Win + R` → `Alt + F4` → `Alt + F4`.
  ![img_22.png](img_22.png)
- `Win + X` → `U` → `I`
- `Ctrl + Alt + Del` → `Tab` 2 kali atau `↓` 2 kali → `Enter` atau `Space`
- Anda bisa keluar (log off) dengan mengetik `logoff`.

## Memindahkan Jendela Menggunakan Keyboard
- `Win + ←` : Pindah ke kiri
- `Win + →` : Pindah ke kanan
- `Win + ↑` : Pindah ke atas / Maksimalkan
- `Win + ↓` : Pindah ke bawah / Minimalkan
- `Win + Shift + ← atau →` : Pindah antar monitor ganda
- `Win + Alt + ← atau → atau ↑ atau ↓` : Memindahkan jendela tanpa memaksimalkan atau meminimalkan
- Saat tidak diminimalkan, tekan `Alt + Space` lalu `M`, lalu pindahkan menggunakan tombol panah.  
*Karena jendela akan mengikuti kursor mouse, Anda dapat menyelamatkan jendela meskipun ditampilkan di luar layar.

## Mengakhiri Proses di Task Manager
![img_24.png](img_24.png)
1. Anda dapat membuka Task Manager dengan `Ctrl + Shift + Esc`.
2. Anda dapat beralih tab dengan `Ctrl + Tab`.
3. Setelah menekan `Tab` pada tab `Details` (Detail), Anda dapat mencari proses berdasarkan awalan dengan mengetikkan huruf di keyboard.
4. Saat nama proses dipilih, Anda dapat mengakhiri proses tersebut dengan menekan tombol `Delete` lalu `Enter`.

## Mengakhiri Proses Berdasarkan Nama Menggunakan Perintah
- Anda dapat mengakhiri proses dengan `taskkill /f /im namaproses`.
Misalnya, Anda dapat mengakhiri Explorer dengan `taskkill /f /im explorer.exe`.

## Menjalankan Beberapa Program yang Sama dari Ikon Taskbar
- Jika Anda mengklik kiri sambil menekan tombol `Shift` di taskbar, Anda dapat menjalankan beberapa program yang sama. (Hanya untuk aplikasi yang mendukung multi-instance).

## Menjalankan Program dengan Hak Administrator
- Jika Anda meluncurkan program sambil menekan `Ctrl + Shift`, Anda dapat meluncurkan program dengan hak administrator.

## Membuka File Explorer
- Anda dapat membuka File Explorer dengan `Win + E`.
- Tampilkan "Run" (Jalankan) dengan `Win + R`, ketik `explorer`, lalu tekan `Enter`.
- Anda dapat membuat folder baru dengan `Ctrl + Shift + N`.

## Membuka Command Prompt di Lokasi yang Sedang Terbuka di File Explorer
- Di Windows 11, Anda dapat membuka Command Prompt dari "Terminal" di menu klik kanan.
- Anda juga dapat membuka Command Prompt dengan mengetik `cmd` di bilah alamat dan menekan `Enter`.

## Menampilkan Riwayat Papan Klip (Clipboard History)
- Anda dapat menampilkan riwayat papan klip dengan `Win + V`.
Jika Anda memilih teks atau gambar yang pernah disalin sebelumnya, Anda dapat menyalinnya lagi.

## Kotak Dialog "Jalankan" (Run)
![img_28.png](img_28.png)
- Anda dapat meluncurkan kotak dialog "Run" dengan `Win + R`.

Berikut adalah beberapa perintah yang dapat dijalankan di "Run" atau Command Prompt.

## Membuka Edge
![img_18.png](img_18.png)
- Ketik `msedge` lalu tekan `Enter`.

## Membuka Internet Explorer 11 (IE11)
![img_25.png](img_25.png)
- Ketik `powershell.exe -Command "(New-Object -ComObject InternetExplorer.Application).Visible = $true"` lalu tekan `Enter`.

## Membuka Terminal
![img_19.png](img_19.png)
- Ketik `wt` lalu tekan `Enter`.

## Membuka Control Panel
![img_15.png](img_15.png)
- Ketik `control` lalu tekan `Enter`.
- Anda juga bisa membukanya dengan `explorer.exe shell:::{26EE0668-A00A-44D7-9371-BEB064C98683}`.

## Membuka Notepad
![img_4.png](img_4.png)
- Ketik `notepad` lalu tekan `Enter`.  

## Membuka Kalkulator
![img_5.png](img_5.png)
- Ketik `calc` lalu tekan `Enter`.

## Membuka Paint
![img_6.png](img_6.png)
- Ketik `mspaint` lalu tekan `Enter`.  

## Membuka PowerShell
![img_7.png](img_7.png)
- Ketik `powershell` lalu tekan `Enter`.  

## Membuka Visual Studio Code
![img_8.png](img_8.png)
- Ketik `code` lalu tekan `Enter`.

## Membuka Excel
![img_9.png](img_9.png)
- Ketik `excel` lalu tekan `Enter`.  
*Hanya jika Excel sudah terinstal.

## Membuka Word
![img_10.png](img_10.png)
- Ketik `winword` lalu tekan `Enter`.  
*Hanya jika Word sudah terinstal.

## Membuka PowerPoint
![img_11.png](img_11.png)
- Ketik `powerpnt` lalu tekan `Enter`.  
  *Hanya jika PowerPoint sudah terinstal.

## Membuka Konfigurasi Sistem (System Configuration)
![img_1.png](img_1.png)
- Ketik `msconfig` lalu tekan `Enter`.  

## Membuka Properti Sistem (System Properties)
![img_2.png](img_2.png)
- Ketik `sysdm.cpl` lalu tekan `Enter`.

## Membuka Informasi Versi Windows
![img_27.png](img_27.png)
- Ketik `winver` lalu tekan `Enter`.

## Membuka Keyboard Layar (On-Screen Keyboard)
![img_14.png](img_14.png)
- Ketik `osk` lalu tekan `Enter`.

## Membuka WordPad
![img_12.png](img_12.png)
- Ketik `wordpad` atau `write` lalu tekan `Enter`.

## Membuka Registry Editor
![img_13.png](img_13.png)
- Ketik `regedit` lalu tekan `Enter`.

## Membuka Program dan Fitur (Programs and Features)
- Ketik `explorer.exe shell:::{7b81be6a-ce2b-4676-a29e-eb907a5126c5}` lalu tekan `Enter`.

## Membuka Properti Keyboard
- Ketik `explorer.exe shell:::{725BE8F7-668E-4C7B-8F90-46BDB0936430}` lalu tekan `Enter`.

## Membuka Properti Mouse
![img_16.png](img_16.png)
- Ketik `explorer.exe shell:::{6C8EEC18-8D75-41B2-A177-8831D59D2D50}` lalu tekan `Enter`.

## Membuka Pengaturan Suara (Sound)
![img_3.png](img_3.png)
- Ketik `explorer.exe shell:::{F2DDFC82-8F12-4CDD-B7DC-D4FE1425AA4D}` lalu tekan `Enter`.

## Membuka Akun Pengguna (User Accounts)
- Ketik `explorer.exe shell:::{60632754-c523-4b62-b45c-4172da012619}` lalu tekan `Enter`.

## Menyalin Teks dari Kotak Pesan Standar
![img_26.png](img_26.png)
- Anda dapat menyalin teks dari kotak pesan standar dengan `Ctrl + C`.
Menyalin kotak pesan di atas akan menyalin hal berikut ke papan klip.
```
[Window Title]
WordPad

[Main Instruction]
Apakah Anda ingin menyimpan perubahan ke Dokumen?

[Simpan (S)] [Jangan simpan (N)] [Batal]
```

## Menyimpan Output Command Prompt ke Papan Klip
Menambahkan ` | clip` (pipa + clip) di akhir perintah, seperti `echo "hello" | clip`, dapat menyalin output standar ke papan klip.

## Output Hierarki Folder ke Teks
Anda dapat mengeluarkan hierarki folder dalam format pohon menggunakan perintah `tree` di Command Prompt.

Contoh output
```
C:.
├─.idea
│  └─libraries
├─binaryeditorbz
├─blog
│  ├─archetypes
│  ├─content
│  ├─data
│  ├─layouts
│  ├─static
│  └─themes
│      └─PaperMod
│          ├─.git
│          │  ├─branches
│          │  ├─hooks
│          │  ├─info
│          │  ├─logs
│          │  │  └─refs
│          │  │      ├─heads
│          │  │      └─remotes
│          │  │          └─origin
│          │  ├─objects
│          │  │  ├─info
│          │  │  └─pack
│          │  └─refs
│          │      ├─heads
│          │      ├─remotes
│          │      │  └─origin
│          │      └─tags
│          ├─.github
│          │  ├─ISSUE_TEMPLATE
│          │  └─workflows
│          ├─assets
│          │  ├─css
│          │  │  ├─common
│          │  │  ├─core
│          │  │  ├─extended
│          │  │  ├─hljs
│          │  │  └─includes
│          │  └─js
│          ├─i18n
│          ├─images
│          └─layouts
│              ├─partials
│              │  └─templates
│              ├─shortcodes
│              └─_default
│                  └─_markup
(dan seterusnya)
```

## Referensi
- [Pintasan keyboard di Windows](https://support.microsoft.com/id-id/windows/pintasan-keyboard-di-windows-dcc61a57-8ff0-cffe-9796-cb9706c75eec)
