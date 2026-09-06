---
title: "透過 curl 呼叫 ChatGPT API"
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
tags: ["ChatGPT", "API", "命令"]
draft: false
image: "img.png"
categories: ["程式設計"]
---
# 透過 curl 呼叫 ChatGPT API

本文假設從 Windows 的命令提示字元呼叫。

```

curl https://api.openai.com/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer sk-proj-XXXXXXXXXXXXXXXXXXXX" -d "{""model"": ""gpt-3.5-turbo"",""messages"": [{""role"": ""system"", ""content"": ""請用關西腔回答。""}, {""role"": ""user"", ""content"": ""在此插入您要發送的訊息""}]}"

```
