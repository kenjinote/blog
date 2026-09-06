---
title: '入力フォームの必須マークについて'
date: 2025-07-14T13:47:51+09:00
tags: ["入力フォーム", "Web開発", "UX"]
draft: false
image: "img.png"
categories: ["ブログ運営"]
---

海外の画面UI（フォーム）における「必須」マークについて、UIガイドライン資料とともに整理しました。

---

## 📌 主な必須マークとベストプラクティス

1. **アスタリスク (\*) の使用**

    * 一般的にもっとも普及しており、必須フィールドに「\*」を付けます。
    * ただし、\**フォーム冒頭に「* は必須項目です」などの説明が必須\*\*です ([Nielsen Norman Group][1], [カリフォルニア州立大学ノースリッジ][2])。
    * 色を使って強調する例もあります（赤文字など） 。

2. **ラベルに “Required” や “(required)” を明記**

    * ラベル内に文字で「Required」を付けることで、スクリーンリーダーにも明示でき、アクセシビリティが向上します ([Deque][3])。

3. **ARIA 属性や HTML5 の `required` 属性の併用**

    * 視覚的表示に加えて、`aria-required="true"` や `<input required>` を使って、プログラム的にも必須と伝えられます ([Deque][3])。

4. **“(optional)” を使って任意フィールドを明示**

    * 必須フィールドの代わりに任意フィールドを「(optional)」と明示する方法もあり、混在する場合に有効。
    * ただし、Nielsen‑Normanは「必須も明示したほうが判断しやすい」と指摘しています ([TPGi][4])。

---

## ✅ UIガイドライン資料まとめ

| 提供元                                        | 内容                                                                  |
| ------------------------------------------ | ------------------------------------------------------------------- |
| **NN/g: Marking Required Fields in Forms** | アスタリスク＋説明文の組み合わせが推奨され、任意のみの表示は不親切という評価 ([Nielsen Norman Group][1])。 |
| **Deque (Anatomy of Accessible Forms)**    | ・ラベル内に「Required」文字列または画像を併用。<br>・色だけでの示唆は不十分と明言 。                   |
| **W3C Techniques (H90)**                   | アスタリスクや「(required)」をラベルに含め、フォーム冒頭で意味を定義する例あり 。                      |
| **TPGi (Doing what's required)**           | アクセシビリティを考慮し、アスタリスク＋ARIA属性＋ラベル文字挿入が最適と評価 。                          |
| **Contensis フォームUXガイド**                    | 一貫したマーク付け（\* または (optional)）が重要と簡潔に整理 。                             |

---

## ✅ 実装上のおすすめアプローチ

* **フォーム冒頭** に説明文を追加：

  > Fields marked with \* are required.
  > （または一括で "All fields are required"、任意がある場合は "unless marked optional"）

* **ラベル付与**：

    * `First Name *` または `Email (required)`のように記述。

* **ARIA属性・HTML5属性**：

  ```html
  <label for="email">Email <abbr title="required">*</abbr></label>
  <input id="email" required aria-required="true">
  ```

* **色だけには頼らない**：視覚的とプログラム的に両対応を。

---

## 🔗 参考リンク（UIガイドライン資料）

* NN/g: *Marking Required Fields in Forms* ([カリフォルニア州立大学ノースリッジ][2], [Nielsen Norman Group][1], [Deque][3])
* Deque: *Anatomy of Accessible Forms* ([Deque][3])
* W3C Techniques: *H90 Indicating required form controls* ([W3C][5])
* TPGi: *Indicating mandatory fields accessibly* ([TPGi][4])
* Contensis: *UX Forms Guidelines* ([Contensis][6])

---

必要であれば、具体的なHTML／CSSのコード例や、Sketch・Figma用のUIコンポーネントデザインテンプレートなどもお伝えできます。お気軽にご相談ください！

[1]: https://www.nngroup.com/articles/required-fields/?utm_source=chatgpt.com "Marking Required Fields in Forms - NN/g"
[2]: https://www.csun.edu/universal-design-center/web-accessibility-criteria-required-fields?utm_source=chatgpt.com "Web Accessibility Criteria - Required Fields - CSUN"
[3]: https://www.deque.com/blog/anatomy-of-accessible-forms-required-form-fields/?utm_source=chatgpt.com "The Anatomy of Accessible Forms: Required Form Fields"
[4]: https://www.tpgi.com/doing-whats-required-indicating-mandatory-fields-in-an-accessible-way/?utm_source=chatgpt.com "Doing what's required: Indicating mandatory fields in an accessible ..."
[5]: https://www.w3.org/TR/WCAG20-TECHS/H90.html?utm_source=chatgpt.com "H90: Indicating required form controls using label or legend - W3C"
[6]: https://www.contensis.com/community/blog/ux-forms-guidelines?utm_source=chatgpt.com "Build better web forms: 15 UX guidelines that work - Contensis"
