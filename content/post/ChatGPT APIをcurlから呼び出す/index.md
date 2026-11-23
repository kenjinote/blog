---
title: 'WindowsのコマンドプロンプトからOpenAI APIをcurlで呼び出す方法'
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
lastmod: "2026-11-23"
tags: ["OpenAI API", "curl", "コマンドプロンプト"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Windowsのコマンドプロンプトからcurl.exeとOpenAI Responses APIを使ってテキストを生成する手順を紹介します。APIキーを環境変数に設定し、リクエストJSONを送る方法を解説します。'
---

ここでは Windows の `cmd.exe` から OpenAI API を呼び出します。新しいアプリでは Responses API が推奨されています。ChatGPT の画面で使うサービスと API Platform は別のサービスで、API の利用料は ChatGPT のサブスクリプションとは別に計算されます。利用前に[API の請求設定](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform)を確認してください。

## APIキーを環境変数に設定する

API Platform の[API keys ページ](https://platform.openai.com/api-keys)でキーを作成します。キーをソースコードやリクエストファイルに書かず、`Win+R` から `sysdm.cpl` を開き、「詳細設定」→「環境変数」→「ユーザー環境変数」の「新規」で名前を `OPENAI_API_KEY`、値を作成したキーに設定します。設定後は新しいコマンドプロンプトを開きます。キーを画面に表示せず設定を確認するには、次を実行します。

```cmd
if defined OPENAI_API_KEY (echo OPENAI_API_KEY is set) else (echo OPENAI_API_KEY is missing)
```

環境変数はアプリのソースにキーを埋め込まないための手段です。公開リポジトリへキーを登録したり、第三者と共有したりしないでください。キーが漏れた場合は API keys ページで失効させ、新しいキーに置き換えます。[APIキーの安全な管理方法](https://developers.openai.com/api/docs/guides/production-best-practices)も参照してください。

## リクエストを作成する

作業フォルダーに `request.json` というファイルを作り、次の JSON を保存します。内容は日本語を含む UTF-8 で保存できます。

```json
{
  "model": "gpt-6.2-sol",
  "instructions": "Answer in Kansai dialect.",
  "input": "Explain what an API is in one sentence."
}
```

モデル ID は変更されることがあり、アカウントやプロジェクトによって利用できるモデルも異なります。使用前に[モデル一覧](https://developers.openai.com/api/docs/models)で現在の ID と利用条件を確認してください。

## curl.exeから送信する

コマンドプロンプトで `request.json` を保存したフォルダーへ移動し、次を実行します。この例は `cmd.exe` 用です。PowerShell では環境変数の参照と行継続記号が異なります。

```cmd
curl.exe --include https://api.openai.com/v1/responses ^
  -H "Content-Type: application/json" ^
  -H "Authorization: Bearer %OPENAI_API_KEY%" ^
  --data-binary "@request.json"
```

`--include` は HTTP ステータスとレスポンスヘッダーも表示します。Responses API のレスポンスは JSON です。テキストは `output` 内の `message` にある `content` の `output_text` として返ります。ツール呼び出しなどでは出力項目が変わるため、固定の配列番号を前提にせず、必要に応じて JSON パーサーで `type` を確認して取り出してください。詳しくは[Responses API のリファレンス](https://developers.openai.com/api/reference/resources/responses/methods/create)を参照してください。

## エラーと利用量

- `401` は API キーが無効、未設定、または対象プロジェクトに対して使えない可能性があります。キーを表示・共有せず設定を確認してください。
- `429` はレート制限または利用可能なクレジット・上限に達した場合などに返ります。レスポンス本文と API Platform の Usage / Billing を確認してください。
- API の使用量はモデルや入力・出力トークンなどで変わります。最新の料金とプロジェクトの利用量を API Platform で確認し、必要に応じて上限や通知を設定してください。

## 参考

- [OpenAI API quickstart](https://developers.openai.com/api/docs/quickstart)
- [Text generation with the Responses API](https://developers.openai.com/api/docs/guides/text)
- [Responses API: create a response](https://developers.openai.com/api/reference/resources/responses/methods/create)
- [API models](https://developers.openai.com/api/docs/models)
- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- [OpenAI API key security best practices](https://developers.openai.com/api/docs/guides/production-best-practices)
- [ChatGPT and API billing are separate](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform)
