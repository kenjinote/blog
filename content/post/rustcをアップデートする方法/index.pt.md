---
title: 'Como atualizar o compilador Rust (rustc) para a versão mais recente'
slug: "rustcをアップデートする方法"
date: "2023-03-18T10:27:02+09:00"
lastmod: "2026-11-25"
tags: ["RUST", "RUSTC", "UPDATE"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Explicamos uma maneira simples de atualizar o rustc, o compilador do Rust, para a versão mais recente. Apenas executando uma linha com o comando `rustup update` no terminal ou prompt de comando, você pode atualizar em lote incluindo todos os componentes relacionados.'
---
# Como atualizar o rustc

Basta executar a seguinte linha de comando.

```
rustup update
```


Esta saída foi registrada em março de 2023; as versões, os componentes instalados e as mensagens podem ser diferentes hoje. A documentação oficial do rustup informa que os downloads usam HTTPS, mas as assinaturas dos arquivos baixados não são validadas. Não interprete o aviso de verificação de assinatura deste exemplo como prova de que o download foi validado; se encontrar um aviso semelhante, verifique o ambiente e a configuração da origem de distribuição. Consulte o [guia oficial do rustup](https://rust-lang.github.io/rustup/basics.html) para as instruções atuais. Para obter detalhes de segurança, consulte a [documentação de segurança do rustup](https://rust-lang.github.io/rustup/security.html).

# Referência de saída

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
