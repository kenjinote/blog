---





title: "'msix에 자체 서명 인증서를 추가하여 설치할 수 있게 만들기'"
date: 2025-08-30T04:18:04+09:00
tags: ["msix", "자체 서명 인증서", "설치"]
draft: false
image: "img.png"
categories: ["IT・테크놀로지"]
---






# msix에 자체 서명 인증서를 추가하여 설치할 수 있게 만들기

Windows에서 앱을 배포할 때, **MSIX 패키지**를 이용하면 설치나 업데이트 구조가 통일되어 편리합니다. 하지만 MSIX에는 '반드시 서명된 인증서'가 필요하다는 제약이 있습니다.
기업이나 개인이 개발한 앱을 테스트 배포하고 싶을 때, "상용 코드 서명 인증서를 구매하는 것은 너무 과하다"고 생각되는 상황도 있을 것입니다.

이럴 때 유용한 것이 **자체 서명 인증서(Self-Signed Certificate)**입니다. 이 글에서는 MSIX에 자체 서명 인증서를 추가하여 로컬 환경에서 설치할 수 있도록 하는 절차를 정리합니다.

---

## 1. 자체 서명 인증서 생성하기

먼저 PowerShell을 관리자 모드로 실행하고, 아래의 명령어를 실행합니다.

```powershell
// 자체 서명 인증서 생성
New-SelfSignedCertificate -Type CodeSigningCert -Subject "CN=035A9AAC-915B-4CE1-AE39-1A101BED42F5" -CertStoreLocation Cert:\CurrentUser\My -NotAfter (Get-Date).AddYears(10) -KeyUsage DigitalSignature -FriendlyName "kenjinote"
```

여기서 생성되는 것은 '코드 서명용' 인증서입니다.

* `-FriendlyName`으로 알기 쉬운 이름을 지정해 두면 나중에 찾기 쉽습니다.
* `-NotAfter`로 유효기간을 조정할 수 있습니다. 이번에는 10년으로 설정했습니다.

---

## 2. PFX 파일 내보내기

생성한 인증서를 PFX 형식으로 내보내어 `signtool`에서 이용할 수 있게 합니다.

```powershell
// pfx 생성
$cert = Get-ChildItem Cert:\CurrentUser\My | Where-Object { $_.FriendlyName -eq "kenjinote" }
$password = ConvertTo-SecureString -String "password" -Force -AsPlainText
Export-PfxCertificate -Cert $cert -FilePath "D:\pfx\cert.pfx" -Password $password
```

이때 설정한 비밀번호(예시에서는 `password`)는 나중에 서명 작업 시 필요합니다.

---

## 3. 자체 서명 인증서를 신뢰할 수 있는 루트 인증 기관에 설치하기

생성한 인증서는 그대로는 Windows에서 신뢰하지 않습니다. 설치하려면 `certmgr.msc`에서 **[신뢰할 수 있는 루트 인증 기관] → [인증서]**로 가져와야 합니다.

내보낸 인증서(`.cer`나 `.pfx`)를 가져오면, 대상 PC 상에서는 신뢰할 수 있는 인증서로 취급됩니다.
이를 통해 MSIX에 서명해도 '신뢰할 수 없는 인증서'라는 경고가 나타나지 않게 됩니다.

---

## 4. 인스톨러(MSIX)에 서명 추가하기

마지막으로, 생성한 PFX 인증서를 사용하여 MSIX에 서명합니다. `signtool`은 Visual Studio나 Windows SDK에 포함되어 있습니다.

```powershell
// 인스톨러에 서명 추가하기
signtool sign /fd SHA256 /f "D:\pfx\cert.pfx" /p "password" "C:\installer\installer.msix"
```

* `/fd SHA256`은 서명 알고리즘을 지정합니다.
* `/f`로 PFX 파일을 지정하고, `/p`로 비밀번호를 전달합니다.
* 마지막으로 MSIX 파일의 경로를 지정해 주세요.
* signtool의 경로가 설정되어 있지 않은 경우에는 전체 경로로 지정해 주세요. 제 환경에서는 아래 위치에 있었습니다.

```
"C:\Program Files (x86)\Microsoft Visual Studio\Shared\NuGetPackages\microsoft.windows.sdk.buildtools\10.0.26100.1742\bin\10.0.26100.0\x64\signtool.exe"
```

이로써 서명이 완료되고, 대상 PC에서 설치 가능한 MSIX가 완성됩니다.

---

## 요약

* **New-SelfSignedCertificate**로 자체 서명 인증서를 생성한다
* **Export-PfxCertificate**로 PFX를 내보낸다
* **신뢰할 수 있는 루트 인증 기관**에 인증서를 설치한다
* **signtool**로 MSIX에 서명한다

이 흐름을 파악해두면, 상용 인증서를 구매하지 않고도 로컬 환경에서 동작 확인이나 테스트 배포가 가능해집니다.
물론 실제 상용 배포에서는 인증 기관에서 발급한 인증서가 필수적이지만, 개발 및 검증 단계에서는 이 방법이 매우 유용합니다.

---

👉 이번에는 installer.msix를 예로 들었지만, 같은 절차를 자작 앱에도 적용할 수 있습니다.

---
