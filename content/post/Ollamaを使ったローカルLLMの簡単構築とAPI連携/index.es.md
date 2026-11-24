---
title: "Ejecutar LLM locales con Ollama: instalación, API REST y Python"
slug: "ollama-local-llm-api-guide"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "programming", "api"]
tags: ["Ollama", "Local LLM", "Python", "Node.js"]
date: "2026-09-11T02:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

## Instalar Ollama y preparar un modelo

Descarga Ollama para Windows, macOS o Linux desde la página oficial. Abre la aplicación en Windows o macOS; en Linux, sigue la instalación oficial e inicia el servidor si aún no está activo. Estos comandos descargan y ejecutan un modelo concreto. Consulta la biblioteca antes, ya que la disponibilidad y el tamaño pueden cambiar.

```bash
ollama pull gemma4:e2b
ollama run gemma4:e2b
```

Después de iniciar un modelo, usa estos comandos en otra terminal para consultar los modelos descargados y dónde se ejecutan. Los archivos ocupan espacio en disco; la inferencia también necesita RAM o memoria de GPU según el modelo y la longitud del contexto.

```bash
ollama list
ollama ps
```

## Llamar a la API REST de chat

La API HTTP local suele estar disponible en `http://localhost:11434`. `/api/chat` recibe el historial como una lista de mensajes y transmite la respuesta de forma predeterminada. Este ejemplo usa `stream: false` para obtener una respuesta JSON completa y solicita salida JSON con `format`.

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "gemma4:e2b",
  "messages": [
    {"role": "user", "content": "Explain what a REST API is in one sentence."}
  ],
  "stream": false,
}'
```

En Windows PowerShell, `curl` puede ser un alias de otro comando; en ese caso, usa `curl.exe`.

El texto de respuesta está en `message.content`. Establece `stream` en `true` o quita el campo para recibir fragmentos sucesivos. Para una sola instrucción sin historial usa `/api/generate`; para obtener vectores, usa `/api/embed` con un modelo de embeddings.

## Usar Ollama desde Python

La biblioteca oficial de Python gestiona la solicitud HTTP y los objetos de respuesta. Antes, inicia el servidor de Ollama y descarga el modelo.

```bash
python -m pip install ollama
```

```python
from ollama import chat

response = chat(
    model="gemma4:e2b",
    messages=[{"role": "user", "content": "Explica en una frase qué es una API REST."}],
    stream=False,
)
print(response.message.content)
```

Para recibir la salida por partes, establece `stream=True` y recorre los fragmentos devueltos. La biblioteca oficial también ofrece `AsyncClient` para aplicaciones asíncronas.

## Usar Ollama desde Node.js

Instala el paquete oficial de JavaScript en tu proyecto de Node.js.

```bash
npm install ollama
```

```javascript
import ollama from 'ollama';

const response = await ollama.chat({
  model: 'gemma4:e2b',
  messages: [{ role: 'user', content: 'Explica en una frase qué es una API REST.' }],
  stream: false,
});
console.log(response.message.content);
```

## Embeddings y búsqueda

La API de embeddings convierte texto en vectores. Un flujo RAG básico los guarda en un índice, recupera pasajes relevantes y los añade al prompt del chat; los embeddings no generan respuestas por sí solos.

```bash
ollama pull embeddinggemma
curl http://localhost:11434/api/embed -d '{
  "model": "embeddinggemma",
  "input": "Explica en una frase qué es una API REST."
}'
```

La respuesta contiene una matriz `embeddings`. Elige el modelo de embeddings y el índice vectorial según el idioma, los datos y las licencias de tu aplicación.

## Medir la velocidad de generación

La respuesta informa del tiempo de carga del modelo, evaluación del prompt, generación y número de tokens generados. `eval_duration` mide la generación en nanosegundos; no es la latencia total e ignora la evaluación del prompt y la carga del modelo. La velocidad se estima así:

$$
\text{tokens/sec} = \frac{\text{eval\_count}}{\text{eval\_duration} / 10^9}
$$

Usa `load_duration` para consultar la carga del modelo y `prompt_eval_duration` para evaluar prompts no almacenados en caché. Compara el mismo modelo, contexto y hardware; la tasa de tokens no mide por sí sola la calidad ni la latencia total.

## Estimar el uso de memoria

El número de parámetros y los bits de cuantización permiten estimar de forma aproximada el almacenamiento mínimo de los pesos. Un modelo 8B a 4 bits ocupa unos 4 GB decimales (3,73 GiB) solo en pesos. No es el requisito total: los metadatos de cuantización, la caché KV, el contexto, el entorno de ejecución y otras aplicaciones necesitan memoria adicional.

$$
\text{weight bytes} \approx \frac{\text{parameter count} \times \text{bits per weight}}{8}
$$

Usa `ollama ps` para ver si el modelo se ejecuta en la GPU, la CPU o ambas. La distribución real depende del hardware disponible y de la compatibilidad del runtime.

## Privacidad, acceso de red y licencias

Distingue el uso exclusivamente local de los modelos en la nube y las aplicaciones conectadas. Antes de enviar datos sensibles, comprueba el modelo, las herramientas y la ruta de red. Si haces que la API sea accesible desde una LAN o Internet, no expongas el puerto sin controles como autenticación y cortafuegos. Revisa la licencia de cada modelo.

Ollama reúne la descarga de modelos, la inferencia local y el acceso desde aplicaciones. Los comandos y ejemplos de API son patrones básicos basados en la documentación oficial. Comprueba las capacidades y requisitos de cada modelo y adapta los ejemplos al equipo que uses.

## Referencias oficiales

- [Ollama Quickstart](https://docs.ollama.com/quickstart)
- [Chat API](https://docs.ollama.com/api/chat)
- [Generate API](https://docs.ollama.com/api/generate)
- [Embeddings API](https://docs.ollama.com/api/embed)
- [Local FAQ and server configuration](https://docs.ollama.com/faq)
- [Official Python library](https://github.com/ollama/ollama-python)
- [Official JavaScript library](https://github.com/ollama/ollama-js)
- [Ollama model library](https://ollama.com/library)
