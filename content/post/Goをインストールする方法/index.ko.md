---



title: "Go 설치와 첫 프로그램 실행하기"
slug: "Goを설치する方法"
date: 2022-09-10T00:48:17+09:00
lastmod: 2026-11-23
lastmod: 2026-11-23
lastmod: 2026-11-23
tags: ["Go","설치"]
draft: false
image: "images/cover.webp"
categories: ["programming"]
description: "Windows, macOS 또는 Linux에 Go를 설치하고 go version으로 확인한 뒤 모듈을 만들고 Hello World를 실행하는 방법입니다."
---

# Go 소개

Go는 Google에서 개발을 시작했으며 현재 오픈 소스 프로젝트로 개발되고 있습니다. 정적 타입 컴파일 언어입니다. Go는 포인터를 지원하지만 포인터 연산은 지원하지 않으며, 런타임에 가비지 컬렉터가 포함됩니다.

# Go 설치

[공식 다운로드 및 설치 안내](https://go.dev/doc/install)를 열고 운영체제(Windows, macOS, Linux)와 CPU 아키텍처에 맞는 절차를 선택하세요. 공식 안내에 따라 설치한 다음 새 터미널을 열고 다음 명령을 실행합니다.

```sh
go version
```

버전이 표시되면 `go` 명령을 사용할 수 있습니다. Go를 업데이트할 때는 공식 교체 절차를 따르고, 기존 설치 폴더 위에 새 버전을 덮어 풀지 마세요. 여러 버전 관리는 [Go 설치 관리](https://go.dev/doc/manage-install)를 참고하세요.

# Hello, World 실행

작업 폴더를 만들고 그 안에서 모듈을 초기화합니다.

```sh
mkdir hello
cd hello
go mod init example/hello
```

같은 폴더에 `hello.go` 파일을 만들고 다음 코드를 저장합니다.

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

다음 명령으로 실행합니다.

```sh
go run .
```

`Hello, World!`가 출력됩니다. 실행 파일을 빌드하려면 `go build`를 실행하세요. 파일 이름과 확장자는 운영체제에 따라 다르며 Windows에서는 일반적으로 `.exe`를 사용합니다.

# 다음 학습 자료

- [Go 공식 튜토리얼: 시작하기](https://go.dev/doc/tutorial/getting-started)
- [Go FAQ](https://go.dev/doc/faq)
- [Go Playground](https://go.dev/play/) (브라우저에서 코드 실행)

공식 입문 자료는 주로 영어로 제공됩니다.
