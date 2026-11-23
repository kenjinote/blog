---
title: 'Ranklet4でGA4の人気ページランキングをHugoに表示する方法'
date: 2023-04-10T20:26:57+09:00
lastmod: 2026-11-23
slug: "Googleアナリティクスから人気ページランキングを取得して配置する方法"
tags: ["Googleアナリティクス", "Ranklet", "HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: '旧Rankletの終了後に提供されたRanklet4を使い、Google Analytics 4（GA4）の人気ページランキングをHugoへ設置する手順を解説します。旧ウィジェットからの移行、権限、テンプレート、外部サービス利用時の確認点を紹介します。'
---

# Ranklet4でGA4の人気ページランキングをHugoに表示する

この記事の旧手順は、Google Analyticsの「ビュー」と終了済みのRankletウィジェットを使っていました。旧Rankletは2023年にサービスを終了しています。現在はGA4に対応した別サービスのRanklet4を使うため、旧タグは新しいタグに置き換えてください。[旧RankletからRanklet4への公式移行案内](https://docs.ranklet4.com/changes.html)

Ranklet4はGA4のレポートデータを集計し、JavaScriptウィジェットとしてランキングを配信します。Hugoなど静的サイトでも利用できます。メニューやプランは変更される可能性があるため、実際の画面と[公式チュートリアル](https://docs.ranklet4.com/tutorial.html)を基準にしてください。

## 利用前に確認すること

* サイトのアクセスデータが記録されているGA4プロパティがあること。
* Googleサインインに使うアカウントが、そのプロパティの「閲覧者」以上の権限を持つこと。運営者権限を持つ個人アカウントを使う必要はありません。
* Ranklet4へGoogle Analyticsデータを共有することになります。利用規約には、アクセス解析データを使用・複製・配布し、派生物を作成・表示するための広いライセンスと、個人を特定できない統計情報を利用・公開できる旨が含まれます。[利用規約](https://docs.ranklet4.com/agreement.html)と[プライバシーポリシー](https://ranklet4.com/docs/privacy)を読み、データを共有する権利と条件を確認してから連携してください。旧Rankletとはデータの利用条件が異なる場合があります。

## ランキングを作成する

1. [Ranklet4](https://ranklet4.com/)へ、対象のGA4プロパティを閲覧できるGoogleアカウントでサインインします。画面の説明と権限を確認してからアクセスを許可してください。
2. 新しいランキングを作り、対象のGA4プロパティ、集計期間、表示件数を選びます。タイトルやURLの条件を設定し、トップページなどランキングに含めたくないページを除外します。
3. 必要に応じてタイトルの文字列置換を設定します。プレビューでタイトルと集計結果を確認してください。
4. デザインギャラリーからテンプレートを選ぶか、HTML/CSSテンプレートをカスタマイズします。新しいテンプレートはHandlebarsを使います。項目名や記法は[テンプレートガイド](https://docs.ranklet4.com/template.html)を確認してください。
5. 保存・公開し、管理画面に表示されたランキングタグをそのままコピーします。旧RankletのタグやIDは流用せず、サービス画面が発行した新しいものを使います。

最小のHTMLテンプレート例です。実際の項目名と繰り返し構文は、公式テンプレートガイドを参照してください。

```handlebars
<ol class="popular-pages">
  {{#each rankings}}
  <li><a href="{{url}}">{{title}}</a></li>
  {{/each}}
</ol>
```

## Hugoに設置する

1. Hugoプロジェクトに`layouts/partials/ranklet4.html`を作り、Ranklet4管理画面で発行されたランキングタグを貼り付けます。
2. 表示したいレイアウト（例:`layouts/_default/single.html`やサイドバーのpartial）に、次のHugoコードを追加します。

```go-html-template
{{- partial "ranklet4.html" . }}
```

3. ローカルでページを表示してレイアウトを確認し、公開後もHTTPSでウィジェットが読み込まれることを確かめます。配信は外部JavaScriptに依存します。表示速度、プライバシー通知、サイトのセキュリティ方針に合うかを確認してください。

## 更新と移行時の注意

ランキングはGA4の集計とRanklet4の更新スケジュールに従うため、アクセス直後に順位が変わるとは限りません。更新頻度、無料・有料機能、クレジットや広告表示は変わることがあるので、[現行プランと仕様](https://docs.ranklet4.com/plan.html)を確認してください。公開ページの情報を取得するRanklet4のクローラーについては[FAQ](https://docs.ranklet4.com/faq.html)に説明があります。

## 公式資料

* [Ranklet4チュートリアル](https://docs.ranklet4.com/tutorial.html)
* [旧RankletとRanklet4の変更点](https://docs.ranklet4.com/changes.html)
* [Ranklet4テンプレートガイド](https://docs.ranklet4.com/template.html)
* [Ranklet4 FAQ](https://docs.ranklet4.com/faq.html)
* [Ranklet4利用規約](https://docs.ranklet4.com/agreement.html)
