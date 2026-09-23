---
title: "Teknologi Jaringan: Penjelasan Teknis HTTP - Protokol Stateless yang Mendukung Web"
description: "Menjelaskan mekanisme dan sejarah HTTP, serta protokol stateless yang mendukung Web."
slug: "history-of-http"
date: "2026-09-23T04:00:00+09:00"
image: "eyecatch.jpg"
categories:
  - Network
tags:
  - HTTP
  - Web
---

# Penjelasan Teknis HTTP

Hypertext Transfer Protocol (HTTP) adalah protokol komunikasi yang menjadi fondasi Web.

## Desain Stateless

HTTP adalah protokol yang tidak memiliki status (stateless). Setiap permintaan diproses secara independen.

```mermaid
graph LR;
    C["Client (Web Browser)"] -- "GET /index.html (HTTP/1.1)" --> S["Server (Web Server)"];
    S -- "200 OK (HTML Content)" --> C;
```

## Pertimbangan Performa

Pada HTTP/2 dan HTTP/3, dampak Round-Trip Time (RTT) dikurangi melalui multiplexing. Waktu muat halaman dapat dimodelkan sebagai berikut.

$$ T_{load} = T_{DNS} + T_{TCP} + T_{TLS} + \sum_{i=1}^{N} \left( rac{S_i}{B} + RTT ight) $$

Dengan multiplexing, bagian $\sum$ di akhir diparalelkan, sehingga waktu dipersingkat secara drastis.
