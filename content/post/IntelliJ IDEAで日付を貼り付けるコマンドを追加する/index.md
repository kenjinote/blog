---
title: 'IntelliJ IDEAで現在の日付を挿入するショートカットの作成方法'
slug: "IntelliJ IDEAで日付を貼り付けるコマンドを追加する"
date: 2022-09-04T05:59:04+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA"]
draft: false
image: "images/IntelliJ_logo.webp"
categories: ["it-technology"]
description: 'IntelliJ IDEAのLive Templateで、ローカルのタイムゾーンオフセットを含むISO 8601形式の日時を挿入する方法を説明します。現在の設定画面、変数式、展開キーをJetBrains公式資料に沿って紹介します。'
---

# はじめに

記事の作成時に日時を何度も入力する場合は、IntelliJ IDEAのLive Templateに登録すると、短い略語から自動挿入できます。以下では、ローカル時刻とUTCオフセットを含むISO 8601形式の日時を挿入する設定を作成します。

## Live Templateを作成する

1. **Settings > Editor > Live Templates** を開きます。Windows/Linuxでは **File > Settings**、macOSでは **IntelliJ IDEA > Settings** から開けます。
2. テンプレートのグループ（例: **other**）を選び、**+ > Live Template** をクリックします。
3. **Abbreviation** に `date`、**Description** に用途を入力します。
4. **Template text** に `$date$` と入力します。
5. **Edit Variables** を開き、変数 `date` の **Expression** に `date("yyyy-MM-dd'T'HH:mm:ssXXX")` を入力します。**Skip if defined** をオンにして、展開時に値を自動計算します。
6. **Define** をクリックし、日付を挿入したいコンテキスト（必要に応じて **Everywhere**）を選びます。設定を保存します。

## テンプレートを使う

エディターで `date` と入力し、既定の展開キー **Tab** を押すと、現在のシステム日時が `2026-11-24T09:30:00+09:00` のような形式で挿入されます。時刻とオフセットはコンピューターの現在のタイムゾーンに基づきます。展開キーを変更している場合は、Live Templates設定でキーを確認してください。

`XXX` はISO 8601形式のタイムゾーンオフセットを出力します。固定の `+09:00` を使わないため、別のタイムゾーンの読者も自分のローカル時刻で使えます。生成された日時が記事の意図する公開時刻と合っているか確認してください。

## 参考

- [Live Templateの作成と編集](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [Live Template変数とdate関数](https://www.jetbrains.com/help/idea/template-variables.html)
- [Live Templateの展開キー設定](https://www.jetbrains.com/help/idea/settings-live-templates.html)
