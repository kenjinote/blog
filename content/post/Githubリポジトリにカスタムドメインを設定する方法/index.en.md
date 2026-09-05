---
title: 'How to set up a custom domain for a Github repository'
date: 2022-09-13T01:16:40+09:00
tags: ["Github","Domain"]
draft: false
image: "images/octocat.png"
categories: ["Tools / Development Environment"]
---
To set up a custom domain for a Github repository, you need to change the domain's DNS settings.
Here, we will explain assuming that you manage your domain with 
<a href="https://px.a8.net/svt/ejp?a8mat=3TJBXA+BKRHS2+50+2HHVNM" rel="nofollow">Onamae.com</a>
<img border="0" width="1" height="1" src="https://www19.a8.net/0.gif?a8mat=3TJBXA+BKRHS2+50+2HHVNM" alt="">.
Similar settings can be applied by rewriting the A record with other registrars as well.

## Change DNS settings on Onamae.com
To change the DNS settings of your domain, log in to the management screen of
<a href="https://px.a8.net/svt/ejp?a8mat=3TJBXA+BKRHS2+50+2HHVNM" rel="nofollow">Onamae.com</a>
<img border="0" width="1" height="1" src="https://www19.a8.net/0.gif?a8mat=3TJBXA+BKRHS2+50+2HHVNM" alt="">.
After logging in, go to the domain management screen.
Once on the domain management screen, change the DNS settings.
To change the DNS settings, configure them as follows:
1. Access https://www.onamae.com/ and click "Onamae.com Navi Login"
2. Enter your "Onamae ID (Member ID)" and "Password" and click the login button
3. Click "Name Server Settings"
4. Click "Domain DNS Settings"
5. Select the domain you want to set up and click "Next"
6. Click "Set up" to the right of "Use DNS record settings"
7. Select A for TYPE, enter 3600 for TTL, enter "185.199.108.153" for VALUE, and click "Add"
8. Add "185.199.109.153", "185.199.110.153", and "185.199.111.153" in the same way as step 7.
9. Ensure that the checkbox in "Confirm name server change for DNS record settings" is checked and click "Proceed to setting screen"
10. If the screen "To prevent unintended DNS setting changes" appears, click "Do not set" (select as necessary)
11. Confirm the setting details and click "Set up"
![img.png](images/img.png)
12. This completes the DNS settings. It may take up to 72 hours for the reflection to complete.
13. If it is not reflected after 72 hours, please try contacting Onamae.com support.

To check if the settings have been reflected in your local environment, try executing the following commands.
Please replace the `example.com` part with the domain you want to check.

### For Linux and Mac
```bash
dig example.com +noall +answer -t A
```
If the result looks like the following, the settings have been reflected.
```bash
example.com.              0       IN      A       185.199.108.153
example.com.              0       IN      A       185.199.109.153
example.com.              0       IN      A       185.199.110.153
example.com.              0       IN      A       185.199.111.153
```

### For Windows
```bash
nslookup -q=a example.com 8.8.8.8
```
If the result looks like the following, the settings have been reflected.
```bash
Server:  dns.google
Address:  8.8.8.8

Non-authoritative answer:
Name:    example.com
Addresses:  185.199.108.153
          185.199.109.153
          185.199.110.153
          185.199.111.153
```

## Set a custom domain in the Github repository
1. Open the repository page and click Settings
2. Click Pages
3. If you want to publish the repository source as is, select "Deploy from a branch" in Source. If you want to build the source using HUGO or similar, select "GitHub Actions".
4. Select the branch to publish in Branch and click Save
5. Enter the acquired domain in Custom domain and click Save.
6. Check "Enforce HTTPS" as necessary to support HTTPS


[PR]
<a href="https://px.a8.net/svt/ejp?a8mat=3TJBXA+BKRHS2+50+2HQGAP" rel="nofollow">
<img border="0" width="468" height="60" alt="" src="https://www24.a8.net/svt/bgt?aid=231009310700&wid=003&eno=01&mid=s00000000018015072000&mc=1"></a>
<img border="0" width="1" height="1" src="https://www14.a8.net/0.gif?a8mat=3TJBXA+BKRHS2+50+2HQGAP" alt="">
