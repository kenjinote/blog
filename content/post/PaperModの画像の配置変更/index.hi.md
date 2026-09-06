---
title: "PaperMod में इमेज लेआउट बदलना"
slug: "PaperMod में इमेज लेआउट बदलना"
date: 2022-09-11T18:50:40+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "images/img.png"
categories: ["ブログ運営"]
---
डिफ़ॉल्ट लेआउट में इमेज को 100% चौड़ाई के साथ केंद्र में रखा गया है,
लेकिन क्योंकि मुझे कभी-कभी यह थोड़ा बड़ा लगता था, मैंने इमेज को शीर्षक के नीचे रैप करने की कोशिश की,
और चौड़ाई को लगभग 150px में बदल दिया।

फ़ाइलों में परिवर्तन इस प्रकार हैं।

## blank.css
मार्जिन, इमेज का आकार और टेक्स्ट डिस्प्ले लाइन को बदलने के लिए, blank.css में निम्नलिखित विवरण जोड़ें।

```css:blank.css
.entry-content {
    -webkit-line-clamp: 4;
}

.entry-footer {
	text-align: right;
}

.entry-cover {
    margin-bottom: initial;
    text-align: center;
}

.entry-cover img {
    border-radius: 4px;
    display: inline;
    max-width: 100%;
}

.post-meta {
    display: block;
    text-align: right;
}
```

## post-entry.css
चूंकि मैं blank.css में परिभाषा को नहीं हटा सका, इसलिए मैंने post-entry.css में निम्नलिखित स्थान पर 1 पंक्ति हटा दी।

```css:post-entry.css
.entry-cover img {
    border-radius: var(--radius);
    pointer-events: none;
    /* width: 100%; */ ← इस लाइन को हटा दें
    height: auto;
}
```

## list.html
इमेज लेआउट को बदलने के लिए, मैंने list.html में निम्नलिखित स्थान को संशोधित किया है।

```html:list.html
<article class="{{ $class }}">
  <!-- {{- $isHidden := (site.Params.cover.hidden | default site.Params.cover.hiddenInList) }} --><!-- नीचे ले जाएँ -->
  <!-- {{- partial "cover.html" (dict "cxt" . "IsHome" true "isHidden" $isHidden) }} --><!-- नीचे ले जाएँ -->
  <header class="entry-header">
    <h2>
      {{- .Title }}
      {{- if .Draft }}<sup><span class="entry-isdraft">&nbsp;&nbsp;[draft]</span></sup>{{- end }}
    </h2>
  </header>
  <div style="display:flex;"><!-- जोड़ा गया -->
    <div style="max-width:150px;margin:11px 15px 0px 0px;"><!-- जोड़ा गया -->
      {{- $isHidden := (site.Params.cover.hidden | default site.Params.cover.hiddenInList) }}<!-- ऊपर से लाया गया -->
      {{- partial "cover.html" (dict "cxt" . "IsHome" true "isHidden" $isHidden) }}<!-- ऊपर से लाया गया -->
    </div><!-- जोड़ा गया -->
    <div style="width:100%;"><!-- जोड़ा गया -->
      {{- if (ne (.Param "hideSummary") true) }}
      <div class="entry-content">
        <p>{{ .Summary | plainify | htmlUnescape }}{{ if .Truncated }}...{{ end }}</p>
      </div>
      {{- end }}
      {{- if not (.Param "hideMeta") }}
      <footer class="entry-footer">
        {{- partial "post_meta.html" . -}}
      </footer>
      {{- end }}
      <a class="entry-link" aria-label="post link to {{ .Title | plainify }}" href="{{ .Permalink }}"></a>
    </div><!-- जोड़ा गया -->
  </div><!-- जोड़ा गया -->
</article>
```

ऐसा लगता है कि ऐसे कुछ अनुरोध नहीं हैं।

[https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)

अगर मूल डेवलपर्स भी इसका समर्थन कर सकें तो बहुत अच्छा होगा।
