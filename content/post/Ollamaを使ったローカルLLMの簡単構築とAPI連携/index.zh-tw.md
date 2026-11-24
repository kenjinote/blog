---
title: "使用 Ollama 執行本機 LLM：安裝、REST API 與 Python"
slug: "ollama-local-llm-api-guide"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "programming", "api"]
tags: ["Ollama", "Local LLM", "Python", "Node.js"]
date: "2026-09-11T02:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

## 安裝 Ollama 並準備模型

從官方頁面下載 Windows、macOS 或 Linux 版 Ollama。在 Windows 和 macOS 啟動應用程式；在 Linux 依官方步驟安裝，若伺服器尚未執行則啟動它。以下命令會下載並執行指定模型。模型供應與下載大小可能改變，請先查看模型庫。

```bash
ollama pull gemma4:e2b
ollama run gemma4:e2b
```

模型啟動後，可在另一個終端機使用這些命令查看已下載的模型及其目前執行位置。模型檔案會占用磁碟空間；推論也需要符合模型與上下文長度的 RAM 或 GPU 記憶體。

```bash
ollama list
ollama ps
```

## 呼叫聊天 REST API

本機 HTTP API 通常位於 `http://localhost:11434`。`/api/chat` 接收由訊息組成的對話歷史，預設以串流方式回傳。範例將 `stream` 設為 `false` 以取得完整 JSON 回應，並透過 `format` 要求 JSON 輸出。

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "gemma4:e2b",
  "messages": [
    {"role": "user", "content": "Explain what a REST API is in one sentence."}
  ],
  "stream": false,
}'
```

在 Windows PowerShell 中，`curl` 可能是其他命令的別名；此時請使用 `curl.exe`。

回應文字位於 `message.content`。將 `stream` 設為 `true` 或省略此欄位，即可逐段接收回應。沒有對話歷史的單一提示可使用 `/api/generate`；需要向量時，搭配嵌入模型使用 `/api/embed`。

## 在 Python 中呼叫 Ollama

官方 Python 套件會處理 HTTP 請求和回應物件。請先啟動 Ollama 伺服器並下載模型。

```bash
python -m pip install ollama
```

```python
from ollama import chat

response = chat(
    model="gemma4:e2b",
    messages=[{"role": "user", "content": "用一句話說明什麼是 REST API。"}],
    stream=False,
)
print(response.message.content)
```

若要逐段輸出，請設定 `stream=True` 並逐一處理回傳的內容區塊。官方套件也提供非同步應用程式使用的 `AsyncClient`。

## 在 Node.js 中呼叫 Ollama

在 Node.js 專案中安裝官方 JavaScript 套件。

```bash
npm install ollama
```

```javascript
import ollama from 'ollama';

const response = await ollama.chat({
  model: 'gemma4:e2b',
  messages: [{ role: 'user', content: '用一句話說明什麼是 REST API。' }],
  stream: false,
});
console.log(response.message.content);
```

## 嵌入與檢索

嵌入 API 會將文字轉換為向量。基本 RAG 流程會將向量存入索引、擷取相關段落，再將內容加入聊天提示；嵌入本身不會產生答案。

```bash
ollama pull embeddinggemma
curl http://localhost:11434/api/embed -d '{
  "model": "embeddinggemma",
  "input": "用一句話說明什麼是 REST API。"
}'
```

回應中包含 `embeddings` 陣列。請依照應用程式的語言、資料和授權需求選擇嵌入模型與向量索引。

## 測量生成速度

回應包含模型載入、提示詞評估、生成耗時及生成的 token 數。`eval_duration` 是生成階段的奈秒耗時，不是端對端延遲，也不包含提示詞處理與模型載入。可用下式估算生成速度：

$$
\text{tokens/sec} = \frac{\text{eval\_count}}{\text{eval\_duration} / 10^9}
$$

使用 `load_duration` 查看模型載入時間，使用 `prompt_eval_duration` 查看未快取提示詞的評估時間。請在相同模型、上下文和硬體條件下比較；吞吐量本身無法代表回答品質或端對端延遲。

## 估算記憶體用量

參數數量和量化位元數可用來粗估權重儲存的下限。4-bit 的 8B 模型光是權重大約需要 4 GB（十進位，約 3.73 GiB）。這不是完整記憶體需求：量化中繼資料、KV 快取、上下文長度、執行環境及其他應用程式都會額外占用記憶體。

$$
\text{weight bytes} \approx \frac{\text{parameter count} \times \text{bits per weight}}{8}
$$

使用 `ollama ps` 查看模型執行於 GPU、CPU 或兩者之間。實際分配取決於可用硬體和執行階段支援。

## 隱私、網路存取與授權

請區分純本機使用、雲端模型和連線應用程式。傳送敏感資料前，先確認所選模型、工具和網路路徑。若要讓 API 可從區域網路或網際網路存取，請使用驗證、防火牆等存取控制，不要直接公開連接埠。也要確認各模型的授權條款。

Ollama 將模型下載、本機推論和應用程式存取整合在同一工具中。本文命令和 API 範例是根據官方文件整理的基本用法。請確認個別模型的功能與需求，再依電腦環境調整。

## 官方資料

- [Ollama Quickstart](https://docs.ollama.com/quickstart)
- [Chat API](https://docs.ollama.com/api/chat)
- [Generate API](https://docs.ollama.com/api/generate)
- [Embeddings API](https://docs.ollama.com/api/embed)
- [Local FAQ and server configuration](https://docs.ollama.com/faq)
- [Official Python library](https://github.com/ollama/ollama-python)
- [Official JavaScript library](https://github.com/ollama/ollama-js)
- [Ollama model library](https://ollama.com/library)
