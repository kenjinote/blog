---
title: "Python से छवि डाउनलोड करें, अस्थायी रूप से सहेजें और खोलें"
slug: "Pythonコード片"
tags: ["Python", "नमूना कोड"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Python standard library से PNG की जाँच करें, उसकी अस्थायी प्रति desktop browser में खोलें और देखने के बाद हटाएँ।"
date: "2025-02-24T18:21:14+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

यह उदाहरण केवल Python standard library का उपयोग करके वेब छवि डाउनलोड करता है, उसे अस्थायी रूप से सहेजता है और स्थानीय desktop browser में खोलता है। इसमें Python.org पर होस्ट किया गया PNG लोगो है। URL बदलें तो भरोसेमंद HTTPS छवि चुनें जिसे देखने की आपको अनुमति हो।

## परिवेश

यह कोड स्थानीय कंप्यूटर पर interactive Python session के लिए है। Colab जैसे remote notebook में runtime की अस्थायी फ़ाइल स्थानीय browser से सीधे उपलब्ध न हो सकती है।

## छवि डाउनलोड करके खोलें

कोड 15 सेकंड का network timeout लगाता है, Content-Type और PNG signature जाँचता है तथा डाउनलोड को 2 MiB तक सीमित करता है। Browser खुलने पर छवि बंद करें, terminal पर लौटें और अस्थायी फ़ाइल हटाने के लिए Enter दबाएँ।

```python
from pathlib import Path
import tempfile
import urllib.request
import webbrowser

image_url = "https://www.python.org/static/community_logos/python-logo.png"
max_bytes = 2 * 1024 * 1024
temp_path = None

try:
    request = urllib.request.Request(image_url, headers={"User-Agent": "Python image example"})
    with urllib.request.urlopen(request, timeout=15) as response:
        if response.status != 200:
            raise RuntimeError(f"Unexpected HTTP status: {response.status}")
        if response.headers.get_content_type() != "image/png":
            raise ValueError("The response is not a PNG image")
        image_data = response.read(max_bytes + 1)

    if len(image_data) > max_bytes:
        raise ValueError("The image exceeds the 2 MiB limit")
    if not image_data.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("The response does not have a PNG signature")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        temp_path = Path(temp_file.name)
        temp_file.write(image_data)

    print(temp_path.as_uri())
    if webbrowser.open(temp_path.as_uri(), new=2):
        input()
    else:
        raise RuntimeError("Could not launch a browser")
finally:
    if temp_path is not None and temp_path.exists():
        temp_path.unlink()
```

## सीमाएँ और ध्यान दें

भरोसेमंद छवि URL उपयोग करें और आवश्यक उपयोग-अधिकार की पुष्टि करें। उदाहरण केवल PNG स्वीकार करता है और 2 MiB से बड़ी फ़ाइल अस्वीकार करता है। Browser शुरू होना OS और execution environment पर निर्भर है।

## आधिकारिक संदर्भ

- [Python: urllib.request](https://docs.python.org/3/library/urllib.request.html)
- [Python: tempfile](https://docs.python.org/3/library/tempfile.html)
- [Python: webbrowser](https://docs.python.org/3/library/webbrowser.html)
- [Python Software Foundation: Python logos](https://www.python.org/community/logos/)
