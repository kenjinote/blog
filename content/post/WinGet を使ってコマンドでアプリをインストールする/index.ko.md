---

title: "WinGet을 사용하여 명령어로 앱 설치하기"
date: 2022-10-05T12:15:20+09:00
tags: ["WinGet"]
draft: false
image: "img.png"
categories: ["도구 및 개발 환경"]
---

## 전제 조건
Windows 11 일 것

## 순서
1. Microsoft Store에서 `앱 인스톨러`를 설치한다
   https://www.microsoft.com/store/productId/9NBLGGH4NNS1
2. 명령 프롬프트에서 앱을 설치한다
    ```powershell
    winget install Google.Chrome
    ```
## 설치할 수 있는 주요 앱
- Google Chrome (명령어 `winget install Google.Chrome`)
- Microsoft Edge (명령어 `winget install Microsoft.Edge`)
- Microsoft Teams (명령어 `winget install Microsoft.Teams`)
- Microsoft Office (명령어 `winget install Microsoft.Office`)
- Visual Studio Code (명령어 `winget install vscode`)
- Slack (명령어 `winget install SlackTechnologies.Slack`)
- Discord (명령어 `winget install Discord.Discord`)
- Docker Desktop (명령어 `winget install Docker.DockerDesktop`)
- Git (명령어 `winget install Git`)
- 7zip (명령어 `winget install 7zip`)
- VLC (명령어 `winget install VideoLAN.VLC`)

## 참고
[winget 도구를 사용한 애플리케이션 설치 및 관리](https://learn.microsoft.com/ja-jp/windows/package-manager/winget/)

### 여담
Paint.Net도 설치할 수 있을까 생각했는데, 설치할 수 없었다.

https://forums.getpaint.net/topic/118574-please-add-paintnet-to-the-available-packages-for-windows-package-manager-winget/
