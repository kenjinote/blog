---
title: '[Pour les débutants] Comment se connecter facilement à un bureau à distance avec TeamViewer'
date: 2023-01-13T01:45:00+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "TeamViewerで簡単Connexion à distance"
tags: ["TeamViewer", "Commande", "Connexion à Distance"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'Explique comment effectuer facilement une connexion au bureau à distance en utilisant TeamViewer. Présente également une astuce pratique pour spécifier l''ID et le mot de passe depuis la ligne de commande afin d''automatiser et d''omettre la connexion via des raccourcis.'
---
## Connexion en ligne de commande sous Windows

La documentation officielle de TeamViewer pour Windows indique que la version complète peut être lancée depuis l’invite de commandes, un script ou un raccourci.

Cet exemple lance `TeamViewer.exe` depuis son dossier d’installation. Saisissez l’ID du partenaire dans `<ID>` et son mot de passe dans `<Password>`. Si TeamViewer est installé ailleurs, remplacez le chemin de l’exécutable.

```cmd
"%ProgramFiles%\TeamViewer\TeamViewer.exe" -i <ID> -p <Password>
```

Si vous omettez `-p`, TeamViewer utilise Easy Access si cette option est disponible ; sinon, il demande le mot de passe.

Un raccourci contenant un mot de passe l’enregistre sous une forme lisible. Ne le partagez pas et ne le placez pas dans un endroit accessible à d’autres personnes. Pour un accès sans surveillance récurrent, envisagez d’associer l’appareil à votre compte et d’utiliser Easy Access, une liste d’autorisation et l’authentification multifacteur plutôt que d’enregistrer un mot de passe.

## Références officielles

- [TeamViewer command-line parameters](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/for-developers/command-line-parameters/)
- [Best practices for secure unattended access](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-classic/security/best-practices/best-practices-for-secure-unattended-access/)
- [TeamViewer security statement](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/security/security-statement/)
