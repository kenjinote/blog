---
title: 'Gmailをcurlから送る'
date: 2025-02-27T02:13:31+09:00
tags: ["gmail", "curl"]
draft: false
image: "img.png"
---

# Gmailをcurlから送る

## 1. アプリパスワードを取得する
https://myaccount.google.com/apppasswords
上記のリンクをクリックして、アプリ名を入力します。
生成したパスワードを保存します。

## 2. curlコマンドでメールを送信する
以下のコマンドを実行します。

下記の例では、mail.txtにメールの内容を記述しています。

```mail.txt
From: from@gmail.com
To: to@gmail.com
Subject: テストメール
Content-Type: text/plain; charset="UTF-8"

テストメールです。
```

上記のファイルを作成して、以下のコマンドを実行します。

```bash
curl --url "smtps://smtp.gmail.com:465" --ssl-reqd --mail-from "from@gmail.com" --mail-rcpt "to@gmail.com" --user "from@gmail.com:xxxxxxxxxxxxxxxx" --upload-file mail.txt
```
※ xxxxxxxxxxxxxxxxはアプリパスワードに置き換えてください。