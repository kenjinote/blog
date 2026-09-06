---



title: "'ChatGPT API를 curl로 호출하기'"
date: 2025-02-01T17:15:34+09:00
tags: ["ChatGPT", "API", "명령어"]
draft: false
image: "img.png"
categories: ["프로그래밍"]
---



# ChatGPT API를 curl로 호출하기

Windows 명령 프롬프트에서 호출하는 것을 전제로 합니다.

```

curl https://api.openai.com/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer sk-proj-XXXXXXXXXXXXXXXXXXXX" -d "{""model"": ""gpt-3.5-turbo"",""messages"": [{""role"": ""system"", ""content"": ""간사이 사투리로 대답해 주세요.""}, {""role"": ""user"", ""content"": ""여기에 보낼 메시지를 입력하세요""}]}"

```
