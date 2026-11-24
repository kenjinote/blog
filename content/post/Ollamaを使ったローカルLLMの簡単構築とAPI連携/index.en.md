---
title: "Run Local LLMs with Ollama: Setup, REST API, and Python"
slug: "ollama-local-llm-api-guide"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "programming", "api"]
tags: ["Ollama", "Local LLM", "Python", "Node.js"]
date: "2026-09-11T02:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

## Install Ollama and prepare a model

Download Ollama for Windows, macOS, or Linux from its official page. Start the app on Windows or macOS; on Linux, follow the official installation steps and start the server if it is not already running. These commands pull and run an explicitly named model. Check the model library before use because availability and download size can change.

```bash
ollama pull gemma4:e2b
ollama run gemma4:e2b
```

After starting a model, use these commands in another terminal to inspect downloaded models and current runtime placement. Model files use disk space; inference also needs RAM or GPU memory based on the model and context length.

```bash
ollama list
ollama ps
```

## Call the chat REST API

The local HTTP API is normally available at `http://localhost:11434`. `/api/chat` accepts conversation history as an array of messages and streams by default. This example sets `stream` to `false` for a single JSON response and requests JSON output with `format`.

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "gemma4:e2b",
  "messages": [
    {"role": "user", "content": "Explain what a REST API is in one sentence."}
  ],
  "stream": false,
}'
```

In Windows PowerShell, `curl` may be an alias for a different command; use `curl.exe` in that case.

The response text is in `message.content`. Set `stream` to `true` (or omit it) to receive incremental response objects. For one prompt without chat history, use `/api/generate`; use `/api/embed` with an embedding model when you need vectors.

## Call Ollama from Python

The official Python library handles the HTTP request and response objects for you. Start the Ollama server and pull the model first.

```bash
python -m pip install ollama
```

```python
from ollama import chat

response = chat(
    model="gemma4:e2b",
    messages=[{"role": "user", "content": "Explain what a REST API is in one sentence."}],
    stream=False,
)
print(response.message.content)
```

For incremental output, set `stream=True` and iterate over the returned chunks. The official library also provides `AsyncClient` for asynchronous applications.

## Call Ollama from Node.js

Install the official JavaScript package in your Node.js project.

```bash
npm install ollama
```

```javascript
import ollama from 'ollama';

const response = await ollama.chat({
  model: 'gemma4:e2b',
  messages: [{ role: 'user', content: 'Explain what a REST API is in one sentence.' }],
  stream: false,
});
console.log(response.message.content);
```

## Embeddings and retrieval

The embeddings API turns text into vectors. A basic RAG flow stores vectors in an index, retrieves relevant passages, and adds them to a chat prompt; embeddings do not generate answers by themselves.

```bash
ollama pull embeddinggemma
curl http://localhost:11434/api/embed -d '{
  "model": "embeddinggemma",
  "input": "Explain what a REST API is in one sentence."
}'
```

The response contains an `embeddings` array. Choose the embedding model and vector index for your language, data, and license requirements.

## Measure generation speed

Responses report model-load time, prompt-evaluation time, generation time, and generated token count. `eval_duration` measures generation time in nanoseconds; it is not end-to-end latency and excludes prompt evaluation and model loading. Estimate generation throughput with:

$$
\text{tokens/sec} = \frac{\text{eval\_count}}{\text{eval\_duration} / 10^9}
$$

Use `load_duration` for model loading and `prompt_eval_duration` for uncached prompt evaluation. Compare runs on the same model, context, and hardware; throughput alone does not describe answer quality or end-to-end latency.

## Estimate memory use

Parameter count and quantization bits give a rough lower-bound estimate for weight storage. An 8B model at 4-bit precision is about 4 GB decimal (3.73 GiB) for weights. This is not a full memory requirement: quantization metadata, KV cache, context length, runtime overhead, and other applications need additional memory.

$$
\text{weight bytes} \approx \frac{\text{parameter count} \times \text{bits per weight}}{8}
$$

Use `ollama ps` to see whether a model is on the GPU, CPU, or split across both. Actual placement depends on available hardware and runtime support.

## Privacy, network access, and licenses

Distinguish local-only use from cloud models and connected applications. Before sending sensitive data, check the selected model, tools, and network path. If you make the API reachable from a LAN or the internet, do not expose the port without access controls such as authentication and a firewall. Check each model's license before using or redistributing it.

Ollama brings model downloads, local inference, and application access together. The commands and API examples here are basic patterns based on the official documentation. Check model-specific capabilities and requirements, then adapt them to your model and machine.

## Official references

- [Ollama Quickstart](https://docs.ollama.com/quickstart)
- [Chat API](https://docs.ollama.com/api/chat)
- [Generate API](https://docs.ollama.com/api/generate)
- [Embeddings API](https://docs.ollama.com/api/embed)
- [Local FAQ and server configuration](https://docs.ollama.com/faq)
- [Official Python library](https://github.com/ollama/ollama-python)
- [Official JavaScript library](https://github.com/ollama/ollama-js)
- [Ollama model library](https://ollama.com/library)
