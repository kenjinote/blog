---
title: "Google Analytics से लोकप्रिय पेज रैंकिंग प्राप्त करके प्रदर्शित करने का तरीका"
slug: "Googleアナリティクスから人気ページランキングを取得して配置する方法"
date: 2023-04-10T20:26:57+09:00
tags: ["Google Analytics", "Ranklet", "HUGO"]
draft: false
image: "img.png"
categories: ["ब्लॉग संचालन"]
---

## परिचय

`Ranklet` नामक सेवा का उपयोग करके, आप Google Analytics से लोकप्रिय पेज रैंकिंग प्राप्त करके आसानी से प्रदर्शित कर सकते हैं।

इस लेख में, मैं HUGO ब्लॉग में इसे प्रदर्शित करने का तरीका बताऊंगा।

## डेमो छवि

![img_1.png](img_1.png)

## तैयारी
- साइट पर Google Analytics सेटअप होना चाहिए

## चरण

1. `Ranklet` पर जाएं
2. `Sign in with Google` पर क्लिक करें और Google खाते से लॉग इन करें (यह Google Analytics खाते से जुड़ा होना चाहिए)
![img_2.png](img_2.png)

`अनुमति दें` पर क्लिक करें

3. बुनियादी जानकारी सेट करें

![img_3.png](img_3.png)
मैंने इसे ऊपर दिखाए अनुसार कॉन्फ़िगर किया।

- `Google Analytics View` में वह व्यू चुनें जिससे आप रैंकिंग प्राप्त करना चाहते हैं।

4. टेक्स्ट प्रतिस्थापन सेट करें

![img_4.png](img_4.png)
मैंने इसे ऊपर दिखाए अनुसार सेट किया।
पेज शीर्षक से ` | kenji.blog` को हटाने के लिए इसे सेट किया गया है।

5. टेम्प्लेट सेट करें

- HTML (रैंकिंग संख्या को छिपा दिया गया है)

```html
<div class="ranklet ranklet-reset">
    <table class="ranklet-table">
        <tbody class="ranklet-pages">
            {{#context.pages}}
            <tr class="ranklet-page">
                <td class="ranklet-image">
                    {{#image}}
                    <a href="{{url}}" class="ranklet-link">
                        <img class="ranklet-img" src="{{image}}" />
                    </a>
                    {{/image}}
                </td>
                <td class="ranklet-meta">
                    <div class="ranklet-title">
                        <a href="{{url}}" class="ranklet-link">
                            {{title}}
                        </a>
                    </div>
                    {{#description}}
                    <div class="ranklet-description">
                        <a href="{{url}}" class="ranklet-link">
                            {{description}}
                        </a>
                    </div>
                    {{/description}}
                </td>
            </tr>
            {{/context.pages}}
        </tbody>
    </table>
</div>
```

- CSS (फ़ॉन्ट आकार बदला और विवरण को 3 पंक्तियों में प्रदर्शित करने के लिए सेट किया)

```css
#ranklet-{{context.id}} {
    .ranklet-reset { // रीसेट
        table, tr, td, div, span {
            margin: 0;
            padding: 0;
            border: 0;
            font-size: 100%;
            font: inherit;
            vertical-align: baseline;
            line-height: 1;
            box-sizing: border-box;
        }
    }

    .ranklet-table {
        border-collapse: separate;
        border-spacing: 8px 24px;
        width: 100%;
        word-break: break-all;

        td {
            vertical-align: middle;
        }

        .ranklet-rank {
            text-align: center;
            font-size: 120%;
        }

        .ranklet-image {
            text-align: center;
            img {
                max-width: 128px;
                max-height: 128px;
            }
        }

        .ranklet-meta {
            .ranklet-title {
                font-size: 20px;
                line-height: 125%;
            }

            .ranklet-description {
                font-size: 16px;
                margin-top: 8px;
                line-height: 125%;
                display: -webkit-box;
                overflow: hidden;
                -webkit-box-orient: vertical;
                -webkit-line-clamp: 3; /* पंक्तियों की संख्या */
            }
        }
    }
}
```

- JavaScript में कोई बदलाव नहीं

6. "साइट पर प्रकाशित करें" से HTML कॉपी करें

![img_5.png](img_5.png)

प्रदर्शित HTML को कॉपी करें

7. HUGO टेम्प्लेट में पेस्ट करें

- `layouts/partials/ranklet.html` बनाएं और कॉपी किए गए HTML को पेस्ट करें
```html
<div id="ranklet-11958"></div><script src="//widget.ranklet.com/v1/ranklet/s3/widgets/11958/widget.js"></script>
```

- `layouts/_default/single.html` में `</footer>` से पहले वाली पंक्ति पर नीचे दिया गया कोड पेस्ट करें
```html
{{- partial "ranklet.html" . }}
```

बस इतना ही। अब रैंकिंग इस पेज के नीचे दिखाए अनुसार प्रदर्शित होगी।
