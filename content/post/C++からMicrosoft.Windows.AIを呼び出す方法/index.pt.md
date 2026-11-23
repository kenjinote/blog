---
title: '[API legado] Carregar um modelo ONNX do C++ com Windows ML'
lastmod: "2026-11-23T09:00:00+09:00"
slug: "C++からMicrosoft.Windows.AIを呼び出す方法"
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "Win32 API"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Aprenda a carregar um modelo ONNX de C++/WinRT com a API legada do Windows ML para Windows 10 versão 1809 ou posterior. Veja a diferença em relação à API atual e por que a inferência exige vinculações de entrada específicas do modelo.'
---

# 🎯 Carregar um modelo ONNX do C++ com a API legada do Windows ML

> **Escopo: API legada.** Este artigo usa a API `Windows.AI.MachineLearning`, introduzida com o Windows 10 versão 1809. Ela foi [substituída pelas APIs atuais do Windows ML](https://learn.microsoft.com/en-us/windows/ai/windows-ml/api-reference). Para novos aplicativos, siga o [guia atual de introdução ao Windows ML da Microsoft](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/get-started). O código abaixo apenas carrega um modelo; não executa inferência. Para um exemplo completo, consulte o [tutorial de C++ para desktop da Microsoft](https://learn.microsoft.com/en-us/windows/ai/windows-ml/get-started-desktop).

## ✅ Preparação

### ◾ Requisitos do Ambiente

* Windows 10 (1809+) ou Windows 11
* Visual Studio 2019 ou posterior (A versão Community é suficiente)
* Integração C++/WinRT para o Windows SDK legado
* Windows SDK 10.0.17763.0 ou superior

---

## ✅ Configuração do Projeto

Para esta API legada, use Windows 10 versão 1809 (build 17763) ou posterior, um Windows SDK compatível, Visual Studio com a carga de trabalho de desktop em C++ e C++/WinRT. Não confunda os pacotes atuais do Windows ML com as dependências desta API legada. Consulte o [guia de implantação](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/distributing-your-app) para os pacotes e requisitos atuais.

---

## ✅ Código de Exemplo

> Isto verifica apenas o carregamento do modelo. Cada modelo ONNX tem nomes, tipos e formatos de entrada próprios; chamar `EvaluateAsync` sem vincular as entradas obrigatórias geralmente não executa a inferência.

### `main.cpp`

Defina o caminho absoluto real de `model.onnx`. Um caminho relativo pode ser resolvido a partir do diretório de trabalho atual, que pode não ser o diretório do executável.

```cpp
#include <windows.h>
#include <winrt/Windows.AI.MachineLearning.h>
#include <winrt/Windows.Storage.h>

#pragma comment(lib, "windowsapp")

using namespace winrt;
using namespace Windows::AI::MachineLearning;
using namespace Windows::Storage;

int WINAPI WinMain(HINSTANCE, HINSTANCE, LPSTR, int)
{
    winrt::init_apartment();

    try {
        // Replace this with the absolute path to your ONNX model.
        constexpr wchar_t modelPath[] = L"C:\\path\\to\\model.onnx";
        auto modelFile = StorageFile::GetFileFromPathAsync(modelPath).get();
        LearningModel model = LearningModel::LoadFromStorageFileAsync(modelFile).get();

        MessageBoxW(nullptr, L"Model loaded", L"Legacy Windows ML", MB_OK);
    }
    catch (winrt::hresult_error const& ex) {
        MessageBoxW(nullptr, ex.message().c_str(), L"Error", MB_OK | MB_ICONERROR);
        return static_cast<int>(ex.code().value);
    }

    return 0;
}
```

## ✅ Complemento: Exemplo de vinculação das entradas do modelo

O trecho a seguir mostra o padrão de vinculação de uma entrada. Adapte `data_0`, o tipo, o formato e os valores ao modelo. Sozinho, ele não é um programa completo que carrega o modelo e retorna resultados de inferência.

```cpp
#include <cstdint>
#include <vector>
#include <winrt/Windows.AI.MachineLearning.h>

using namespace Windows::AI::MachineLearning;

void RunWithInput(LearningModel const& model)
{
    LearningModelSession session{model};
    LearningModelBinding binding{session};

    // Example only: replace the feature name, type, shape, and values for your model.
    std::vector<float> inputData{0.5f, 0.3f, 0.2f};
    std::vector<int64_t> shape{1, 3};
    TensorFloat tensor = TensorFloat::CreateFromArray(shape, inputData);
    binding.Bind(L"data_0", tensor);

    auto result = session.Evaluate(binding, L"example");
    // Read result.Outputs() using the output feature name and type defined by the model.
}
```

Os nomes e tipos de saída também dependem do modelo. Inspecione as entradas e saídas ONNX com uma ferramenta como o Netron e vincule valores compatíveis.

[Microsoft Learn: TensorFloat::CreateFromArray](https://learn.microsoft.com/en-us/uwp/api/windows.ai.machinelearning.tensorfloat.createfromarray?view=winrt-28000) documents the API used in the binding fragment.

## ✅ Resumo

Este exemplo demonstra apenas o carregamento de modelo com a API legada `Windows.AI.MachineLearning`. Ele não garante execução na GPU nem inferência bem-sucedida para um modelo específico. Em novos projetos, escolha as APIs atuais do Windows ML e confira os requisitos de pacote e sistema operacional no guia oficial.

## ✅ Alternativa: Para quem não quer usar WinRT

* Usando o `ONNX Runtime` da Microsoft, ** você pode lidar com modelos ONNX a partir de C++ de forma totalmente sem WinRT **.
* É multiplataforma, permitindo código comum entre Windows e Linux.

---

## 📌 Conclusão

Este exemplo demonstra apenas o carregamento de modelo com a API legada `Windows.AI.MachineLearning`. Ele não garante execução na GPU nem inferência bem-sucedida para um modelo específico. Em novos projetos, escolha as APIs atuais do Windows ML e confira os requisitos de pacote e sistema operacional no guia oficial.
