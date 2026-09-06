---



title: "'Visual Studio Code에 Qt Extension Pack을 설치해 보았다'"
date: 2024-09-13T00:53:53+09:00
tags: ["Visual Studio Code", "Qt Extension Pack"]
draft: false
image: "img_1.png"
categories: ["도구・개발 환경"]
---




# VSCode에서 Qt 개발 시작하기: Qt Extension Pack 설치 방법

안녕하세요, Kenji입니다.
이번에는 "Visual Studio Code(이하 VSCode)에서 Qt 개발 환경을 구축하는 방법"에 대해 소개합니다.

최근에는 공식 Qt Creator 외에도 가볍고 확장성이 뛰어난 VSCode를 사용하여 Qt 앱을 개발하고 싶다는 목소리도 많아졌습니다.
그런 분들에게 추천하는 것이 "**Qt Extension Pack**"입니다.
이 확장 팩을 설치하는 것만으로 Qt와 관련된 주요 확장 기능들이 한 번에 갖춰집니다.

---

## 대상 독자

* Qt를 사용한 GUI 앱 개발을 시작하고 싶은 분
* Qt Creator가 아닌 VSCode에서 개발하고 싶은 분
* 확장 기능을 하나씩 찾는 것이 번거로운 분

---

## 전제 조건

* VSCode가 설치되어 있을 것
  ([공식 사이트에서 무료로 다운로드할 수 있습니다](https://code.visualstudio.com/))
* Qt 라이브러리 본체가 설치되어 있을 것([Qt 공식 사이트](https://www.qt.io/))

---

## Qt Extension Pack이란?

Qt Extension Pack은 VSCode용 확장 기능 팩입니다.
설치하면 다음과 같은 기능이 자동으로 추가됩니다:

* `.ui` 파일(Qt Designer) 지원
* `.pro` 파일 및 `.qrc` 파일 구문 강조
* Qt용 C++ 코드 완성, 빌드, 디버깅 지원
* Qt Resource Browser(리소스 참조)

---

## 설치 순서

### 1. VSCode 열기

먼저 VSCode를 실행합니다.

### 2. 확장 기능 뷰 열기

왼쪽의 액티비티 바(사각형 블록 아이콘)를 클릭하여 "확장 기능"을 표시합니다.

또는 단축키로
`Ctrl + Shift + X`를 눌러도 됩니다.

### 3. "Qt Extension Pack" 검색

검색 창에 다음 키워드를 입력합니다:

```
Qt Extension Pack
```

![img.png](img.png)

### 4. 설치 버튼 클릭

대상 팩이 표시되면 "설치" 버튼을 클릭합니다.
이것으로 다음과 같은 여러 확장 기능이 한 번에 설치됩니다:

* Qt Language Support
* QML Support
* Qt Designer Integration
* CMake Tools(CMake 기반 Qt 개발 시 필수)

---

## 프로젝트 설정 보충 (CMake + Qt의 예)

만약 Qt를 CMake 기반으로 사용하는 경우, 다음 확장 기능과의 조합을 추천합니다:

* [CMake Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)
* [CMake Language Support](https://marketplace.visualstudio.com/items?itemName=twxs.cmake)

또한 CMakeLists.txt에 다음과 같은 내용을 추가해 두면 Qt와의 연동이 원활합니다:

```cmake
find_package(Qt6 REQUIRED COMPONENTS Widgets)
target_link_libraries(MyApp PRIVATE Qt6::Widgets)
```

---

## 부록: .ui 파일은 어떻게 열까?

`.ui` 파일은 Qt Designer에서 편집할 수 있습니다.
VSCode 상에서 `.ui` 파일을 마우스 오른쪽 버튼으로 클릭 → `Open with Qt Designer`를 선택할 수 있게 됩니다(환경 변수 `PATH`에 Qt Designer가 포함되어 있어야 함).

---

## 요약

| 순서 | 내용                          |
| -- | --------------------------- |
| 1  | VSCode 실행                    |
| 2  | 확장 기능 패널 열기                  |
| 3  | "Qt Extension Pack" 검색 |
| 4  | 설치 버튼 클릭              |

VSCode에 Qt 환경을 구축하는 것이 이전보다 훨씬 간단해졌습니다.
Qt Creator의 대안으로도 충분한 기능이 있으며, 가볍게 작업하고 싶은 분들에게 추천합니다.

---

## 추천 링크 모음

* [Qt 공식](https://www.qt.io/)
* [Qt Extension Pack - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=TheQtCompany.qt)
* [VSCode 공식](https://code.visualstudio.com/)
* [CMake Tools 확장](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)

---

## 마무리하며

앞으로는 이 환경에서 Qt의 UI 도구나 QML을 활용한 개발도 진행해 볼 생각입니다.
다음에는 **Qt로 Hello World 앱을 VSCode에서 빌드하고 실행하는 방법**에 대해 해설할 예정입니다.

그럼 다음에 또 만나요!
