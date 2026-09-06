---
title: "Comment configurer un domaine personnalisé sur un dépôt Github"
slug: "Comment configurer un domaine personnalisé sur un dépôt Github"
date: 2022-09-13T01:16:40+09:00
tags: ["Github","ドメイン"]
draft: false
image: "images/octocat.png"
categories: ["ツール・開発環境"]
---
Pour configurer un domaine personnalisé sur un dépôt Github, vous devez modifier les paramètres DNS de votre domaine.
Ici, nous allons expliquer en supposant que vous gérez votre domaine avec <a href="https://px.a8.net/svt/ejp?a8mat=3TJBXA+BKRHS2+50+2HHVNM" rel="nofollow">Onamae.com</a>.
<img border="0" width="1" height="1" src="https://www19.a8.net/0.gif?a8mat=3TJBXA+BKRHS2+50+2HHVNM" alt="">
Vous pouvez effectuer des configurations similaires en réécrivant les enregistrements A avec d'autres registraires.

## Modifier les paramètres DNS sur Onamae.com
Pour modifier les paramètres DNS de votre domaine, connectez-vous à l'écran de gestion de <a href="https://px.a8.net/svt/ejp?a8mat=3TJBXA+BKRHS2+50+2HHVNM" rel="nofollow">Onamae.com</a>.
<img border="0" width="1" height="1" src="https://www19.a8.net/0.gif?a8mat=3TJBXA+BKRHS2+50+2HHVNM" alt="">
Après vous être connecté, allez à l'écran de gestion de domaine.
Une fois sur l'écran de gestion de domaine, modifiez les paramètres DNS.
Pour modifier les paramètres DNS, configurez-les comme suit :
1. Accédez à https://www.onamae.com/ et cliquez sur « Connexion Onamae.com Navi »
2. Entrez votre « ID Onamae (ID membre) » et votre « Mot de passe » et cliquez sur le bouton de connexion
3. Cliquez sur « Paramètres du serveur de noms »
4. Cliquez sur « Paramètres DNS du domaine »
5. Sélectionnez le domaine que vous souhaitez configurer et cliquez sur « Suivant »
6. Cliquez sur « Configurer » à droite de « Utiliser la configuration des enregistrements DNS »
7. Sélectionnez A pour TYPE, entrez 3600 pour TTL et « 185.199.108.153 » pour VALUE, puis cliquez sur « Ajouter »
8. Comme pour 7., ajoutez également pour « 185.199.109.153 », « 185.199.110.153 » et « 185.199.111.153 »
9. Assurez-vous que la case est cochée sous « Confirmation de modification du serveur de noms pour la configuration des enregistrements DNS », puis cliquez sur « Aller à l'écran de configuration »
10. Si un écran indiquant « Pour éviter des modifications involontaires des paramètres DNS » s'affiche, cliquez sur « Ne pas configurer » (sélectionnez selon vos besoins)
11. Vérifiez les détails de la configuration et cliquez sur « Configurer »
![img.png](images/img.png)
12. Ceci termine la configuration DNS. La prise en compte peut prendre jusqu'à environ 72 heures.
13. Si ce n'est pas pris en compte après 72 heures, essayez de contacter le support d'Onamae.com.

Pour vérifier si les paramètres sont pris en compte dans votre environnement local, essayez d'exécuter la commande suivante.
Veuillez remplacer la partie `example.com` par le domaine que vous souhaitez vérifier.

### Pour Linux, Mac
```bash
dig example.com +noall +answer -t A
```
Si le résultat est le suivant, la configuration a été prise en compte.
```bash
example.com.              0       IN      A       185.199.108.153
example.com.              0       IN      A       185.199.109.153
example.com.              0       IN      A       185.199.110.153
example.com.              0       IN      A       185.199.111.153
```

### Pour Windows
```bash
nslookup -q=a example.com 8.8.8.8
```
Si le résultat est le suivant, la configuration a été prise en compte.
```bash
Serveur:  dns.google
Address:  8.8.8.8

Réponse ne faisant pas autorité :
Nom:    example.com
Addresses:  185.199.108.153
          185.199.109.153
          185.199.110.153
          185.199.111.153
```

## Configurer un domaine personnalisé sur un dépôt Github
1. Ouvrez la page du dépôt et cliquez sur Settings
2. Cliquez sur Pages
3. Si vous publiez le code source du dépôt tel quel, sélectionnez « Deploy from a branch » dans Source. Si vous compilez le code source (comme HUGO), sélectionnez « GitHub Actions ».
4. Sélectionnez la branche à publier dans Branch et cliquez sur Save
5. Entrez le domaine que vous avez obtenu dans Custom domain, puis cliquez sur Save.
6. Si nécessaire, cochez la case « Enforce HTTPS » pour activer la prise en charge de HTTPS


[PR]
<a href="https://px.a8.net/svt/ejp?a8mat=3TJBXA+BKRHS2+50+2HQGAP" rel="nofollow">
<img border="0" width="468" height="60" alt="" src="https://www24.a8.net/svt/bgt?aid=231009310700&wid=003&eno=01&mid=s00000000018015072000&mc=1"></a>
<img border="0" width="1" height="1" src="https://www14.a8.net/0.gif?a8mat=3TJBXA+BKRHS2+50+2HQGAP" alt="">
