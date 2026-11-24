---
title: 'How to Delete Local and Remote Tags in Git'
slug: "gitでタグを消す"
date: 2022-10-02T02:18:04+09:00
lastmod: "2026-11-25T00:00:00+09:00"
tags: ["git"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'A simple explanation of how to delete tags that are no longer needed in Git. Covers everything from local tag deletion using ''git tag -d'' to deleting tags on the remote repository using ''git push origin --delete''.'
---
# Delete a local tag

1. Check existing local tags with `git tag`.
2. Delete the tag with `git tag -d v0.1.0`. (Replace `v0.1.0` with the tag you want to delete)

# Delete a remote tag

1. Check existing remote tags with `git ls-remote --tags --refs origin`.
2. Delete the remote tag with `git push origin --delete v0.1.0`. (Replace `v0.1.0` with the tag you want to delete)

Deleting the remote tag does not automatically remove local copies held by collaborators. Verify the target first because this affects everyone using the remote.

Deleting a tag removes that reference; it does not directly delete the commit it pointed to or rewrite other branch history. The commit will no longer be reachable by that tag name. `origin` is an example remote name, so replace it if your remote uses another name.

## References
[git-tag](https://git-scm.com/docs/git-tag), [git-ls-remote](https://git-scm.com/docs/git-ls-remote), [git-push](https://git-scm.com/docs/git-push)
