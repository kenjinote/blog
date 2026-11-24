---
title: "Ollama로 로컬 LLM 실행하기: 설치, REST API, Python 연동"
slug: "ollama-local-llm-api-guide"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "programming", "api"]
tags: ["Ollama", "Local LLM", "Python", "Node.js"]
date: "2026-09-11T02:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

## Ollama 설치 및 모델 준비

공식 페이지에서 Windows, macOS 또는 Linux용 Ollama를 내려받습니다. Windows와 macOS에서는 앱을 실행하고, Linux에서는 공식 절차에 따라 설치한 뒤 서버가 실행 중이 아니면 시작합니다. 다음 명령은 이름을 지정한 모델을 내려받고 실행합니다. 제공 여부와 다운로드 크기는 바뀔 수 있으므로 모델 라이브러리를 먼저 확인하세요.

```bash
ollama pull gemma4:e2b
ollama run gemma4:e2b
```

모델을 시작한 뒤 다른 터미널에서 다음 명령으로 내려받은 모델과 현재 실행 메모리를 확인할 수 있습니다. 모델 파일은 디스크 공간을 사용하고, 추론에는 모델과 컨텍스트 길이에 따라 RAM 또는 GPU 메모리도 필요합니다.

```bash
ollama list
ollama ps
```

## 채팅 REST API 호출

로컬 HTTP API는 보통 `http://localhost:11434`에서 사용할 수 있습니다. `/api/chat`은 메시지 배열로 대화 기록을 받으며 기본적으로 응답을 스트리밍합니다. 이 예제는 완성된 JSON 응답을 받도록 `stream: false`를 지정하고 `format`으로 JSON 출력을 요청합니다.

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "gemma4:e2b",
  "messages": [
    {"role": "user", "content": "Explain what a REST API is in one sentence."}
  ],
  "stream": false,
}'
```

Windows PowerShell에서는 `curl`이 다른 명령의 별칭일 수 있습니다. 이 경우 `curl.exe`를 사용하세요.

응답 텍스트는 `message.content`에 있습니다. 응답 조각을 받으려면 `stream`을 `true`로 설정하거나 필드를 생략하세요. 대화 기록 없는 단일 프롬프트에는 `/api/generate`, 벡터에는 임베딩 모델과 `/api/embed`를 사용합니다.

## Python에서 Ollama 호출

공식 Python 라이브러리를 사용하면 HTTP 요청과 응답 객체 처리를 맡길 수 있습니다. 먼저 Ollama 서버를 시작하고 모델을 내려받으세요.

```bash
python -m pip install ollama
```

```python
from ollama import chat

response = chat(
    model="gemma4:e2b",
    messages=[{"role": "user", "content": "REST API가 무엇인지 한 문장으로 설명하세요."}],
    stream=False,
)
print(response.message.content)
```

응답을 순차적으로 받으려면 `stream=True`를 설정하고 반환된 청크를 반복 처리하세요. 공식 라이브러리는 비동기 애플리케이션용 `AsyncClient`도 제공합니다.

## Node.js에서 Ollama 호출

공식 JavaScript 패키지를 Node.js 프로젝트에 설치하세요.

```bash
npm install ollama
```

```javascript
import ollama from 'ollama';

const response = await ollama.chat({
  model: 'gemma4:e2b',
  messages: [{ role: 'user', content: 'REST API가 무엇인지 한 문장으로 설명하세요.' }],
  stream: false,
});
console.log(response.message.content);
```

## 임베딩과 검색

임베딩 API는 텍스트를 벡터로 변환합니다. 기본 RAG 흐름은 벡터를 인덱스에 저장하고 관련 문단을 검색해 채팅 프롬프트에 추가합니다. 임베딩 자체가 답변을 만들지는 않습니다.

```bash
ollama pull embeddinggemma
curl http://localhost:11434/api/embed -d '{
  "model": "embeddinggemma",
  "input": "REST API가 무엇인지 한 문장으로 설명하세요."
}'
```

응답에는 `embeddings` 배열이 포함됩니다. 사용할 언어, 데이터, 라이선스 요구 사항에 맞는 임베딩 모델과 벡터 인덱스를 선택하세요.

## 생성 속도 측정

응답에는 모델 로드, 프롬프트 평가, 생성 시간과 생성된 토큰 수가 포함됩니다. `eval_duration`은 생성에 걸린 나노초이며 전체 지연 시간이 아닙니다. 프롬프트 평가와 모델 로드 시간은 포함하지 않습니다. 토큰 생성 속도는 다음과 같이 계산합니다.

$$
\text{tokens/sec} = \frac{\text{eval\_count}}{\text{eval\_duration} / 10^9}
$$

모델 로드는 `load_duration`, 캐시되지 않은 프롬프트 평가는 `prompt_eval_duration`을 확인하세요. 같은 모델, 컨텍스트, 하드웨어에서 비교해야 합니다. 토큰 속도만으로 답변 품질이나 전체 지연 시간을 알 수는 없습니다.

## 메모리 사용량 추정

파라미터 수와 양자화 비트로 가중치 저장 공간의 대략적인 최솟값을 계산할 수 있습니다. 4-bit 8B 모델은 가중치만 약 4GB(십진 단위, 3.73GiB)입니다. 실제 전체 메모리는 더 필요합니다. 양자화 메타데이터, KV 캐시, 컨텍스트 길이, 런타임과 다른 앱도 메모리를 사용합니다.

$$
\text{weight bytes} \approx \frac{\text{parameter count} \times \text{bits per weight}}{8}
$$

`ollama ps`에서 모델이 GPU, CPU 또는 양쪽에서 실행되는지 확인할 수 있습니다. 실제 배치는 하드웨어와 런타임 지원에 따라 달라집니다.

## 개인정보, 네트워크 접근 및 라이선스

로컬에서만 쓰는 경우와 클라우드 모델 및 연결 앱을 사용하는 경우를 구분하세요. 민감한 데이터를 보내기 전에 모델, 도구, 네트워크 경로를 확인합니다. LAN이나 인터넷에서 API에 접근하도록 설정한다면 인증과 방화벽 같은 접근 제어 없이 포트를 노출하지 마세요. 모델별 라이선스도 확인해야 합니다.

Ollama는 모델 다운로드, 로컬 추론, 애플리케이션 연동을 한곳에서 제공합니다. 명령과 API 예제는 공식 문서에 기반한 기본 형태입니다. 모델별 기능과 요구 사항을 확인한 뒤 사용 환경에 맞게 조정하세요.

## 공식 자료

- [Ollama Quickstart](https://docs.ollama.com/quickstart)
- [Chat API](https://docs.ollama.com/api/chat)
- [Generate API](https://docs.ollama.com/api/generate)
- [Embeddings API](https://docs.ollama.com/api/embed)
- [Local FAQ and server configuration](https://docs.ollama.com/faq)
- [Official Python library](https://github.com/ollama/ollama-python)
- [Official JavaScript library](https://github.com/ollama/ollama-js)
- [Ollama model library](https://ollama.com/library)
