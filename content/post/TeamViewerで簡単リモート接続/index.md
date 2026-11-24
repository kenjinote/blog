---
title: '【初心者向け】TeamViewerで簡単にリモートデスクトップ接続をする方法'
date: 2023-01-13T01:45:00+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "TeamViewerで簡単リモート接続"
tags: ["TeamViewer", "コマンド", "リモート接続"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'TeamViewerを使って簡単にリモートデスクトップ接続を行う方法を解説します。コマンドラインからIDやパスワードを指定し、ショートカットで接続を自動化・省略する便利な小技もあわせて紹介します。'
---
## Windows版のコマンドライン接続

TeamViewer公式のWindows版コマンドライン資料に基づき、フル版のTeamViewerをコマンドプロンプト、スクリプト、ショートカットから起動できます。

次の例では、TeamViewerのインストール先にある`TeamViewer.exe`を起動します。`<ID>`には接続先のID、`<Password>`にはパスワードを指定します。実際のインストール先が異なる場合は、実行ファイルのパスを置き換えてください。

```cmd
"%ProgramFiles%\TeamViewer\TeamViewer.exe" -i <ID> -p <Password>
```

`-p`を省略すると、Easy Accessが利用できる場合はそれを使い、利用できない場合はパスワードの入力を求められます。

パスワードを含むショートカットには、パスワードが読める形で保存されます。共有したり、他人が読める場所に置いたりしないでください。常時接続が必要なら、パスワードを保存する代わりに、アカウントへのデバイス割り当て、Easy Access、許可リスト、多要素認証の利用を検討してください。

## 参考資料

- [TeamViewer command-line parameters](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/for-developers/command-line-parameters/)
- [Best practices for secure unattended access](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-classic/security/best-practices/best-practices-for-secure-unattended-access/)
- [TeamViewer security statement](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/security/security-statement/)
