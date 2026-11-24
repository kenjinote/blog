---
title: 'Comment générer un code QR dans l''invite de commande à l''aide de la commande curl'
slug: "curlでCode QR生成"
date: "2024-04-16T00:42:27+09:00"
lastmod: "2026-11-25"
tags: ["Code QR", "curl", "Invite de commandes"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'Cet article explique comment utiliser curl dans l’invite de commandes Windows pour générer des QR codes textuels et image, et précise les précautions à prendre lors de l’envoi de données à des services externes.'
---

## Générer un code QR avec curl

Attention : Les méthodes présentées renvoient un code QR généré côté serveur, il est donc possible que des journaux soient enregistrés. Soyez prudent lorsque vous convertissez des informations confidentielles, telles que des informations personnelles, en code QR.

Le texte saisi est envoyé à un service externe ; n’utilisez donc aucune information confidentielle.

### Méthode 1

Il s'agit d'une méthode pour générer un code QR dans l'invite de commandes.
`qrenco.de` renvoie une réponse sous forme de texte.

```
curl.exe https://qrenco.de/kenji.blog
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

L’API GoQR renvoie du PNG par défaut. Encodez la valeur de `data` dans l’URL si elle contient des espaces ou des caractères spéciaux.

```
curl.exe -o qr.png "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=HelloWorld"
```

- Résultat de sortie
![Exemple d’image de code QR](qr.webp)

#### Référence
- [QR Code Generator](https://goqr.me/api/doc/create-qr-code/)
- [curl command-line manual](https://curl.se/docs/manpage.html)
