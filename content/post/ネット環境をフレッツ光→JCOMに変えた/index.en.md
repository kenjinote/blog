---
title: 'Changed my internet environment from Flets Hikari to J:COM'
slug: "ネット環境をフレッツ光→JCOMに変えた"
date: 2022-09-05T22:48:51+09:00
tags: ["J:COM","Flets Hikari","Internet Connection"]
draft: false
image: "jcom.png"
categories: ["IT & Technology"]
---

# Changed my home internet environment from Flets Hikari to J:COM

![](flets_hikari.png)

![](jcom.png)

On a friend's recommendation, I changed my home internet connection from Flets Hikari to J:COM. The reasons are:

1. The monthly fee will be cheaper. 3,619 yen → 2,180 yen
2. Internet speed will increase from 100MBps to 320MBps

These points.

# Impressions after using it
It's been about a week since the switch, and so far there are almost no problems. I'll note a few things I noticed below.

After actually changing, I noticed that the download speed definitely became faster, going from 60MBps to just under 320MBps. However, the upload speed, which was around 40MBps with Flets Hikari, dropped to about 10MBps. This seems to be a specification on J:COM's side.
For now, I won't be doing any streaming or uploading massive amounts of data, so I'll wait and see.

Also, recently my family and I are mainly working remotely, and today for the first time the internet went down for a few tens of minutes. It recovered automatically, but it might not be a very good omen. It hasn't even been a week since the switch, though...

As a side note, J:COM regulates P2P communication, so it seems you won't get good speeds on P2P apps. Those who use P2P should be careful.

# About the service
At the time of signing up, I was told that if I join Netflix or Disney+, I could get 40,000 yen worth of QUO cards, which offsets the respective service contract fees and makes the average monthly fee a bit cheaper, so I signed up for the services at the same time as the contract. It seems Netflix is a 1-year contract and Disney+ is a half-year contract, and I need to complete the cancellation procedures myself.

Since it hasn't been long since the switch, if I have any additional usability issues or thoughts, I'd like to update the article again. See you,

# 09/06 It became hard to connect to the internet
- 2022/09/06 around 13:13 for about 3 to 5 minutes
- 2022/09/06 around 13:30 for about 3 to 5 minutes
- And several times after that...

![Network Diagnostics](trouble_shooting.png)

It seems DNS is the problem, so I configured the DNS server referring to [here](https://internet.watch.impress.co.jp/docs/column/shimizu/1367271.html).
We'll see how this goes... Even with the DNS setting, it fell into a state where it couldn't connect, so when I inquired with support, they said they were doing emergency maintenance... Right after inquiring, the connection status improved, so I think they took some sort of countermeasure.
