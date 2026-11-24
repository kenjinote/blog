---
title: "使用 Ollama 运行本地 LLM：安装、REST API 与 Python"
slug: "ollama-local-llm-api-guide"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "programming", "api"]
tags: ["Ollama", "Local LLM", "Python", "Node.js"]
date: "2026-09-11T02:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

## 安装 Ollama 并准备模型

从官方页面下载适用于 Windows、macOS 或 Linux 的 Ollama。在 Windows 和 macOS 上启动应用；在 Linux 上按照官方步骤安装，如果服务尚未运行则启动它。以下命令会下载并运行指定模型。模型供应和下载大小可能变化，请先查看模型库。

```bash
ollama pull gemma4:e2b
ollama run gemma4:e2b
```

模型启动后，可在另一个终端使用这些命令查看已下载的模型及其当前运行位置。模型文件占用磁盘空间；推理还需要与模型和上下文长度相匹配的 RAM 或 GPU 显存。

```bash
ollama list
ollama ps
```

## 调用聊天 REST API

本地 HTTP API 通常位于 `http://localhost:11434`。`/api/chat` 接收由消息组成的对话历史，默认以流式方式返回。示例将 `stream` 设为 `false` 以获得完整 JSON 响应，并通过 `format` 请求 JSON 输出。

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "gemma4:e2b",
  "messages": [
    {"role": "user", "content": "Explain what a REST API is in one sentence."}
  ],
  "stream": false,
}'
```

在 Windows PowerShell 中，`curl` 可能是其他命令的别名；此时请使用 `curl.exe`。

回答文本位于 `message.content`。将 `stream` 设为 `true` 或省略该字段即可逐段接收响应。没有对话历史的单条提示可使用 `/api/generate`；需要向量时，配合嵌入模型使用 `/api/embed`。

## 在 Python 中调用 Ollama

官方 Python 库会处理 HTTP 请求和响应对象。请先启动 Ollama 服务并下载模型。

```bash
python -m pip install ollama
```

```python
from ollama import chat

response = chat(
    model="gemma4:e2b",
    messages=[{"role": "user", "content": "用一句话解释什么是 REST API。"}],
    stream=False,
)
print(response.message.content)
```

如需逐段输出，请设置 `stream=True` 并遍历返回的内容块。官方库还提供用于异步应用的 `AsyncClient`。

## 在 Node.js 中调用 Ollama

在 Node.js 项目中安装官方 JavaScript 软件包。

```bash
npm install ollama
```

```javascript
import ollama from 'ollama';

const response = await ollama.chat({
  model: 'gemma4:e2b',
  messages: [{ role: 'user', content: '用一句话解释什么是 REST API。' }],
  stream: false,
});
console.log(response.message.content);
```

## 嵌入与检索

嵌入 API 会将文本转换为向量。基本 RAG 流程会将向量存入索引、检索相关段落，并把它们加入聊天提示；嵌入本身不会生成答案。

```bash
ollama pull embeddinggemma
curl http://localhost:11434/api/embed -d '{
  "model": "embeddinggemma",
  "input": "用一句话解释什么是 REST API。"
}'
```

响应中包含 `embeddings` 数组。请根据应用的语言、数据和许可要求选择嵌入模型及向量索引。

## 测量生成速度

响应中包含模型加载、提示词评估、生成耗时以及生成的 token 数。`eval_duration` 是生成阶段的纳秒耗时，不是端到端延迟，也不包含提示词处理和模型加载。可用下式估算生成速度：

$$
\text{tokens/sec} = \frac{\text{eval\_count}}{\text{eval\_duration} / 10^9}
$$

使用 `load_duration` 查看模型加载时间，使用 `prompt_eval_duration` 查看未缓存提示词的评估时间。请在相同模型、上下文和硬件条件下比较；吞吐量本身不能说明回答质量或端到端延迟。

## 估算内存用量

参数数量和量化位数可用于粗略估算权重存储的下限。4-bit 的 8B 模型仅权重大约需要 4 GB（十进制，约 3.73 GiB）。这不是完整内存需求：量化元数据、KV 缓存、上下文长度、运行时和其他应用还会占用内存。

$$
\text{weight bytes} \approx \frac{\text{parameter count} \times \text{bits per weight}}{8}
$$

使用 `ollama ps` 查看模型运行在 GPU、CPU 还是两者之间。实际分配取决于可用硬件和运行时支持。

## 隐私、网络访问与许可

请区分纯本地使用、云端模型和联网应用。发送敏感数据前，先确认所选模型、工具和网络路径。如果要让 API 可从局域网或互联网访问，请使用身份验证、防火墙等访问控制，不要直接暴露端口。还应检查每个模型的许可。

Ollama 将模型下载、本地推理和应用接入集中在一个工具中。本文命令和 API 示例是根据官方文档整理的基础用法。请核对具体模型的功能和要求，再按设备情况调整。

## 官方资料

- [Ollama Quickstart](https://docs.ollama.com/quickstart)
- [Chat API](https://docs.ollama.com/api/chat)
- [Generate API](https://docs.ollama.com/api/generate)
- [Embeddings API](https://docs.ollama.com/api/embed)
- [Local FAQ and server configuration](https://docs.ollama.com/faq)
- [Official Python library](https://github.com/ollama/ollama-python)
- [Official JavaScript library](https://github.com/ollama/ollama-js)
- [Ollama model library](https://ollama.com/library)
