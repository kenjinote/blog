---








title: 'Cómo llamar a la API de ChatGPT desde curl en la línea de comandos de Windows'
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
tags: ["ChatGPT", "API", "Comandos"]
draft: false
image: "img.webp"
categories: ["Programación"]
description: 'Explicamos cómo llamar a la API de ChatGPT de OpenAI desde el comando curl usando el símbolo del sistema (cmd) de Windows. Introducimos de forma sencilla los comandos necesarios y la configuración de parámetros.'
---








# Llamar a la API de ChatGPT desde curl

Se asume que se llama desde el símbolo del sistema de Windows.

```

curl https://api.openai.com/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer sk-proj-XXXXXXXXXXXXXXXXXXXX" -d "{""model"": ""gpt-3.5-turbo"",""messages"": [{""role"": ""system"", ""content"": ""Por favor, responde en dialecto de Kansai.""}, {""role"": ""user"", ""content"": ""Inserta el mensaje que deseas enviar aquí""}]}"

```
