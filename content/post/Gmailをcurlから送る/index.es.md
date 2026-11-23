---









slug: "Gmailをcurlから送る"
tags: ["gmail", "curl"]
draft: false
image: "img.webp"
categories: ["ai-technology"]
title: "Enviar correo de Gmail con curl"
date: "2025-02-27T02:13:31+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Envía correo mediante Gmail SMTP con curl: autenticación con contraseña de aplicación, TLS, archivo RFC 5322 y comandos para Bash y Windows PowerShell."
---

curl puede conectarse a Gmail SMTP y cargar un archivo de mensaje preparado previamente. No es la API de Gmail. Google recomienda normalmente OAuth 2.0; el ejemplo es para una prueba manual con una cuenta que admita contraseñas de aplicación.

## Elegir la autenticación

No uses la contraseña normal de tu cuenta de Google para SMTP. Si la aplicación admite OAuth 2.0, prefiérelo. Para una prueba manual, puede servir una contraseña de aplicación si la cuenta tiene activada la verificación en dos pasos. Créala en [Contraseñas de aplicaciones de Google](https://myaccount.google.com/apppasswords). No todos los tipos de cuenta muestran esta opción; las políticas de una organización o los ajustes de seguridad pueden impedirlo. Google no recomienda estas contraseñas para la mayoría de los usos. Revócala cuando ya no la necesites.

## Crear el archivo del mensaje

En una carga SMTP, curl no redacta ni convierte el mensaje. El archivo debe contener los encabezados y el cuerpo en formato RFC 5322. El ejemplo usa direcciones ASCII. Mantén el encabezado `From` alineado con la cuenta de Gmail usada para autenticarte. Un asunto con caracteres no ASCII requiere codificación MIME.

Guarda este mensaje como `mail.txt`.

```text
From: sender@gmail.com
To: recipient@example.com
Subject: Test message
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8

This is a test message sent with curl.
```

## Enviar con curl

Este ejemplo usa TLS implícito en el puerto 465. Como `--user` solo incluye el usuario, curl solicita la contraseña; introduce la contraseña de aplicación en ese aviso. Para el puerto 587, usa `smtp://smtp.gmail.com:587` y `--ssl-reqd` para solicitar STARTTLS.

### Bash, zsh, Linux y macOS

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

## Proteger las credenciales

No pongas la contraseña de aplicación en la línea de comandos, el archivo del mensaje, el historial del shell, un repositorio ni los registros. Usa el aviso de contraseña de curl. Protege también el archivo del mensaje si contiene datos personales o confidenciales.

Documentación oficial: [Gmail SMTP settings and OAuth support](https://developers.google.com/workspace/gmail/imap/imap-smtp), [Google app passwords](https://support.google.com/accounts/answer/185833), [Gmail OAuth 2.0 for SMTP](https://developers.google.com/workspace/gmail/imap/xoauth2-protocol), and the [curl manual for --user and --upload-file](https://curl.se/docs/manpage.html).
