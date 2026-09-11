---
title: 'Wie man das Farbschema und Farbthema des Hugo PaperMod-Themes mit CSS ändert'
slug: "PaperModの配色変更"
date: 2022-09-07T15:30:21+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.webp"
categories: ["Blog-Verwaltung"]
description: 'Erklärt, wie man das allgemeine Farbschema im PaperMod-Theme von Hugo anpasst. Stellt konkrete Beispiele für Variableneinstellungen vor, um ein bevorzugtes Farbschema anzuwenden, indem das CSS (blank.css) bearbeitet wird, das Stildefinitionen für Hintergrundfarbe, Textfarbe, Codeblöcke usw. enthält.'
---
Ich habe das Farbschema des PaperMod-Themas geändert. Für die Änderungsmethode habe ich Folgendes konsultiert.

https://github.com/adityatelange/hugo-PaperMod/discussions/645

Der CSS-Pfad lautet wie folgt.

`themes/PaperMod/assets/css/extended/blank.css`

```
:root {
    --entry: #fbf7ef;
    --primary: rgba(113, 103, 91, 1.00);
    --secondary: rgba(113, 103, 91, 0.95);
    --tertiary: rgba(113, 103, 91, 0.50);
    --content: rgba(113, 103, 91, 0.85);
    --hljs-bg: #34231B;
    --code-bg: #ebe4d7;
    --border: #fdfaf5;
    --theme: #fbf7ef;
}
.dark {
}
```

Vorerst keine Änderungen für den Dunkelmodus.
