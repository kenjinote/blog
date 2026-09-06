---
title: '全选网页内的所有复选框'
slug: "Webページ内のすべてのチェックボックスを全チェックする"
date: 2022-10-05T20:07:06+09:00
tags: ["javascript", "自动化"]
draft: false
image: "img.png"
categories: ["博客运营"]
---

要全选网页内的所有复选框，请按F12打开DevTools，将以下代码粘贴到控制台并执行。
```js
let boxes = document.querySelectorAll('input[type="checkbox"]');
for (let i = 0; i < boxes.length; i++) {
    if (!boxes[i].disabled) {
        boxes[i].checked = true;
    }
}
```

或者，

创建一个新书签，在注册时的地址栏（通常输入https://...的部分）中粘贴以下代码并保存。
打开想要勾选的网页，点击创建好的书签，所有的复选框就会被全选。
```
javascript:(function(){let boxes=document.querySelectorAll('input[type="checkbox"]');for(let i=0;i<boxes.length;i++){if(!boxes[i].disabled){boxes[i].checked=true;}}})();
```

如果要全部取消勾选，请将上述脚本中的 `boxes[i].checked = true;` 修改为 `boxes[i].checked = false;`。
