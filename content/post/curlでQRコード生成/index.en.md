---
title: 'How to Generate QR Codes in Command Prompt using curl Command'
slug: "curlでQRコード生成"
date: 2024-04-16T00:42:27+09:00
tags: ["QR code", "curl", "Command Prompt"]
draft: false
image: "img.webp"
categories: ["IT/Technology"]
description: 'We introduce how to generate and display text-based QR codes using the curl command in the Windows command prompt. Since it uses an external API (qrenco.de), we also explain precautions regarding the handling of personal information.'
---

## Generate QR code with curl

Note: The method introduced below generates the QR code on the server side and returns it, so logs might be kept. Please be careful when converting confidential information such as personal information into a QR code.

### Method 1

This is a method to generate a QR code in the command prompt.
`qrenco.de` returns a text-based response.

```
curl qrenco.de/kenji.blog
```

- Output result

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

#### Reference
- [qrenco.de](https://qrenco.de/)

### Method 2

`api.qrserver.com` returns an image.

```
curl -o qr.webp "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=HelloWorld"
```

- Output result
![](qr.webp)

#### Reference
- [QR Code Generator](https://goqr.me/api/doc/create-qr-code/)
