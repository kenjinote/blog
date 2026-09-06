---




title: "TeamViewer로 간단한 원격 연결"
date: 2023-01-13T01:45:00+09:00
tags: ["TeamViewer", "명령어", "원격 연결"]
draft: false
image: "img.png"
categories: ["IT·테크놀로지"]
---





# TeamViewer로 간단한 원격 연결

TeamViewer를 사용하면 원격 데스크톱 연결을 간단하게 할 수 있습니다.

원격 대상과 원격 주체에서 TeamViewer를 실행하고,
원격 주체에서 원격 대상의 ID와 비밀번호를 입력하면 원격 연결이 가능합니다.

명령줄에서 원격 연결을 할 경우에는 다음과 같이 합니다.

```text
%ProgramFiles%\TeamViewer\TeamViewer.exe -i <ID> -P <Password>
```
`<ID>`에는 원격 대상의 ID를, `<Password>`에는 원격 대상의 비밀번호를 입력합니다.

위의 명령어로 바로가기 파일을 만들어 두면, ID/PW 입력을 생략할 수 있어 편리합니다.

참고 사이트: [Command line parameters](https://community.teamviewer.com/English/kb/articles/34447-command-line-parameters)
