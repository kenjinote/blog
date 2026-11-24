---
title: "Mit der X API und Google Colab posten [Python]"
date: "2023-04-08T18:48:32+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Twitter APIとGoogle Colaboratoryを使ってTweetする方法"
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Lies Zugangsdaten aus Google Colab Secrets und veröffentliche mit Tweepy und X API v2 einen Beitrag. Prüfe vor dem Ausführen den aktuellen API-Zugang und die Preise."
---

# Einführung

Dieses Minimalbeispiel verwendet Tweepy in Google Colab, um mit X API v2 einen Beitrag im eigenen Konto zu veröffentlichen. Zugang, Preise und Authentifizierungsanforderungen können sich ändern. Prüfe daher vor dem Ausführen die offizielle Dokumentation und Developer Console.

## Wichtig: Zugangsdaten aus der vorherigen Version

Eine frühere Version dieses Artikels enthielt API-Schlüssel und Zugriffstokens im Text. Behandle alle veröffentlichten Zugangsdaten als kompromittiert. Falls die Werte echt und aktiv waren, widerrufe die betroffenen Schlüssel und Tokens in der X Developer Console und erstelle neue. Kopien können in der Repository-Historie verbleiben; die Entfernung von der aktuellen Seite allein reicht daher nicht aus.

# Vorbereitung

1. Erstelle in der [X Developer Console](https://developer.x.com/en/portal/dashboard) ein Project und eine App und richte Benutzerzugangsdaten mit Schreibberechtigung ein. Bei OAuth 1.0a User Context musst du die Lese- und Schreibrechte der App konfigurieren, bevor du Zugriffstokens erstellst. Bei OAuth 2.0 PKCE fordere die nötigen Scopes einschließlich `tweet.write` an.
2. Prüfe in der Developer Console den aktuellen Tarif, den Preis des Schreib-Endpunkts und die Nutzungslimits. Preise und Zugang können sich ändern; verlasse dich nicht auf alte Tutorials oder frühere Preisangaben.
3. Erstelle ein Notebook in [Google Colab](https://colab.research.google.com/). Lege im Bereich Secrets (Schlüsselsymbol) vier Secrets mit den Namen unten an und erlaube diesem Notebook den Zugriff. Trage deine eigenen App-Werte ein und füge sie nicht in Notebook-Code oder Ausgaben ein.
   - `X_API_KEY`
   - `X_API_KEY_SECRET`
   - `X_ACCESS_TOKEN`
   - `X_ACCESS_TOKEN_SECRET`

# Einen Beitrag veröffentlichen

Beim Ausführen dieser Zelle wird der Text aus `text` über dein X-Konto öffentlich gepostet. Prüfe Konto und Text vor dem Ausführen. Es können X-API-Gebühren anfallen.

```python
%pip install -q tweepy

from google.colab import userdata
import tweepy

client = tweepy.Client(
    consumer_key=userdata.get("X_API_KEY"),
    consumer_secret=userdata.get("X_API_KEY_SECRET"),
    access_token=userdata.get("X_ACCESS_TOKEN"),
    access_token_secret=userdata.get("X_ACCESS_TOKEN_SECRET"),
)

text = "Hello from the X API"
response = client.create_tweet(text=text)
print(response.data["id"])
```

## Automatisierung

Dieses Beispiel veröffentlicht einen Beitrag nur, wenn du die Zelle manuell ausführst. Lies vor einer Erweiterung um geplante Beiträge oder automatische Antworten die [X-Automatisierungsregeln](https://help.x.com/en/rules-and-policies/x-automation). Für automatische Antworten gelten zusätzliche Anforderungen, etwa eine klare Absichtserklärung der empfangenden Person. Colab garantiert keinen dauerhaften Betrieb; Laufzeiten und Nutzungslimits können sich ändern.

## Quellen

- [X API: Create or Edit Post](https://docs.x.com/x-api/posts/create-post)
- [X API v2 authentication mapping](https://docs.x.com/fundamentals/authentication/guides/v2-authentication-mapping)
- [X API pricing and credits](https://docs.x.com/x-api/getting-started/pricing)
- [X automation rules](https://help.x.com/en/rules-and-policies/x-automation)
- [Google Colab FAQ](https://research.google.com/colaboratory/faq.html)
- [Tweepy Client reference](https://docs.tweepy.org/en/stable/client.html)
- [Tweepy authentication guide](https://docs.tweepy.org/en/stable/authentication.html)
