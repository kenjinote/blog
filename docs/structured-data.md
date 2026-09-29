# JSON-LD

`layouts/partials/head/structured-data.html` で各ページの head に JSON-LD を出力します。
Google の記事向けガイド: https://developers.google.com/search/docs/appearance/structured-data/article

- 全ページ（404 を除く）: 言語別の `WebSite` とページを `isPartOf` で関連付けます。
- `params.mainSections` に含まれる記事: `BlogPosting`。タイトル、説明、公開日、更新日、著者、発行者、画像、タグ、言語、正規 URL を出力します。
- ホーム・セクション・カテゴリ・タグ・アーカイブ: `CollectionPage`。
- その他の固定ページ: `WebPage`。

標準の著者・発行者は `hugo.yaml` の `params.author` で設定します。
記事の front matter に文字列の `author` があれば著者名を上書きします。
その場合、標準著者のプロフィール URL は流用しません。
画像は既存の Open Graph と同じヘルパーで解決し、日付や画像がない場合は該当プロパティを省略します。
値は `jsonify` でシリアライズし、引用符・改行・HTML 特殊文字を安全にエスケープします。

検証:

```powershell
hugo --minify --buildFuture
python scripts/check_structured_data.py public
```

検証スクリプトは生成済みのサイトマップに載る全 HTML ページを対象とします。
これにより、再利用した `public` に残っている削除済み記事などの古いファイルを除外します。

公開後の検索エンジン側の検証には Google のリッチリザルトテストを利用できます。
