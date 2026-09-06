---
title: '使用curl调用ChatGPT API'
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
tags: ["ChatGPT", "API", "命令"]
draft: false
image: "img.png"
categories: ["编程"]
---
# 使用curl调用ChatGPT API

前提是在Windows的命令提示符下调用。

```

curl https://api.openai.com/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer sk-proj-XXXXXXXXXXXXXXXXXXXX" -d "{""model"": ""gpt-3.5-turbo"",""messages"": [{""role"": ""system"", ""content"": ""请用关西腔回答。""}, {""role"": ""user"", ""content"": ""在此插入要发送的消息""}]}"

```
