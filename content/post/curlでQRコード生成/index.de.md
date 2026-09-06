---
title: "QR-Code mit curl generieren"
slug: "curlでQRコード生成"
date: 2024-04-16T00:42:27+09:00
tags: ["QR-Code", "curl", "Eingabeaufforderung"]
draft: false
image: "img.png"
categories: ["IT & Technologie"]
---

## QR-Code mit curl generieren

Achtung: Die vorgestellten Methoden geben einen serverseitig generierten QR-Code zurück, sodass möglicherweise Protokolle aufgezeichnet werden. Seien Sie vorsichtig, wenn Sie vertrauliche Informationen, wie z. B. persönliche Daten, in einen QR-Code umwandeln.

### Methode 1

Dies ist eine Methode, um einen QR-Code in der Eingabeaufforderung zu generieren.
`qrenco.de` gibt die Antwort textbasiert zurück.

```
curl qrenco.de/kenji.blog
```

- Ausgabeergebnis

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

#### Referenz
- [qrenco.de](https://qrenco.de/)

### Methode 2

`api.qrserver.com` gibt ein Bild zurück.

```
curl -o qr.png "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=HelloWorld"
```

- Ausgabeergebnis
![](qr.png)

#### Referenz
- [QR Code Generator](https://goqr.me/api/doc/create-qr-code/)
