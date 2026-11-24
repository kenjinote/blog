---
title: "Membersihkan Postingan Salesforce Chatter: Penyimpanan dan Langkah Aman"

slug: "SalesforceCeloteh全消しPerintah"
date: 2022-09-19T21:59:14+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: "Postingan Chatter tidak menggunakan penyimpanan data Salesforce. Periksa jenis penyimpanan, tinjau dan cadangkan posting terpilih, lalu hapus dengan aman menggunakan Data Loader."
---
**Penting:** Postingan, komentar, dan perubahan terlacak Chatter tidak dihitung dalam penyimpanan data Salesforce. File lampiran dihitung dalam penyimpanan file. Periksa **Storage Usage** di Setup terlebih dahulu untuk mengetahui kategori yang hampir mencapai batas. Menghapus semua posting tidak akan membebaskan penyimpanan data.

## Meninjau posting berlampiran dengan aman

Contoh SOQL berikut hanya-baca. Contoh ini mencantumkan posting dengan lampiran file (`Type = 'ContentPost'`) untuk ditinjau dan tidak menghapus apa pun.

```sql
SELECT Id, CreatedDate, CreatedById, ParentId, Type
FROM FeedItem
WHERE Type = 'ContentPost'
ORDER BY CreatedDate ASC
```

1. Ekspor ID kandidat dengan Data Loader atau Workbench, lalu persempit berdasarkan tanggal, penulis, record induk, atau kriteria lain yang disetujui.
2. Periksa rencana pencadangan dan pemulihan organisasi, lalu uji prosesnya di Sandbox. Minta admin dan pemilik data meninjau ID serta jumlah penghapusan.
3. Setelah disetujui, hapus hanya ID terpilih menggunakan operasi Delete di Data Loader. Prosedur massal resmi Salesforce juga mengekspor ID FeedItem `Type = ContentPost` sebelum menghapusnya.

Penghapusan FeedItem dapat bersifat permanen, melewati Recycle Bin, dan tidak dapat dipulihkan. Menghapus posting menghapus lampiran dari feed; apakah file tetap ada di lokasi asal atau share lain bergantung pada statusnya. Jangan menghapus semua `ContentDocument` tanpa filter atau mengosongkan seluruh Recycle Bin. Untuk membersihkan penyimpanan file, periksa Storage Usage, pemilik file, share, dan dampaknya sebelum bertindak.

## Referensi

- [Work with Chatter Posts — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_posts_parent.htm&language=en_US&type=5)
- [Data and Storage Resources — Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.admin_monitorresources.htm&language=en_US&type=5)
- [Mass Delete Chatter Feed Item records that contain an attachment — Salesforce Help](https://help.salesforce.com/s/articleView?id=000198685&language=en_US&type=1)
- [FeedItem — Salesforce Developers](https://developer.salesforce.com/docs/platform/object-reference/references/standard-objects/object-feeditem.html)
- [Delete Files and Links from Chatter Feeds — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_attachments_del.htm&language=en_US&type=5)
