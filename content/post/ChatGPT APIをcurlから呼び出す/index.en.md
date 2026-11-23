---
title: 'How to Call the OpenAI API with curl from Windows Command Prompt'
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
lastmod: "2026-11-23"
tags: ["ChatGPT", "API", "Command"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Send a text request to OpenAI''s Responses API from Windows cmd.exe. Set the API key as an environment variable and send JSON without putting the key in the request file.'
---


This guide calls the OpenAI API from Windows `cmd.exe`. The Responses API is recommended for new applications. ChatGPT and the API Platform are separate services, and API usage is billed separately from a ChatGPT subscription. Check [API billing setup](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform) before making requests.

## Set the API key as an environment variable

Create a key on the API Platform [API keys page](https://platform.openai.com/api-keys). Do not put it in source code or the request file. In Windows, press `Win+R`, run `sysdm.cpl`, and choose **Advanced > Environment Variables > User variables > New**. Set the variable name to `OPENAI_API_KEY` and its value to your key, then open a new Command Prompt. You can check that it is set without displaying the secret:

```cmd
if defined OPENAI_API_KEY (echo OPENAI_API_KEY is set) else (echo OPENAI_API_KEY is missing)
```

An environment variable keeps the key out of the application source; it does not make the key safe to publish or share. Revoke and replace a leaked key on the API keys page. See [API key security best practices](https://developers.openai.com/api/docs/guides/production-best-practices).

## Create the request

Save this JSON as `request.json` in your working folder. Save the file as UTF-8 if you include non-ASCII text.

```json
{
  "model": "gpt-6.2-sol",
  "instructions": "Answer in Kansai dialect.",
  "input": "Explain what an API is in one sentence."
}
```

Model IDs can change, and model access depends on the API project. Check the current [model catalog](https://developers.openai.com/api/docs/models) before using the example model.

## Send the request with curl.exe

In Command Prompt, change to the folder containing `request.json` and run:

```cmd
curl.exe --include https://api.openai.com/v1/responses ^
  -H "Content-Type: application/json" ^
  -H "Authorization: Bearer %OPENAI_API_KEY%" ^
  --data-binary "@request.json"
```

`--include` displays the HTTP status and response headers. The Responses API returns JSON. Generated text is in an `output_text` content item inside an output message. Tool calls and other response types can add different items, so use a JSON parser and inspect each item's `type` instead of assuming a fixed array index. See the [Responses API reference](https://developers.openai.com/api/reference/resources/responses/methods/create).

## Errors and usage

- `401` can indicate a missing, invalid, or unauthorized API key. Check the key configuration without printing or sharing the value.
- `429` can indicate a rate limit or an exhausted credit or usage limit. Read the response body and check API Platform Usage and Billing.
- API cost depends on the model and input/output tokens. Check current pricing and project usage in the API Platform, and configure limits or alerts if needed.

## References

- [OpenAI API quickstart](https://developers.openai.com/api/docs/quickstart)
- [Text generation with the Responses API](https://developers.openai.com/api/docs/guides/text)
- [Responses API: create a response](https://developers.openai.com/api/reference/resources/responses/methods/create)
- [API models](https://developers.openai.com/api/docs/models)
- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- [OpenAI API key security best practices](https://developers.openai.com/api/docs/guides/production-best-practices)
- [ChatGPT and API billing are separate](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform)
