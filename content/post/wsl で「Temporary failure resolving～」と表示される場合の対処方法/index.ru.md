---
title: "Как исправить ошибку 'Temporary failure resolving...' в WSL"
slug: "wsl で「Temporary failure resolving～」と表示される場合の対処方法"
date: 2024-03-31T16:57:33+09:00
tags: ["wsl", "устранение неполадок"]
draft: false
image: "img.png"
categories: ["Инструменты и среда разработки"]
---

# Как исправить ошибку 'Temporary failure resolving...' в WSL

`
kenji@MyComputer:~$ sudo apt update
[sudo] password for kenji:
Err:1 http://archive.ubuntu.com/ubuntu focal InRelease
  Temporary failure resolving 'archive.ubuntu.com'
`

Когда в WSL появляется вышеуказанная ошибка, возможно, неправильно настроен DNS-сервер.
В моей среде проблема была решена с помощью следующих шагов:

1. Запустите WSL.
2. Выполните команду `sudo nano /etc/resolv.conf`.
3. Измените строку `nameserver` следующим образом:
`
nameserver 8.8.8.8
`
4. Сохраните, нажав `Ctrl` + `S`, и выйдите, нажав `Ctrl` + `X`.
5. Выполните команду `sudo apt update`.
6. Если ошибка не появляется, проблема решена.

## Если вышеуказанные шаги не помогли

Кажется, в некоторых случаях вышеуказанные шаги не решают проблему. Пожалуйста, обратитесь к следующей статье.

- [Как решить проблему 'Temporary failure resolving...' при apt update в WSL](https://qiita.com/ryosukeYamazaki/items/c04ec3ff78aac6eb8d26)