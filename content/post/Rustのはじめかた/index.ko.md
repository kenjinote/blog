---




title: "'Rust 시작하기'"
slug: "Rustのはじめかた"
date: 2022-09-06T00:12:36+09:00
tags: ["Rust"]
draft: false
image: "images/rust_logo.png"
categories: ["프로그래밍"]
---




# 시작하며
Rust는 빠르고 메모리 효율이 높은 모듈을 모던한 표기법으로 작성할 수 있는 비교적 새로운 프로그래밍 언어입니다.
멀티 플랫폼을 지원하며, WebAssembly나 임베디드 환경에서도 사용되고 있습니다.
유명한 곳으로는 Firefox나 DropBox, Cloudflare에서도 채택하고 있습니다.

C++의 대체 언어로도 주목받고 있습니다.

# 설치 방법

[Rust 설치](https://www.rust-lang.org/ja/tools/install)

위 사이트에서 각 플랫폼을 위한 설치 방법을 제공하고 있습니다.

# 첫 프로그램

다음 프로그램을 `main.rs`로 저장합니다.

```
fn main() {
    println!("Hello, world!");
}
```

명령 프롬프트 또는 터미널에서 `rustc main.rs`를 실행하면,
컴파일이 진행되며, `./main`(Windows의 경우 `main.exe`)을 실행하면 `Hello, world!`가 출력됩니다.

# 일본어 문서

[The Rust Programming Language 일본어판](https://doc.rust-jp.rs/book-ja/)

Rust를 배우는 데 필요한 설명은 위 링크(일본어 번역판)에 모여 있습니다.
Rust 교재를 구입할 필요가 없을 정도로 충실하게 구성되어 있습니다.

# Web에서 실행해 보고 싶은 경우

컴파일러를 설치하지 않고 Web에서 실행해 보고 싶은 경우에는 [The Rust Playground](https://play.rust-lang.org/)를 사용할 수 있습니다.
코드를 입력하고 「실행 버튼」을 누르면, Web 상에서 컴파일되어 실행됩니다.
