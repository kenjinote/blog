---
title: "Webページのチェックボックスを一括で選択・解除する方法"
slug: "Webページ内のすべてのチェックボックスを全チェックする"
tags: ["javascript", "checkbox", "bookmarklet"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "JavaScriptで現在のページの有効なチェックボックスを選択または解除する方法と、ブックマークレットを紹介します。実行前にページの動作を確認してください。"
date: "2022-10-05T20:07:06+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Webページのチェックボックスを一括で選択・解除する方法

このスクリプトは、現在のページにある有効なチェックボックスをクリックして切り替えます。画面上のボタンを一つずつ操作する代わりにまとめて変更できます。

## 実行前の注意

信頼できるページでのみ実行してください。チェック操作にページ側のイベントが反応して、設定変更や通信が発生することがあります。選択結果を確認してから送信・保存などの操作を行ってください。

## DevToolsで実行する

対象ページを開き、DevToolsのConsoleで次のコードを実行します。F12でDevToolsが開かない環境ではブラウザーのメニューから開いてください。

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (!box.checked) box.click();
}
```

全解除するコードは次のとおりです。

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (box.checked) box.click();
}
```

## ブックマークレットを作成する

新しいブックマークを作り、ブックマークの編集画面でURL欄に次の1行を登録します。アドレスバーに入力するのではなく、ブックマークのURLとして保存してください。対象ページでブックマークを選ぶと有効なチェックボックスを選択します。

**Select all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(!box.checked)box.click()})();
```

**Clear all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(box.checked)box.click()})();
```

全解除したい場合は、2つ目のコードまたは解除用ブックマークレットを使用します。スクリプトは現在の文書だけを対象にし、無効なチェックボックスを飛ばします。

チェックボックスの`.checked`プロパティを直接変更するだけでは、通常のクリック操作で発生するイベントがページに伝わらない場合があります。`.click()`を使うとクリック動作を発生させます。ページ固有の処理によって一部の項目が変更されないこともあります。

## 参考資料

- [MDN: HTMLElement.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click)
- [MDN: HTMLInputElement.checked](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/checked)
- [MDN: change event](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event)
