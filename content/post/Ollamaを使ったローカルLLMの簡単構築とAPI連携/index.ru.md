---
title: "Запуск локальных LLM с Ollama: установка, REST API и Python"
slug: "ollama-local-llm-api-guide"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "programming", "api"]
tags: ["Ollama", "Local LLM", "Python", "Node.js"]
date: "2026-09-11T02:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

## Установка Ollama и подготовка модели

Загрузите Ollama для Windows, macOS или Linux с официальной страницы. Запустите приложение в Windows или macOS; в Linux следуйте официальной инструкции и запустите сервер, если он ещё не работает. Эти команды загружают и запускают указанную модель. Перед использованием проверьте библиотеку моделей: наличие и размер загрузки могут меняться.

```bash
ollama pull gemma4:e2b
ollama run gemma4:e2b
```

После запуска модели выполните эти команды в другом терминале, чтобы посмотреть загруженные модели и текущее размещение в памяти. Файлы моделей занимают место на диске; для вывода также нужны RAM или память GPU в зависимости от модели и длины контекста.

```bash
ollama list
ollama ps
```

## Вызов REST API чата

Локальный HTTP API обычно доступен по адресу `http://localhost:11434`. `/api/chat` принимает историю в виде массива сообщений и по умолчанию передаёт ответ потоком. В примере `stream: false` задаёт единый ответ JSON, а `format` запрашивает JSON-вывод.

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "gemma4:e2b",
  "messages": [
    {"role": "user", "content": "Explain what a REST API is in one sentence."}
  ],
  "stream": false,
}'
```

В Windows PowerShell `curl` может быть псевдонимом другой команды; в этом случае используйте `curl.exe`.

Текст ответа находится в `message.content`. Установите `stream` в `true` или опустите это поле, чтобы получать части ответа. Для одного запроса без истории используйте `/api/generate`, а для векторов — `/api/embed` с моделью эмбеддингов.

## Вызов Ollama из Python

Официальная библиотека Python выполняет HTTP-запрос и обрабатывает объект ответа. Сначала запустите сервер Ollama и загрузите модель.

```bash
python -m pip install ollama
```

```python
from ollama import chat

response = chat(
    model="gemma4:e2b",
    messages=[{"role": "user", "content": "Объясните одним предложением, что такое REST API."}],
    stream=False,
)
print(response.message.content)
```

Чтобы получать ответ по частям, установите `stream=True` и перебирайте возвращённые фрагменты. В официальной библиотеке также есть `AsyncClient` для асинхронных приложений.

## Вызов Ollama из Node.js

Установите официальный пакет JavaScript в проект Node.js.

```bash
npm install ollama
```

```javascript
import ollama from 'ollama';

const response = await ollama.chat({
  model: 'gemma4:e2b',
  messages: [{ role: 'user', content: 'Объясните одним предложением, что такое REST API.' }],
  stream: false,
});
console.log(response.message.content);
```

## Эмбеддинги и поиск

API эмбеддингов преобразует текст в векторы. В простом процессе RAG векторы сохраняют в индексе, находят подходящие фрагменты и добавляют их в запрос чату; сами эмбеддинги ответы не создают.

```bash
ollama pull embeddinggemma
curl http://localhost:11434/api/embed -d '{
  "model": "embeddinggemma",
  "input": "Объясните одним предложением, что такое REST API."
}'
```

Ответ содержит массив `embeddings`. Выберите модель и векторный индекс с учётом языка, данных и требований лицензии.

## Измерение скорости генерации

В ответе указаны время загрузки модели, обработки prompt, генерации и число созданных токенов. `eval_duration` — время генерации в наносекундах; это не полная задержка, оно не включает обработку prompt и загрузку модели. Скорость генерации оценивается так:

$$
\text{tokens/sec} = \frac{\text{eval\_count}}{\text{eval\_duration} / 10^9}
$$

Для загрузки модели используйте `load_duration`, а для оценки некэшированного prompt — `prompt_eval_duration`. Сравнивайте одинаковые модели, контекст и оборудование; скорость токенов сама по себе не описывает качество ответа и полную задержку.

## Оценка использования памяти

Число параметров и разрядность квантования дают примерную нижнюю оценку объёма для весов. Модель 8B с 4-битными весами занимает около 4 десятичных ГБ (3,73 GiB) только для весов. Полная потребность выше: метаданные квантования, KV-кэш, длина контекста, среда выполнения и другие программы тоже занимают память.

$$
\text{weight bytes} \approx \frac{\text{parameter count} \times \text{bits per weight}}{8}
$$

Команда `ollama ps` показывает, работает ли модель на GPU, CPU или на обоих. Реальное распределение зависит от оборудования и поддержки со стороны runtime.

## Приватность, сетевой доступ и лицензии

Различайте полностью локальную работу, облачные модели и подключённые приложения. Перед отправкой конфиденциальных данных проверьте модель, инструменты и сетевой маршрут. Если API доступен по локальной сети или через Интернет, не открывайте порт без средств контроля доступа, например аутентификации и межсетевого экрана. Проверяйте лицензию каждой модели.

Ollama объединяет загрузку моделей, локальный вывод и доступ из приложений. Команды и примеры API здесь — базовые шаблоны из официальной документации. Проверьте возможности и требования конкретной модели и адаптируйте их к своему компьютеру.

## Официальные источники

- [Ollama Quickstart](https://docs.ollama.com/quickstart)
- [Chat API](https://docs.ollama.com/api/chat)
- [Generate API](https://docs.ollama.com/api/generate)
- [Embeddings API](https://docs.ollama.com/api/embed)
- [Local FAQ and server configuration](https://docs.ollama.com/faq)
- [Official Python library](https://github.com/ollama/ollama-python)
- [Official JavaScript library](https://github.com/ollama/ollama-js)
- [Ollama model library](https://ollama.com/library)
