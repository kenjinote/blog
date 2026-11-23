---
title: 'Windows Command Prompt से curl द्वारा OpenAI API को कॉल करना'
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
lastmod: "2026-11-23"
tags: ["ChatGPT", "API", "कमांड"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Windows cmd.exe से OpenAI Responses API को टेक्स्ट अनुरोध भेजने का तरीका जानें। API key को environment variable में रखें और अनुरोध फ़ाइल में key डाले बिना JSON भेजें।'
---


यह मार्गदर्शिका Windows `cmd.exe` से OpenAI API को कॉल करती है। नए ऐप्लिकेशन के लिए Responses API की अनुशंसा की जाती है। ChatGPT और API Platform अलग सेवाएँ हैं; API का उपयोग ChatGPT सदस्यता से अलग बिल किया जाता है। अनुरोध भेजने से पहले [API बिलिंग सेटअप](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform) देखें।

## API key को environment variable में सेट करें

API Platform के [API keys पेज](https://platform.openai.com/api-keys) पर key बनाएँ। इसे source code या अनुरोध फ़ाइल में न रखें। Windows में `Win+R` दबाएँ, `sysdm.cpl` चलाएँ और **Advanced > Environment Variables > User variables > New** चुनें। नाम `OPENAI_API_KEY` और मान अपनी key रखें, फिर Command Prompt की नई विंडो खोलें। secret दिखाए बिना जाँचें कि variable सेट है:

```cmd
if defined OPENAI_API_KEY (echo OPENAI_API_KEY is set) else (echo OPENAI_API_KEY is missing)
```

Environment variable से key ऐप्लिकेशन source में हार्डकोड नहीं होती, लेकिन इससे उसे प्रकाशित या साझा करना सुरक्षित नहीं हो जाता। लीक हुई key को API keys पेज पर रद्द करके बदलें। [API key सुरक्षा की सर्वोत्तम प्रक्रियाएँ](https://developers.openai.com/api/docs/guides/production-best-practices) भी देखें।

## अनुरोध बनाएँ

इस JSON को काम के फ़ोल्डर में `request.json` नाम से सहेजें। ASCII से बाहर के अक्षर शामिल हों तो UTF-8 में सहेजें।

```json
{
  "model": "gpt-6.2-sol",
  "instructions": "Answer in Kansai dialect.",
  "input": "Explain what an API is in one sentence."
}
```

Model ID बदल सकते हैं और उपलब्धता API project पर निर्भर करती है। उदाहरण वाला model इस्तेमाल करने से पहले वर्तमान [model catalog](https://developers.openai.com/api/docs/models) देखें।

## curl.exe से अनुरोध भेजें

Command Prompt में `request.json` वाले फ़ोल्डर पर जाएँ और यह चलाएँ:

```cmd
curl.exe --include https://api.openai.com/v1/responses ^
  -H "Content-Type: application/json" ^
  -H "Authorization: Bearer %OPENAI_API_KEY%" ^
  --data-binary "@request.json"
```

`--include` HTTP status और response headers दिखाता है। Responses API JSON लौटाती है। बनाया गया text output message के भीतर `output_text` content item में होता है। Tool calls और अन्य response types में अलग items हो सकते हैं; इसलिए fixed array index मानने के बजाय JSON parser से हर item का `type` जाँचें। [Responses API reference](https://developers.openai.com/api/reference/resources/responses/methods/create) देखें।

## त्रुटियाँ और उपयोग

- `401` का अर्थ key का अनुपस्थित या अमान्य होना अथवा project के लिए अनुमति न होना हो सकता है। मान दिखाए या साझा किए बिना सेटिंग जाँचें।
- `429` rate limit या उपलब्ध credit अथवा usage limit समाप्त होने का संकेत हो सकता है। Response body और API Platform के Usage तथा Billing पेज देखें।
- लागत model और input/output tokens पर निर्भर है। API Platform में नवीनतम कीमत और project usage देखें; ज़रूरत हो तो limits या alerts सेट करें।

## References

- [OpenAI API quickstart](https://developers.openai.com/api/docs/quickstart)
- [Text generation with the Responses API](https://developers.openai.com/api/docs/guides/text)
- [Responses API: create a response](https://developers.openai.com/api/reference/resources/responses/methods/create)
- [API models](https://developers.openai.com/api/docs/models)
- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- [OpenAI API key security best practices](https://developers.openai.com/api/docs/guides/production-best-practices)
- [ChatGPT and API billing are separate](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform)
