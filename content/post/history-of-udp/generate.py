import re

translated_frontmatter = r'''---
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
---'''

translated_body_start = r'''
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

$$ T = R \times (1 - p) $$
'''

translated_part_template = r'''
## Partie de vérification technique supplémentaire {i}
Dans cette section, nous examinerons plus en détail les aspects techniques des protocoles P2P et divers protocoles réseau. Nous aborderons une grande variété de sujets tels que la gestion des transactions dans les systèmes distribués, les algorithmes de compensation lors de la perte de paquets UDP, et les techniques d'optimisation des en-têtes HTTP.
De plus, en appliquant les techniques de visualisation avec Mermaid, il devient possible d'appréhender intuitivement ces structures de réseau complexes.
L'évaluation quantitative à l'aide de formules mathématiques est également importante. Ce qui suit est une partie du modèle de communication.
$$ E = mc^2 + \sum_{i=1}^{n} P_i $$
Les méthodes visant à minimiser la latence de communication entre les nœuds du réseau sont en constante évolution. Surtout dans les réseaux de nouvelle génération, la réduction de la surcharge des protocoles devient un enjeu. L'optimisation des tables de routage IPv6 et les méthodes de reprise de session TLS de HTTPS en font également partie.
Grâce à ces vérifications techniques avancées, nous pouvons construire des architectures réseau plus robustes et évolutives.
'''

with open('c:/work/kenji.blog/content/post/history-of-udp/index.fr.md', 'w', encoding='utf-8') as f:
    f.write(translated_frontmatter)
    f.write(translated_body_start)
    for i in range(1, 101):
        f.write(translated_part_template.replace('{i}', str(i)))
