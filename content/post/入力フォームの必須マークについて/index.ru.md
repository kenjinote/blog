---
title: "О знаке обязательного заполнения в формах ввода"
slug: "о-знаке-обязательного-заполнения-в-формах-ввода"
date: 2025-07-14T13:47:51+09:00
tags: ["Формы ввода", "Веб-разработка", "UX"]
draft: false
image: "img.png"
categories: ["Ведение блога"]
---

Мы обобщили информацию об отметках "обязательно" в зарубежных пользовательских интерфейсах (формах) вместе с материалами руководств по UI.

---

## 📌 Основные знаки обязательного заполнения и лучшие практики

1. **Использование звездочки (\*)**

    * Это наиболее распространенный и широко используемый способ, когда обязательные поля помечаются символом "\*".
    * Однако **в начале формы обязательно должно быть пояснение, например, "* — обязательное поле"** ([Nielsen Norman Group][1], [California State University, Northridge][2]).
    * Также есть примеры использования цвета для выделения (например, красный текст).

2. **Явное указание "Required" или "(required)" в метке**

    * Добавление слова "Required" в текстовую метку (label) делает его понятным для программ чтения с экрана, что улучшает доступность ([Deque][3]).

3. **Совместное использование атрибутов ARIA и атрибута `required` в HTML5**

    * В дополнение к визуальному отображению использование `aria-required="true"` и `<input required>` позволяет программно передать обязательность поля ([Deque][3]).

4. **Использование "(optional)" для явного указания необязательных полей**

    * Вместо обязательных полей можно использовать "(optional)" для указания необязательных, что эффективно при их смешивании.
    * Однако Nielsen‑Norman отмечает, что "легче принимать решения, когда обязательные поля также четко обозначены" ([TPGi][4]).

---

## ✅ Краткое изложение руководств по UI

| Источник | Содержание |
| --- | --- |
| **NN/g: Marking Required Fields in Forms** | Рекомендуется комбинация звездочки и пояснительного текста; отображение только необязательных полей считается недружелюбным ([Nielsen Norman Group][1]). |
| **Deque (Anatomy of Accessible Forms)** | ・Использование строки "Required" или изображения внутри метки.<br>・Четко указано, что одной лишь цветовой индикации недостаточно. |
| **W3C Techniques (H90)** | Примеры включения звездочки или "(required)" в метку с определением значения в начале формы. |
| **TPGi (Doing what's required)** | С учетом доступности комбинация звездочки, атрибута ARIA и текстовой вставки в метку оценивается как оптимальная. |
| **Contensis Руководство по UX форм** | Кратко отмечено, что важна последовательная разметка (например, \* или (optional)) . |

---

## ✅ Рекомендуемый подход к реализации

* Добавьте пояснительный текст **в начале формы** :

  > Fields marked with \* are required.
  > (Или все вместе: "All fields are required", а если есть необязательные: "unless marked optional")

* **Добавление меток (Label)** :

    * Напишите, например, `First Name *` или `Email (required)`.

* **Атрибуты ARIA и HTML5** :

  ```html
  <label for="email">Email <abbr title="required">*</abbr></label>
  <input id="email" required aria-required="true">
  ```

* **Не полагайтесь только на цвет** : обеспечьте поддержку как визуально, так и программно.

---

## 🔗 Полезные ссылки (материалы руководств по UI)

* NN/g: *Marking Required Fields in Forms* ([California State University, Northridge][2], [Nielsen Norman Group][1], [Deque][3])
* Deque: *Anatomy of Accessible Forms* ([Deque][3])
* W3C Techniques: *H90 Indicating required form controls* ([W3C][5])
* TPGi: *Indicating mandatory fields accessibly* ([TPGi][4])
* Contensis: *UX Forms Guidelines* ([Contensis][6])

---

При необходимости мы также можем предоставить конкретные примеры кода HTML/CSS, шаблоны дизайна компонентов UI для Sketch или Figma и т. д. Пожалуйста, обращайтесь к нам!

[1]: https://www.nngroup.com/articles/required-fields/?utm_source=chatgpt.com "Marking Required Fields in Forms - NN/g"
[2]: https://www.csun.edu/universal-design-center/web-accessibility-criteria-required-fields?utm_source=chatgpt.com "Web Accessibility Criteria - Required Fields - CSUN"
[3]: https://www.deque.com/blog/anatomy-of-accessible-forms-required-form-fields/?utm_source=chatgpt.com "The Anatomy of Accessible Forms: Required Form Fields"
[4]: https://www.tpgi.com/doing-whats-required-indicating-mandatory-fields-in-an-accessible-way/?utm_source=chatgpt.com "Doing what's required: Indicating mandatory fields in an accessible ..."
[5]: https://www.w3.org/TR/WCAG20-TECHS/H90.html?utm_source=chatgpt.com "H90: Indicating required form controls using label or legend - W3C"
[6]: https://www.contensis.com/community/blog/ux-forms-guidelines?utm_source=chatgpt.com "Build better web forms: 15 UX guidelines that work - Contensis"
