---
slug: "Gmailをcurlから送る"
tags: ["gmail", "curl"]
draft: false
image: "img.webp"
categories: ["ai-technology"]
title: "使用 curl 从 Gmail 发送邮件"
date: "2025-02-27T02:13:31+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "介绍如何通过 curl 和 Gmail SMTP 发送邮件，包括应用专用密码、TLS、RFC 5322 邮件文件，以及 Bash 和 Windows PowerShell 命令。"
---

curl 可以连接 Gmail SMTP 并上传预先准备好的邮件文件。这不是 Gmail API。Google 通常建议使用 OAuth 2.0；以下示例适合使用应用专用密码的账户进行手动测试。

## 选择身份验证方式

不要在 SMTP 中使用 Google 账户的常规密码。若应用支持，请优先使用 OAuth 2.0。手动测试时，如果账户已启用两步验证，可以使用应用专用密码。请在[Google 账户应用专用密码](https://myaccount.google.com/apppasswords)中创建。并非所有账户都能使用此选项；组织政策或安全设置可能会隐藏该选项。Google 不建议在大多数情况下使用应用专用密码。不再需要时请撤销。

## 创建邮件文件

通过 SMTP 上传时，curl 不会编写或转换邮件。文件必须包含 RFC 5322 格式的邮件头和正文。示例使用 ASCII 地址。`From` 邮件头应与用于身份验证的 Gmail 账户一致。非 ASCII 主题需要 MIME 编码。

将此内容保存为 `mail.txt`。

```text
From: sender@gmail.com
To: recipient@example.com
Subject: Test message
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8

This is a test message sent with curl.
```

## 使用 curl 发送

此示例使用 465 端口的隐式 TLS。`--user`只提供用户名时，curl 会提示输入密码；请在提示处输入应用专用密码。使用 587 端口时，改用`smtp://smtp.gmail.com:587`并添加`--ssl-reqd`以请求 STARTTLS。

### Bash、zsh、Linux 和 macOS

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

## 保护凭据

不要将应用专用密码写在命令行、邮件文件、shell 历史、代码仓库或日志中。使用 curl 的密码提示。若邮件文件包含个人或机密信息，也请妥善保护。

官方文档： [Gmail SMTP settings and OAuth support](https://developers.google.com/workspace/gmail/imap/imap-smtp), [Google app passwords](https://support.google.com/accounts/answer/185833), [Gmail OAuth 2.0 for SMTP](https://developers.google.com/workspace/gmail/imap/xoauth2-protocol), and the [curl manual for --user and --upload-file](https://curl.se/docs/manpage.html).
