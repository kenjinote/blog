---
title: 'Как вызвать OpenAI API через curl из командной строки Windows'
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
lastmod: "2026-11-23"
tags: ["ChatGPT", "API", "Команда"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Отправьте текстовый запрос в OpenAI Responses API из cmd.exe в Windows. Задайте ключ API как переменную среды и передавайте JSON, не сохраняя ключ в файле запроса.'
---


В этом руководстве OpenAI API вызывается из `cmd.exe` в Windows. Для новых приложений рекомендуется Responses API. ChatGPT и API Platform — отдельные сервисы, а использование API оплачивается отдельно от подписки ChatGPT. Перед запросами проверьте [настройки оплаты API](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform).

## Задайте ключ API как переменную среды

Создайте ключ на странице [API keys в API Platform](https://platform.openai.com/api-keys). Не записывайте его в исходный код или файл запроса. В Windows нажмите `Win+R`, запустите `sysdm.cpl` и выберите **Дополнительно > Переменные среды > Переменные пользователя > Создать**. Укажите имя `OPENAI_API_KEY` и значение с ключом, затем откройте новое окно командной строки. Проверить наличие переменной можно, не показывая секрет:

```cmd
if defined OPENAI_API_KEY (echo OPENAI_API_KEY is set) else (echo OPENAI_API_KEY is missing)
```

Переменная среды помогает не встраивать ключ в исходный код приложения, но не делает его безопасным для публикации или передачи. Если ключ стал доступен посторонним, отзовите его и создайте новый на странице API keys. См. также [рекомендации по защите ключей API](https://developers.openai.com/api/docs/guides/production-best-practices).

## Создайте запрос

Сохраните этот JSON в файле `request.json` в рабочей папке. При использовании символов вне ASCII сохраните файл в UTF-8.

```json
{
  "model": "gpt-6.2-sol",
  "instructions": "Answer in Kansai dialect.",
  "input": "Explain what an API is in one sentence."
}
```

Идентификаторы моделей могут меняться, а доступ зависит от проекта API. Перед использованием модели из примера проверьте [текущий каталог моделей](https://developers.openai.com/api/docs/models).

## Отправьте запрос через curl.exe

В командной строке перейдите в папку с `request.json` и выполните:

```cmd
curl.exe --include https://api.openai.com/v1/responses ^
  -H "Content-Type: application/json" ^
  -H "Authorization: Bearer %OPENAI_API_KEY%" ^
  --data-binary "@request.json"
```

`--include` выводит HTTP-статус и заголовки ответа. Responses API возвращает JSON. Сгенерированный текст находится в элементе содержимого `output_text` внутри выходного сообщения. Вызовы инструментов и другие типы ответов могут содержать другие элементы, поэтому используйте JSON-парсер и проверяйте `type`, а не предполагайте фиксированный индекс массива. См. [справочник Responses API](https://developers.openai.com/api/reference/resources/responses/methods/create).

## Ошибки и использование

- `401` может означать, что ключ отсутствует, недействителен или не разрешён для проекта. Проверьте настройку, не выводя и не передавая значение ключа.
- `429` может означать ограничение частоты запросов или исчерпание кредитов либо лимита использования. Проверьте текст ответа и разделы Usage и Billing в API Platform.
- Стоимость зависит от модели и входных и выходных токенов. Проверяйте актуальные тарифы и использование проекта в API Platform; при необходимости задайте лимиты или уведомления.

## References

- [OpenAI API quickstart](https://developers.openai.com/api/docs/quickstart)
- [Text generation with the Responses API](https://developers.openai.com/api/docs/guides/text)
- [Responses API: create a response](https://developers.openai.com/api/reference/resources/responses/methods/create)
- [API models](https://developers.openai.com/api/docs/models)
- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- [OpenAI API key security best practices](https://developers.openai.com/api/docs/guides/production-best-practices)
- [ChatGPT and API billing are separate](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform)
