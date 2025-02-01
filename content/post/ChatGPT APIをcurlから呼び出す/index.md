---
title: 'ChatGPT APIをcurlから呼び出す'
date: 2025-02-01T17:15:34+09:00
tags: ["ChatGPT", "API", "コマンド"]
draft: false
image: "img.png"
---
# ChatGPT APIをcurlから呼び出す

Windowsのコマンドプロンプトから呼び出すことを前提としています。

```

curl https://api.openai.com/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer sk-proj-XXXXXXXXXXXXXXXXXXXX" -d "{""model"": ""gpt-3.5-turbo"",""messages"": [{""role"": ""system"", ""content"": ""関西弁で答えてください。""}, {""role"": ""user"", ""content"": ""ここに送りたいメッセージを挿入する""}]}"

```