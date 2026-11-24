---







title: 'Cómo generar códigos QR en el símbolo del sistema usando el comando curl'
slug: "curlでCódigo QR生成"
date: "2024-04-16T00:42:27+09:00"
lastmod: "2026-11-25"
tags: ["Código QR", "curl", "Símbolo del sistema"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'Este artículo explica cómo usar curl en el símbolo del sistema de Windows para generar códigos QR de texto e imagen, y qué tener en cuenta al enviar datos a servicios externos.'
---








## Generar código QR con curl

Nota: El método presentado devuelve un código QR generado en el lado del servidor, por lo que es posible que se registren logs. Ten cuidado al convertir información confidencial, como información personal, en un código QR.

El texto que introduzcas se envía a un servicio externo; no uses información confidencial.

### Método 1

Este es el método para generar un código QR en el Símbolo del sistema.
`qrenco.de` devuelve la respuesta basada en texto.

```
curl.exe https://qrenco.de/kenji.blog
```

- Resultado de salida

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

#### Referencia
- [qrenco.de](https://qrenco.de/)

### Método 2

`api.qrserver.com` devuelve una imagen.

La API de GoQR devuelve PNG de forma predeterminada. Codifica en URL el valor de `data` si contiene espacios o caracteres especiales.

```
curl.exe -o qr.png "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=HelloWorld"
```

- Resultado de salida
![Imagen de ejemplo de un código QR](qr.webp)

#### Referencia
- [QR Code Generator](https://goqr.me/api/doc/create-qr-code/)
- [curl command-line manual](https://curl.se/docs/manpage.html)
