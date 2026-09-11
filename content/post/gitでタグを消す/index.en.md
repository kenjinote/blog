---
title: 'How to Delete Local and Remote Tags in Git'
slug: "gitでタグを消す"
date: 2022-10-02T02:18:04+09:00
tags: ["git"]
draft: false
image: "img.webp"
categories: ["Tools & Development Environment"]
description: 'A simple explanation of how to delete tags that are no longer needed in Git. Covers everything from local tag deletion using ''git tag -d'' to deleting tags on the remote repository using ''git push origin --delete''.'
---
# Delete a local tag

1. Check existing local tags with `git tag`.
2. Delete the tag with `git tag -d v0.1.0`. (Replace `v0.1.0` with the tag you want to delete)

# Delete a remote tag

1. Check existing remote tags with `git ls-remote --tags`.
2. Delete the remote tag with `git push origin --delete v0.1.0`. (Replace `v0.1.0` with the tag you want to delete)

## Reference
[How to delete a tag in git locally and remotely!](https://qumeru.com/magazine/528)
