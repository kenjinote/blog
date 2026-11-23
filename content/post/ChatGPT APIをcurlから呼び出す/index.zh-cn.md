---
title: '在 Windows 命令提示符中使用 curl 调用 OpenAI API'
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
lastmod: "2026-11-23"
tags: ["ChatGPT", "API", "命令"]
draft: false
image: "img.webp"
categories: ["programming"]
description: '介绍如何从 Windows cmd.exe 向 OpenAI Responses API 发送文本请求。将 API 密钥设为环境变量，并通过 JSON 文件发送请求，避免把密钥写入请求内容。'
---


本文介绍从 Windows `cmd.exe` 调用 OpenAI API。新应用推荐使用 Responses API。ChatGPT 与 API Platform 是两项独立服务，API 使用费用与 ChatGPT 订阅分开结算。发送请求前请先查看 [API 计费设置](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform)。

## 将 API 密钥设为环境变量

在 API Platform 的[API keys 页面](https://platform.openai.com/api-keys)创建密钥。不要将密钥写入源代码或请求文件。在 Windows 中按 `Win+R`，运行 `sysdm.cpl`，选择“高级”→“环境变量”→“用户变量”→“新建”。变量名设为 `OPENAI_API_KEY`，变量值设为密钥，然后重新打开命令提示符。可以在不显示密钥的情况下检查变量是否存在：

```cmd
if defined OPENAI_API_KEY (echo OPENAI_API_KEY is set) else (echo OPENAI_API_KEY is missing)
```

环境变量可以避免将密钥写入应用源码，但不代表可以公开或分享密钥。如果密钥泄漏，请在 API keys 页面撤销并更换。另请参阅 [API 密钥安全最佳实践](https://developers.openai.com/api/docs/guides/production-best-practices)。

## 创建请求文件

将以下 JSON 保存为工作目录中的 `request.json`。若包含非 ASCII 文本，请使用 UTF-8 保存。

```json
{
  "model": "gpt-6.2-sol",
  "instructions": "Answer in Kansai dialect.",
  "input": "Explain what an API is in one sentence."
}
```

模型 ID 可能会变更，且不同 API 项目可使用的模型也可能不同。使用示例模型前，请查看当前[模型目录](https://developers.openai.com/api/docs/models)。

## 使用 curl.exe 发送请求

在命令提示符中切换到 `request.json` 所在文件夹，然后运行：

```cmd
curl.exe --include https://api.openai.com/v1/responses ^
  -H "Content-Type: application/json" ^
  -H "Authorization: Bearer %OPENAI_API_KEY%" ^
  --data-binary "@request.json"
```

`--include` 会显示 HTTP 状态码和响应头。Responses API 返回 JSON，生成的文本位于输出消息中的 `output_text` 内容项里。工具调用等响应可能包含不同项目，因此请使用 JSON 解析器检查每项的 `type`，不要假定固定的数组位置。详见 [Responses API 参考](https://developers.openai.com/api/reference/resources/responses/methods/create)。

## 错误与用量

- `401` 可能表示密钥未设置、无效，或无权用于该项目。请检查配置，不要打印或分享密钥值。
- `429` 可能表示触发速率限制，或可用额度、用量上限已耗尽。请查看响应正文以及 API Platform 的 Usage 和 Billing 页面。
- API 费用取决于模型以及输入、输出 token 数。请在 API Platform 查看当前价格和项目用量，并按需设置上限或提醒。

## References

- [OpenAI API quickstart](https://developers.openai.com/api/docs/quickstart)
- [Text generation with the Responses API](https://developers.openai.com/api/docs/guides/text)
- [Responses API: create a response](https://developers.openai.com/api/reference/resources/responses/methods/create)
- [API models](https://developers.openai.com/api/docs/models)
- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- [OpenAI API key security best practices](https://developers.openai.com/api/docs/guides/production-best-practices)
- [ChatGPT and API billing are separate](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform)
