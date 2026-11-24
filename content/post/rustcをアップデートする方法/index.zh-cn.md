---
title: '将Rust编译器(rustc)更新到最新版本的方法'
slug: "rustcをアップデートする方法"
date: "2023-03-18T10:27:02+09:00"
lastmod: "2026-11-25"
tags: ["RUST", "RUSTC", "UPDATE"]
draft: false
image: "img.webp"
categories: ["programming"]
description: '讲解将Rust编译器rustc更新到最新版本的简单方法。只需在终端或命令提示符中执行一行`rustup update`命令，即可包括相关组件在内进行一键更新。'
---
# 如何更新rustc

只需在命令行中执行以下一行命令。

```
rustup update
```


以下是2023年3月记录的输出示例；当前的版本、安装组件和提示信息可能不同。Rustup官方文档说明，下载通过HTTPS进行，但不会验证下载内容的签名。不要把示例中的签名验证警告当作下载已通过验证的证明；如果遇到类似警告，请检查环境和发行源配置。当前更新方法请参阅[Rustup官方指南](https://rust-lang.github.io/rustup/basics.html)。 有关安全性的详情，请参阅 [rustup 安全文档](https://rust-lang.github.io/rustup/security.html)。

# 输出参考

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
