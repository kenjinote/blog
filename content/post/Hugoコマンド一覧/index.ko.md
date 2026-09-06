---








title: "'Hugo 명령어 목록'"
date: 2024-05-31T01:36:00+09:00
tags: ["hugo", "명령어"]
draft: false
image: "img.png"
categories: ["블로그 운영"]
---









# Hugo란

Hugo는 정적 사이트 생성기 중 하나입니다. Markdown 파일을 HTML로 변환하여 웹사이트를 만들 수 있습니다. Hugo는 Go 언어로 작성되어 빠르게 동작합니다.

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
hugo new site <사이트명>
```

새로운 사이트를 생성하는 명령어입니다. `<사이트명>`에는 사이트의 이름을 지정합니다.

## 새로운 글 작성하기

```bash
hugo new <기사명>.md
```

새로운 글을 작성하는 명령어입니다. `<기사명>`에는 글의 이름을 지정합니다.

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

사이트를 배포하는 명령어입니다. 배포처 설정은 `config.toml` 파일에서 합니다.

## 글 목록 표시하기

```bash
hugo list all
```

작성된 글 목록을 표시하는 명령어입니다.

## 설정 확인하기

```bash
hugo config
```

설정을 확인하는 명령어입니다.

## 도움말 표시하기

```bash
hugo help
```

도움말을 표시하는 명령어입니다.

## 버전 표시하기

```bash
hugo version
```

버전을 표시하는 명령어입니다.

이상이 Hugo 명령어 목록입니다. 이 외에도 다양한 명령어가 준비되어 있으므로 공식 문서를 참고해 주세요.

# 참고
- [Hugo 공식 문서](https://gohugo.io/documentation/)
