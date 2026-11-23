---
title: 'Hugo CLI 설치 및 자주 사용하는 기본 명령어 목록'
slug: "Hugo명령어一覧"
date: 2024-05-31T01:36:00+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["hugo", "명령어"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: '고속 정적 사이트 생성기 Hugo의 CLI 설치 방법과 블로그 운영에서 자주 사용하는 기본 명령어 목록을 소개합니다. 신규 사이트 구축, 기사 작성, 로컬 서버 기동, 빌드 등 Hugo 초보자가 기억해야 할 조작을 해설합니다.'
---

# Hugo란

Hugo는 정적 사이트 생성기 중 하나입니다. Markdown 파일을 HTML로 변환하여 웹사이트를 만들 수 있습니다. Hugo는 [Go](https://kenji.blog/ko/p/programming-languages-history-paradigm-evolution/) 언어로 작성되어 빠르게 동작합니다.

이 블로그도 Hugo로 제작되었습니다.

# Hugo CLI 설치

Hugo CLI를 설치하려면 다음 명령어를 실행합니다.

※ macOS의 경우의 예시입니다. 다른 OS의 경우, 공식 문서를 참조하세요.

```bash
brew install hugo
```

Homebrew를 사용하여 설치할 수 있습니다.

# Hugo 명령어 목록

Hugo에는 다양한 명령어가 준비되어 있습니다. 아래에 자주 사용하는 명령어를 정리했습니다.

## 새로운 사이트 만들기

```bash
hugo new project <site-name>
```

지정한 이름으로 새 사이트를 만듭니다.

## 새로운 글 작성하기

```bash
hugo new content posts/<post-name>.md
```

지정한 경로에 새 콘텐츠 파일을 만듭니다.

## 서버 실행하기

```bash
hugo server
```

로컬 서버를 기동하는 명령어입니다. `http://localhost:1313`으로 접속할 수 있습니다.

## 빌드하기

```bash
hugo
```

사이트를 빌드하는 명령어입니다. `public` 디렉토리에 HTML 파일이 생성됩니다.

## 배포하기

```bash
hugo deploy
```

이 명령은 지원되는 클라우드 스토리지 제공업체에 사이트를 배포합니다. 사이트 설정의 `deployment` 섹션에서 대상을 지정하고 제공업체 CLI로 인증해야 합니다. GitHub Pages 같은 모든 웹 호스팅에 사용하는 범용 배포 명령은 아닙니다. Hugo v0.159.2 이상에서는 Deploy 에디션이 필요합니다.

## 글 목록 표시하기

```bash
hugo list all
```

초안, 미래 날짜로 예약된 콘텐츠, 만료된 콘텐츠를 포함한 모든 콘텐츠를 표시합니다.

## 설정 확인하기

```bash
hugo config
```

기본값과 사이트에 설정된 구성 값을 모두 표시합니다.

## 도움말 표시하기

```bash
hugo help
```

도움말을 표시하는 명령어입니다.

## 버전 표시하기

```bash
hugo version
```

Hugo 버전과 실행 환경 정보를 표시합니다.


이상이 Hugo 명령어 목록입니다. 이 외에도 다양한 명령어가 준비되어 있으므로 공식 문서를 참고해 주세요.

# 참고
- [프로젝트 만들기](https://gohugo.io/commands/hugo_new_project/)
- [콘텐츠 만들기](https://gohugo.io/commands/hugo_new_content/)
- [배포](https://gohugo.io/commands/hugo_deploy/)
- [모든 콘텐츠 목록](https://gohugo.io/commands/hugo_list_all/)
- [macOS 설치](https://gohugo.io/installation/macos/)
