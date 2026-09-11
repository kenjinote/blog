---
title: 'كيفية استدعاء واجهة برمجة تطبيقات ChatGPT باستخدام curl في موجه أوامر Windows'
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
tags: ["ChatGPT", "API", "أمر"]
draft: false
image: "img.webp"
categories: ["برمجة"]
description: 'نشرح كيفية استدعاء ChatGPT API الخاص بـ OpenAI من خلال أمر curl باستخدام موجه أوامر Windows (cmd). سنعرض بشكل مبسط الأوامر المطلوبة وكيفية إعداد المعلمات.'
---
# استدعاء واجهة برمجة تطبيقات ChatGPT من curl

يفترض هذا استدعاءه من موجه أوامر Windows.

```

curl https://api.openai.com/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer sk-proj-XXXXXXXXXXXXXXXXXXXX" -d "{""model"": ""gpt-3.5-turbo"",""messages"": [{""role"": ""system"", ""content"": ""يرجى الإجابة بلهجة كانساي.""}, {""role"": ""user"", ""content"": ""أدخل الرسالة التي تريد إرسالها هنا""}]}"

```
