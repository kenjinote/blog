---





title: "'【초보자용】vcpkg로 libcurl(OpenSSL 지원)을 Visual Studio에 도입하는 절차'"
date: 2025-07-07T21:46:08+09:00
tags: ["vcpkg", "curl", "Visual Studio", "C++"]
draft: false
image: "img.png"
categories: ["도구・개발 환경"]
---






## Visual Studio에서 libcurl(OpenSSL 지원)을 사용한다면, vcpkg 도입이 쉽고 추천합니다

C++에서 HTTP 통신을 다룰 때 자주 사용되는 것이 `libcurl`입니다. 하지만 빌드나 의존성 조정은 의외로 번거롭죠.

그럴 때 유용한 것이 Microsoft에서 만든 C++ 라이브러리 관리 도구인 '**vcpkg**'입니다.
이번에는 `vcpkg`를 사용하여 `libcurl`(OpenSSL 지원)을 도입하고, Visual Studio에서 원활하게 사용할 수 있도록 하는 절차를 소개합니다.

---

### vcpkg 설치 (미도입자만)

먼저 `vcpkg`를 설치합시다. 다음 절차를 PowerShell에서 실행해 주세요.

```powershell
git clone https://github.com/microsoft/vcpkg
cd vcpkg
.\bootstrap-vcpkg.bat
```

※Git이 아직 설치되어 있지 않은 경우, [Git 공식 사이트](https://git-scm.com/)에서 설치해 주세요.

---

### libcurl(OpenSSL 지원) 설치

이어서 vcpkg를 사용하여 `libcurl`을 설치합니다. OpenSSL을 지원하는 64bit 버전을 지정하려면 다음 명령을 실행합니다.

```powershell
vcpkg install curl[ssl] --triplet x64-windows
```

이 명령을 실행하면 필요한 의존성(OpenSSL 등)도 자동으로 설정됩니다.

---

### Visual Studio와의 연동 설정

vcpkg로 도입한 라이브러리를 Visual Studio 프로젝트에서 쉽게 사용할 수 있도록 하려면 다음 명령으로 통합 설정을 수행합니다.

```powershell
vcpkg integrate install
```

이 설정을 해두면 Visual Studio 프로젝트에서 자동으로 `#include <curl/curl.h>`를 사용할 수 있게 되며, 라이브러리 경로 및 링커 설정을 수동으로 할 필요가 없어집니다.

---

## 마치며

이것으로 Visual Studio에 `libcurl`(OpenSSL 지원)을 도입할 준비가 완료되었습니다.

* vcpkg를 사용하면 번거로운 의존성도 일괄적으로 관리할 수 있다
* `vcpkg install curl[ssl] --triplet x64-windows`로 libcurl을 쉽게 도입
* `vcpkg integrate install`로 Visual Studio와 자동 연동 가능

이제 프로젝트 내에서 헤더를 인클루드하고 libcurl의 API를 사용하여 개발을 시작해 봅시다.
편리한 vcpkg를 활용하여 개발 효율을 단번에 높여보세요.
