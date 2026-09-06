---
title: "Отметить все флажки на веб-странице"
slug: "Webページ内のすべてのチェックボックスを全チェックする"
date: 2022-10-05T20:07:06+09:00
tags: ["javascript", "автоматизация"]
draft: false
image: "img.png"
categories: ["управление блогом"]
---

Чтобы отметить все флажки на веб-странице, откройте DevTools с помощью F12, вставьте следующий код в консоль и выполните его.
```js
let boxes = document.querySelectorAll('input[type="checkbox"]');
for (let i = 0; i < boxes.length; i++) {
    if (!boxes[i].disabled) {
        boxes[i].checked = true;
    }
}
```

Или,

Создайте новую закладку и вставьте следующий код в адрес регистрации (обычно там, где вы вводите https://...).
Откройте веб-страницу, на которой вы хотите отметить флажки, нажмите на созданную закладку, и все флажки будут отмечены.
```
javascript:(function(){let boxes=document.querySelectorAll('input[type="checkbox"]');for(let i=0;i<boxes.length;i++){if(!boxes[i].disabled){boxes[i].checked=true;}}})();
```

Если вы хотите снять все флажки, измените часть `boxes[i].checked = true;` в приведенном выше скрипте на `boxes[i].checked = false;`.
