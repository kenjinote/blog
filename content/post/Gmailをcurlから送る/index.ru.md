---
slug: "Gmailをcurlから送る"
tags: ["gmail", "curl"]
draft: false
image: "img.webp"
categories: ["ai-technology"]
title: "Отправка писем Gmail с помощью curl"
date: "2025-02-27T02:13:31+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Отправка писем через Gmail SMTP с помощью curl: пароль приложения, TLS, файл сообщения RFC 5322, команды для Bash и Windows PowerShell."
---

curl может подключиться к Gmail SMTP и загрузить подготовленный файл сообщения. Это не Gmail API. Google обычно рекомендует OAuth 2.0; пример ниже подходит для ручной проверки с аккаунтом, которому доступен пароль приложения.

## Выберите способ аутентификации

Не используйте обычный пароль Google-аккаунта для SMTP. Если приложение поддерживает OAuth 2.0, отдайте ему предпочтение. Для ручной проверки можно использовать пароль приложения, если включена двухэтапная аутентификация. Создайте его на странице [паролей приложений Google](https://myaccount.google.com/apppasswords). Эта возможность доступна не всем аккаунтам: ее могут скрывать политика организации или настройки безопасности. Google не рекомендует пароли приложений для большинства случаев. Отзовите пароль, когда он больше не нужен.

## Создайте файл сообщения

При отправке через SMTP curl не формирует и не преобразует письмо. Файл должен содержать заголовки и текст сообщения в формате RFC 5322. В примере используются ASCII-адреса. Заголовок `From` должен соответствовать Gmail-аккаунту для аутентификации. Тема с символами вне ASCII требует MIME-кодирования.

Сохраните это сообщение в файле `mail.txt`.

```text
From: sender@gmail.com
To: recipient@example.com
Subject: Test message
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8

This is a test message sent with curl.
```

## Отправьте письмо через curl

В примере используется неявный TLS на порту 465. Поскольку в `--user` указан только логин, curl запросит пароль; введите пароль приложения в ответ на запрос. Для порта 587 укажите `smtp://smtp.gmail.com:587` и `--ssl-reqd`, чтобы запросить STARTTLS.

### Bash, zsh, Linux и macOS

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

## Защитите учетные данные

Не помещайте пароль приложения в командную строку, файл письма, историю оболочки, репозиторий или журналы. Используйте запрос пароля curl. Защитите и сам файл, если в нем есть личные или конфиденциальные сведения.

Официальная документация: [Gmail SMTP settings and OAuth support](https://developers.google.com/workspace/gmail/imap/imap-smtp), [Google app passwords](https://support.google.com/accounts/answer/185833), [Gmail OAuth 2.0 for SMTP](https://developers.google.com/workspace/gmail/imap/xoauth2-protocol), and the [curl manual for --user and --upload-file](https://curl.se/docs/manpage.html).
