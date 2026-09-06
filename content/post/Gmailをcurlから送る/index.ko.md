---








title: "'curl로 Gmail 보내기'"
slug: "Gmailをcurlから送る"
date: 2025-02-27T02:13:31+09:00
tags: ["gmail", "curl"]
draft: false
image: "img.png"
categories: ["AI・기술"]
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
