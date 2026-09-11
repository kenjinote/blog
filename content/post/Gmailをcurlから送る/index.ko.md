---








title: 'curl 명령을 사용하여 Gmail에서 이메일을 보내는 방법'
slug: "Gmailをcurlから送る"
date: 2025-02-27T02:13:31+09:00
tags: ["gmail", "curl"]
draft: false
image: "img.webp"
categories: ["AI・기술"]
description: '명령줄 도구인 ''curl''을 사용하여 Gmail 계정을 통해 이메일을 보내는 방법을 해설합니다. Google의 앱 비밀번호 취득 절차부터 curl의 옵션 지정이나 이메일 본문 파일 작성 및 전송 명령까지 자세히 소개합니다.'
---









# curl로 Gmail 보내기

## 1. 앱 비밀번호 얻기
https://myaccount.google.com/apppasswords
위의 링크를 클릭하여 앱 이름을 입력합니다.
생성된 비밀번호를 저장합니다.

## 2. curl 명령어로 메일 보내기
아래의 명령어를 실행합니다.

다음 예제에서는 mail.txt에 메일 내용을 작성합니다.

```mail.txt
From: from@gmail.com
To: to@gmail.com
Subject: 테스트 메일
Content-Type: text/plain; charset="UTF-8"

테스트 메일입니다.
```

위의 파일을 작성하고, 아래의 명령어를 실행합니다.

```bash
curl --url "smtps://smtp.gmail.com:465" --ssl-reqd --mail-from "from@gmail.com" --mail-rcpt "to@gmail.com" --user "from@gmail.com:xxxxxxxxxxxxxxxx" --upload-file mail.txt
```
※ xxxxxxxxxxxxxxxx는 앱 비밀번호로 바꿔주세요.
