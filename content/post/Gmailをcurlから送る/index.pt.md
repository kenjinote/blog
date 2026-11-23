---
slug: "Gmailをcurlから送る"
tags: ["gmail", "curl"]
draft: false
image: "img.webp"
categories: ["ai-technology"]
title: "Enviar e-mail do Gmail com curl"
date: "2025-02-27T02:13:31+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Envie e-mail pelo SMTP do Gmail com curl: senha de app, TLS, arquivo RFC 5322 e comandos para Bash e Windows PowerShell."
---

O curl pode se conectar ao SMTP do Gmail e enviar um arquivo de mensagem preparado. Isso não é a API do Gmail. O Google geralmente recomenda OAuth 2.0; o exemplo é para um teste manual com uma conta que possa usar senha de app.

## Escolher a autenticação

Não use a senha normal da Conta do Google no SMTP. Prefira OAuth 2.0 quando o aplicativo oferecer suporte. Para um teste manual, uma senha de app pode funcionar se a verificação em duas etapas estiver ativada. Crie-a em [Senhas de app da Conta do Google](https://myaccount.google.com/apppasswords). A opção não está disponível para todas as contas; políticas da organização ou configurações de segurança podem ocultá-la. O Google não recomenda senhas de app para a maioria dos usos. Revogue-a quando não precisar mais.

## Criar o arquivo da mensagem

No envio por SMTP, o curl não compõe nem converte a mensagem. O arquivo precisa conter cabeçalhos e corpo no formato RFC 5322. O exemplo usa endereços ASCII. Mantenha o cabeçalho `From` alinhado à conta Gmail usada na autenticação. Um assunto com caracteres não ASCII requer codificação MIME.

Salve esta mensagem como `mail.txt`.

```text
From: sender@gmail.com
To: recipient@example.com
Subject: Test message
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8

This is a test message sent with curl.
```

## Enviar com curl

Este exemplo usa TLS implícito na porta 465. Como `--user` contém apenas o nome de usuário, o curl solicita a senha; digite a senha de app nesse prompt. Para a porta 587, use `smtp://smtp.gmail.com:587` com `--ssl-reqd` para solicitar STARTTLS.

### Bash, zsh, Linux e macOS

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

## Proteger as credenciais

Não coloque a senha de app na linha de comando, arquivo de mensagem, histórico do shell, repositório ou log. Use o prompt de senha do curl. Proteja também o arquivo se contiver informações pessoais ou confidenciais.

Documentação oficial: [Gmail SMTP settings and OAuth support](https://developers.google.com/workspace/gmail/imap/imap-smtp), [Google app passwords](https://support.google.com/accounts/answer/185833), [Gmail OAuth 2.0 for SMTP](https://developers.google.com/workspace/gmail/imap/xoauth2-protocol), and the [curl manual for --user and --upload-file](https://curl.se/docs/manpage.html).
