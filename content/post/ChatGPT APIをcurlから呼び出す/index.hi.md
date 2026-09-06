---
title: "curl से ChatGPT API को कॉल करना"
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
tags: ["ChatGPT", "API", "कमांड"]
draft: false
image: "img.png"
categories: ["प्रोग्रामिंग"]
---
# curl से ChatGPT API को कॉल करना

यह मान कर चला जाता है कि इसे Windows के कमांड प्रॉम्प्ट से कॉल किया जा रहा है।

```

curl https://api.openai.com/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer sk-proj-XXXXXXXXXXXXXXXXXXXX" -d "{""model"": ""gpt-3.5-turbo"",""messages"": [{""role"": ""system"", ""content"": ""कृपया कंसाई बोली में उत्तर दें।""}, {""role"": ""user"", ""content"": ""यहां वह संदेश डालें जिसे आप भेजना चाहते हैं""}]}"

```
