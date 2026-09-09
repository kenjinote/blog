---
title: 'Como Enviar E-mails do Gmail Usando o Comando curl'
slug: "enviar-gmail-com-curl"
date: 2025-02-27T02:13:31+09:00
tags: ["gmail", "curl"]
draft: false
image: "img.webp"
categories: ["IA e Tecnologia"]
description: 'Explicamos como enviar e-mails via conta do Gmail através da ferramenta de linha de comando ''curl''. Detalhamos desde o processo para obter uma Senha de App do Google, até as opções do comando curl e a criação e envio do arquivo do corpo do e-mail.'
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
