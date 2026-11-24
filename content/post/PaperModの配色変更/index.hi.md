---
title: "CSS variables से Hugo PaperMod के रंग बदलें"
slug: "PaperModの配色変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Extended CSS से PaperMod के light और dark रंग बदलें और टेक्स्ट का contrast जाँचें।"
date: "2022-09-07T15:30:21+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PaperMod के रंग CSS custom properties (variables) से बदले जा सकते हैं। Theme फ़ाइलें संपादित करने के बजाय अपने साइट के `assets/css/extended/` में overrides रखें, ताकि theme update के दौरान बदलाव बनाए रखना आसान हो। नीचे warm light और dark palette का उदाहरण है; रंग अपने साइट के अनुसार बदलें।

## Dark mode और वर्तमान variables

वर्तमान PaperMod dark mode के लिए `html` element पर `data-theme="dark"` लगाता है। केवल `.dark` चुनने वाले पुराने उदाहरण इस selector पर लागू न हों। `--hljs-bg` भी अब code block background की वर्तमान variable नहीं है; इसका नाम `--code-block-bg` है।

```css
/* Save as assets/css/extended/theme-colors.css */
:root {
    color-scheme: light;
    --theme: #fbf7ef;
    --entry: #fffdfa;
    --primary: #433a32;
    --secondary: #665b50;
    --tertiary: #8b7f72;
    --content: #453d35;
    --code-block-bg: #34231b;
    --code-bg: #efe7da;
    --border: #ddd3c5;
}

:root[data-theme="dark"] {
    color-scheme: dark;
    --theme: #1d1e20;
    --entry: #22252a;
    --primary: #e8e6e1;
    --secondary: #b5b2ac;
    --tertiary: #55575c;
    --content: #d2d0ca;
    --code-block-bg: #17181a;
    --code-bg: #37383e;
    --border: #48484c;
}
```

## टेक्स्ट contrast

इस उदाहरण में सामान्य टेक्स्ट रंग `--primary` और `--content` अपने background से स्पष्ट contrast रखते हैं। नमूने में light mode में `--primary` और `--theme` का अनुपात लगभग 10.4:1 तथा dark mode में 13.4:1 है। सामान्य टेक्स्ट के लिए WCAG 2.2 AA का मान 4.5:1 है; syntax colors, links, borders और अन्य अवस्थाएँ अलग से जाँचें।

## Extended CSS जोड़ें और जाँचें

साइट root में stylesheet को `assets/css/extended/theme-colors.css` नाम से सहेजें। PaperMod FAQ के अनुसार `assets/css/extended/` की CSS theme styles के साथ bundle होती है। Hugo चलाकर light/dark toggle, cards, मुख्य टेक्स्ट, inline code, code blocks और links जाँचें।

## दायरा

यह केवल palette का उदाहरण है; हर टेक्स्ट, चित्र या interactive control की accessibility की गारंटी नहीं। Syntax highlight रंग `--code-block-bg` से अलग CSS में तय होते हैं, इसलिए code-block background बदलने के बाद code की पठनीयता दोबारा देखें।

## संदर्भ

- [PaperMod FAQ: custom CSS and theme assets](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current theme color variables](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/core/theme-vars.css)
- [PaperMod discussion: changing background and text colors](https://github.com/adityatelange/hugo-PaperMod/discussions/645)
- [W3C: WCAG 2.2 contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum)
