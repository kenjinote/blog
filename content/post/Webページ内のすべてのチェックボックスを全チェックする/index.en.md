---
title: "Select or Clear All Checkboxes on a Web Page"
slug: "Webページ内のすべてのチェックボックスを全チェックする"
tags: ["javascript", "checkbox", "bookmarklet"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Use JavaScript or bookmarklets to select or clear enabled checkboxes in the current page. Review the page behavior before running the code."
date: "2022-10-05T20:07:06+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Select or Clear All Checkboxes on a Web Page

This script clicks enabled checkboxes in the current page so you can change them together instead of one at a time.

## Before you run it

Run this only on pages you trust. A page may react to checkbox clicks by changing settings or sending requests. Review the resulting selections before submitting or saving anything.

## Run it in DevTools

Open the target page and run the code below in the DevTools Console. If F12 does not open DevTools in your browser, use the browser menu.

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (!box.checked) box.click();
}
```

To clear all enabled checkboxes, use this code.

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (box.checked) box.click();
}
```

## Create a bookmarklet

Create a bookmark and paste the one-line code below into the bookmark URL field using the bookmark editor. Do not enter it in the address bar. Choose the bookmark while viewing the target page to select enabled checkboxes.

**Select all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(!box.checked)box.click()})();
```

**Clear all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(box.checked)box.click()})();
```

To clear the selections, use the second code sample or the clear-all bookmarklet. The script affects only the current document and skips disabled checkboxes.

Changing the `.checked` property alone may not notify page code through the events that normally accompany a click. `.click()` triggers click behavior. Page-specific handlers can still prevent some items from changing.

## References

- [MDN: HTMLElement.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click)
- [MDN: HTMLInputElement.checked](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/checked)
- [MDN: change event](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event)
