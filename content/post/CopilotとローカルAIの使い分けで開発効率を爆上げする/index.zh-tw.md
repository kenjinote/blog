---
title: "Copilot 或本機 AI？依資料邊界與實測結果選擇"
slug: "hybrid-ai-development-workflow"
date: "2026-09-11T21:00:00+09:00"
lastmod: "2026-11-23T12:00:00+09:00"
description: "依據資料政策、任務品質、延遲、成本與硬體，選擇 GitHub Copilot 等雲端工具或本機模型。"
image: "img/eyecatch.jpg"
categories: ["programming", "ai", "productivity"]
tags: ["GitHub Copilot", "Local AI", "Workflow", "Privacy"]
---

# [Copilot 或本機 AI？依資料邊界與實測結果選擇](https://kenji.blog/p/hybrid-ai-development-workflow/)

程式開發助理涵蓋 IDE 自動補全到代理式程式碼編輯。不要假設雲端一定更強、本機一定更安全。應確認傳送哪些資料、適用條款、實際任務品質、延遲和營運成本。

本文依據 2026 年 11 月 23 日核對的官方文件編寫。產品、模型、設定和政策會變動，採用前請重新確認連結和組織規範。

## 雲端 AI 與本機推論的資料路徑不同

GitHub Copilot 等雲端功能可能會依模型和 IDE 功能，將提示、程式碼片段及相關儲存庫脈絡傳送到服務。GitHub 現行政策說明，個人 Copilot 方案的互動資料可能用於模型訓練和改善，個人設定可選擇退出。GitHub 也表示，未經客戶授權，不會使用 Copilot Business 和 Enterprise 客戶資料訓練模型。請確認自己的方案、模型託管者、功能與管理員設定。

- [GitHub Copilot 個人訂閱者政策](https://docs.github.com/en/copilot/how-tos/manage-your-account/manage-policies)
- [GitHub Copilot 模型託管和資料處理方式](https://docs.github.com/en/copilot/reference/ai-models/model-hosting)

本機推論是在自己的裝置上執行模型，推論輸入可以留在本機。但選擇本機模型不代表一定完全離線。請檢查 IDE 擴充功能的遙測、同步、外部工具，以及下載模型時的網路流量。Continue 的離線指南說明如何預先準備擴充功能和模型，並關閉匿名遙測。

- [沒有網際網路時使用 Continue](https://docs.continue.dev/guides/running-continue-without-internet)

Ollama 同時提供本機 API（`http://localhost:11434`）和需使用 API 金鑰的託管雲端 API（`https://ollama.com/api`）。使用 Ollama 不代表推論一定在本機。請檢查設定中的端點。若將本機伺服器開放到網路，應另外設計存取控制。

- [Ollama API 端點與用法](https://docs.ollama.com/api/introduction)

## 依任務和資料分類選擇處理路徑

先依組織的資料分類和 AI 使用政策，決定哪些程式碼、記錄、設計文件和憑證可以離開核准環境。無論使用本機或雲端模型，都不要在提示中放入秘密資料，應改用測試值。雲端服務還需核實依方案而異的訓練用途、保留期間、濫用監控、處理地區、管理員控制和轉交模型託管者的情形。

- 日常補全、註解或測試草稿：比較品質、延遲、IDE 整合和傳送資料；使用核准的雲端功能或小型本機模型。
- 摘要或修改內部程式碼：確認輸入範圍、結果審查、合約和保留條款；使用組織核准的雲端服務或受控本機環境。
- 機密或受法規管制的程式碼：檢查外部傳送、記錄、網路邊界和稽核；需組織核准且符合要求的隔離本機環境。
- 大型設計或困難除錯：評估品質、上下文限制、工具權限和成本；採用符合要求的雲端或內部託管模型。
- 沒有網際網路的作業：預先下載模型、檢查擴充功能流量、更新和安全修補；驗證離線設定。

這不是產品效能排名，而是根據組織規範和任務評測縮小選項的起點。

## 用相同任務測量品質、延遲和成本

根據實際工作建立小型測試集，制定成功條件、失敗案例和評分方式。提供候選模型相同的程式碼和指示，記錄模型 ID、擴充功能、日期和設定。比較正確性、測試通過情況、與現有設計的一致性、安全拒絕，以及人工修正時間。輸出可能不同，應多次測試；重要程式碼由開發者審查並執行測試。

分別測量首個輸出和完整完成的時間。總成本要計入雲端用量、訂閱、重試和審查時間，以及本機硬體購置、電費和維護。本機速度與品質取決於模型大小、量化、上下文長度、GPU／記憶體和 IDE 設定。不要只根據參數數量或單一 VRAM 估值決定，應在自己的硬體上測試。

## 試用本機模型的最短流程

安裝 Ollama，並在模型目錄確認授權、下載大小和功能，再下載確切標籤：

```sh
ollama pull <model-name:tag>
```

Continue 目前的設定格式可如下登錄 Ollama。將 `<MODEL_ID>` 換成 `ollama list` 顯示的已下載模型 ID。

```yaml
name: Local coding model
version: 0.0.1
schema: v1
models:
  - name: Local model
    provider: ollama
    model: <MODEL_ID>
    apiBase: http://localhost:11434
    roles:
      - chat
```

工具呼叫、影像輸入和上下文限制會因模型而異。即使 IDE 自動偵測功能，也要實際測試。從最小權限開始；會修改檔案或執行 Shell 命令的代理必須經人工審查和核准。也要留意外部程式碼中的提示注入。

- [Ollama API](https://docs.ollama.com/api/introduction)
- [Continue 的 Ollama 設定](https://docs.continue.dev/customize/model-providers/top-level/ollama)
- [Ollama 模型庫](https://ollama.com/library)

## 從低風險工作開始，條件變動時重新評估

選擇低風險任務，以相同測試集比較核准的雲端功能和本機模型。檢視輸出品質、修正時間、延遲、成本和資料去向，並與團隊訂定各任務的規則。模型、方案、擴充功能或合約變更時，重新檢查政策和評測。

安全性不只取決於雲端或本機。了解資料處理路徑、盡量減少輸入，並在核准的環境中測試。
