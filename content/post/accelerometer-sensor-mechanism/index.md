---
title: "加速度センサーの仕組み：重力・傾き・動きを測るMEMS"
description: "MEMS加速度センサーの可動質量とバネ、静電容量・ピエゾ抵抗による検出、重力と直線加速度を区別する際の限界を解説します。"
date: "2026-10-01T21:47:14+09:00"
lastmod: 2026-11-23
slug: "accelerometer-sensor-mechanism"
categories: ["technology", "hardware"]
tags: ["tech", "sensor", "mems", "hardware"]
image: "eyecatch.jpg"
draft: false
---

## 加速度センサーが測るもの

加速度は速度の変化率です。ニュートンの運動方程式 $F=ma$ は、質量 $m$ の物体に働く合力 $F$ と加速度 $a$ の関係を表します。加速度センサーは、内部の小さな質量に作用する**比力（specific force）**を測り、加速度に対応する値を出力します。軸の向きや符号は製品ごとの規約に従います。

ここでいう比力は、重力そのものを直接測った値とは異なります。机の上に静止しているスマートフォンでは、重力を支える机からの力があるため、センサーは重力加速度と同程度、約 $1g$（標準重力加速度は $9.80665\,\mathrm{m/s^2}$）を示します。自由落下中は支持力がほぼなくなり、理想的には加速度計の出力は $0g$ に近づきます。

## 重力から傾きを推定する

端末が静止、または十分ゆっくり動いているときは、重力ベクトルが3軸にどう投影されるかから傾きを推定できます。ただし、加速度計だけでは重力による成分と端末の直線運動による成分を区別できません。移動中に生じる加速や振動は傾きの推定を乱します。スマートフォンなどでは、用途に応じてジャイロスコープやフィルタを組み合わせ、姿勢を推定します。推定精度は動きやアルゴリズムに依存します。

## MEMSの可動質量とバネ

多くのMEMS加速度センサーは、微小な**可動質量（proof mass）**をバネ状の支持部でつり下げた構造を使います。チップが加速すると可動質量は慣性によって外枠に対してずれ、バネが変形します。その相対変位を電気信号に変換し、回路で補正・処理して出力します。実際の設計には減衰や複数の構造があり、単純な「重りとバネ」は基本モデルです。

## 変位を検出する方法

### 静電容量方式

静電容量方式では、可動部と固定電極の間の静電容量変化を読み取ります。理想的な平行板コンデンサーでは $C=\varepsilon A/d$（誘電率 $\varepsilon$、重なり面積 $A$、電極間隔 $d$）です。実際のMEMSには櫛歯電極など異なる形状があり、変位に応じて電極間隔や重なり面積を変化させます。専用回路が小さな容量差を電気信号に変換し、製品によってはデジタル値として出力します。

### ピエゾ抵抗方式

ピエゾ抵抗方式では、加速度で梁などが変形したときに生じる電気抵抗の変化を検出します。抵抗をブリッジ回路に組み込んで電圧として読み取る設計があります。高衝撃を測る試験用センサーなどに使われますが、適した方式は測定範囲、帯域、温度、消費電力などの要件で異なります。すべての製品に当てはまる優劣はありません。

## どこで使われるか

加速度センサーは、端末の画面回転、ジェスチャーや歩数の推定、ゲーム・VR機器の動き検出、ドローンや機器の姿勢制御などに使われます。自動車の衝突検知にも加速度計が利用されますが、エアバッグの展開はセンサー単体ではなく、車両ごとに検証された制御システムが判断します。歩数や睡眠などの機能も、加速度データを使ったソフトウェア上の推定です。

### 参考資料

- [STMicroelectronics：MEMSセンサーの仕組み](https://www.st.com/content/st_com/en/support/learning/essentials-and-insights/mems/how-does-a-mems-sensor-work.html)
- [Analog Devices：加速度計による傾斜計測](https://www.analog.com/en/resources/app-notes/an-1057.html)
- [Bosch Sensortec：センサーフュージョン](https://www.bosch-sensortec.com/en/software-tools/software/sensor-fusion-software-bsx)
- [Analog Devices：加速度計の検出・静電容量方式](https://www.analog.com/en/resources/technical-articles/accelerometer-and-gyroscopes-sensors-operation-sensing-and-applications.html)
- [Analog Devices：加速度計と自動車の衝突検知](https://www.analog.com/en/resources/product-faqs/adxl213.html)

加速度計はチップの向きに沿った加速度情報を測るセンサーです。傾きや移動状態は、その出力と他のセンサー情報をソフトウェアで解釈して得られます。

[PCB Piezotronics: Piezoresistive shock accelerometers](https://www.pcb.com/sensors-for-test-measurement/accelerometers/piezoresistive-shock)
