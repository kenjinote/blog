---
title: "Technologie réseau : Explication technique d'UDP - Poursuivre la vitesse de la communication sans connexion"
description: "Explication du fonctionnement et de l'histoire du protocole UDP, ainsi que de la communication sans connexion qui privilégie la vitesse."
slug: "history-of-udp"
date: "2026-09-23T04:00:00+09:00"
image: "eyecatch.jpg"
categories:
  - Network
tags:
  - UDP
  - Protocol
---
# Explication technique d'UDP

User Datagram Protocol (UDP) est l'un des membres principaux de la suite de protocoles Internet.

## La force du mode sans connexion

UDP ne procède pas à un handshake (poignée de main) comme TCP et transmet les données telles quelles. Cela permet de minimiser la latence.

```mermaid
sequenceDiagram
    participant S as "Sender (Application)"
    participant R as "Receiver (Application)"
    S->>R: "Datagram 1 (No ACK needed)"
    S->>R: "Datagram 2 (No ACK needed)"
    S->>R: "Datagram 3 (Lost)"
    S->>R: "Datagram 4 (No ACK needed)"
```

## Modélisation du taux de transmission

Si le taux de perte de paquets est $p$ et le taux de transmission est $R$, le débit effectif $T$ est approximé comme suit (dans le cas d'UDP, puisqu'il n'y a pas de contrôle de retransmission, ils sont perdus tels quels).

$$ T = R 	imes (1 - p) $$
