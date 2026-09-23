---
title: "Technologie réseau : Explication technique du P2P (Peer-to-Peer) - La puissance des systèmes distribués"
description: "Nous expliquons le mécanisme et l'histoire des réseaux P2P, ainsi que la puissance des systèmes distribués."
slug: "history-of-p2p"
date: "2026-09-23T04:00:00+09:00"
image: "eyecatch.jpg"
categories:
  - Network
tags:
  - P2P
  - Decentralized
---

# Explication technique du P2P (Peer-to-Peer)

Le peer-to-peer (P2P), contrairement au modèle client-serveur, est une architecture réseau dans laquelle chaque nœud (pair) communique sur un pied d'égalité.

## Aperçu

Dans un réseau P2P, chaque nœud agit à la fois comme client et comme serveur. Cela élimine les points de défaillance uniques (SPOF) et améliore la disponibilité globale du système.

```mermaid
graph TD;
    A["Node A (Peer)"] <--> B["Node B (Peer)"];
    B <--> C["Node C (Peer)"];
    C <--> A;
    C <--> D["Node D (Peer)"];
```

## Modélisation mathématique

La disponibilité des ressources dans un réseau P2P augmente de manière évolutive avec le nombre de nœuds $N$. La bande passante totale $B_{total}$ est exprimée comme suit :

$$ B_{total} = \sum_{i=1}^{N} b_i $$

Où $b_i$ est la bande passante fournie par chaque nœud.
