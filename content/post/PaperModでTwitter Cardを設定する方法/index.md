---
title: "Hugo PaperModでTwitter Card（Xカード）を設定する方法"
slug: "PaperModでTwitter Cardを設定する方法"
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "PaperModの公式仕様に沿ってXカード画像を設定し、生成HTMLとXの投稿作成画面で確認する方法を説明します。"
date: "2022-09-10T18:41:22+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PaperModはOpen GraphとTwitter Card用のメタデータを生成できます。テーマの版や独自レイアウトによって出力は異なるため、設定例だけで判断せず、公開HTMLに出た値を確認してください。

## サイト全体の設定

PaperModのSEOメタデータは、本番環境としてビルドした場合に有効になります。サイト設定で環境をproductionにします。

```toml
[params]
  env = "production"
```

サイト全体の既定画像には、`static`以下に置いた画像を指定します。これは記事固有の画像を用意していない場合の候補です。画像URLが実際に公開サイト上でどう出力されるかも確認します。

```toml
[params]
  images = ["/twitter-card-1200x630.webp"]
```

## 記事ごとの画像

記事ごとに画像を指定するには、記事のPage Bundle内の画像を`cover.image`に設定します。`relative: true`はPage Bundle内の相対パスを使う設定です。PaperModの説明では、カバー画像があればカード画像に使われ、なければ記事の`images`、さらに条件に合うBundle画像が候補になります。

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
```

## 本文にカバーを表示しない

`cover.hidden: true`は記事本文上のカバー表示を隠しつつ、構造化データ用には画像を残す設定です。SNSカード用だけに画像を設定したいときに利用できます。テーマのバージョンや上書きテンプレートがある場合は、生成HTMLで必ず確認してください。

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
  hidden: true
```

## カード種別と画像サイズ

古い記事にあった「summary_large_imageのみ」「800×418固定」という説明は一般化できません。カード種別はテーマ版やサイト側テンプレートで異なります。幅広の画像を作る場合、1200×630（約1.90:1）は共有用の実用的な目安ですが、Xでの表示を保証する仕様値ではありません。

## 出力とプレビューを確認する

Hugoを本番設定でビルドし、記事のHTMLソースで`twitter:card`、`twitter:image`、`og:image`、タイトル、説明を確認します。画像URLがHTTPSで直接取得でき、ログイン不要で公開されていることも確かめます。Xは2022年にCard Validatorのプレビュー機能を終了し、投稿作成画面での確認を案内しました。リンクをXの投稿作成画面に貼り、投稿せずにプレビューを確認します。キャッシュ反映には時間がかかることがあります。

この説明はリンクしたPaperMod資料とX開発者フォーラムを2026年11月24日に確認したものです。テーマのfork、独自テンプレート、X側の仕様変更により実際のカード表示は変わることがあります。

## 参考資料

- [PaperMod: Features and Twitter Cards](https://github.com/adityatelange/hugo-PaperMod/wiki/Features)
- [PaperMod: Variables](https://github.com/adityatelange/hugo-PaperMod/wiki/Variables)
- [Hugo: Page bundles](https://gohugo.io/content-management/page-bundles/)
- [X Developer Community: Card Validator preview removal](https://devcommunity.x.com/t/card-validator-preview-removal/175006)
