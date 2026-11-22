---
title: "加速度计如何工作：MEMS、重力与倾斜测量"
description: "介绍MEMS加速度计中的悬置质量块、电容式和压阻式检测，以及单靠加速度计难以区分重力与直线运动的原因。"
date: "2026-10-01T21:47:14+09:00"
lastmod: 2026-11-23
slug: "accelerometer-sensor-mechanism"
categories: ["technology", "hardware"]
tags: ["tech", "sensor", "mems", "hardware"]
image: "eyecatch.jpg"
draft: false
---

## 加速度计测量什么

加速度是速度随时间的变化率。牛顿第二定律 $F=ma$ 描述了作用于质量 $m$ 的合力 $F$ 与加速度 $a$ 的关系。加速度计感知作用在内部微小质量块上的**比力（specific force）**，并输出与加速度相关的数值。各轴方向和正负号取决于具体器件的约定。

比力并不是直接测量重力本身。手机静置在桌面上时受到桌面的支撑力，因此加速度计大约显示 $1g$（标准重力加速度为 $9.80665\,\mathrm{m/s^2}$）。自由落体时几乎没有支撑力，理想加速度计的读数会接近 $0g$。

## 根据重力估算倾斜

设备静止或运动足够缓慢时，可以根据重力向量在三个轴上的投影估算倾斜角。但仅靠加速度计无法区分重力与设备直线运动产生的加速度，因此运动和振动会干扰倾斜估计。手机等设备可结合陀螺仪和滤波算法估算姿态；准确度取决于运动情况和算法。

## MEMS中的质量块和弹簧

许多MEMS加速度计用类似弹簧的支撑结构悬置微小的**检测质量块（proof mass）**。芯片加速时，质量块因惯性相对于外框移动，使支撑结构发生形变。传感器将这种相对位移转换成电信号，再由芯片内电路调理和处理。真实器件还包含阻尼等更复杂结构，“弹簧上的质量块”只是基础模型。

## 将位移转换为信号

### 电容式检测

电容式传感器检测活动结构与固定电极之间的电容变化。理想平行板电容器满足 $C=\varepsilon A/d$，其中 $\varepsilon$ 是介电常数，$A$ 是重叠面积，$d$ 是间距。MEMS也会采用交错梳齿电极等结构，运动可能改变电极间距或重叠面积。专用电路将微小电容变化转换成信号；部分器件提供数字输出。

### 压阻式检测

压阻式传感器检测加速度使梁或其他结构形变时产生的电阻变化。电桥电路可将变化转换为电压。部分用于冲击测试的传感器采用这种方法。适用方案取决于量程、带宽、温度、功耗等要求，没有一种方法在所有场景下都更好。

## 应用场景

加速度计可用于屏幕旋转、手势和步数估计、游戏与VR的运动检测，以及无人机和其他设备的姿态控制。汽车碰撞检测也会使用加速度计，但安全气囊是否展开由针对具体车型验证过的控制系统决定，并非由单个传感器决定。步数和睡眠阶段等功能也是软件根据包括加速度数据在内的信息作出的估算。

### 参考资料

- [STMicroelectronics：MEMS传感器的工作原理](https://www.st.com/content/st_com/en/support/learning/essentials-and-insights/mems/how-does-a-mems-sensor-work.html)
- [Analog Devices：使用加速度计测量倾斜](https://www.analog.com/en/resources/app-notes/an-1057.html)
- [Bosch Sensortec：传感器融合](https://www.bosch-sensortec.com/en/software-tools/software/sensor-fusion-software-bsx)
- [Analog Devices：加速度计的电容式检测](https://www.analog.com/en/resources/technical-articles/accelerometer-and-gyroscopes-sensors-operation-sensing-and-applications.html)
- [Analog Devices：加速度计与汽车碰撞检测](https://www.analog.com/en/resources/product-faqs/adxl213.html)

加速度计测量沿传感器轴向的加速度相关数据。倾斜和运动状态由软件结合这些数据及其他传感器信息推算得出。

[PCB Piezotronics: Piezoresistive shock accelerometers](https://www.pcb.com/sensors-for-test-measurement/accelerometers/piezoresistive-shock)
