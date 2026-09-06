---
title: "PaperMod की रंग योजना बदलना"
slug: "PaperModの配色変更"
date: 2022-09-07T15:30:21+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.png"
categories: ["ब्लॉग संचालन"]
---
मैंने PaperMod थीम की रंग योजना बदल दी है। परिवर्तन विधि के लिए मैंने निम्नलिखित का संदर्भ लिया।

https://github.com/adityatelange/hugo-PaperMod/discussions/645

CSS का पथ नीचे दिया गया है।

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

डार्क मोड के लिए अभी कोई बदलाव नहीं।
