---
title: "Mengganti Internet Rumah dari Flets Hikari ke J:COM"
slug: "ネット環境をフレッツ光→JCOMに変えた"
date: 2022-09-05T22:48:51+09:00
tags: ["J:COM", "Flets Hikari", "Koneksi Internet"]
draft: false
image: "jcom.png"
categories: ["IT / Teknologi"]
---

# Mengganti Internet Rumah dari Flets Hikari ke J:COM

![](flets_hikari.png)

![](jcom.png)

Atas rekomendasi seorang kenalan, saya mengganti koneksi internet rumah dari Flets Hikari ke J:COM. Alasannya adalah:

1. Biaya bulanan menjadi lebih murah. 3.619 yen -> 2.180 yen
2. Kecepatan internet naik dari 100 MBps menjadi 320 MBps

Itu poin utamanya.

# Kesan Setelah Menggunakan
Sudah sekitar seminggu sejak beralih, dan sejauh ini hampir tidak ada masalah. Di bawah ini saya tuliskan sedikit hal yang menjadi perhatian.

Setelah benar-benar berubah, saya perhatikan bahwa kecepatan unduh memang menjadi lebih cepat, dari 60 MBps kini bisa mencapai hampir 320 MBps. Namun,
untuk kecepatan unggah, yang sebelumnya mencapai 40 MBps saat menggunakan Flets Hikari, kini turun menjadi sekitar 10 MBps. Tampaknya ini memang spesifikasi dari pihak J:COM.
Karena saat ini saya tidak melakukan streaming atau mengunggah data dalam jumlah besar, saya akan memantau situasinya.

Selain itu, akhir-akhir ini saya dan keluarga lebih banyak bekerja dari rumah, namun hari ini untuk pertama kalinya internet terputus selama beberapa puluh menit. Itu pulih secara otomatis, tapi,
mungkin ini bukan awal yang baik. Padahal, belum genap seminggu sejak saya beralih...

Sebagai catatan, tampaknya kecepatan aplikasi P2P lambat karena J:COM membatasi komunikasi P2P. Bagi yang menggunakan P2P sebaiknya berhati-hati.

# Tentang Layanan
Saat penandatanganan kontrak, jika bergabung dengan Netflix atau Disney+, saya akan mendapatkan kartu QUO senilai 40.000 yen, yang akan menutupi biaya kontrak masing-masing layanan dan membuat biaya bulanan rata-rata sedikit lebih murah.
Oleh karena itu, saya mengontrak layanannya bersamaan dengan kontrak internet. Kontrak Netflix berlaku selama 1 tahun dan Disney+ selama setengah tahun, sepertinya saya perlu membatalkan kontrak sendiri.

Karena saya baru saja beralih, jika ada tambahan kesan dan pengalaman, saya akan memperbarui artikel ini lagi. Sampai jumpa.

# 09/06 Sulit Terhubung ke Internet
- 2022/09/06 sekitar pukul 13:13 selama 3 sampai 5 menit
- 2022/09/06 sekitar pukul 13:30 selama 3 sampai 5 menit
- Beberapa kali setelahnya...

![Diagnosis Jaringan](trouble_shooting.png)

Sepertinya masalahnya ada di DNS, jadi saya mengatur server DNS merujuk ke [sini](https://internet.watch.impress.co.jp/docs/column/shimizu/1367271.html).
Mari kita lihat apa yang terjadi... Karena saya tidak dapat terhubung bahkan dengan pengaturan DNS, saya menghubungi bagian dukungan, dan mereka mengatakan sedang ada pemeliharaan darurat... Segera setelah saya menghubungi mereka, status koneksi membaik, jadi saya rasa mereka telah mengambil tindakan.
