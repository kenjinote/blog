---
title: 'Call ChatGPT API from curl'
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
tags: ["ChatGPT", "API", "Command"]
draft: false
image: "img.png"
categories: ["Programming"]
---
# Call ChatGPT API from curl

This assumes calling from the Windows Command Prompt.

```

curl https://api.openai.com/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer sk-proj-XXXXXXXXXXXXXXXXXXXX" -d "{""model"": ""gpt-3.5-turbo"",""messages"": [{""role"": ""system"", ""content"": ""Please answer in Kansai dialect.""}, {""role"": ""user"", ""content"": ""Insert the message you want to send here""}]}"

```
