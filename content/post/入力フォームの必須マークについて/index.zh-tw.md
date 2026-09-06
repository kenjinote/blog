---
title: "關於輸入表單的必填標記"
slug: "入力フォームの必須マークについて"
date: 2025-07-14T13:47:51+09:00
tags: ["輸入表單", "網頁開發", "UX"]
draft: false
image: "img.png"
categories: ["部落格營運"]
---

我們整理了關於國外介面（表單）中「必填」標記的相關資訊，並附上 UI 設計指南。

---

## 📌 主要的必填標記與最佳實踐

1. **使用星號 (\*)**

    * 最常見且普及的方式，在必填欄位加上「\*」。
    * 然而， **在表單開頭必須加上「* 為必填項目」等說明** ([Nielsen Norman Group][1], [California State University, Northridge][2])。
    * 也有使用顏色來強調的例子（如紅字）。

2. **在標籤中明確標示 "Required" 或 "(required)"**

    * 在標籤內加入文字「Required」，可以讓螢幕閱讀器明確識別，提升無障礙體驗 ([Deque][3])。

3. **結合使用 ARIA 屬性與 HTML5 的 `required` 屬性**

    * 除了視覺顯示外，使用 `aria-required="true"` 或 `<input required>`，也能在程式層面傳達必填的資訊 ([Deque][3])。

4. **使用 "(optional)" 來明示選填欄位**

    * 也有不標示必填，而是將選填欄位標示為「(optional)」的方法，這在兩者混合的情況下很有效。
    * 不過，Nielsen‑Norman 指出「同時明示必填欄位會更容易判斷」 ([TPGi][4])。

---

## ✅ UI 設計指南資料總結

| 來源                                        | 內容                                                                  |
| ------------------------------------------ | ------------------------------------------------------------------- |
| **NN/g: Marking Required Fields in Forms** | 建議結合星號與說明文，僅標示選填欄位被認為是不夠友善的做法 ([Nielsen Norman Group][1])。 |
| **Deque (Anatomy of Accessible Forms)**    | ・在標籤內結合使用「Required」字串或圖片。<br>・明確表示僅用顏色提示是不夠的。                   |
| **W3C Techniques (H90)**                   | 有在標籤中包含星號或「(required)」，並在表單開頭定義其含義的範例。                      |
| **TPGi (Doing what's required)**           | 考量到無障礙體驗，結合星號＋ARIA 屬性＋標籤文字插入被評為最佳做法。                          |
| **Contensis 表單 UX 指南**                    | 簡潔地整理出：一致的標記（\* 或 (optional)）非常重要。                             |

---

## ✅ 實作上的建議方法

* 在 **表單開頭** 加入說明文：

  > Fields marked with \* are required.
  > （或統一使用 "All fields are required"，若有選填則加上 "unless marked optional"）

* **附加標籤** ：

    * 寫作 `First Name *` 或 `Email (required)`。

* **ARIA 屬性・HTML5 屬性** ：

  ```html
  <label for="email">Email <abbr title="required">*</abbr></label>
  <input id="email" required aria-required="true">
  ```

* **不要僅依賴顏色** ：視覺與程式層面都需對應。

---

## 🔗 參考連結（UI 設計指南資料）

* NN/g: *Marking Required Fields in Forms* ([California State University, Northridge][2], [Nielsen Norman Group][1], [Deque][3])
* Deque: *Anatomy of Accessible Forms* ([Deque][3])
* W3C Techniques: *H90 Indicating required form controls* ([W3C][5])
* TPGi: *Indicating mandatory fields accessibly* ([TPGi][4])
* Contensis: *UX Forms Guidelines* ([Contensis][6])

---

如果需要，我也可以提供具體的 HTML／CSS 程式碼範例，或是 Sketch・Figma 用的 UI 元件設計模板。歡迎隨時提出討論！

[1]: https://www.nngroup.com/articles/required-fields/?utm_source=chatgpt.com "Marking Required Fields in Forms - NN/g"
[2]: https://www.csun.edu/universal-design-center/web-accessibility-criteria-required-fields?utm_source=chatgpt.com "Web Accessibility Criteria - Required Fields - CSUN"
[3]: https://www.deque.com/blog/anatomy-of-accessible-forms-required-form-fields/?utm_source=chatgpt.com "The Anatomy of Accessible Forms: Required Form Fields"
[4]: https://www.tpgi.com/doing-whats-required-indicating-mandatory-fields-in-an-accessible-way/?utm_source=chatgpt.com "Doing what's required: Indicating mandatory fields in an accessible ..."
[5]: https://www.w3.org/TR/WCAG20-TECHS/H90.html?utm_source=chatgpt.com "H90: Indicating required form controls using label or legend - W3C"
[6]: https://www.contensis.com/community/blog/ux-forms-guidelines?utm_source=chatgpt.com "Build better web forms: 15 UX guidelines that work - Contensis"
