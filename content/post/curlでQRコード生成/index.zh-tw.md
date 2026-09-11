---
title: '使用curl指令在命令提示字元中生成QR Code的方法'
slug: "curlでQRコード生成"
date: 2024-04-16T00:42:27+09:00
tags: ["QR Code", "curl", "命令提示字元"]
draft: false
image: "img.webp"
categories: ["IT 與科技"]
description: '介紹如何使用Windows的命令提示字元與curl指令，生成並顯示基於文字的QR Code。由於需要利用外部API（qrenco.de），本文也會說明處理個人資訊時應注意的事項。'
---

## 使用 curl 產生 QR Code

注意：所介紹的方法是透過伺服器端產生 QR Code 並回傳，因此可能會被記錄日誌。將個人資訊等機密資訊轉換為 QR Code 時請多加留意。

### 方法 1

這是在命令提示字元中產生 QR Code 的方法。
`qrenco.de` 會以文字形式回傳結果。

```
curl qrenco.de/kenji.blog
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

```
curl -o qr.webp "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=HelloWorld"
```

- 輸出結果
![](qr.webp)

#### 參考
- [QR Code Generator](https://goqr.me/api/doc/create-qr-code/)
