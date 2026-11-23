---
slug: "Gmailをcurlから送る"
tags: ["gmail", "curl"]
draft: false
image: "img.webp"
categories: ["ai-technology"]
title: "使用 curl 從 Gmail 寄送電子郵件"
date: "2025-02-27T02:13:31+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "說明如何透過 curl 與 Gmail SMTP 寄信，涵蓋應用程式密碼、TLS、RFC 5322 郵件檔，以及 Bash 和 Windows PowerShell 指令。"
---

curl 可以連線到 Gmail SMTP 並上傳事先準備好的郵件檔。這不是 Gmail API。Google 通常建議使用 OAuth 2.0；以下範例適合可使用應用程式密碼的帳戶進行手動測試。

## 選擇驗證方式

不要在 SMTP 中使用 Google 帳戶的一般密碼。若應用程式支援，請優先使用 OAuth 2.0。手動測試時，若帳戶已啟用兩步驟驗證，可使用應用程式密碼。請至 [Google 帳戶應用程式密碼](https://myaccount.google.com/apppasswords)建立。並非所有帳戶都能使用此選項；組織政策或安全設定可能會隱藏該選項。Google 不建議在大多數情況下使用應用程式密碼。不再需要時請撤銷。

## 建立郵件檔

透過 SMTP 上傳時，curl 不會撰寫或轉換郵件。檔案必須包含 RFC 5322 格式的郵件標頭與內文。範例使用 ASCII 地址。`From` 標頭應與用於驗證的 Gmail 帳戶一致。非 ASCII 主旨需要 MIME 編碼。

將此內容儲存為 `mail.txt`。

```text
From: sender@gmail.com
To: recipient@example.com
Subject: Test message
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8

This is a test message sent with curl.
```

## 使用 curl 寄送

此範例使用 465 埠的隱含 TLS。`--user`只提供使用者名稱時，curl 會提示輸入密碼；請在提示處輸入應用程式密碼。若使用 587 埠，請改用`smtp://smtp.gmail.com:587`並加入`--ssl-reqd`以要求 STARTTLS。

### Bash、zsh、Linux 與 macOS

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

## 保護認證資訊

不要將應用程式密碼寫在命令列、郵件檔、shell 歷程、程式碼儲存庫或記錄中。請使用 curl 的密碼提示。若郵件檔包含個人或機密資訊，也請妥善保護。

官方文件： [Gmail SMTP settings and OAuth support](https://developers.google.com/workspace/gmail/imap/imap-smtp), [Google app passwords](https://support.google.com/accounts/answer/185833), [Gmail OAuth 2.0 for SMTP](https://developers.google.com/workspace/gmail/imap/xoauth2-protocol), and the [curl manual for --user and --upload-file](https://curl.se/docs/manpage.html).
