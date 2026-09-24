---
title: 'Cara Memanggil API ChatGPT dari curl di Command Prompt Windows'
slug: "ChatGPT APIをcurlから呼び出す"
date: "2026-09-24T16:08:36+09:00"
tags: ["ChatGPT", "API", "Perintah"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Menjelaskan cara memanggil API ChatGPT dari OpenAI melalui perintah curl menggunakan Command Prompt (cmd) Windows. Kami memperkenalkan dengan mudah perintah yang diperlukan dan cara mengatur parameternya.'
---
# Memanggil API ChatGPT dari curl

Ini diasumsikan dipanggil dari command prompt Windows.

```

curl https://api.openai.com/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer sk-proj-XXXXXXXXXXXXXXXXXXXX" -d "{""model"": ""gpt-3.5-turbo"",""messages"": [{""role"": ""system"", ""content"": ""Tolong jawab dalam dialek Kansai.""}, {""role"": ""user"", ""content"": ""Masukkan pesan yang ingin Anda kirim di sini""}]}"

```
