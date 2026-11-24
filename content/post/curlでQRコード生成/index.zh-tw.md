---
title: '使用curl指令在命令提示字元中生成QR Code的方法'
slug: "curlでQR碼生成"
date: "2024-04-16T00:42:27+09:00"
lastmod: "2026-11-25"
tags: ["QR Code", "curl", "命令提示字元"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: '本文介紹如何在 Windows 命令提示字元中使用 curl 產生文字與圖片 QR Code，並說明將資料傳送至外部服務時應注意的事項。'
---

## 使用 curl 產生 QR Code

注意：所介紹的方法是透過伺服器端產生 QR Code 並回傳，因此可能會被記錄日誌。將個人資訊等機密資訊轉換為 QR Code 時請多加留意。

輸入的文字會傳送至外部服務，因此請勿使用機密資訊。

### 方法 1

這是在命令提示字元中產生 QR Code 的方法。
`qrenco.de` 會以文字形式回傳結果。

```
curl.exe https://qrenco.de/kenji.blog
```

- 輸出結果

```
█████████████████████████████
█████████████████████████████
████ ▄▄▄▄▄ █ ▄ ▄ █ ▄▄▄▄▄ ████
████ █   █ █ ▀▀▀██ █   █ ████
████ █▄▄▄█ █▀▀█▀▄█ █▄▄▄█ ████
████▄▄▄▄▄▄▄█▄▀ ▀ █▄▄▄▄▄▄▄████
████▄ █▀▄ ▄▀█▄▀ ▀██▄▀   ▄████
████▀▀▀█  ▄▄ ▄█▄█▀█▀▄██ ▀████
████▄▄▄██▄▄█ █▀█ ▄██▀▀█ █████
████ ▄▄▄▄▄ █▀█ ▀  ▄▀▄▄▄ ▀████
████ █   █ █▄▄ ▄▀▄▀▄ ██ ▀████
████ █▄▄▄█ █▀▀█ ▀▄▄▄ ▄▄██████
████▄▄▄▄▄▄▄█▄▄███▄▄█▄███▄████
█████████████████████████████
█████████████████████████████
```

#### 參考
- [qrenco.de](https://qrenco.de/)

### 方法 2

`api.qrserver.com` 會回傳一張圖片。

GoQR API 預設會回傳 PNG。若 `data` 值包含空格或特殊字元，請先進行 URL 編碼。

```
curl.exe -o qr.png "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=HelloWorld"
```

- 輸出結果
![QR 碼範例圖片](qr.webp)

#### 參考
- [QR Code Generator](https://goqr.me/api/doc/create-qr-code/)
- [curl command-line manual](https://curl.se/docs/manpage.html)
