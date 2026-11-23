---
title: 'Windows에 Gemini CLI를 설치하는 방법｜Node.js부터 철저 해설'
slug: "Gemini CLI を Windows 環境に설치する方法"
tags: ["Gemini", "CLI", "Windows", "설치", "개발"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
date: "2025-07-13T23:49:56+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Windows에서 Node.js와 npm으로 Gemini CLI를 설치하고 인증하는 방법, PATH 점검과 안전한 도구 승인을 설명합니다."
---

# Windows에서 Gemini CLI 설치하고 사용하기

Gemini CLI는 터미널에서 Gemini를 사용하는 오픈 소스 명령줄 도구입니다. 아래 절차는 현재 공식 안내에 따릅니다. 변경 사항은 [공식 설치 가이드](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/installation.mdx)에서 확인하세요.

## 1. Node.js와 npm 준비

Gemini CLI에는 Node.js 20.0.0 이상이 필요합니다. 공식 문서는 Windows 11 24H2 이상을 권장하고 PowerShell을 지원하며 인터넷 연결을 요구합니다. [Node.js 사이트](https://nodejs.org/en/download/)에서 Windows용 LTS 설치 파일을 받으세요.

```powershell
node --version
npm --version
```

## 2. npm으로 Gemini CLI 설치

계속 사용할 경우 패키지를 전역 설치합니다.

```powershell
npm install -g @google/gemini-cli
```

```powershell
gemini --version
gemini
```

`gemini`를 찾지 못하면 `npm config get prefix`로 폴더를 확인해 Windows `PATH`에 추가하고, 새 PowerShell 창을 연 뒤 `Get-Command gemini`로 확인하세요. [npm 문서](https://docs.npmjs.com/cli/v11/configuring-npm/folders/)를 참고하세요.

## 3. 첫 실행과 인증

PowerShell에서 `gemini`를 시작하고 첫 실행 인증 안내를 따릅니다. Google 계정, Gemini API 키, Vertex AI 등이 공식 문서에 안내된 방법입니다. 이용 가능 여부, 요금, 할당량, 약관은 계정과 서비스에 따라 다르므로 [인증 가이드](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/authentication.mdx)를 확인하세요. API 키를 프롬프트나 공개 저장소에 넣지 마세요.

```powershell
gemini
```

`gemini --help`로 명령을 확인하고 대화형 세션에서 `/quit`를 입력해 종료합니다.

## 4. 전역 설치 없이 한 번 실행

한 번만 실행하려면 `npx`를 사용합니다. 영구 설치가 아니므로 다음 세션에서 명령을 다시 실행해야 합니다. Gemini CLI는 파일을 읽고 수정하거나 셸 명령을 실행할 수 있습니다. 신뢰하는 프로젝트에서 사용하고, 실행 전 확인 요청을 검토하세요. [도구 및 보안 안내](https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/tools.md)

```powershell
npx @google/gemini-cli
```

## 5. 요약

1. Node.js 20 이상을 준비합니다.
2. 계속 사용하려면 npm으로 전역 설치합니다.
3. `gemini`를 시작하고 인증합니다.
4. 한 번만 실행하려면 `npx`를 사용합니다. 최신 요구 사항과 약관은 공식 안내를 확인하세요.
