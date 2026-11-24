---
title: "macOSのSMB共有で.DS_Storeの読み取りを切り替える"
slug: "macOSで.DS_Storeを自動生成しないようにするコマンド"
date: 2022-09-12T16:03:42+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["macOS"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: "Apple公式の手順に基づき、macOSでSMB共有上の.DS_Store読み取りを無効化・再有効化する方法を説明します。ファイルの新規生成を止める設定ではなく、変更後はログアウトと再ログインが必要です。"
---
Appleが案内しているのは、**SMB共有上の`.DS_Store`をmacOSが読み取らないようにする設定**です。`.DS_Store`ファイルの新規生成を止めたり、既存ファイルを削除したりする設定ではありません。この変更後はFinderの並び順などの表示が変わることがあります。

### SMB共有上での読み取りを無効にする

ターミナルで次のコマンドを実行します。

```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE
```

変更を反映するには、macOSアカウントからログアウトし、再度ログインします。Finderは`.DS_Store`の情報を使わず、基本情報に基づいてフォルダ内容を表示します。

### 再び有効にする

設定を戻すには、値を`FALSE`にします。

```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool FALSE
```

その後、ログアウトして再度ログインします。Appleはこの設定をSMB共有の閲覧を調整する方法として案内しており、記事は主に企業・教育機関の管理者向けです。詳しくは[Appleの手順](https://support.apple.com/en-us/102064)を参照してください。
