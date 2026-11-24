---
title: "Как отметить или снять отметку во всех флажках на веб-странице"
slug: "Webページ内のすべてのチェックボックスを全チェックする"
tags: ["javascript", "checkbox", "bookmarklet"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Используйте JavaScript или букмарклет, чтобы отметить или снять отметку во включённых флажках текущей страницы. Перед запуском проверьте поведение страницы."
date: "2022-10-05T20:07:06+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Как отметить или снять отметку во всех флажках на веб-странице

Скрипт нажимает на доступные флажки в текущем документе, чтобы изменить их сразу, а не по одному.

## Перед запуском

Запускайте код только на доверенных страницах. Страница может реагировать на нажатия, менять настройки или отправлять запросы. Проверьте выбор перед отправкой или сохранением.

## Запуск в DevTools

Откройте нужную страницу и выполните код ниже в консоли DevTools. Если F12 не открывает DevTools, воспользуйтесь меню браузера.

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (!box.checked) box.click();
}
```

Чтобы снять отметки во всех доступных флажках, используйте этот код.

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (box.checked) box.click();
}
```

## Создание букмарклета

Создайте закладку и вставьте однострочный код в поле URL через редактор закладок. Не вводите его в адресную строку. Выберите закладку на нужной странице, чтобы отметить доступные флажки.

**Select all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(!box.checked)box.click()})();
```

**Clear all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(box.checked)box.click()})();
```

Чтобы снять отметки, используйте второй пример или букмарклет для снятия всех отметок. Скрипт действует только в текущем документе и пропускает отключённые флажки.

Одно лишь изменение свойства `.checked` может не передать коду страницы события, которые обычно возникают при нажатии. `.click()` запускает поведение щелчка, однако обработчик самой страницы всё равно может помешать некоторым изменениям.

## Источники

- [MDN: HTMLElement.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click)
- [MDN: HTMLInputElement.checked](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/checked)
- [MDN: change event](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event)
