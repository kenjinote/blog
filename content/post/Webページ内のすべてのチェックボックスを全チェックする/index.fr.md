---
title: "Cocher toutes les cases sur une page web"
slug: "Cocher toutes les cases sur une page web"
date: 2022-10-05T20:07:06+09:00
tags: ["javascript", "automatisation"]
draft: false
image: "img.png"
categories: ["gestion de blog"]
---

Pour cocher toutes les cases sur une page web, ouvrez les DevTools avec F12, collez le code suivant dans la console et exécutez-le.
```js
let boxes = document.querySelectorAll('input[type="checkbox"]');
for (let i = 0; i < boxes.length; i++) {
    if (!boxes[i].disabled) {
        boxes[i].checked = true;
    }
}
```

Ou,

Créez un nouveau favori et collez le code suivant dans l'adresse d'enregistrement (la partie où vous tapez généralement https://...).
Affichez la page web que vous souhaitez cocher, puis cliquez sur le favori créé pour cocher toutes les cases.
```
javascript:(function(){let boxes=document.querySelectorAll('input[type="checkbox"]');for(let i=0;i<boxes.length;i++){if(!boxes[i].disabled){boxes[i].checked=true;}}})();
```

Pour tout décocher, remplacez la partie `boxes[i].checked = true;` du script ci-dessus par `boxes[i].checked = false;`.
