---







title: "Generar código QR con curl"
slug: "curlでQRコード生成"
date: 2024-04-16T00:42:27+09:00
tags: ["Código QR", "curl", "Símbolo del sistema"]
draft: false
image: "img.png"
categories: ["TI y Tecnología"]
---








## Generar código QR con curl

Nota: El método presentado devuelve un código QR generado en el lado del servidor, por lo que es posible que se registren logs. Ten cuidado al convertir información confidencial, como información personal, en un código QR.

### Método 1

Este es el método para generar un código QR en el Símbolo del sistema.
`qrenco.de` devuelve la respuesta basada en texto.

```
curl qrenco.de/kenji.blog
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

```
curl -o qr.png "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=HelloWorld"
```

- Resultado de salida
![](qr.png)

#### Referencia
- [QR Code Generator](https://goqr.me/api/doc/create-qr-code/)
