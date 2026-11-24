---
title: 'Wie man mit dem curl-Befehl einen QR-Code in der Eingabeaufforderung generiert'
slug: "curlでQR-Code生成"
date: "2024-04-16T00:42:27+09:00"
lastmod: "2026-11-25"
tags: ["QR-Code", "curl", "Eingabeaufforderung"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'Dieser Artikel zeigt, wie Sie mit curl in der Windows-Eingabeaufforderung QR-Codes als Text und Bild erzeugen, und erläutert, worauf beim Senden von Daten an externe Dienste zu achten ist.'
---

## QR-Code mit curl generieren

Achtung: Die vorgestellten Methoden geben einen serverseitig generierten QR-Code zurück, sodass möglicherweise Protokolle aufgezeichnet werden. Seien Sie vorsichtig, wenn Sie vertrauliche Informationen, wie z. B. persönliche Daten, in einen QR-Code umwandeln.

Der eingegebene Text wird an einen externen Dienst gesendet. Verwenden Sie daher keine vertraulichen Informationen.

### Methode 1

Dies ist eine Methode, um einen QR-Code in der Eingabeaufforderung zu generieren.
`qrenco.de` gibt die Antwort textbasiert zurück.

```
curl.exe https://qrenco.de/kenji.blog
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

Die GoQR-API liefert standardmäßig PNG. URL-kodieren Sie den Wert von `data`, wenn er Leerzeichen oder Sonderzeichen enthält.

```
curl.exe -o qr.png "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=HelloWorld"
```

- Ausgabeergebnis
![Beispielbild eines QR-Codes](qr.webp)

#### Referenz
- [QR Code Generator](https://goqr.me/api/doc/create-qr-code/)
- [curl command-line manual](https://curl.se/docs/manpage.html)
