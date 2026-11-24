---
title: "Lokale LLMs mit Ollama ausführen: Einrichtung, REST-API und Python"
slug: "ollama-local-llm-api-guide"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "programming", "api"]
tags: ["Ollama", "Local LLM", "Python", "Node.js"]
date: "2026-09-11T02:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

## Ollama installieren und ein Modell vorbereiten

Laden Sie Ollama für Windows, macOS oder Linux von der offiziellen Seite herunter. Starten Sie unter Windows und macOS die App; folgen Sie unter Linux der offiziellen Anleitung und starten Sie den Server, falls er noch nicht läuft. Die Befehle laden ein ausdrücklich genanntes Modell herunter und starten es. Prüfen Sie vorher die Modellbibliothek, da Verfügbarkeit und Downloadgröße variieren können.

```bash
ollama pull gemma4:e2b
ollama run gemma4:e2b
```

Nach dem Start eines Modells können Sie in einem weiteren Terminal die heruntergeladenen Modelle und deren aktuelle Speicherbelegung prüfen. Modelldateien benötigen Speicherplatz; für die Inferenz werden je nach Modell und Kontextlänge zusätzlicher RAM oder GPU-Speicher benötigt.

```bash
ollama list
ollama ps
```

## Die Chat-REST-API aufrufen

Die lokale HTTP-API ist normalerweise unter `http://localhost:11434` erreichbar. `/api/chat` erwartet den Gesprächsverlauf als Nachrichtenliste und streamt standardmäßig. Dieses Beispiel setzt `stream` auf `false`, damit eine vollständige JSON-Antwort zurückkommt, und fordert mit `format` JSON an.

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "gemma4:e2b",
  "messages": [
    {"role": "user", "content": "Explain what a REST API is in one sentence."}
  ],
  "stream": false,
}'
```

In Windows PowerShell kann `curl` ein Alias für einen anderen Befehl sein. Verwenden Sie dann `curl.exe`.

Der Antworttext steht in `message.content`. Setzen Sie `stream` auf `true` oder lassen Sie das Feld weg, um Teilergebnisse zu erhalten. Für eine einzelne Eingabe ohne Gesprächsverlauf verwenden Sie `/api/generate`; für Vektoren `/api/embed` mit einem Embedding-Modell.

## Ollama aus Python aufrufen

Die offizielle Python-Bibliothek übernimmt HTTP-Aufruf und Antwortobjekte. Starten Sie zuvor den Ollama-Server und laden Sie das Modell herunter.

```bash
python -m pip install ollama
```

```python
from ollama import chat

response = chat(
    model="gemma4:e2b",
    messages=[{"role": "user", "content": "Erkläre in einem Satz, was eine REST-API ist."}],
    stream=False,
)
print(response.message.content)
```

Für eine schrittweise Ausgabe setzen Sie `stream=True` und durchlaufen die zurückgegebenen Chunks. Die offizielle Bibliothek bietet für asynchrone Anwendungen außerdem `AsyncClient`.

## Ollama aus Node.js aufrufen

Installieren Sie das offizielle JavaScript-Paket in Ihrem Node.js-Projekt.

```bash
npm install ollama
```

```javascript
import ollama from 'ollama';

const response = await ollama.chat({
  model: 'gemma4:e2b',
  messages: [{ role: 'user', content: 'Erkläre in einem Satz, was eine REST-API ist.' }],
  stream: false,
});
console.log(response.message.content);
```

## Embeddings und Suche

Die Embeddings-API wandelt Text in Vektoren um. Ein einfacher RAG-Ablauf speichert diese in einem Index, ruft passende Textstellen ab und ergänzt damit den Chat-Prompt; Embeddings erzeugen selbst keine Antworten.

```bash
ollama pull embeddinggemma
curl http://localhost:11434/api/embed -d '{
  "model": "embeddinggemma",
  "input": "Erkläre in einem Satz, was eine REST-API ist."
}'
```

Die Antwort enthält ein `embeddings`-Array. Wählen Sie Modell und Vektorindex passend zu Sprache, Daten und Lizenzbedingungen.

## Generierungsgeschwindigkeit messen

Die Antwort enthält Ladezeit, Prompt-Auswertungszeit, Generierungszeit und die Anzahl erzeugter Tokens. `eval_duration` misst die Generierung in Nanosekunden; es ist nicht die gesamte Antwortzeit und enthält weder Prompt-Auswertung noch Modellladen. Die Tokenrate lässt sich so abschätzen:

$$
\text{tokens/sec} = \frac{\text{eval\_count}}{\text{eval\_duration} / 10^9}
$$

Verwenden Sie `load_duration` für das Laden des Modells und `prompt_eval_duration` für die Auswertung nicht zwischengespeicherter Prompts. Vergleichen Sie dieselben Modelle, Kontexte und Geräte; die Tokenrate allein sagt nichts über Antwortqualität oder Gesamtlatenz aus.

## Speicherbedarf abschätzen

Parameterzahl und Quantisierungsbits liefern eine grobe Untergrenze für den Speicherbedarf der Gewichte. Ein 8B-Modell mit 4 Bit benötigt dafür etwa 4 GB dezimal (3,73 GiB). Das ist nicht der gesamte Speicherbedarf: Quantisierungsdaten, KV-Cache, Kontextlänge, Laufzeit und andere Programme benötigen zusätzlichen Speicher.

$$
\text{weight bytes} \approx \frac{\text{parameter count} \times \text{bits per weight}}{8}
$$

Mit `ollama ps` sehen Sie, ob ein Modell auf der GPU, der CPU oder auf beiden ausgeführt wird. Die tatsächliche Verteilung hängt von der Hardware und der Laufzeitunterstützung ab.

## Datenschutz, Netzwerkzugriff und Lizenzen

Unterscheiden Sie die rein lokale Nutzung von Cloud-Modellen und verbundenen Anwendungen. Prüfen Sie vor der Eingabe vertraulicher Daten das Modell, die Werkzeuge und den Netzwerkpfad. Wenn die API im LAN oder Internet erreichbar sein soll, darf der Port nicht ohne Zugriffsschutz wie Authentifizierung und Firewall offengelegt werden. Beachten Sie die Lizenz jedes Modells.

Ollama bündelt Modelldownload, lokale Inferenz und den Zugriff aus Anwendungen. Die Befehle und API-Beispiele sind Grundmuster aus der offiziellen Dokumentation. Prüfen Sie die Funktionen und Anforderungen des jeweiligen Modells und passen Sie die Beispiele an Ihre Umgebung an.

## Offizielle Quellen

- [Ollama Quickstart](https://docs.ollama.com/quickstart)
- [Chat API](https://docs.ollama.com/api/chat)
- [Generate API](https://docs.ollama.com/api/generate)
- [Embeddings API](https://docs.ollama.com/api/embed)
- [Local FAQ and server configuration](https://docs.ollama.com/faq)
- [Official Python library](https://github.com/ollama/ollama-python)
- [Official JavaScript library](https://github.com/ollama/ollama-js)
- [Ollama model library](https://ollama.com/library)
