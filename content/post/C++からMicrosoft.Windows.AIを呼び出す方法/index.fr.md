---
title: "Comment appeler Microsoft.Windows.AI depuis C++"
slug: "comment-appeler-microsoft-windows-ai-depuis-c++"
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "Win32 API"]
draft: false
image: "img.png"
categories: ["Outils et environnement de développement"]
---

# 🎯 Comment appeler `Microsoft.Windows.AI` depuis C++ 【Avec code d'exemple】

Depuis Windows 10, Windows inclut en standard un **runtime capable d'exécuter des modèles d'IA au format ONNX** . Il s'agit de **Windows ML (Windows.AI.MachineLearning)** .

Dans cet article, nous expliquerons concrètement comment appeler `Microsoft.Windows.AI.MachineLearning` depuis **C++ (basé sur une application Win32)** avec **du code d'exemple** .

---

## ✅ Préparation

### ◾ Environnement requis

* Windows 10 (1809+) ou Windows 11
* Visual Studio 2019 ou ultérieur (l'édition Community suffit)
* Prise en charge de C++/WinRT (`Microsoft.Windows.CppWinRT`)
* Windows SDK 10.0.17763.0 ou supérieur

---

## ✅ Structure du projet

Créez un projet avec la structure suivante dans Visual Studio.

* Type : Application de bureau Windows C++ (projet vide)
* Sous-système : Windows (`WinMain`)
* Ajoutez le package suivant via NuGet

  ```
  Microsoft.Windows.CppWinRT
  ```

---

## ✅ Code d'exemple

Voici un exemple minimal utilisant `WinMain` qui combine l'API Win32 et `Windows.AI.MachineLearning`.

> ※ Le modèle ONNX utilisé sera nommé `model.onnx` et doit être placé dans le même dossier que le fichier exécutable.

### `main.cpp`

```cpp
#include <windows.h>
#include <winrt/Windows.AI.MachineLearning.h>
#include <winrt/Windows.Storage.h>

#pragma comment(lib, "windowsapp") // Pour le lien WinRT

using namespace winrt;
using namespace Windows::AI::MachineLearning;
using namespace Windows::Storage;

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE, LPSTR, int nCmdShow)
{
    // Initialisation WinRT (MTA ou STA sont acceptés)
    winrt::init_apartment();

    try {
        // Charger le fichier du modèle
        auto modelFile = StorageFile::GetFileFromPathAsync(L"model.onnx").get();
        LearningModel model = LearningModel::LoadFromStorageFileAsync(modelFile).get();

        // Créer une session
        LearningModelSession session(model);
        LearningModelBinding binding(session);

        // Entrée/Sortie du modèle (ici une entrée vide à titre d'exemple)
        // En pratique, une liaison avec TensorFloat etc. est nécessaire
        
        // Exécution de l'inférence
        auto result = session.EvaluateAsync(binding, L"").get();

        MessageBox(nullptr, L"Inférence terminée", L"Windows ML (C++)", MB_OK);
    }
    catch (winrt::hresult_error const& ex) {
        MessageBox(nullptr, ex.message().c_str(), L"Erreur", MB_ICONERROR);
    }

    return 0;
}
```

---

## ✅ Supplément : Comment spécifier les tenseurs d'entrée et de sortie

Selon le modèle, il est nécessaire de **créer et lier un tenseur (Tensor)** avant l'inférence.

Exemple :

```cpp
// Convertir un tableau float 1D en Tenseur
std::vector<float> inputData = {0.5f, 0.3f, 0.2f};
std::vector<int64_t> shape = {1, 3}; // Forme : [1, 3]

auto tensor = TensorFloat::CreateFromArray(shape, inputData);

// Liaison d'entrée (doit correspondre au nom d'entrée du modèle)
binding.Bind(L"input_0", tensor);
```

La sortie peut également être obtenue de la même manière avec `result.Outputs().Lookup(L"output_0")`.

---

## ✅ Points d'attention lors du débogage

* Si le fichier du modèle n'est pas dans le dossier d'exécution, une `FileNotFoundException` sera levée.
* Si les noms d'entrée et de sortie ne correspondent pas, une erreur `invalid_argument` se produira.
* Les spécifications exactes des E/S du modèle peuvent être vérifiées avec des outils comme [Netron](https://netron.app).

---

## ✅ Résumé

| Élément | Contenu |
| ----- | ---------------------------------- |
| API utilisée | Windows.AI.MachineLearning (WinRT) |
| Langage | C++ (basé sur Win32) |
| Méthode recommandée | Via l'en-tête C++/WinRT |
| Avantages | Les modèles ONNX fonctionnent nativement, prise en charge du GPU possible |
| Attention | Faites attention aux noms d'entrée du modèle et à la forme du tenseur |

---

## ✅ Alternative : Pour ceux qui ne veulent pas utiliser WinRT

* En utilisant `ONNX Runtime` de Microsoft, **vous pouvez gérer des modèles ONNX depuis C++ sans utiliser WinRT du tout** .
* Il est multiplateforme, permettant d'utiliser un code commun sur Windows/Linux.

---

## 📌 En conclusion

Windows ML (Microsoft.Windows.AI) est un moteur d'inférence d'IA puissant qui peut être utilisé de manière robuste même depuis C++. Si vous avez besoin d'une inférence native sous Windows, n'hésitez pas à l'essayer.

Si vous souhaitez des exemples concrets de création de modèles ONNX ou de liaison de tenseurs, nous prévoyons de les expliquer dans un prochain article !
