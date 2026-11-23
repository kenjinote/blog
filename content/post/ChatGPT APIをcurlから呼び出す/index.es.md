---








title: 'Cómo llamar a la API de OpenAI con curl desde el símbolo del sistema de Windows'
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
lastmod: "2026-11-23"
tags: ["ChatGPT", "API", "Comandos"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Envía una solicitud de texto a la Responses API de OpenAI desde cmd.exe en Windows. Configura la clave como variable de entorno y envía JSON sin incluir la clave en el archivo de solicitud.'
---


Esta guía llama a la API de OpenAI desde `cmd.exe` de Windows. Se recomienda Responses API para las aplicaciones nuevas. ChatGPT y API Platform son servicios separados, y el uso de la API se factura aparte de la suscripción de ChatGPT. Consulta la [configuración de facturación de la API](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform) antes de enviar solicitudes.

## Configurar la clave como variable de entorno

Crea una clave en la página [API keys de API Platform](https://platform.openai.com/api-keys). No la incluyas en el código fuente ni en el archivo de solicitud. En Windows, pulsa `Win+R`, ejecuta `sysdm.cpl` y ve a **Opciones avanzadas > Variables de entorno > Variables de usuario > Nueva**. Usa `OPENAI_API_KEY` como nombre y la clave como valor; después abre una nueva ventana del Símbolo del sistema. Comprueba que está configurada sin mostrar el secreto:

```cmd
if defined OPENAI_API_KEY (echo OPENAI_API_KEY is set) else (echo OPENAI_API_KEY is missing)
```

Una variable de entorno evita incluir la clave en el código de la aplicación, pero no hace que sea seguro publicarla o compartirla. Revoca y sustituye cualquier clave expuesta en la página API keys. Consulta también las [prácticas recomendadas de seguridad para claves](https://developers.openai.com/api/docs/guides/production-best-practices).

## Crear la solicitud

Guarda este JSON como `request.json` en tu carpeta de trabajo. Si incluyes texto no ASCII, guarda el archivo en UTF-8.

```json
{
  "model": "gpt-6.2-sol",
  "instructions": "Answer in Kansai dialect.",
  "input": "Explain what an API is in one sentence."
}
```

Los ID de modelo pueden cambiar y el acceso depende del proyecto API. Consulta el [catálogo actual de modelos](https://developers.openai.com/api/docs/models) antes de usar el modelo del ejemplo.

## Enviar con curl.exe

En el Símbolo del sistema, cambia a la carpeta que contiene `request.json` y ejecuta:

```cmd
curl.exe --include https://api.openai.com/v1/responses ^
  -H "Content-Type: application/json" ^
  -H "Authorization: Bearer %OPENAI_API_KEY%" ^
  --data-binary "@request.json"
```

`--include` muestra el estado HTTP y las cabeceras de respuesta. Responses API devuelve JSON. El texto generado está en un elemento de contenido `output_text` dentro de un mensaje de salida. Las llamadas a herramientas y otros tipos de respuesta pueden incluir elementos distintos; usa un analizador JSON y comprueba el `type` en vez de suponer un índice fijo. Consulta la [referencia de Responses API](https://developers.openai.com/api/reference/resources/responses/methods/create).

## Errores y uso

- `401` puede indicar que falta la clave, que no es válida o que no tiene permiso para el proyecto. Comprueba la configuración sin imprimir ni compartir su valor.
- `429` puede indicar un límite de velocidad o que se agotaron los créditos o el límite de uso. Revisa el cuerpo de respuesta y las páginas Usage y Billing de API Platform.
- El coste depende del modelo y de los tokens de entrada y salida. Consulta los precios actuales y el uso del proyecto en API Platform; configura límites o alertas si hace falta.

## References

- [OpenAI API quickstart](https://developers.openai.com/api/docs/quickstart)
- [Text generation with the Responses API](https://developers.openai.com/api/docs/guides/text)
- [Responses API: create a response](https://developers.openai.com/api/reference/resources/responses/methods/create)
- [API models](https://developers.openai.com/api/docs/models)
- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- [OpenAI API key security best practices](https://developers.openai.com/api/docs/guides/production-best-practices)
- [ChatGPT and API billing are separate](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform)
