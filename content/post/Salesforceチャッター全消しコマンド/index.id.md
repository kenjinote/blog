---
title: 'Salesforce: Perintah untuk Menghapus Semua Postingan Chatter dan Lampiran'
slug: "Salesforceチャッター全消しコマンド"
date: 2022-09-19T21:59:14+09:00
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.webp"
categories: ["TI & Teknologi"]
description: 'Memperkenalkan perintah untuk menghapus massal semua postingan Chatter, lampiran, dan data tempat sampah, yang berguna saat kapasitas penyimpanan organisasi di Salesforce menipis. Ini adalah cara untuk membersihkan dengan cepat menggunakan Jendela Eksekusi Anonim dari Konsol Pengembang.'
---
# Perintah untuk Menghapus Semua Chatter Salesforce
Ini adalah perintah untuk menghapus semua postingan dan lampiran di Salesforce Chatter.
Buka Developer Console, pilih "Open Execute anonymous Window" dari menu Debug, tempelkan kode berikut, dan jalankan.
Secara pribadi, saya menggunakannya saat kapasitas penyimpanan organisasi hampir habis.

```
delete [select id from FeedItem];
delete [select id from FeedAttachment];
delete [select id from ContentDocument];

// Kosongkan tempat sampah
database.emptyRecycleBin([select id from ContentDocument where IsDeleted = true ALL ROWS]);
```
