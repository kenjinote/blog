---
title: "Visual Studio Code 추천 확장: 작업별 가이드"
date: "2024-05-29T17:20:19+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Visual Studio Codeおすすめ拡張機能"
tags: ["Visual Studio Code", "VSCode", "拡張機能", "エクステンション"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "원격 개발, GitHub, 웹·클라우드, 데이터, 임베디드, 언어 도구용 VS Code 확장을 소개합니다."
---

# 작업별로 VS Code 확장 선택하기

필요한 확장만 설치하세요. 이 글은 대표적인 확장을 용도별로 정리합니다. Marketplace의 이름과 기능은 변경될 수 있으므로 2024년판의 오래된 이름, 중복 기능, 오해를 부를 수 있는 설명을 정리하고 각 항목을 Marketplace 페이지에 연결했습니다.

VS Code에는 기본 Git 통합과 JavaScript/TypeScript 디버깅 같은 기능이 이미 포함되어 있습니다. 먼저 내장 기능을 사용하고, 필요한 기능만 확장으로 추가하세요.

## 원격 개발과 컨테이너

- [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
- [Container Tools](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-containers)

## GitHub와 Git

- [GitHub Pull Requests](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)
- [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
- [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)

## 웹 개발

- [Microsoft Edge Tools for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-edgedevtools.vscode-edge-devtools)
- [Vue (Official)](https://marketplace.visualstudio.com/items?itemName=Vue.volar)
- [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss)

## 클라우드

- [AWS Toolkit](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.aws-toolkit-vscode)
- [Google Cloud Code](https://marketplace.visualstudio.com/items?itemName=GoogleCloudTools.cloudcode)
- [GitHub Copilot for Azure](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azure-github-copilot)

## 데이터베이스와 임베디드 개발

- [SQLTools](https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools)
- [PlatformIO IDE](https://marketplace.visualstudio.com/items?itemName=platformio.platformio-ide)
- [Arduino Community Edition](https://marketplace.visualstudio.com/items?itemName=vscode-arduino.vscode-arduino-community)
- [Cortex-Debug](https://marketplace.visualstudio.com/items?itemName=marus25.cortex-debug)

## 언어와 빌드 도구

- [C/C++](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
- [CMake Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

## 편집과 협업

- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
- [Hex Editor](https://marketplace.visualstudio.com/items?itemName=ms-vscode.hexeditor)
- [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv)
- [Draw.io Integration](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio)
- [Japanese Language Pack](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-ja)
- [Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare)

Arduino Community Edition은 커뮤니티가 유지 관리하는 이전 Arduino 확장의 포크이며 Microsoft 공식 제품이 아닙니다.

SQLTools는 여러 데이터베이스에 연결하는 커뮤니티 확장입니다. 데이터베이스에 맞는 드라이버를 선택하고 게시자와 접근 권한을 확인하세요.

GitHub Copilot for Azure는 Copilot에 Azure 기술을 추가합니다. 일반적인 Azure 관리 확장은 아닙니다.

## 설치 전에 확인할 사항

VS Code 확장은 VS Code와 동일한 권한으로 실행됩니다. 파일을 읽고 쓸 수 있고, 네트워크 요청을 보내며 외부 프로세스를 실행할 수도 있습니다. 설치 전에 게시자, 확장 팩이 추가하는 종속 확장, 업데이트 기록, 지원 정보와 개인정보 처리 조건을 확인하세요. AI 기능이 있는 확장은 코드나 프롬프트를 외부 서비스로 보낼 수 있습니다. 민감한 작업에서는 서비스의 데이터 이용 조건과 조직 정책을 확인하세요.

## 요약

확장을 많이 설치한다고 생산성이 자동으로 향상되지는 않습니다. 용도, 게시자, 권한 및 유지 관리 상태를 확인하고 사용하는 것만 설치하세요.

- [VS Code extension runtime security](https://code.visualstudio.com/docs/configure/extensions/extension-runtime-security)
- [VS Code extension Marketplace](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace)
