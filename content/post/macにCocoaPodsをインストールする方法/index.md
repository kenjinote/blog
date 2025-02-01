---
title: 'macにCocoaPodsをインストールする方法'
date: 2023-04-09T03:25:54+09:00
tags: ["mac", "CocoaPods", "macOS", "xcode"]
draft: false
image: "img_1.png"
---

# ターミナルでインストール
1. ターミナルを開く
2. `sudo gem install cocoapods`を実行
→なぜか下記のようなエラーメッセージが出てインストールに失敗した。

<details>
  <summary>出力</summary>

```
ERROR:  Error installing cocoapods:
	The last version of activesupport (>= 5.0, < 8) to support your Ruby & RubyGems was 6.1.7.3. Try installing it with `gem install activesupport -v 6.1.7.3` and then running the current command again
	activesupport requires Ruby version >= 2.7.0. The current ruby version is 2.6.10.210.
```

</details>

3. そこでエラーメッセージをWeb検索して（以下「参考」を参照）、下記のコマンドを実行した

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

<details>
<summary>出力</summary>

```
==> Checking for `sudo` access (which may request your password)...
==> This script will install:
/usr/local/bin/brew
/usr/local/share/doc/homebrew
/usr/local/share/man/man1/brew.1
/usr/local/share/zsh/site-functions/_brew
/usr/local/etc/bash_completion.d/brew
/usr/local/Homebrew
==> The following new directories will be created:
/usr/local/bin
/usr/local/etc
/usr/local/include
/usr/local/lib
/usr/local/sbin
/usr/local/share
/usr/local/var
/usr/local/opt
/usr/local/share/zsh
/usr/local/share/zsh/site-functions
/usr/local/var/homebrew
/usr/local/var/homebrew/linked
/usr/local/Cellar
/usr/local/Caskroom
/usr/local/Frameworks
==> The Xcode Command Line Tools will be installed.

Press RETURN/ENTER to continue or any other key to abort:
==> /usr/bin/sudo /bin/mkdir -p /usr/local/bin /usr/local/etc /usr/local/include /usr/local/lib /usr/local/sbin /usr/local/share /usr/local/var /usr/local/opt /usr/local/share/zsh /usr/local/share/zsh/site-functions /usr/local/var/homebrew /usr/local/var/homebrew/linked /usr/local/Cellar /usr/local/Caskroom /usr/local/Frameworks
==> /usr/bin/sudo /bin/chmod ug=rwx /usr/local/bin /usr/local/etc /usr/local/include /usr/local/lib /usr/local/sbin /usr/local/share /usr/local/var /usr/local/opt /usr/local/share/zsh /usr/local/share/zsh/site-functions /usr/local/var/homebrew /usr/local/var/homebrew/linked /usr/local/Cellar /usr/local/Caskroom /usr/local/Frameworks
==> /usr/bin/sudo /bin/chmod go-w /usr/local/share/zsh /usr/local/share/zsh/site-functions
==> /usr/bin/sudo /usr/sbin/chown kenji /usr/local/bin /usr/local/etc /usr/local/include /usr/local/lib /usr/local/sbin /usr/local/share /usr/local/var /usr/local/opt /usr/local/share/zsh /usr/local/share/zsh/site-functions /usr/local/var/homebrew /usr/local/var/homebrew/linked /usr/local/Cellar /usr/local/Caskroom /usr/local/Frameworks
==> /usr/bin/sudo /usr/bin/chgrp admin /usr/local/bin /usr/local/etc /usr/local/include /usr/local/lib /usr/local/sbin /usr/local/share /usr/local/var /usr/local/opt /usr/local/share/zsh /usr/local/share/zsh/site-functions /usr/local/var/homebrew /usr/local/var/homebrew/linked /usr/local/Cellar /usr/local/Caskroom /usr/local/Frameworks
==> /usr/bin/sudo /bin/mkdir -p /usr/local/Homebrew
==> /usr/bin/sudo /usr/sbin/chown -R kenji:admin /usr/local/Homebrew
==> /usr/bin/sudo /bin/mkdir -p /Users/kenji/Library/Caches/Homebrew
==> /usr/bin/sudo /bin/chmod g+rwx /Users/kenji/Library/Caches/Homebrew
==> /usr/bin/sudo /usr/sbin/chown -R kenji /Users/kenji/Library/Caches/Homebrew
==> Searching online for the Command Line Tools
==> /usr/bin/sudo /usr/bin/touch /tmp/.com.apple.dt.CommandLineTools.installondemand.in-progress
==> Installing Command Line Tools for Xcode-14.3
==> /usr/bin/sudo /usr/sbin/softwareupdate -i Command\ Line\ Tools\ for\ Xcode-14.3
Software Update Tool

Finding available software

Downloading Command Line Tools for Xcode
Downloaded Command Line Tools for Xcode
Installing Command Line Tools for Xcode
Done with Command Line Tools for Xcode
Done.
==> /usr/bin/sudo /usr/bin/xcode-select --switch /Library/Developer/CommandLineTools
==> /usr/bin/sudo /bin/rm -f /tmp/.com.apple.dt.CommandLineTools.installondemand.in-progress
==> Downloading and installing Homebrew...
remote: Enumerating objects: 236191, done.
remote: Counting objects: 100% (504/504), done.
remote: Compressing objects: 100% (327/327), done.
remote: Total 236191 (delta 176), reused 468 (delta 158), pack-reused 235687
Receiving objects: 100% (236191/236191), 68.37 MiB | 15.51 MiB/s, done.
Resolving deltas: 100% (173058/173058), done.
From https://github.com/Homebrew/brew
 * [new branch]          master       -> origin/master
 * [new branch]          test-runners -> origin/test-runners
 * [new tag]             0.1          -> 0.1
 * [new tag]             0.2          -> 0.2
 * [new tag]             0.3          -> 0.3
 * [new tag]             0.4          -> 0.4
 * [new tag]             0.5          -> 0.5
 * [new tag]             0.6          -> 0.6
 * [new tag]             0.7          -> 0.7
 * [new tag]             0.7.1        -> 0.7.1
 * [new tag]             0.8          -> 0.8
 * [new tag]             0.8.1        -> 0.8.1
 * [new tag]             0.9          -> 0.9
 * [new tag]             0.9.1        -> 0.9.1
 * [new tag]             0.9.2        -> 0.9.2
 * [new tag]             0.9.3        -> 0.9.3
 * [new tag]             0.9.4        -> 0.9.4
 * [new tag]             0.9.5        -> 0.9.5
 * [new tag]             0.9.8        -> 0.9.8
 * [new tag]             0.9.9        -> 0.9.9
 * [new tag]             1.0.0        -> 1.0.0
 * [new tag]             1.0.1        -> 1.0.1
 * [new tag]             1.0.2        -> 1.0.2
 * [new tag]             1.0.3        -> 1.0.3
 * [new tag]             1.0.4        -> 1.0.4
 * [new tag]             1.0.5        -> 1.0.5
 * [new tag]             1.0.6        -> 1.0.6
 * [new tag]             1.0.7        -> 1.0.7
 * [new tag]             1.0.8        -> 1.0.8
 * [new tag]             1.0.9        -> 1.0.9
 * [new tag]             1.1.0        -> 1.1.0
 * [new tag]             1.1.1        -> 1.1.1
 * [new tag]             1.1.10       -> 1.1.10
 * [new tag]             1.1.11       -> 1.1.11
 * [new tag]             1.1.12       -> 1.1.12
 * [new tag]             1.1.13       -> 1.1.13
 * [new tag]             1.1.2        -> 1.1.2
 * [new tag]             1.1.3        -> 1.1.3
 * [new tag]             1.1.4        -> 1.1.4
 * [new tag]             1.1.5        -> 1.1.5
 * [new tag]             1.1.6        -> 1.1.6
 * [new tag]             1.1.7        -> 1.1.7
 * [new tag]             1.1.8        -> 1.1.8
 * [new tag]             1.1.9        -> 1.1.9
 * [new tag]             1.2.0        -> 1.2.0
 * [new tag]             1.2.1        -> 1.2.1
 * [new tag]             1.2.2        -> 1.2.2
 * [new tag]             1.2.3        -> 1.2.3
 * [new tag]             1.2.4        -> 1.2.4
 * [new tag]             1.2.5        -> 1.2.5
 * [new tag]             1.2.6        -> 1.2.6
 * [new tag]             1.3.0        -> 1.3.0
 * [new tag]             1.3.1        -> 1.3.1
 * [new tag]             1.3.2        -> 1.3.2
 * [new tag]             1.3.3        -> 1.3.3
 * [new tag]             1.3.4        -> 1.3.4
 * [new tag]             1.3.5        -> 1.3.5
 * [new tag]             1.3.6        -> 1.3.6
 * [new tag]             1.3.7        -> 1.3.7
 * [new tag]             1.3.8        -> 1.3.8
 * [new tag]             1.3.9        -> 1.3.9
 * [new tag]             1.4.0        -> 1.4.0
 * [new tag]             1.4.1        -> 1.4.1
 * [new tag]             1.4.2        -> 1.4.2
 * [new tag]             1.4.3        -> 1.4.3
 * [new tag]             1.5.0        -> 1.5.0
 * [new tag]             1.5.1        -> 1.5.1
 * [new tag]             1.5.10       -> 1.5.10
 * [new tag]             1.5.11       -> 1.5.11
 * [new tag]             1.5.12       -> 1.5.12
 * [new tag]             1.5.13       -> 1.5.13
 * [new tag]             1.5.14       -> 1.5.14
 * [new tag]             1.5.2        -> 1.5.2
 * [new tag]             1.5.3        -> 1.5.3
 * [new tag]             1.5.4        -> 1.5.4
 * [new tag]             1.5.5        -> 1.5.5
 * [new tag]             1.5.6        -> 1.5.6
 * [new tag]             1.5.7        -> 1.5.7
 * [new tag]             1.5.8        -> 1.5.8
 * [new tag]             1.5.9        -> 1.5.9
 * [new tag]             1.6.0        -> 1.6.0
 * [new tag]             1.6.1        -> 1.6.1
 * [new tag]             1.6.10       -> 1.6.10
 * [new tag]             1.6.11       -> 1.6.11
 * [new tag]             1.6.12       -> 1.6.12
 * [new tag]             1.6.13       -> 1.6.13
 * [new tag]             1.6.14       -> 1.6.14
 * [new tag]             1.6.15       -> 1.6.15
 * [new tag]             1.6.16       -> 1.6.16
 * [new tag]             1.6.17       -> 1.6.17
 * [new tag]             1.6.2        -> 1.6.2
 * [new tag]             1.6.3        -> 1.6.3
 * [new tag]             1.6.4        -> 1.6.4
 * [new tag]             1.6.5        -> 1.6.5
 * [new tag]             1.6.6        -> 1.6.6
 * [new tag]             1.6.7        -> 1.6.7
 * [new tag]             1.6.8        -> 1.6.8
 * [new tag]             1.6.9        -> 1.6.9
 * [new tag]             1.7.0        -> 1.7.0
 * [new tag]             1.7.1        -> 1.7.1
 * [new tag]             1.7.2        -> 1.7.2
 * [new tag]             1.7.3        -> 1.7.3
 * [new tag]             1.7.4        -> 1.7.4
 * [new tag]             1.7.5        -> 1.7.5
 * [new tag]             1.7.6        -> 1.7.6
 * [new tag]             1.7.7        -> 1.7.7
 * [new tag]             1.8.0        -> 1.8.0
 * [new tag]             1.8.1        -> 1.8.1
 * [new tag]             1.8.2        -> 1.8.2
 * [new tag]             1.8.3        -> 1.8.3
 * [new tag]             1.8.4        -> 1.8.4
 * [new tag]             1.8.5        -> 1.8.5
 * [new tag]             1.8.6        -> 1.8.6
 * [new tag]             1.9.0        -> 1.9.0
 * [new tag]             1.9.1        -> 1.9.1
 * [new tag]             1.9.2        -> 1.9.2
 * [new tag]             1.9.3        -> 1.9.3
 * [new tag]             2.0.0        -> 2.0.0
 * [new tag]             2.0.1        -> 2.0.1
 * [new tag]             2.0.2        -> 2.0.2
 * [new tag]             2.0.3        -> 2.0.3
 * [new tag]             2.0.4        -> 2.0.4
 * [new tag]             2.0.5        -> 2.0.5
 * [new tag]             2.0.6        -> 2.0.6
 * [new tag]             2.1.0        -> 2.1.0
 * [new tag]             2.1.1        -> 2.1.1
 * [new tag]             2.1.10       -> 2.1.10
 * [new tag]             2.1.11       -> 2.1.11
 * [new tag]             2.1.12       -> 2.1.12
 * [new tag]             2.1.13       -> 2.1.13
 * [new tag]             2.1.14       -> 2.1.14
 * [new tag]             2.1.15       -> 2.1.15
 * [new tag]             2.1.16       -> 2.1.16
 * [new tag]             2.1.2        -> 2.1.2
 * [new tag]             2.1.3        -> 2.1.3
 * [new tag]             2.1.4        -> 2.1.4
 * [new tag]             2.1.5        -> 2.1.5
 * [new tag]             2.1.6        -> 2.1.6
 * [new tag]             2.1.7        -> 2.1.7
 * [new tag]             2.1.8        -> 2.1.8
 * [new tag]             2.1.9        -> 2.1.9
 * [new tag]             2.2.0        -> 2.2.0
 * [new tag]             2.2.1        -> 2.2.1
 * [new tag]             2.2.10       -> 2.2.10
 * [new tag]             2.2.11       -> 2.2.11
 * [new tag]             2.2.12       -> 2.2.12
 * [new tag]             2.2.13       -> 2.2.13
 * [new tag]             2.2.14       -> 2.2.14
 * [new tag]             2.2.15       -> 2.2.15
 * [new tag]             2.2.16       -> 2.2.16
 * [new tag]             2.2.17       -> 2.2.17
 * [new tag]             2.2.2        -> 2.2.2
 * [new tag]             2.2.3        -> 2.2.3
 * [new tag]             2.2.4        -> 2.2.4
 * [new tag]             2.2.5        -> 2.2.5
 * [new tag]             2.2.6        -> 2.2.6
 * [new tag]             2.2.7        -> 2.2.7
 * [new tag]             2.2.8        -> 2.2.8
 * [new tag]             2.2.9        -> 2.2.9
 * [new tag]             2.3.0        -> 2.3.0
 * [new tag]             2.4.0        -> 2.4.0
 * [new tag]             2.4.1        -> 2.4.1
 * [new tag]             2.4.10       -> 2.4.10
 * [new tag]             2.4.11       -> 2.4.11
 * [new tag]             2.4.12       -> 2.4.12
 * [new tag]             2.4.13       -> 2.4.13
 * [new tag]             2.4.14       -> 2.4.14
 * [new tag]             2.4.15       -> 2.4.15
 * [new tag]             2.4.16       -> 2.4.16
 * [new tag]             2.4.2        -> 2.4.2
 * [new tag]             2.4.3        -> 2.4.3
 * [new tag]             2.4.4        -> 2.4.4
 * [new tag]             2.4.5        -> 2.4.5
 * [new tag]             2.4.6        -> 2.4.6
 * [new tag]             2.4.7        -> 2.4.7
 * [new tag]             2.4.8        -> 2.4.8
 * [new tag]             2.4.9        -> 2.4.9
 * [new tag]             2.5.0        -> 2.5.0
 * [new tag]             2.5.1        -> 2.5.1
 * [new tag]             2.5.10       -> 2.5.10
 * [new tag]             2.5.11       -> 2.5.11
 * [new tag]             2.5.12       -> 2.5.12
 * [new tag]             2.5.2        -> 2.5.2
 * [new tag]             2.5.3        -> 2.5.3
 * [new tag]             2.5.4        -> 2.5.4
 * [new tag]             2.5.5        -> 2.5.5
 * [new tag]             2.5.6        -> 2.5.6
 * [new tag]             2.5.7        -> 2.5.7
 * [new tag]             2.5.8        -> 2.5.8
 * [new tag]             2.5.9        -> 2.5.9
 * [new tag]             2.6.0        -> 2.6.0
 * [new tag]             2.6.1        -> 2.6.1
 * [new tag]             2.6.2        -> 2.6.2
 * [new tag]             2.7.0        -> 2.7.0
 * [new tag]             2.7.1        -> 2.7.1
 * [new tag]             2.7.2        -> 2.7.2
 * [new tag]             2.7.3        -> 2.7.3
 * [new tag]             2.7.4        -> 2.7.4
 * [new tag]             2.7.5        -> 2.7.5
 * [new tag]             2.7.6        -> 2.7.6
 * [new tag]             2.7.7        -> 2.7.7
 * [new tag]             3.0.0        -> 3.0.0
 * [new tag]             3.0.1        -> 3.0.1
 * [new tag]             3.0.10       -> 3.0.10
 * [new tag]             3.0.11       -> 3.0.11
 * [new tag]             3.0.2        -> 3.0.2
 * [new tag]             3.0.3        -> 3.0.3
 * [new tag]             3.0.4        -> 3.0.4
 * [new tag]             3.0.5        -> 3.0.5
 * [new tag]             3.0.6        -> 3.0.6
 * [new tag]             3.0.7        -> 3.0.7
 * [new tag]             3.0.8        -> 3.0.8
 * [new tag]             3.0.9        -> 3.0.9
 * [new tag]             3.1.0        -> 3.1.0
 * [new tag]             3.1.1        -> 3.1.1
 * [new tag]             3.1.10       -> 3.1.10
 * [new tag]             3.1.11       -> 3.1.11
 * [new tag]             3.1.12       -> 3.1.12
 * [new tag]             3.1.2        -> 3.1.2
 * [new tag]             3.1.3        -> 3.1.3
 * [new tag]             3.1.4        -> 3.1.4
 * [new tag]             3.1.5        -> 3.1.5
 * [new tag]             3.1.6        -> 3.1.6
 * [new tag]             3.1.7        -> 3.1.7
 * [new tag]             3.1.8        -> 3.1.8
 * [new tag]             3.1.9        -> 3.1.9
 * [new tag]             3.2.0        -> 3.2.0
 * [new tag]             3.2.1        -> 3.2.1
 * [new tag]             3.2.10       -> 3.2.10
 * [new tag]             3.2.11       -> 3.2.11
 * [new tag]             3.2.12       -> 3.2.12
 * [new tag]             3.2.13       -> 3.2.13
 * [new tag]             3.2.14       -> 3.2.14
 * [new tag]             3.2.15       -> 3.2.15
 * [new tag]             3.2.16       -> 3.2.16
 * [new tag]             3.2.17       -> 3.2.17
 * [new tag]             3.2.2        -> 3.2.2
 * [new tag]             3.2.3        -> 3.2.3
 * [new tag]             3.2.4        -> 3.2.4
 * [new tag]             3.2.5        -> 3.2.5
 * [new tag]             3.2.6        -> 3.2.6
 * [new tag]             3.2.7        -> 3.2.7
 * [new tag]             3.2.8        -> 3.2.8
 * [new tag]             3.2.9        -> 3.2.9
 * [new tag]             3.3.0        -> 3.3.0
 * [new tag]             3.3.1        -> 3.3.1
 * [new tag]             3.3.10       -> 3.3.10
 * [new tag]             3.3.11       -> 3.3.11
 * [new tag]             3.3.12       -> 3.3.12
 * [new tag]             3.3.13       -> 3.3.13
 * [new tag]             3.3.14       -> 3.3.14
 * [new tag]             3.3.15       -> 3.3.15
 * [new tag]             3.3.16       -> 3.3.16
 * [new tag]             3.3.2        -> 3.3.2
 * [new tag]             3.3.3        -> 3.3.3
 * [new tag]             3.3.4        -> 3.3.4
 * [new tag]             3.3.5        -> 3.3.5
 * [new tag]             3.3.6        -> 3.3.6
 * [new tag]             3.3.7        -> 3.3.7
 * [new tag]             3.3.8        -> 3.3.8
 * [new tag]             3.3.9        -> 3.3.9
 * [new tag]             3.4.0        -> 3.4.0
 * [new tag]             3.4.1        -> 3.4.1
 * [new tag]             3.4.10       -> 3.4.10
 * [new tag]             3.4.11       -> 3.4.11
 * [new tag]             3.4.2        -> 3.4.2
 * [new tag]             3.4.3        -> 3.4.3
 * [new tag]             3.4.4        -> 3.4.4
 * [new tag]             3.4.5        -> 3.4.5
 * [new tag]             3.4.6        -> 3.4.6
 * [new tag]             3.4.7        -> 3.4.7
 * [new tag]             3.4.8        -> 3.4.8
 * [new tag]             3.4.9        -> 3.4.9
 * [new tag]             3.5.0        -> 3.5.0
 * [new tag]             3.5.1        -> 3.5.1
 * [new tag]             3.5.10       -> 3.5.10
 * [new tag]             3.5.2        -> 3.5.2
 * [new tag]             3.5.3        -> 3.5.3
 * [new tag]             3.5.4        -> 3.5.4
 * [new tag]             3.5.5        -> 3.5.5
 * [new tag]             3.5.6        -> 3.5.6
 * [new tag]             3.5.7        -> 3.5.7
 * [new tag]             3.5.8        -> 3.5.8
 * [new tag]             3.5.9        -> 3.5.9
 * [new tag]             3.6.0        -> 3.6.0
 * [new tag]             3.6.1        -> 3.6.1
 * [new tag]             3.6.10       -> 3.6.10
 * [new tag]             3.6.11       -> 3.6.11
 * [new tag]             3.6.12       -> 3.6.12
 * [new tag]             3.6.13       -> 3.6.13
 * [new tag]             3.6.14       -> 3.6.14
 * [new tag]             3.6.15       -> 3.6.15
 * [new tag]             3.6.16       -> 3.6.16
 * [new tag]             3.6.17       -> 3.6.17
 * [new tag]             3.6.18       -> 3.6.18
 * [new tag]             3.6.19       -> 3.6.19
 * [new tag]             3.6.2        -> 3.6.2
 * [new tag]             3.6.20       -> 3.6.20
 * [new tag]             3.6.21       -> 3.6.21
 * [new tag]             3.6.3        -> 3.6.3
 * [new tag]             3.6.4        -> 3.6.4
 * [new tag]             3.6.5        -> 3.6.5
 * [new tag]             3.6.6        -> 3.6.6
 * [new tag]             3.6.7        -> 3.6.7
 * [new tag]             3.6.8        -> 3.6.8
 * [new tag]             3.6.9        -> 3.6.9
 * [new tag]             4.0.0        -> 4.0.0
 * [new tag]             4.0.1        -> 4.0.1
 * [new tag]             4.0.10       -> 4.0.10
 * [new tag]             4.0.11       -> 4.0.11
 * [new tag]             4.0.2        -> 4.0.2
 * [new tag]             4.0.3        -> 4.0.3
 * [new tag]             4.0.4        -> 4.0.4
 * [new tag]             4.0.5        -> 4.0.5
 * [new tag]             4.0.6        -> 4.0.6
 * [new tag]             4.0.7        -> 4.0.7
 * [new tag]             4.0.8        -> 4.0.8
 * [new tag]             4.0.9        -> 4.0.9
HEAD is now at c51687009 Merge pull request #15168 from reitermarkus/api-ruby-source-path
==> Installation successful!

==> Homebrew has enabled anonymous aggregate formulae and cask analytics.
Read the analytics documentation (and how to opt-out) here:
  https://docs.brew.sh/Analytics
No analytics data has been sent yet (nor will any be during this install run).

==> Homebrew is run entirely by unpaid volunteers. Please consider donating:
  https://github.com/Homebrew/brew#donations

==> Next steps:
- Run these two commands in your terminal to add Homebrew to your PATH:
    (echo; echo 'eval "$(/usr/local/bin/brew shellenv)"') >> /Users/kenji/.zprofile
    eval "$(/usr/local/bin/brew shellenv)"
- Run brew help to get started
- Further documentation:
    https://docs.brew.sh
```

</details>

4. `brew install cocoapods`を実行

<details>
  <summary>出力</summary>

```
Warning: Treating cocoapods as a formula. For the cask, use homebrew/cask/cocoapods
==> Fetching dependencies for cocoapods: libyaml, ca-certificates, openssl@1.1, readline and ruby
==> Fetching libyaml
==> Downloading https://ghcr.io/v2/homebrew/core/libyaml/manifests/0.2.5
######################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libyaml/blobs/sha256:b49e62f014
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################## 100.0%
==> Fetching ca-certificates
==> Downloading https://ghcr.io/v2/homebrew/core/ca-certificates/manifests/2023-
######################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/ca-certificates/blobs/sha256:11
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################## 100.0%
==> Fetching openssl@1.1
==> Downloading https://ghcr.io/v2/homebrew/core/openssl/1.1/manifests/1.1.1t
######################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/openssl/1.1/blobs/sha256:97676d
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################## 100.0%
==> Fetching readline
==> Downloading https://ghcr.io/v2/homebrew/core/readline/manifests/8.2.1
######################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/readline/blobs/sha256:abe9d3f3e
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################## 100.0%
==> Fetching ruby
==> Downloading https://ghcr.io/v2/homebrew/core/ruby/manifests/3.2.2
######################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/ruby/blobs/sha256:a4ac080688e87
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################## 100.0%
==> Fetching cocoapods
==> Downloading https://ghcr.io/v2/homebrew/core/cocoapods/manifests/1.12.0
######################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/cocoapods/blobs/sha256:11226288
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################## 100.0%
==> Installing dependencies for cocoapods: libyaml, ca-certificates, openssl@1.1, readline and ruby
==> Installing cocoapods dependency: libyaml
==> Pouring libyaml--0.2.5.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/libyaml/0.2.5: 10 files, 330KB
==> Installing cocoapods dependency: ca-certificates
==> Pouring ca-certificates--2023-01-10.all.bottle.tar.gz
==> Regenerating CA certificate bundle from keychain, this may take a while...
🍺  /usr/local/Cellar/ca-certificates/2023-01-10: 3 files, 216.9KB
==> Installing cocoapods dependency: openssl@1.1
==> Pouring openssl@1.1--1.1.1t.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/openssl@1.1/1.1.1t: 8,101 files, 18.5MB
==> Installing cocoapods dependency: readline
==> Pouring readline--8.2.1.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/readline/8.2.1: 50 files, 1.7MB
==> Installing cocoapods dependency: ruby
==> Pouring ruby--3.2.2.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/ruby/3.2.2: 16,605 files, 46.3MB
==> Installing cocoapods
==> Pouring cocoapods--1.12.0.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/cocoapods/1.12.0: 13,436 files, 27.8MB
==> Running `brew cleanup cocoapods`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
```

</details>

5. `pod --version`を実行

<details>
  <summary>出力</summary>

```
1.12.0
```

</details>

一応、うまく入ったようだ。

# 参考
- [Installing "CocoaPods"](https://stackoverflow.com/questions/75755162/installing-cocoapods)