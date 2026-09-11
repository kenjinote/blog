---








title: 'Windows 명령 프롬프트에서 curl로 ChatGPT API를 호출하는 방법'
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
tags: ["ChatGPT", "API", "명령어"]
draft: false
image: "img.webp"
categories: ["프로그래밍"]
description: 'Windows 명령 프롬프트(cmd)를 사용하여 curl 명령으로 OpenAI의 ChatGPT API를 호출하는 방법을 해설합니다. 필요한 명령어나 매개변수 설정 방법을 알기 쉽게 소개합니다.'
---








# ChatGPT API를 curl로 호출하기

Windows 명령 프롬프트에서 호출하는 것을 전제로 합니다.

```

curl https://api.openai.com/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer sk-proj-XXXXXXXXXXXXXXXXXXXX" -d "{""model"": ""gpt-3.5-turbo"",""messages"": [{""role"": ""system"", ""content"": ""간사이 사투리로 대답해 주세요.""}, {""role"": ""user"", ""content"": ""여기에 보낼 메시지를 입력하세요""}]}"

```
