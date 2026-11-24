---
title: "reflog से git reset से पहले का commit वापस पाएं"
slug: "git resetを取り消す方法"
date: 2024-05-15T23:32:43+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["git", "रिस्टोर", "अनडू"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "reflog में पिछला HEAD ढूँढें, उसे branch से सुरक्षित रखें और --hard के जोखिम समझें।"
---

# reflog से git reset से पहले का commit वापस पाएं

यदि local reflog में reset से पहले वाले commit का संदर्भ है, तो उसे वापस पाया जा सकता है। `git reflog --date=local` देखें और सही `HEAD@{n}` entry चुनें; नीचे `HEAD@{1}` सिर्फ उदाहरण है।

`git reset --hard` tracked files के uncommitted बदलाव हटा देता है। पहले ज़रूरी काम का backup लें और ऐसा rescue branch नाम चुनें जो मौजूद न हो। hard reset से पहले ही खोए uncommitted संपादन reflog से वापस नहीं आते। साझा इतिहास के लिए सहयोगियों से तालमेल करें और आम तौर पर `git revert` पर विचार करें।

```sh
git reflog --date=local
git show --no-patch --oneline 'HEAD@{1}'
git branch rescue-before-reset 'HEAD@{1}'
git reset --hard rescue-before-reset
```

`HEAD@{1}` को चुनी हुई reflog entry से और `rescue-before-reset` को नए branch नाम से बदलें। आखिरी command से पहले commit जाँचें और branch बनने की पुष्टि करें।

## संदर्भ

[git reset का आधिकारिक मैनुअल](https://git-scm.com/docs/git-reset)

[git reflog का आधिकारिक मैनुअल](https://git-scm.com/docs/git-reflog)
