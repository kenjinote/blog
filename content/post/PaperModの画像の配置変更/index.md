---
title: "Hugo PaperModの記事一覧でカバー画像のサイズと配置を変える"
slug: "PaperModの画像の配置変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "PaperMod公式の拡張CSS機能とCSS Gridを使い、記事一覧カードのカバー画像を小さくして本文の横に配置します。"
date: "2022-09-11T18:50:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

この記事は、PaperModの記事一覧にあるカードのカバー画像を小さくし、タイトルの下で要約の横に置く例です。テーマのCSSファイルや配布テンプレートは直接編集せず、サイト側の拡張CSSを使います。PaperModのクラス名を対象にするため、テーマを更新した後はブラウザーで表示を確認してください。

## 拡張CSSを追加する

サイトのルートに`assets/css/extended/custom.css`を作成します。PaperModはこのフォルダー内のCSSをテーマのスタイルに追加します。画像とテキストの順番は既存のHTMLを保ったままCSS Gridで配置します。

```css
/* Add to assets/css/extended/custom.css */
.post-entry {
    display: grid;
    grid-template-columns: minmax(0, 150px) minmax(0, 1fr);
    grid-template-areas:
        "cover title"
        "cover summary"
        "cover meta";
    column-gap: 1rem;
    align-items: start;
}

.post-entry > .entry-cover {
    grid-area: cover;
    margin-bottom: 0;
}

.post-entry > .entry-header {
    grid-area: title;
    min-width: 0;
}

.post-entry > .entry-content {
    grid-area: summary;
    min-width: 0;
}

.post-entry > .entry-footer {
    grid-area: meta;
}

.post-entry .entry-cover img {
    display: block;
    width: 100%;
    height: auto;
}

@media (max-width: 600px) {
    .post-entry {
        grid-template-columns: minmax(0, 96px) minmax(0, 1fr);
        column-gap: 0.75rem;
    }
}
```

## 狭い画面で調整する

画面が狭いときは列幅と間隔を小さくして、本文が読みづらくならないようにします。好みの見た目に合わせて150pxやブレークポイントを調整してください。画像は`height: auto`で縦横比を保ちます。切り抜きたい場合だけ`aspect-ratio`と`object-fit: cover`を追加します。

## テーマファイルを直接編集しない

以前の例にあった`blank.css`は拡張CSSが空のときに使われるプレースホルダーです。テーマ同梱の`post-entry.css`を変更したり、そこにあるコメント済みの`/* width: 100%; */`を削除したりする必要はありません。コメントを消してもスタイルは変わりません。HTML構造そのものを変えたい場合はサイト側にレイアウトを複製してオーバーライドできますが、テーマ更新時に差分を保守する必要があります。

## 表示を確認する

Hugoを起動し、ホームとタグ・カテゴリ一覧を広い画面と狭い画面で確認します。カード内で画像、タイトル、要約、メタデータが重ならず、記事リンクを覆うテーマ既定のクリック領域も動作することを確かめます。テーマ更新でクラス名やHTMLが変わった場合はCSSを調整してください。この記事の例はPaperModの一覧カード用で、記事本文中の画像には適用されません。

## 参考資料

- [PaperMod FAQ: bundling custom CSS and overriding templates](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current post-entry CSS selectors](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/common/post-entry.css)
- [PaperMod discussion #159](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)
