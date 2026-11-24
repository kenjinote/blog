---
title: "Windows 11: चालू होने पर डिस्प्ले स्केलिंग बदले तो Fast Startup जाँचें"

slug: "मल्टी-मॉनिटरで毎回起動時にDPIの設定がリセットされてしまうときの対処法"
date: 2024-04-29T19:42:20+09:00
lastmod: "2026-11-24T00:00:00+09:00"

tags: ["मल्टीपल मॉनिटर", "DPI", "कंट्रोल पैनल"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Windows 11 में डिस्प्ले स्केलिंग बदलने पर Fast Startup को अस्थायी रूप से बंद करके जाँचें; यदि लाभ न हो तो सेटिंग वापस चालू करें।"
---
Fast Startup शटडाउन के समय kernel session और device-driver की स्थिति को hibernation फ़ाइल में सहेजता है, जिससे अगला स्टार्टअप तेज़ होता है। इसे बंद करने से स्टार्टअप धीमा हो सकता है। Microsoft दस्तावेज़ इसे मल्टी-मॉनिटर स्केलिंग रीसेट का कारण नहीं बताते; नीचे दिए चरण केवल अस्थायी जाँच हैं, प्रमाणित समाधान नहीं।

## सेटिंग अस्थायी रूप से बदलें

1. Control Panel खोलें और **Power Options** चुनें।
2. **Choose what the power buttons do** खोलें।
3. **Change settings that are currently unavailable** चुनें (व्यवस्थापक अनुमति आवश्यक हो सकती है)।
4. **Turn on fast startup (recommended)** का चेक हटाएँ और **Save changes** चुनें।
5. **Shut down** करें, फिर PC चालू करके देखें कि स्केलिंग बनी रहती है या नहीं। परीक्षण में शटडाउन के बाद पावर ऑन करें; **Restart** Fast Startup का उपयोग नहीं करता।

यदि लाभ न हो, तो उसी स्क्रीन पर Fast Startup फिर चालू करें। Windows की भाषा और अपडेट के अनुसार मेनू के नाम बदल सकते हैं।

## Microsoft संदर्भ

- [Shut down, sleep, or hibernate your PC — Microsoft Support](https://support.microsoft.com/en-us/windows/experience/power-battery/shut-down-sleep-or-hibernate-your-pc)
- [System power states — Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/power/system-power-states)
- [Distinguishing Fast Startup from Wake-from-Hibernation — Microsoft Learn](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/distinguishing-fast-startup-from-wake-from-hibernation)
