---
title: "網路技術：HTTP技術解說 - 支撐Web的無狀態協定"
description: "解說HTTP的機制與歷史，以及支撐Web的無狀態協定。"
slug: "history-of-http"
date: "2026-09-23T04:00:00+09:00"
image: "eyecatch.jpg"
categories:
  - Network
tags:
  - HTTP
  - Web
---

# HTTP技術解說

Hypertext Transfer Protocol (HTTP) 是作為Web基礎的通訊協定。

## 無狀態設計

HTTP是無狀態（Stateless）協定。每個請求都會被獨立處理。

```mermaid
graph LR;
    C["Client (Web Browser)"] -- "GET /index.html (HTTP/1.1)" --> S["Server (Web Server)"];
    S -- "200 OK (HTML Content)" --> C;
```

## 效能考察

在HTTP/2與HTTP/3中，透過多工（Multiplexing）減輕了來回通訊延遲（RTT）的影響。頁面的載入時間可以使用以下模型表示：

$$ T_{load} = T_{DNS} + T_{TCP} + T_{TLS} + \sum_{i=1}^{N} \left( \frac{S_i}{B} + RTT \right) $$

透過多工，後半部的 $\sum$ 部分可以被平行處理，從而大幅縮短時間。
