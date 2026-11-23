---
date: 2022-09-11T22:59:52+09:00
lastmod: 2026-11-23
title: 'Hugoの組み込みショートコード：埋め込みとプライバシー設定'
slug: "HUGOで使えるショートコード"
tags: ["HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'Hugoの組み込みショートコードの種類、バージョンによる違い、動画・SNS埋め込みの設定とプライバシー上の注意を紹介します。'
---

# Hugoの組み込みショートコード：埋め込みとプライバシー設定

ショートコードはMarkdown本文にテンプレート機能を呼び出す記法です。Hugo本体に組み込まれたもの、テーマやモジュールが提供するもの、自作したものがあります。名前と引数はHugoのバージョンによって異なるため、実際に使うバージョンの公式ドキュメントを確認してください。

## Hugoの組み込みショートコード

FlickrはHugo本体の組み込みショートコードではありません。利用できる場合は、テーマ・モジュール・プロジェクト独自の`layouts/_shortcodes/flickr.html`などが提供元です。組み込みかどうかを確認せず、同名の記法をコピーしないでください。

現在の公式一覧には`details`、`figure`、`highlight`、`instagram`、`param`、`qr`、`ref`、`relref`、`vimeo`、`x`、`youtube`などがあります。完全な一覧と引数は公式ページを参照してください。

## メディアの例

### YouTube

動画URLの`v`パラメーターにあるIDを指定します。

`{{</* youtube 0RKpf3rK57I */>}}`

### X（Hugo 0.141.0以降）

投稿URLのユーザー名と投稿IDを指定します。

`{{</* x user="SanDiegoZoo" id="1453110110599868418" */>}}`

### 旧Twitter（Hugo 0.139.0）

Hugo 0.139.0では次の名前付き引数を使います。

`{{</* twitter user="SanDiegoZoo" id="1453110110599868418" */>}}`

### Instagram

Instagram投稿URLの最後の部分が投稿IDです。

`{{</* instagram CxOWiQNP2MO */>}}`

### Vimeo

Vimeo動画のURL末尾にある数値IDを使います。

`{{</* vimeo 19899678 */>}}`

## バージョン差に注意

このブログのビルドはHugo 0.139.0に固定されています。この版ではX（旧Twitter）の組み込み名は`twitter`で、ユーザー名と投稿IDを名前付き引数で渡します。`x`ショートコードはHugo 0.141.0で追加され、後の版では`twitter`が非推奨になりました。新しい版の例を使う前に、プロジェクトのHugoバージョンを確認してください。

## プライバシー設定

YouTube、X、Instagram、Vimeoの埋め込みは外部サービスへ接続する要素を生成します。Hugoの`privacy`設定では、埋め込みを無効にしたり、利用できるサービスでは簡易表示を選んだりできます。YouTubeの`privacyEnhanced`は、訪問者が動画を再生するまで情報保存を抑えます。

YouTubeのプライバシー強化:

```yaml
privacy:
  youTube:
    privacyEnhanced: true
```

Xの簡易表示:

```yaml
privacy:
  x:
    simple: true
    enableDNT: true
```

旧Twitter（Hugo 0.139.0）:

```yaml
privacy:
  twitter:
    simple: true
    enableDNT: true
```

設定名は使用するHugoのバージョンに対応した公式ドキュメントで確認してください。

Instagramの簡易表示でも画像はInstagramのサーバーから読み込まれます。Vimeoの簡易表示ではサムネイルを取得し、クリック後はVimeoを新しいタブで開きます。外部通信を完全になくす設定ではありません。

埋め込みを公開する前に、プロバイダーへの通信、Cookie等の動作、利用地域のプライバシー要件を確認してください。

## 記法を文字として表示する

ショートコードの記法を記事内にそのまま見せる場合は、例のように区切りへ`/*`と`*/`を加えてエスケープします。

`{{</*/* youtube 0RKpf3rK57I */*/>}}`

## 公式ドキュメント

- [ショートコードの概要](https://gohugo.io/content-management/shortcodes/)
- [組み込みショートコード一覧](https://gohugo.io/shortcodes/)
- [YouTube](https://gohugo.io/shortcodes/youtube/)
- [X](https://gohugo.io/shortcodes/x/)
- [Instagram](https://gohugo.io/shortcodes/instagram/)
- [Vimeo](https://gohugo.io/shortcodes/vimeo/)
- [プライバシー設定](https://gohugo.io/configuration/privacy/)
