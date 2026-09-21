---
title: "PWA（漸進式網路應用程式）的潛力與實作（Service Worker 的力量）"
description: "從 PWA 的全貌到 Service Worker 的生命週期、離線快取以及推播通知進行解說。"
slug: "pwa-progressive-web-apps-service-worker"
date: "2026-09-22T08:00:00+09:00"
image: "eyecatch.jpg"
categories:
    - "frontend"
    - "web"
tags:
    - "pwa"
    - "service-worker"
    - "offline"

---

## 1. 簡介：PWA 是什麼？

網路技術在過去幾十年取得了戲劇性的進展。從靜態 HTML 文件的連結集合開始，經歷了動態 DOM 操作、透過 Ajax 的非同步通訊，以及 SPA（單頁應用程式）的出現，現在已能建立媲美甚至超越原生應用程式使用者體驗（UX）的應用程式。處於這項進化最前線的，就是 **PWA (Progressive Web Apps)**。

簡而言之，PWA 就是「兼具 Web 的可及性，以及原生應用程式高效能、高 UX 的網路應用程式」。傳統的網路應用程式，如果在離線狀態下造訪，通常會出現「未連接網際網路」的錯誤畫面（以 Chrome 來說，就是著名的恐龍遊戲畫面）。然而，只要正確實作 PWA 技術，即使在離線狀態，也能啟動應用程式、瀏覽快取的內容，或在背景執行資料同步處理。

本文將從 PWA 的全貌出發，針對其核心的 **Service Worker** 生命週期、進階快取策略、與 IndexedDB 的整合，以及未來的展望，提供非常詳細且全面的解說。

---

## 2. 原生應用程式 vs PWA

在開發網路應用程式時，「該選擇原生應用程式還是 PWA？」始終是爭論的焦點。深入了解兩者的優缺點，才能為專案選定最合適的技術。

### 2.1. 原生應用程式的優勢與劣勢

原生應用程式（針對 iOS 使用 Swift/Objective-C，Android 使用 Kotlin/Java 等開發的應用程式）最大的優勢，就是擁有對 OS API 的完全存取權限。
這使得它能夠充分利用相機、GPS、藍牙、NFC 以及各種感測器等，實現進階功能。此外，由於針對 OS 進行了最佳化，繪圖效能極高，對於大量使用複雜動畫或 3D 圖形的遊戲等，原生應用程式具有壓倒性的優勢。

另一方面，原生應用程式存在以下幾個明顯的弱點（挑戰）：

- ** 開發成本與學習成本 **：需要分別維護 iOS 和 Android 的程式碼庫（雖然可以透過 React Native 或 Flutter 等跨平台框架減輕負擔，但無法完全歸零）。
- ** 應用程式商店的審查 **：必須通過 Apple 的 App Store 或 Google Play 的審查才能發布，更新時也可能會產生數天的審查等待時間。
- ** 獲取使用者的門檻 **：打開應用程式商店、搜尋、下載到安裝的過程，對使用者來說是一大麻煩（阻力）。

### 2.2. PWA 解決的挑戰

PWA 旨在發揮 Web 優勢的同時，克服原生應用程式的弱點。

- ** 單一原始碼，多平台使用 **：利用 HTML、CSS、JavaScript 等網頁標準技術開發的單一程式碼庫，即可在所有搭載瀏覽器的裝置（手機、平板、桌上型電腦）上運作。
- ** 免審查，立即更新 **：因為 PWA 本質上只是一個網站，所以不需要通過應用程式商店的審查。只要更新伺服器上的檔案，使用者就能隨時使用最新版本。
- ** 免安裝的無縫體驗 **：使用者只需造訪 URL 即可開始使用應用程式。如果喜歡，透過「加入主畫面（Install）」，就能像原生應用程式一樣從圖示啟動。
- ** 透過連結分享 **：能將特定畫面或狀態作為 URL 分享，是 Web 特有的強大武器。

當然，PWA 也有其限制。特別是在 iOS（Safari）環境中，由於 Apple 的方針，Web API 的實作往往較為落後，例如直到最近對推播通知的支援仍不夠完善，或是對背景執行有嚴格的限制。然而，近年來 Safari 也加強了對 PWA 的支援，兩者的差距正在逐漸縮小。

---

## 3. 構成 PWA 的三大支柱

要實現 PWA，需要以下三個主要的技術要素。

### 3.1. HTTPS (安全的通訊)

基於安全性考量，PWA 的強大功能（Service Worker、推播通知、Geolocation 等）只能在 **HTTPS** 環境下運作（作為例外的本機開發環境 `localhost` 則被允許）。這是為了防止這些功能遭到惡意第三方的中間人攻擊等篡改或濫用。

### 3.2. Web App Manifest

Web App Manifest（ `manifest.json` ）是向瀏覽器提供關於網路應用程式詮釋資料的 JSON 檔案。這能定義應用程式的圖示、名稱、主題顏色、顯示模式等，以控制安裝到裝置時類似原生應用程式的外觀。

### 3.3. Service Worker

Service Worker 才是將 PWA 從單純的網站昇華為「應用程式」的魔法棒。這是一個由瀏覽器在背景執行的 JavaScript 環境，與網頁在不同的執行緒中運作。它可以攔截（代理）網路請求、管理快取、或接收推播通知。

---

## 4. Web App Manifest 詳細設定

Web App Manifest 可說是 PWA 的門面設定檔。它決定了使用者安裝應用程式時的外觀與行為。

以下是常見的 `manifest.json` 設定範例：

```json
{
  "name": "Progressive Web App Example",
  "short_name": "PWA Example",
  "description": "A comprehensive example of a Progressive Web App.",
  "start_url": "/?source=pwa",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#0055ff",
  "icons": [
    {
      "src": "/images/icons/icon-192x192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "any maskable"
    },
    {
      "src": "/images/icons/icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ],
  "orientation": "portrait",
  "scope": "/"
}
```

### 主要屬性解說

- **name** 與 **short_name**：在安裝提示或主畫面應用程式圖示下方顯示的名稱。在空間有限的主畫面上會優先使用 `short_name`。
- **start_url**：使用者從主畫面圖示啟動應用程式時，最初載入的 URL。透過附加追蹤參數（例如： `?source=pwa` ），即可在流量分析工具中判別來自 PWA 的存取。
- **display**：指定應用程式的顯示模式。
  - `standalone`：完全隱藏瀏覽器的 UI（如 URL 列和返回按鈕），像原生應用程式一樣顯示。這是最推薦的設定。
  - `fullscreen`：使用整個畫面，甚至隱藏狀態列（最適合遊戲或影片應用程式）。
  - `minimal-ui`：只顯示基本的導覽 UI。
  - `browser`：作為一般的瀏覽器分頁顯示。
- **theme_color** 與 **background_color**：定義應用程式的主題顏色，以及啟動時啟動畫面的背景色。
- **icons**：作為應用程式圖示使用的圖片陣列。為了對應不同的裝置解析度，建議準備多種尺寸（至少 192x192 和 512x512）。指定 `purpose: "maskable"` 可在 Android 等系統上將圖示裁切最佳化。

---

## 5. Service Worker 的核心與生命週期

Service Worker 堪稱 PWA 的「心臟」。與以往在網頁內執行的 JavaScript 不同，它沒有存取 DOM 的權限。取而代之的是，它負責仲介網路請求、操作快取、以及背景同步處理等。

### 5.1. Service Worker 的生命週期

Service Worker 擁有與網頁獨立的專屬生命週期。正確理解這個生命週期，是防止發生意外的快取問題（例如已更新但畫面卻沒改變等）的關鍵。

以下的 Mermaid 圖表呈現了 Service Worker 的狀態轉換。

```mermaid
stateDiagram-v2
    direction TB
    "Parsed" --> "Installing" : "Registration"
    "Installing" --> "Installed (Waiting)" : "Success"
    "Installing" --> "Redundant" : "Error"
    "Installed (Waiting)" --> "Activating" : "All clients closed / skipWaiting()"
    "Activating" --> "Activated" : "Success"
    "Activating" --> "Redundant" : "Error"
    "Activated" --> "Redundant" : "Replaced by new SW"
```

1. **Parsed (已解析)**：瀏覽器下載 Service Worker 的腳本並完成語法解析的狀態。
2. **Installing (安裝中)**：觸發 `install` 事件的狀態。這個階段主要用於快取（Pre-caching）應用程式運作不可或缺的靜態資源（HTML、CSS、JS、圖片等）。若安裝失敗（例如儲存快取失敗），Service Worker 將被捨棄。
3. **Installed / Waiting (待命中)**：安裝已完成，但由於現有舊版的 Service Worker 仍在其他分頁中活躍運作，因此處於等待交接的狀態。使用者關閉所有分頁並重新開啟，或是呼叫 `self.skipWaiting()` 即可進入下一個階段。
4. **Activating (啟用中)**：觸發 `activate` 事件的狀態。這個階段主要用於清理舊版 Service Worker 所建立的無用快取，執行清理作業。
5. **Activated (已啟用)**：完全運作，能控制並處理來自網頁的 `fetch` 事件或 `push` 事件的狀態。
6. **Redundant (已捨棄)**：安裝失敗、啟用失敗，或被新版 Service Worker 替換掉的狀態。

### 5.2. 註冊 Service Worker

要使用 Service Worker，首先必須從主 JavaScript 執行緒進行註冊。

```javascript
// main.js 或 index.html 的 <script> 內
if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker
      .register("/sw.js", { scope: "/" })
      .then((registration) => {
        console.log("ServiceWorker 註冊成功，範圍為: ", registration.scope);
      })
      .catch((error) => {
        console.error("ServiceWorker 註冊失敗: ", error);
      });
  });
}
```

這裡重要的是 Service Worker 的範圍（scope）。預設情況下，它只會攔截 Service Worker 檔案所在目錄以下的請求。換言之，如果是 `/sw.js`，就能攔截整個網站 `/` 的請求，但如果放在 `/js/sw.js`，就只能攔截 `/js/` 以下的請求。

---

## 6. 快取策略的完整指南

Service Worker 最大的魅力在於，可以攔截網路請求（ `fetch` 事件），並實作專屬的快取策略。根據資源的類型（圖片、API 回應、HTML）和應用程式的需求，必須靈活運用合適的快取策略。

### 6.1. Cache First (快取優先)

最基本且快速的策略。首先檢查快取，如果存在就回傳快取；如果不存在再去網路取得，並將結果儲存至快取。非常適合圖片檔或字型等不常變更的靜態資源。

```mermaid
flowchart TD
    "Page" -->|"1. Request"| "Service Worker"
    "Service Worker" -->|"2. Check Cache"| "Cache"
    "Cache" -->|"3a. Cache Hit"| "Service Worker"
    "Service Worker" -->|"4a. Response"| "Page"
    "Cache" -->|"3b. Cache Miss"| "Network"
    "Network" -->|"4b. Response"| "Service Worker"
    "Service Worker" -->|"5b. Save to Cache"| "Cache"
    "Service Worker" -->|"6b. Response"| "Page"
```

### 6.2. Network First (網路優先)

始終以取得最新資料為優先的策略。首先向網路發出請求，若成功則將結果存入快取並回傳給網頁。只有在離線狀態等網路通訊失敗時，才會退而求其次（Fallback）使用快取。適合頻繁更新的文章資料或 API 回應。

```mermaid
flowchart TD
    "Page" -->|"1. Request"| "Service Worker"
    "Service Worker" -->|"2. Fetch"| "Network"
    "Network" -->|"3a. Success"| "Service Worker"
    "Service Worker" -->|"4a. Save to Cache"| "Cache"
    "Service Worker" -->|"5a. Response"| "Page"
    "Network" -->|"3b. Error / Offline"| "Service Worker"
    "Service Worker" -->|"4b. Check Cache"| "Cache"
    "Cache" -->|"5b. Cache Hit"| "Service Worker"
    "Service Worker" -->|"6b. Fallback Response"| "Page"
```

### 6.3. Stale-while-revalidate (回傳舊快取的同時在背景更新)

兼顧速度與新鮮度，是非常強大且現代的策略。
發生請求時，立即回傳快取（舊的、Stale 的資料）以快速繪製畫面。同時，在背景（while-revalidate）向網路發送請求，取得最新資料並更新快取。使用者在下次造訪時就會看到最新的資料。

```mermaid
flowchart TD
    "Page" -->|"1. Request"| "Service Worker"
    "Service Worker" -->|"2. Check Cache"| "Cache"
    "Cache" -->|"3. Cache Hit (Fast Response)"| "Service Worker"
    "Service Worker" -->|"4. Return Stale Response"| "Page"
    "Service Worker" -.->|"5. Fetch (Background)"| "Network"
    "Network" -.->|"6. Network Response"| "Service Worker"
    "Service Worker" -.->|"7. Update Cache"| "Cache"
```

### 6.4. Cache Only / Network Only

- **Cache Only**：完全只從快取回傳回應。如果不存在就會發生錯誤。僅用於確保事先已確實下載完畢的特定資源。
- **Network Only**：完全不看快取，總是向網路發出請求。用於身分驗證 API 或 POST 請求等不該被快取的通訊。

---

## 7. Service Worker 實作範例（程式碼詳解）

那麼，基於上述的生命週期與快取策略，讓我們來看看實際的 `sw.js`（Service Worker 檔案）實作範例。

### 7.1. 安裝事件與預先快取

在 `install` 事件中，會預先快取應用程式的外殼（基本的 HTML、CSS、JS）。這樣一來，即使是下次存取或離線時，也能立刻顯示應用程式的框架。

```javascript
// sw.js
const CACHE_NAME = "pwa-cache-v1";
const PRECACHE_URLS = [
  "/",
  "/index.html",
  "/css/style.css",
  "/js/app.js",
  "/images/logo.png",
  "/offline.html"
];

self.addEventListener("install", (event) => {
  console.log("[ServiceWorker] 安裝事件");
  
  // 透過呼叫 self.skipWaiting()，跳過待命狀態並立即啟用。
  self.skipWaiting();

  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log("[ServiceWorker] 預先快取離線頁面");
      return cache.addAll(PRECACHE_URLS);
    })
  );
});
```

### 7.2. 啟用事件與清理快取

當更改快取名稱的版本（例如：從 `pwa-cache-v1` 變為 `v2`）時，必須刪除舊的無用快取以節省儲存空間。這會在 `activate` 事件中進行。

```javascript
self.addEventListener("activate", (event) => {
  console.log("[ServiceWorker] 啟用事件");
  
  // 透過 self.clients.claim() 立即接管所有目前開啟的頁面。
  event.waitUntil(self.clients.claim());

  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            console.log("[ServiceWorker] 刪除舊快取:", cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
```

### 7.3. 處理 Fetch 事件

攔截 `fetch` 事件，並根據請求的資源類型切換策略的進階實作範例。可以分歧處理：圖片使用 Cache First，HTML 導覽請求使用 Network First 加上 Fallback（退而求其次）等。

```javascript
self.addEventListener("fetch", (event) => {
  const request = event.request;
  const url = new URL(request.url);

  // POST 請求或對外部網域的請求直接放行給網路
  if (request.method !== "GET") return;

  // HTML 請求（頁面跳轉）使用 Network First 策略 + 離線 Fallback
  if (request.mode === "navigate" || request.headers.get("accept").includes("text/html")) {
    event.respondWith(
      fetch(request)
        .then((response) => {
          return caches.open(CACHE_NAME).then((cache) => {
            cache.put(request, response.clone());
            return response;
          });
        })
        .catch(() => {
          // 網路錯誤（離線）時從快取取得，若無則回傳專屬的離線頁面
          return caches.match(request).then((cachedResponse) => {
            return cachedResponse || caches.match("/offline.html");
          });
        })
    );
    return;
  }

  // 圖片等靜態資源使用 Cache First 策略
  if (url.pathname.match(/\.(png|jpg|jpeg|gif|svg|css|js)$/)) {
    event.respondWith(
      caches.match(request).then((cachedResponse) => {
        if (cachedResponse) {
          return cachedResponse;
        }
        return fetch(request).then((networkResponse) => {
          return caches.open(CACHE_NAME).then((cache) => {
            cache.put(request, networkResponse.clone());
            return networkResponse;
          });
        });
      })
    );
    return;
  }

  // 其他 API 請求等套用 Stale-while-revalidate
  event.respondWith(
    caches.match(request).then((cachedResponse) => {
      const fetchPromise = fetch(request).then((networkResponse) => {
        return caches.open(CACHE_NAME).then((cache) => {
          cache.put(request, networkResponse.clone());
          return networkResponse;
        });
      });
      // 如果有快取就先回傳，並在背景繼續發送請求處理。如果沒有快取就等待 fetchPromise。
      return cachedResponse || fetchPromise;
    })
  );
});
```

---

## 8. 與 IndexedDB 整合：更進階的資料管理

Service Worker 的 `caches` API（Cache Storage）非常適合用來儲存整個 HTTP 回應（HTML 檔案、圖片、CSS 等）。然而，對於管理應用程式處理的結構化資料（JSON 格式的 API 回應、使用者設定資料、離線時發布的文字資料等）而言，這可能還不夠。

這時就輪到 **IndexedDB** 登場了。

IndexedDB 是內建於瀏覽器的非同步交易式 NoSQL 資料庫。它可以儲存非常大量的資料，並支援複雜的索引搜尋。

### 8.1. 為什麼只有 Cache Storage 還不夠？

舉例來說，假設在待辦事項應用程式中，於離線狀態時新增了一項新任務。此時，要將「新增任務的 POST 請求」本身儲存到 Cache Storage 是很困難的。
若要在離線時儲存操作動作，並在恢復連線時重新傳送，就需要這樣的整合：先將任務資料暫存在 IndexedDB 中，並在背景同步（後述）的時機從資料庫取出資料並發送至 API。

### 8.2. 在 Service Worker 內使用 IndexedDB

從 Service Worker 的範圍內也可以存取 IndexedDB。由於直接操作 IndexedDB API 的程式碼往往較為繁瑣，一般會使用 Google 提供的 `idb` 這個輕量級包裝函式庫。

在具備進階離線功能的 PWA 中，它將從 API 取得的文章列表 JSON 存入 IndexedDB 而非快取 API，並進行細緻的管理與查詢，此時 IndexedDB 就扮演著重要的角色。

---

## 9. 推播通知與背景同步 (Background Sync)

讓 PWA 最接近原生應用程式的功能，就是推播通知與背景執行。

### 9.1. Web Push API

Web Push 是一種即使應用程式未開啟，也能由伺服器啟動 Service Worker 將通知送達使用者的機制。

1. ** 訂閱 (Subscribe)**：在瀏覽器端請求使用者允許通知，取得 Push 服務的訂閱資訊（端點和加密金鑰）並儲存在自家伺服器。
2. ** 傳送 (Push)**：從自家伺服器向瀏覽器廠商的 Push 服務（FCM 或 Apple Push Notification service）傳送訊息。
3. ** 接收 (Push Event)**：當 Push 服務將資料傳送到裝置時，瀏覽器會在背景啟動 Service Worker 並觸發 `push` 事件。Service Worker 呼叫 `self.registration.showNotification()` 方法，顯示 OS 原生的通知 UI。

```javascript
self.addEventListener("push", (event) => {
  const data = event.data ? event.data.json() : {};
  const title = data.title || "有新訊息";
  const options = {
    body: data.body || "請打開應用程式確認。",
    icon: "/images/icons/icon-192x192.png",
    badge: "/images/icons/badge.png",
  };

  event.waitUntil(self.registration.showNotification(title, options));
});
```

### 9.2. Background Sync (背景同步)

假設使用者在離線的地下鐵車廂內按下了傳送訊息按鈕。在一般的網路應用程式中這會發生錯誤，但如果使用 Background Sync API，瀏覽器就會看準「網路連線恢復的時機」，在 Service Worker 中觸發 `sync` 事件。

應用程式端會在離線時將資料暫存至 IndexedDB，並向 Service Worker 註冊同步任務（ `registration.sync.register('send-messages')` ）。之後，在恢復連線並觸發 `sync` 事件時，就會從 IndexedDB 取出資料並傳送至伺服器。透過這個機制，使用者就能完全不必在意網路狀態，繼續使用應用程式。

---

## 10. PWA 的未來與挑戰（透過 Project Fugu 帶來的進化）

PWA 至今仍在不斷進化。特別是由 Google、Microsoft、Intel 等主導的 **Project Fugu**（Web Capabilities）計畫，更進一步模糊了 Web 與原生應用程式的界線。

Project Fugu 的目標，是讓 Web 也能安全地存取以往只有原生應用程式才能使用的強大 OS 功能。這使得以下的新 API 陸續在瀏覽器中實作。

- **Web Bluetooth API**：與 IoT 裝置直接通訊
- **Web USB API** / **Web Serial API**：與特殊硬體連接
- **File System Access API**：直接讀寫使用者本機檔案系統上的檔案（這對 IDE 或編輯器 PWA 很重要）
- **Contact Picker API**：存取裝置的聯絡人資料
- **Web Share Target API**：將 PWA 註冊為 OS「分享選單」的目標

在挑戰方面，Apple（iOS/Safari）的支援狀況依然首當其衝。基於隱私、安全，以及與 App Store 商業模式的考量，Apple 對許多 Project Fugu API 採取謹慎的態度。然而，從 iOS 16.4 支援 Web Push 等舉動來看，為了回應使用者的強烈需求，他們逐漸加強對 PWA 的支援也是事實。

在未來的網路應用程式開發中， **PWA** 絕對不再只是個選項，而是為使用者提供最佳體驗的必備技術標準（基準）。

---

## 11. 結語

本文從 PWA 的基本概念，到 Service Worker 複雜的生命週期、多樣的快取策略、與 IndexedDB 的整合，以及最新網路技術的動態，進行了非常深入的解說。

初次接觸 Service Worker 時，可能會對其非同步特性或快取行為感到困惑。然而，只要正確理解生命週期，並選擇合適的快取策略進行實作，就能建構出令人驚豔的快速且具彈性（Resilient）的網路應用程式。

「離線也能運作」的體驗，對使用者來說不只是個方便的功能，更會讓他們對應用程式產生深厚的信任與依賴。請務必在您的專案中導入 PWA 技術，將 Web 的潛力發揮到極致。
