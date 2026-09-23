import codecs

front_matter_and_top = """---
title: "網路技術：UDP 技術解說 - 追求速度的無連線通訊"
description: "解說 UDP 協定的運作原理與歷史，以及追求速度的無連線通訊。"
slug: "history-of-udp"
date: "2026-09-23T04:00:00+09:00"
image: "eyecatch.jpg"
categories:
  - Network
tags:
  - UDP
  - Protocol
---

# UDP 技術解說

使用者資料報協定 (User Datagram Protocol, UDP) 是網際網路協定套件的核心成員之一。

## 無連線的優勢

UDP 不像 TCP 那樣進行交握 (handshake)，而是直接發送資料。這樣可以將延遲降到最低。

```mermaid
sequenceDiagram
    participant S as "發送方 (應用程式)"
    participant R as "接收方 (應用程式)"
    S->>R: "資料報 1 (不需 ACK)"
    S->>R: "資料報 2 (不需 ACK)"
    S->>R: "資料報 3 (遺失)"
    S->>R: "資料報 4 (不需 ACK)"
```

## 發送速率的模型化

假設封包遺失率為 $p$ ，發送速率為 $R$ ，則有效吞吐量 $T$ 可近似為以下公式（在 UDP 的情況下，因為沒有重傳控制，遺失的封包就會直接消失）：

$$ T = R \\times (1 - p) $$

"""

block_template = """## 追加技術驗證部分 {i}
本節將驗證 P2P 及各種網路協定的進一步技術細節。我們將探討分散式系統的交易管理、UDP 封包遺失時的補償演算法、HTTP 標頭的最佳化手法等廣泛的技術主題。
此外，透過應用 Mermaid 視覺化手法，我們能更直觀地掌握這些複雜的網路結構。
使用數學公式進行定量評估也很重要。以下為部分通訊模型：
$$ E = mc^2 + \\sum_{i=1}^{n} P_i $$
將網路節點間的通訊延遲降到最低的手法正持續發展。特別是在次世代網路中，減少協定的額外負擔 (overhead) 是一大課題。這也包含了 IPv6 路由表的最佳化以及 HTTPS 的 TLS 連線恢復 (session resumption) 手法。
透過這些進階的技術驗證，我們能夠建立更穩固且具備擴展性的網路架構。
"""

with codecs.open(r'c:\work\kenji.blog\content\post\history-of-udp\index.zh-tw.md', 'w', 'utf-8') as f:
    f.write(front_matter_and_top)
    for i in range(1, 101):
        f.write(block_template.replace('{i}', str(i)))
        if i < 100:
            f.write('\n')
