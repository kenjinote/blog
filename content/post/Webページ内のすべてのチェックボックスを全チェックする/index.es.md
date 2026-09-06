---

title: "Marcar todas las casillas de verificación en una página web"
date: 2022-10-05T20:07:06+09:00
tags: ["javascript", "automatización"]
draft: false
image: "img.png"
categories: ["gestión de blog"]
---


Para marcar todas las casillas de verificación en una página web, abra DevTools con F12, pegue el siguiente código en la consola y ejecútelo.
```js
let boxes = document.querySelectorAll('input[type="checkbox"]');
for (let i = 0; i < boxes.length; i++) {
    if (!boxes[i].disabled) {
        boxes[i].checked = true;
    }
}
```

O bien,

Cree un nuevo marcador y pegue el siguiente código en la dirección al registrarse (generalmente donde ingresa https://...).
Muestre la página web donde desea marcar las casillas de verificación y haga clic en el marcador que creó para marcar todas las casillas de verificación.
```
javascript:(function(){let boxes=document.querySelectorAll('input[type="checkbox"]');for(let i=0;i<boxes.length;i++){if(!boxes[i].disabled){boxes[i].checked=true;}}})();
```

Si desea desmarcar todas, cambie la parte de `boxes[i].checked = true;` del script anterior a `boxes[i].checked = false;`.
