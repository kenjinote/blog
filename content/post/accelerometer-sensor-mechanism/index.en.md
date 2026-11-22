---
title: "How Accelerometers Work: MEMS, Gravity, Tilt, and Motion"
description: "See how a MEMS accelerometer uses a suspended proof mass, capacitive or piezoresistive sensing, and why gravity and linear motion can be difficult to separate."
date: "2026-10-01T21:47:14+09:00"
lastmod: 2026-11-23
slug: "accelerometer-sensor-mechanism"
categories: ["technology", "hardware"]
tags: ["tech", "sensor", "mems", "hardware"]
image: "eyecatch.jpg"
draft: false
---

## What an accelerometer measures

Acceleration is the rate of change of velocity. Newton’s second law, $F=ma$, relates the net force $F$ on a mass $m$ to its acceleration $a$. An accelerometer senses **specific force** acting on a tiny internal mass and reports a value corresponding to acceleration. Axis direction and sign conventions vary by device.

Specific force is not a direct measurement of gravity itself. A phone resting on a desk is supported by the desk, so its accelerometer reads roughly $1g$ (standard gravity is $9.80665\,\mathrm{m/s^2}$). In free fall, the supporting force is nearly absent and an ideal accelerometer approaches $0g$.

## Estimating tilt from gravity

When a device is stationary or moving slowly enough, tilt can be estimated from how the gravity vector projects onto its three axes. But an accelerometer alone cannot distinguish gravity from acceleration caused by the device’s linear motion. Acceleration and vibration while moving can therefore corrupt a tilt estimate. Phones and other devices may combine accelerometer data with a gyroscope and filtering to estimate orientation. Accuracy depends on motion and the algorithm.

## A MEMS proof mass and springs

Many MEMS accelerometers suspend a tiny **proof mass** from spring-like supports. When the chip accelerates, inertia makes the mass shift relative to the frame, deforming the supports. The sensor converts this relative displacement into an electrical signal; onboard circuitry conditions and processes it. Real devices include damping and more complex structures, so “a mass on a spring” is a basic model.

## Turning displacement into a signal

### Capacitive sensing

Capacitive sensors detect a change in capacitance between a moving structure and fixed electrodes. For an ideal parallel-plate capacitor, $C=\varepsilon A/d$, where $\varepsilon$ is permittivity, $A$ is the overlapping area, and $d$ is the gap. MEMS designs also use geometries such as interdigitated comb fingers, where motion can change the gap or overlap. A dedicated circuit converts the tiny capacitance change into a signal; some devices provide digital output.

### Piezoresistive sensing

Piezoresistive sensors detect a change in electrical resistance when acceleration strains a beam or another structure. A bridge circuit can convert that change into a voltage. This approach is used in some test sensors for high-shock measurements. The best sensing method depends on range, bandwidth, temperature, power, and other requirements; there is no universal winner.

## Where accelerometers are used

Accelerometers contribute to screen rotation, gesture and step estimates, motion tracking in games and VR, and attitude control in drones and other equipment. They are also used in automotive crash sensing, but airbag deployment is decided by a vehicle-specific, validated control system—not by a sensor alone. Step counts and sleep features are software estimates based in part on acceleration data.

### References

- [STMicroelectronics: How MEMS sensors work](https://www.st.com/content/st_com/en/support/learning/essentials-and-insights/mems/how-does-a-mems-sensor-work.html)
- [Analog Devices: Using an accelerometer for tilt](https://www.analog.com/en/resources/app-notes/an-1057.html)
- [Bosch Sensortec: Sensor fusion](https://www.bosch-sensortec.com/en/software-tools/software/sensor-fusion-software-bsx)
- [Analog Devices: Accelerometer sensing and capacitive detection](https://www.analog.com/en/resources/technical-articles/accelerometer-and-gyroscopes-sensors-operation-sensing-and-applications.html)
- [Analog Devices: Accelerometers and automotive crash sensing](https://www.analog.com/en/resources/product-faqs/adxl213.html)

An accelerometer measures acceleration-related data along its sensor axes. Tilt and motion states are inferred by software from that output, often together with other sensors.

[PCB Piezotronics: Piezoresistive shock accelerometers](https://www.pcb.com/sensors-for-test-measurement/accelerometers/piezoresistive-shock)
