---
title: "Вызов API ChatGPT из curl"
slug: "вызов-api-chatgpt-из-curl"
date: 2025-02-01T17:15:34+09:00
tags: ["ChatGPT", "API", "Команда"]
draft: false
image: "img.png"
categories: ["Программирование"]
---
# Вызов API ChatGPT из curl

Предполагается вызов из командной строки Windows.

```

curl https://api.openai.com/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer sk-proj-XXXXXXXXXXXXXXXXXXXX" -d "{""model"": ""gpt-3.5-turbo"",""messages"": [{""role"": ""system"", ""content"": ""Пожалуйста, отвечайте на кансайском диалекте.""}, {""role"": ""user"", ""content"": ""Вставьте сюда сообщение, которое хотите отправить""}]}"

```
