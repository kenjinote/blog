---
title: 'Get only the latest of a git repository'
date: 2024-04-27T02:54:12+09:00
tags: ["git", "repository", "command"]
draft: false
image: "img.png"
categories: ["Tools & Development Environment"]
---

# Get only the latest of a git repository

You can get only the latest of a repository with the following command.
It is useful when you want to quickly fetch a repository to save disk space.

```
git clone --depth 1 <repository URL>
```
