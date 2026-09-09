---
title: '[JS] How to Check All Checkboxes on a Web Page at Once (with Bookmarklet)'
slug: "Webページ内のすべてのチェックボックスを全チェックする"
date: 2022-10-05T20:07:06+09:00
tags: ["javascript", "automation"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'Explains how to check all checkboxes on a web page at once. Introduces the JavaScript code to run in Chrome''s DevTools console and the steps to create a convenient bookmarklet that allows you to select or deselect all with a single click.'
---

To check all checkboxes in a web page, open DevTools with F12, paste the following code into the console, and execute it.
```js
let boxes = document.querySelectorAll('input[type="checkbox"]');
for (let i = 0; i < boxes.length; i++) {
    if (!boxes[i].disabled) {
        boxes[i].checked = true;
    }
}
```

Alternatively,

Create a new bookmark, and in the address field when registering (where you usually enter https://...), paste the following code and save it.
Display the web page where you want to check the boxes, and click the created bookmark to check all checkboxes.
```
javascript:(function(){let boxes=document.querySelectorAll('input[type="checkbox"]');for(let i=0;i<boxes.length;i++){if(!boxes[i].disabled){boxes[i].checked=true;}}})();
```

If you want to uncheck all, change the `boxes[i].checked = true;` part of the above script to `boxes[i].checked = false;`.
