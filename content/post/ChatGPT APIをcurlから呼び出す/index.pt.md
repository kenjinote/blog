---
title: 'Como Chamar a API do ChatGPT com o comando curl no Prompt de Comando do Windows'
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
tags: ["ChatGPT", "API", "Comando"]
draft: false
image: "img.webp"
categories: ["Programação"]
description: 'Aprenda a chamar a API do ChatGPT da OpenAI via comando curl usando o Prompt de Comando do Windows (cmd). Mostramos de forma clara como configurar os comandos e parâmetros necessários.'
---
# Chamar a API do ChatGPT pelo curl

Presume-se que a chamada seja feita a partir do prompt de comando do Windows.

```

curl https://api.openai.com/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer sk-proj-XXXXXXXXXXXXXXXXXXXX" -d "{""model"": ""gpt-3.5-turbo"",""messages"": [{""role"": ""system"", ""content"": ""Responda em dialeto Kansai.""}, {""role"": ""user"", ""content"": ""Insira a mensagem que deseja enviar aqui""}]}"

```
