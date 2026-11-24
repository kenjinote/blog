---
date: 2023-04-07T21:06:32+09:00
lastmod: 2026-11-25




title: 'Windows 환경에서 OpenSSL을 빌드 및 설치하는 절차와 환경 구축 방법'
slug: "Windows で OpenSSL を빌드する方法"
tags: ["Windows", "OpenSSL", "빌드", "C++"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Windows에서 OpenSSL 소스를 빌드하는 방법을 OpenSSL 3.5.9 예제로 설명하고 필요한 도구와 x64 빌드 절차를 소개합니다."
---





# OpenSSL이란

애플리케이션에서 OpenSSL을 사용하려면 개발 헤더와 라이브러리가 필요합니다. 바이너리 배포본을 받거나 필요에 맞게 소스를 빌드할 수 있으며, 이 문서에서는 소스 빌드 방법을 설명합니다.

Below, we will introduce the build procedure.
# 빌드 환경 준비

- **Perl**

  [https://strawberryperl.com/](https://strawberryperl.com/)에서 `strawberry-perl-5.42.3.1-64bit.msi`를 다운로드합니다. 버전은 최신 버전이어도 무방합니다.

- **NASM**

  [https://www.nasm.us/](https://www.nasm.us/)의 `Download`에서 `3.02/nasm-3.02-win64.zip`을 다운로드합니다. 버전은 rc가 아닌 최신 버전이어도 무방합니다.
  설치 후에는 NASM이 설치된 폴더를 환경 변수 PATH에 등록해야 합니다.

- **Visual Studio 2022 ** 또는 ** Build Tools for Visual Studio 2022**

  [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/)에서 `Visual Studio 2022 Community` 또는 `Build Tools for Visual Studio 2022`를 설치합니다.
  
# Windows에서의 OpenSSL 빌드 절차

1. [https://openssl-library.org/source/](https://openssl-library.org/source/)에서 `openssl-3.5.9.tar.gz`를 다운로드하여 압축을 풉니다. 압축을 풀 수 없는 경우, 명령 프롬프트에서 `tar -xzf openssl-3.5.9.tar.gz`를 실행합니다.

2026-11-25 기준 OpenSSL 3.5.9는 지원 중인 LTS 계열인 3.5에 속하며, 지원은 2030-04-08까지입니다. 빌드 시 공식 다운로드 페이지에서 최신 지원 패치 버전을 확인하세요.

2. Visual Studio x64 개발자 명령 프롬프트를 사용하세요. Program Files에 설치할 때만 관리자 권한으로 여세요.
3. 압축을 푼 폴더를 엽니다.
4. 아래 명령을 실행합니다. ※`Community` 부분은 설치한 Visual Studio의 버전에 맞게 변경합니다.
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" amd64
```
5. 아래 명령을 실행합니다.
```
perl Configure VC-WIN64A
```
6. 아래 명령을 실행합니다. (시간이 꽤 걸립니다.)
```
nmake
```
7. 아래 명령을 실행합니다. (시간이 꽤 걸립니다.)
```
nmake test
```
8. 아래 명령을 실행합니다.
```
nmake install
```

성공한 경우 `C:\Program Files\OpenSSL`에 OpenSSL이 설치됩니다.
기본 설치 위치에 설치하려면 관리자 권한이 필요합니다. 권한 상승을 피하려면 구성할 때 쓰기 가능한 prefix를 지정하세요.

이상

# 참고 자료

- [OpenSSL supported releases and lifecycle](https://openssl-library.org/source/)
- [OpenSSL Windows build notes](https://github.com/openssl/openssl/blob/master/NOTES-WINDOWS.md)
- [OpenSSL build and install guide](https://github.com/openssl/openssl/blob/master/INSTALL.md)
- [Microsoft: x64 MSVC command prompt](https://learn.microsoft.com/en-us/cpp/build/how-to-enable-a-64-bit-visual-cpp-toolset-on-the-command-line?view=msvc-170)
- [NASM stable releases](https://www.nasm.us/)
- [Strawberry Perl for Windows](https://strawberryperl.com/)