---
title: "حول علامة الإلزامية في نماذج الإدخال"
slug: "حول-علامة-الإلزامية-في-نماذج-الإدخال"
date: 2025-07-14T13:47:51+09:00
tags: ["نماذج الإدخال", "تطوير الويب", "تجربة المستخدم"]
draft: false
image: "img.png"
categories: ["إدارة المدونة"]
---

لقد قمنا بتلخيص المعلومات حول علامة "مطلوب" أو الإلزامية في واجهات المستخدم (النماذج) في الخارج، مع مواد توجيهية لواجهة المستخدم.

---

## 📌 علامات الإلزامية الرئيسية وأفضل الممارسات

1. **استخدام علامة النجمة (\*)**

    * هو الأكثر شيوعًا وانتشارًا، حيث يتم وضع "\*" على الحقول المطلوبة.
    * ومع ذلك، **من الضروري وجود شرح في بداية النموذج مثل "* حقل مطلوب"** ([Nielsen Norman Group][1], [California State University, Northridge][2]).
    * هناك أيضًا أمثلة تستخدم الألوان للتأكيد (مثل النص الأحمر).

2. **تحديد "Required" أو "(required)" بوضوح في التسمية**

    * عن طريق إضافة كلمة "Required" في التسمية (Label)، يمكن توضيح ذلك لقارئات الشاشة، مما يحسن إمكانية الوصول ([Deque][3]).

3. **الاستخدام المشترك لسمات ARIA وسمة `required` في HTML5**

    * بالإضافة إلى العرض المرئي، باستخدام `aria-required="true"` و `<input required>`، يمكن توصيل الإلزامية برمجيًا ([Deque][3]).

4. **استخدام "(optional)" لتحديد الحقول الاختيارية بوضوح**

    * هناك أيضًا طريقة لتوضيح الحقول الاختيارية باستخدام "(optional)" بدلاً من الحقول المطلوبة، وهي فعالة عند خلط الاثنين.
    * ومع ذلك، يشير Nielsen‑Norman إلى أنه "من الأسهل الحكم إذا تم توضيح الإلزامية أيضًا" ([TPGi][4]).

---

## ✅ ملخص مواد توجيهات واجهة المستخدم

| المصدر | المحتوى |
| --- | --- |
| **NN/g: Marking Required Fields in Forms** | يُنصح باستخدام النجمة + نص توضيحي، ويُعتبر عرض الاختياري فقط غير ودي ([Nielsen Norman Group][1]). |
| **Deque (Anatomy of Accessible Forms)** | ・استخدام نص "Required" أو صورة في التسمية.<br>・تم التصريح بأن الإشارة باللون وحده غير كافية. |
| **W3C Techniques (H90)** | تضمين النجمة أو "(required)" في التسمية، وتحديد المعنى في بداية النموذج. |
| **TPGi (Doing what's required)** | مع مراعاة إمكانية الوصول، تم تقييم إدراج النجمة + سمة ARIA + نص التسمية على أنه الأمثل. |
| **دليل Contensis لتجربة مستخدم النماذج** | تم تلخيصه بإيجاز بأن وضع العلامات المتسق (\* أو (optional)) أمر مهم. |

---

## ✅ النهج الموصى به في التنفيذ

* إضافة نص توضيحي **في بداية النموذج** :

  > Fields marked with \* are required.
  > (أو بشكل جماعي "All fields are required"، وإذا كان هناك خيار اختياري "unless marked optional")

* **إضافة تسمية (Label)** :

    * الكتابة مثل `First Name *` أو `Email (required)`.

* **سمات ARIA و HTML5** :

  ```html
  <label for="email">Email <abbr title="required">*</abbr></label>
  <input id="email" required aria-required="true">
  ```

* **لا تعتمد على اللون فقط** : قم بدعم العرض المرئي والبرمجي معًا.

---

## 🔗 روابط مرجعية (مواد إرشادات واجهة المستخدم)

* NN/g: *Marking Required Fields in Forms* ([California State University, Northridge][2], [Nielsen Norman Group][1], [Deque][3])
* Deque: *Anatomy of Accessible Forms* ([Deque][3])
* W3C Techniques: *H90 Indicating required form controls* ([W3C][5])
* TPGi: *Indicating mandatory fields accessibly* ([TPGi][4])
* Contensis: *UX Forms Guidelines* ([Contensis][6])

---

إذا لزم الأمر، يمكننا أيضًا تقديم أمثلة محددة لأكواد HTML/CSS، وقوالب تصميم مكونات واجهة المستخدم لـ Sketch أو Figma، وما إلى ذلك. لا تتردد في استشارتنا!

[1]: https://www.nngroup.com/articles/required-fields/?utm_source=chatgpt.com "Marking Required Fields in Forms - NN/g"
[2]: https://www.csun.edu/universal-design-center/web-accessibility-criteria-required-fields?utm_source=chatgpt.com "Web Accessibility Criteria - Required Fields - CSUN"
[3]: https://www.deque.com/blog/anatomy-of-accessible-forms-required-form-fields/?utm_source=chatgpt.com "The Anatomy of Accessible Forms: Required Form Fields"
[4]: https://www.tpgi.com/doing-whats-required-indicating-mandatory-fields-in-an-accessible-way/?utm_source=chatgpt.com "Doing what's required: Indicating mandatory fields in an accessible ..."
[5]: https://www.w3.org/TR/WCAG20-TECHS/H90.html?utm_source=chatgpt.com "H90: Indicating required form controls using label or legend - W3C"
[6]: https://www.contensis.com/community/blog/ux-forms-guidelines?utm_source=chatgpt.com "Build better web forms: 15 UX guidelines that work - Contensis"
