---
title: "在網頁中一次勾選或取消勾選所有核取方塊"
slug: "Webページ内のすべてのチェックボックスを全チェックする"
tags: ["javascript", "checkbox", "bookmarklet"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "使用JavaScript或書籤小程式，勾選或取消勾選目前頁面中可用的核取方塊。執行前請先確認頁面行為。"
date: "2022-10-05T20:07:06+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# 在網頁中一次勾選或取消勾選所有核取方塊

此程式會點擊目前頁面中可用的核取方塊，讓您一次完成變更。

## 執行前注意

只在可信任的網頁上執行。頁面可能會對點擊作出反應，例如變更設定或傳送要求。送出或儲存前請檢查選取結果。

## 在DevTools中執行

開啟目標網頁，並在DevTools的Console中執行下方程式碼。如果F12無法開啟DevTools，請使用瀏覽器選單。

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (!box.checked) box.click();
}
```

若要取消所有可用核取方塊，請使用以下程式碼。

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (box.checked) box.click();
}
```

## 建立書籤小程式

新增書籤，並透過書籤編輯器將下方單行程式碼貼到URL欄位。不要輸入到網址列。在目標頁面選取該書籤即可勾選可用的核取方塊。

**Select all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(!box.checked)box.click()})();
```

**Clear all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(box.checked)box.click()})();
```

若要全部取消勾選，請使用第二段程式碼或取消全選書籤小程式。程式只會作用於目前文件，並略過停用的核取方塊。

只變更`.checked`屬性可能不會透過一般點擊時發生的事件通知頁面程式。`.click()`會觸發點擊行為，但頁面本身的處理程式仍可能阻止部分變更。

## 參考資料

- [MDN: HTMLElement.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click)
- [MDN: HTMLInputElement.checked](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/checked)
- [MDN: change event](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event)
