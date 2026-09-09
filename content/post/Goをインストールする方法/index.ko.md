---



title: 'Go 언어(Golang) 설치 절차 및 첫 프로그램 실행 방법'
slug: "Goをインストールする方法"
date: 2022-09-10T00:48:17+09:00
tags: ["Go","설치"]
draft: false
image: "images/cover.webp"
categories: ["프로그래밍"]
description: 'Google이 개발한 프로그래밍 언어 ''Go(Golang)''의 설치 방법을 초보자를 위해 해설합니다. 설치 프로그램 가져오기부터 Hello World 프로그램 작성, 컴파일, 실행 절차까지 첫 Go 언어 입문에 최적입니다.'
---



# 시작하며
Go는 Google이 2009년에 공개한 비교적 새로운 프로그래밍 언어입니다.
Go의 컴파일러, 도구, 라이브러리는 오픈 소스로 공개되어 있습니다.
또한, Go는 C 언어나 Java와 같은 정적 타입 언어이지만, C 언어와 같은 포인터를 사용하지 않는 언어입니다.

# 설치 방법

[Go 설치](https://go.dev/dl/)

위 사이트에서 각 플랫폼용 설치 프로그램이 공개되어 있습니다.

화면에 따라 설치를 진행합니다.
![img.png](images/img.webp)

![img_1.png](images/img_1.webp)

![img_2.png](images/img_2.webp)

![img_3.png](images/img_3.webp)

![img_5.png](images/img_5.webp)

![img_6.png](images/img_6.webp)

설치가 완료되었습니다. 간단하죠.

# 첫 번째 프로그램

다음 프로그램을 `hello.go`로 저장합니다.

```go
package main

import "fmt"

func main() {
  fmt.Printf("Hello World\n")
}
```

명령 프롬프트나 터미널에서 `go run hello.go`를 실행하면 `Hello, world!`가 출력됩니다.

컴파일할 경우에는 `go build hello.go`를 실행하면 `hello.exe`가 생성됩니다.
`hello.exe`를 실행하면 `Hello, world!`가 출력됩니다.

# 웹 페이지에서 코드를 실행할 수도 있습니다

[https://go.dev/play/](https://go.dev/play/)

![img_7.png](images/img_7.webp)

# 일본어 문서

[http://go.shibu.jp/](http://go.shibu.jp/)

Go를 배우는 데 필요한 설명은 위 링크(일본어 번역판)에 모여 있습니다.
Go와 관련된 기술은 오픈되어 있어서 종이 교재를 구입할 필요가 없을 정도로 충실합니다.

그럼 즐거운 Go 라이프를!
