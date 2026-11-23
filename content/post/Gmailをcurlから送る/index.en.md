---
slug: "Gmailをcurlから送る"
tags: ["gmail", "curl"]
draft: false
image: "img.webp"
categories: ["ai-technology"]
title: "Send Email from Gmail with curl"
date: "2025-02-27T02:13:31+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Send a message through Gmail SMTP with curl. Learn about app-password eligibility, TLS, RFC 5322 message files, and commands for Bash and Windows PowerShell."
---

curl can connect to Gmail SMTP and upload a message file you prepare. This is not the Gmail API. Google generally recommends OAuth 2.0; the example below is for a manual test with an account that can use an app password.

## Choose an authentication method

Never use your normal Google Account password for SMTP. Prefer OAuth 2.0 when your application supports it. For a quick manual test, an app password may work if 2-Step Verification is enabled on your Google Account. Create one at [Google Account app passwords](https://myaccount.google.com/apppasswords). The option is not available for every account; organization policy or account security settings may hide it. Google does not recommend app passwords for most uses. Revoke one when you no longer need it.

## Create the message file

For SMTP uploads, curl does not compose or convert the message. The file must contain the message headers and body in RFC 5322 format. This example uses ASCII addresses. Keep the `From` header aligned with the Gmail account used to authenticate. A non-ASCII subject needs MIME header encoding.

Save this message as `mail.txt`.

```text
From: sender@gmail.com
To: recipient@example.com
Subject: Test message
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8

This is a test message sent with curl.
```

## Send with curl

This example uses implicit TLS on port 465. Since `--user` includes only the username, curl prompts for a password; enter the app password at that prompt. For port 587, use `smtp://smtp.gmail.com:587` with `--ssl-reqd` to request STARTTLS.

### Bash, zsh, Linux, and macOS

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

## Protect credentials

Do not put an app password in a command line, message file, shell history, repository, or log. Use curl’s password prompt. Protect the message file too, especially if it contains personal or confidential information.

Official documentation: [Gmail SMTP settings and OAuth support](https://developers.google.com/workspace/gmail/imap/imap-smtp), [Google app passwords](https://support.google.com/accounts/answer/185833), [Gmail OAuth 2.0 for SMTP](https://developers.google.com/workspace/gmail/imap/xoauth2-protocol), and the [curl manual for --user and --upload-file](https://curl.se/docs/manpage.html).
