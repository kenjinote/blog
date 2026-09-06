---
title: '如何为 Github 仓库配置自定义域名'
slug: "Githubリポジトリにカスタムドメインを設定する方法"
date: 2022-09-13T01:16:40+09:00
tags: ["Github","域名"]
draft: false
image: "images/octocat.png"
categories: ["工具·开发环境"]
---
要为 Github 仓库配置自定义域名，你需要修改域名的 DNS 设置。
这里我们假设你是在
<a href="https://px.a8.net/svt/ejp?a8mat=3TJBXA+BKRHS2+50+2HHVNM" rel="nofollow">お名前.com</a>
<img border="0" width="1" height="1" src="https://www19.a8.net/0.gif?a8mat=3TJBXA+BKRHS2+50+2HHVNM" alt="">
管理你的域名来进行说明。
在其他注册商处，也可以通过重写 A 记录来进行类似的设置。




## 在お名前.com中修改 DNS 设置
要修改域名的 DNS 设置，请登录
<a href="https://px.a8.net/svt/ejp?a8mat=3TJBXA+BKRHS2+50+2HHVNM" rel="nofollow">お名前.com</a>
<img border="0" width="1" height="1" src="https://www19.a8.net/0.gif?a8mat=3TJBXA+BKRHS2+50+2HHVNM" alt="">
的管理界面。
登录后，进入域名管理界面。
进入域名管理界面后，修改 DNS 设置。
要修改 DNS 设置，请按照以下步骤操作：
1. 访问 https://www.onamae.com/ 并点击“お名前.com Navi 登录”
2. 输入“お名前ID（会员ID）”和“密码”，然后点击登录按钮
3. 点击“名称服务器设置”
4. 点击“域名的 DNS 设置”
5. 选择要设置的域名，然后点击“下一步”
6. 点击“使用 DNS 记录设置”右侧的“设置”
7. 在 TYPE 中选择 A，在 TTL 中输入 3600，在 VALUE 中输入“185.199.108.153”，然后点击“添加”
8. 按照与步骤 7 相同的方法，添加“185.199.109.153”、“185.199.110.153”和“185.199.111.153”
9. 确认勾选了“DNS 记录设置用名称服务器更改确认”，然后点击“进入设置界面”
10. 如果出现“为了防止意外的 DNS 设置更改”的界面，请点击“不设置”（可根据需要选择）
11. 确认设置内容，然后点击“设置”
![img.png](images/img.png)
12. 这样 DNS 设置就完成了。最多可能需要约 72 小时才能完成生效。
13. 如果 72 小时后仍未生效，请尝试联系お名前.com的支持人员。

要在本地环境中确认设置是否已生效，请尝试运行以下命令。
请将 `example.com` 替换为您要确认的域名。

### 对于 Linux、Mac
```bash
dig example.com +noall +answer -t A
```
如果结果如下所示，则说明设置已生效。
```bash
example.com.              0       IN      A       185.199.108.153
example.com.              0       IN      A       185.199.109.153
example.com.              0       IN      A       185.199.110.153
example.com.              0       IN      A       185.199.111.153
```

### 对于 Windows
```bash
nslookup -q=a example.com 8.8.8.8
```
如果结果如下所示，则说明设置已生效。
```bash
服务器:  dns.google
Address:  8.8.8.8

非权威应答:
名称:    example.com
Addresses:  185.199.108.153
          185.199.109.153
          185.199.110.153
          185.199.111.153
```

## 为 Github 仓库配置自定义域名
1. 打开仓库页面，点击 Settings
2. 点击 Pages
3. 如果直接发布仓库源码，在 Source 中选择“Deploy from a branch”。如果需要编译源码（如 HUGO），则选择“GitHub Actions”。
4. 在 Branch 中选择要发布的分支，然后点击 Save
5. 在 Custom domain 中输入已获取的域名，然后点击 Save。
6. 根据需要勾选“Enforce HTTPS”以启用 HTTPS 支持


[PR]
<a href="https://px.a8.net/svt/ejp?a8mat=3TJBXA+BKRHS2+50+2HQGAP" rel="nofollow">
<img border="0" width="468" height="60" alt="" src="https://www24.a8.net/svt/bgt?aid=231009310700&wid=003&eno=01&mid=s00000000018015072000&mc=1"></a>
<img border="0" width="1" height="1" src="https://www14.a8.net/0.gif?a8mat=3TJBXA+BKRHS2+50+2HQGAP" alt="">

