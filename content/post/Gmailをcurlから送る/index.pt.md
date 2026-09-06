---
title: "Enviar Gmail com curl"
slug: "enviar-gmail-com-curl"
date: 2025-02-27T02:13:31+09:00
tags: ["gmail", "curl"]
draft: false
image: "img.png"
categories: ["IA e Tecnologia"]
---

# Enviar Gmail com curl

## 1. Obter uma senha de aplicativo
https://myaccount.google.com/apppasswords
Clique no link acima e insira o nome do aplicativo.
Salve a senha gerada.

## 2. Enviar email com o comando curl
Execute o seguinte comando.

No exemplo abaixo, o conteúdo do email está escrito em mail.txt.

```mail.txt
From: from@gmail.com
To: to@gmail.com
Subject: Email de teste
Content-Type: text/plain; charset="UTF-8"

Este é um email de teste.
```

Crie o arquivo acima e execute o seguinte comando.

```bash
curl --url "smtps://smtp.gmail.com:465" --ssl-reqd --mail-from "from@gmail.com" --mail-rcpt "to@gmail.com" --user "from@gmail.com:xxxxxxxxxxxxxxxx" --upload-file mail.txt
```
※ Substitua xxxxxxxxxxxxxxxx pela sua senha de aplicativo.
