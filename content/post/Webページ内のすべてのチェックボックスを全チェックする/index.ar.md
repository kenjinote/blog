---
title: "تحديد جميع مربعات الاختيار في صفحة الويب"
slug: "Webページ内のすべてのチェックボックスを全チェックする"
date: 2022-10-05T20:07:06+09:00
tags: ["javascript", "أتمتة"]
draft: false
image: "img.png"
categories: ["إدارة المدونة"]
---

لتحديد جميع مربعات الاختيار في صفحة ويب، افتح أدوات المطور (DevTools) بالضغط على F12، ثم الصق الكود التالي في وحدة التحكم (Console) وقم بتشغيله.
```js
let boxes = document.querySelectorAll('input[type="checkbox"]');
for (let i = 0; i < boxes.length; i++) {
    if (!boxes[i].disabled) {
        boxes[i].checked = true;
    }
}
```

أو،

أنشئ إشارة مرجعية جديدة، وفي عنوان التسجيل (الجزء الذي تكتب فيه عادةً https://...) الصق الكود التالي.
افتح صفحة الويب التي تريد تحديد مربعات الاختيار فيها، وانقر على الإشارة المرجعية التي أنشأتها، وسيتم تحديد جميع مربعات الاختيار.
```
javascript:(function(){let boxes=document.querySelectorAll('input[type="checkbox"]');for(let i=0;i<boxes.length;i++){if(!boxes[i].disabled){boxes[i].checked=true;}}})();
```

إذا كنت تريد إلغاء تحديد الكل، فقم بتغيير جزء `boxes[i].checked = true;` في البرنامج النصي أعلاه إلى `boxes[i].checked = false;`.
