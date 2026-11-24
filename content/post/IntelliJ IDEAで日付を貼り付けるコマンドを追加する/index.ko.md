---
title: 'IntelliJ IDEA에서 현재 날짜를 삽입하는 바로 가기 생성 방법'
slug: "IntelliJ IDEAで날짜を貼り付ける명령어を追加する"
date: 2022-09-04T05:59:04+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA"]
draft: false
image: "images/IntelliJ_logo.webp"
categories: ["it-technology"]
description: 'IntelliJ IDEA Live Template으로 로컬 시간대 오프셋을 포함한 ISO 8601 타임스탬프를 삽입하는 방법을 설명합니다. 설정 경로, 날짜 표현식, 확장 키는 JetBrains의 최신 문서를 따릅니다.'
---

# 소개

글을 쓰면서 타임스탬프를 자주 입력한다면 IntelliJ IDEA Live Template에 등록해 짧은 약어로 삽입할 수 있습니다. 이 예제는 컴퓨터의 로컬 시간과 시간대 오프셋이 포함된 ISO 8601 타임스탬프를 만듭니다.

## Live Template 만들기

1. **Settings > Editor > Live Templates**를 엽니다. Windows/Linux에서는 **File > Settings**, macOS에서는 **IntelliJ IDEA > Settings**에서 엽니다.
2. 템플릿 그룹(예: **other**)을 선택하고 **+ > Live Template**을 클릭합니다.
3. **Abbreviation**에 `date`를 입력하고 짧은 **Description**을 작성합니다.
4. **Template text**에 `$date$`를 입력합니다.
5. **Edit Variables**를 클릭합니다. `date` 변수의 **Expression**에 `date("yyyy-MM-dd'T'HH:mm:ssXXX")`를 입력합니다. 템플릿을 확장할 때 값을 자동 계산하도록 **Skip if defined**를 선택합니다.
6. **Define**을 클릭하고 템플릿을 사용할 컨텍스트를 선택합니다(필요하면 **Everywhere**). 설정을 저장합니다.

## 템플릿 사용하기

편집기에서 `date`를 입력하고 기본 확장 키인 **Tab**을 누릅니다. IntelliJ IDEA가 `2026-11-24T09:30:00+09:00`와 같은 형식으로 현재 시스템 날짜와 시간을 삽입합니다. 시간과 오프셋은 컴퓨터의 현재 시간대를 따릅니다. 확장 키를 변경했다면 Live Templates 설정에서 확인하세요.

`XXX` 패턴은 ISO 8601 시간대 오프셋을 출력합니다. `+09:00`을 고정하지 않으므로 각 독자의 로컬 시간대를 사용합니다. 생성된 타임스탬프가 의도한 게시 시각과 맞는지 확인하세요.

## 참고 자료

- [Live Template 만들기 및 편집](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [Live Template 변수와 date 함수](https://www.jetbrains.com/help/idea/template-variables.html)
- [Live Template 확장 키 설정](https://www.jetbrains.com/help/idea/settings-live-templates.html)
