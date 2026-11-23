---
title: 'Ranklet4로 GA4 인기 페이지 순위를 Hugo에 표시하기'
date: 2023-04-10T20:26:57+09:00
lastmod: 2026-11-23







slug: "Google 애널리틱스から人気ページランキングを取得して配置する方法"
tags: ["Google 애널리틱스", "Ranklet", "HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: '서비스가 종료된 기존 Ranklet 위젯의 GA4 후속 서비스인 Ranklet4로 Hugo에 인기 페이지 순위를 표시하는 방법을 소개합니다. 마이그레이션, 권한, 템플릿, 외부 서비스 이용 시 확인할 점을 다룹니다.'
---

# Ranklet4로 GA4 인기 페이지 순위를 Hugo에 표시하기

기존 안내는 Google Analytics 보기(View)와 이전 Ranklet 위젯을 사용했습니다. 이전 Ranklet 서비스는 2023년에 종료되었습니다. 기존 태그를 GA4용 별도 서비스인 Ranklet4에서 새로 발급한 태그로 교체하세요. [공식 이전 안내](https://docs.ranklet4.com/changes.html)를 참고하세요.

Ranklet4는 GA4 보고서 데이터를 집계해 Hugo 같은 정적 사이트에도 JavaScript 위젯으로 순위를 제공합니다. 메뉴와 요금제는 바뀔 수 있으므로 [현재 공식 튜토리얼](https://docs.ranklet4.com/tutorial.html)을 기준으로 진행하세요.

## 시작하기 전에

* 사이트 방문이 기록되는 GA4 속성이 있어야 합니다.
* 로그인에 사용할 Google 계정은 해당 속성에서 최소 **뷰어** 권한이 필요합니다. 관리자 권한 계정을 사용할 필요는 없습니다.
* Ranklet4가 Google Analytics 데이터에 접근하게 됩니다. 이용약관은 분석 데이터를 사용·복제·배포하고 파생물을 만들거나 표시·실행할 수 있는 폭넓은 라이선스를 부여하며, 개인을 식별할 수 없는 통계 정보의 사용·공개도 허용합니다. 연결 전에 [이용약관](https://docs.ranklet4.com/agreement.html)과 [개인정보처리방침](https://ranklet4.com/docs/privacy)을 읽고 데이터를 공유할 권리가 있는지 확인하세요.

## 순위 생성 및 게시

1. 대상 GA4 속성을 조회할 수 있는 계정으로 [Ranklet4](https://ranklet4.com/)에 로그인합니다. 권한을 허용하기 전에 요청 내용을 확인하세요.
2. 새 순위를 만들고 GA4 속성, 집계 기간, 표시 개수를 선택합니다. 필요하다면 제목이나 URL 필터로 홈을 제외합니다.
3. 필요에 따라 제목 문자열 치환을 설정하고 미리 보기에서 결과를 확인합니다.
4. 디자인 갤러리에서 템플릿을 고르거나 HTML/CSS를 수정합니다. 새 템플릿은 Handlebars를 사용하며 필드명과 문법은 [템플릿 가이드](https://docs.ranklet4.com/template.html)를 확인하세요.
5. 저장 및 게시한 뒤 관리 화면에서 생성된 태그를 복사합니다. 이전 Ranklet의 태그나 ID를 재사용하지 마세요.

최소 HTML 템플릿 예시입니다. 지원 필드와 반복 문법은 공식 가이드를 확인하세요.

```handlebars
<ol class="popular-pages">
  {{#each rankings}}
  <li><a href="{{url}}">{{title}}</a></li>
  {{/each}}
</ol>
```

## Hugo에 추가하기

1. `layouts/partials/ranklet4.html`을 만들고 Ranklet4가 생성한 순위 태그를 그대로 붙여 넣습니다.
2. 순위를 표시할 레이아웃(예: `layouts/_default/single.html` 또는 사이드바 partial)에 다음 Hugo 코드를 추가합니다.

```go-html-template
{{- partial "ranklet4.html" . }}
```

3. 로컬에서 페이지를 미리 보고, 배포 후 위젯이 HTTPS로 로드되는지 확인합니다. 외부 JavaScript에 의존하므로 페이지 속도, 개인정보 안내, 사이트 보안 정책을 고려하세요.

## 업데이트와 이전 참고

순위는 GA4 보고서와 Ranklet4의 갱신 일정에 따라 달라지므로 방문 직후 바로 바뀌지 않을 수 있습니다. 갱신 횟수, 요금제 기능, 크레딧, 광고 정책은 변경될 수 있으니 [현재 요금제](https://docs.ranklet4.com/plan.html)를 확인하세요. Ranklet4 크롤러는 공개 페이지 정보를 읽습니다. 자세한 내용은 [FAQ](https://docs.ranklet4.com/faq.html)를 참고하세요.

## 공식 자료

* [Ranklet4 공식 튜토리얼](https://docs.ranklet4.com/tutorial.html)
* [기존 Ranklet과의 변경 사항](https://docs.ranklet4.com/changes.html)
* [Ranklet4 템플릿 가이드](https://docs.ranklet4.com/template.html)
* [Ranklet4 FAQ](https://docs.ranklet4.com/faq.html)
* [Ranklet4 이용약관](https://docs.ranklet4.com/agreement.html)
* [Ranklet4 개인정보처리방침](https://ranklet4.com/docs/privacy)
