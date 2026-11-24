---
title: "Seleccionar o desmarcar todas las casillas de una página web"
slug: "Webページ内のすべてのチェックボックスを全チェックする"
tags: ["javascript", "checkbox", "bookmarklet"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Usa JavaScript o un marcador para seleccionar o desmarcar casillas habilitadas en la página actual. Revisa el comportamiento de la página antes de ejecutar el código."
date: "2022-10-05T20:07:06+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Seleccionar o desmarcar todas las casillas de una página web

Este script hace clic en las casillas habilitadas de la página actual para cambiarlas todas a la vez.

## Antes de ejecutarlo

Ejecútalo solo en páginas de confianza. La página puede reaccionar a los clics cambiando ajustes o enviando solicitudes. Revisa el resultado antes de enviar o guardar nada.

## Ejecutarlo en DevTools

Abre la página y ejecuta el código siguiente en la consola de DevTools. Si F12 no abre DevTools en tu navegador, usa el menú del navegador.

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (!box.checked) box.click();
}
```

Para desmarcar todas las casillas habilitadas, usa este código.

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (box.checked) box.click();
}
```

## Crear un marcador

Crea un marcador y pega el código de una línea en el campo URL mediante el editor de marcadores. No lo escribas en la barra de direcciones. Al seleccionar el marcador en la página, se marcarán las casillas habilitadas.

**Select all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(!box.checked)box.click()})();
```

**Clear all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(box.checked)box.click()})();
```

Para desmarcarlas, usa el segundo ejemplo o el marcador para desmarcar todo. El script solo afecta al documento actual y omite las casillas deshabilitadas.

Cambiar solo la propiedad `.checked` puede no notificar al código de la página mediante los eventos habituales de un clic. `.click()` activa el comportamiento del clic; aun así, el código propio de la página puede impedir algunos cambios.

## Referencias

- [MDN: HTMLElement.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click)
- [MDN: HTMLInputElement.checked](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/checked)
- [MDN: change event](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event)
