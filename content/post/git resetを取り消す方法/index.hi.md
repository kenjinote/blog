---
title: "git reset को कैसे अनडू करें"
slug: "git-reset-ko-kaise-undo-kare"
date: 2024-05-15T23:32:43+09:00
tags: ["git", "रिस्टोर", "अनडू"]
draft: false
image: "img.png"
categories: ["उपकरण और विकास पर्यावरण"]
---
# git reset को कैसे अनडू करें
git commit करने के बाद, यदि आप गलती से git reset चला देते हैं, तो यहां बताया गया है कि git reset को कैसे अनडू करें (git commit के समय की स्थिति को कैसे रिस्टोर करें)।

1. रिसेट से पहले के कमिट ID को `git reflog` से जांचें
2. `git reset --hard HEAD@{नंबर}` के साथ रिसेट से पहले की स्थिति में वापस लौटें

git reset को अनडू करने के बारे में बस इतना ही।
