---
slug: "Gmailをcurlから送る"
tags: ["gmail", "curl"]
draft: false
image: "img.webp"
categories: ["ai-technology"]
title: "curlでGmailからメールを送信する方法"
date: "2025-02-27T02:13:31+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "curlでGmail SMTPからメールを送る方法を解説。アプリパスワード、TLS接続、RFC 5322形式の本文ファイル、bashとWindows PowerShellのコマンドを紹介します。"
---

curlはGmail SMTPサーバーへ接続し、作成済みのメールファイルを送信できます。これはGmail APIの使い方ではありません。Googleは通常OAuth 2.0を推奨しています。以下は、アプリパスワードを利用できるアカウントで手動テストする場合の例です。

## 認証方法を選ぶ

Googleアカウントの通常パスワードをSMTPに渡してはいけません。OAuth 2.0を使えるアプリではOAuthを優先してください。手動の簡単なテストでアプリパスワードを使う場合は、Googleアカウントで2段階認証を有効にし、[アプリパスワード](https://myaccount.google.com/apppasswords)を作成します。アプリパスワードは利用可能なアカウントに限られ、組織のポリシーなどで項目が表示されない場合があります。Googleはアプリパスワードの利用を推奨しておらず、不要になったら取り消してください。

## メールファイルを作る

SMTPへのアップロードでは、curlはメール本文を自動生成・変換しません。ファイルにはRFC 5322形式のヘッダーと本文を記述します。ASCIIの宛先を例にしています。送信元ヘッダーは認証するGmailアドレスと一致させてください。日本語の件名にはMIMEエンコードが必要です。

`mail.txt`という名前で保存します。

```text
From: sender@gmail.com
To: recipient@example.com
Subject: Test message
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8

This is a test message sent with curl.
```

## curlで送信する

この例は465番ポートの暗黙TLSを使います。`--user`にはユーザー名だけを指定するため、curlがパスワード入力を促します。プロンプトにアプリパスワードを入力します。587番ポートを使う場合は`smtp://smtp.gmail.com:587`と`--ssl-reqd`を使ってSTARTTLSに切り替えます。

### Bash、zsh、Linux、macOS

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

## 認証情報を安全に扱う

コマンド行、メールファイル、シェル履歴、リポジトリへアプリパスワードを書かないでください。curlの認証プロンプトを使い、共有端末では入力後に画面を離席しないでください。メール本文ファイルにも個人情報や機密情報を残さないよう注意します。

公式資料： [GmailのSMTP設定とOAuth対応](https://developers.google.com/workspace/gmail/imap/imap-smtp), [Googleアプリパスワード](https://support.google.com/accounts/answer/185833), [Gmail SMTPのOAuth 2.0](https://developers.google.com/workspace/gmail/imap/xoauth2-protocol)、および[curlの--userと--upload-fileのマニュアル](https://curl.se/docs/manpage.html).
