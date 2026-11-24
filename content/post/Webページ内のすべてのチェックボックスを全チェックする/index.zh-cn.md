---
title: "在网页中批量勾选或取消勾选复选框"
slug: "Webページ内のすべてのチェックボックスを全チェックする"
tags: ["javascript", "checkbox", "bookmarklet"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "使用JavaScript或书签脚本，在当前网页中勾选或取消勾选可用的复选框。运行前请先了解页面行为。"
date: "2022-10-05T20:07:06+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# 在网页中批量勾选或取消勾选复选框

此脚本会点击当前网页中可用的复选框，从而一次性更改，而不必逐个操作。

## 运行前请注意

仅在可信网页上运行。页面可能会对勾选操作作出反应，例如更改设置或发送请求。提交或保存之前，请检查选择结果。

## 在DevTools中运行

打开目标网页，在DevTools的Console中运行以下代码。如果浏览器中的F12无法打开DevTools，请使用浏览器菜单打开。

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (!box.checked) box.click();
}
```

如需取消所有可用复选框的勾选，请使用以下代码。

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (box.checked) box.click();
}
```

## 创建书签脚本

新建书签，并通过书签编辑器将下面的一行代码粘贴到书签URL栏中。不要在地址栏中输入。打开目标网页后选择该书签，即可勾选可用的复选框。

**Select all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(!box.checked)box.click()})();
```

**Clear all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(box.checked)box.click()})();
```

如需取消所有选择，请使用第二段代码或取消全选书签脚本。脚本只作用于当前文档，并跳过已禁用的复选框。

仅更改`.checked`属性可能不会触发页面通常在点击时接收的事件。`.click()`会触发点击行为，但页面自身的处理程序仍可能阻止某些项目更改。

## 参考资料

- [MDN: HTMLElement.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click)
- [MDN: HTMLInputElement.checked](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/checked)
- [MDN: change event](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event)
