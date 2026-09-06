---




title: "'입력 폼의 필수 마크에 대하여'"
date: 2025-07-14T13:47:51+09:00
tags: ["입력 폼", "Web 개발", "UX"]
draft: false
image: "img.png"
categories: ["블로그 운영"]
---





해외의 화면 UI(폼)에서의 「필수」 마크에 대해, UI 가이드라인 자료와 함께 정리했습니다.

---

## 📌 주요 필수 마크와 베스트 프랙티스

1. **애스터리스크 (\*) 사용**

    * 일반적으로 가장 널리 보급되어 있으며, 필수 필드에 「\*」를 붙입니다.
    * 단, \**폼 앞부분에 「* 는 필수 항목입니다」 등의 설명이 필수\*\*입니다 ([Nielsen Norman Group][1], [캘리포니아 주립 대학교 노스리지][2]).
    * 색상을 사용하여 강조하는 예도 있습니다(빨간 글씨 등).

2. **레이블에 “Required” 나 “(required)” 명시**

    * 레이블 내에 문자로 「Required」를 붙임으로써 스크린 리더에도 명시할 수 있어, 접근성이 향상됩니다 ([Deque][3]).

3. **ARIA 속성이나 HTML5의 `required` 속성 병용**

    * 시각적 표시와 더불어, `aria-required="true"`나 `<input required>`를 사용하여 프로그래밍적으로도 필수임을 전달할 수 있습니다 ([Deque][3]).

4. **“(optional)”을 사용하여 선택 필드 명시**

    * 필수 필드 대신 선택 필드를 「(optional)」로 명시하는 방법도 있으며, 혼재하는 경우에 유효합니다.
    * 단, Nielsen-Norman은 「필수도 명시하는 편이 판단하기 쉽다」고 지적하고 있습니다 ([TPGi][4]).

---

## ✅ UI 가이드라인 자료 요약

| 제공처                                        | 내용                                                                  |
| ------------------------------------------ | ------------------------------------------------------------------- |
| **NN/g: Marking Required Fields in Forms** | 애스터리스크 + 설명문 조합이 권장되며, 선택 사항만 표시하는 것은 불친절하다는 평가 ([Nielsen Norman Group][1]). |
| **Deque (Anatomy of Accessible Forms)**    | ・레이블 내에 「Required」 문자열 또는 이미지를 병용.<br>・색상만으로 나타내는 것은 불충분하다고 명언.                   |
| **W3C Techniques (H90)**                   | 애스터리스크나 「(required)」를 레이블에 포함시키고, 폼 앞부분에 의미를 정의하는 예가 있음.                      |
| **TPGi (Doing what's required)**           | 접근성을 고려하여 애스터리스크 + ARIA 속성 + 레이블 문자 삽입이 최적이라고 평가.                          |
| **Contensis 폼 UX 가이드**                    | 일관된 마크 지정(\* 또는 (optional))이 중요하다고 간결하게 정리.                             |

---

## ✅ 구현 시 추천 어프로치

* **폼 앞부분**에 설명문 추가：

  > Fields marked with \* are required.
  > (또는 일괄적으로 "All fields are required", 선택 항목이 있는 경우는 "unless marked optional")

* **레이블 부여**：

    * `First Name *` 또는 `Email (required)`와 같이 기술.

* **ARIA 속성・HTML5 속성**：

  ```html
  <label for="email">Email <abbr title="required">*</abbr></label>
  <input id="email" required aria-required="true">
  ```

* **색상에만 의존하지 않기**：시각적 및 프로그래밍적 양쪽 모두에 대응.

---

## 🔗 참고 링크 (UI 가이드라인 자료)

* NN/g: *Marking Required Fields in Forms* ([캘리포니아 주립 대학교 노스리지][2], [Nielsen Norman Group][1], [Deque][3])
* Deque: *Anatomy of Accessible Forms* ([Deque][3])
* W3C Techniques: *H90 Indicating required form controls* ([W3C][5])
* TPGi: *Indicating mandatory fields accessibly* ([TPGi][4])
* Contensis: *UX Forms Guidelines* ([Contensis][6])

---

필요하시다면, 구체적인 HTML/CSS 코드 예시나 Sketch/Figma용 UI 컴포넌트 디자인 템플릿 등도 전달해 드릴 수 있습니다. 부담 없이 상담해 주세요!

[1]: https://www.nngroup.com/articles/required-fields/?utm_source=chatgpt.com "Marking Required Fields in Forms - NN/g"
[2]: https://www.csun.edu/universal-design-center/web-accessibility-criteria-required-fields?utm_source=chatgpt.com "Web Accessibility Criteria - Required Fields - CSUN"
[3]: https://www.deque.com/blog/anatomy-of-accessible-forms-required-form-fields/?utm_source=chatgpt.com "The Anatomy of Accessible Forms: Required Form Fields"
[4]: https://www.tpgi.com/doing-whats-required-indicating-mandatory-fields-in-an-accessible-way/?utm_source=chatgpt.com "Doing what's required: Indicating mandatory fields in an accessible ..."
[5]: https://www.w3.org/TR/WCAG20-TECHS/H90.html?utm_source=chatgpt.com "H90: Indicating required form controls using label or legend - W3C"
[6]: https://www.contensis.com/community/blog/ux-forms-guidelines?utm_source=chatgpt.com "Build better web forms: 15 UX guidelines that work - Contensis"
