---
title: "如何在 Github 儲存庫中設定自訂網域"
slug: "如何在 Github 儲存庫中設定自訂網域"
date: 2022-09-13T01:16:40+09:00
tags: ["Github","ドメイン"]
draft: false
image: "images/octocat.png"
categories: ["ツール・開発環境"]
---
要為 Github 儲存庫設定自訂網域，您需要變更網域的 DNS 設定。
在此，我們將假設您使用 <a href="https://px.a8.net/svt/ejp?a8mat=3TJBXA+BKRHS2+50+2HHVNM" rel="nofollow">Onamae.com</a> 管理您的網域。
<img border="0" width="1" height="1" src="https://www19.a8.net/0.gif?a8mat=3TJBXA+BKRHS2+50+2HHVNM" alt="">
您可以透過在其他註冊商處覆寫 A 記錄來進行類似的設定。

## 在 Onamae.com 中變更 DNS 設定
要變更網域的 DNS 設定，請登入 <a href="https://px.a8.net/svt/ejp?a8mat=3TJBXA+BKRHS2+50+2HHVNM" rel="nofollow">Onamae.com</a> 的管理畫面。
<img border="0" width="1" height="1" src="https://www19.a8.net/0.gif?a8mat=3TJBXA+BKRHS2+50+2HHVNM" alt="">
登入後，請前往網域管理畫面。
進入網域管理畫面後，請變更 DNS 設定。
要變更 DNS 設定，請按照以下步驟進行：
1. 存取 https://www.onamae.com/ 並點擊「Onamae.com Navi 登入」
2. 輸入您的「Onamae ID (會員 ID)」與「密碼」，然後點擊登入按鈕
3. 點擊「名稱伺服器設定」
4. 點擊「網域 DNS 設定」
5. 選擇您想設定的網域，然後點擊「下一步」
6. 點擊「使用 DNS 記錄設定」右側的「設定」
7. 在 TYPE 選擇 A，在 TTL 輸入 3600，在 VALUE 輸入「185.199.108.153」，然後點擊「新增」
8. 與步驟 7 相同，也為「185.199.109.153」、「185.199.110.153」和「185.199.111.153」進行新增
9. 確認已勾選「DNS 記錄設定用名稱伺服器變更確認」，然後點擊「前往設定畫面」
10. 如果出現「為了防止意外的 DNS 設定變更」畫面，請點擊「不設定」（請視需要選擇）
11. 確認設定內容，然後點擊「設定」
![img.png](images/img.png)
12. 這樣 DNS 設定就完成了。最多可能需要約 72 小時才能完成生效。
13. 如果 72 小時後仍未生效，請嘗試聯絡 Onamae.com 的支援團隊。

要確認設定是否已反映在您的本機環境中，請嘗試執行以下命令。
請將 `example.com` 替換為您想確認的網域。

### 適用於 Linux、Mac
```bash
dig example.com +noall +answer -t A
```
如果結果如下，則表示設定已反映。
```bash
example.com.              0       IN      A       185.199.108.153
example.com.              0       IN      A       185.199.109.153
example.com.              0       IN      A       185.199.110.153
example.com.              0       IN      A       185.199.111.153
```

### 適用於 Windows
```bash
nslookup -q=a example.com 8.8.8.8
```
如果結果如下，則表示設定已反映。
```bash
伺服器:  dns.google
Address:  8.8.8.8

未授權的回答:
名稱:    example.com
Addresses:  185.199.108.153
          185.199.109.153
          185.199.110.153
          185.199.111.153
```

## 在 Github 儲存庫中設定自訂網域
1. 打開儲存庫頁面，然後點擊 Settings
2. 點擊 Pages
3. 如果您要直接發佈儲存庫的原始碼，請在 Source 中選擇「Deploy from a branch」。如果您要建置原始碼（如 HUGO），請選擇「GitHub Actions」。
4. 在 Branch 中選擇要發佈的分支，然後點擊 Save
5. 在 Custom domain 中輸入您取得的網域，然後點擊 Save。
6. 如果需要，請勾選「Enforce HTTPS」以啟用 HTTPS 支援


[PR]
<a href="https://px.a8.net/svt/ejp?a8mat=3TJBXA+BKRHS2+50+2HQGAP" rel="nofollow">
<img border="0" width="468" height="60" alt="" src="https://www24.a8.net/svt/bgt?aid=231009310700&wid=003&eno=01&mid=s00000000018015072000&mc=1"></a>
<img border="0" width="1" height="1" src="https://www14.a8.net/0.gif?a8mat=3TJBXA+BKRHS2+50+2HQGAP" alt="">
