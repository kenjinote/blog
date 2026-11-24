---
title: '將 Rust 編譯器 (rustc) 更新至最新版本的方法'
slug: "rustcをアップデートする方法"
date: "2023-03-18T10:27:02+09:00"
lastmod: "2026-11-25"
tags: ["RUST", "RUSTC", "UPDATE"]
draft: false
image: "img.webp"
categories: ["programming"]
description: '說明將 Rust 編譯器 rustc 更新至最新版本的簡單方法。只需在終端機或命令提示字元中執行一行 `rustup update` 指令，即可包含相關元件進行批次更新。'
---
# 如何更新 rustc

只需在命令列中執行以下一行。

```
rustup update
```


以下是 2023 年 3 月記錄的輸出範例；目前的版本、安裝元件及訊息可能不同。Rustup 官方文件指出，下載會透過 HTTPS 進行，但不會驗證下載檔案的簽章。請勿將範例中的簽章驗證警告視為下載已通過驗證；若出現類似警告，請檢查環境與發行來源設定。最新更新方式請參閱 [Rustup 官方指南](https://rust-lang.github.io/rustup/basics.html)。 安全性詳細資訊請參閱 [rustup 安全性文件](https://rust-lang.github.io/rustup/security.html)。

# 輸出參考

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
