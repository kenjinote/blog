---
title: "Qiskit के साथ क्वांटम प्रोग्रामिंग का परिचय"
slug: "qiskit-quantum-programming-intro"
date: "2026-09-11T20:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["programming", "quantum-computing", "python"]
tags: ["Qiskit", "Python", "Quantum Computing", "IBM"]
description: "क्यूबिट, मापन और एंटैंगलमेंट की मूल बातें जानें और वर्तमान Qiskit तथा AerSimulator से Bell अवस्था का अनुकरण करें।"
lastmod: 2026-11-24
---
# क्वांटम प्रोग्रामिंग की मूल बातें

क्वांटम कंप्यूटर क्वांटम यांत्रिकी के नियमों वाले अवस्थाओं को बदलकर गणना करते हैं। वे हर समस्या को तेज़ नहीं करते; ज्ञात लाभ खास समस्याओं और मान्यताओं पर निर्भर हैं। व्यावहारिक प्रदर्शन एल्गोरिदम, हार्डवेयर, शोर और त्रुटि-सुधार पर निर्भर करता है।

## क्यूबिट और मापन

एक क्यूबिट की शुद्ध अवस्था $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$ होती है, जहाँ $|\alpha|^2+|\beta|^2=1$। कम्प्यूटेशनल आधार में मापन से 0 या 1 मिलने की संभावनाएँ क्रमशः $|\alpha|^2$ और $|\beta|^2$ हैं। n क्यूबिट के अवस्था-वेक्टर में $2^n$ आयाम होते हैं, पर इससे $2^n$ उत्तर एक साथ पढ़े नहीं जा सकते और न ही हर गणना घातांकीय रूप से तेज़ होती है।

## गेट और एंटैंगलमेंट

क्वांटम गेट अवस्थाओं पर एकात्मक रूपांतरण हैं। X, 0 और 1 को बदलता है; H आधार-अवस्था को सुपरपोज़िशन में बदलता है; नियंत्रण बिट 1 होने पर CNOT लक्ष्य को पलटता है। पहले क्यूबिट पर H और फिर CNOT लगाने से Bell अवस्था $(|00\rangle+|11\rangle)/\sqrt{2}$ मिलती है। मापन परिणाम सहसंबद्ध होते हैं, लेकिन एंटैंगलमेंट से प्रकाश से तेज़ सूचना नहीं भेजी जा सकती।

## Qiskit स्थापित करें और Bell सर्किट बनाएँ

Qiskit SDK से सर्किट बनाए और रूपांतरित किए जाते हैं। Qiskit 1.0 से Aer अलग `qiskit-aer` पैकेज है। यह उदाहरण स्थानीय आदर्श सिम्युलेटर चलाता है; यह वास्तविक हार्डवेयर के शोर या प्रदर्शन को नहीं दर्शाता।

```bash
python -m pip install qiskit qiskit-aer
```

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

circuit = QuantumCircuit(2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure_all()

simulator = AerSimulator()
result = simulator.run(circuit, shots=1000).result()
print(result.get_counts(circuit))
```

आदर्श सिमुलेशन में केवल `00` और `11` आते हैं और शॉट बढ़ाने पर उनकी संख्या लगभग आधी-आधी होती है। सीमित नमूने में अंतर हो सकता है। हार्डवेयर शोर से `01` या `10` भी आ सकते हैं। बिट स्ट्रिंग का क्रम समझते समय क्लासिकल रजिस्टर के नियम देखें।

## एल्गोरिदम की गति के बारे में

Deutsch–Jozsa का एक ओरेकल-कॉल परिणाम क्वेरी जटिलता के संदर्भ में है: फ़ंक्शन के स्थिर या संतुलित होने की शर्त और आदर्श ओरेकल माना जाता है। Grover खोज बिना संरचना वाले N उम्मीदवारों में चिह्नित वस्तु को $O(\sqrt{N})$ आदर्श ओरेकल कॉल में ढूँढती है। इसका अर्थ यह नहीं कि हर डेटाबेस कार्य उसी अनुपात में तेज़ होगा।

## संदर्भ

- [Qiskit installation](https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit)
- [Local simulators](https://quantum.cloud.ibm.com/docs/en/guides/local-simulators)
- [Qiskit 1.0 migration notes](https://quantum.cloud.ibm.com/docs/en/guides/qiskit-1.0-features)
- [QuantumCircuit API](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.QuantumCircuit)
- [AerSimulator API](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html)
