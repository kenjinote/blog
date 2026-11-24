---
title: "PaperMod पोस्ट सूची में कवर चित्रों का आकार और स्थान बदलें"
slug: "PaperModのछविの配置変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "PaperMod के extended CSS और CSS Grid से पोस्ट कार्ड के कवर छोटे करें और सारांश के पास रखें।"
date: "2022-09-11T18:50:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

यह उदाहरण PaperMod पोस्ट सूची के कार्ड में कवर चित्रों को छोटा करके शीर्षक के नीचे और सारांश के बगल में रखता है। इसमें थीम की CSS या शामिल template को बदलने के बजाय साइट का extended CSS इस्तेमाल होता है। चयनकर्ता PaperMod की classes पर निर्भर हैं, इसलिए theme अपडेट के बाद ब्राउज़र में परिणाम जाँचें।

## Extended CSS जोड़ें

साइट की root में `assets/css/extended/custom.css` बनाएँ। PaperMod इस फ़ोल्डर की CSS को अपनी theme styles के साथ शामिल करता है। CSS Grid मौजूदा HTML संरचना बदले बिना दृश्य क्रम बदलता है।

```css
/* Add to assets/css/extended/custom.css */
.post-entry {
    display: grid;
    grid-template-columns: minmax(0, 150px) minmax(0, 1fr);
    grid-template-areas:
        "cover title"
        "cover summary"
        "cover meta";
    column-gap: 1rem;
    align-items: start;
}

.post-entry > .entry-cover {
    grid-area: cover;
    margin-bottom: 0;
}

.post-entry > .entry-header {
    grid-area: title;
    min-width: 0;
}

.post-entry > .entry-content {
    grid-area: summary;
    min-width: 0;
}

.post-entry > .entry-footer {
    grid-area: meta;
}

.post-entry .entry-cover img {
    display: block;
    width: 100%;
    height: auto;
}

@media (max-width: 600px) {
    .post-entry {
        grid-template-columns: minmax(0, 96px) minmax(0, 1fr);
        column-gap: 0.75rem;
    }
}
```

## संकीर्ण स्क्रीन के लिए समायोजन

संकीर्ण स्क्रीन पर कॉलम और gap छोटे करें ताकि सारांश पढ़ने योग्य रहे। 150px और breakpoint को अपने डिज़ाइन के अनुसार बदलें। `height: auto` चित्र का अनुपात बनाए रखता है। समान आकार में crop करना हो तभी `aspect-ratio` और `object-fit: cover` जोड़ें।

## Theme फ़ाइलें सीधे न बदलें

PaperMod के अनुसार `blank.css` उस placeholder फ़ाइल की तरह है जो extended CSS फ़ोल्डर खाली होने पर काम आती है। थीम के `post-entry.css` को बदलने या टिप्पणी वाली `/* width: 100%; */` पंक्ति हटाने की ज़रूरत नहीं है; CSS comment हटाने से style नहीं बदलता। HTML संरचना बदलनी हो तो site के `layouts/` में template की प्रति रखकर override कर सकते हैं, लेकिन theme बदलने पर उस प्रति को बनाए रखना होगा।

## लेआउट जाँचें

Hugo चलाकर home, tag और category सूचियों को चौड़ी तथा संकीर्ण स्क्रीन पर देखें। चित्र, शीर्षक, सारांश और metadata एक-दूसरे पर न चढ़ें और पूरे कार्ड का link काम करे। Theme update में classes या HTML बदलें तो CSS समायोजित करें। यह उदाहरण सूची के cover पर लागू है, लेख के अंदर की छवियों पर नहीं।

## संदर्भ

- [PaperMod FAQ: bundling custom CSS and overriding templates](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current post-entry CSS selectors](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/common/post-entry.css)
- [PaperMod discussion #159](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)
