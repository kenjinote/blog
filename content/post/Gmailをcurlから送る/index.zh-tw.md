---
title: "透過 curl 發送 Gmail"
slug: "透過-curl-發送-gmail"
date: 2025-02-27T02:13:31+09:00
tags: ["gmail", "curl"]
draft: false
image: "img.png"
categories: ["AI 與科技"]
---

# 透過 curl 發送 Gmail

## 1. 取得應用程式密碼
https://myaccount.google.com/apppasswords
點擊上方連結，並輸入應用程式名稱。
儲存產生的密碼。

## 2. 使用 curl 指令發送電子郵件
執行以下指令。

在下面的範例中，郵件內容寫在 mail.txt 中。

```mail.txt
From: from@gmail.com
To: to@gmail.com
Subject: 測試郵件
Content-Type: text/plain; charset="UTF-8"

這是一封測試郵件。
```

建立上述檔案後，執行以下指令。

```bash
curl --url "smtps://smtp.gmail.com:465" --ssl-reqd --mail-from "from@gmail.com" --mail-rcpt "to@gmail.com" --user "from@gmail.com:xxxxxxxxxxxxxxxx" --upload-file mail.txt
```
※ 請將 xxxxxxxxxxxxxxxx 替換為您的應用程式密碼。
