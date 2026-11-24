---
title: 'Windows में राइट-क्लिक मेनू में Hidemaru Editor का grep जोड़ने का तरीका'
date: 2024-04-03T00:00:46+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "एक्सप्लोररのराइट-क्लिक मेनूにहिडेमारू एडिटरgrepを追加する"
tags: ["Hidemaru Editor", "एक्सप्लोरर", "संदर्भ मेनू", "grep", "रजिस्ट्री"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Windows 10/11 के फाइल एक्सप्लोरर के राइट-क्लिक मेनू में Hidemaru Editor की grep सुविधा को जोड़ने के लिए सुविधाजनक सेटिंग प्रक्रिया का परिचय दिया गया है। रजिस्ट्री पंजीकरण फ़ाइल का उपयोग करके आसान तरीका समझाया गया है।'
---
यहां बताया गया है कि Windows 10/11 में एक्सप्लोरर के राइट-क्लिक मेनू (संदर्भ मेनू) में Hidemaru Editor के grep को कैसे जोड़ा जाए।

 **चेतावनी: निम्नलिखित प्रक्रिया रजिस्ट्री को बदल देती है। कृपया इसे अपने जोखिम पर करें।**

यह फ़ाइल केवल मौजूदा उपयोगकर्ता के फ़ोल्डर मेनू में विकल्प जोड़ती है; यह हर फ़ाइल में “Hidemaru से खोलें” या पूरे कंप्यूटर की सेटिंग नहीं जोड़ती। आयात से पहले Notepad में खोलकर executable पथ जाँचें या बदलें। यदि लक्षित keys पहले से हैं, तो Registry Editor में उन्हें चुनकर File > Export से बैकअप लें। Windows 11 में पुराने कमांड “Show more options” में हो सकते हैं। Windows 10 का समर्थन 14 अक्टूबर 2025 को समाप्त हुआ। शामिल removal फ़ाइल केवल मौजूदा उपयोगकर्ता की प्रविष्टियाँ हटाती है; यह पुराना system-wide registration वापस नहीं करती। यदि आपने पुरानी फ़ाइल आयात की थी, तो Registry Editor में उसकी keys अलग से जाँचकर हटाएँ।
## प्रक्रिया

1. नीचे दिए गए लिंक को खोलें और इसे किसी भी फ़ोल्डर में सहेजें।

[秀丸レジストリ登録.reg](秀丸レジストリ登録.reg)

[Hidemaru registry प्रविष्टियाँ हटाएँ](秀丸レジストリ解除.reg)

2. रजिस्ट्री में जोड़ने के लिए `秀丸レジストリ登録.reg` फ़ाइल पर डबल-क्लिक करें।

## संदर्भ

- [秀丸grepをフォルダの右クリックメニューから行う](https://aimek-developer.blogspot.com/2019/02/grep.html)

## आधिकारिक संदर्भ

- [Hidemaru startup options](https://help.maruo.co.jp/hidemaru/html/230_Option.html)
- [Microsoft: Back up and restore the registry](https://support.microsoft.com/en-us/windows/experience/backup-recovery/how-to-back-up-and-restore-the-registry-in-windows)
- [Microsoft: File Explorer context menu](https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows)
- [Microsoft: Windows 10 end of support](https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/windows-10-support-has-ended-on-october-14-2025)
- [Microsoft: reg import](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg-import)
