---
title: 'How to Undo an Accidentally Executed git reset | Commit Restoration Steps'
slug: "git resetを取り消す方法"
date: 2024-05-15T23:32:43+09:00
tags: ["git", "restore", "undo"]
draft: false
image: "img.webp"
categories: ["Tools/Development Environment"]
description: 'We explain how to undo a reset and restore the original commit state when you accidentally execute ''git reset'' in Git. We clearly introduce the procedure to check the commit ID using ''git reflog'' and correctly revert the state.'
---
# How to undo git reset
If you accidentally run git reset after making a git commit, here is how to undo the git reset (restore the state at the time of the git commit).

1. Check the commit ID before the reset with `git reflog`
2. Revert to the state before the reset with `git reset --hard HEAD@{number}`

That's how to undo a git reset.
