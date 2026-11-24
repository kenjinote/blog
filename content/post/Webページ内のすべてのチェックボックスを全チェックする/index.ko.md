---
title: "웹 페이지의 체크박스를 한 번에 선택하거나 해제하기"
slug: "Webページ内のすべてのチェックボックスを全チェックする"
tags: ["javascript", "checkbox", "bookmarklet"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "JavaScript 또는 북마클릿으로 현재 페이지의 사용 가능한 체크박스를 선택하거나 해제합니다. 코드를 실행하기 전에 페이지 동작을 확인하세요."
date: "2022-10-05T20:07:06+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# 웹 페이지의 체크박스를 한 번에 선택하거나 해제하기

이 스크립트는 현재 페이지에서 사용할 수 있는 체크박스를 클릭하여 하나씩 조작하지 않고 함께 변경합니다.

## 실행 전 주의사항

신뢰할 수 있는 페이지에서만 실행하세요. 체크 동작에 페이지가 반응하여 설정을 바꾸거나 요청을 보낼 수 있습니다. 제출하거나 저장하기 전에 선택 결과를 확인하세요.

## DevTools에서 실행

대상 페이지를 열고 DevTools Console에서 아래 코드를 실행합니다. 브라우저에서 F12로 DevTools가 열리지 않으면 브라우저 메뉴를 이용하세요.

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (!box.checked) box.click();
}
```

사용 가능한 체크박스를 모두 해제하려면 다음 코드를 사용하세요.

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (box.checked) box.click();
}
```

## 북마클릿 만들기

새 북마크를 만들고 북마크 편집기에서 아래 한 줄 코드를 URL 칸에 붙여 넣습니다. 주소창에 입력하지 마세요. 대상 페이지에서 북마크를 선택하면 사용 가능한 체크박스가 선택됩니다.

**Select all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(!box.checked)box.click()})();
```

**Clear all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(box.checked)box.click()})();
```

선택을 해제하려면 두 번째 코드 또는 전체 해제 북마클릿을 사용하세요. 스크립트는 현재 문서만 대상으로 하며 비활성화된 체크박스는 건너뜁니다.

`.checked` 속성만 바꾸면 일반 클릭과 함께 발생하는 이벤트가 페이지 코드에 전달되지 않을 수 있습니다. `.click()`은 클릭 동작을 발생시킵니다. 페이지 자체 처리에 따라 일부 항목은 바뀌지 않을 수 있습니다.

## 참고 자료

- [MDN: HTMLElement.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click)
- [MDN: HTMLInputElement.checked](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/checked)
- [MDN: change event](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event)
