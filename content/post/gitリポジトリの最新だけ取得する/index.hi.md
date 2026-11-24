---
title: 'उथले इतिहास के साथ Git रिपॉज़िटरी कैसे क्लोन करें'
slug: "gitरिपॉजिटरीの最新だけ取得する"
date: 2024-04-27T02:54:12+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["git", "रिपॉजिटरी", "कमांड"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'जानें कि git clone --depth 1 क्या डाउनलोड करता है, शाखा कैसे चुनें और बाद में अधिक इतिहास कैसे लें।'
---

# उथले इतिहास के साथ Git रिपॉज़िटरी क्लोन करें

`git clone --depth 1` चुनी हुई शाखा के नवीनतम सिरे से इतिहास की गहराई एक वाला shallow clone बनाता है। डिफ़ॉल्ट रूप से चुनी हुई शाखा रिमोट की default branch होती है। इससे भेजे जाने वाले commit इतिहास की मात्रा घटती है, लेकिन Git वर्तमान फ़ाइलें और ज़रूरी ऑब्जेक्ट डाउनलोड करता है; इसलिए बड़ी फ़ाइलों वाली रिपॉज़िटरी फिर भी बड़ी हो सकती है।

```sh
git clone --depth 1 <repository-url>
```

किसी शाखा को चुनने के लिए उसका नाम दें:

```sh
git clone --depth 1 --single-branch --branch <branch> <repository-url>
```

बाद में और इतिहास प्राप्त किया जा सकता है, उदाहरण के लिए:

```sh
git -C <directory> fetch --deepen=50 origin <branch>
```

`<directory>` और `<branch>` को अपने वास्तविक नामों से बदलें। `--depth` के साथ, जब तक इसे बदला न जाए, Git `--single-branch` भी लागू करता है। `--unshallow` समेत विवरण के लिए आधिकारिक [`git clone`](https://git-scm.com/docs/git-clone) और [`git fetch`](https://git-scm.com/docs/git-fetch) मैनुअल देखें।
