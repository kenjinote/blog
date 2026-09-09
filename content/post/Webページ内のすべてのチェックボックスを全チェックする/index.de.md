---
title: '[JS] Wie man alle Kontrollkästchen auf einer Webseite auf einmal auswählt (mit Bookmarklet)'
slug: "Alle Kontrollkästchen auf einer Webseite aktivieren"
date: 2022-10-05T20:07:06+09:00
tags: ["javascript", "automatisierung"]
draft: false
image: "img.webp"
categories: ["blog-management"]
description: 'Wir erklären, wie Sie alle Kontrollkästchen auf einer Webseite auf einmal auswählen. Wir stellen den JavaScript-Code zur Ausführung in der Chrome DevTools-Konsole sowie die Schritte zur Erstellung eines praktischen Bookmarklets vor, mit dem alles mit einem Klick ausgewählt oder abgewählt werden kann.'
---

Um alle Kontrollkästchen auf einer Webseite zu aktivieren, öffnen Sie die DevTools mit F12, fügen Sie den folgenden Code in die Konsole ein und führen Sie ihn aus.
```js
let boxes = document.querySelectorAll('input[type="checkbox"]');
for (let i = 0; i < boxes.length; i++) {
    if (!boxes[i].disabled) {
        boxes[i].checked = true;
    }
}
```

Oder,

Erstellen Sie ein neues Lesezeichen und fügen Sie den folgenden Code in die Registrierungsadresse ein (der Teil, in den Sie normalerweise https://... eingeben).
Zeigen Sie die Webseite an, die Sie aktivieren möchten, und klicken Sie auf das erstellte Lesezeichen. Alle Kontrollkästchen werden aktiviert.
```
javascript:(function(){let boxes=document.querySelectorAll('input[type="checkbox"]');for(let i=0;i<boxes.length;i++){if(!boxes[i].disabled){boxes[i].checked=true;}}})();
```

Um alle zu deaktivieren, ändern Sie bitte den Teil `boxes[i].checked = true;` des obigen Skripts in `boxes[i].checked = false;`.
