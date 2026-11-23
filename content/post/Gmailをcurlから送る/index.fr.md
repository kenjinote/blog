---
slug: "Gmailをcurlから送る"
tags: ["gmail", "curl"]
draft: false
image: "img.webp"
categories: ["ai-technology"]
title: "Envoyer un e-mail Gmail avec curl"
date: "2025-02-27T02:13:31+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Envoyez un e-mail via Gmail SMTP avec curl : mot de passe d’application, TLS, fichier RFC 5322 et commandes pour Bash et Windows PowerShell."
---

curl peut se connecter au serveur SMTP de Gmail et envoyer un fichier de message préparé. Il ne s’agit pas de l’API Gmail. Google recommande généralement OAuth 2.0 ; l’exemple ci-dessous convient à un test manuel avec un compte éligible aux mots de passe d’application.

## Choisir l’authentification

N’utilisez pas le mot de passe habituel de votre compte Google pour SMTP. Préférez OAuth 2.0 si votre application le prend en charge. Pour un test manuel, un mot de passe d’application peut convenir si la validation en deux étapes est activée. Créez-le dans [les mots de passe d’application du compte Google](https://myaccount.google.com/apppasswords). Cette option n’est pas disponible pour tous les comptes ; une règle d’organisation ou des paramètres de sécurité peuvent la masquer. Google ne recommande pas ces mots de passe pour la plupart des usages. Révoquez-le quand vous n’en avez plus besoin.

## Créer le fichier du message

Pour l’envoi SMTP, curl ne compose ni ne convertit le message. Le fichier doit contenir les en-têtes et le corps au format RFC 5322. L’exemple utilise des adresses ASCII. Faites correspondre l’en-tête `From` au compte Gmail utilisé pour l’authentification. Un sujet non ASCII nécessite un encodage MIME.

Enregistrez ce message sous le nom `mail.txt`.

```text
From: sender@gmail.com
To: recipient@example.com
Subject: Test message
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8

This is a test message sent with curl.
```

## Envoyer avec curl

L’exemple utilise TLS implicite sur le port 465. Comme `--user` ne contient que le nom d’utilisateur, curl demande le mot de passe ; saisissez alors le mot de passe d’application. Pour le port 587, utilisez `smtp://smtp.gmail.com:587` avec `--ssl-reqd` afin de demander STARTTLS.

### Bash, zsh, Linux et macOS

```bash
curl --url "smtps://smtp.gmail.com:465" \
  --mail-from "sender@gmail.com" \
  --mail-rcpt "recipient@example.com" \
  --user "sender@gmail.com" \
  --upload-file mail.txt
```

### Windows PowerShell

```powershell
curl.exe --url "smtps://smtp.gmail.com:465" --mail-from "sender@gmail.com" --mail-rcpt "recipient@example.com" --user "sender@gmail.com" --upload-file "mail.txt"
```

## Protéger les identifiants

Ne placez pas le mot de passe d’application dans la commande, le fichier du message, l’historique du shell, un dépôt ou des journaux. Utilisez l’invite de mot de passe de curl. Protégez aussi le fichier s’il contient des données personnelles ou confidentielles.

Documentation officielle : [Gmail SMTP settings and OAuth support](https://developers.google.com/workspace/gmail/imap/imap-smtp), [Google app passwords](https://support.google.com/accounts/answer/185833), [Gmail OAuth 2.0 for SMTP](https://developers.google.com/workspace/gmail/imap/xoauth2-protocol), and the [curl manual for --user and --upload-file](https://curl.se/docs/manpage.html).
