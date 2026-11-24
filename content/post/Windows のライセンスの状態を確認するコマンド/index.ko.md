---

title: 'Windows의 라이선스 인증 상태를 확인하는 방법! 명령 한 번으로 간단하게 체크'
slug: "Windows の라이선스の状態を確認する명령어"
date: "2025-04-14T00:41:45+09:00"
lastmod: "2026-11-25"
tags: ["Windows", "라이선스", "명령 프롬프트"]
draft: false
image: "img_1.webp"
categories: ["pc-gadgets"]
description: 'Windows 기본 slmgr 명령(/dli, /dlv, /xpr)으로 라이선스 채널과 정품 인증 상태를 확인하는 방법과 인증 상태가 라이선스 사용 권한을 증명하지 않는 이유를 설명합니다.'
---

# [Windows] 라이선스 상태를 확인하는 방법 (명령어 하나로 OK)

Windows 라이선스가 정상적으로 인증되어 있는지 궁금했던 적이 있으신가요?

그럴 때 유용한 것이 **명령어 한 번으로 라이선스 정보를 확인할 수 있는 방법** 입니다. 다음 단계를 실행하는 것만으로 현재 라이선스 상태를 쉽게 체크할 수 있습니다.

## 라이선스 상태를 확인하는 명령어

Windows에 기본 탑재된 스크립트 도구를 사용하여 라이선스 정보를 표시할 수 있습니다. 사용하는 명령어는 다음과 같습니다:

```
slmgr /dli
```

이 명령어를 실행하면 라이선스의 일부 정보가 창으로 표시됩니다.

## 실행 방법

1. 시작 메뉴에서 `cmd`를 검색해 명령 프롬프트를 엽니다. `/dli`, `/dlv`, `/xpr` 확인에는 관리자 권한이 필요하지 않습니다.

2. 명령 프롬프트에 다음을 입력하고 Enter 키를 누릅니다:

   ```
   slmgr /dli
   ```

3. 몇 초 기다리면 다음과 같은 라이선스 정보가 표시됩니다.

   ![Windows 라이선스 상태 창](img.webp)

## 표시되는 주요 정보

* 제품 키 일부
* 라이선스 채널(예: Retail, OEM)
* 라이선스 상태(표시 항목은 에디션과 채널에 따라 다름)

## 더 자세한 정보를 알고 싶다면?

다음과 같은 명령어도 있습니다:

* `slmgr /dlv` : 더 자세한 라이선스 정보를 표시
* `slmgr /xpr`: 정품 인증 만료일 표시

`/xpr`은 정품 인증 만료일을 표시하며 주로 KMS 클라이언트에 유용합니다. Retail 및 MAK 인증은 보통 영구적으로 표시됩니다. `slmgr`은 Windows 라이선스를 합법적으로 취득했는지 검증하지 않습니다. Windows 11에서는 설정 > 시스템 > 정품 인증에서도 상태를 확인할 수 있습니다.

## 요약

Windows 라이선스 상태는 명령어 하나로 쉽게 확인할 수 있습니다.

* **간단 확인** : `slmgr /dli`
* **자세한 확인** : `slmgr /dlv`
* **만료일 확인** : `slmgr /xpr`

예상과 다른 상태가 표시되면 Windows 정품 인증 설정을 확인하거나 판매처 또는 조직 관리자에게 문의하세요.

## 참고

- [Slmgr.vbs options for obtaining volume activation information](https://learn.microsoft.com/en-us/windows-server/get-started/activation-slmgr-vbs-options)
- [Activate Windows](https://support.microsoft.com/en-us/windows/activation/activate-windows)
