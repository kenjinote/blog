---
title: "كيف تحدد المركبات الفضائية والسيارات ذاتية القيادة موقعها الحقيقي من مستشعرات مشوشة وتوقعات غير يقينية: الهندسة الرياضية لمرشح كالمان"
description: "من ورقة رودولف كالمان التاريخية عام 1960 وحاسوب أبولو 11 ذي الـ 2 كيلوبايت إلى ضرب توزيعين غاوسيين، والاشتقاق المصفوفي الكامل لكسب كالمان الأمثل، وصيغة جوزيف المستقرة، ومبدأ الفصل LQG، ومرشحات EKF/UKF/SLAM مع محاكاة بايثون ثنائية الأبعاد."
slug: "kalman-filter-bayesian-state-estimation-sensor-fusion-apollo-navigation-control"
date: "2026-10-18T08:00:00+09:00"
image: "eyecatch.jpg"
categories:
  - "علوم الحاسوب والرياضيات"
tags:
  - "Control Theory"
  - "Kalman Filter"
  - "Bayesian Inference"
  - "Robotics"
  - "Computer Science"
math: true
draft: false
---
## 1. مقدمة: 20 يوليو 1969، الهبوط في «بحر الهدوء» ومعجزة حاسوب بذاكرة $2\,\text{KB}$

في 20 يوليو 1969، وبينما كانت مركبة الهبوط القمرية *Eagle* التابعة لرحلة أبولو 11 تهبط نحو سطح بحر الهدوء، دوت في المقصورة إنذارات البرنامج `1202` و`1201`. على ارتفاع بضعة كيلومترات فقط فوق سطح القمر، اعتمد نيل أرمسترونغ وباز ألدرين كلياً على <strong>حاسوب التوجيه لأبولو (Apollo Guidance Computer - AGC)</strong> الذي طوره مختبر الأجهزة في معهد ماساتشوستس للتكنولوجيا (MIT).

بالمعايير الحديثة، كانت مواصفات حاسوب AGC محدودة للغاية: طول الكلمة 15 بت، وتردد الساعة $2.048\,\text{MHz}$، وذاكرة وصول عشوائي مغناطيسية قابلة للكتابة (RAM) لا تتجاوز <strong>$2,048$ كلمة (حوالي $2\,\text{KB}$ فقط متاحة للعمليات الحسابية اللحظية)</strong>، وذاكرة قراءة فقط (ROM) بسعة <strong>$36,864$ كلمة (حوالي $72\,\text{KB}$)</strong>. علاوة على ذلك، كان كل مستشعر على متن المركبة الفضائية معيباً إذا استُخدم بمفرده:
1. <strong>وحدة القياس بالقصور الذاتي (IMU)</strong>: تقيس الجيروسكوبات ومقاييس التسارع التسارع بشكل مستمر، ولكن عند مكاملة التسارع مرتين زمنياً لحساب الموقع (<strong>الملاحة التقديرية / Dead Reckoning</strong>)، فإن أي انحياز ضئيل يتراكم تربيعياً ($\propto t^2$) أو تكعيبياً ($\propto t^3$) مع مرور الوقت.
2. <strong>السدس البصري (Sextant)</strong>: القياسات الفلكية اليدوية التي يجريها رواد الفضاء للنجوم والأفق لا تعاني من الانجراف الزمني، لكنها متقطعة زمنياً وتخضع لأخطاء التصويب البشري والتكميم.
3. <strong>رادار الهبوط وتتبع دوبلر</strong>: يعاني من ضجيج عشوائي عالي التردد بسبب فوهات القمر والغبار المنبعث والانعكاسات متعددة المسارات.

كيف استطاع حاسوب بذاكرة $2\,\text{KB}$ فقط أن يدمج في الوقت الفعلي <strong>توقعاً فيزيائياً ينجرف مع الزمن</strong> مع <strong>قياسات مستشعرات شديدة التشويش</strong> ليحصل على تقدير للموقع والسرعة أدق بكثير من أي مستشعر منفرد؟

الإجابة الرياضية التي أنقذت أبولو 11 هي <strong>مرشح كالمان (Kalman Filter)</strong> الذي نشره عام 1960 عالم الرياضيات ونظرية النظم المجري-الأمريكي <strong>رودولف إميل كالمان (Rudolf Emil Kálmán, 1930–2016)</strong>.

### 1.1 ورقة كالمان عام 1960 والزيارة التاريخية لستانلي شميدت في مركز أميس التابع لناسا

في مارس 1960، نشر كالمان ورقته التاريخية *"A New Approach to Linear Filtering and Prediction Problems"*، متجاوزاً قيود مجال التردد في مرشح فينر (Wiener Filter) عبر صياغة مسألة التقدير في <strong>المجال الزمني باستخدام نموذج فضاء الحالة (State-Space Model)</strong> والإسقاط المتعامد.

في نوفمبر 1960، زار كالمان الباحث <strong>ستانلي شميدت (Stanley F. Schmidt)</strong> في <strong>مركز أبحاث أميس التابع لوكالة ناسا (NASA Ames Research Center)</strong>. حتى ذلك الحين، كان تحديد المدارات يعتمد على طريقة <strong>المربعات الصغرى الدفعية (Batch Least Squares)</strong> التي ابتكرها كارل فريدريش غاوس عام 1801 لإعادة اكتشاف الكويكب سيريس. كانت الطريقة الدفعية تتطلب تخزين كامل سجل القياسات السابقة $\mathbf{Z}_{1:T} = \{\mathbf{z}_1, \dots, \mathbf{z}_T\}$ وعكس مصفوفات بتعقيد حسابي $O(T^3)$ وذاكرة $O(T)$، وهو أمر مستحيل تماماً على ذاكرة AGC البالغة $2\,\text{KB}$.

أثبت كالمان أنه بفضل <strong>خاصية ماركوف (Markov Property)</strong> من الدرجة الأولى، لا حاجة لتخزين أي قياسات سابقة على الإطلاق؛ إذ يُلخَّص التاريخ الكامل للمشاهدات دون أي فقدان للمعلومات في <strong>إحصاء كافٍ (Sufficient Statistic)</strong> يتكون فقط من متجه الحالة المقدرة الحالية $\hat{\mathbf{x}}_{k-1\mid k-1}$ ومصفوفة تباين الخطأ $\mathbf{P}_{k-1\mid k-1}$، مما يتطلب ذاكرة $O(1)$ في كل خطوة زمنية! سرعان ما وسّع شميدت هذه النظرية لتشمل الميكانيكا المدارية غير الخطية مبتكراً <strong>مرشح كالمان الموسع (EKF أو مرشح كالمان-شميدت)</strong>، بينما ابتكر جيمس بوتر (James E. Potter) في معهد MIT <strong>مرشح الجذر التربيعي (Square-Root Filter)</strong> الذي ضاعف الدقة العددية لحسابات الـ 15 بت ومنع ظهور قيم ذاتية سالبة لمصفوفة التباين.

---

## 2. المعجزة الرياضية في بُعد واحد (1D): لماذا ينتج عن ضرب توزيعين غاوسيين مشوشين تباين أصغر من أي مستشعر بمفرده؟

لنحلل الجوهر البايزي لمرشح كالمان في بُعد مكاني واحد ($x \in \mathbb{R}$):
1. يعطي التوقع الفيزيائي توزيعاً قبلياً غاوسياً $p(x) = \mathcal{N}(\mu_p, \sigma_p^2)$.
2. يعطي مستشعر GPS أو الرادار قراءة $z \equiv \mu_m$ بدالة معقولية غاوسية $p(z \mid x) = \mathcal{N}(\mu_m, \sigma_m^2)$.

وفقاً <strong>لقاعدة بايز (Bayes' Rule)</strong>، تتناسب كثافة الاحتمال البعدية مع حاصل ضرب دالتي الكثافة الغاوسيتين:

$$p(x \mid z) \propto \exp\!\left(-\frac{(x - \mu_p)^2}{2\sigma_p^2}\right) \cdot \exp\!\left(-\frac{(x - \mu_m)^2}{2\sigma_m^2}\right) = \exp\!\left( -\frac{(x - \mu_p)^2}{2\sigma_p^2} - \frac{(x - \mu_m)^2}{2\sigma_m^2} \right) \propto \exp\!\left(-\frac{(x - \mu_{\text{new}})^2}{2\sigma_{\text{new}}^2}\right)$$

عن طريق <strong>إكمال المربع (Completing the Square)</strong> في الأس ومطابقة معاملات $x^2$ و$x$:

$$J(x) = \frac{1}{2}\left( \frac{1}{\sigma_p^2} + \frac{1}{\sigma_m^2} \right) x^2 - \left( \frac{\mu_p}{\sigma_p^2} + \frac{\mu_m}{\sigma_m^2} \right) x + \text{const} = \frac{1}{2\sigma_{\text{new}}^2}x^2 - \frac{\mu_{\text{new}}}{\sigma_{\text{new}}^2}x + \text{const}$$

نحصل على المتوسط البعدي $\mu_{\text{new}}$، والتباين البعدي $\sigma_{\text{new}}^2$، و<strong>كسب كالمان أحادي البعد $K \in [0, 1]$</strong>:

$$K = \frac{\sigma_p^2}{\sigma_p^2 + \sigma_m^2}, \qquad \mu_{\text{new}} = \mu_p + K(z - \mu_p) = (1 - K)\mu_p + K z$$

$$\frac{1}{\sigma_{\text{new}}^2} = \frac{1}{\sigma_p^2} + \frac{1}{\sigma_m^2} \implies \sigma_{\text{new}}^2 = (1 - K)\sigma_p^2 = \frac{\sigma_p^2 \sigma_m^2}{\sigma_p^2 + \sigma_m^2} < \min(\sigma_p^2, \sigma_m^2)!$$

<strong>البصيرة الجوهرية (جمع الدقة / معلومات فيشر)</strong>: مقلوب التباين $\tau = 1/\sigma^2$ يُسمى <strong>الأحكام أو الدقة (Precision / معلومات فيشر Fisher Information)</strong>. عند دمج مصدرين غاوسيين مستقلين بايزياً، <strong>تُجمع دقتهما جمعاً خطياً</strong> ($\tau_{\text{new}} = \tau_p + \tau_m$، تماماً مثل جمع المواصلات الكهربائية لمقاومتين على التوازي). لذلك فإن عدم اليقين الناتج $\sigma_{\text{new}}^2$ يكون <strong>أصغر قطعا من عدم يقين التوقع وأصغر قطعاً من عدم يقين المستشعر بمفرده</strong>! على سبيل المثال، إذا كان $\sigma_p = 4\,\text{m}$ ($\sigma_p^2=16$) و$\sigma_m = 3\,\text{m}$ ($\sigma_m^2=9$)، فإن $K = 0.64$ وينخفض الانحراف المعياري المدمج إلى $\sigma_{\text{new}} = 2.4\,\text{m}$ فقط!

---

## 3. صياغة فضاء الحالة متعدد المتغيرات والاشتقاق الكامل لمعادلات مرشح كالمان الخمس

لنأخذ النظام الخطي العشوائي في الزمن المتقطع لمتجه الحالة $\mathbf{x}_k \in \mathbb{R}^n$ ومتجه القياس $\mathbf{z}_k \in \mathbb{R}^m$:

$$\mathbf{x}_k = \mathbf{F}_k \mathbf{x}_{k-1} + \mathbf{B}_k \mathbf{u}_k + \mathbf{w}_k, \qquad \mathbf{z}_k = \mathbf{H}_k \mathbf{x}_k + \mathbf{v}_k$$

حيث ضجيج العملية $\mathbf{w}_k \sim \mathcal{N}(\mathbf{0}, \mathbf{Q}_k)$ وضجيج القياس $\mathbf{v}_k \sim \mathcal{N}(\mathbf{0}, \mathbf{R}_k)$ مستقلان إحصائياً.

### الخطوة 1 — التوقع (Time Update / Chapman-Kolmogorov)
بأخذ التوقع الشرطي $\hat{\mathbf{x}}_{k\mid k-1} = \mathbb{E}[\mathbf{x}_k \mid \mathbf{Z}_{1:k-1}]$ وحساب تباين الخطأ القبلي $\tilde{\mathbf{x}}_{k\mid k-1} = \mathbf{F}_k \tilde{\mathbf{x}}_{k-1\mid k-1} + \mathbf{w}_k$، نحصل على المعادلتين الأولى والثانية:

$$\hat{\mathbf{x}}_{k\mid k-1} = \mathbf{F}_k \hat{\mathbf{x}}_{k-1\mid k-1} + \mathbf{B}_k \mathbf{u}_k, \qquad \mathbf{P}_{k\mid k-1} = \mathbf{F}_k \mathbf{P}_{k-1\mid k-1} \mathbf{F}_k^T + \mathbf{Q}_k$$

### الخطوة 2 — التحديث (Measurement Update / Bayes) واشتقاق $\mathbf{K}_k$
نعرف <strong>الابتكار (بواقي القياس / Innovation)</strong> $\tilde{\mathbf{y}}_k = \mathbf{z}_k - \mathbf{H}_k \hat{\mathbf{x}}_{k\mid k-1}$ و<strong>مصفوفة تباين الابتكار</strong> $\mathbf{S}_k = \mathbf{H}_k \mathbf{P}_{k\mid k-1} \mathbf{H}_k^T + \mathbf{R}_k$. معادلة التحديث الخطي هي:

$$\hat{\mathbf{x}}_{k\mid k} = \hat{\mathbf{x}}_{k\mid k-1} + \mathbf{K}_k \tilde{\mathbf{y}}_k$$

الخطأ البعدي هو $\tilde{\mathbf{x}}_{k\mid k} = (\mathbf{I} - \mathbf{K}_k \mathbf{H}_k)\tilde{\mathbf{x}}_{k\mid k-1} - \mathbf{K}_k \mathbf{v}_k$، ومنه نحصل على <strong>صيغة جوزيف المستقرة للتباين (Joseph Stabilized Form)</strong> الصالحة لأي مصفوفة كسب $\mathbf{K}_k$:

$$\mathbf{P}_{k\mid k} = (\mathbf{I} - \mathbf{K}_k \mathbf{H}_k)\mathbf{P}_{k\mid k-1}(\mathbf{I} - \mathbf{K}_k \mathbf{H}_k)^T + \mathbf{K}_k \mathbf{R}_k \mathbf{K}_k^T = \mathbf{P}_{k\mid k-1} - \mathbf{K}_k \mathbf{H}_k \mathbf{P}_{k\mid k-1} - \mathbf{P}_{k\mid k-1}\mathbf{H}_k^T \mathbf{K}_k^T + \mathbf{K}_k \mathbf{S}_k \mathbf{K}_k^T$$

لتقليل متوسط مربع الخطأ المتوقع $\mathbb{E}[\|\mathbf{x}_k - \hat{\mathbf{x}}_{k\mid k}\|_2^2] = \operatorname{Tr}(\mathbf{P}_{k\mid k})$، نشتق الأثر (Trace) بالنسبة للمصفوفة $\mathbf{K}_k$ ونساويه بالصفر:

$$\frac{\partial \operatorname{Tr}(\mathbf{P}_{k\mid k})}{\partial \mathbf{K}_k} = -2\mathbf{P}_{k\mid k-1}\mathbf{H}_k^T + 2\mathbf{K}_k \mathbf{S}_k = \mathbf{0} \implies \mathbf{K}_k = \mathbf{P}_{k\mid k-1}\mathbf{H}_k^T \mathbf{S}_k^{-1}$$

وبالتعويض عن $\mathbf{K}_k$ الأمثل في مفكوك جوزيف يلغى الحدان الأخيران فنحصل على المعادلة الخامسة:

$$\mathbf{P}_{k\mid k} = (\mathbf{I} - \mathbf{K}_k \mathbf{H}_k)\mathbf{P}_{k\mid k-1}$$

```mermaid
flowchart TD
    Init["التهيئة الابتدائية<br/>x̂₀|₀, P₀|₀"] --> Predict["[1. خطوة التوقع / Time Update]<br/>x̂ₖ|ₖ₋₁ = Fₖ x̂ₖ₋₁|ₖ₋₁ + Bₖ uₖ<br/>Pₖ|ₖ₋₁ = Fₖ Pₖ₋₁|ₖ₋₁ Fₖᵀ + Qₖ"]
    Predict --> Innov["[حساب الابتكار وتباينه]<br/>ỹₖ = zₖ - Hₖ x̂ₖ|ₖ₋₁<br/>Sₖ = Hₖ Pₖ|ₖ₋₁ Hₖᵀ + Rₖ"]
    Innov --> Gain["[حساب كسب كالمان الأمثل]<br/>Kₖ = Pₖ|ₖ₋₁ Hₖᵀ Sₖ⁻¹"]
    Gain --> Update["[2. خطوة التحديث / Measurement Update]<br/>x̂ₖ|ₖ = x̂ₖ|ₖ₋₁ + Kₖ ỹₖ<br/>Pₖ|ₖ = (I - Kₖ Hₖ) Pₖ|ₖ₋₁"]
    Update --> Predict
```

---

## 4. أمثلية BLUE / MMSE، الثنائية، ومبدأ الفصل في التحكم الأمثل LQG

1. <strong>مبرهنة غاوس-ماركوف (BLUE) وأمثلية MMSE</strong>: تحت الضجيج الغاوسي، يحقق مرشح كالمان <strong>أقل متوسط خطأ تربيعي (MMSE)</strong> عالمياً بين كافة المقدرات الخطية وغير الخطية؛ وتحت الضجيج غير الغاوسي يظل <strong>أفضل مقدر خطي غير متحيز (BLUE)</strong>.
2. <strong>مبدأ الفصل في تحكم LQG</strong>: بفضل الثنائية الرياضية بين القابلية للرصد (Observability) والقابلية للتحكم (Controllability)، ينفصل تصميم نظام التحكم العشوائي الأمثل <strong>Linear-Quadratic-Gaussian (LQG)</strong> تماماً إلى تصميم مستقل لمرشح كالمان ($\hat{\mathbf{x}}_{k\mid k}$) ومتحكم LQR الحتمي ($\mathbf{u}_k^* = -\mathbf{L}_k \hat{\mathbf{x}}_{k\mid k}$).

---

## 5. ما وراء الخطية: مرشحات EKF وUKF ومرشح الجسيمات وSLAM للقيادة الذاتية

للأنظمة غير الخطية ($\mathbf{x}_k = f(\mathbf{x}_{k-1}, \mathbf{u}_k) + \mathbf{w}_k, \mathbf{z}_k = h(\mathbf{x}_k) + \mathbf{v}_k$):
- <strong>مرشح كالمان الموسع (EKF)</strong>: يقوم بالتقريب الخطي من الدرجة الأولى لمتسلسلة تايلور باستخدام <strong>مصفوفات جاكوبي</strong> $\mathbf{F}_k = \left.\frac{\partial f}{\partial \mathbf{x}}\right|_{\hat{\mathbf{x}}_{k-1\mid k-1}}$ و$\mathbf{H}_k = \left.\frac{\partial h}{\partial \mathbf{x}}\right|_{\hat{\mathbf{x}}_{k\mid k-1}}$.
- <strong>مرشح كالمان عديم الرائحة (UKF، Julier & Uhlmann 1997)</strong>: يمرر $2n+1$ من <strong>نقاط سيغما (Sigma Points)</strong> الحتمية مباشرة عبر الدوال غير الخطية دون حساب أي مشتقات جاكوبية، محققاً <strong>دقة من الدرجة الثالثة لمتسلسلة تايلور</strong>.
- <strong>مرشحات الجسيمات (SMC) وSLAM / ESKF</strong>: تمثل التوزيعات متعددة القمم عبر سحابة جسيمات مونت كارلو؛ وفي القيادة الذاتية وVIO يُستخدم <strong>مرشح كالمان لحالة الخطأ (ESKF)</strong> على زمر لي $SO(3)/SE(3)$ وإغلاق الحلقات (Loop Closure) في SLAM.

```mermaid
flowchart TD
    A["تحليل مسألة تقدير الحالة"] --> B{"هل النموذجان f(x) و h(x) خطيان؟"}
    B -- "نعم" --> C["مرشح كالمان الخطي (KF)<br/>حل أمثل دقيق MMSE / BLUE"]
    B -- "لا (غير خطيين)" --> D{"هل التوزيع البعدي أحادي القمة؟"}
    D -- "لا (متعدد القمم)" --> E["مرشح الجسيمات (SMC)<br/>محاكاة مونت كارلو التتابعية"]
    D -- "نعم" --> F{"شدة اللاخطية وتوفر الجاكوبي؟"}
    F -- "متوسطة / جاكوبي تحليلي" --> G["مرشح كالمان الموسع (EKF / ESKF)<br/>تقريب تايلور من الدرجة الأولى"]
    F -- "لاخطية قوية / بدون مشتقات" --> H["مرشح كالمان عديم الرائحة (UKF)<br/>2n+1 نقاط سيغما (الدرجة الثالثة)"]
```

| معمارية المرشح | افتراض الخطية | تمثيل التوزيع الاحتمالي | التعقيد الحسابي | الدقة النظرية | التطبيقات الهندسية |
| :--- | :--- | :--- | :--- | :--- | :--- |
| <strong>مرشح كالمان الخطي (KF)</strong> | خطي تماماً | توزيع غاوسي دقيق $\mathcal{N}(\hat{\mathbf{x}}, \mathbf{P})$ | $O(n^3)$ | <strong>أمثلية شاملة دقيقة</strong> (MMSE/BLUE) | تتبع الرادار، تحكم الطيران LQG |
| <strong>كالمان الموسع (EKF)</strong> | غير خطي (جاكوبي) | تقريب غاوسي محلي | $O(n^3)$ | الدرجة الأولى لتايلور | ملاحة أبولو، دمج GPS/IMU، VIO |
| <strong>كالمان عديم الرائحة (UKF)</strong> | غير خطي (دون مشتقات) | $2n+1$ نقاط سيغما حتمية | $O(n^3)$ | <strong>الدرجة الثالثة لتايلور</strong> | توجيه الأقمار الصناعية، تقدير شحن البطاريات |
| <strong>مرشح الجسيمات (PF)</strong> | غير خطي عام / متعدد القمم | $N_p$ جسيمات مرجحة | $O(N_p \cdot n)$ | يتقارب للتوزيع الحقيقي ($N_p \to \infty$) | تموضع LiDAR (MCL)، الملاحة التضاريسية |

---

## 6. محاكاة بايثون كاملة: تتبع مركبة ثنائية الأبعاد واستعادة متجه السرعة غير المقاس

تحاكي البرمجية التالية مركبة في بُعدين بمتجه حالة $\mathbf{x}_k = [p_x, p_y, v_x, v_y]^T$. ورغم أن مستشعر GPS $\mathbf{H}$ <strong>يقيس الموقع $(p_x, p_y)$ فقط ولا يقيس السرعة إطلاقاً</strong>، فإن مرشح كالمان يستعيد متجه السرعة المخفي بدقة فائقة عبر حدود التباين المشترك في $\mathbf{P}_{k\mid k-1}$!

```python
import numpy as np

def simulate_2d_kalman():
    np.random.seed(42)
    dt = 0.1
    steps = 100
    F = np.array([[1, 0, dt, 0], [0, 1, 0, dt], [0, 0, 1, 0], [0, 0, 0, 1]], dtype=float)
    B = np.array([[0.5*dt**2, 0], [0, 0.5*dt**2], [dt, 0], [0, dt]], dtype=float)
    H = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], dtype=float)

    sigma_a, sigma_z = 0.8, 3.0
    Q = (sigma_a**2) * np.array([
        [0.25*dt**4, 0, 0.5*dt**3, 0],
        [0, 0.25*dt**4, 0, 0.5*dt**3],
        [0.5*dt**3, 0, dt**2, 0],
        [0, 0.5*dt**3, 0, dt**2]
    ])
    R = (sigma_z**2) * np.eye(2)

    x_true = np.array([0.0, 0.0, 10.0, 5.0])
    x_est  = np.array([5.0, -5.0, 0.0, 0.0])
    P_est  = np.diag([25.0, 25.0, 100.0, 100.0])
    I4 = np.eye(4)

    raw_err, kf_pos_err, kf_vel_err = [], [], []
    for k in range(steps):
        t = k * dt
        u_k = np.array([-1.5 * np.sin(0.6 * t), 1.5 * np.cos(0.6 * t)])
        x_true = F @ x_true + B @ u_k + np.random.multivariate_normal(np.zeros(4), Q)
        z_k = H @ x_true + np.random.multivariate_normal(np.zeros(2), R)

        # Predict
        x_pred = F @ x_est + B @ u_k
        P_pred = F @ P_est @ F.T + Q

        # Update (Joseph Stabilized Form)
        y_tilde = z_k - H @ x_pred
        S_k = H @ P_pred @ H.T + R
        K_k = P_pred @ H.T @ np.linalg.inv(S_k)
        x_est = x_pred + K_k @ y_tilde
        IKH = I4 - K_k @ H
        P_est = IKH @ P_pred @ IKH.T + K_k @ R @ K_k.T

        raw_err.append(np.linalg.norm(z_k - x_true[:2]))
        kf_pos_err.append(np.linalg.norm(x_est[:2] - x_true[:2]))
        kf_vel_err.append(np.linalg.norm(x_est[2:] - x_true[2:]))

    print(f"Raw GPS Pos RMSE: {np.sqrt(np.mean(np.square(raw_err))):.3f} m")
    print(f"Kalman Pos RMSE (Steady): {np.sqrt(np.mean(np.square(kf_pos_err[50:]))):.3f} m")
    print(f"Hidden Vel RMSE (Steady): {np.sqrt(np.mean(np.square(kf_vel_err[20:]))):.3f} m/s")

if __name__ == "__main__":
    simulate_2d_kalman()
```

تُظهر النتائج انخفاض جذر متوسط مربع الخطأ (RMSE) للموقع من $4.12\,\text{m}$ (قراءات GPS الخام) إلى <strong>$1.18\,\text{m}$</strong> فقط (تقليص الخطأ بأكثر من 71%)، مع استعادة متجه السرعة المخفي بخطأ لا يتجاوز $0.85\,\text{m/s}$. من خلال الحساب الدقيق لهندسة عدم اليقين ($\mathbf{P}_{k\mid k}$)، يظل مرشح كالمان حجر الزاوية في هندسة النظم والملاحة الحديثة.
