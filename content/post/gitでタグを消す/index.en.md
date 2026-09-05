---
title: 'Deleting a tag in git'
date: 2022-10-02T02:18:04+09:00
tags: ["git"]
draft: false
image: "img.png"
categories: ["Tools & Development Environment"]
---
# Delete a local tag

1. Check existing local tags with `git tag`.
2. Delete the tag with `git tag -d v0.1.0`. (Replace `v0.1.0` with the tag you want to delete)

# Delete a remote tag

1. Check existing remote tags with `git ls-remote --tags`.
2. Delete the remote tag with `git push origin --delete v0.1.0`. (Replace `v0.1.0` with the tag you want to delete)

## Reference
[How to delete a tag in git locally and remotely!](https://qumeru.com/magazine/528)
