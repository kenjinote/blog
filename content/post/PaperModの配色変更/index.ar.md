---
title: 'كيفية تغيير الألوان ونظام الألوان في قالب Hugo PaperMod باستخدام CSS'
date: "2026-09-24T19:44:38+09:00"
slug: "PaperModの配色変更"
date: 2022-09-07T15:30:21+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'نشرح كيفية تخصيص نظام الألوان بالكامل في قالب Hugo PaperMod. نعرض أمثلة محددة لإعداد المتغيرات من أجل تطبيق نظام الألوان المفضل لديك عن طريق تحرير ملف CSS (blank.css) الذي يتضمن تعريفات أنماط لون الخلفية، ولون النص، وكتل الأكواد، وغيرها.'
---
لقد قمت بتغيير نظام الألوان لسمة PaperMod. لقد أشرت إلى ما يلي لطريقة التغيير.

https://github.com/adityatelange/hugo-PaperMod/discussions/645

[مسار](/ar/p/windows-%E3%81%A7%D9%85%D8%B3%D8%A7%D8%B1%E3%81%AE%E9%80%9A%E3%81%A3%E3%81%9F%D9%85%D9%84%D9%81-%D8%AA%D9%86%D9%81%D9%8A%D8%B0%D9%8A%E3%81%AE%E5%A0%B4%E6%89%80%E3%82%92%E8%A6%8B%E3%81%A4%E3%81%91%E3%82%8B%E6%96%B9%E6%B3%95/) CSS هو كما يلي.

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

لا توجد تغييرات على المظهر الداكن في الوقت الحالي.
