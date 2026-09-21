---
title: "PWA (Progressive Web Apps) 的潜力与实现（Service Worker的力量）"
description: "从PWA全貌到Service Worker的生命周期、离线缓存和Push通知的全面解说。"
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

## 1. 引言：什么是PWA？

网络技术在过去几十年里取得了剧烈的进步。从静态的HTML文档链接集开始，经过动态DOM操作、Ajax异步通信、SPA（Single Page Application）的出现，现在已经能够构建出匹敌甚至超越原生应用用户体验（UX）的应用程序。处于这一进化最前沿的就是 **PWA (Progressive Web Apps)** 。

PWA，简而言之，就是“兼具Web可访问性与原生应用高性能、高用户体验的Web应用程序”。在传统的Web应用中，离线访问时理所当然会显示“未连接到互联网”的错误画面（在Chrome中就是著名的恐龙游戏画面）。但是，如果适当地实现了PWA技术，即使在离线状态下也能启动应用，浏览缓存的内容，或者在后台进行数据同步处理。

本文将从PWA的全貌出发，非常详细且全面地解说其核心—— **Service Worker** 的生命周期、高级缓存策略、与IndexedDB的协作，以及未来的展望。

---

## 2. 原生应用 vs PWA

在开发Web应用程序时，常常成为讨论焦点的是“应该采用原生应用还是PWA”。通过深入理解各自的优缺点，可以为项目进行最佳的技术选型。

### 2.1. 原生应用的优缺点

原生应用（使用iOS的Swift/Objective-C、Android的Kotlin/Java等开发的应用）最大的优势在于拥有对OS API的完全访问权限。
借此，可以实现最大限度利用相机、GPS、蓝牙、NFC及各种传感器等的高级功能。此外，由于针对OS进行了优化，渲染性能极高，在频繁使用复杂动画和3D图形的游戏等方面，原生应用具有压倒性的优势。

另一方面，原生应用也存在以下重大弱点（课题）：

- **开发成本与学习成本** ：需要分别维护针对iOS和Android的代码库（虽然可以通过React Native或Flutter等跨平台框架来减轻，但无法完全归零）。
- **应用商店的审核** ：如果不通过Apple的App Store或Google Play的审核就无法发布，而且在更新时有时会产生数天的等待审核时间。
- **获取用户的障碍** ：打开应用商店、搜索、下载并安装的过程，对用户来说是巨大的麻烦（摩擦）。

### 2.2. PWA解决的课题

PWA旨在发挥Web优势的同时克服原生应用的弱点。

- **单一代码库、多端运行** ：使用HTML、CSS、JavaScript等Web标准技术开发的单一代码库，可以在所有搭载浏览器的设备（手机、平板、桌面电脑）上运行。
- **无需审核即可即时更新** ：由于PWA只是一个Web网站，因此无需通过应用商店的审核。只需更新服务器上的文件，用户就能始终使用最新版本。
- **无需安装的无缝体验** ：用户只需访问URL即可开始使用应用。如果喜欢，通过“添加到主屏幕（Install）”，就能像原生应用一样从应用图标启动。
- **通过链接共享** ：能够将特定画面或状态作为URL共享，是Web独有的强大武器。

当然，PWA也有其局限性。特别是在iOS（Safari）环境中，由于Apple的策略，Web API的实现往往滞后，对Push通知的支持直到最近都不够完善，后台运行也受到严格限制。然而，近年来Safari也在加强对PWA的支持，这些差距正在逐渐缩小。

---

## 3. 构成PWA的3个支柱

为了实现PWA，需要以下3个主要的技术要素。

### 3.1. HTTPS (安全的通信)

出于安全原因，PWA的强大功能（Service Worker、Push通知、Geolocation等）只能在 **HTTPS** 环境下运行（作为例外的本地开发环境 `localhost` 是允许的）。这是为了防止这些功能被恶意的第三方通过中间人攻击等方式篡改或滥用。

### 3.2. Web App Manifest

Web App Manifest（ `manifest.json` ）是向浏览器提供Web应用相关元数据的JSON文件。通过它，可以定义应用的图标、名称、主题颜色、显示模式等，并控制其安装到设备时类似原生应用的外观。

### 3.3. Service Worker

Service Worker正是将PWA从单纯的网站升华为“应用程序”的魔法棒。它是浏览器在后台执行的JavaScript环境，在独立于网页的线程中运行。它可以拦截（代理）网络请求、管理缓存以及接收Push通知。

---

## 4. Web App Manifest 的详细设置

Web App Manifest 可以说是PWA的“门面”配置文件。它决定了用户安装应用时的外观和行为。

以下是常见的 `manifest.json` 配置示例。

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

### 主要属性解说

- **name** 和 **short_name** ：这是在安装时的提示或主屏幕上的应用图标下方显示的名称。在空间有限的主屏幕上，会优先使用 `short_name` 。
- **start_url** ：用户从主屏幕图标启动应用时最先加载的URL。通过附加跟踪参数（如： `?source=pwa` ），可以在访问分析工具中识别出这是来自PWA的访问。
- **display** ：指定应用的显示模式。
  - `standalone` ：完全隐藏浏览器的UI（URL栏、返回按钮等），像原生应用一样显示。这是最推荐的设置。
  - `fullscreen` ：使用整个屏幕，甚至隐藏状态栏（最适合游戏或视频应用）。
  - `minimal-ui` ：只显示基本的导航UI。
  - `browser` ：作为普通的浏览器标签页显示。
- **theme_color** 和 **background_color** ：定义应用的主题颜色以及启动时闪屏界面的背景色。
- **icons** ：作为应用图标使用的图像数组。为了适应不同的设备分辨率，建议提供多种尺寸（至少192x192和512x512）。指定 `purpose: "maskable"` 可以优化Android等平台上的图标裁剪。

---

## 5. Service Worker 的核心与生命周期

Service Worker 是应被称为PWA“心脏”的存在。它与在传统网页中执行的JavaScript不同，没有对DOM的访问权限。取而代之的是，它执行网络请求的中介、缓存操作、后台同步处理等工作。

### 5.1. Service Worker 的生命周期

Service Worker 拥有独立于页面的自身生命周期。准确理解这个生命周期是防止意外缓存问题（如更新后画面没有变化等）的关键。

以下的Mermaid图表展示了Service Worker的状态转换。

```mermaid
stateDiagram-v2
    direction TB
    "已解析" --> "安装中" : "注册"
    "安装中" --> "等待中" : "成功"
    "安装中" --> "废弃" : "错误"
    "等待中" --> "激活中" : "所有客户端关闭 / skipWaiting()"
    "激活中" --> "已激活" : "成功"
    "激活中" --> "废弃" : "错误"
    "已激活" --> "废弃" : "被新SW替换"
```

1. **已解析 (Parsed)** ：浏览器下载Service Worker脚本并完成语法解析的状态。
2. **安装中 (Installing)** ：触发了 `install` 事件的状态。此阶段主要用于预缓存（Pre-caching）应用程序运行必须的静态资源（HTML、CSS、JS、图片等）。如果安装失败（如缓存保存失败），Service Worker将被丢弃。
3. **等待中 (Installed / Waiting)** ：安装已完成，但因为现有的旧版Service Worker仍在其他标签页中活跃运行，所以正在等待交接的状态。当用户关闭所有相关标签页并重新打开，或者调用 `self.skipWaiting()` 时，将进入下一阶段。
4. **激活中 (Activating)** ：触发了 `activate` 事件的状态。此阶段主要用于清理旧版Service Worker创建的废弃缓存。
5. **已激活 (Activated)** ：完全运转，能够控制和处理来自页面的 `fetch` 事件或 `push` 事件的状态。
6. **废弃 (Redundant)** ：安装失败、激活失败或被新版本的Service Worker替换后的状态。

### 5.2. Service Worker 的注册

要使用Service Worker，首先需要从主JavaScript线程进行注册处理。

```javascript
// main.js 或者 index.html 的 <script> 标签内
if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker
      .register("/sw.js", { scope: "/" })
      .then((registration) => {
        console.log("ServiceWorker 注册成功，作用域为: ", registration.scope);
      })
      .catch((error) => {
        console.error("ServiceWorker 注册失败: ", error);
      });
  });
}
```

这里重要的是Service Worker的作用域。默认情况下，它只拦截放置Service Worker文件的目录及其子目录下的请求。也就是说，如果是 `/sw.js` ，则可以拦截对全站 `/` 的请求，但如果放在 `/js/sw.js` ，就只能拦截 `/js/` 及其以下的请求了。

---

## 6. 缓存策略完全指南

Service Worker 最大的魅力在于它能拦截网络请求（ `fetch` 事件）并实现自定义的缓存策略。根据资源类型（图片、API响应、HTML）和应用程序的需求，必须灵活运用合适的缓存策略。

### 6.1. Cache First (缓存优先)

这是最基本、最快的策略。首先检查缓存，如果存在就返回缓存；如果不存在则向网络请求，并将结果保存到缓存中。它非常适合图片文件、字体等不经常更改的静态资源。

```mermaid
flowchart TD
    "页面" -->|"1. 请求"| "Service Worker"
    "Service Worker" -->|"2. 检查缓存"| "缓存"
    "缓存" -->|"3a. 命中缓存"| "Service Worker"
    "Service Worker" -->|"4a. 响应"| "页面"
    "缓存" -->|"3b. 未命中缓存"| "网络"
    "网络" -->|"4b. 响应"| "Service Worker"
    "Service Worker" -->|"5b. 保存至缓存"| "缓存"
    "Service Worker" -->|"6b. 响应"| "页面"
```

### 6.2. Network First (网络优先)

这是始终优先获取最新数据的策略。首先向网络发送请求，如果成功则将结果保存到缓存中并返回给页面。只有在离线状态等网络通信失败的情况下，才会降级使用缓存。适合频繁更新的文章数据或API响应。

```mermaid
flowchart TD
    "页面" -->|"1. 请求"| "Service Worker"
    "Service Worker" -->|"2. 获取"| "网络"
    "网络" -->|"3a. 成功"| "Service Worker"
    "Service Worker" -->|"4a. 保存至缓存"| "缓存"
    "Service Worker" -->|"5a. 响应"| "页面"
    "网络" -->|"3b. 错误 / 离线"| "Service Worker"
    "Service Worker" -->|"4b. 检查缓存"| "缓存"
    "缓存" -->|"5b. 命中缓存"| "Service Worker"
    "Service Worker" -->|"6b. 降级响应"| "页面"
```

### 6.3. Stale-while-revalidate (返回旧缓存的同时在后台更新)

这是一种兼顾速度和新鲜度的极其强大的现代策略。
当请求发生时，立即返回缓存（旧的、Stale的数据）以快速渲染画面。同时，在后台（while-revalidate）向网络发送请求，获取最新数据并更新缓存。用户在下次访问时就能看到最新的数据。

```mermaid
flowchart TD
    "页面" -->|"1. 请求"| "Service Worker"
    "Service Worker" -->|"2. 检查缓存"| "缓存"
    "缓存" -->|"3. 命中缓存 (快速响应)"| "Service Worker"
    "Service Worker" -->|"4. 返回旧缓存响应"| "页面"
    "Service Worker" -.->|"5. 获取 (后台)"| "网络"
    "网络" -.->|"6. 网络响应"| "Service Worker"
    "Service Worker" -.->|"7. 更新缓存"| "缓存"
```

### 6.4. Cache Only / Network Only

- **Cache Only（仅缓存）** ：完全只从缓存返回响应。如果不存在则报错。仅用于保证事先已确实下载完成的特定资源。
- **Network Only（仅网络）** ：根本不看缓存，始终向网络请求。用于不应被缓存的通信，如认证API、POST请求等。

---

## 7. Service Worker 的实现示例（代码详解）

那么，结合上述的生命周期和缓存策略，让我们来看一下实际的 `sw.js` （Service Worker文件）的实现示例。

### 7.1. 安装事件与预缓存

在 `install` 事件中，预先缓存应用的壳层（基础的HTML、CSS、JS）。这样一来，即使是后续的访问或在离线时，也能瞬间显示出应用的框架。

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
  console.log("[ServiceWorker] 安装事件");
  
  // 通过调用 self.skipWaiting()，跳过等待状态并立即激活。
  self.skipWaiting();

  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log("[ServiceWorker] 预缓存离线页面");
      return cache.addAll(PRECACHE_URLS);
    })
  );
});
```

### 7.2. 激活事件与缓存的清理

当修改了缓存名称的版本（例如：从 `pwa-cache-v1` 改为 `v2` ）时，需要删除旧的废弃缓存以节省存储空间。这是在 `activate` 事件中进行的。

```javascript
self.addEventListener("activate", (event) => {
  console.log("[ServiceWorker] 激活事件");
  
  // self.clients.claim() 立即接管所有当前打开的页面。
  event.waitUntil(self.clients.claim());

  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            console.log("[ServiceWorker] 删除旧缓存:", cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
```

### 7.3. 处理 Fetch 事件

拦截 `fetch` 事件并根据请求资源类型切换策略的高级实现示例。比如图片采用 Cache First，HTML导航请求采用带有降级处理的 Network First，以此来分支处理。

```javascript
self.addEventListener("fetch", (event) => {
  const request = event.request;
  const url = new URL(request.url);

  // POST请求或向外部域名的请求会直接放行给网络
  if (request.method !== "GET") return;

  // HTML请求（页面跳转）采用 Network First 策略 + 离线降级
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
          // 网络错误（离线）时从缓存中获取，如果没有则返回专用的离线页面
          return caches.match(request).then((cachedResponse) => {
            return cachedResponse || caches.match("/offline.html");
          });
        })
    );
    return;
  }

  // 图片等静态资源采用 Cache First 策略
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

  // 其他的API请求等应用 Stale-while-revalidate 策略
  event.respondWith(
    caches.match(request).then((cachedResponse) => {
      const fetchPromise = fetch(request).then((networkResponse) => {
        return caches.open(CACHE_NAME).then((cache) => {
          cache.put(request, networkResponse.clone());
          return networkResponse;
        });
      });
      // 如果有缓存则先返回，并在后台继续请求处理。如果没有缓存则等待 fetchPromise。
      return cachedResponse || fetchPromise;
    })
  );
});
```

---

## 8. 与 IndexedDB 的协作：更高级的数据管理

Service Worker 的 `caches` API（Cache Storage）非常适合保存整个 HTTP 响应（HTML文件、图片、CSS等）。但是，用来管理应用程序处理的结构化数据（JSON格式的API响应、用户设置数据、离线时发布的文本数据等）时可能不够用。

这时候登场的就是 **IndexedDB** 了。

IndexedDB 是内置于浏览器中的异步事务型 NoSQL 数据库。它可以保存非常大量的数据，并且能够进行复杂的索引搜索。

### 8.1. 为什么仅用 Cache Storage 是不够的？

例如，假设你在离线状态下的待办事项（ToDo）应用中添加了一个新任务。此时，要想把“添加任务的POST请求”本身保存到 Cache Storage 中是很困难的。
在那种要求保存离线时的操作、待恢复在线时再重新发送的需求中，需要一种协作机制：把任务数据暂时保存在 IndexedDB 中，然后在后台同步（后述）的时机从数据库中取出数据并发送给API。

### 8.2. 在 Service Worker 内部使用 IndexedDB

从 Service Worker 的作用域内也是可以访问 IndexedDB 的。不过，直接操作 IndexedDB API 会让代码变得繁杂，因此一般会使用 Google 提供的轻量级包装库 `idb` 。

在一个具有高级离线功能的 PWA 中，比如将从 API 获取的文章列表 JSON 保存到 IndexedDB 而不是缓存 API 中进行详细管理和查询，IndexedDB 就扮演着重要的角色。

---

## 9. Push 通知与后台同步 (Background Sync)

PWA 最逼近原生应用的功能，就是 Push 通知和后台运行能力。

### 9.1. Web Push API

Web Push 是一种机制，即使应用没有打开，也能从服务器启动 Service Worker 将通知送达给用户。

1. **订阅 (Subscribe)** ：在浏览器端向用户请求通知许可，获取 Push 服务的订阅信息（端点和加密密钥）并保存到自家服务器。
2. **发送 (Push)** ：从自家服务器向浏览器厂商的 Push 服务（如 FCM 或 Apple Push Notification service）发送消息。
3. **接收 (Push Event)** ：当 Push 服务向设备发送数据时，浏览器会在后台启动 Service Worker 并触发 `push` 事件。Service Worker 调用 `self.registration.showNotification()` 方法来显示系统原生级别的通知UI。

```javascript
self.addEventListener("push", (event) => {
  const data = event.data ? event.data.json() : {};
  const title = data.title || "有新消息";
  const options = {
    body: data.body || "请打开应用查看。",
    icon: "/images/icons/icon-192x192.png",
    badge: "/images/icons/badge.png",
  };

  event.waitUntil(self.registration.showNotification(title, options));
});
```

### 9.2. Background Sync (后台同步)

假设用户在离线的地铁里按下了发送消息按钮。在普通的 Web 应用中这会报错，但如果使用 Background Sync API，浏览器就会在“网络连接恢复的时机”，为 Service Worker 触发一次 `sync` 事件。

应用端会在离线时将数据暂时保存到 IndexedDB 中，并向 Service Worker 注册一个同步任务（ `registration.sync.register('send-messages')` ）。之后，在恢复在线且触发了 `sync` 事件时，从 IndexedDB 取出数据再发送给服务器。这样一来，用户就可以完全不必在意网络状态而持续使用应用。

---

## 10. PWA 的未来与课题（借助 Project Fugu 的进化）

PWA 现在依然在不断进化。特别是由 Google、Microsoft、Intel 等主导的名为 **Project Fugu** （Web Capabilities）的项目，正进一步模糊 Web 与原生应用之间的界限。

Project Fugu 的目标，是让 Web 也能安全地访问以往只有原生应用才被允许使用的那些强大的操作系统级功能。以此为契机，以下等新 API 正接连被实现到浏览器中：

- **Web Bluetooth API** ：与 IoT 设备的直接通信
- **Web USB API** / **Web Serial API** ：与特殊硬件的连接
- **File System Access API** ：直接读写用户本地文件系统上的文件（对于 IDE 或编辑器类的 PWA 很重要）
- **Contact Picker API** ：访问设备的通讯录数据
- **Web Share Target API** ：将 PWA 注册为系统“共享菜单”的接收目标

至于课题，依然包括 Apple（iOS/Safari）的适配状况。出于对隐私、安全以及 App Store 商业模式的考量，Apple 对 Project Fugu 的多数 API 都保持着谨慎的态度。然而，顺应用户的强烈需求，例如在 iOS 16.4 中支持 Web Push，他们逐步加强对 PWA 的支持也是不争的事实。

在未来的 Web 应用开发中， **PWA** 将不再仅仅是一个选项，而必定会成为为用户提供最佳体验时必不可少的技术基准（baseline）。

---

## 11. 结语

在本文中，我们从 PWA 的基本概念开始，深入讲解了 Service Worker 复杂的生命周期、多样化的缓存策略、与 IndexedDB 的协作，以及最新 Web 技术的动向。

刚接触 Service Worker 时，可能会对其异步性或缓存的行为感到困惑。但是，只要正确理解生命周期，并选择、实现合适的缓存策略，你就能构建出令人惊叹的、高速且具有韧性（恢复力）的 Web 应用程序。

“离线也能运行”的体验，对用户来说超越了单纯的便利功能，会孕育出对应用程序深深的信任与喜爱。请务必也在你的项目中引入 PWA 技术，最大限度地发挥 Web 的潜力。
