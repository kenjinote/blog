---
slug: "Gmailをcurlから送る"
tags: ["gmail", "curl"]
draft: false
image: "img.webp"
categories: ["ai-technology"]
title: "E-Mails aus Gmail mit curl senden"
date: "2025-02-27T02:13:31+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "E-Mail über Gmail SMTP mit curl senden: Anwendungs-Passwort, TLS, RFC-5322-Nachrichtendatei sowie Befehle für Bash und Windows PowerShell."
---

curl kann sich mit Gmail SMTP verbinden und eine vorbereitete Nachrichtendatei hochladen. Dies ist nicht die Gmail API. Google empfiehlt generell OAuth 2.0; das Beispiel eignet sich für einen manuellen Test mit einem Konto, das ein Anwendungs-Passwort verwenden darf.

## Authentifizierung auswählen

Verwenden Sie für SMTP niemals Ihr normales Google-Kontopasswort. Bevorzugen Sie OAuth 2.0, wenn Ihre Anwendung es unterstützt. Für einen manuellen Test kann ein Anwendungs-Passwort funktionieren, sofern die Bestätigung in zwei Schritten aktiviert ist. Erstellen Sie es unter [Google-Konto: App-Passwörter](https://myaccount.google.com/apppasswords). Die Option ist nicht für jedes Konto verfügbar; Organisationsrichtlinien oder Sicherheitseinstellungen können sie ausblenden. Google empfiehlt Anwendungs-Passwörter für die meisten Zwecke nicht. Widerrufen Sie es, wenn Sie es nicht mehr benötigen.

## Nachrichtendatei erstellen

Bei SMTP-Uploads erstellt oder konvertiert curl die Nachricht nicht. Die Datei muss Kopfzeilen und Textkörper im RFC-5322-Format enthalten. Das Beispiel verwendet ASCII-Adressen. Der `From`-Header sollte zum authentifizierten Gmail-Konto passen. Ein Betreff mit Nicht-ASCII-Zeichen benötigt MIME-Kodierung.

Speichern Sie diese Nachricht als `mail.txt`.

```text
From: sender@gmail.com
To: recipient@example.com
Subject: Test message
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8

This is a test message sent with curl.
```

## Mit curl senden

Das Beispiel verwendet implizites TLS auf Port 465. Da `--user` nur den Benutzernamen enthält, fragt curl nach dem Passwort; geben Sie dort das Anwendungs-Passwort ein. Für Port 587 verwenden Sie `smtp://smtp.gmail.com:587` und `--ssl-reqd`, um STARTTLS anzufordern.

### Bash, zsh, Linux und macOS

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

## Zugangsdaten schützen

Schreiben Sie das Anwendungs-Passwort nicht in die Befehlszeile, Nachrichtendatei, Shell-Historie, ein Repository oder ein Protokoll. Verwenden Sie die Passwortabfrage von curl. Schützen Sie auch die Nachrichtendatei, wenn sie persönliche oder vertrauliche Daten enthält.

Offizielle Dokumentation: [Gmail SMTP settings and OAuth support](https://developers.google.com/workspace/gmail/imap/imap-smtp), [Google app passwords](https://support.google.com/accounts/answer/185833), [Gmail OAuth 2.0 for SMTP](https://developers.google.com/workspace/gmail/imap/xoauth2-protocol), and the [curl manual for --user and --upload-file](https://curl.se/docs/manpage.html).
