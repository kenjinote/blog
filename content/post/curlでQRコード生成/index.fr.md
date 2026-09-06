---
title: "Générer un code QR avec curl"
slug: "curlでQRコード生成"
date: 2024-04-16T00:42:27+09:00
tags: ["Code QR", "curl", "Invite de commandes"]
draft: false
image: "img.png"
categories: ["Informatique et Technologie"]
---

## Générer un code QR avec curl

Attention : Les méthodes présentées renvoient un code QR généré côté serveur, il est donc possible que des journaux soient enregistrés. Soyez prudent lorsque vous convertissez des informations confidentielles, telles que des informations personnelles, en code QR.

### Méthode 1

Il s'agit d'une méthode pour générer un code QR dans l'invite de commandes.
`qrenco.de` renvoie une réponse sous forme de texte.

```
curl qrenco.de/kenji.blog
```

- Résultat de sortie

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

#### Référence
- [qrenco.de](https://qrenco.de/)

### Méthode 2

`api.qrserver.com` renvoie une image.

```
curl -o qr.png "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=HelloWorld"
```

- Résultat de sortie
![](qr.png)

#### Référence
- [QR Code Generator](https://goqr.me/api/doc/create-qr-code/)
