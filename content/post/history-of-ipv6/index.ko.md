---
title: "네트워크 기술: IPv4에서 IPv6로의 변화와 차세대 인터넷"
description: "IPv4에서 IPv6로의 변화와 차세대 인터넷 기술에 대해 설명합니다."
slug: "history-of-ipv6"
date: "2026-09-23T04:00:00+09:00"
image: "eyecatch.jpg"
categories:
  - Network
tags:
  - IPv6
  - Protocol
  - Internet
---

# IPv4에서 IPv6로의 변화

IPv6는 고갈된 IPv4 주소 공간을 확장하기 위해 설계된 차세대 인터넷 프로토콜입니다.

## 주소 공간의 확장

IPv6의 주소 길이는 128비트이며, 천문학적인 수의 주소를 제공합니다.

```mermaid
graph TD;
    V4["IPv4 (32-bit: ~4.3 Billion Addresses)"] --> Need["Address Exhaustion (NAT usage)"];
    Need --> V6["IPv6 (128-bit: ~3.4×10^38 Addresses)"];
```

## 수학적 표현

IPv6의 총 주소 수 $A_{IPv6}$는 2의 128승입니다.

$$ A_{IPv6} = 2^{128} pprox 3.4 \times 10^{38} $$

이로 인해 사실상 모든 활성 장치에 고유한 글로벌 IP 주소를 할당할 수 있게 됩니다.
