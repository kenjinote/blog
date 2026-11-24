---
title: "Alle Kontrollkästchen auf einer Webseite aktivieren oder deaktivieren"
slug: "Webページ内のすべてのチェックボックスを全チェックする"
tags: ["javascript", "checkbox", "bookmarklet"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Mit JavaScript oder einem Bookmarklet können Sie aktivierte Kontrollkästchen im aktuellen Dokument auswählen oder abwählen. Prüfen Sie das Verhalten der Seite, bevor Sie den Code ausführen."
date: "2022-10-05T20:07:06+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Alle Kontrollkästchen auf einer Webseite aktivieren oder deaktivieren

Dieses Skript klickt die aktivierten Kontrollkästchen im aktuellen Dokument an, damit sie gemeinsam statt einzeln geändert werden.

## Vor der Ausführung

Führen Sie den Code nur auf vertrauenswürdigen Seiten aus. Eine Seite kann auf Klicks reagieren, Einstellungen ändern oder Anfragen senden. Prüfen Sie die Auswahl, bevor Sie etwas absenden oder speichern.

## In DevTools ausführen

Öffnen Sie die Zielseite und führen Sie den folgenden Code in der DevTools-Konsole aus. Falls F12 DevTools nicht öffnet, verwenden Sie das Browsermenü.

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (!box.checked) box.click();
}
```

Verwenden Sie diesen Code, um alle aktivierten Kontrollkästchen abzuwählen.

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (box.checked) box.click();
}
```

## Bookmarklet erstellen

Erstellen Sie ein Lesezeichen und fügen Sie den einzeiligen Code im Lesezeichen-Editor in das URL-Feld ein. Geben Sie ihn nicht in die Adressleiste ein. Wählen Sie das Lesezeichen auf der Zielseite aus, um aktivierte Kontrollkästchen anzuklicken.

**Select all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(!box.checked)box.click()})();
```

**Clear all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(box.checked)box.click()})();
```

Zum Abwählen verwenden Sie das zweite Beispiel oder das Bookmarklet zum Abwählen aller Kästchen. Das Skript wirkt nur im aktuellen Dokument und überspringt deaktivierte Kästchen.

Eine Änderung nur der `.checked`-Eigenschaft löst möglicherweise nicht die Ereignisse aus, die bei einem normalen Klick auftreten. `.click()` löst das Klickverhalten aus; seiteneigener Code kann einzelne Änderungen dennoch verhindern.

## Quellen

- [MDN: HTMLElement.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click)
- [MDN: HTMLInputElement.checked](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/checked)
- [MDN: change event](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event)
