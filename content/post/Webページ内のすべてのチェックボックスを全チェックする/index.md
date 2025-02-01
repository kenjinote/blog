---
title: 'Webページ内のすべてのチェックボックスを全チェックする'
date: 2022-10-05T20:07:06+09:00
tags: ["javascript", "自動化"]
draft: false
image: "img.png"
---

Webページ内のチェックボックスを全チェックするには、F12でDevToolsを開き、コンソールに以下のコードを貼り付けて実行します。
```js
let boxes = document.querySelectorAll('input[type="checkbox"]');
for (let i = 0; i < boxes.length; i++) {
    if (!boxes[i].disabled) {
        boxes[i].checked = true;
    }
}
```

または、

新規でブックマークを作成して、登録時のアドレス(通常はhttps://...と入力する部分に)に以下のコードを貼り付けて登録します。
チェックをつけたいWebページを表示し、作成したブックマークをクリックするとすべてのチェックボックスがチェックされます。
```
javascript:(function(){let boxes=document.querySelectorAll('input[type="checkbox"]');for(let i=0;i<boxes.length;i++){if(!boxes[i].disabled){boxes[i].checked=true;}}})();
```

全解除した場合は、上記スクリプトの`boxes[i].checked = true;`の部分を`boxes[i].checked = false;`に変更してください。