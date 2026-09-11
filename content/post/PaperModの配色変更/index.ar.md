---
title: 'كيفية تغيير الألوان ونظام الألوان في قالب Hugo PaperMod باستخدام CSS'
slug: "PaperModの配色変更"
date: 2022-09-07T15:30:21+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.webp"
categories: ["إدارة المدونة"]
description: 'نشرح كيفية تخصيص نظام الألوان بالكامل في قالب Hugo PaperMod. نعرض أمثلة محددة لإعداد المتغيرات من أجل تطبيق نظام الألوان المفضل لديك عن طريق تحرير ملف CSS (blank.css) الذي يتضمن تعريفات أنماط لون الخلفية، ولون النص، وكتل الأكواد، وغيرها.'
---
لقد قمت بتغيير نظام الألوان لسمة PaperMod. لقد أشرت إلى ما يلي لطريقة التغيير.

https://github.com/adityatelange/hugo-PaperMod/discussions/645

مسار CSS هو كما يلي.

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
