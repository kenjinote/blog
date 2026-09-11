---
title: 'How to Change the Color Scheme and Theme of Hugo PaperMod Theme Using CSS'
slug: "PaperModの配色変更"
date: 2022-09-07T15:30:21+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.webp"
categories: ["Blog Management"]
description: 'Explains how to customize the overall color scheme in Hugo''s PaperMod theme. Introduces specific variable setting examples to apply your preferred color scheme by editing the CSS (blank.css) that contains style definitions such as background colors, text colors, and code blocks.'
---
I changed the color scheme of the PaperMod theme. I referred to the following for the method.

https://github.com/adityatelange/hugo-PaperMod/discussions/645

The CSS path is as follows.

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

No changes for dark mode for now.
