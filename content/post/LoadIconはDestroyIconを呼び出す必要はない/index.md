---
title: 'LoadIconはDestroyIconを呼び出す必要はない'
date: 2024-04-19T01:55:17+09:00
tags: ["アイコン", "LoadIcon", "DestroyIcon", "Windowsプログラミング"]
draft: false
---

# DestroyIconを呼び出す必要について

DestroyIcon を呼び出す必要があるのは下記の場合となる。
 
- CreateIconFromResourceEx (LR_SHARED フラグなしで呼び出された場合)
- CreateIconIndirect 
- CopyIcon

上記の関数で作成された場合。

- LoadIcon
- LoadImage ( LR_SHARED フラグを使用する場合)
- CopyImage ( LR_COPYRETURNORG フラグを使用し、 hImage パラメーターが共有アイコンの場合)
- CreateIconFromResource
- CreateIconFromResourceEx ( LR_SHARED フラグを使用する場合)

上記の場合で作成およびロードされたアイコンはDestroyIconを呼び出してはいけない。

### 参考
- [DestroyIcon 関数 (winuser.h)](https://learn.microsoft.com/ja-JP/windows/win32/api/winuser/nf-winuser-destroyicon)
