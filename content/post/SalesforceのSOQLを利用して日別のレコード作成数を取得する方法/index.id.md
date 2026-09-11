---
title: 'Salesforce: Cara Mendapatkan Jumlah Pembuatan Catatan Harian dengan SOQL'
slug: "SalesforceのSOQLを利用して日別のレコード作成数を取得する方法"
date: 2023-04-09T02:50:30+09:00
tags: ["salesforce", "soql", "tanggal", "agregasi"]
draft: false
image: "img.webp"
categories: ["IT dan Teknologi"]
description: 'Menjelaskan metode spesifik dan sintaks kueri untuk mengumpulkan dan mendapatkan jumlah catatan harian yang dibuat, seperti akun, menggunakan SOQL dari Konsol Pengembang Salesforce. Anda akan memahami prosedur analisis data yang berguna yang memanfaatkan klausa GROUP BY.'
---

# Cara Mendapatkan Jumlah Pembuatan Record per Hari Menggunakan SOQL di Salesforce

1. Buka Developer Console.
2. Buka tab `Query Editor`.
3. Tempel dan jalankan SOQL berikut.
```sql
select day_only(createdDate), count(createdDate) from account group by day_only(createdDate) order by count(createdDate) desc limit 10
```
Harap ubah `account` menjadi nama objek apa pun yang ingin Anda dapatkan lalu jalankan.

# Referensi
- [Is there a way to group by the date portion of a datetime field in SOQL?](https://stackoverflow.com/questions/9187737/is-there-a-way-to-group-by-the-date-portion-of-a-datetime-field-in-soql)
