---
title: "Executar LLMs locais com Ollama: instalação, API REST e Python"
slug: "ollama-local-llm-api-guide"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "programming", "api"]
tags: ["Ollama", "Local LLM", "Python", "Node.js"]
date: "2026-09-11T02:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

## Instalar o Ollama e preparar um modelo

Baixe o Ollama para Windows, macOS ou Linux na página oficial. Abra o aplicativo no Windows ou macOS; no Linux, siga a instalação oficial e inicie o servidor se ele ainda não estiver ativo. Estes comandos baixam e executam um modelo específico. Consulte a biblioteca antes, pois a disponibilidade e o tamanho do download podem mudar.

```bash
ollama pull gemma4:e2b
ollama run gemma4:e2b
```

Depois de iniciar um modelo, use estes comandos em outro terminal para ver os modelos baixados e onde estão sendo executados. Os arquivos ocupam espaço em disco; a inferência também precisa de RAM ou memória de GPU conforme o modelo e o tamanho do contexto.

```bash
ollama list
ollama ps
```

## Chamar a API REST de chat

A API HTTP local costuma estar disponível em `http://localhost:11434`. `/api/chat` recebe o histórico como uma lista de mensagens e transmite a resposta por padrão. Este exemplo define `stream: false` para uma resposta JSON completa e solicita a saída JSON com `format`.

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "gemma4:e2b",
  "messages": [
    {"role": "user", "content": "Explain what a REST API is in one sentence."}
  ],
  "stream": false,
}'
```

No Windows PowerShell, `curl` pode ser um alias de outro comando; nesse caso, use `curl.exe`.

O texto da resposta fica em `message.content`. Defina `stream` como `true` ou omita o campo para receber partes da resposta. Para um único prompt sem histórico, use `/api/generate`; para vetores, use `/api/embed` com um modelo de embeddings.

## Usar o Ollama com Python

A biblioteca oficial para Python cuida da requisição HTTP e dos objetos de resposta. Inicie o servidor do Ollama e baixe o modelo antes.

```bash
python -m pip install ollama
```

```python
from ollama import chat

response = chat(
    model="gemma4:e2b",
    messages=[{"role": "user", "content": "Explique em uma frase o que é uma API REST."}],
    stream=False,
)
print(response.message.content)
```

Para receber a saída gradualmente, defina `stream=True` e percorra os blocos retornados. A biblioteca oficial também oferece `AsyncClient` para aplicações assíncronas.

## Usar o Ollama com Node.js

Instale o pacote oficial de JavaScript no seu projeto Node.js.

```bash
npm install ollama
```

```javascript
import ollama from 'ollama';

const response = await ollama.chat({
  model: 'gemma4:e2b',
  messages: [{ role: 'user', content: 'Explique em uma frase o que é uma API REST.' }],
  stream: false,
});
console.log(response.message.content);
```

## Embeddings e busca

A API de embeddings transforma texto em vetores. Um fluxo RAG básico armazena os vetores em um índice, recupera trechos relevantes e os acrescenta ao prompt do chat; embeddings não geram respostas por conta própria.

```bash
ollama pull embeddinggemma
curl http://localhost:11434/api/embed -d '{
  "model": "embeddinggemma",
  "input": "Explique em uma frase o que é uma API REST."
}'
```

A resposta contém um vetor `embeddings`. Escolha o modelo de embeddings e o índice vetorial conforme o idioma, os dados e os requisitos de licença.

## Medir a velocidade de geração

A resposta informa os tempos de carregamento do modelo, avaliação do prompt e geração, além da quantidade de tokens gerados. `eval_duration` mede a geração em nanossegundos; não é a latência total e não inclui avaliação do prompt nem carregamento do modelo. Estime a taxa de tokens assim:

$$
\text{tokens/sec} = \frac{\text{eval\_count}}{\text{eval\_duration} / 10^9}
$$

Use `load_duration` para o carregamento do modelo e `prompt_eval_duration` para avaliar prompts fora do cache. Compare o mesmo modelo, contexto e hardware; a taxa de tokens, sozinha, não mede qualidade nem latência total.

## Estimar o uso de memória

A quantidade de parâmetros e os bits de quantização fornecem uma estimativa aproximada do mínimo para armazenar os pesos. Um modelo 8B em 4 bits usa cerca de 4 GB decimais (3,73 GiB) só para os pesos. Não é a necessidade total: metadados de quantização, cache KV, tamanho do contexto, runtime e outros aplicativos exigem memória adicional.

$$
\text{weight bytes} \approx \frac{\text{parameter count} \times \text{bits per weight}}{8}
$$

Use `ollama ps` para ver se o modelo está na GPU, na CPU ou dividido entre ambas. A distribuição real depende do hardware disponível e do suporte do runtime.

## Privacidade, acesso à rede e licenças

Diferencie o uso somente local de modelos na nuvem e aplicativos conectados. Antes de enviar dados confidenciais, confira o modelo, as ferramentas e o caminho de rede. Se tornar a API acessível na rede local ou na Internet, não exponha a porta sem controles como autenticação e firewall. Verifique também a licença de cada modelo.

O Ollama reúne download de modelos, inferência local e acesso por aplicativos. Os comandos e exemplos de API são padrões básicos da documentação oficial. Confira os recursos e requisitos de cada modelo e adapte-os ao seu computador.

## Referências oficiais

- [Ollama Quickstart](https://docs.ollama.com/quickstart)
- [Chat API](https://docs.ollama.com/api/chat)
- [Generate API](https://docs.ollama.com/api/generate)
- [Embeddings API](https://docs.ollama.com/api/embed)
- [Local FAQ and server configuration](https://docs.ollama.com/faq)
- [Official Python library](https://github.com/ollama/ollama-python)
- [Official JavaScript library](https://github.com/ollama/ollama-js)
- [Ollama model library](https://ollama.com/library)
