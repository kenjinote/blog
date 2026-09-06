---
title: "Envoyer un Gmail avec curl"
slug: "envoyer-un-gmail-avec-curl"
date: 2025-02-27T02:13:31+09:00
tags: ["gmail", "curl"]
draft: false
image: "img.png"
categories: ["IA et Technologie"]
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
