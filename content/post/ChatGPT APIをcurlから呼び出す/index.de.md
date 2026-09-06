---
title: "ChatGPT API über curl aufrufen"
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
tags: ["ChatGPT", "API", "Befehl"]
draft: false
image: "img.png"
categories: ["Programmierung"]
---
# ChatGPT API über curl aufrufen

Es wird davon ausgegangen, dass der Aufruf über die Windows-Eingabeaufforderung erfolgt.

```

curl https://api.openai.com/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer sk-proj-XXXXXXXXXXXXXXXXXXXX" -d "{""model"": ""gpt-3.5-turbo"",""messages"": [{""role"": ""system"", ""content"": ""Bitte im Kansai-Dialekt antworten.""}, {""role"": ""user"", ""content"": ""Fügen Sie hier die Nachricht ein, die Sie senden möchten""}]}"

```
