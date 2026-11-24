---
title: 'How to Generate QR Codes in Command Prompt using curl Command'
slug: "curlでQR Code生成"
date: "2024-04-16T00:42:27+09:00"
lastmod: "2026-11-25"
tags: ["QR code", "curl", "Command Prompt"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'This article shows how to use curl in Windows Command Prompt to generate text and image QR codes, and explains what to consider when sending data to external services.'
---

## Generate QR code with curl

Note: The method introduced below generates the QR code on the server side and returns it, so logs might be kept. Please be careful when converting confidential information such as personal information into a QR code.

The text you enter is sent to an external service, so do not use confidential information.

### Method 1

This is a method to generate a QR code in the command prompt.
`qrenco.de` returns a text-based response.

```
curl.exe https://qrenco.de/kenji.blog
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

The GoQR API returns PNG by default. URL-encode the `data` value if it contains spaces or special characters.

```
curl.exe -o qr.png "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=HelloWorld"
```

- Output result
![Sample QR code image](qr.webp)

#### Reference
- [QR Code Generator](https://goqr.me/api/doc/create-qr-code/)
- [curl command-line manual](https://curl.se/docs/manpage.html)
