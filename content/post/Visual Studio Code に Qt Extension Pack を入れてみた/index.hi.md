---
title: "मैंने Visual Studio Code में Qt Extension Pack इंस्टॉल करने का प्रयास किया"
slug: "Visual Studio Code に Qt Extension Pack を入れてみた"
date: 2024-09-13T00:53:53+09:00
tags: ["Visual Studio Code", "Qt Extension Pack"]
draft: false
image: "img_1.png"
categories: ["ツール・開発環境"]
---

# VSCode में Qt डेवलपमेंट शुरू करना: Qt Extension Pack कैसे इंस्टॉल करें

नमस्ते, मैं Kenji हूँ।
इस बार मैं "Visual Studio Code (इसके बाद VSCode) में Qt डेवलपमेंट वातावरण को कैसे सेट करें" का परिचय दूंगा।

हाल ही में, आधिकारिक Qt Creator के अलावा, हल्के और अत्यधिक एक्सटेंसिबल VSCode का उपयोग करके Qt ऐप्स विकसित करने के इच्छुक लोगों की संख्या बढ़ रही है।
ऐसे लोगों के लिए, मैं **"Qt Extension Pack"** की सलाह देता हूँ।
बस इस एक्सटेंशन पैक को इंस्टॉल करने से आपको Qt से संबंधित सभी प्रमुख एक्सटेंशन एक साथ मिल जाएंगे।

---

## लक्षित दर्शक

* जो लोग Qt का उपयोग करके GUI ऐप डेवलपमेंट शुरू करना चाहते हैं
* जो लोग Qt Creator के बजाय VSCode में डेवलपमेंट करना चाहते हैं
* जिन लोगों को एक-एक करके एक्सटेंशन खोजना मुश्किल लगता है

---

## पूर्वापेक्षाएँ

* VSCode इंस्टॉल होना चाहिए
  ([आप इसे आधिकारिक वेबसाइट से मुफ्त में डाउनलोड कर सकते हैं](https://code.visualstudio.com/))
* Qt लाइब्रेरी स्वयं इंस्टॉल होनी चाहिए ([Qt की आधिकारिक वेबसाइट](https://www.qt.io/))

---

## Qt Extension Pack क्या है?

Qt Extension Pack VSCode के लिए एक एक्सटेंशन पैक है।
इसे इंस्टॉल करने से, निम्नलिखित सुविधाएँ स्वचालित रूप से जुड़ जाती हैं:

* `.ui` फ़ाइलों के लिए समर्थन (Qt Designer)
* `.pro` और `.qrc` फ़ाइलों के लिए सिंटैक्स हाइलाइटिंग
* Qt के लिए C++ कोड पूर्णता, बिल्ड और डिबग समर्थन
* Qt Resource Browser (संसाधन संदर्भ)

---

## इंस्टॉलेशन के चरण

### 1. VSCode खोलें

सबसे पहले, VSCode प्रारंभ करें।

### 2. एक्सटेंशन व्यू खोलें

"एक्सटेंशन" प्रदर्शित करने के लिए बाईं ओर एक्टिविटी बार (वर्गाकार ब्लॉक आइकन) पर क्लिक करें।

या आप शॉर्टकट के रूप में
`Ctrl + Shift + X` दबा सकते हैं।

### 3. "Qt Extension Pack" खोजें

सर्च बार में निम्नलिखित कीवर्ड दर्ज करें:

```
Qt Extension Pack
```

![img.png](img.png)

### 4. इंस्टॉल बटन पर क्लिक करें

जब लक्षित पैक प्रदर्शित हो जाए, तो "इंस्टॉल" बटन पर क्लिक करें।
इससे निम्नलिखित जैसे कई एक्सटेंशन एक ही बार में इंस्टॉल हो जाएंगे:

* Qt Language Support
* QML Support
* Qt Designer Integration
* CMake Tools (CMake संगत Qt डेवलपमेंट के लिए आवश्यक)

---

## प्रोजेक्ट सेटिंग पूरक (CMake + Qt उदाहरण)

यदि आप CMake-आधारित Qt का उपयोग करते हैं, तो निम्नलिखित एक्सटेंशन के साथ संयोजन की अनुशंसा की जाती है:

* [CMake Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)
* [CMake Language Support](https://marketplace.visualstudio.com/items?itemName=twxs.cmake)

इसके अलावा, यदि आप CMakeLists.txt में निम्नलिखित विवरण शामिल करते हैं, तो Qt के साथ एकीकरण सुचारू होगा:

```cmake
find_package(Qt6 REQUIRED COMPONENTS Widgets)
target_link_libraries(MyApp PRIVATE Qt6::Widgets)
```

---

## बोनस: मैं .ui फ़ाइलें कैसे खोलूं?

`.ui` फ़ाइलों को Qt Designer में संपादित किया जा सकता है।
VSCode में, आप `.ui` फ़ाइल पर राइट-क्लिक करने में सक्षम होंगे → `Open with Qt Designer` चुनें (पर्यावरण चर `PATH` में Qt Designer शामिल होना चाहिए)।

---

## सारांश

| चरण | सामग्री                          |
| -- | --------------------------- |
| 1  | VSCode प्रारंभ करें                    |
| 2  | एक्सटेंशन पैनल खोलें                  |
| 3  | "Qt Extension Pack" खोजें |
| 4  | इंस्टॉल बटन पर क्लिक करें              |

VSCode में Qt वातावरण बनाना पहले की तुलना में बहुत आसान हो गया है।
इसमें Qt Creator के विकल्प के रूप में पर्याप्त सुविधाएँ हैं और उन लोगों के लिए अनुशंसित है जो हल्के ढंग से काम करना चाहते हैं।

---

## अनुशंसित लिंक संग्रह

* [Qt आधिकारिक](https://www.qt.io/)
* [Qt Extension Pack - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=TheQtCompany.qt)
* [VSCode आधिकारिक](https://code.visualstudio.com/)
* [CMake Tools एक्सटेंशन](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)

---

## अंत में

भविष्य में, मैं इस वातावरण में Qt के UI टूल और QML का उपयोग करके विकास को आगे बढ़ाने की योजना बना रहा हूँ।
अगली बार, मैं **VSCode से Qt Hello World ऐप कैसे बनाएं और चलाएं** के बारे में बताऊंगा।

फिर मिलेंगे!
