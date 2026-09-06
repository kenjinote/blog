---





title: "Enviar Gmail desde curl"
date: 2025-02-27T02:13:31+09:00
tags: ["gmail", "curl"]
draft: false
image: "img.png"
categories: ["IA y Tecnología"]
---






# Enviar Gmail desde curl

## 1. Obtener la contraseña de la aplicación
https://myaccount.google.com/apppasswords
Haz clic en el enlace de arriba e introduce el nombre de la aplicación.
Guarda la contraseña generada.

## 2. Enviar un correo electrónico con el comando curl
Ejecuta el siguiente comando.

En el ejemplo de abajo, el contenido del correo electrónico está descrito en mail.txt.

```mail.txt
From: from@gmail.com
To: to@gmail.com
Subject: Correo de prueba
Content-Type: text/plain; charset="UTF-8"

Este es un correo de prueba.
```

Crea el archivo anterior y ejecuta el siguiente comando.

```bash
curl --url "smtps://smtp.gmail.com:465" --ssl-reqd --mail-from "from@gmail.com" --mail-rcpt "to@gmail.com" --user "from@gmail.com:xxxxxxxxxxxxxxxx" --upload-file mail.txt
```
※ Sustituye xxxxxxxxxxxxxxxx por la contraseña de tu aplicación.
