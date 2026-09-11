---
title: 'Comment envoyer un e-mail avec Gmail à l''aide de la commande curl'
slug: "Gmailをcurlから送る"
date: 2025-02-27T02:13:31+09:00
tags: ["gmail", "curl"]
draft: false
image: "img.webp"
categories: ["IA et Technologie"]
description: 'Nous expliquons comment envoyer un e-mail via votre compte Gmail à l''aide de l''outil de ligne de commande « curl ». Nous présentons en détail la procédure d''obtention d''un mot de passe d''application Google, la spécification des options de curl, ainsi que la création et l''envoi d''un fichier de corps d''e-mail.'
---

# Envoyer un Gmail avec curl

## 1. Obtenir un mot de passe d'application
https://myaccount.google.com/apppasswords
Cliquez sur le lien ci-dessus et entrez le nom de l'application.
Enregistrez le mot de passe généré.

## 2. Envoyer un e-mail avec la commande curl
Exécutez la commande suivante.

Dans l'exemple ci-dessous, le contenu de l'e-mail est écrit dans mail.txt.

```mail.txt
From: from@gmail.com
To: to@gmail.com
Subject: E-mail de test
Content-Type: text/plain; charset="UTF-8"

Ceci est un e-mail de test.
```

Créez le fichier ci-dessus et exécutez la commande suivante.

```bash
curl --url "smtps://smtp.gmail.com:465" --ssl-reqd --mail-from "from@gmail.com" --mail-rcpt "to@gmail.com" --user "from@gmail.com:xxxxxxxxxxxxxxxx" --upload-file mail.txt
```
※ Veuillez remplacer xxxxxxxxxxxxxxxx par votre mot de passe d'application.
