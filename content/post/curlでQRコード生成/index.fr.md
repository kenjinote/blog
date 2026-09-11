---
title: 'Comment générer un code QR dans l''invite de commande à l''aide de la commande curl'
slug: "curlでQRコード生成"
date: 2024-04-16T00:42:27+09:00
tags: ["Code QR", "curl", "Invite de commandes"]
draft: false
image: "img.webp"
categories: ["Informatique et Technologie"]
description: 'Nous présentons comment générer et afficher un code QR textuel en utilisant la commande curl dans l''invite de commande Windows. Étant donné l''utilisation d''une API externe (qrenco.de), nous expliquons également les précautions à prendre concernant le traitement des informations personnelles.'
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
curl -o qr.webp "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=HelloWorld"
```

- Résultat de sortie
![](qr.webp)

#### Référence
- [QR Code Generator](https://goqr.me/api/doc/create-qr-code/)
