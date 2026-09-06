---
title: "勾選網頁中的所有核取方塊"
slug: "勾選網頁中的所有核取方塊"
date: 2022-10-05T20:07:06+09:00
tags: ["javascript", "自動化"]
draft: false
image: "img.png"
categories: ["部落格營運"]
---

要勾選網頁中的所有核取方塊，請按 F12 開啟 DevTools，將以下代碼貼上到主控台並執行。
```js
let boxes = document.querySelectorAll('input[type="checkbox"]');
for (let i = 0; i < boxes.length; i++) {
    if (!boxes[i].disabled) {
        boxes[i].checked = true;
    }
}
```

或者，

建立一個新書籤，並將以下代碼貼上到註冊網址處（通常是輸入 https://... 的地方）進行註冊。
顯示您想要勾選的網頁，然後點擊已建立的書籤，所有的核取方塊就會被勾選。
```
javascript:(function(){let boxes=document.querySelectorAll('input[type="checkbox"]');for(let i=0;i<boxes.length;i++){if(!boxes[i].disabled){boxes[i].checked=true;}}})();
```

如果要全部取消勾選，請將上述腳本中的 `boxes[i].checked = true;` 部分更改為 `boxes[i].checked = false;`。
