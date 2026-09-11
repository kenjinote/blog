---
title: 'Как отправлять электронные письма из Gmail с помощью команды curl'
slug: "Gmailをcurlから送る"
date: 2025-02-27T02:13:31+09:00
tags: ["gmail", "curl"]
draft: false
image: "img.webp"
categories: ["AI・テクノロジー"]
description: 'Объясняется, как отправлять почту через аккаунт Gmail с помощью инструмента командной строки «curl». Подробно описаны шаги от получения пароля приложения Google до указания опций curl, создания файла с текстом письма и команды отправки.'
---

# Отправка электронной почты Gmail с помощью curl

## 1. Получение пароля приложения
https://myaccount.google.com/apppasswords
Нажмите на ссылку выше и введите имя приложения.
Сохраните сгенерированный пароль.

## 2. Отправка электронной почты с помощью команды curl
Выполните следующую команду.

В приведенном ниже примере содержимое письма написано в mail.txt.

```mail.txt
From: from@gmail.com
To: to@gmail.com
Subject: Тестовое письмо
Content-Type: text/plain; charset="UTF-8"

Это тестовое письмо.
```

Создайте указанный выше файл и выполните следующую команду.

```bash
curl --url "smtps://smtp.gmail.com:465" --ssl-reqd --mail-from "from@gmail.com" --mail-rcpt "to@gmail.com" --user "from@gmail.com:xxxxxxxxxxxxxxxx" --upload-file mail.txt
```
※ Пожалуйста, замените xxxxxxxxxxxxxxxx на пароль вашего приложения.
