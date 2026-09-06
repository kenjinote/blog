---





title: "'【HUGO】로컬 환경에서 표시 프리뷰'"
slug: "【HUGO】ローカルで環境で表示プレビュー"
date: 2022-09-05T12:28:01+09:00
tags: ["HUGO"]
draft: false
image: "img.png"
categories: ["블로그 운영"]
---





# HUGO 설치

## 다운로드
[HUGO 다운로드](https://github.com/gohugoio/hugo/releases)

위 사이트에서 환경에 맞는 Windows 모듈을 다운로드하여 압축을 풉니다.
제 경우에는 "hugo_0.102.3_Windows-64bit.zip"을 다운로드했습니다.

## 압축 풀기
다운로드한 zip 파일의 압축을 풀고 그 안의 hugo.exe를 예를 들어 C:\bin 등 폴더를 만들어 그곳에 복사합니다.

## 환경 변수 등록
아무 위치에서나 hugo.exe를 실행하기 위해 환경 변수에 등록합니다.
Windows 11에서의 조작이지만 다음과 같은 절차로 등록할 수 있을 것입니다.

1. Win+Pause 버튼을 눌러 버전 정보 열기
2. 시스템 고급 설정 클릭
3. 환경 변수 클릭
4. Path를 선택하고 편집 클릭
5. 새로 만들기를 클릭하고 새 줄에 "C:\bin"을 입력한 후 확인을 눌러 대화 상자 닫기
 
# 블로그 프리뷰하기
명령 프롬프트에서 HUGO 블로그 폴더로 이동하여 아래 명령을 실행합니다.

`hugo server -D`

실행 결과는 아래와 같습니다. (-D는 임시 글을 표시하는 옵션입니다.)

```
C:\Users\win11\IdeaProjects\kenji.blog>hugo server -D
Start building sites …
hugo v0.102.3-b76146b129d7caa52417f8e914fc5b9271bf56fc windows/amd64 BuildDate=2022-09-01T10:16:19Z VendorInfo=gohugoio

                   | JA
-------------------+-----
Pages            | 39
Paginator pages  |  0
Non-page files   |  7
Static files     |  0
Processed images |  0
Aliases          | 13
Sitemaps         |  1
Cleaned          |  0

Built in 161 ms
Watching for changes in C:\Users\win11\IdeaProjects\kenji.blog\{archetypes,content,themes}
Watching for config changes in C:\Users\win11\IdeaProjects\kenji.blog\config.toml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```

주소는 실행 시 출력되므로 (위 예에서는 `http://localhost:1313/`), 브라우저에 주소를 복사합니다.
프리뷰는 파일이 저장될 때마다 자동 업데이트됩니다.
프리뷰를 마치려면 명령 프롬프트에서 Ctrl+C를 입력합니다.
