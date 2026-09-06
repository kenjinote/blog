---

title: "Web페이지 내의 모든 체크박스를 전체 체크하기"
date: 2022-10-05T20:07:06+09:00
tags: ["javascript", "자동화"]
draft: false
image: "img.png"
categories: ["블로그 운영"]
---


Web페이지 내의 체크박스를 전체 체크하려면, F12로 DevTools를 열고, 콘솔에 다음 코드를 붙여넣어 실행합니다.
```js
let boxes = document.querySelectorAll('input[type="checkbox"]');
for (let i = 0; i < boxes.length; i++) {
    if (!boxes[i].disabled) {
        boxes[i].checked = true;
    }
}
```

또는,

새로 북마크를 생성하고, 등록할 주소(보통 https://...라고 입력하는 부분)에 다음 코드를 붙여넣어 등록합니다.
체크하고 싶은 Web페이지를 표시하고, 생성한 북마크를 클릭하면 모든 체크박스가 체크됩니다.
```
javascript:(function(){let boxes=document.querySelectorAll('input[type="checkbox"]');for(let i=0;i<boxes.length;i++){if(!boxes[i].disabled){boxes[i].checked=true;}}})();
```

전체 해제할 경우에는, 위 스크립트의 `boxes[i].checked = true;` 부분을 `boxes[i].checked = false;`로 변경해 주세요.
