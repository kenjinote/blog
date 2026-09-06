---
title: "Gmail mit curl senden"
slug: "gmail-mit-curl-senden"
date: 2025-02-27T02:13:31+09:00
tags: ["gmail", "curl"]
draft: false
image: "img.png"
categories: ["KI & Technologie"]
---

# Gmail mit curl senden

## 1. App-Passwort abrufen
https://myaccount.google.com/apppasswords
Klicken Sie auf den obigen Link und geben Sie den App-Namen ein.
Speichern Sie das generierte Passwort.

## 2. E-Mail mit dem curl-Befehl senden
Führen Sie den folgenden Befehl aus.

Im folgenden Beispiel wird der E-Mail-Inhalt in mail.txt geschrieben.

```mail.txt
From: from@gmail.com
To: to@gmail.com
Subject: Test-E-Mail
Content-Type: text/plain; charset="UTF-8"

Dies ist eine Test-E-Mail.
```

Erstellen Sie die obige Datei und führen Sie den folgenden Befehl aus.

```bash
curl --url "smtps://smtp.gmail.com:465" --ssl-reqd --mail-from "from@gmail.com" --mail-rcpt "to@gmail.com" --user "from@gmail.com:xxxxxxxxxxxxxxxx" --upload-file mail.txt
```
※ Bitte ersetzen Sie xxxxxxxxxxxxxxxx durch Ihr App-Passwort.
