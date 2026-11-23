---
title: '如何在 Windows 命令提示字元中使用 curl 呼叫 OpenAI API'
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
lastmod: "2026-11-23"
tags: ["ChatGPT", "API", "命令"]
draft: false
image: "img.webp"
categories: ["programming"]
description: '說明如何從 Windows cmd.exe 向 OpenAI Responses API 傳送文字請求。將 API 金鑰設為環境變數，並透過 JSON 檔案傳送請求，避免把金鑰寫入請求內容。'
---


本文說明如何從 Windows `cmd.exe` 呼叫 OpenAI API。新應用程式建議使用 Responses API。ChatGPT 與 API Platform 是不同服務，API 使用費與 ChatGPT 訂閱分開計算。傳送請求前請先查看 [API 計費設定](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform)。

## 將 API 金鑰設為環境變數

在 API Platform 的[API keys 頁面](https://platform.openai.com/api-keys)建立金鑰。不要將金鑰寫進原始碼或請求檔。在 Windows 按 `Win+R`，執行 `sysdm.cpl`，選擇「進階」→「環境變數」→「使用者變數」→「新增」。變數名稱設為 `OPENAI_API_KEY`，變數值設為金鑰，然後重新開啟命令提示字元。可在不顯示金鑰的情況下檢查是否已設定：

```cmd
if defined OPENAI_API_KEY (echo OPENAI_API_KEY is set) else (echo OPENAI_API_KEY is missing)
```

環境變數可避免將金鑰硬編碼在應用程式原始碼中，但不代表可以公開或分享金鑰。若金鑰外洩，請在 API keys 頁面撤銷並換新。另請參閱 [API 金鑰安全最佳實務](https://developers.openai.com/api/docs/guides/production-best-practices)。

## 建立請求檔

將以下 JSON 儲存為工作資料夾中的 `request.json`。若包含非 ASCII 文字，請使用 UTF-8 儲存。

```json
{
  "model": "gpt-6.2-sol",
  "instructions": "Answer in Kansai dialect.",
  "input": "Explain what an API is in one sentence."
}
```

模型 ID 可能變更，且不同 API 專案可使用的模型也可能不同。使用範例模型前，請先查看目前的[模型目錄](https://developers.openai.com/api/docs/models)。

## 使用 curl.exe 傳送請求

在命令提示字元切換到 `request.json` 所在資料夾，然後執行：

```cmd
curl.exe --include https://api.openai.com/v1/responses ^
  -H "Content-Type: application/json" ^
  -H "Authorization: Bearer %OPENAI_API_KEY%" ^
  --data-binary "@request.json"
```

`--include` 會顯示 HTTP 狀態與回應標頭。Responses API 回傳 JSON，產生的文字位於輸出訊息中的 `output_text` 內容項目。工具呼叫等回應可能含有不同項目，請使用 JSON 剖析器檢查各項目的 `type`，不要假設陣列位置固定。詳見 [Responses API 參考資料](https://developers.openai.com/api/reference/resources/responses/methods/create)。

## 錯誤與用量

- `401` 可能表示金鑰未設定、無效或無權用於該專案。請檢查設定，不要輸出或分享金鑰值。
- `429` 可能表示觸發速率限制，或可用額度、用量上限已用完。請查看回應內容以及 API Platform 的 Usage 和 Billing。
- API 費用取決於模型以及輸入、輸出 token 數。請在 API Platform 查看目前價格和專案用量，並視需要設定上限或通知。

## References

- [OpenAI API quickstart](https://developers.openai.com/api/docs/quickstart)
- [Text generation with the Responses API](https://developers.openai.com/api/docs/guides/text)
- [Responses API: create a response](https://developers.openai.com/api/reference/resources/responses/methods/create)
- [API models](https://developers.openai.com/api/docs/models)
- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- [OpenAI API key security best practices](https://developers.openai.com/api/docs/guides/production-best-practices)
- [ChatGPT and API billing are separate](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform)
