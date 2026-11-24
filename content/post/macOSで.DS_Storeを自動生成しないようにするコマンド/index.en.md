---
title: "Control .DS_Store Reading on SMB Shares in macOS"
slug: "macOSで.DS_Storeを自動生成しないようにするCommand"
date: 2022-09-12T16:03:42+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["macOS"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: "Follow Apple’s instructions to disable or re-enable reading .DS_Store files on SMB shares in macOS. This does not stop file creation; log out and back in after changing the setting."
---
Apple documents this preference as a way to make SMB browsing faster by telling macOS **not to read `.DS_Store` files on SMB shares**. It does not prevent new `.DS_Store` files from being created, and it does not delete existing files. Finder’s display and sorting behavior may change.

### Disable reading on SMB shares

Run this command in Terminal:

```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE
```

Log out of your macOS account and log back in for the change to take effect. Finder will use basic information rather than `.DS_Store` metadata when displaying folders.

### Re-enable reading

Set the preference to `FALSE` to restore the default behavior:

```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool FALSE
```

Then log out and back in again. Apple presents this as an SMB browsing adjustment and notes that the guidance is intended for enterprise and education administrators. See [Apple Support](https://support.apple.com/en-us/102064).
