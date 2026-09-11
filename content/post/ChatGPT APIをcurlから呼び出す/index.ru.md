---
title: 'Как вызвать ChatGPT API через curl в командной строке Windows'
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
tags: ["ChatGPT", "API", "Команда"]
draft: false
image: "img.webp"
categories: ["Программирование"]
description: 'В этой статье объясняется, как вызвать ChatGPT API от OpenAI через команду curl, используя командную строку Windows (cmd). Понятно описываются необходимые команды и способы настройки параметров.'
---
# Вызов API ChatGPT из curl

Предполагается вызов из командной строки Windows.

```

curl https://api.openai.com/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer sk-proj-XXXXXXXXXXXXXXXXXXXX" -d "{""model"": ""gpt-3.5-turbo"",""messages"": [{""role"": ""system"", ""content"": ""Пожалуйста, отвечайте на кансайском диалекте.""}, {""role"": ""user"", ""content"": ""Вставьте сюда сообщение, которое хотите отправить""}]}"

```
