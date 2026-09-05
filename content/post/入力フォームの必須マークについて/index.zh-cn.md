---
title: '关于输入表单中的必填标记'
date: 2025-07-14T13:47:51+09:00
tags: ["输入表单", "Web开发", "UX"]
draft: false
image: "img.png"
categories: ["博客运营"]
---

我结合UI指南资料，整理了海外界面UI（表单）中关于“必填”标记的相关内容。

---

## 📌 主要必填标记及最佳实践

1. **使用星号 (\*)**

    * 一般最为普及，在必填字段上添加“\*”。
    * 但是，**必须在表单开头添加“* 为必填项”等说明** ([Nielsen Norman Group][1], [加州州立大学北岭分校][2])。
    * 也有使用颜色进行强调的例子（如红色文字）。

2. **在标签上明确标示 “Required” 或 “(required)”**

    * 通过在标签内添加“Required”文字，可以向屏幕阅读器明确提示，从而提高无障碍访问能力 ([Deque][3])。

3. **结合使用 ARIA 属性和 HTML5 的 `required` 属性**

    * 除了视觉上的显示，还可以使用 `aria-required="true"` 或 `<input required>`，在程序层面上告知其为必填项 ([Deque][3])。

4. **使用 “(optional)” 明示选填字段**

    * 也有不标必填字段，而是将选填字段明示为“(optional)”的方法，在两者混合出现时比较有效。
    * 不过，Nielsen‑Norman指出，“同时标明必填项更容易判断” ([TPGi][4])。

---

## ✅ UI指南资料汇总

| 来源                                        | 内容                                                                  |
| ------------------------------------------ | ------------------------------------------------------------------- |
| **NN/g: Marking Required Fields in Forms** | 推荐使用星号＋说明文的组合，认为仅标示选填项不够友好 ([Nielsen Norman Group][1])。 |
| **Deque (Anatomy of Accessible Forms)**    | ・在标签内并用“Required”字符串或图片。<br>・明确指出仅靠颜色提示是不够的。                   |
| **W3C Techniques (H90)**                   | 有在标签中包含星号或“(required)”，并在表单开头定义其含义的例子。                      |
| **TPGi (Doing what's required)**           | 考虑到无障碍访问，认为星号＋ARIA属性＋插入标签文字是最佳选择。                          |
| **Contensis 表单UX指南**                    | 简明扼要地指出，一致的标记（\* 或 (optional)）非常重要。                             |

---

## ✅ 开发实现建议方案

* **表单开头**添加说明文：

  > Fields marked with \* are required.
  > （或者统一写 "All fields are required"，有选填项时写 "unless marked optional"）

* **添加标签**：

    * 写成 `First Name *` 或 `Email (required)`。

* **ARIA属性・HTML5属性**：

  ```html
  <label for="email">Email <abbr title="required">*</abbr></label>
  <input id="email" required aria-required="true">
  ```

* **不要仅依赖颜色**：需要同时满足视觉和程序上的要求。

---

## 🔗 参考链接（UI指南资料）

* NN/g: *Marking Required Fields in Forms* ([加州州立大学北岭分校][2], [Nielsen Norman Group][1], [Deque][3])
* Deque: *Anatomy of Accessible Forms* ([Deque][3])
* W3C Techniques: *H90 Indicating required form controls* ([W3C][5])
* TPGi: *Indicating mandatory fields accessibly* ([TPGi][4])
* Contensis: *UX Forms Guidelines* ([Contensis][6])

---

如果有需要，我还可以提供具体的 HTML／CSS 代码示例，或者适用于 Sketch・Figma 的 UI 组件设计模板。随时欢迎咨询！

[1]: https://www.nngroup.com/articles/required-fields/?utm_source=chatgpt.com "Marking Required Fields in Forms - NN/g"
[2]: https://www.csun.edu/universal-design-center/web-accessibility-criteria-required-fields?utm_source=chatgpt.com "Web Accessibility Criteria - Required Fields - CSUN"
[3]: https://www.deque.com/blog/anatomy-of-accessible-forms-required-form-fields/?utm_source=chatgpt.com "The Anatomy of Accessible Forms: Required Form Fields"
[4]: https://www.tpgi.com/doing-whats-required-indicating-mandatory-fields-in-an-accessible-way/?utm_source=chatgpt.com "Doing what's required: Indicating mandatory fields in an accessible ..."
[5]: https://www.w3.org/TR/WCAG20-TECHS/H90.html?utm_source=chatgpt.com "H90: Indicating required form controls using label or legend - W3C"
[6]: https://www.contensis.com/community/blog/ux-forms-guidelines?utm_source=chatgpt.com "Build better web forms: 15 UX guidelines that work - Contensis"
