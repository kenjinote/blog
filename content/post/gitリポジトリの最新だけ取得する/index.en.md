---
title: 'How to Get Only the Latest Commit of a Repository with Git clone'
slug: "gitリポジトリの最新だけ取得する"
date: 2024-04-27T02:54:12+09:00
tags: ["git", "repository", "command"]
draft: false
image: "img.webp"
categories: ["Tools & Development Environment"]
description: 'We explain how to get only the latest commit (shallow clone) without downloading the entire history of a Git repository. This is a convenient technique to save disk space and quickly clone a repository using the ''--depth 1'' option.'
---

# Get only the latest of a git repository

You can get only the latest of a repository with the following command.
It is useful when you want to quickly fetch a repository to save disk space.

```
git clone --depth 1 <repository URL>
```
