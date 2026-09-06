---
title: 'Fast Batch Deletion of Large Folders'
slug: "大きなフォルダーを高速一括削除"
date: 2022-09-20T16:04:02+09:00
tags: ["Command Prompt"]
draft: false
image: "img.png"
categories: ["IT / Technology"]
---
## Fast Batch Deletion of Large Folders
When deleting a large folder in Explorer, the deletion is executed after all the folder contents are fully searched, which is slow.
By deleting with a command as shown below, the search and deletion are executed simultaneously, allowing you to delete large folders at high speed.

1. Move to the target folder level in the Command Prompt.
2. Execute `DEL /F /Q /S folder_name > NUL`.
3. Execute `RMDIR /Q /S folder_name`.
