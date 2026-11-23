---
title: "Copilot과 로컬 AI 중 무엇을 쓸까? 데이터 경계와 측정으로 결정하기"
slug: "hybrid-ai-development-workflow"
date: "2026-09-11T21:00:00+09:00"
lastmod: "2026-11-23T12:00:00+09:00"
description: "데이터 정책, 작업 품질, 지연 시간, 비용, 하드웨어를 기준으로 GitHub Copilot 같은 클라우드 도구와 로컬 모델을 선택하는 방법입니다."
image: "img/eyecatch.jpg"
categories: ["programming", "ai", "productivity"]
tags: ["GitHub Copilot", "Local AI", "Workflow", "Privacy"]
---

# [Copilot과 로컬 AI 중 무엇을 쓸까? 데이터 경계와 측정으로 결정하기](https://kenji.blog/p/hybrid-ai-development-workflow/)

코딩 보조 도구는 IDE 자동완성부터 에이전트식 편집까지 다양합니다. 클라우드는 더 강력하고 로컬은 더 안전하다고 단정하지 마세요. 전송되는 데이터, 적용 약관, 실제 작업 품질, 지연 시간과 운영비를 확인해야 합니다.

이 글은 2026년 11월 23일 공식 문서를 확인해 작성했습니다. 제품, 모델, 설정과 정책은 바뀌므로 도입 전 링크와 조직 규정을 다시 확인하세요.

## 클라우드 AI와 로컬 추론은 데이터 경로가 다릅니다

GitHub Copilot 같은 클라우드 기능은 모델과 IDE 기능에 따라 프롬프트, 코드 조각, 관련 저장소 맥락을 서비스로 보낼 수 있습니다. GitHub의 현재 정책에 따르면 개인 Copilot 플랜의 상호작용 데이터는 모델 학습과 개선에 사용될 수 있으며 개인 설정에서 거부할 수 있습니다. Copilot Business와 Enterprise 고객 데이터는 고객 승인 없이 학습에 사용하지 않는다고 설명합니다. 플랜, 모델 호스팅 주체, 기능, 관리자 설정을 확인하세요.

- [개인 구독자를 위한 GitHub Copilot 정책](https://docs.github.com/en/copilot/how-tos/manage-your-account/manage-policies)
- [GitHub Copilot 모델 호스팅과 데이터 처리](https://docs.github.com/en/copilot/reference/ai-models/model-hosting)

로컬 추론은 자신의 기기에서 모델을 실행하므로 입력을 기기 안에 둘 수 있습니다. 하지만 로컬 모델을 선택하는 것만으로 완전한 오프라인 환경이 되지는 않습니다. 확장 기능의 텔레메트리와 동기화, 외부 도구, 모델 다운로드 중 네트워크 통신을 확인하세요. Continue의 오프라인 안내에는 확장과 모델을 미리 준비하고 익명 텔레메트리를 끄는 방법이 나와 있습니다.

- [인터넷 없이 Continue 실행하기](https://docs.continue.dev/guides/running-continue-without-internet)

Ollama에는 `http://localhost:11434`의 로컬 API와 API 키가 필요한 호스팅 클라우드 API `https://ollama.com/api`가 모두 있습니다. Ollama를 쓴다고 추론이 항상 로컬인 것은 아닙니다. 설정된 endpoint를 확인하세요. 로컬 서버를 네트워크에 공개한다면 별도로 접근 제어를 설계해야 합니다.

- [Ollama API endpoint와 사용법](https://docs.ollama.com/api/introduction)

## 작업과 데이터 분류에 맞춰 경로 선택하기

먼저 조직의 데이터 분류와 AI 이용 정책으로 어떤 코드, 로그, 설계 문서, 자격 증명을 승인된 환경 밖으로 보낼 수 있는지 정하세요. 로컬이든 클라우드든 비밀 값을 프롬프트에 넣지 말고 테스트 값으로 바꾸세요. 클라우드는 플랜별 학습 이용, 보존, 악용 모니터링, 지역, 관리자 제어, 모델 호스트로의 재전송도 확인합니다.

- 일상적인 자동완성, 주석, 테스트 초안: 품질, 지연, IDE 통합, 전송 데이터 확인; 승인된 클라우드 기능 또는 소형 로컬 모델.
- 내부 코드 요약·수정: 입력 범위, 근거 검토, 계약, 보존 조건 확인; 조직 승인 클라우드 또는 통제된 로컬 환경.
- 기밀·규제 코드: 외부 전송, 로그, 네트워크 경계, 감사 확인; 조직 승인을 받은 격리 로컬 환경.
- 대규모 설계·복잡한 디버깅: 평가 품질, 컨텍스트 한도, 도구 권한, 비용 확인; 요구사항에 맞는 클라우드 또는 사내 호스팅 모델.
- 인터넷이 없는 환경: 사전 다운로드, 확장 네트워크, 업데이트와 보안 패치 확인; 검증된 오프라인 구성.

이는 성능 순위가 아닙니다. 조직 규칙과 작업 평가로 경로를 좁히기 위한 시작점입니다.

## 같은 작업에서 품질·지연·비용 측정하기

실제 업무에서 성공 기준, 실패 사례, 점수 기준이 있는 작은 테스트 세트를 만드세요. 후보 모델에 같은 코드와 지시를 주고 모델 ID, 확장 기능, 날짜, 설정을 기록합니다. 정확성, 테스트 통과, 기존 설계와의 일관성, 안전한 거부, 수정 시간을 비교하세요. 결과는 달라질 수 있으므로 여러 번 실행하고, 중요한 코드는 개발자가 검토하고 테스트를 실행해야 합니다.

첫 출력까지와 완료까지의 시간을 구분합니다. 총비용에는 클라우드 이용료, 구독, 재시도와 검토 시간뿐 아니라 로컬 하드웨어 구매, 전력, 유지보수도 포함하세요. 로컬 속도와 품질은 모델 크기, 양자화, 컨텍스트 길이, GPU/메모리, IDE 설정에 따라 달라집니다. 파라미터 수나 VRAM의 단일 추정치만으로 판단하지 말고 실제 장비에서 테스트하세요.

## 로컬 모델을 시험하는 최소 절차

Ollama를 설치하고 모델 카탈로그에서 라이선스, 다운로드 크기, 기능을 확인한 뒤 정확한 태그를 가져옵니다.

```sh
ollama pull <model-name:tag>
```

Continue의 현재 설정 형식으로 Ollama를 다음과 같이 등록할 수 있습니다. `<MODEL_ID>`를 `ollama list`에 표시되는 다운로드된 모델 ID로 바꾸세요.

```yaml
name: Local coding model
version: 0.0.1
schema: v1
models:
  - name: Local model
    provider: ollama
    model: <MODEL_ID>
    apiBase: http://localhost:11434
    roles:
      - chat
```

도구 호출, 이미지 입력, 컨텍스트 한도는 모델마다 다릅니다. IDE가 자동 감지하더라도 실제로 시험하세요. 최소 권한으로 시작하고 파일을 수정하거나 셸 명령을 실행하는 에이전트에는 사람의 검토와 승인을 요구하세요. 외부 코드에 포함된 프롬프트 인젝션도 고려해야 합니다.

- [Ollama API](https://docs.ollama.com/api/introduction)
- [Continue의 Ollama 설정](https://docs.continue.dev/customize/model-providers/top-level/ollama)
- [Ollama 모델 라이브러리](https://ollama.com/library)

## 작은 작업부터 시작하고 조건 변경 시 재평가하기

위험이 낮은 작업을 선택하고 같은 테스트 세트로 승인된 클라우드 기능과 로컬 모델을 비교하세요. 출력 품질, 수정 시간, 지연, 비용, 데이터 목적지를 검토한 뒤 작업별 팀 규칙을 정합니다. 모델, 플랜, 확장 기능, 계약이 바뀌면 정책과 평가도 다시 확인하세요.

안전성은 클라우드인지 로컬인지 하나만으로 결정되지 않습니다. 데이터 처리 경로를 파악하고 입력을 최소화하며 승인된 환경에서 검증하세요.
