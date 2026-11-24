---
title: "تشغيل نماذج LLM محلية باستخدام Ollama: التثبيت وREST API وPython"
slug: "ollama-local-llm-api-guide"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "programming", "api"]
tags: ["Ollama", "Local LLM", "Python", "Node.js"]
date: "2026-09-11T02:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

## تثبيت Ollama وتجهيز نموذج

نزّل Ollama لنظام Windows أو macOS أو Linux من الصفحة الرسمية. شغّل التطبيق في Windows وmacOS؛ وفي Linux اتبع خطوات التثبيت الرسمية وشغّل الخادم إن لم يكن يعمل. تنزّل الأوامر التالية نموذجاً محدداً وتشغّله. تحقق من مكتبة النماذج أولاً لأن التوفر وحجم التنزيل قد يتغيران.

```bash
ollama pull gemma4:e2b
ollama run gemma4:e2b
```

بعد بدء النموذج، استخدم هذه الأوامر في نافذة طرفية أخرى لعرض النماذج المنزّلة ومكان تشغيلها الحالي. تشغل ملفات النماذج مساحة على القرص، ويتطلب الاستدلال أيضاً ذاكرة RAM أو GPU وفقاً للنموذج وطول السياق.

```bash
ollama list
ollama ps
```

## استدعاء Chat REST API

تتوفر واجهة HTTP المحلية عادةً على `http://localhost:11434`. يستقبل `/api/chat` سجل المحادثة على هيئة قائمة رسائل، ويعيد الإجابة على شكل تدفق افتراضياً. يضبط المثال `stream` على `false` للحصول على استجابة JSON كاملة، ويطلب تنسيق JSON عبر `format`.

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "gemma4:e2b",
  "messages": [
    {"role": "user", "content": "Explain what a REST API is in one sentence."}
  ],
  "stream": false,
}'
```

في Windows PowerShell، قد يكون `curl` اسماً مستعاراً لأمر آخر؛ استخدم `curl.exe` في هذه الحالة.

يوجد نص الإجابة في `message.content`. اضبط `stream` على `true` أو احذف الحقل لتلقي أجزاء متتابعة من الإجابة. لطلب واحد بلا سجل محادثة استخدم `/api/generate`؛ ولإنشاء المتجهات استخدم `/api/embed` مع نموذج تضمين.

## استخدام Ollama من Python

تتولى مكتبة Python الرسمية إرسال طلب HTTP والتعامل مع كائن الاستجابة. شغّل خادم Ollama ونزّل النموذج أولاً.

```bash
python -m pip install ollama
```

```python
from ollama import chat

response = chat(
    model="gemma4:e2b",
    messages=[{"role": "user", "content": "اشرح في جملة واحدة معنى REST API."}],
    stream=False,
)
print(response.message.content)
```

لتلقي الخرج تدريجياً، اضبط `stream=True` وكرّر على الأجزاء المعادة. وتوفر المكتبة الرسمية أيضاً `AsyncClient` للتطبيقات غير المتزامنة.

## استخدام Ollama من Node.js

ثبّت حزمة JavaScript الرسمية في مشروع Node.js.

```bash
npm install ollama
```

```javascript
import ollama from 'ollama';

const response = await ollama.chat({
  model: 'gemma4:e2b',
  messages: [{ role: 'user', content: 'اشرح في جملة واحدة معنى REST API.' }],
  stream: false,
});
console.log(response.message.content);
```

## التضمينات والبحث

تحوّل واجهة التضمين النص إلى متجهات. يخزّن مسار RAG الأساسي المتجهات في فهرس، ويسترجع المقاطع ذات الصلة، ثم يضيفها إلى مطالبة المحادثة؛ ولا تنشئ المتجهات إجابات بمفردها.

```bash
ollama pull embeddinggemma
curl http://localhost:11434/api/embed -d '{
  "model": "embeddinggemma",
  "input": "اشرح في جملة واحدة معنى REST API."
}'
```

تحتوي الاستجابة على مصفوفة `embeddings`. اختر نموذج التضمين وفهرس المتجهات وفقاً للغة والبيانات ومتطلبات الترخيص في تطبيقك.

## قياس سرعة التوليد

تتضمن الاستجابة أزمنة تحميل النموذج وتقييم المطالبة والتوليد وعدد الرموز الناتجة. يقيس `eval_duration` زمن التوليد بالنانوثانية؛ وليس زمن الاستجابة الكلي، إذ لا يشمل تقييم المطالبة أو تحميل النموذج. قدّر معدل التوليد بهذه المعادلة:

$$
\text{tokens/sec} = \frac{\text{eval\_count}}{\text{eval\_duration} / 10^9}
$$

استخدم `load_duration` لزمن تحميل النموذج و`prompt_eval_duration` لتقييم المطالبات غير المخزنة مؤقتاً. قارن النموذج والسياق والعتاد نفسها؛ فمعدل الرموز وحده لا يعبّر عن جودة الإجابة أو زمن الاستجابة الكلي.

## تقدير استخدام الذاكرة

يساعد عدد المعلمات وعدد بتات التكميم على تقدير الحد الأدنى التقريبي لتخزين الأوزان. يحتاج نموذج 8B بتكميم 4-bit إلى نحو 4 GB عشرياً (3.73 GiB) للأوزان وحدها. ولا يشمل ذلك الذاكرة الكلية: فبيانات التكميم وذاكرة KV وطول السياق وبيئة التشغيل والتطبيقات الأخرى تحتاج إلى مساحة إضافية.

$$
\text{weight bytes} \approx \frac{\text{parameter count} \times \text{bits per weight}}{8}
$$

استخدم `ollama ps` لمعرفة ما إذا كان النموذج يعمل على GPU أو CPU أو كليهما. يعتمد التوزيع الفعلي على العتاد المتاح ودعم بيئة التشغيل.

## الخصوصية والوصول الشبكي والتراخيص

ميّز بين الاستخدام المحلي فقط والنماذج السحابية والتطبيقات المتصلة. قبل إرسال بيانات حساسة، تحقق من النموذج والأدوات ومسار الشبكة. إذا جعلت الواجهة متاحة عبر الشبكة المحلية أو الإنترنت، فلا تكشف المنفذ من دون ضوابط وصول مثل المصادقة وجدار الحماية. تحقق أيضاً من ترخيص كل نموذج.

يجمع Ollama تنزيل النماذج وتشغيلها محلياً وإتاحتها للتطبيقات. الأوامر وأمثلة API هنا أنماط أساسية مستندة إلى الوثائق الرسمية. راجع إمكانات النموذج ومتطلباته ثم عدّل الأمثلة لتناسب حاسوبك.

## المراجع الرسمية

- [Ollama Quickstart](https://docs.ollama.com/quickstart)
- [Chat API](https://docs.ollama.com/api/chat)
- [Generate API](https://docs.ollama.com/api/generate)
- [Embeddings API](https://docs.ollama.com/api/embed)
- [Local FAQ and server configuration](https://docs.ollama.com/faq)
- [Official Python library](https://github.com/ollama/ollama-python)
- [Official JavaScript library](https://github.com/ollama/ollama-js)
- [Ollama model library](https://ollama.com/library)
