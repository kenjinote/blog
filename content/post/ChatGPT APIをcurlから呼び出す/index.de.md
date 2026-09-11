---
title: 'Wie man die ChatGPT API über curl in der Windows-Eingabeaufforderung aufruft'
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
tags: ["ChatGPT", "API", "Befehl"]
draft: false
image: "img.webp"
categories: ["Programmierung"]
description: 'Wir erklären, wie man die ChatGPT API von OpenAI über den curl-Befehl in der Windows-Eingabeaufforderung (cmd) aufruft. Wir stellen die benötigten Befehle und die Konfiguration der Parameter leicht verständlich vor.'
---
# ChatGPT API über curl aufrufen

Es wird davon ausgegangen, dass der Aufruf über die Windows-Eingabeaufforderung erfolgt.

```

curl https://api.openai.com/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer sk-proj-XXXXXXXXXXXXXXXXXXXX" -d "{""model"": ""gpt-3.5-turbo"",""messages"": [{""role"": ""system"", ""content"": ""Bitte im Kansai-Dialekt antworten.""}, {""role"": ""user"", ""content"": ""Fügen Sie hier die Nachricht ein, die Sie senden möchten""}]}"

```
