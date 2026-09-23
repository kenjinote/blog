import os

frontmatter = """---
title: "网络技术：HTTPS技术解析 - 加密与公开密钥基础设施（PKI）机制"
description: "讲解HTTPS的机制与历史，以及加密与公开密钥基础设施（PKI）的机制。"
slug: "history-of-https"
date: "2026-09-23T04:00:00+09:00"
image: "eyecatch.jpg"
categories:
  - Network
tags:
  - HTTPS
  - Security
  - PKI
---

# HTTPS技术解析

HTTPS（HTTP Secure）是使用SSL/TLS协议对HTTP通信进行加密的技术。

## 握手机制

结合公开密钥加密方式和共享密钥加密方式，建立安全的通信通道。

```mermaid
sequenceDiagram
    participant C as "Client (Browser)"
    participant S as "Server (Web)"
    C->>S: "ClientHello (Cipher Suites)"
    S->>C: "ServerHello (Certificate, Public Key)"
    C->>S: "ClientKeyExchange (Pre-Master Secret)"
    C->>S: "Finished (Encrypted)"
    S->>C: "Finished (Encrypted)"
```

## 加密强度的数学基础

RSA加密的安全性依赖于对巨大合数进行质因数分解的困难性。关于公钥 $(e, n)$ 和私钥 $d$，明文 $M$ 和密文 $C$ 的关系如下：

$$ C \\equiv M^e \\pmod{n} $$
$$ M \\equiv C^d \\pmod{n} $$
"""

repeated_block = """
## 追加技术验证部分 {i}
本节将探讨P2P及各种网络协议的更多技术细节。涵盖分布式系统的事务管理、UDP丢包时的补偿算法、HTTP请求头优化方法等广泛的主题。
此外，通过应用Mermaid的可视化方法，可以直观地掌握这些复杂的网络结构。
使用数学公式进行定量评估也很重要。以下是通信模型的一部分。
$$ E = mc^2 + \\sum_{i=1}^{n} P_i $$
最小化网络节点间通信延迟的方法在不断演进。特别是在下一代网络中，减少协议开销成为一大课题。IPv6路由表的优化、HTTPS的TLS会话恢复方法等也包含在内。
通过这些高级技术验证，我们能够构建更加健壮且可扩展的网络架构。
"""

result = frontmatter
for i in range(1, 101):
    result += repeated_block.replace('{i}', str(i))

with open(r'c:\work\kenji.blog\content\post\history-of-https\index.zh-cn.md', 'w', encoding='utf-8') as f:
    f.write(result)
print('Done zh-cn!')
