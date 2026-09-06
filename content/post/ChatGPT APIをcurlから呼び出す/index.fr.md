---
title: "Appeler l'API ChatGPT depuis curl"
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
tags: ["ChatGPT", "API", "Commande"]
draft: false
image: "img.png"
categories: ["Programmation"]
---
# Appeler l'API ChatGPT depuis curl

Il est supposé que l'appel est effectué depuis l'invite de commande Windows.

```

curl https://api.openai.com/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer sk-proj-XXXXXXXXXXXXXXXXXXXX" -d "{""model"": ""gpt-3.5-turbo"",""messages"": [{""role"": ""system"", ""content"": ""Veuillez répondre dans le dialecte du Kansai.""}, {""role"": ""user"", ""content"": ""Insérez le message que vous souhaitez envoyer ici""}]}"

```
