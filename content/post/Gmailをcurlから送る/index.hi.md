---
slug: "Gmailをcurlから送る"
tags: ["gmail", "curl"]
draft: false
image: "img.webp"
categories: ["ai-technology"]
title: "curl से Gmail ईमेल भेजें"
date: "2025-02-27T02:13:31+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "curl के साथ Gmail SMTP से ईमेल भेजें: ऐप पासवर्ड, TLS, RFC 5322 संदेश फ़ाइल और Bash तथा Windows PowerShell कमांड।"
---

curl Gmail SMTP से जुड़कर पहले से तैयार संदेश फ़ाइल अपलोड कर सकता है। यह Gmail API का तरीका नहीं है। Google सामान्यतः OAuth 2.0 की सलाह देता है; नीचे का उदाहरण ऐसे खाते के मैन्युअल परीक्षण के लिए है जिसमें ऐप पासवर्ड उपलब्ध हो।

## प्रमाणीकरण विधि चुनें

SMTP के लिए अपने Google खाते का सामान्य पासवर्ड कभी न दें। ऐप समर्थन करे तो OAuth 2.0 को प्राथमिकता दें। मैन्युअल परीक्षण में, 2-Step Verification चालू होने पर ऐप पासवर्ड काम कर सकता है। इसे [Google Account app passwords](https://myaccount.google.com/apppasswords) से बनाएँ। यह विकल्प हर खाते में उपलब्ध नहीं होता; संगठन नीति या सुरक्षा सेटिंग इसे छिपा सकती है। Google अधिकांश उपयोगों के लिए ऐप पासवर्ड की सलाह नहीं देता। आवश्यकता खत्म होने पर इसे रद्द करें।

## संदेश फ़ाइल बनाएँ

SMTP अपलोड में curl संदेश नहीं बनाता और न ही उसे बदलता है। फ़ाइल में RFC 5322 प्रारूप के हेडर और संदेश का पाठ होना चाहिए। उदाहरण में ASCII पते हैं। `From` हेडर प्रमाणीकरण वाले Gmail खाते से मेल खाना चाहिए। ASCII से बाहर के विषय के लिए MIME encoding चाहिए।

इस संदेश को `mail.txt` नाम से सहेजें。

```text
From: sender@gmail.com
To: recipient@example.com
Subject: Test message
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8

This is a test message sent with curl.
```

## curl से भेजें

यह उदाहरण पोर्ट 465 पर implicit TLS उपयोग करता है। `--user` में केवल उपयोगकर्ता नाम देने पर curl पासवर्ड पूछता है; उस prompt पर ऐप पासवर्ड दर्ज करें। पोर्ट 587 के लिए `smtp://smtp.gmail.com:587` के साथ `--ssl-reqd` उपयोग करके STARTTLS माँगें।

### Bash, zsh, Linux और macOS

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

## क्रेडेंशियल सुरक्षित रखें

ऐप पासवर्ड को कमांड लाइन, संदेश फ़ाइल, shell history, repository या logs में न लिखें। curl के password prompt का उपयोग करें। निजी या गोपनीय जानकारी होने पर संदेश फ़ाइल को भी सुरक्षित रखें।

आधिकारिक दस्तावेज़: [Gmail SMTP settings and OAuth support](https://developers.google.com/workspace/gmail/imap/imap-smtp), [Google app passwords](https://support.google.com/accounts/answer/185833), [Gmail OAuth 2.0 for SMTP](https://developers.google.com/workspace/gmail/imap/xoauth2-protocol), and the [curl manual for --user and --upload-file](https://curl.se/docs/manpage.html).
