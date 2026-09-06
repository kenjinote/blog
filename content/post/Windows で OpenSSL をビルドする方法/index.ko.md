---




title: "'Windows에서 OpenSSL 빌드하는 방법'"
slug: "Windows で OpenSSL をビルドする方法"
date: 2023-04-07T21:06:32+09:00
tags: ["Windows", "OpenSSL", "빌드", "C++"]
draft: false
image: "img.png"
categories: ["프로그래밍"]
---





# OpenSSL이란

암호화 통신을 수행하는 데 필요한 처리를 제공하는 오픈 소스 라이브러리입니다.

프로그램에서 사용하려면 C언어 소스 코드가 공개되어 있으므로, 빌드하여 라이브러리를 생성해야 합니다.

아래에서는 빌드 절차를 소개합니다.

# 빌드 환경 준비

- **Perl**

  [https://strawberryperl.com/](https://strawberryperl.com/)에서 `strawberry-perl-5.32.1.1-64bit.msi`를 다운로드합니다. 버전은 최신 버전이어도 무방합니다.

- **NASM**

  [https://www.nasm.us/](https://www.nasm.us/)의 `Download`에서 `2.16.01/nasm-2.16.01-win64.zip`을 다운로드합니다. 버전은 rc가 아닌 최신 버전이어도 무방합니다.
  설치 후에는 NASM이 설치된 폴더를 환경 변수 PATH에 등록해야 합니다.

- **Visual Studio 2022 ** 또는 ** Build Tools for Visual Studio 2022**

  [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/)에서 `Visual Studio 2022 Community` 또는 `Build Tools for Visual Studio 2022`를 설치합니다.
  
# Windows에서의 OpenSSL 빌드 절차

1. [https://www.openssl.org/source/](https://www.openssl.org/source/)에서 `openssl-3.1.0.tar.gz`를 다운로드하여 압축을 풉니다. 압축을 풀 수 없는 경우, 명령 프롬프트에서 `tar -xzf openssl-3.1.0.tar.gz`를 실행합니다.
2. **관리자 권한으로** 명령 프롬프트를 실행합니다.
3. 압축을 푼 폴더를 엽니다.
4. 아래 명령을 실행합니다. ※`Community` 부분은 설치한 Visual Studio의 버전에 맞게 변경합니다.
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
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

이상

# 참고
[https://ja.wikipedia.org/wiki/OpenSSL](https://ja.wikipedia.org/wiki/OpenSSL)
