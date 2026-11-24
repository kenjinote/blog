---
title: "Menghitung Jumlah Record Salesforce per Hari dengan SOQL"

slug: "SalesforceのSOQLを利用して日別のレコード作成数を取得する方法"
date: 2023-04-09T02:50:30+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["salesforce", "soql", "tanggal", "agregasi"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Contoh SOQL yang mengelompokkan CreatedDate menurut hari lokal pengguna dengan DAY_ONLY dan convertTimezone serta menampilkan sepuluh hari dengan jumlah record tertinggi."
---
Buka `Query Editor` di Developer Console dan jalankan kueri berikut.

`Account` adalah contoh objek standar; ganti dengan nama API objek yang diperlukan. `COUNT(Id)` menghitung record di setiap kelompok. Tanggal dikonversi ke zona waktu pengguna yang menjalankan kueri dan hasilnya menampilkan sepuluh hari tersibuk, belum tentu yang terbaru. Tambahkan `WHERE CreatedDate` untuk membatasi periode. Hari tanpa record tidak ditampilkan.

```sql
SELECT DAY_ONLY(convertTimezone(CreatedDate)), COUNT(Id)
FROM Account
GROUP BY DAY_ONLY(convertTimezone(CreatedDate))
ORDER BY COUNT(Id) DESC
LIMIT 10
```

## Referensi

- [Date Functions in SOQL — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-date-functions.html)
- [convertTimezone() — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-convert-time-zone.html)
- [Aggregate Functions — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-agg_functions.html)
- [Execute a SOQL Query — Salesforce Help](https://help.salesforce.com/s/articleView?id=code_dev_console_tab_query_editor_soql_sosl.htm&language=en_US&type=0)