---
title: "TeamViewer के साथ आसान रिमोट कनेक्शन"
slug: "TeamViewer के साथ आसान रिमोट कनेक्शन"
date: 2023-01-13T01:45:00+09:00
tags: ["TeamViewer", "कमांड", "रिमोट कनेक्शन"]
draft: false
image: "img.png"
categories: ["आईटी・प्रौद्योगिकी"]
---

# TeamViewer के साथ आसान रिमोट कनेक्शन

TeamViewer का उपयोग करके रिमोट डेस्कटॉप कनेक्शन आसानी से किया जा सकता है।

रिमोट गंतव्य और रिमोट स्रोत दोनों पर TeamViewer शुरू करें,
रिमोट स्रोत पर रिमोट गंतव्य का ID और पासवर्ड दर्ज करने पर रिमोट कनेक्शन किया जा सकता है।

कमांड लाइन के माध्यम से रिमोट कनेक्ट करने के लिए, निम्न कार्य करें:

```
%ProgramFiles%\TeamViewer\TeamViewer.exe -i <ID> -P <Password>
```
`<ID>` में रिमोट गंतव्य का ID दर्ज करें, और `<Password>` में रिमोट गंतव्य का पासवर्ड दर्ज करें।

यदि आप उपरोक्त कमांड का उपयोग करके एक शॉर्टकट फ़ाइल बनाते हैं, तो यह सुविधाजनक है क्योंकि आप ID/PW दर्ज करने से बच सकते हैं।

संदर्भ साइट: [Command line parameters](https://community.teamviewer.com/English/kb/articles/34447-command-line-parameters)
