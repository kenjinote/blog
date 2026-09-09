---
title: '使用curl命令通过Gmail发送邮件的方法'
slug: "Gmailをcurlから送る"
date: 2025-02-27T02:13:31+09:00
tags: ["gmail", "curl"]
draft: false
image: "img.webp"
categories: ["AI・技术"]
description: '本文讲解如何使用命令行工具“curl”通过Gmail账号发送邮件。详细介绍从获取Google应用密码的步骤，到指定curl选项和创建/发送邮件正文文件的命令。'
---

# 使用curl发送Gmail

## 1. 获取应用专用密码
https://myaccount.google.com/apppasswords
点击上面的链接，然后输入应用名称。
保存生成的密码。

## 2. 使用curl命令发送邮件
执行以下命令。

在下面的示例中，邮件内容写在mail.txt中。

```mail.txt
From: from@gmail.com
To: to@gmail.com
Subject: 测试邮件
Content-Type: text/plain; charset="UTF-8"

这是一封测试邮件。
```

创建上述文件后，执行以下命令。

```bash
curl --url "smtps://smtp.gmail.com:465" --ssl-reqd --mail-from "from@gmail.com" --mail-rcpt "to@gmail.com" --user "from@gmail.com:xxxxxxxxxxxxxxxx" --upload-file mail.txt
```
※ 请将xxxxxxxxxxxxxxxx替换为应用专用密码。
