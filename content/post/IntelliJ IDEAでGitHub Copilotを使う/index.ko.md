---
title: 'IntelliJ IDEA에 GitHub Copilot을 도입 및 활성화하는 방법'
slug: "IntelliJ IDEAでGitHub Copilotを使う"
date: 2022-09-10T09:44:55+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA","GitHub Copilot"]
draft: false
image: "images/img.webp"
categories: ["tools-development-environment"]
description: 'IntelliJ IDEA에 GitHub Copilot 플러그인을 설치하고 GitHub에 로그인해 인라인 코드 제안을 사용하는 방법을 안내합니다. 필요한 이용 권한과 현재 인증 절차를 설명하고 공식 안내 링크를 제공합니다.'
---
# 소개

GitHub Copilot 플러그인을 설치하면 JetBrains IDE에서 인라인 코드 제안과 Copilot Chat을 사용할 수 있습니다. 이 문서에서는 IntelliJ IDEA의 기본 설치와 로그인 방법을 설명합니다. 메뉴 이름과 화면은 IDE 및 플러그인 버전에 따라 다를 수 있습니다.

## 시작하기 전에

Copilot을 사용할 수 있는 GitHub 계정과 호환되는 IntelliJ IDEA 버전이 필요합니다. Copilot Free에는 사용량 제한이 있으며 유료 요금제는 더 많은 기능을 제공합니다. 요금제와 IDE 호환성은 바뀔 수 있으므로 최신 공식 문서를 확인하세요.

## 플러그인 설치

1. Plugins 설정을 엽니다. Windows/Linux에서는 **File > Settings > Plugins**, macOS에서는 **IntelliJ IDEA > Settings > Plugins**를 선택합니다.
2. Marketplace에서 **GitHub Copilot**을 검색하고 GitHub에서 제공하는 플러그인의 **Install**을 클릭합니다.
3. 설치가 끝나면 IDE를 다시 시작합니다.

## GitHub 로그인

1. **Tools > GitHub Copilot > Login to GitHub**를 엽니다.
2. 로그인 대화상자에서 **Copy and Open**을 클릭합니다. 브라우저가 열립니다.
3. 브라우저에서 GitHub에 로그인하고 IDE에 표시된 장치 코드를 붙여 넣은 다음 **Continue**를 클릭합니다.
4. 요청된 권한을 확인하고 **Authorize GitHub Copilot Plugin**을 선택합니다. IDE로 돌아와 확인 화면에서 **OK**를 클릭합니다.

## 코드 제안 사용

편집기에서 입력을 시작하면 Copilot이 회색 글자로 제안을 표시합니다. 제안을 적용하려면 **Tab**을 누릅니다. 제안은 문맥을 바탕으로 생성되므로 사용 전에 내용을 확인하고 필요한 부분을 수정하세요. IDE 오른쪽의 GitHub Copilot Chat 아이콘을 열면 대화를 시작할 수 있습니다.

메뉴와 기능은 변경될 수 있습니다. 최신 절차와 호환성은 공식 문서를 참고하세요.

## 참고 자료

- [GitHub Copilot 플러그인 설치 및 로그인](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [JetBrains IDE에서 코드 제안 받기](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [JetBrains Marketplace의 GitHub Copilot 플러그인](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
