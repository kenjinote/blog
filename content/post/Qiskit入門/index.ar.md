---
title: "مقدمة في البرمجة الكمومية باستخدام Qiskit"
date: "2026-09-24T19:44:38+09:00"
slug: 'qiskit-quantum-programming-intro'
date: '2026-09-11T20:00:00+09:00'
image: 'img/eyecatch.jpg'
math: true
mermaid: true
categories: ["programming", "quantum-computing", "python"]
tags: ["Qiskit", "Python", "Quantum Computing", "IBM"]
description: "تعرّف إلى الكيوبتات والقياس والتشابك، ثم حاك حالة بيل باستخدام Qiskit وAerSimulator بالإصدارات الحالية."
lastmod: 2026-11-24
---
# أساسيات البرمجة الكمومية

تحسب الحواسيب الكمومية عبر معالجة حالات تخضع لميكانيكا الكم. وهي لا تسرّع كل المسائل؛ فالتسريعات المعروفة تخص مسائل وافتراضات محددة. ويتوقف الأداء العملي على الخوارزمية والعتاد والضوضاء وتصحيح الأخطاء.

## الكيوبتات والقياس

تكتب الحالة النقية لكيوبت واحد على الصورة $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$، حيث $|\alpha|^2+|\beta|^2=1$. يعطي القياس في الأساس الحاسوبي 0 أو 1 باحتمالين $|\alpha|^2$ و$|\beta|^2$. يحتوي متجه الحالة لـn كيوبتات على $2^n$ سعة، لكن هذا لا يعني إمكانية قراءة $2^n$ جواب دفعة واحدة أو تسريع أي حساب أُسّيًا.

## البوابات والتشابك

البوابات الكمومية تحويلات وحدوية للحالات. تبدّل X بين 0 و1؛ وتحول H حالة أساس إلى تراكب؛ وتقلب CNOT الهدف عندما تكون قيمة التحكم 1. يؤدي تطبيق H على الكيوبت الأول ثم CNOT إلى حالة بيل $(|00\rangle+|11\rangle)/\sqrt{2}$. تتسم نتائج القياس بالترابط، لكن التشابك لا يتيح إرسال معلومات أسرع من الضوء.

## تثبيت Qiskit وبناء دائرة بيل

تُستخدم حزمة Qiskit SDK لإنشاء الدوائر وتحويلها. ومنذ Qiskit 1.0، تتوفر Aer في حزمة منفصلة اسمها `qiskit-aer`. يستخدم المثال محاكيًا محليًا مثاليًا؛ ولا يحاكي ضوضاء العتاد الحقيقي أو أداءه.

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

في المحاكاة المثالية لا تظهر إلا `00` و`11`، ويقترب عدد كل منهما من النصف عند زيادة عدد القياسات. وقد تختلف عينة محدودة. يمكن لضوضاء العتاد أن تنتج أيضًا `01` أو `10`. راجع اصطلاح السجل الكلاسيكي عند تفسير ترتيب البتات.

## حول تسريع الخوارزميات

نتيجة استدعاء واحد لخوارزمية Deutsch–Jozsa هي نتيجة في تعقيد الاستعلامات، وتفترض أن الدالة ثابتة أو متوازنة وأن الصندوق الأسود مثالي. تبحث خوارزمية Grover عن عنصر معلّم بين N مرشحًا غير منظّم باستخدام $O(\sqrt{N})$ استدعاءات مثالية للصندوق الأسود. ولا يعني ذلك تسريع كل مهام قواعد البيانات بهذه النسبة.

## مراجع

- [Qiskit installation](https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit)
- [Local simulators](https://quantum.cloud.ibm.com/docs/en/guides/local-simulators)
- [Qiskit 1.0 migration notes](https://quantum.cloud.ibm.com/docs/en/guides/qiskit-1.0-features)
- [QuantumCircuit API](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.QuantumCircuit)
- [AerSimulator API](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html)
