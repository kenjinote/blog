---
title: 'Como chamar a API da OpenAI com curl no Prompt de Comando do Windows'
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
lastmod: "2026-11-23"
tags: ["ChatGPT", "API", "Comando"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Envie uma solicitação de texto para a Responses API da OpenAI pelo cmd.exe do Windows. Configure a chave como variável de ambiente e envie JSON sem gravar a chave no arquivo de solicitação.'
---


Este guia chama a API da OpenAI pelo `cmd.exe` do Windows. A Responses API é recomendada para novas aplicações. ChatGPT e API Platform são serviços separados, e o uso da API é cobrado separadamente da assinatura do ChatGPT. Confira a [configuração de cobrança da API](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform) antes de enviar solicitações.

## Configurar a chave como variável de ambiente

Crie uma chave na página [API keys da API Platform](https://platform.openai.com/api-keys). Não a coloque no código-fonte nem no arquivo de solicitação. No Windows, pressione `Win+R`, execute `sysdm.cpl` e abra **Avançado > Variáveis de Ambiente > Variáveis de usuário > Novo**. Use `OPENAI_API_KEY` como nome e a chave como valor; depois abra um novo Prompt de Comando. Confira se está definida sem exibir o segredo:

```cmd
if defined OPENAI_API_KEY (echo OPENAI_API_KEY is set) else (echo OPENAI_API_KEY is missing)
```

A variável de ambiente evita incluir a chave no código da aplicação, mas não torna seguro publicá-la ou compartilhá-la. Se a chave vazar, revogue-a na página API keys e substitua-a. Consulte também as [práticas recomendadas de segurança para chaves](https://developers.openai.com/api/docs/guides/production-best-practices).

## Criar a solicitação

Salve este JSON como `request.json` na pasta de trabalho. Salve em UTF-8 se incluir texto não ASCII.

```json
{
  "model": "gpt-6.2-sol",
  "instructions": "Answer in Kansai dialect.",
  "input": "Explain what an API is in one sentence."
}
```

Os IDs dos modelos podem mudar, e o acesso varia conforme o projeto da API. Consulte o [catálogo atual de modelos](https://developers.openai.com/api/docs/models) antes de usar o modelo do exemplo.

## Enviar com curl.exe

No Prompt de Comando, acesse a pasta que contém `request.json` e execute:

```cmd
curl.exe --include https://api.openai.com/v1/responses ^
  -H "Content-Type: application/json" ^
  -H "Authorization: Bearer %OPENAI_API_KEY%" ^
  --data-binary "@request.json"
```

`--include` exibe o status HTTP e os cabeçalhos da resposta. A Responses API retorna JSON. O texto gerado está em um item de conteúdo `output_text` dentro de uma mensagem de saída. Chamadas de ferramentas e outros tipos de resposta podem acrescentar itens diferentes; use um analisador JSON e verifique o `type` de cada item em vez de presumir um índice fixo. Consulte a [referência da Responses API](https://developers.openai.com/api/reference/resources/responses/methods/create).

## Erros e uso

- `401` pode indicar chave ausente, inválida ou sem autorização para o projeto. Confira a configuração sem imprimir ou compartilhar o valor.
- `429` pode indicar limite de requisições ou esgotamento de créditos ou do limite de uso. Leia o corpo da resposta e confira Usage e Billing na API Platform.
- O custo depende do modelo e dos tokens de entrada e saída. Confira os preços atuais e o uso do projeto na API Platform; configure limites ou alertas se necessário.

## References

- [OpenAI API quickstart](https://developers.openai.com/api/docs/quickstart)
- [Text generation with the Responses API](https://developers.openai.com/api/docs/guides/text)
- [Responses API: create a response](https://developers.openai.com/api/reference/resources/responses/methods/create)
- [API models](https://developers.openai.com/api/docs/models)
- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- [OpenAI API key security best practices](https://developers.openai.com/api/docs/guides/production-best-practices)
- [ChatGPT and API billing are separate](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform)
