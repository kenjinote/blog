---
title: "Chamar a API do ChatGPT pelo curl"
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
tags: ["ChatGPT", "API", "Comando"]
draft: false
image: "img.png"
categories: ["Programação"]
---
# Chamar a API do ChatGPT pelo curl

Presume-se que a chamada seja feita a partir do prompt de comando do Windows.

```

curl https://api.openai.com/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer sk-proj-XXXXXXXXXXXXXXXXXXXX" -d "{""model"": ""gpt-3.5-turbo"",""messages"": [{""role"": ""system"", ""content"": ""Responda em dialeto Kansai.""}, {""role"": ""user"", ""content"": ""Insira a mensagem que deseja enviar aqui""}]}"

```
