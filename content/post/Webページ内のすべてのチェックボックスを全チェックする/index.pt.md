---
title: "Marcar todas as caixas de seleção em uma página da web"
slug: "Marcar todas as caixas de seleção em uma página da web"
date: 2022-10-05T20:07:06+09:00
tags: ["javascript", "automatização"]
draft: false
image: "img.png"
categories: ["gestão de blog"]
---

Para marcar todas as caixas de seleção em uma página da web, abra o DevTools com F12, cole o seguinte código no console e execute-o.
```js
let boxes = document.querySelectorAll('input[type="checkbox"]');
for (let i = 0; i < boxes.length; i++) {
    if (!boxes[i].disabled) {
        boxes[i].checked = true;
    }
}
```

Ou,

Crie um novo favorito e cole o seguinte código no endereço de registro (a parte onde você normalmente digita https://...).
Exiba a página da web que deseja marcar e clique no favorito criado; todas as caixas de seleção serão marcadas.
```
javascript:(function(){let boxes=document.querySelectorAll('input[type="checkbox"]');for(let i=0;i<boxes.length;i++){if(!boxes[i].disabled){boxes[i].checked=true;}}})();
```

Para desmarcar todas, altere a parte `boxes[i].checked = true;` do script acima para `boxes[i].checked = false;`.
