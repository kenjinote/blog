---
title: 'Hugo CLIのインストールとよく使う基本コマンド一覧'
slug: "Hugoコマンド一覧"
date: 2024-05-31T01:36:00+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["hugo", "コマンド"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: '高速な静的サイトジェネレーターHugoのCLIインストール方法と、ブログ運営で頻繁に使用する基本コマンド一覧を紹介します。新規サイト立ち上げ、記事の作成、ローカルサーバー起動、ビルドなど、Hugo初心者が覚えておくべき操作を解説します。'
---

# Hugo とは

Hugo は、静的サイトジェネレーターの一つです。MarkdownファイルをHTMLに変換して、Webサイトを作成することができます。Hugo は、[Go](https://kenji.blog/p/programming-languages-history-paradigm-evolution/)言語で書かれており、高速で動作します。

このブログもHugo で作成されています。

# Hugo のCLIのインストール

Hugo のCLIをインストールするには、以下のコマンドを実行します。

※ macOSの場合の例です。他のOSの場合は、公式ドキュメントを参照してください。

```bash
brew install hugo
```

Homebrew を使ってインストールすることができます。

# Hugo のコマンド一覧

Hugo には、様々なコマンドが用意されています。以下に、よく使うコマンドをまとめました。

## 新しいサイトを作成する

```bash
hugo new project <site-name>
```

指定した名前の新しいサイトを作成します。

## 新しい記事を作成する

```bash
hugo new content posts/<post-name>.md
```

指定したパスに新しいコンテンツファイルを作成します。

## サーバーを起動する

```bash
hugo server
```

ローカルサーバーを起動するコマンドです。`http://localhost:1313`でアクセスできます。

## ビルドする

```bash
hugo
```

サイトをビルドするコマンドです。`public`ディレクトリにHTMLファイルが生成されます。

## デプロイする

```bash
hugo deploy
```

クラウドストレージへのデプロイ機能です。デプロイ先は設定ファイルの `deployment` セクションで指定し、クラウド事業者のCLIで認証します。一般的なWebホスティングやGitHub Pages向けの汎用コマンドではありません。Hugo 0.159.2以降ではDeployエディションが必要です。

## 記事一覧を表示する

```bash
hugo list all
```

下書き、公開予定日が未来の記事、期限切れの記事も含めて、すべてのコンテンツを表示します。

## 設定の確認

```bash
hugo config
```

既定値とサイトで指定した設定を表示します。

## ヘルプを表示する

```bash
hugo help
```

ヘルプを表示するコマンドです。

## バージョンを表示する

```bash
hugo version
```

Hugoのバージョンと実行環境の情報を表示します。


以上が、Hugo のコマンド一覧です。他にも、様々なコマンドが用意されていますので、公式ドキュメントを参照してください。

# 参考
- [新しいプロジェクト](https://gohugo.io/commands/hugo_new_project/)
- [新しいコンテンツ](https://gohugo.io/commands/hugo_new_content/)
- [デプロイ](https://gohugo.io/commands/hugo_deploy/)
- [すべてのコンテンツ](https://gohugo.io/commands/hugo_list_all/)
- [macOSへのインストール](https://gohugo.io/installation/macos/)