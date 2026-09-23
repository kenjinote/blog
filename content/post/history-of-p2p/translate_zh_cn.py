import re

def translate():
    with open(r'c:\work\kenji.blog\content\post\history-of-p2p\index.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # Frontmatter
    content = content.replace(
        'title: "ネットワーク技術: P2P(ピアツーピア)の技術解説 - 分散型システムの力"',
        'title: "网络技术：P2P（点对点）技术解析 - 分布式系统的力量"'
    )
    content = content.replace(
        'description: "P2Pネットワークの仕組みと歴史、分散型システムの力について解説します。"',
        'description: "解析P2P网络的机制与历史，以及分布式系统的力量。"'
    )
    
    # Body
    content = content.replace(
        '# P2P(ピアツーピア)の技術解説',
        '# P2P（点对点）技术解析'
    )
    
    content = content.replace(
        'ピアツーピア（Peer-to-Peer、P2P）は、クライアントサーバーモデルとは異なり、各ノード（ピア）が対等な関係で通信を行うネットワークアーキテクチャです。',
        '点对点（Peer-to-Peer，P2P）与客户端-服务器模型不同，是一种各节点（Peer）以对等关系进行通信的网络架构。'
    )

    content = content.replace(
        '## 概要',
        '## 概述'
    )

    content = content.replace(
        'P2Pネットワークでは、各ノードがクライアントとしてもサーバーとしても機能します。これにより、単一障害点（SPOF）がなくなり、システム全体の可用性が向上します。',
        '在P2P网络中，每个节点既可以作为客户端也可以作为服务器。这消除了单点故障（SPOF），从而提高了整个系统的可用性。'
    )

    content = content.replace(
        '## 数学的モデリング',
        '## 数学建模'
    )

    content = content.replace(
        'P2Pネットワークにおけるリソースの可用性は、ノード数 $N$ に対してスケーラブルに増加します。総帯域幅 $B_{total}$ は次のように表されます。',
        'P2P网络中资源的可用性随着节点数 $N$ 的增加而呈可扩展性增长。总带宽 $B_{total}$ 表示如下：'
    )

    content = content.replace(
        'ここで、$b_i$ は各ノードが提供する帯域幅です。',
        '在这里，$b_i$ 是每个节点提供的带宽。'
    )

    # Repeating sections
    content = re.sub(
        r'## 追加技術検証パート (\d+)',
        r'## 附加技术验证部分 \1',
        content
    )

    content = content.replace(
        '本セクションでは、P2Pおよび各種ネットワークプロトコルの更なる技術的詳細について検証する。分散システムのトランザクション管理や、UDPのパケットロス時の補償アルゴリズム、HTTPヘッダの最適化手法など、多岐にわたるトピックを扱う。',
        '本节将探讨P2P及各种网络协议的进一步技术细节。涵盖分布式系统的事务管理、UDP丢包时的补偿算法、HTTP头优化方法等广泛的主题。'
    )

    content = content.replace(
        'また、Mermaidによる可視化手法を応用することで、これら複雑なネットワーク構造を直感的に把握することが可能となる。',
        '此外，通过应用Mermaid进行可视化，可以直观地掌握这些复杂的网络结构。'
    )

    content = content.replace(
        '数式を用いた定量的評価も重要である。以下は通信モデルの一部である。',
        '使用数学公式进行定量评估也很重要。以下是通信模型的一部分。'
    )

    content = content.replace(
        'ネットワークノード間の通信遅延を最小化するための手法は常に進化している。特に次世代ネットワークにおいては、プロトコルのオーバーヘッド削減が課題となる。IPv6のルーティングテーブルの最適化や、HTTPSのTLSセッション再開の手法もこれに含まれる。',
        '最小化网络节点间通信延迟的方法在不断演进。特别是在下一代网络中，减少协议开销将成为一项挑战。IPv6路由表的优化、HTTPS的TLS会话恢复技术也包含在内。'
    )

    content = content.replace(
        'これらの高度な技術検証を通じて、我々はより堅牢でスケーラブルなネットワークアーキテクチャを構築することができる。',
        '通过这些高级技术验证，我们能够构建更加健壮且可扩展的网络架构。'
    )

    # Mermaid nodes check.
    def repl_mermaid(m):
        block = m.group(0)
        block = re.sub(r'([A-Za-z0-9_]+)\[(?!")([^\]]+)\]', r'\1["\2"]', block)
        return block

    content = re.sub(r'```mermaid.*?```', repl_mermaid, content, flags=re.DOTALL)
    
    with open(r'c:\work\kenji.blog\content\post\history-of-p2p\index.zh-cn.md', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    translate()
