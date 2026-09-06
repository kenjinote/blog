---
title: "Cara Mengatasi GitHub Copilot yang Tidak Dapat Digunakan Karena Kesalahan Sertifikat"
slug: "cara-mengatasi-github-copilot-yang-tidak-dapat-digunakan-karena-kesalahan-sertifikat"
date: 2024-04-21T18:47:26+09:00
tags: ["GitHub Copilot", ""]
draft: false
image: "img.png"
categories: ["ツール・開発環境"]
---

# Cara Mengatasi Pesan Kesalahan Berikut di GitHub Copilot

GitHub Copilot berhenti berfungsi sekitar tanggal 19 April 2024. Pesan kesalahannya adalah sebagai berikut:

```
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

## Cara Mengatasi
Tampaknya ini adalah bug pada ESET. Di pengaturan lanjutan ESET, matikan "Aktifkan SSL/TLS".
![img_1.png](img_1.png)

## Referensi

Tampaknya kesalahan yang sama juga terjadi pada AWS CDK.
- [AWS CDK bootstrap certificate warning-error](https://repost.aws/questions/QU2H94hF04SIuEVejK_a1mtQ/aws-cdk-bootstrap-certificate-warning-error)
