---
title: 'TinyLLaMA를 C++에서 실행! llama.cpp를 사용한 로컬 LLM 환경 구축 절차'
date: "2025-07-19T09:40:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "TinyLLaMA を C++ から呼び出せるようにする手順（llama.cpp使用）"
tags: ["C++", "llama.cpp", "TinyLLaMA", "AI"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'TinyLLaMA를 C++에서 호출하여 실행하기 위한 설정 절차를 설명합니다. llama.cpp 빌드부터 HuggingFace에서의 모델 가져오기, 다양한 환경에서의 구축 방법까지 초보자도 알기 쉽게 정리했습니다.'
---

2026년 11월 24일에 개정했습니다. 2025년 7월 버전의 변환 명령과 C++ 코드는 현재 llama.cpp에서 그대로 동작하지 않아 현재 GGUF 모델과 공식 C++ 예제로 바꿨습니다.

## 1. 설치

llama.cpp는 추론 라이브러리와 명령줄 도구를 제공합니다. Windows에서는 WinGet, macOS/Linux에서는 공식 설치 프로그램을 사용하세요.

```powershell
winget install llama.cpp
```

macOS/Linux 공식 설치 프로그램:

```sh
curl -LsSf https://llama.app/install.sh | sh
```

## 2. 모델 실행

TinyLLaMA 원본 가중치는 Hugging Face 형식입니다. 여기서는 llama.cpp용으로 제3자가 변환한 Q4_K_M GGUF를 사용하므로 직접 변환할 필요가 없습니다. 최초 실행 시 약 669 MB를 다운로드합니다.

```sh
llama cli -hf TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

## 3. C++ 예제 빌드

C++ 앱에 통합하려면 공식 `llama-simple` 예제를 참고하세요. 최신 C++17 코드와 CMake 대상은 모델 로드, 토큰화, 추론, 샘플링, 해제를 보여 줍니다. API가 바뀔 수 있으므로 같은 소스 버전의 예제와 헤더를 사용하세요.

```sh
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
cmake -B build -DLLAMA_BUILD_EXAMPLES=ON
cmake --build build --config Release --target llama-simple
```

## 4. 모델 크기와 한계

Q4_K_M 파일은 약 669 MB입니다. 모델 카드의 CPU 전용 RAM 기준은 약 3.17 GB이며 실제 요구량은 OS와 컨텍스트 등에 따라 달라집니다. TinyLLaMA 1.1B Chat v1.0은 작고 오래된 모델입니다. 품질과 언어 지원을 평가하고 결과를 검증한 뒤 사용하세요.

## 참고 자료

- [llama.cpp 공식 저장소](https://github.com/ggml-org/llama.cpp)
- [공식 C++ 예제](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/simple.cpp)
- [공식 CMake 대상](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/CMakeLists.txt)
- [예제 실행 방법](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/README.md)
- [TinyLLaMA 원본 모델](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- [TinyLLaMA GGUF 모델 카드](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF)
- [Q4_K_M 파일](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf)
