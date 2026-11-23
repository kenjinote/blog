---








title: 'Windows 명령 프롬프트에서 curl로 OpenAI API 호출하기'
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
lastmod: "2026-11-23"
tags: ["ChatGPT", "API", "명령어"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Windows cmd.exe에서 OpenAI Responses API로 텍스트 요청을 보내는 방법을 설명합니다. API 키를 환경 변수로 설정하고 요청 파일에 키를 넣지 않은 채 JSON을 전송합니다.'
---


이 문서는 Windows `cmd.exe`에서 OpenAI API를 호출합니다. 새 애플리케이션에는 Responses API가 권장됩니다. ChatGPT와 API Platform은 별도 서비스이며 API 사용 요금은 ChatGPT 구독 요금과 별도로 청구됩니다. 요청을 보내기 전에 [API 결제 설정](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform)을 확인하세요.

## API 키를 환경 변수로 설정하기

API Platform의 [API keys 페이지](https://platform.openai.com/api-keys)에서 키를 만듭니다. 키를 소스 코드나 요청 파일에 넣지 마세요. Windows에서 `Win+R`을 누르고 `sysdm.cpl`을 실행한 다음 **고급 > 환경 변수 > 사용자 변수 > 새로 만들기**로 이동합니다. 변수 이름은 `OPENAI_API_KEY`, 값은 생성한 키로 설정하고 새 명령 프롬프트를 엽니다. 키를 표시하지 않고 설정 여부를 확인할 수 있습니다.

```cmd
if defined OPENAI_API_KEY (echo OPENAI_API_KEY is set) else (echo OPENAI_API_KEY is missing)
```

환경 변수는 애플리케이션 소스에 키를 하드코딩하지 않도록 도와주지만 키를 공개하거나 공유해도 안전해지는 것은 아닙니다. 키가 노출되면 API keys 페이지에서 폐기하고 새 키로 교체하세요. [API 키 보안 모범 사례](https://developers.openai.com/api/docs/guides/production-best-practices)도 참고하세요.

## 요청 파일 만들기

아래 JSON을 작업 폴더에 `request.json`으로 저장합니다. ASCII가 아닌 문자를 넣을 경우 UTF-8로 저장하세요.

```json
{
  "model": "gpt-6.2-sol",
  "instructions": "Answer in Kansai dialect.",
  "input": "Explain what an API is in one sentence."
}
```

모델 ID는 변경될 수 있고 API 프로젝트에 따라 사용 가능한 모델이 다릅니다. 예제 모델을 쓰기 전에 현재 [모델 카탈로그](https://developers.openai.com/api/docs/models)를 확인하세요.

## curl.exe로 요청 보내기

명령 프롬프트에서 `request.json`이 있는 폴더로 이동해 실행합니다.

```cmd
curl.exe --include https://api.openai.com/v1/responses ^
  -H "Content-Type: application/json" ^
  -H "Authorization: Bearer %OPENAI_API_KEY%" ^
  --data-binary "@request.json"
```

`--include`는 HTTP 상태와 응답 헤더를 표시합니다. Responses API는 JSON을 반환하며, 생성된 텍스트는 출력 메시지 안의 `output_text` 콘텐츠 항목에 있습니다. 도구 호출 등의 응답에는 다른 항목이 포함될 수 있으므로 배열 번호를 고정해서 가정하지 말고 JSON 파서로 각 항목의 `type`을 확인하세요. 자세한 내용은 [Responses API 참조](https://developers.openai.com/api/reference/resources/responses/methods/create)를 확인하세요.

## 오류와 사용량

- `401`은 키가 없거나 잘못되었거나 해당 프로젝트에서 사용할 권한이 없음을 뜻할 수 있습니다. 키를 출력하거나 공유하지 말고 설정을 확인하세요.
- `429`는 요청 속도 제한 또는 사용 가능한 크레딧·한도 소진을 뜻할 수 있습니다. 응답 본문과 API Platform의 Usage 및 Billing을 확인하세요.
- API 비용은 모델과 입력·출력 토큰에 따라 달라집니다. API Platform에서 최신 가격과 프로젝트 사용량을 확인하고 필요한 경우 한도나 알림을 설정하세요.

## References

- [OpenAI API quickstart](https://developers.openai.com/api/docs/quickstart)
- [Text generation with the Responses API](https://developers.openai.com/api/docs/guides/text)
- [Responses API: create a response](https://developers.openai.com/api/reference/resources/responses/methods/create)
- [API models](https://developers.openai.com/api/docs/models)
- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- [OpenAI API key security best practices](https://developers.openai.com/api/docs/guides/production-best-practices)
- [ChatGPT and API billing are separate](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform)
