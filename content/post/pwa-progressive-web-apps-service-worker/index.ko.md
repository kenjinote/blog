---
title: "PWA (Progressive Web Apps) 의 가능성과 구현 (Service Worker의 힘)"
description: "PWA의 전체 모습부터 Service Worker의 수명 주기, 오프라인 캐시, Push 알림까지 해설합니다."
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

## 1. 시작하며: PWA란 무엇인가?

웹 기술은 지난 수십 년 동안 극적인 진화를 이루었습니다. 정적인 HTML 문서의 링크 모음으로 시작하여 동적인 DOM 조작, Ajax를 통한 비동기 통신, SPA(Single Page Application)의 등장을 거쳐, 현재는 네이티브 앱에 필적하거나 이를 뛰어넘는 사용자 경험(UX)을 제공하는 애플리케이션을 구축하는 것이 가능해졌습니다. 그 진화의 최전선에 위치한 것이 바로 **PWA (Progressive Web Apps)** 입니다.

PWA란 단적으로 말하면 "웹의 접근성과 네이티브 앱의 높은 성능 및 UX를 겸비한 웹 애플리케이션"을 의미합니다. 기존의 웹 앱에서는 오프라인 상태일 때 접속하면 "인터넷에 연결되어 있지 않습니다"라는 에러 화면(Chrome으로 말하자면 유명한 공룡 게임 화면)이 표시되는 것이 당연했습니다. 하지만 PWA 기술을 적절히 구현하면 오프라인 상태에서도 앱을 실행하고, 캐시된 콘텐츠를 열람하거나 백그라운드에서 데이터 동기화 처리를 수행하는 것이 가능해집니다.

본 기사에서는 PWA의 전체적인 모습부터 그 핵심인 **Service Worker** 의 수명 주기, 고도화된 캐시 전략, IndexedDB와의 연동, 그리고 향후 전망까지 매우 상세하고 포괄적으로 해설합니다.

---

## 2. 네이티브 앱 vs PWA

웹 애플리케이션을 개발할 때 항상 논의의 대상이 되는 것이 "네이티브 앱과 PWA 중 어느 것을 채택할 것인가"라는 점입니다. 각각의 장단점을 깊이 이해함으로써 프로젝트에 최적의 기술을 선택할 수 있습니다.

### 2.1. 네이티브 앱의 강점과 약점

네이티브 앱(iOS의 Swift/Objective-C, Android의 Kotlin/Java 등으로 개발된 앱)의 가장 큰 강점은 OS의 API에 대한 완전한 접근 권한을 가진다는 것입니다.
이를 통해 카메라, GPS, Bluetooth, NFC, 각종 센서 등을 최대한 활용한 고도화된 기능을 구현할 수 있습니다. 또한, OS에 최적화되어 있기 때문에 렌더링 성능이 매우 뛰어나며, 복잡한 애니메이션이나 3D 그래픽을 다수 사용하는 게임 등에는 네이티브 앱이 압도적으로 유리합니다.

반면에 네이티브 앱에는 다음과 같은 큰 약점(과제)이 존재합니다.

- ** 개발 비용 및 학습 비용 ** : iOS와 Android용으로 별도의 코드 베이스를 유지 보수해야 합니다 (React Native나 Flutter 같은 크로스 플랫폼 프레임워크로 완화할 수 있지만, 완전히 제로가 되지는 않습니다).
- ** 앱 스토어 심사 ** : Apple의 App Store나 Google Play의 심사를 통과해야만 출시할 수 있으며, 업데이트 시에도 며칠간의 심사 대기 시간이 발생할 수 있습니다.
- ** 사용자 확보의 장벽 ** : 앱 스토어를 열고, 검색하고, 다운로드하여 설치하는 과정은 사용자에게 큰 번거로움(마찰)입니다.

### 2.2. PWA가 해결하는 과제

PWA는 웹의 강점을 살리면서 네이티브 앱의 약점을 극복하는 것을 목표로 합니다.

- ** 원 소스 멀티 유즈 ** : HTML, CSS, JavaScript라는 웹 표준 기술로 개발된 단일 코드 베이스가 브라우저를 탑재한 모든 디바이스(모바일, 태블릿, 데스크톱)에서 동작합니다.
- ** 심사 없는 즉각적인 업데이트 ** : PWA는 단순한 웹 사이트이기 때문에 앱 스토어의 심사를 통과할 필요가 없습니다. 서버의 파일을 업데이트하는 것만으로 사용자는 항상 최신 버전을 이용할 수 있습니다.
- ** 설치가 필요 없는 원활한 경험 ** : 사용자는 URL에 접속하는 것만으로 앱을 사용하기 시작할 수 있습니다. 마음에 든다면 "홈 화면에 추가(Install)"하여 네이티브 앱처럼 앱 아이콘을 통해 실행할 수 있게 됩니다.
- ** 링크를 통한 공유성 ** : 특정 화면이나 상태를 URL로 공유할 수 있는 것은 웹만의 강력한 무기입니다.

물론 PWA에도 제약은 있습니다. 특히 iOS(Safari) 환경에서는 Apple의 정책으로 인해 웹 API의 구현이 늦어지는 경향이 있으며, Push 알림 지원이 최근까지 불충분하거나 백그라운드 동작에 엄격한 제한이 있기도 합니다. 하지만 최근에는 Safari도 PWA 지원을 강화하고 있어 그 격차는 점차 줄어들고 있습니다.

---

## 3. PWA를 구성하는 3가지 기둥

PWA를 실현하기 위해서는 다음의 3가지 주요 기술 요소가 필요합니다.

### 3.1. HTTPS (안전한 통신)

PWA의 강력한 기능(Service Worker, Push 알림, Geolocation 등)은 보안상의 이유로 **HTTPS** 환경에서만 동작합니다 (로컬 개발 환경인 `localhost` 는 예외로 허용됩니다). 이는 이러한 기능들이 악의적인 제3자에 의한 중간자 공격 등으로 변조되거나 악용되는 것을 방지하기 위함입니다.

### 3.2. Web App Manifest

Web App Manifest ( `manifest.json` )는 브라우저에게 웹 앱에 관한 메타데이터를 제공하는 JSON 파일입니다. 이를 통해 앱의 아이콘, 이름, 테마 색상, 표시 모드 등을 정의하고, 디바이스에 설치했을 때 네이티브 앱과 같은 외관을 제어합니다.

### 3.3. Service Worker

Service Worker야말로 PWA를 단순한 웹 사이트에서 "애플리케이션"으로 승화시키는 마법의 지팡이입니다. 이는 브라우저가 백그라운드에서 실행하는 JavaScript 환경이며, 웹 페이지와는 별도의 스레드에서 동작합니다. 네트워크 요청을 가로채거나(프록시), 캐시를 관리하고, Push 알림을 받을 수 있습니다.

---

## 4. Web App Manifest의 상세 설정

Web App Manifest는 PWA의 얼굴이라고도 할 수 있는 설정 파일입니다. 사용자가 앱을 설치할 때의 외관과 동작을 결정합니다.

다음은 일반적인 `manifest.json` 의 설정 예시입니다.

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

### 주요 속성 해설

- **name** 과 **short_name** : 설치 시 프롬프트나 홈 화면의 앱 아이콘 하단에 표시되는 이름입니다. 공간이 제한된 홈 화면에서는 `short_name` 이 우선적으로 사용됩니다.
- **start_url** : 사용자가 홈 화면의 아이콘을 통해 앱을 실행했을 때 처음으로 로드되는 URL입니다. 추적 매개변수(예: `?source=pwa` )를 부여함으로써 PWA를 통한 접속을 접속 분석 도구에서 판별할 수 있게 됩니다.
- **display** : 앱의 표시 모드를 지정합니다.
  - `standalone` : 브라우저의 UI(URL 표시줄이나 뒤로 가기 버튼 등)를 완전히 숨기고 네이티브 앱처럼 표시합니다. 가장 권장되는 설정입니다.
  - `fullscreen` : 화면 전체를 사용하며 상태 표시줄조차 숨깁니다 (게임이나 동영상 앱에 최적).
  - `minimal-ui` : 기본적인 내비게이션 UI만을 표시합니다.
  - `browser` : 일반적인 브라우저 탭으로 표시합니다.
- **theme_color** 와 **background_color** : 앱의 테마 색상과 실행 시 스플래시 화면의 배경색을 정의합니다.
- **icons** : 앱의 아이콘으로 사용되는 이미지의 배열입니다. 다양한 디바이스 해상도에 대응하기 위해 여러 크기(최소 192x192와 512x512)를 준비하는 것이 권장됩니다. `purpose: "maskable"` 을 지정하면 Android 등에서 아이콘 자르기를 최적화할 수 있습니다.

---

## 5. Service Worker의 핵심과 수명 주기

Service Worker는 PWA의 "심장부"라고 불러야 할 존재입니다. 기존의 웹 페이지 내에서 실행되는 JavaScript와는 달리 DOM에 대한 접근 권한을 가지지 않습니다. 대신 네트워크 요청 중재, 캐시 조작, 백그라운드 동기화 처리 등을 수행합니다.

### 5.1. Service Worker의 수명 주기

Service Worker는 페이지와는 독립적인 자체 수명 주기를 가집니다. 이 수명 주기를 정확히 이해하는 것이 예상치 못한 캐시 문제(업데이트했는데 화면이 바뀌지 않는 등)를 방지하기 위한 핵심입니다.

다음의 Mermaid 다이어그램은 Service Worker의 상태 전이를 나타냅니다.

```mermaid
stateDiagram-v2
    direction TB
    "파싱됨" --> "설치 중" : "등록"
    "설치 중" --> "설치됨 (대기 중)" : "성공"
    "설치 중" --> "폐기됨" : "에러"
    "설치됨 (대기 중)" --> "활성화 중" : "모든 클라이언트 종료 / skipWaiting()"
    "활성화 중" --> "활성화됨" : "성공"
    "활성화 중" --> "폐기됨" : "에러"
    "활성화됨" --> "폐기됨" : "새로운 서비스 워커로 교체됨"
```

1. **파싱됨 (Parsed)** : 브라우저가 Service Worker 스크립트를 다운로드하고 구문 분석을 마친 상태.
2. **설치 중 (Installing)** : `install` 이벤트가 발생한 상태. 이 단계는 주로 애플리케이션 동작에 필수적인 정적 에셋(HTML, CSS, JS, 이미지 등)을 캐시(Pre-caching)하는 데 사용됩니다. 설치에 실패(캐시 저장 실패 등)하면 Service Worker는 폐기됩니다.
3. **설치됨 / 대기 중 (Installed / Waiting)** : 설치는 완료되었지만, 기존의 오래된 Service Worker가 여전히 다른 탭에서 활성화되어 작동 중이기 때문에 교체를 기다리고 있는 상태입니다. 사용자가 모든 탭을 닫고 다시 열거나, `self.skipWaiting()` 을 호출함으로써 다음 단계로 넘어갑니다.
4. **활성화 중 (Activating)** : `activate` 이벤트가 발생한 상태. 이 단계는 주로 오래된 Service Worker가 생성한 불필요한 캐시를 삭제하고 정리(cleanup)를 수행하는 데 사용됩니다.
5. **활성화됨 (Activated)** : 완전히 가동되어 페이지로부터의 `fetch` 이벤트나 `push` 이벤트를 제어 및 처리할 수 있는 상태.
6. **폐기됨 (Redundant)** : 설치 실패, 활성화 실패, 또는 새로운 버전의 Service Worker로 대체된 상태.

### 5.2. Service Worker 등록

Service Worker를 이용하려면 먼저 메인 JavaScript 스레드에서 등록 처리를 수행해야 합니다.

```javascript
// main.js 또는 index.html의 <script> 내부
if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker
      .register("/sw.js", { scope: "/" })
      .then((registration) => {
        console.log("스코프와 함께 서비스 워커 등록 성공: ", registration.scope);
      })
      .catch((error) => {
        console.error("서비스 워커 등록 실패: ", error);
      });
  });
}
```

여기서 중요한 것은 Service Worker의 스코프입니다. 기본적으로 Service Worker 파일이 배치된 디렉토리 하위의 요청만을 가로챕니다. 즉, `/sw.js` 라면 사이트 전체의 `/` 에 대한 요청을 후킹할 수 있지만, `/js/sw.js` 에 배치하면 `/js/` 하위의 요청만 후킹할 수 있게 됩니다.

---

## 6. 캐시 전략 완벽 가이드

Service Worker의 가장 큰 묘미는 네트워크 요청( `fetch` 이벤트)을 후킹하여 독자적인 캐시 전략을 구현할 수 있다는 점입니다. 리소스의 종류(이미지, API 응답, HTML)나 애플리케이션의 요구 사항에 따라 적절한 캐시 전략을 나누어 사용해야 합니다.

### 6.1. Cache First (캐시 우선)

가장 기본적이고 빠른 전략입니다. 먼저 캐시를 확인하고, 존재하면 그것을 반환하며, 존재하지 않으면 네트워크로 가져오러 가서 그 결과를 캐시에 저장합니다. 이미지 파일이나 폰트 등 자주 변경되지 않는 정적 리소스에 최적입니다.

```mermaid
flowchart TD
    "페이지" -->|"1. 요청"| "서비스 워커"
    "서비스 워커" -->|"2. 캐시 확인"| "캐시"
    "캐시" -->|"3a. 캐시 적중"| "서비스 워커"
    "서비스 워커" -->|"4a. 응답"| "페이지"
    "캐시" -->|"3b. 캐시 미스"| "네트워크"
    "네트워크" -->|"4b. 응답"| "서비스 워커"
    "서비스 워커" -->|"5b. 캐시에 저장"| "캐시"
    "서비스 워커" -->|"6b. 응답"| "페이지"
```

### 6.2. Network First (네트워크 우선)

항상 최신 데이터를 가져오는 것을 우선하는 전략입니다. 먼저 네트워크로 요청을 보내고, 성공하면 그 결과를 캐시에 저장한 후 페이지로 반환합니다. 오프라인 상태 등으로 네트워크 통신이 실패했을 경우에만 캐시로 폴백합니다. 자주 업데이트되는 기사 데이터나 API 응답에 적합합니다.

```mermaid
flowchart TD
    "페이지" -->|"1. 요청"| "서비스 워커"
    "서비스 워커" -->|"2. 가져오기"| "네트워크"
    "네트워크" -->|"3a. 성공"| "서비스 워커"
    "서비스 워커" -->|"4a. 캐시에 저장"| "캐시"
    "서비스 워커" -->|"5a. 응답"| "페이지"
    "네트워크" -->|"3b. 에러 / 오프라인"| "서비스 워커"
    "서비스 워커" -->|"4b. 캐시 확인"| "캐시"
    "캐시" -->|"5b. 캐시 적중"| "서비스 워커"
    "서비스 워커" -->|"6b. 폴백 응답"| "페이지"
```

### 6.3. Stale-while-revalidate (오래된 캐시를 반환하며 백그라운드에서 업데이트)

속도와 최신 상태를 양립시키는 매우 강력하고 모던한 전략입니다.
요청이 발생했을 때 즉시 캐시(오래된·Stale한 데이터)를 반환하여 빠르게 화면을 렌더링합니다. 이와 동시에 백그라운드(while-revalidate)에서 네트워크로 요청을 보내 최신 데이터를 가져와 캐시를 업데이트합니다. 사용자는 다음 접속 시에 최신 데이터를 보게 됩니다.

```mermaid
flowchart TD
    "페이지" -->|"1. 요청"| "서비스 워커"
    "서비스 워커" -->|"2. 캐시 확인"| "캐시"
    "캐시" -->|"3. 캐시 적중 (빠른 응답)"| "서비스 워커"
    "서비스 워커" -->|"4. 오래된 응답 반환"| "페이지"
    "서비스 워커" -.->|"5. 가져오기 (백그라운드)"| "네트워크"
    "네트워크" -.->|"6. 네트워크 응답"| "서비스 워커"
    "서비스 워커" -.->|"7. 캐시 업데이트"| "캐시"
```

### 6.4. Cache Only / Network Only

- **Cache Only** : 완전히 캐시에서만 응답을 반환합니다. 존재하지 않으면 에러가 발생합니다. 사전에 확실히 다운로드되었음이 보장되는 특정 에셋에만 사용됩니다.
- **Network Only** : 캐시를 전혀 보지 않고 항상 네트워크로 요청합니다. 인증 API나 POST 요청 등 캐시해서는 안 되는 통신에 사용됩니다.

---

## 7. Service Worker 구현 예시 (코드 상세 해설)

그러면 앞서 언급한 수명 주기와 캐시 전략을 바탕으로 실제 `sw.js` (Service Worker 파일)의 구현 예시를 살펴보겠습니다.

### 7.1. 설치 이벤트와 사전 캐싱

`install` 이벤트에서는 앱의 셸(기본적인 HTML, CSS, JS)을 사전에 캐시합니다. 이를 통해 다음 접속 이후나 오프라인 시에도 앱의 틀을 즉시 표시할 수 있습니다.

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
  console.log("[서비스 워커] 설치 이벤트");
  
  // self.skipWaiting()을 호출하여 대기 상태를 건너뛰고 즉시 활성화합니다.
  self.skipWaiting();

  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log("[서비스 워커] 오프라인 페이지 사전 캐싱");
      return cache.addAll(PRECACHE_URLS);
    })
  );
});
```

### 7.2. 활성화 이벤트와 캐시 정리

캐시 이름의 버전(예: `pwa-cache-v1` 에서 `v2` 로)을 변경했을 때, 오래되고 불필요해진 캐시를 삭제하여 스토리지를 절약해야 합니다. 이는 `activate` 이벤트에서 수행합니다.

```javascript
self.addEventListener("activate", (event) => {
  console.log("[서비스 워커] 활성화 이벤트");
  
  // self.clients.claim()으로 현재 열려 있는 모든 페이지를 즉시 제어하에 둡니다.
  event.waitUntil(self.clients.claim());

  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            console.log("[서비스 워커] 오래된 캐시 삭제:", cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
```

### 7.3. Fetch 이벤트 핸들링

`fetch` 이벤트를 후킹하여 요청의 리소스 타입에 따라 전략을 전환하는 고도화된 구현 예시입니다. 이미지는 Cache First, HTML 내비게이션 요청은 Network First로 폴백을 제공하는 등 처리를 분기합니다.

```javascript
self.addEventListener("fetch", (event) => {
  const request = event.request;
  const url = new URL(request.url);

  // POST 요청이나 외부 도메인에 대한 요청은 네트워크로 통과
  if (request.method !== "GET") return;

  // HTML 요청(페이지 전환)은 Network First 전략 + 오프라인 폴백
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
          // 네트워크 에러(오프라인) 시에는 캐시에서 가져오고, 없으면 전용 오프라인 페이지를 반환
          return caches.match(request).then((cachedResponse) => {
            return cachedResponse || caches.match("/offline.html");
          });
        })
    );
    return;
  }

  // 이미지 등 정적 에셋은 Cache First 전략
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

  // 기타 API 요청 등은 Stale-while-revalidate 적용
  event.respondWith(
    caches.match(request).then((cachedResponse) => {
      const fetchPromise = fetch(request).then((networkResponse) => {
        return caches.open(CACHE_NAME).then((cache) => {
          cache.put(request, networkResponse.clone());
          return networkResponse;
        });
      });
      // 캐시가 있으면 먼저 반환하고, 백그라운드에서 페치 처리를 계속. 캐시가 없으면 fetchPromise를 대기.
      return cachedResponse || fetchPromise;
    })
  );
});
```

---

## 8. IndexedDB와의 연동: 더욱 고도화된 데이터 관리

Service Worker의 `caches` API(Cache Storage)는 HTTP 응답 전체(HTML 파일, 이미지, CSS 등)를 저장하는 데 매우 적합합니다. 하지만 애플리케이션이 다루는 구조화된 데이터(JSON 형식의 API 응답, 사용자의 설정 데이터, 오프라인 시에 작성된 텍스트 데이터 등)를 관리하기에는 불충분한 경우가 있습니다.

그래서 등장하는 것이 **IndexedDB** 입니다.

IndexedDB는 브라우저에 내장된 비동기 트랜잭션 방식의 [NoSQL](https://kenji.blog/ko/p/nosql-database-selection-kvs-document-graph-wide-column/) 데이터베이스입니다. 매우 대용량의 데이터를 저장할 수 있으며, 복잡한 인덱스 검색도 가능합니다.

### 8.1. 왜 Cache Storage만으로는 불충분한가?

예를 들어 ToDo 앱에서 오프라인 상태일 때 새로운 태스크를 추가했다고 가정해 봅시다. 이때 "태스크를 추가하는 POST 요청" 자체를 Cache Storage에 저장하는 것은 어렵습니다.
오프라인 시의 액션을 저장하고 온라인 복귀 시에 재전송하는 것과 같은 요구 사항에서는, IndexedDB에 일시적으로 태스크 데이터를 저장하고 백그라운드 동기화(후술) 시점에 데이터베이스에서 데이터를 꺼내어 API로 전송하는 등의 연동이 필요해집니다.

### 8.2. Service Worker 내에서의 IndexedDB 이용

Service Worker의 스코프 내에서도 IndexedDB에 접근하는 것이 가능합니다. 직접 IndexedDB API를 조작하는 것은 코드가 복잡해지기 쉽기 때문에, Google이 제공하는 `idb` 라는 경량 래퍼 라이브러리를 사용하는 것이 일반적입니다.

API에서 가져온 기사 목록 JSON을 캐시 API가 아닌 IndexedDB에 저장하여 세밀하게 관리하고 쿼리하는 등, 고도화된 오프라인 기능을 가지는 PWA에서는 이 IndexedDB가 중요한 역할을 담당합니다.

---

## 9. Push 알림과 백그라운드 동기화 (Background Sync)

PWA가 네이티브 앱에 가장 근접하는 기능이 바로 Push 알림과 백그라운드에서의 동작입니다.

### 9.1. Web Push API

Web Push는 앱이 열려 있지 않아도 서버에서 Service Worker를 기동하여 사용자에게 알림을 전달하는 메커니즘입니다.

1. ** 구독 (Subscribe)** : 브라우저 측에서 사용자에게 알림 권한을 요청하고, Push 서비스의 구독 정보(엔드포인트와 암호화 키)를 가져와 자사 서버에 저장합니다.
2. ** 송신 (Push)** : 자사 서버에서 브라우저 벤더의 Push 서비스(FCM이나 Apple Push Notification service)로 메시지를 전송합니다.
3. ** 수신 (Push Event)** : Push 서비스가 디바이스로 데이터를 전송하면 브라우저가 백그라운드에서 Service Worker를 기동하고, `push` 이벤트를 발생시킵니다. Service Worker는 `self.registration.showNotification()` 메서드를 호출하여 OS 네이티브 알림 UI를 표시합니다.

```javascript
self.addEventListener("push", (event) => {
  const data = event.data ? event.data.json() : {};
  const title = data.title || "새로운 메시지가 있습니다";
  const options = {
    body: data.body || "앱을 열어서 확인해 주세요.",
    icon: "/images/icons/icon-192x192.png",
    badge: "/images/icons/badge.png",
  };

  event.waitUntil(self.registration.showNotification(title, options));
});
```

### 9.2. Background Sync (백그라운드 동기화)

사용자가 오프라인 상태인 지하철 안에서 메시지 전송 버튼을 눌렀다고 가정해 봅시다. 일반적인 웹 앱에서는 에러가 발생하지만, Background Sync API를 사용하면 브라우저가 "네트워크 연결이 회복된 타이밍"을 가늠하여 Service Worker에 `sync` 이벤트를 발생시켜 줍니다.

앱 측은 오프라인 시에 데이터를 IndexedDB에 임시 저장하고, Service Worker에 동기화 태스크를 등록( `registration.sync.register('send-messages')` )합니다. 그 후 온라인으로 복귀하여 `sync` 이벤트가 발생했을 때, IndexedDB에서 데이터를 꺼내 서버로 전송합니다. 이를 통해 사용자는 네트워크 상태를 전혀 신경 쓰지 않고 앱을 계속 사용할 수 있습니다.

---

## 10. PWA의 미래와 과제 (Project Fugu에 의한 진화)

PWA는 현재도 진화를 계속하고 있습니다. 특히 Google이나 Microsoft, Intel 등이 주도하는 **Project Fugu** (Web Capabilities)라는 이니셔티브가 웹과 네이티브의 경계를 더욱 모호하게 만들고 있습니다.

Project Fugu의 목표는 네이티브 앱에만 허용되었던 OS의 강력한 기능에 웹에서도 안전하게 접근할 수 있도록 하는 것입니다. 이를 통해 다음과 같은 새로운 API들이 속속 브라우저에 구현되고 있습니다.

- **Web Bluetooth API** : IoT 기기와의 직접 통신
- **Web USB API** / **Web Serial API** : 특수한 하드웨어와의 연결
- **File System Access API** : 사용자의 로컬 파일 시스템에 있는 파일을 직접 읽고 쓰기 (IDE나 에디터 PWA에서 중요)
- **Contact Picker API** : 디바이스의 연락처 데이터에 대한 접근
- **Web Share Target API** : PWA를 OS의 "공유 메뉴" 대상으로 등록

과제로는 여전히 Apple(iOS/Safari)의 지원 상황을 꼽을 수 있습니다. Apple은 프라이버시나 보안, 그리고 App Store의 비즈니스 모델과의 균형 문제로 인해 Project Fugu API의 상당수에 신중한 자세를 보이고 있습니다. 하지만 iOS 16.4에서의 Web Push 지원 등, 사용자의 강력한 요구에 부응하는 형태로 점차 PWA 지원을 강화하고 있는 것도 사실입니다.

앞으로의 웹 애플리케이션 개발에서 **PWA** 는 단순한 선택 사항이 아니라, 사용자에게 최고의 경험을 제공하기 위한 필수 기술 기준(베이스라인)이 되어갈 것임은 틀림없습니다.

---

## 11. 마치며

본 기사에서는 PWA의 기본 개념부터 Service Worker의 복잡한 수명 주기, 다양한 캐시 전략, IndexedDB와의 연동, 그리고 최신 웹 기술 동향까지 매우 깊이 있는 수준으로 해설을 진행했습니다.

Service Worker는 처음 접할 때는 그 비동기성이나 캐시의 동작에 당황할지도 모릅니다. 하지만 수명 주기를 올바르게 이해하고 적절한 캐시 전략을 선택하여 구현함으로써 놀라울 정도로 빠르고 회복력 있는(resilient) 웹 애플리케이션을 구축할 수 있습니다.

"오프라인에서도 동작한다"는 경험은 사용자에게 단순한 편리한 기능을 넘어 애플리케이션에 대한 깊은 신뢰와 애착을 만들어냅니다. 꼭 여러분의 프로젝트에서도 PWA 기술을 도입하여 웹의 가능성을 최대한으로 끌어내 보시기 바랍니다.
