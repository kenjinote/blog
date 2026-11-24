---
title: "WSL में “Temporary failure resolving” त्रुटि का समाधान"
slug: "wsl で「Temporary failure resolving～」と表示される場合のसमाधान"
tags: ["WSL", "DNS", "troubleshooting"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "WSL की नाम-रिज़ॉल्यूशन समस्या को Windows नेटवर्क समस्या से अलग करके WSL अपडेट, DNS टनलिंग, VPN और फ़ायरवॉल जाँचें।"
date: "2024-03-31T16:57:33+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# WSL में “Temporary failure resolving” त्रुटि का समाधान

इस त्रुटि का अर्थ है कि WSL होस्ट नाम को IP पते में बदल नहीं सका। DNS सर्वर सेटिंग इसका केवल एक संभावित कारण है। पहले पता करें कि समस्या Windows, WSL या दोनों में है।

## पहले ये जाँचें

1. Windows PowerShell में `Resolve-DnsName archive.ubuntu.com` चलाएँ। यदि Windows में भी विफल हो, तो पहले Windows नेटवर्क, DNS और VPN जाँचें।

2. WSL में `getent hosts archive.ubuntu.com` चलाएँ। यदि Windows नाम हल कर पाता है लेकिन WSL नहीं, तो आगे के चरण अपनाएँ।

PowerShell में `wsl --update`, फिर `wsl --shutdown` चलाएँ। WSL को फिर खोलें और `getent hosts archive.ubuntu.com` तथा `sudo apt update` दोबारा आज़माएँ।

Windows 11 संस्करण 22H2 और बाद के संस्करणों में नए WSL में DNS टनलिंग डिफ़ॉल्ट रूप से चालू होती है। VPN के दौरान नाम हल न हो तो WSL अपडेट करें और `.wslconfig` के `[wsl2]` भाग में `dnsTunneling=true` बंद न हो, यह जाँचें। बदलाव के बाद PowerShell में `wsl --shutdown` चलाएँ।

`8.8.8.8` जैसे किसी भी सार्वजनिक DNS को `/etc/resolv.conf` में सीधे स्थायी रूप से न लिखें। इससे VPN या संगठन की DNS नीति बायपास हो सकती है और WSL की स्वचालित सेटिंग से टकराव हो सकता है। यदि आपके परिवेश में मैन्युअल बदलाव आवश्यक हो, तो Microsoft के VPN-विशिष्ट निर्देश अपनाएँ और नेटवर्क प्रशासक से पूछें।

## समस्या बनी रहे तो

समस्या बनी रहे तो VPN, Windows Firewall, सुरक्षा सॉफ़्टवेयर और संगठन की नेटवर्क नीतियाँ जाँचें। यदि नाम हल हो जाता है लेकिन `apt update` विफल रहता है, तो proxy, mirror और repository सेटिंग भी जाँचें।

```powershell
Resolve-DnsName archive.ubuntu.com
wsl --update
wsl --shutdown
```

```bash
getent hosts archive.ubuntu.com
sudo apt update
```

## संदर्भ

- [Microsoft Learn: WSL troubleshooting](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting)
- [Microsoft Learn: WSL networking and DNS tunneling](https://learn.microsoft.com/en-us/windows/wsl/networking)
- [Microsoft Learn: WSL configuration](https://learn.microsoft.com/en-us/windows/wsl/wsl-config)
