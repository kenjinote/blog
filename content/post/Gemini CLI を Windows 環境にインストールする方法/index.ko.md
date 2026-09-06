---




title: "'Gemini CLI를 Windows 환경에 설치하는 방법'"
date: 2025-07-13T23:49:56+09:00
tags: ["Gemini", "CLI", "Windows", "설치", "개발"]
draft: false
image: "img.png"
categories: ["PC・가젯"]
---





# 【초보자용】 Windows에 Gemini CLI를 설치하는 방법

Google의 생성형 AI 'Gemini'를 커맨드라인에서 사용할 수 있게 해주는 'Gemini CLI'.
이 글에서는 Windows 환경에 Gemini CLI를 설치하는 과정을 최대한 알기 쉽게 설명합니다.

---

## 1. 사전 준비: Node.js 및 npm 설치

먼저, Gemini CLI는 'Node.js'라는 환경에서 작동하므로 다음 항목들을 설치해야 합니다.

* **Node.js**
* **npm (Node.js에 포함된 패키지 관리 도구)**
* **npx (npm에 포함된 명령어 실행 도구)**

아래의 공식 웹사이트에서 Windows용 Node.js를 다운로드하세요 (LTS 버전을 권장합니다):

👉 [Node.js 공식 웹사이트](https://nodejs.org/)

설치가 완료되면 다음 명령어로 제대로 설치되었는지 확인해 봅시다.

```powershell
node -v
npm -v
```

---

## 2. PowerShell 실행하기

Windows에서 Gemini CLI를 사용하려면 PowerShell을 이용해 조작하는 것이 일반적입니다.
시작 메뉴에서 'PowerShell'을 입력하여 실행하세요.

---

## 3. Gemini CLI 설치하기

아래 명령어를 PowerShell에 복사하여 붙여넣고 실행합니다:

```bash
npx @google/gemini-cli
```

이 명령어는 Google이 공개한 Gemini CLI 패키지를 임시로 실행하기 위한 것입니다.
필요에 따라 초기 설정이나 로그인이 요구될 수도 있습니다.

※ 처음에는 몇 분 정도 걸릴 수 있습니다. 오류가 발생할 경우 Node.js나 네트워크 환경을 다시 확인해 보세요.

---

## 4. 설치 완료! 다음으로 할 일

이것으로 Windows에 Gemini CLI가 설치되었습니다.
앞으로는 커맨드라인에서 Gemini를 사용하여 텍스트 생성이나 코드 완성 등 다양한 작업이 가능해집니다.

공식 문서나 도움말을 확인하고 싶다면 아래와 같은 명령어도 활용할 수 있습니다.

```bash
npx @google/gemini-cli --help
```

---

## 마무리

Windows에 Gemini CLI를 도입하는 과정을 복습해 보겠습니다.

1. Node.js 및 npm 설치
2. PowerShell 실행
3. `npx @google/gemini-cli` 실행

이것으로 준비 완료입니다!
생성형 AI를 로컬에서 사용하고 싶은 분은 이 과정을 참고하여 도전해 보세요.
