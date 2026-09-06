---
title: 'Send Gmail from curl'
slug: "Gmailをcurlから送る"
date: 2025-02-27T02:13:31+09:00
tags: ["gmail", "curl"]
draft: false
image: "img.png"
categories: ["AI & Technology"]
---

# Send Gmail from curl

## 1. Get an App Password
https://myaccount.google.com/apppasswords
Click the link above and enter an app name.
Save the generated password.

## 2. Send an email with the curl command
Run the following command.

In the example below, the email content is written in `mail.txt`.

```mail.txt
From: from@gmail.com
To: to@gmail.com
Subject: Test Email
Content-Type: text/plain; charset="UTF-8"

This is a test email.
```

Create the above file and run the following command.

```bash
curl --url "smtps://smtp.gmail.com:465" --ssl-reqd --mail-from "from@gmail.com" --mail-rcpt "to@gmail.com" --user "from@gmail.com:xxxxxxxxxxxxxxxx" --upload-file mail.txt
```
* Replace xxxxxxxxxxxxxxxx with your app password.
