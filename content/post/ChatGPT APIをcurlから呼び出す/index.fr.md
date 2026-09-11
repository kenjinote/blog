---
title: 'Comment appeler l''API ChatGPT avec curl dans l''invite de commande Windows'
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
tags: ["ChatGPT", "API", "Commande"]
draft: false
image: "img.webp"
categories: ["Programmation"]
description: 'Nous expliquons comment utiliser la commande curl depuis l''invite de commande Windows (cmd) pour appeler l''API ChatGPT d''OpenAI. Nous présentons clairement comment définir les commandes et les paramètres nécessaires.'
---
# Appeler l'API ChatGPT depuis curl

Il est supposé que l'appel est effectué depuis l'invite de commande Windows.

```

curl https://api.openai.com/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer sk-proj-XXXXXXXXXXXXXXXXXXXX" -d "{""model"": ""gpt-3.5-turbo"",""messages"": [{""role"": ""system"", ""content"": ""Veuillez répondre dans le dialecte du Kansai.""}, {""role"": ""user"", ""content"": ""Insérez le message que vous souhaitez envoyer ici""}]}"

```
