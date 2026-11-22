---
title: "加速度計如何運作：MEMS、重力與傾斜測量"
description: "介紹 MEMS 加速度計中的懸置質量塊、電容式與壓阻式檢測，以及單靠加速度計難以區分重力與直線運動的原因。"
date: "2026-10-01T21:47:14+09:00"
lastmod: 2026-11-23
slug: "accelerometer-sensor-mechanism"
categories: ["technology", "hardware"]
tags: ["tech", "sensor", "mems", "hardware"]
image: "eyecatch.jpg"
draft: false
---

## 加速度計測量什麼

加速度是速度隨時間的變化率。牛頓第二運動定律 $F=ma$ 描述作用於質量 $m$ 的合力 $F$ 與加速度 $a$ 之間的關係。加速度計感測作用在內部微小質量塊上的**比力（specific force）**，並輸出與加速度相關的數值。各軸方向與正負號取決於元件的規約。

比力並不是直接測量重力本身。手機靜置在桌面上時受到桌面的支撐力，因此加速度計大約顯示 $1g$（標準重力加速度為 $9.80665\,\mathrm{m/s^2}$）。自由落體時幾乎沒有支撐力，理想加速度計的讀值會接近 $0g$。

## 根據重力估算傾斜

裝置靜止或移動得夠慢時，可根據重力向量在三個軸上的投影估算傾斜角。不過，單靠加速度計無法區分重力與裝置直線運動所產生的加速度，因此移動和震動可能干擾傾斜估算。手機等裝置可結合陀螺儀和濾波演算法估算姿態；準確度取決於運動狀態和演算法。

## MEMS 中的質量塊與彈簧

許多 MEMS 加速度計以類似彈簧的支撐結構懸置微小的**檢測質量塊（proof mass）**。晶片加速時，質量塊因慣性而相對外框移動，使支撐結構變形。感測器將這種相對位移轉換成電訊號，再由晶片內電路調理與處理。實際元件還包含阻尼等更複雜結構，「彈簧上的質量塊」只是基本模型。

## 將位移轉換成訊號

### 電容式檢測

電容式感測器偵測活動結構與固定電極之間的電容變化。理想平行板電容器滿足 $C=\varepsilon A/d$，其中 $\varepsilon$ 是介電常數、$A$ 是重疊面積、$d$ 是間距。MEMS 也會使用交錯梳齒電極等結構，運動可能改變電極間距或重疊面積。專用電路會將微小的電容變化轉成訊號；部分元件提供數位輸出。

### 壓阻式檢測

壓阻式感測器偵測加速度使樑或其他結構變形時產生的電阻變化。電橋電路可將變化轉換成電壓。部分用於衝擊測試的感測器採用此方法。適用方案取決於量程、頻寬、溫度、功耗等需求，沒有一種方式在所有情況下都較好。

## 應用

加速度計可用於螢幕旋轉、手勢和步數估算、遊戲與 VR 的動作偵測，以及無人機和其他設備的姿態控制。汽車碰撞偵測也會使用加速度計，但安全氣囊是否展開由針對特定車款驗證過的控制系統判斷，不是由單一感測器決定。步數和睡眠階段等功能同樣是軟體根據包括加速度資料在內的資訊所做的估算。

### 參考資料

- [STMicroelectronics：MEMS 感測器的運作方式](https://www.st.com/content/st_com/en/support/learning/essentials-and-insights/mems/how-does-a-mems-sensor-work.html)
- [Analog Devices：使用加速度計測量傾斜](https://www.analog.com/en/resources/app-notes/an-1057.html)
- [Bosch Sensortec：感測器融合](https://www.bosch-sensortec.com/en/software-tools/software/sensor-fusion-software-bsx)
- [Analog Devices：加速度計的電容式檢測](https://www.analog.com/en/resources/technical-articles/accelerometer-and-gyroscopes-sensors-operation-sensing-and-applications.html)
- [Analog Devices：加速度計與汽車碰撞偵測](https://www.analog.com/en/resources/product-faqs/adxl213.html)

加速度計測量沿感測器各軸的加速度相關資料。傾斜和運動狀態由軟體結合這些資料及其他感測器資訊推算而得。

[PCB Piezotronics: Piezoresistive shock accelerometers](https://www.pcb.com/sensors-for-test-measurement/accelerometers/piezoresistive-shock)
