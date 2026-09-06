---
title: "So richten Sie eine benutzerdefinierte Domain in einem Github-Repository ein"
slug: "So richten Sie eine benutzerdefinierte Domain in einem Github-Repository ein"
date: 2022-09-13T01:16:40+09:00
tags: ["Github","ドメイン"]
draft: false
image: "images/octocat.png"
categories: ["ツール・開発環境"]
---
Um eine benutzerdefinierte Domain in einem Github-Repository einzurichten, müssen Sie die DNS-Einstellungen Ihrer Domain ändern.
Hier erklären wir dies unter der Annahme, dass Sie Ihre Domain mit <a href="https://px.a8.net/svt/ejp?a8mat=3TJBXA+BKRHS2+50+2HHVNM" rel="nofollow">Onamae.com</a> verwalten.
<img border="0" width="1" height="1" src="https://www19.a8.net/0.gif?a8mat=3TJBXA+BKRHS2+50+2HHVNM" alt="">
Sie können ähnliche Einstellungen vornehmen, indem Sie die A-Einträge bei anderen Registraren überschreiben.

## DNS-Einstellungen in Onamae.com ändern
Um die DNS-Einstellungen Ihrer Domain zu ändern, loggen Sie sich in den Verwaltungsbildschirm von <a href="https://px.a8.net/svt/ejp?a8mat=3TJBXA+BKRHS2+50+2HHVNM" rel="nofollow">Onamae.com</a> ein.
<img border="0" width="1" height="1" src="https://www19.a8.net/0.gif?a8mat=3TJBXA+BKRHS2+50+2HHVNM" alt="">
Gehen Sie nach dem Login zum Domain-Verwaltungsbildschirm.
Wenn Sie sich auf dem Domain-Verwaltungsbildschirm befinden, ändern Sie die DNS-Einstellungen.
Um die DNS-Einstellungen zu ändern, konfigurieren Sie sie wie folgt:
1. Greifen Sie auf https://www.onamae.com/ zu und klicken Sie auf „Onamae.com Navi Login“
2. Geben Sie Ihre „Onamae-ID (Mitglieds-ID)“ und Ihr „Passwort“ ein und klicken Sie auf den Login-Button
3. Klicken Sie auf „Nameserver-Einstellungen“
4. Klicken Sie auf „Domain-DNS-Einstellungen“
5. Wählen Sie die Domain aus, die Sie einrichten möchten, und klicken Sie auf „Weiter“
6. Klicken Sie rechts neben „DNS-Eintrags-Einstellungen verwenden“ auf „Einstellen“
7. Wählen Sie A für TYPE, geben Sie 3600 für TTL und „185.199.108.153“ für VALUE ein und klicken Sie dann auf „Hinzufügen“
8. Fügen Sie ähnlich wie bei 7. auch für „185.199.109.153“, „185.199.110.153“ und „185.199.111.153“ hinzu
9. Vergewissern Sie sich, dass das Kontrollkästchen unter „Bestätigung der Nameserver-Änderung für DNS-Eintrags-Einstellungen“ aktiviert ist, und klicken Sie auf „Zum Einstellungsbildschirm gehen“
10. Wenn ein Bildschirm mit der Meldung „Um unbeabsichtigte Änderungen der DNS-Einstellungen zu verhindern“ angezeigt wird, klicken Sie auf „Nicht einstellen“ (wählen Sie nach Bedarf aus)
11. Überprüfen Sie die Einstellungsdetails und klicken Sie auf „Einstellen“
![img.png](images/img.png)
12. Damit sind die DNS-Einstellungen abgeschlossen. Es kann bis zu etwa 72 Stunden dauern, bis die Übernahme abgeschlossen ist.
13. Wenn dies nach 72 Stunden nicht der Fall ist, versuchen Sie bitte, den Support von Onamae.com zu kontaktieren.

Um zu überprüfen, ob die Einstellungen in Ihrer lokalen Umgebung übernommen wurden, versuchen Sie, den folgenden Befehl auszuführen.
Bitte ersetzen Sie den Teil `example.com` durch die Domain, die Sie überprüfen möchten.

### Für Linux, Mac
```bash
dig example.com +noall +answer -t A
```
Wenn das Ergebnis wie folgt aussieht, wurde die Einstellung übernommen.
```bash
example.com.              0       IN      A       185.199.108.153
example.com.              0       IN      A       185.199.109.153
example.com.              0       IN      A       185.199.110.153
example.com.              0       IN      A       185.199.111.153
```

### Für Windows
```bash
nslookup -q=a example.com 8.8.8.8
```
Wenn das Ergebnis wie folgt aussieht, wurde die Einstellung übernommen.
```bash
Server:  dns.google
Address:  8.8.8.8

Nicht autorisierende Antwort:
Name:    example.com
Addresses:  185.199.108.153
          185.199.109.153
          185.199.110.153
          185.199.111.153
```

## Eine benutzerdefinierte Domain in einem Github-Repository einrichten
1. Öffnen Sie die Repository-Seite und klicken Sie auf Settings
2. Klicken Sie auf Pages
3. Wenn Sie den Quellcode des Repositories wie besehen veröffentlichen, wählen Sie unter Source „Deploy from a branch“. Wenn Sie den Quellcode erstellen (z. B. HUGO), wählen Sie „GitHub Actions“.
4. Wählen Sie in Branch den zu veröffentlichenden Branch aus und klicken Sie auf Save
5. Geben Sie die von Ihnen erhaltene Domain unter Custom domain ein und klicken Sie auf Save.
6. Aktivieren Sie bei Bedarf das Kontrollkästchen „Enforce HTTPS“, um die HTTPS-Unterstützung zu aktivieren


[PR]
<a href="https://px.a8.net/svt/ejp?a8mat=3TJBXA+BKRHS2+50+2HQGAP" rel="nofollow">
<img border="0" width="468" height="60" alt="" src="https://www24.a8.net/svt/bgt?aid=231009310700&wid=003&eno=01&mid=s00000000018015072000&mc=1"></a>
<img border="0" width="1" height="1" src="https://www14.a8.net/0.gif?a8mat=3TJBXA+BKRHS2+50+2HQGAP" alt="">
