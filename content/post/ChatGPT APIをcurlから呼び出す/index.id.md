---
title: "Memanggil API ChatGPT dari curl"
slug: "memanggil-api-chatgpt-dari-curl"
date: 2025-02-01T17:15:34+09:00
tags: ["ChatGPT", "API", "Perintah"]
draft: false
image: "img.png"
categories: ["Pemrograman"]
---
# Memanggil API ChatGPT dari curl

Ini diasumsikan dipanggil dari command prompt Windows.

```

curl https://api.openai.com/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer sk-proj-XXXXXXXXXXXXXXXXXXXX" -d "{""model"": ""gpt-3.5-turbo"",""messages"": [{""role"": ""system"", ""content"": ""Tolong jawab dalam dialek Kansai.""}, {""role"": ""user"", ""content"": ""Masukkan pesan yang ingin Anda kirim di sini""}]}"

```
