---








title: "'TinyLLaMA를 C++에서 호출할 수 있게 하는 절차(llama.cpp 사용)'"
date: 2025-07-19T09:40:53+09:00
tags: ["C++", "llama.cpp", "TinyLLaMA", "AI"]
draft: false
image: "img.png"
categories: ["프로그래밍"]
---









# ✅ TinyLLaMA × C++ 설정 절차(`llama.cpp` 사용)

---

## 🔧 Step 1: llama.cpp 준비하기

### 1-1. 필요한 환경 (최소한)

* OS: Windows / Linux / macOS
* 개발 환경: g++ / clang / MSVC
* Git / CMake

### 1-2. llama.cpp 가져오기 및 빌드

```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
mkdir build
cd build
cmake ..
cmake --build . --config Release
```

> Windows라면 `Visual Studio Developer Command Prompt`에서 `cmake --build . --config Release`를 사용하면 편합니다.

---

## 📦 Step 2: TinyLLaMA 모델 다운로드 및 변환

### 2-1. HuggingFace에서 원본 모델 가져오기

예: [TinyLLaMA-1.1B](https://huggingface.co/openaccess-ai-collective/TinyLlama-1.1B-Chat-v1.0)

```bash
# 필요에 따라 transformers를 사용하여 다운로드
pip install transformers huggingface_hub

python3 -m transformers.models.llama.convert_llama_weights_to_hf \
    --input_dir ./TinyLlama-1.1B-Chat \
    --model_size 1B \
    --output_dir ./hf_model
```

> 이는 Hugging Face 형식으로 변환하는 단계입니다.

---

### 2-2. GGUF 형식으로 변환(`llama.cpp`용)

```bash
cd llama.cpp
python3 convert.py ./hf_model --outfile tinyllama.gguf
```

### 2-3. 모델 양자화(크기 축소)

```bash
./quantize ./tinyllama.gguf ./tinyllama-q4.gguf q4_0
```

> `q4_0`은 4bit 양자화입니다. 모델 크기가 약 **350MB 내외**로 작아집니다.

---

## 🧪 Step 3: C++에서 모델 호출하기(코드 예시)

### 3-1. 간단한 C++ 코드(추론)

```cpp
#include "llama.h"
#include <iostream>

int main() {
    llama_model_params model_params = llama_model_default_params();
    llama_context_params ctx_params = llama_context_default_params();

    llama_model *model = llama_load_model_from_file("tinyllama-q4.gguf", model_params);
    llama_context *ctx = llama_new_context_with_model(model, ctx_params);

    std::string prompt = "사용자가 Excel 데이터를 읽어와 필터링한 후 저장하고 싶다고 합니다. 노드 구성은?";
    llama_batch batch = llama_batch_init(512, 0, 1);
    llama_token BOS = llama_token_bos(model);
    batch.token[0] = BOS;

    // 토크나이즈
    std::vector<llama_token> tokens(prompt.size() + 8);
    int n = llama_tokenize(model, prompt.c_str(), tokens.data(), tokens.size(), true);
    tokens.resize(n);

    for (size_t i = 0; i < tokens.size(); ++i) {
        batch.token[i + 1] = tokens[i];
    }

    batch.n_tokens = tokens.size() + 1;
    llama_decode(ctx, batch);

    // 추론 결과 가져오기
    for (int i = 0; i < 50; ++i) {
        llama_token next = llama_sample_token(ctx, nullptr);
        std::cout << llama_token_to_str(model, next);
        llama_batch next_batch = llama_batch_init(1, 0, 1);
        next_batch.token[0] = next;
        next_batch.n_tokens = 1;
        llama_decode(ctx, next_batch);
    }

    llama_free(ctx);
    llama_free_model(model);
    return 0;
}
```

---

## 🧱 Step 4: 컴파일 방법(예시)

```bash
g++ -I./llama.cpp main.cpp ./llama.cpp/build/libllama.a -o tiny_infer -pthread -std=c++11
```

> `libllama.a`는 빌드 후 `build/` 디렉토리에 생성됩니다.

---

## ✅ 결과물 구성 예시(정리)

```
my_app/
├── tinyllama-q4.gguf      # 양자화된 모델 (~350MB)
├── main.cpp               # 위의 C++ 코드
├── llama.cpp/             # llama.cpp 본체
└── build/
    └── libllama.a         # 컴파일된 라이브러리
```

---

## 🧠 사용 사례 적용을 위한 보충

* 출력을 받아 `노드 템플릿을 대조 및 선정`하는 코드를 C++ 내에 둠
* 예: "Excel", "필터", "저장"이 포함됨 → 해당 노드 그룹 생성
* 이 부분은 `if 문 + JSON 템플릿 읽기`와 같은 간단한 구성으로 충분함

---

## 📌 요약

| 항목 | 내용 |
| ----- | ------------------------------------ |
| 권장 모델 | TinyLLaMA-1.1B-Chat v1.0 (GGUF + 양자화) |
| 크기 | \~350〜450MB (4bit 양자화) |
| C++ 연동 | `llama.cpp`를 사용하여 가능, 외부 의존성 거의 없음 |
| 처리 능력 | 간단한 의도 파악 및 출력문 생성에 충분 (자연어→구성) |
| 확장성 | 슬롯 채우기 및 템플릿 호출과 결합하여 노드 생성 AI로 활용 가능 |
