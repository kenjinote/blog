---
title: "Ollama से स्थानीय LLM चलाएँ: सेटअप, REST API और Python"
slug: "ollama-local-llm-api-guide"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "programming", "api"]
tags: ["Ollama", "Local LLM", "Python", "Node.js"]
date: "2026-09-11T02:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

## Ollama स्थापित करें और मॉडल तैयार करें

आधिकारिक पेज से Windows, macOS या Linux के लिए Ollama डाउनलोड करें। Windows और macOS पर ऐप खोलें; Linux पर आधिकारिक स्थापना निर्देश अपनाएँ और सर्वर चालू न हो तो उसे शुरू करें। ये कमांड निर्दिष्ट मॉडल डाउनलोड करके चलाते हैं। मॉडल की उपलब्धता और डाउनलोड आकार बदल सकते हैं, इसलिए पहले मॉडल लाइब्रेरी देखें।

```bash
ollama pull gemma4:e2b
ollama run gemma4:e2b
```

मॉडल शुरू होने के बाद, दूसरे टर्मिनल में ये कमांड डाउनलोड किए गए मॉडल और उनकी मौजूदा मेमोरी स्थिति दिखाते हैं। मॉडल फ़ाइलों को डिस्क स्थान चाहिए; अनुमान के लिए मॉडल और कॉन्टेक्स्ट लंबाई के अनुसार RAM या GPU मेमोरी भी चाहिए।

```bash
ollama list
ollama ps
```

## Chat REST API कॉल करें

स्थानीय HTTP API सामान्यतः `http://localhost:11434` पर उपलब्ध होती है। `/api/chat` संदेशों की सूची के रूप में बातचीत का इतिहास लेता है और डिफ़ॉल्ट रूप से स्ट्रीम करता है। यह उदाहरण पूर्ण JSON उत्तर के लिए `stream: false` और JSON आउटपुट के लिए `format` सेट करता है।

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "gemma4:e2b",
  "messages": [
    {"role": "user", "content": "Explain what a REST API is in one sentence."}
  ],
  "stream": false,
}'
```

Windows PowerShell में `curl` किसी दूसरे कमांड का alias हो सकता है; ऐसी स्थिति में `curl.exe` लिखें।

उत्तर का पाठ `message.content` में होता है। क्रमिक हिस्से पाने के लिए `stream` को `true` करें या यह फ़ील्ड छोड़ दें। बातचीत के इतिहास के बिना एक प्रॉम्प्ट के लिए `/api/generate` और वेक्टर के लिए एम्बेडिंग मॉडल के साथ `/api/embed` का उपयोग करें।

## Python से Ollama चलाएँ

आधिकारिक Python लाइब्रेरी HTTP अनुरोध और उत्तर ऑब्जेक्ट संभालती है। पहले Ollama सर्वर चालू करें और मॉडल डाउनलोड करें।

```bash
python -m pip install ollama
```

```python
from ollama import chat

response = chat(
    model="gemma4:e2b",
    messages=[{"role": "user", "content": "एक वाक्य में बताएँ कि REST API क्या है।"}],
    stream=False,
)
print(response.message.content)
```

क्रमशः आउटपुट पाने के लिए `stream=True` रखें और लौटे हुए हिस्सों पर क्रम से चलें। आधिकारिक लाइब्रेरी में असिंक्रोनस ऐप्लिकेशन के लिए `AsyncClient` भी है।

## Node.js से Ollama चलाएँ

आधिकारिक JavaScript पैकेज को अपने Node.js प्रोजेक्ट में इंस्टॉल करें।

```bash
npm install ollama
```

```javascript
import ollama from 'ollama';

const response = await ollama.chat({
  model: 'gemma4:e2b',
  messages: [{ role: 'user', content: 'एक वाक्य में बताएँ कि REST API क्या है।' }],
  stream: false,
});
console.log(response.message.content);
```

## एम्बेडिंग और खोज

Embeddings API पाठ को वेक्टर में बदलती है। RAG की मूल प्रक्रिया वेक्टर को इंडेक्स में रखती है, संबंधित अंश खोजती है और उन्हें चैट प्रॉम्प्ट में जोड़ती है; embeddings अपने आप उत्तर नहीं बनाते।

```bash
ollama pull embeddinggemma
curl http://localhost:11434/api/embed -d '{
  "model": "embeddinggemma",
  "input": "एक वाक्य में बताएँ कि REST API क्या है।"
}'
```

उत्तर में `embeddings` ऐरे होता है। अपनी भाषा, डेटा और लाइसेंस आवश्यकताओं के अनुसार embedding मॉडल और वेक्टर इंडेक्स चुनें।

## जनरेशन गति मापें

उत्तर में मॉडल लोड, प्रॉम्प्ट मूल्यांकन और जनरेशन का समय तथा बने हुए टोकन की संख्या होती है। `eval_duration` नैनोसेकंड में केवल जनरेशन समय है; यह कुल प्रतीक्षा समय नहीं है और इसमें प्रॉम्प्ट मूल्यांकन या मॉडल लोड शामिल नहीं है। गति का अनुमान इस प्रकार लगाएँ:

$$
\text{tokens/sec} = \frac{\text{eval\_count}}{\text{eval\_duration} / 10^9}
$$

मॉडल लोड के लिए `load_duration` और कैश में न रखे गए प्रॉम्प्ट के मूल्यांकन के लिए `prompt_eval_duration` देखें। समान मॉडल, कॉन्टेक्स्ट और हार्डवेयर पर तुलना करें; केवल गति से गुणवत्ता या कुल विलंबता का पता नहीं चलता।

## मेमोरी का अनुमान लगाएँ

पैरामीटर की संख्या और क्वांटाइज़ेशन बिट से वज़न के लिए न्यूनतम स्टोरेज का मोटा अनुमान मिलता है। 4-bit वाला 8B मॉडल वज़न के लिए लगभग 4 दशमलव GB (3.73 GiB) लेता है। कुल आवश्यकता इससे अधिक होती है: क्वांटाइज़ेशन मेटाडेटा, KV cache, कॉन्टेक्स्ट लंबाई, runtime और अन्य ऐप्लिकेशन अतिरिक्त मेमोरी लेते हैं।

$$
\text{weight bytes} \approx \frac{\text{parameter count} \times \text{bits per weight}}{8}
$$

`ollama ps` से देखें कि मॉडल GPU, CPU या दोनों पर चल रहा है। वास्तविक मेमोरी विभाजन उपलब्ध हार्डवेयर और runtime समर्थन पर निर्भर करता है।

## गोपनीयता, नेटवर्क पहुँच और लाइसेंस

केवल स्थानीय उपयोग और क्लाउड मॉडल या जुड़े ऐप्लिकेशन में अंतर रखें। संवेदनशील डेटा भेजने से पहले मॉडल, टूल और नेटवर्क पथ जाँचें। यदि API को LAN या इंटरनेट से उपलब्ध कराते हैं, तो प्रमाणीकरण और फ़ायरवॉल जैसे नियंत्रणों के बिना पोर्ट सार्वजनिक न करें। हर मॉडल का लाइसेंस देखें।

Ollama मॉडल डाउनलोड, स्थानीय अनुमान और ऐप्लिकेशन एकीकरण को एक जगह लाता है। यहाँ दिए कमांड और API उदाहरण आधिकारिक दस्तावेज़ के मूल पैटर्न हैं। मॉडल की सुविधाएँ और आवश्यकताएँ देखकर उन्हें अपने कंप्यूटर के अनुसार ढालें।

## आधिकारिक संदर्भ

- [Ollama Quickstart](https://docs.ollama.com/quickstart)
- [Chat API](https://docs.ollama.com/api/chat)
- [Generate API](https://docs.ollama.com/api/generate)
- [Embeddings API](https://docs.ollama.com/api/embed)
- [Local FAQ and server configuration](https://docs.ollama.com/faq)
- [Official Python library](https://github.com/ollama/ollama-python)
- [Official JavaScript library](https://github.com/ollama/ollama-js)
- [Ollama model library](https://ollama.com/library)
