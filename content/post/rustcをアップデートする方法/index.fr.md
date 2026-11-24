---
title: 'Comment mettre à jour le compilateur Rust (rustc) vers la dernière version'
slug: "rustcをアップデートする方法"
date: "2023-03-18T10:27:02+09:00"
lastmod: "2026-11-25"
tags: ["RUST", "RUSTC", "UPDATE"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Explique une méthode simple pour mettre à jour rustc, le compilateur pour Rust, à la dernière version. Vous pouvez mettre à jour en lot, y compris les composants associés, simplement en exécutant la commande `rustup update` sur une seule ligne dans le terminal ou l''invite de commande.'
---
# Comment mettre à jour rustc

Exécutez simplement la ligne suivante en ligne de commande.

```
rustup update
```


Cette sortie a été enregistrée en mars 2023 ; les versions, composants installés et messages peuvent être différents aujourd’hui. La documentation officielle de rustup précise que les téléchargements utilisent HTTPS, mais que leurs signatures ne sont pas validées. Ne considérez pas l’avertissement de vérification de signature de cet exemple comme la preuve qu’un téléchargement a été vérifié ; si un avertissement similaire apparaît, vérifiez votre environnement et la configuration de la source de distribution. Consultez le [guide officiel de rustup](https://rust-lang.github.io/rustup/basics.html) pour les instructions actuelles. Pour en savoir plus sur la sécurité, consultez la [documentation de sécurité de rustup](https://rust-lang.github.io/rustup/security.html).

# Référence de sortie

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
