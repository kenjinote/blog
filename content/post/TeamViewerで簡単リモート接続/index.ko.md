---
title: '[초보자용] TeamViewer로 간단하게 원격 데스크톱에 연결하는 방법'
date: 2023-01-13T01:45:00+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "TeamViewerで簡単원격 연결"
tags: ["TeamViewer", "명령어", "원격 연결"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'TeamViewer를 사용하여 간단하게 원격 데스크톱 연결을 하는 방법을 설명합니다. 명령줄에서 ID나 비밀번호를 지정하고 바로가기로 연결을 자동화 및 간소화하는 유용한 팁도 함께 소개합니다.'
---
## Windows 명령줄 연결

TeamViewer의 공식 Windows 명령줄 문서에 따르면 정식 버전은 명령 프롬프트, 스크립트 또는 바로가기로 실행할 수 있습니다.

이 예시는 설치 폴더의 `TeamViewer.exe`를 실행합니다. `<ID>`에는 연결할 상대 ID를, `<Password>`에는 비밀번호를 입력합니다. TeamViewer가 다른 위치에 설치되어 있다면 실행 파일 경로를 바꾸세요.

```cmd
"%ProgramFiles%\TeamViewer\TeamViewer.exe" -i <ID> -p <Password>
```

`-p`를 생략하면 Easy Access를 사용할 수 있는 경우 이를 사용하고, 그렇지 않으면 비밀번호 입력을 요청합니다.

비밀번호가 포함된 바로가기에는 비밀번호가 읽을 수 있는 형태로 저장됩니다. 공유하거나 다른 사람이 읽을 수 있는 곳에 두지 마세요. 반복적인 무인 접속이 필요하면 비밀번호를 저장하는 대신 기기를 계정에 할당하고 Easy Access, 허용 목록, 다중 인증을 사용하는 방법을 고려하세요.

## 공식 참고 자료

- [TeamViewer command-line parameters](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/for-developers/command-line-parameters/)
- [Best practices for secure unattended access](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-classic/security/best-practices/best-practices-for-secure-unattended-access/)
- [TeamViewer security statement](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/security/security-statement/)
