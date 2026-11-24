---
title: "OllamaでローカルLLMを動かす：導入・REST API・Python／Node.js連携"
slug: "ollama-local-llm-api-guide"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "programming", "api"]
tags: ["Ollama", "Local LLM", "Python", "Node.js"]
date: "2026-09-11T02:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

## インストールとモデルの準備

公式のダウンロードページからWindows、macOS、Linux向けのOllamaを入手します。WindowsとmacOSではアプリを起動し、Linuxでは公式手順に従ってインストール後にサーバーを起動します。以下はモデル名を明示して取得・起動する例です。モデルの提供状況やサイズは変わるため、実行前にモデルライブラリを確認してください。

```bash
ollama pull gemma4:e2b
ollama run gemma4:e2b
```

モデルが起動したら、別のターミナルで一覧と実行状況を確認できます。モデルデータはディスク容量を使い、実行時はモデルとコンテキストに応じたRAMやGPUメモリが必要です。

```bash
ollama list
ollama ps
```

## REST APIでチャットする

通常、ローカルHTTP APIは `http://localhost:11434` で利用できます。`/api/chat` は会話履歴をメッセージ配列で受け取り、既定では応答をストリーミングします。次の例は一括応答にするため `stream: false` を指定し、JSONを返す `format` も指定しています。

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "gemma4:e2b",
  "messages": [
    {"role": "user", "content": "Explain what a REST API is in one sentence."}
  ],
  "stream": false,
}'
```

Windows PowerShellでは `curl` が別コマンドの別名になっている場合があります。その場合は `curl.exe` と入力してください。

応答本文は `message.content` に入ります。`stream: true` を指定するか省略すると、応答を分割して受け取れます。会話履歴を使わない単一プロンプトには `/api/generate`、ベクトルが必要な場合は埋め込みモデルと `/api/embed` を使います。

## Pythonから呼び出す

公式Pythonライブラリを使うと、HTTP本文やストリームの解析を自分で書かずにチャットを呼び出せます。先にOllamaサーバーを起動し、モデルを取得しておきます。

```bash
python -m pip install ollama
```

```python
from ollama import chat

response = chat(
    model="gemma4:e2b",
    messages=[{"role": "user", "content": "REST APIとは何かを一文で説明してください。"}],
    stream=False,
)
print(response.message.content)
```

逐次出力するには `stream=True` を指定し、返されたチャンクを順に読み取ります。非同期アプリケーションでは公式ライブラリの `AsyncClient` も利用できます。

## Node.jsから呼び出す

公式JavaScriptライブラリを使うには、Node.jsプロジェクトにパッケージを追加します。

```bash
npm install ollama
```

```javascript
import ollama from 'ollama';

const response = await ollama.chat({
  model: 'gemma4:e2b',
  messages: [{ role: 'user', content: 'REST APIとは何かを一文で説明してください。' }],
  stream: false,
});
console.log(response.message.content);
```

## 埋め込みと検索

埋め込みAPIは文章をベクトルに変換します。ベクトルを検索用インデックスに保存し、関連する文章をチャットのコンテキストに加えるのがRAGの基本形です。埋め込みだけで回答が生成されるわけではありません。

```bash
ollama pull embeddinggemma
curl http://localhost:11434/api/embed -d '{
  "model": "embeddinggemma",
  "input": "REST APIとは何かを一文で説明してください。"
}'
```

応答には `embeddings` 配列が含まれます。利用する言語、データ、ライセンス条件に合わせて埋め込みモデルとベクトル検索の仕組みを選んでください。

## 生成速度を計測する

応答にはモデルのロード時間、プロンプト評価時間、生成時間、生成トークン数が含まれます。`eval_duration` は生成部分の時間（ナノ秒）で、プロンプト処理やモデル読み込みを含む総待ち時間ではありません。生成速度の目安は次の式で求められます。

$$
\text{tokens/sec} = \frac{\text{eval\_count}}{\text{eval\_duration} / 10^9}
$$

モデルのロードには `load_duration`、キャッシュされていないプロンプトの評価には `prompt_eval_duration` を参照します。同じモデル、コンテキスト、ハードウェアで比較してください。生成速度だけでは回答品質や全体の待ち時間は分かりません。

## メモリ使用量を見積もる

パラメーター数と量子化ビット数から、重みだけの理論的な容量を概算できます。8B・4-bitなら約4GB（十進単位、約3.73GiB）です。これは実際の必要メモリ量ではありません。量子化メタデータ、KVキャッシュ、コンテキスト長、ランタイム、他のアプリも追加のメモリを使います。

$$
\text{weight bytes} \approx \frac{\text{parameter count} \times \text{bits per weight}}{8}
$$

`ollama ps` でモデルがGPU、CPU、または両方に配置されているかを確認できます。実際の配置は使用可能なハードウェアとランタイムの対応状況で変わります。

## プライバシー、公開範囲、ライセンス

Ollamaをローカルモデルだけで使う場合と、クラウドモデルや連携アプリを使う場合を区別してください。機密データを扱う前に、選択したモデル、ツール、通信経路を確認します。APIをLANやインターネットから使えるように設定する場合は、公開ポートをそのまま露出させず、認証とファイアウォールなどのアクセス制御を設けてください。モデルごとのライセンスも確認が必要です。

Ollamaは、ローカルモデルの取得、実行、アプリ連携をひとつのツールで行える環境です。この記事のコマンドとAPI例は公式資料を参照した基本形です。モデル固有の機能や要件を確認し、使用するモデルと実行環境に合わせて調整してください。

## 公式資料

- [Ollama Quickstart](https://docs.ollama.com/quickstart)
- [Chat API](https://docs.ollama.com/api/chat)
- [Generate API](https://docs.ollama.com/api/generate)
- [Embeddings API](https://docs.ollama.com/api/embed)
- [Local FAQ and server configuration](https://docs.ollama.com/faq)
- [Official Python library](https://github.com/ollama/ollama-python)
- [Official JavaScript library](https://github.com/ollama/ollama-js)
- [Ollama model library](https://ollama.com/library)
