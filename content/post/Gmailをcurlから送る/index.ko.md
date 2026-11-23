---









slug: "Gmailをcurlから送る"
tags: ["gmail", "curl"]
draft: false
image: "img.webp"
categories: ["ai-technology"]
title: "curl로 Gmail에서 이메일 보내기"
date: "2025-02-27T02:13:31+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "curl과 Gmail SMTP로 이메일을 보내는 방법을 설명합니다. 앱 비밀번호, TLS, RFC 5322 메시지 파일, Bash와 Windows PowerShell 명령을 다룹니다."
---

curl은 Gmail SMTP 서버에 연결해 미리 작성한 메시지 파일을 업로드할 수 있습니다. Gmail API 사용법은 아닙니다. Google은 일반적으로 OAuth 2.0을 권장하며, 아래 예제는 앱 비밀번호를 사용할 수 있는 계정에서 수동 테스트할 때를 위한 것입니다.

## 인증 방식 선택

SMTP에 Google 계정의 일반 비밀번호를 사용하지 마세요. 앱이 지원하면 OAuth 2.0을 우선 사용하세요. 수동 테스트에서는 2단계 인증이 설정된 계정에 한해 앱 비밀번호를 사용할 수 있습니다. [Google 계정 앱 비밀번호](https://myaccount.google.com/apppasswords)에서 만드세요. 모든 계정에서 사용할 수 있는 것은 아니며 조직 정책이나 보안 설정으로 메뉴가 보이지 않을 수 있습니다. Google은 대부분의 경우 앱 비밀번호를 권장하지 않습니다. 사용이 끝나면 취소하세요.

## 메시지 파일 만들기

SMTP 업로드에서 curl은 메시지를 작성하거나 변환하지 않습니다. 파일에 RFC 5322 형식의 헤더와 본문을 직접 넣어야 합니다. 예제는 ASCII 주소를 사용합니다. `From` 헤더는 인증에 사용하는 Gmail 계정과 일치시킵니다. ASCII가 아닌 제목에는 MIME 인코딩이 필요합니다.

이 내용을 `mail.txt` 파일로 저장하세요.

```text
From: sender@gmail.com
To: recipient@example.com
Subject: Test message
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8

This is a test message sent with curl.
```

## curl로 전송하기

이 예제는 465 포트에서 암시적 TLS를 사용합니다. `--user`에 사용자 이름만 넣으면 curl이 비밀번호를 묻습니다. 그때 앱 비밀번호를 입력하세요. 587 포트에서는 `smtp://smtp.gmail.com:587`과 `--ssl-reqd`를 사용해 STARTTLS를 요청합니다.

### Bash, zsh, Linux 및 macOS

```bash
curl --url "smtps://smtp.gmail.com:465" \
  --mail-from "sender@gmail.com" \
  --mail-rcpt "recipient@example.com" \
  --user "sender@gmail.com" \
  --upload-file mail.txt
```

### Windows PowerShell

```powershell
curl.exe --url "smtps://smtp.gmail.com:465" --mail-from "sender@gmail.com" --mail-rcpt "recipient@example.com" --user "sender@gmail.com" --upload-file "mail.txt"
```

## 자격 증명 보호하기

앱 비밀번호를 명령줄, 메시지 파일, 셸 기록, 저장소 또는 로그에 쓰지 마세요. curl의 비밀번호 입력 프롬프트를 사용하세요. 메시지 파일에 개인정보나 기밀이 있으면 파일도 안전하게 보관하세요.

공식 문서: [Gmail SMTP settings and OAuth support](https://developers.google.com/workspace/gmail/imap/imap-smtp), [Google app passwords](https://support.google.com/accounts/answer/185833), [Gmail OAuth 2.0 for SMTP](https://developers.google.com/workspace/gmail/imap/xoauth2-protocol), and the [curl manual for --user and --upload-file](https://curl.se/docs/manpage.html).
