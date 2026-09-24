---
title: 'How to Call ChatGPT API from curl in Windows Command Prompt'
date: "2026-09-24T19:44:38+09:00"
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
tags: ["ChatGPT", "API", "Command"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'We explain how to call OpenAI''s ChatGPT API from the curl command using the Windows Command Prompt (cmd). We introduce how to set up the necessary commands and parameters in an easy-to-understand manner.'
---
# Call ChatGPT API from curl

This assumes calling from the Windows Command Prompt.

```

curl https://api.openai.com/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer sk-proj-XXXXXXXXXXXXXXXXXXXX" -d "{""model"": ""gpt-3.5-turbo"",""messages"": [{""role"": ""system"", ""content"": ""Please answer in Kansai dialect.""}, {""role"": ""user"", ""content"": ""Insert the message you want to send here""}]}"

```
