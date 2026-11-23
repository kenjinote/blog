---
title: 'Die OpenAI-API mit curl in der Windows-Eingabeaufforderung aufrufen'
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
lastmod: "2026-11-23"
tags: ["ChatGPT", "API", "Befehl"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Senden Sie mit Windows cmd.exe eine Textanfrage an die OpenAI Responses API. Legen Sie den API-Schlüssel als Umgebungsvariable fest und senden Sie JSON, ohne den Schlüssel in der Anfragedatei zu speichern.'
---


Diese Anleitung ruft die OpenAI-API über `cmd.exe` unter Windows auf. Für neue Anwendungen wird die Responses API empfohlen. ChatGPT und API Platform sind getrennte Dienste; die API-Nutzung wird zusätzlich zum ChatGPT-Abonnement abgerechnet. Prüfen Sie vor Anfragen die [API-Abrechnungseinstellungen](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform).

## API-Schlüssel als Umgebungsvariable festlegen

Erstellen Sie einen Schlüssel auf der API-Platform-Seite [API keys](https://platform.openai.com/api-keys). Schreiben Sie ihn weder in den Quellcode noch in die Anfragedatei. Drücken Sie unter Windows `Win+R`, starten Sie `sysdm.cpl` und öffnen Sie **Erweitert > Umgebungsvariablen > Benutzervariablen > Neu**. Verwenden Sie `OPENAI_API_KEY` als Namen und den Schlüssel als Wert. Öffnen Sie danach eine neue Eingabeaufforderung. Prüfen Sie die Variable, ohne den Schlüssel anzuzeigen:

```cmd
if defined OPENAI_API_KEY (echo OPENAI_API_KEY is set) else (echo OPENAI_API_KEY is missing)
```

Eine Umgebungsvariable hält den Schlüssel aus dem Anwendungscode heraus, macht eine Veröffentlichung oder Weitergabe aber nicht sicher. Widerrufen und ersetzen Sie einen offengelegten Schlüssel auf der API-keys-Seite. Beachten Sie auch die [Sicherheitsempfehlungen für API-Schlüssel](https://developers.openai.com/api/docs/guides/production-best-practices).

## Die Anfrage erstellen

Speichern Sie dieses JSON als `request.json` im Arbeitsordner. Verwenden Sie UTF-8, wenn Sie Nicht-ASCII-Zeichen einfügen.

```json
{
  "model": "gpt-6.2-sol",
  "instructions": "Answer in Kansai dialect.",
  "input": "Explain what an API is in one sentence."
}
```

Modell-IDs können sich ändern, und die Verfügbarkeit hängt vom API-Projekt ab. Prüfen Sie vor Verwendung das aktuelle [Modellverzeichnis](https://developers.openai.com/api/docs/models).

## Die Anfrage mit curl.exe senden

Wechseln Sie in der Eingabeaufforderung in den Ordner mit `request.json` und führen Sie Folgendes aus:

```cmd
curl.exe --include https://api.openai.com/v1/responses ^
  -H "Content-Type: application/json" ^
  -H "Authorization: Bearer %OPENAI_API_KEY%" ^
  --data-binary "@request.json"
```

`--include` zeigt HTTP-Status und Antwort-Header an. Die Responses API gibt JSON zurück. Der generierte Text steht in einem `output_text`-Inhaltselement innerhalb einer Ausgabenachricht. Tool-Aufrufe und andere Antworttypen können weitere Elemente enthalten; verwenden Sie einen JSON-Parser und prüfen Sie deren `type`, statt einen festen Array-Index anzunehmen. Siehe die [Responses-API-Referenz](https://developers.openai.com/api/reference/resources/responses/methods/create).

## Fehler und Nutzung

- `401` kann auf einen fehlenden, ungültigen oder für das Projekt nicht zugelassenen API-Schlüssel hinweisen. Prüfen Sie die Konfiguration, ohne den Wert auszugeben oder weiterzugeben.
- `429` kann eine Ratenbegrenzung oder aufgebrauchte Credits beziehungsweise Nutzungslimits bedeuten. Lesen Sie den Antworttext und prüfen Sie Usage und Billing in API Platform.
- Die Kosten hängen vom Modell und den Ein- und Ausgabetokens ab. Prüfen Sie aktuelle Preise und Projektnutzung in API Platform und richten Sie bei Bedarf Limits oder Warnungen ein.

## References

- [OpenAI API quickstart](https://developers.openai.com/api/docs/quickstart)
- [Text generation with the Responses API](https://developers.openai.com/api/docs/guides/text)
- [Responses API: create a response](https://developers.openai.com/api/reference/resources/responses/methods/create)
- [API models](https://developers.openai.com/api/docs/models)
- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- [OpenAI API key security best practices](https://developers.openai.com/api/docs/guides/production-best-practices)
- [ChatGPT and API billing are separate](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform)
