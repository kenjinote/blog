---
title: "إضافة أمر لإدراج التاريخ في IntelliJ IDEA"
slug: "IntelliJ IDEAで日付を貼り付けるコマンドを追加する"
date: 2022-09-04T05:59:04+09:00
tags: ["IntelliJ IDEA"]
draft: false
image: "images/IntelliJ_logo.png"
categories: ["IT・テクノロジー"]
---
# مقدمة
عند كتابة هذه المدونة، أستخدم IntelliJ IDEA. إنه مناسب لأن توافقه مع Git جيد ويعرض معاينة Markdown.
في كل مرة أكتب فيها في المدونة، أضطر إلى كتابة التاريخ في ترويسة ملف md، ولا يبدو أن هناك اختصارًا لإدراج التاريخ، لذلك قمت بإنشاء أمر لإدراج التاريخ بالرجوع إلى الموقع أدناه. آمل أن يكون هذا مفيدًا.

[Is there a shortcut for inserting date/time in IntelliJ IDEA?](https://stackoverflow.com/questions/8714779/is-there-a-shortcut-for-inserting-date-time-in-intellij-idea)

# خطوات الإعداد
1. افتح من القائمة "File" > "Settings..."  
   ![settings](./images/settings.png)
2. حدد "Editor" > "Live Template" > "HTML/XML" وانقر فوق "+"
3. اختر Live Template
4. أدخل "date" في Abbreviation
5. أدخل "إدراج التاريخ والوقت" في Description
6. أدخل "$date$" في Template Text
7. انقر فوق زر Edit Variables  
   ![edit_template_variables](./images/edit_template_variables.png)
8. أدخل "date" في Name
9. أدخل ``date("yyyy-MM-dd'T'HH:mm:ss'+09:00'")`` في Expression
10. أغلق مربع الحوار بالنقر فوق OK
11. اضغط على Define أو Change وحدد مربع "Everywhere"
12. أغلق مربع الحوار بالنقر فوق OK
13. في محرر التعليمات البرمجية، اكتب "date" واضغط على Enter. إذا تم إدراج التاريخ "2022-09-04T05:59:04+09:00"، يكون الإعداد قد اكتمل!

هذا كل شيء.

# خاتمة
سأشاركها مرة أخرى إذا وجدت حيلًا صغيرة أخرى لـ IntelliJ IDEA!
