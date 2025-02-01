---
title: 'PaperModでTwitter Cardを設定する方法'
date: 2022-09-10T18:41:22+09:00
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.png"
---
# はじめに
PaperModテーマはTwitter Cardに対応しています。
ただし、Twitter Cardの設定は、`config.toml`まはた各記事の`*.md`のヘッダ情報に記述する必要があります。
各記事と`config.toml`の両方に設定した場合は、各記事のヘッダ情報が優先されます。

# 設定方法
## config.toml
`config.toml`には、`[params]`の下に、`images`という項目を追加します。
`images`には、Twitter Cardに表示する画像のパスを記述します。
画像を`static`フォルダに配置する場合は、ファイル名だけの指定でOKです。

```
[params]
  images = ["twitter_card.jpg"]
```

フォルダ構成
```
root
│  config.toml (ココに記述)
├─content
│  └─posts
│      └─記事フォルダ
│         │  index.md (ココに記述)
│         └─images
│             cover.png (ココに配置)
└─static
    twitter_card.jpg (ココに配置)
```

## 各記事のヘッダ情報
各記事のヘッダ情報には、`cover`の配下に`image`という項目を追加します。
`relative`を`true`にすると、記事の`*.md`からの相対パスで指定できます。

```
cover:
  image: "images/cover.jpg"
  relative: true
```

### 記事の上部には表示させたくない場合
記事の上部にカバー画像を表示させたくない場合は、`cover`の配下に`hidden`という項目を追加て`true`に設定します。
```
cover:
  image: "images/cover.jpg"
  relative: true
  hidden: true
```

# 画像のサイズについて

現状のPaperModの仕様でTwitter Cardのサイズは、`summary_large_image`のみ対応しているようです。
`summary_large_image`の適切なサイズ（解像度）は、諸説ありますが`800 x 418`（画像比1.91:1）あたりがよさそうです。

[参考サイト1](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/summary-card-with-large-image)
[参考サイト2](https://developers.facebook.com/docs/sharing/best-practices)


できれば、画像サイズをリサイズして投稿することをおすすめします。

# 設定の確認方法
Twitter Cardの設定を確認するには、[Twitter Card Validator](https://cards-dev.twitter.com/validator)を利用します。
ただし、私の環境ではうまくプレビューが表示されなかったため、もしプレビューが表示が表示されない場合は非公開のアカウント等を使って投稿前に一度確認しておくことをおすすめします。

