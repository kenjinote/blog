---
title: "Exécuter des LLM locaux avec Ollama : installation, API REST et Python"
slug: "ollama-local-llm-api-guide"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "programming", "api"]
tags: ["Ollama", "LLM Local", "Python", "Node.js"]
date: "2026-09-11T02:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

## Installer Ollama et préparer un modèle

Téléchargez Ollama pour Windows, macOS ou Linux depuis la page officielle. Lancez l’application sous Windows ou macOS ; sous Linux, suivez la procédure officielle et démarrez le serveur s’il ne fonctionne pas déjà. Ces commandes téléchargent puis lancent un modèle nommé explicitement. Consultez la bibliothèque avant utilisation, car la disponibilité et la taille peuvent changer.

```bash
ollama pull gemma4:e2b
ollama run gemma4:e2b
```

Une fois le modèle lancé, utilisez ces commandes dans un autre terminal pour voir les modèles téléchargés et leur emplacement d’exécution. Les fichiers occupent de l’espace disque ; l’inférence requiert aussi de la mémoire vive ou GPU selon le modèle et la longueur du contexte.

```bash
ollama list
ollama ps
```

## Appeler l’API REST de chat

L’API HTTP locale est normalement disponible à `http://localhost:11434`. `/api/chat` reçoit l’historique sous forme de tableau de messages et diffuse la réponse par défaut. Cet exemple définit `stream` à `false` pour recevoir une réponse JSON complète et demande un format JSON avec `format`.

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "gemma4:e2b",
  "messages": [
    {"role": "user", "content": "Explain what a REST API is in one sentence."}
  ],
  "stream": false,
}'
```

Dans Windows PowerShell, `curl` peut être un alias d’une autre commande ; utilisez alors `curl.exe`.

Le texte de la réponse se trouve dans `message.content`. Définissez `stream` à `true` ou omettez ce champ pour recevoir des fragments successifs. Pour une seule consigne sans historique, utilisez `/api/generate` ; pour des vecteurs, `/api/embed` avec un modèle d’embeddings.

## Appeler Ollama depuis Python

La bibliothèque Python officielle gère la requête HTTP et les objets de réponse. Démarrez d’abord le serveur Ollama et téléchargez le modèle.

```bash
python -m pip install ollama
```

```python
from ollama import chat

response = chat(
    model="gemma4:e2b",
    messages=[{"role": "user", "content": "Expliquez en une phrase ce qu’est une API REST."}],
    stream=False,
)
print(response.message.content)
```

Pour afficher la sortie progressivement, définissez `stream=True` et parcourez les fragments retournés. La bibliothèque officielle propose également `AsyncClient` pour les applications asynchrones.

## Appeler Ollama depuis Node.js

Installez le paquet JavaScript officiel dans votre projet Node.js.

```bash
npm install ollama
```

```javascript
import ollama from 'ollama';

const response = await ollama.chat({
  model: 'gemma4:e2b',
  messages: [{ role: 'user', content: 'Expliquez en une phrase ce qu’est une API REST.' }],
  stream: false,
});
console.log(response.message.content);
```

## Embeddings et recherche

L’API d’embeddings transforme le texte en vecteurs. Un flux RAG élémentaire les stocke dans un index, récupère des passages pertinents et les ajoute au prompt du chat ; les embeddings ne génèrent pas eux-mêmes de réponse.

```bash
ollama pull embeddinggemma
curl http://localhost:11434/api/embed -d '{
  "model": "embeddinggemma",
  "input": "Expliquez en une phrase ce qu’est une API REST."
}'
```

La réponse contient un tableau `embeddings`. Choisissez le modèle et l’index vectoriel en fonction de la langue, des données et des licences de votre application.

## Mesurer la vitesse de génération

La réponse indique les durées de chargement, d’évaluation du prompt et de génération, ainsi que le nombre de tokens générés. `eval_duration` mesure la génération en nanosecondes ; ce n’est pas la latence totale et cette valeur exclut l’évaluation du prompt et le chargement du modèle. Estimez le débit ainsi :

$$
\text{tokens/sec} = \frac{\text{eval\_count}}{\text{eval\_duration} / 10^9}
$$

Utilisez `load_duration` pour le chargement du modèle et `prompt_eval_duration` pour l’évaluation des prompts non mis en cache. Comparez le même modèle, le même contexte et le même matériel ; le débit seul ne mesure ni la qualité ni la latence totale.

## Estimer la mémoire nécessaire

Le nombre de paramètres et la quantification donnent une estimation minimale du stockage des poids. Un modèle 8B en 4 bits demande environ 4 Go décimaux (3,73 Gio) pour les poids seuls. Ce n’est pas le besoin total : métadonnées de quantification, cache KV, longueur du contexte, moteur et autres applications demandent de la mémoire en plus.

$$
\text{weight bytes} \approx \frac{\text{parameter count} \times \text{bits per weight}}{8}
$$

`ollama ps` indique si le modèle s’exécute sur le GPU, le CPU ou les deux. La répartition réelle dépend du matériel disponible et du moteur pris en charge.

## Confidentialité, accès réseau et licences

Distinguez l’usage uniquement local des modèles cloud et des applications connectées. Avant d’envoyer des données sensibles, vérifiez le modèle, les outils et le chemin réseau. Si l’API est accessible sur un réseau local ou sur Internet, ne publiez pas le port sans contrôles d’accès comme l’authentification et un pare-feu. Vérifiez la licence de chaque modèle.

Ollama regroupe le téléchargement des modèles, l’inférence locale et l’accès depuis les applications. Les commandes et exemples d’API sont des modèles de base issus de la documentation officielle. Vérifiez les fonctions et besoins propres au modèle, puis adaptez-les à votre machine.

## Références officielles

- [Ollama Quickstart](https://docs.ollama.com/quickstart)
- [Chat API](https://docs.ollama.com/api/chat)
- [Generate API](https://docs.ollama.com/api/generate)
- [Embeddings API](https://docs.ollama.com/api/embed)
- [Local FAQ and server configuration](https://docs.ollama.com/faq)
- [Official Python library](https://github.com/ollama/ollama-python)
- [Official JavaScript library](https://github.com/ollama/ollama-js)
- [Ollama model library](https://ollama.com/library)
