---
title: "Cara Mendapatkan Jumlah Pembuatan Record per Hari Menggunakan SOQL di Salesforce"
slug: "cara-mendapatkan-jumlah-pembuatan-record-per-hari-menggunakan-soql-di-salesforce"
date: 2023-04-09T02:50:30+09:00
tags: ["salesforce", "soql", "tanggal", "agregasi"]
draft: false
image: "img.png"
categories: ["IT dan Teknologi"]
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
