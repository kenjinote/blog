---
title: "Como chamar Microsoft.Windows.AI a partir de C++"
slug: "como-chamar-microsoft-windows-ai-a-partir-de-cpp"
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "Win32 API"]
draft: false
image: "img.png"
categories: ["Ferramentas e Ambiente de Desenvolvimento"]
---

# 🎯 Como chamar `Microsoft.Windows.AI` a partir de C++ [Com código de exemplo]

A partir do Windows 10, o Windows inclui nativamente um ** runtime capaz de executar modelos de IA no formato ONNX **. Esse é o ** Windows ML (Windows.AI.MachineLearning) **.

Neste artigo, explicarei de forma prática como chamar `Microsoft.Windows.AI.MachineLearning` a partir de ** C++ (baseado em aplicativo Win32) **, com ** código de exemplo **.

---

## ✅ Preparação

### ◾ Requisitos do Ambiente

* Windows 10 (1809+) ou Windows 11
* Visual Studio 2019 ou posterior (A versão Community é suficiente)
* Suporte a C++/WinRT (`Microsoft.Windows.CppWinRT`)
* Windows SDK 10.0.17763.0 ou superior

---

## ✅ Configuração do Projeto

Crie um projeto no Visual Studio com a seguinte configuração:

* Tipo: Aplicativo de Área de Trabalho do Windows em C++ (Projeto Vazio)
* Subsistema: Windows (`WinMain`)
* Adicione o seguinte pacote via NuGet:

  ```
  Microsoft.Windows.CppWinRT
  ```

---

## ✅ Código de Exemplo

Abaixo está um exemplo de configuração mínima que usa `WinMain` para combinar a API Win32 e `Windows.AI.MachineLearning`.

> ※ O modelo ONNX utilizado será chamado `model.onnx` e deve ser colocado na mesma pasta que o arquivo executável.

### `main.cpp`

```cpp
#include <windows.h>
#include <winrt/Windows.AI.MachineLearning.h>
#include <winrt/Windows.Storage.h>

#pragma comment(lib, "windowsapp") // Para linkagem WinRT

using namespace winrt;
using namespace Windows::AI::MachineLearning;
using namespace Windows::Storage;

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE, LPSTR, int nCmdShow)
{
    // Inicialização WinRT (MTA ou STA são válidos)
    winrt::init_apartment();

    try {
        // Carregar o arquivo do modelo
        auto modelFile = StorageFile::GetFileFromPathAsync(L"model.onnx").get();
        LearningModel model = LearningModel::LoadFromStorageFileAsync(modelFile).get();

        // Criar uma sessão
        LearningModelSession session(model);
        LearningModelBinding binding(session);

        // Entrada e saída do modelo (aqui temporariamente entrada vazia)
        // Na prática, é necessário fazer bind com TensorFloat, etc.

        // Executar inferência
        auto result = session.EvaluateAsync(binding, L"").get();

        MessageBox(nullptr, L"Inferência concluída", L"Windows ML (C++)", MB_OK);
    }
    catch (winrt::hresult_error const& ex) {
        MessageBox(nullptr, ex.message().c_str(), L"Erro", MB_ICONERROR);
    }

    return 0;
}
```

---

## ✅ Complemento: Como especificar Tensors de Entrada/Saída

Dependendo do modelo, ** a criação e o bind de Tensors ** são necessários antes da inferência.

Exemplo:

```cpp
// Converter um array float unidimensional para Tensor
std::vector<float> inputData = {0.5f, 0.3f, 0.2f};
std::vector<int64_t> shape = {1, 3}; // Formato: [1, 3]

auto tensor = TensorFloat::CreateFromArray(shape, inputData);

// Bind de entrada (deve corresponder ao nome de entrada do modelo)
binding.Bind(L"input_0", tensor);
```

A saída pode ser obtida de forma semelhante com `result.Outputs().Lookup(L"output_0")`.

---

## ✅ Pontos de Atenção na Depuração

* Se o arquivo do modelo não existir na pasta de execução, ocorrerá uma `FileNotFoundException`.
* Se os nomes de entrada/saída não corresponderem, resultará em um erro `invalid_argument`.
* As especificações exatas de E/S do modelo podem ser verificadas com ferramentas como o [Netron](https://netron.app).

---

## ✅ Resumo

| Item | Descrição |
| ----- | ---------------------------------- |
| API Usada | Windows.AI.MachineLearning (WinRT) |
| Linguagem | C++ (baseado em Win32) |
| Método Recomendado | Através de cabeçalhos C++/WinRT |
| Vantagens | Modelos ONNX rodam nativamente, suporte a GPU disponível |
| Atenção | Cuidado com os nomes de entrada do modelo e formato do Tensor |

---

## ✅ Alternativa: Para quem não quer usar WinRT

* Usando o `ONNX Runtime` da Microsoft, ** você pode lidar com modelos ONNX a partir de C++ de forma totalmente sem WinRT **.
* É multiplataforma, permitindo código comum entre Windows e Linux.

---

## 📌 Conclusão

O Windows ML (Microsoft.Windows.AI) é um motor de inferência de IA poderoso que pode ser perfeitamente utilizado também a partir de C++. Se você precisa de inferência nativa no Windows, não deixe de experimentar.

Para aqueles que desejam exemplos concretos de criação de modelos ONNX e binding de Tensor, explicaremos isso em artigos subsequentes!
