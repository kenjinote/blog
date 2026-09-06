---
title: "wsl में 'Temporary failure resolving...' त्रुटि को कैसे ठीक करें"
slug: "wsl で「Temporary failure resolving～」と表示される場合の対処方法"
date: 2024-03-31T16:57:33+09:00
tags: ["wsl", "対処方法"]
draft: false
image: "img.png"
categories: ["ツール・開発環境"]
---

# wsl में 'Temporary failure resolving...' त्रुटि को कैसे ठीक करें

```
kenji@MyComputer:~$ sudo apt update
[sudo] password for kenji:
Err:1 http://archive.ubuntu.com/ubuntu focal InRelease
  Temporary failure resolving 'archive.ubuntu.com'
```

जब wsl में उपरोक्त त्रुटि प्रदर्शित होती है, तो DNS सर्वर सेटिंग्स गलत हो सकती हैं।
मेरे वातावरण में, इसे निम्नलिखित चरणों से हल किया गया था।

1. wsl प्रारंभ करें।
2. `sudo nano /etc/resolv.conf` निष्पादित करें।
3. `nameserver` लाइन को निम्नानुसार बदलें:
```
nameserver 8.8.8.8
```
4. `Ctrl` + `S` के साथ सहेजें, और `Ctrl` + `X` के साथ बाहर निकलें।
5. `sudo apt update` निष्पादित करें।
6. यदि त्रुटि प्रदर्शित नहीं होती है, तो यह हल हो गया है।

## यदि उपरोक्त चरणों से हल नहीं होता है

ऐसा लगता है कि ऐसे मामले हैं जहां उपरोक्त चरणों से इसका समाधान नहीं होता है। कृपया निम्नलिखित लेख देखें।

- [WSL में apt update के दौरान 'Temporary failure resolving ～' को कैसे हल करें](https://qiita.com/ryosukeYamazaki/items/c04ec3ff78aac6eb8d26)
