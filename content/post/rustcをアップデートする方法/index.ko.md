---




title: 'Rust 컴파일러(rustc)를 최신 버전으로 업데이트하는 방법'
slug: "rustcをアップデートする方法"
date: "2023-03-18T10:27:02+09:00"
lastmod: "2026-11-25"
tags: ["RUST", "RUSTC", "UPDATE"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Rust의 컴파일러인 rustc를 최신 버전으로 업데이트하는 간단한 방법을 설명합니다. 터미널이나 명령 프롬프트에서 `rustup update` 명령어를 한 줄 실행하는 것만으로 관련 구성 요소를 포함하여 일괄 업데이트할 수 있습니다.'
---




# rustc를 업데이트하는 방법

아래의 한 줄을 명령어로 실행하기만 하면 됩니다.

```
rustup update
```


다음은 2023년 3월에 기록된 출력 예입니다. 현재 버전, 설치되는 구성 요소 및 메시지는 다를 수 있습니다. rustup 공식 문서에 따르면 다운로드는 HTTPS로 이루어지지만 다운로드 서명은 검증되지 않습니다. 이 예의 서명 검증 경고를 다운로드가 검증되었다는 뜻으로 받아들이지 마세요. 비슷한 경고가 나타나면 환경과 배포 서버 설정을 확인하세요. 최신 업데이트 방법은 [rustup 공식 가이드](https://rust-lang.github.io/rustup/basics.html)를 참조하세요. 보안에 관한 자세한 내용은 [rustup 보안 문서](https://rust-lang.github.io/rustup/security.html)를 참조하세요.

# 출력 참고

```
rustup update
info: syncing channel updates for 'stable-x86_64-pc-windows-msvc'
warning: Signature verification failed for 'https://static.rust-lang.org/dist/channel-rust-stable.toml'
info: latest update on 2023-03-09, rust version 1.68.0 (2c8cc3432 2023-03-06)
info: downloading component 'rust-src'
info: downloading component 'cargo'
info: downloading component 'clippy'
info: downloading component 'rust-docs'
info: downloading component 'rust-std'
info: downloading component 'rustc'
 63.9 MiB /  63.9 MiB (100 %)  37.5 MiB/s in  1s ETA:  0s
info: downloading component 'rustfmt'
info: removing previous version of component 'rust-src'
info: removing previous version of component 'cargo'
info: removing previous version of component 'clippy'
info: removing previous version of component 'rust-docs'
info: removing previous version of component 'rust-std'
info: removing previous version of component 'rustc'
info: removing previous version of component 'rustfmt'
info: installing component 'rust-src'
info: installing component 'cargo'
info: installing component 'clippy'
info: installing component 'rust-docs'
 19.4 MiB /  19.4 MiB (100 %)   2.4 MiB/s in  6s ETA:  0s
info: installing component 'rust-std'
 27.6 MiB /  27.6 MiB (100 %)  12.7 MiB/s in  2s ETA:  0s
info: installing component 'rustc'
 63.9 MiB /  63.9 MiB (100 %)  13.8 MiB/s in  4s ETA:  0s
info: installing component 'rustfmt'
info: checking for self-updates
info: downloading self-update

  stable-x86_64-pc-windows-msvc updated - rustc 1.68.0 (2c8cc3432 2023-03-06) (from rustc 1.64.0 (a55dd71d5 2022-09-19))

info: cleaning up downloads & tmp directories
```
