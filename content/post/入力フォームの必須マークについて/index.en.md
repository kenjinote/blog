---
title: 'About Required Marks in Input Forms'
slug: "入力フォームの必須マークについて"
date: 2025-07-14T13:47:51+09:00
tags: ["Input Form", "Web Development", "UX"]
draft: false
image: "img.png"
categories: ["Blog Management"]
---

I have summarized information about the "required" mark in overseas screen UI (forms), along with UI guideline materials.

---

## 📌 Main Required Marks and Best Practices

1. **Using an Asterisk (\*)**

    * This is generally the most widespread method, adding "\*" to required fields.
    * However, **an explanation such as "\* indicates a required field" at the beginning of the form is essential** ([Nielsen Norman Group][1], [California State University, Northridge][2]).
    * There are also examples that use color for emphasis (such as red text).

2. **Clearly Stating "Required" or "(required)" in the Label**

    * By explicitly adding "Required" in text within the label, it can be clearly communicated to screen readers, improving accessibility ([Deque][3]).

3. **Using ARIA Attributes or HTML5 `required` Attribute in Conjunction**

    * In addition to visual indication, using `aria-required="true"` or `<input required>` allows you to programmatically communicate that a field is required ([Deque][3]).

4. **Clearly Stating Optional Fields Using "(optional)"**

    * There is also a method of explicitly indicating optional fields as "(optional)" instead of required fields, which is effective when both are mixed.
    * However, Nielsen-Norman points out that "it is easier to judge if required fields are also explicitly indicated" ([TPGi][4]).

---

## ✅ Summary of UI Guideline Materials

| Source | Content |
| --- | --- |
| **NN/g: Marking Required Fields in Forms** | A combination of an asterisk + explanatory text is recommended, and showing only optional fields is evaluated as unfriendly ([Nielsen Norman Group][1]). |
| **Deque (Anatomy of Accessible Forms)** | - Use the string "Required" or an image within the label.<br>- Explicitly states that suggesting by color alone is insufficient. |
| **W3C Techniques (H90)** | There are examples of including an asterisk or "(required)" in the label and defining the meaning at the beginning of the form. |
| **TPGi (Doing what's required)** | Considering accessibility, evaluated that an asterisk + ARIA attribute + inserting label text is optimal. |
| **Contensis UX Forms Guidelines** | Briefly summarizes that consistent marking (\* or (optional)) is important. |

---

## ✅ Recommended Implementation Approach

* **Add an explanatory text at the beginning of the form**:

  > Fields marked with \* are required.
  > (Or collectively "All fields are required", and if there are optional fields, "unless marked optional")

* **Applying Labels**:

    * Write it like `First Name *` or `Email (required)`.

* **ARIA Attributes / HTML5 Attributes**:

  ```html
  <label for="email">Email <abbr title="required">*</abbr></label>
  <input id="email" required aria-required="true">
  ```

* **Do not rely on color alone**: Support both visual and programmatic indications.

---

## 🔗 Reference Links (UI Guideline Materials)

* NN/g: *Marking Required Fields in Forms* ([California State University, Northridge][2], [Nielsen Norman Group][1], [Deque][3])
* Deque: *Anatomy of Accessible Forms* ([Deque][3])
* W3C Techniques: *H90 Indicating required form controls* ([W3C][5])
* TPGi: *Indicating mandatory fields accessibly* ([TPGi][4])
* Contensis: *UX Forms Guidelines* ([Contensis][6])

---

If necessary, I can also provide specific HTML/CSS code examples, UI component design templates for Sketch/Figma, etc. Please feel free to consult with me!

[1]: https://www.nngroup.com/articles/required-fields/?utm_source=chatgpt.com "Marking Required Fields in Forms - NN/g"
[2]: https://www.csun.edu/universal-design-center/web-accessibility-criteria-required-fields?utm_source=chatgpt.com "Web Accessibility Criteria - Required Fields - CSUN"
[3]: https://www.deque.com/blog/anatomy-of-accessible-forms-required-form-fields/?utm_source=chatgpt.com "The Anatomy of Accessible Forms: Required Form Fields"
[4]: https://www.tpgi.com/doing-whats-required-indicating-mandatory-fields-in-an-accessible-way/?utm_source=chatgpt.com "Doing what's required: Indicating mandatory fields in an accessible ..."
[5]: https://www.w3.org/TR/WCAG20-TECHS/H90.html?utm_source=chatgpt.com "H90: Indicating required form controls using label or legend - W3C"
[6]: https://www.contensis.com/community/blog/ux-forms-guidelines?utm_source=chatgpt.com "Build better web forms: 15 UX guidelines that work - Contensis"
