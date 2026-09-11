---
title: 'Windows कमांड प्रॉम्प्ट में curl से ChatGPT API को कॉल करने का तरीका'
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
tags: ["ChatGPT", "API", "कमांड"]
draft: false
image: "img.webp"
categories: ["प्रोग्रामिंग"]
description: 'हम बताएंगे कि Windows कमांड प्रॉम्प्ट (cmd) का उपयोग करके curl कमांड से OpenAI के ChatGPT API को कैसे कॉल करें। हम आवश्यक कमांड और पैरामीटर सेट करने के तरीके स्पष्ट रूप से प्रस्तुत करेंगे。'
---
# curl से ChatGPT API को कॉल करना

यह मान कर चला जाता है कि इसे Windows के कमांड प्रॉम्प्ट से कॉल किया जा रहा है।

```

curl https://api.openai.com/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer sk-proj-XXXXXXXXXXXXXXXXXXXX" -d "{""model"": ""gpt-3.5-turbo"",""messages"": [{""role"": ""system"", ""content"": ""कृपया कंसाई बोली में उत्तर दें।""}, {""role"": ""user"", ""content"": ""यहां वह संदेश डालें जिसे आप भेजना चाहते हैं""}]}"

```
