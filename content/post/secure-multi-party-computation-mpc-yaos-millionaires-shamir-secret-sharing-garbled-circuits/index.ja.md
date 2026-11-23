---
title: "入力を互いに明かさずに共同計算する仕組み：秘密計算（MPC）とヤオの億万長者問題"
description: "秘密計算（MPC）の理想・現実シミュレーション、シャミア秘密分散、BGW、SPDZ、ビーバーの乗算トリプル、紛失通信とガーブルド・サーキットを解説。FHE・ZKP・TEEとの違い、実例、出力・運用上の限界も紹介します。"
slug: "secure-multi-party-computation-mpc-yaos-millionaires-shamir-secret-sharing-garbled-circuits"
date: "2026-10-18T08:00:00+09:00"
lastmod: "2026-11-23"
image: "eyecatch.jpg"
categories:
  - "コンピュータ・暗号"
tags:
  - "Cryptography"
  - "Multi-Party Computation"
  - "Privacy-Enhancing Technologies"
  - "Information Security"
  - "Computer Science"
math: true
draft: false
---

「複数の病院が患者のゲノムを共同解析したいが、法令・契約・倫理審査や各機関の方針に従い、個人データの共有方法を慎重に設計する必要がある」
「競合する複数の銀行が、互いの顧客リストや不正取引の検知ノウハウを一切明かさずに、業界全体のマネーロンダリング経路だけを共同で特定したい」

常識的に考えれば、これらは矛盾した要求に見える。何らかの関数 $f(x_1, x_2, \dots, x_n)$ を計算するには、中央の主体が入力を集めて平文で処理する設計がまず思い浮かぶ。従来の設計では、信頼できる第三者（Trusted Third Party: TTP）——たとえば預託機関、銀行、監査法人、クラウド事業者——に役割を委ね、その管理策や約束を信頼することがある。MPCは、特定の脅威モデルのもとで、単一の主体に全入力を渡さず参加者が共同計算する別の設計を提供する。

しかし1980年代後半、現代暗号理論は、明示した攻撃者モデルや暗号学的仮定のもとで、信頼できる第三者を置かずに複数参加者が関数を共同計算するプロトコルを構成できることを示した。安全性は通常、各参加者が自身の入力・出力から知り得る情報を除き、プロトコル中の追加情報が理想機能以上に漏れないこととして定義される。公開された出力そのものが入力について情報を与える場合や、可用性・公平性など別の性質は、この定義だけでは解決しない。

この技術は<strong>秘密計算（Secure Multi-Party Computation: MPC）</strong>と呼ばれる。本稿では、紙とペンだけで理解できる直感的な2つの思考実験から出発し、MPCを支える2大数学エンジン——<strong>シャミアの秘密分散法（ラグランジュ補間）とビーバーの乗算トリプル</strong>による算術回路アプローチ、そして<strong>紛失通信（Oblivious Transfer）とヤオのガーブルド・サーキット（Garbled Circuits）</strong>による論理回路アプローチ——の内部構造を数式とPython実装で完全に解き明かす。さらに、完全準同型暗号（FHE）やゼロ知識証明（ZKP）、ハードウェア安全領域（TEE）との決定的な違いと、オークション・医療・暗号資産ウォレットにおける最先端の実社会応用までを体系的に掘り下げる。

---


**安全性の読み方**：本文中の「秘密が漏れない」という説明は、個別に示した脅威モデル・安全性定義・暗号学的仮定の範囲に限られます。通常は許可された入力・出力から推測できる情報を除く追加漏えいを評価し、出力自体の推測、実装・運用・可用性・サイドチャネルは別に検討します。

## 1. 直感を裏切る2つの思考実験：「上司なしの平均年収計算」と「ヤオの億万長者問題」

秘密計算の核心にある「データを隠したまま計算する」という感覚を掴むため、まずは暗号学の歴史において極めて重要な2つの思考実験を見てみよう。

### 1.1 思考実験①：誰にも自分の年収を知られずに「平均年収」だけを知る方法

同じカフェテーブルを囲む3人のエンジニア $A, B, C$ がいる。彼らは自分たちの待遇が妥当かを知るために、3人の<strong>平均年収 $\bar{x} = \frac{x_A + x_B + x_C}{3}$</strong> を知りたいと考えた。しかし、プライドや社内規定の都合上、<strong>自分の年収 $x_A, x_B, x_C$ がいくらであるかは、他の2人には絶対に知られたくない</strong>。また、彼ら全員が信頼できる上司や第三者もその場にはいない。紙とペンと耳打ち（1対1の秘匿通信）だけを使って、どうすれば各人の年収を平文で渡さずに、3人の合計 $S = x_A + x_B + x_C$ を求められるだろうか？

もし $A$ がそのまま自分の年収 $x_A = 800\text{万円}$ を $B$ に耳打ちしてしまえば、その瞬間に $B$ に $A$ の年収がバレてしまう。そこで $A$ は、計算を始める前に<strong>巨大な乱数によるマスク（ワンタイムパッド）</strong>をかけるという巧妙なトリックを使う。

1. <strong>乱数マスクの生成と最初の耳打ち（$A \to B$）</strong>：
   全員であらかじめ、3人の年収の合計よりも十分に大きな整数 $M$（たとえば $M = 10^9$）を決めておく。すべての計算は $M$ で割った余り（剰余環 $\mathbb{Z}_M = \{0, 1, \dots, M-1\}$）の上で行う。
   まずエンジニア $A$ は、サイコロや乱数生成器を使って、自分だけが知る一様乱数 $r \in \mathbb{Z}_M$（たとえば $r = 742,918,305$）を秘密裏に1つ選ぶ。そして自分の本当の年収 $x_A$ にこの乱数 $r$ を足し合わせた値
   $$s_1 = (x_A + r) \bmod M$$
   を計算し、この $s_1$ だけを隣の $B$ に耳打ちする。
   ここで重要なのは、$B$ の視点から見たとき、受け取った数値 $s_1$ は<strong>一様乱数 $r$ によって完全にマスクされているため、$x_A$ が 0 円であっても 5000 万円であっても、$s_1$ がその値になる確率はまったく同じ $1/M$ である</strong>という点だ。つまり、クロード・シャノンが証明した<strong>ワンタイムパッド（One-Time Pad）の完全秘匿性</strong>により、$B$ は $s_1$ から $x_A$ に関する情報を文字通り<strong>1ビットも得ることができない</strong>（相互情報量 $I(X_A; S_1) = 0$）。
2. <strong>第2の加算と耳打ち（$B \to C$）</strong>：
   数値 $s_1$ を受け取ったエンジニア $B$ は、そこに自分の年収 $x_B$ を足し合わせる：
   $$s_2 = (s_1 + x_B) \bmod M = (x_A + x_B + r) \bmod M$$
   そして $B$ はこの $s_2$ を隣の $C$ に耳打ちする。$C$ にとっても、乱数 $r$ の値がまったく分からないため、$s_2$ は依然として $\mathbb{Z}_M$ 上の単なる一様乱数にしか見えず、$x_A + x_B$ がいくらなのか1ビットも推測できない。
3. <strong>第3の加算と返却（$C \to A$）</strong>：
   数値 $s_2$ を受け取ったエンジニア $C$ は、そこに自分の年収 $x_C$ を足し合わせる：
   $$s_3 = (s_2 + x_C) \bmod M = (x_A + x_B + x_C + r) \bmod M$$
   そして $C$ はこの $s_3$ を最初のエンジニア $A$ に伝える。
4. <strong>乱数マスクの除去と結果の公表</strong>：
   最後に、乱数 $r$ を最初に作った張本人である $A$ が、受け取った $s_3$ から自分の乱数 $r$ を引き算する：
   $$S = (s_3 - r) \bmod M = x_A + x_B + x_C$$
   $A$ はこの合計 $S$ を3で割った平均年収 $\bar{x} = S / 3$ をテーブルの全員に公表する。

このプロトコルを振り返ってみよう。$B$ が見たのは $x_A + r$ と最終結果 $x_A + x_B + x_C$ だけであり、$r$ を知らないため $x_A$ と $x_C$ の内訳を知ることはできない。$C$ が見たのは $x_A + x_B + r$ と最終結果だけであり、やはり $x_A$ と $x_B$ の内訳は分からない。そして最初の $A$ も、自分が受け取った $s_3$ から $r$ を引いたときに初めて2人の合計 $x_B + x_C$ を知るが、それは「3人の合計 $S$ と自分の年収 $x_A$ から当然逆算できる情報（$S - x_A = x_B + x_C$）」に過ぎず、$B$ と $C$ の個別の年収がいくらであるかは $A$ にも決して分からない！

> **この耳打ち例の限界**：これは秘密計算プロトコルの証明ではなく、教材用の例である。隣接する通信が秘密で、参加者が正直に動き、共謀しないことを仮定する。たとえば $B$ と $C$ が手元の値を共有すると、公開された合計と合わせて $A$ の入力を復元できる。実運用には安全性が証明されたプロトコルを使う必要がある。さらに、剰余による折り返しを避けるには $M$ を入力合計より大きくしなければならない。

> [!NOTE]
> <strong>なぜ「2人」ではなく「3人以上」で平均を計算するのか？</strong>
> もし参加者がアリスとボブの2人だけだった場合、たとえ神様が間に入って2人の平均年収 $\bar{x} = \frac{x_A + x_B}{2}$ だけを教えてくれたとしても、アリスは自分の年収 $x_A$ を知っているため、$x_B = 2\bar{x} - x_A$ という引き算によってボブの年収を100%特定できてしまう。これは計算プロトコルの欠陥ではなく、<strong>「計算したい関数 $f(x_A, x_B) = \frac{x_A + x_B}{2}$ の出力そのものが相手の秘密を完全に決定してしまう」</strong>という数学的性質である。秘密計算（MPC）が保証するのは「<strong>最終出力 $f(x_1, \dots, x_n)$ から論理的に導かれる情報以外に、計算の過程から1ビットも余計な情報を漏らさないこと</strong>」である。出力から個人値をどこまで推測できるかは、入力の範囲・相関・他に公開する出力にも依存する。参加者が3人いるだけでプライバシーが保証されるわけではない。

ちなみに、上記の耳打ち方式はもう一歩洗練させることができる。エンジニア $A$ が自分の年収 $x_A$ を、ランダムな3つの断片（シェア） $x_{A,1}, x_{A,2}, x_{A,3} \in \mathbb{Z}_M$ に分解し、
$$x_A \equiv x_{A,1} + x_{A,2} + x_{A,3} \pmod M$$
となるようにして、$x_{A,1}$ を自分自身の手元に残し、$x_{A,2}$ を $B$ に、$x_{A,3}$ を $C$ に配るのである。$B$ と $C$ もまったく同じように自分の年収を3つのランダムなシェアに分解して互いに配る。その後、3人がそれぞれ「手元に集まった3つのシェアの合計 $S_j = (x_{A,j} + x_{B,j} + x_{C,j}) \bmod M$」を計算して一斉に公開し、最後に $S = (S_1 + S_2 + S_3) \bmod M$ を足し合わせればよい。これを<strong>加法的秘密分散（Additive Secret Sharing）</strong>と呼び、現代の高速秘密計算フレームワークの最も基本的な構成要素となっている。

---

### 1.2 思考実験②：アンドリュー・ヤオの「億万長者問題（Millionaires' Problem）」

足し算だけであれば、上記のように乱数でマスクして足し合わせるだけで驚くほど簡単に秘密計算ができた。では、<strong>「大小比較（不等号）」</strong>はどうだろうか？

1982年、のちにチューリング賞を受賞する計算機科学者<strong>アンドリュー・ヤオ（Andrew Chi-Chih Yao）</strong>は、歴史的論文 *"Protocols for Secure Computations"* の中で、現代の秘密計算（MPC）という学問分野そのものを創始する有名な問題を提起した。それが<strong>「ヤオの億万長者問題（Yao's Millionaires' Problem）」</strong>である。

* <strong>問題設定</strong>：2人の億万長者アリス（資産 $x$ 百万ドル）とボブ（資産 $y$ 百万ドル）が偶然出会った。2人は<strong>「どちらがより裕福か（すなわち $x > y$ かどうか）」</strong>を計算したい。比較結果自体は相手に知られるため、理想的な安全性であってもこの出力から得られる情報は避けられない。目標は、明示した脅威モデルと暗号学的仮定のもとで、出力から推測できる以上の資産情報をプロトコルが漏らさないことである。

一見すると先ほどの平均年収問題に似ているが、数学的な難易度は劇的に跳ね上がる。
もし先ほどの方法で $x - y$ を計算して公開してしまえば、その瞬間に相手の資産額そのものが $x = y + (x - y)$ として完全にバレてしまう。知りたいのは差額 $x - y$ ではなく、その符号を表す<strong>非線形なステップ関数（比較述語）</strong>
$$f(x, y) = \begin{cases} 1 & (x > y \text{ のとき}) \\ 0 & (x \le y \text{ のとき}) \end{cases}$$
の1ビットだけなのだ。二進数のビット列で $x > y$ を判定するには、最上位ビットから順番に「両方のビットが等しいか（XOR の否定）」と「どちらが 1 でどちらが 0 か（AND ゲート）」を連鎖的に評価していく必要がある。つまり、<strong>単なる足し算（線形演算）だけでなく、掛け算（AND演算・非線形演算）を秘密のまま実行する仕組み</strong>が不可欠になるのである。

ヤオはこの問題を解くために、のちに<strong>「ガーブルド・サーキット（Garbled Circuits：暗号化回路）」</strong>と呼ばれる革命的な手法を考案した。その詳細なメカニズムは第5節で完全に解説するが、まずはその前に、「秘密計算が安全である」とは数学的にどういうことなのかを厳密に定義しておこう。

---

## 2. 秘密計算（MPC）の数学的定式化：理想世界と現実世界のシミュレーション・パラダイム

暗号プロトコルを設計する際、「アリスはボブの入力 $y$ を知ることができない」という主張は、脅威モデルと許可される出力を定めて数学的に表す必要がある。たとえば出力や事前知識から推測できる情報と、通信記録が新たに漏らす情報を区別する。安全性定義によって実際の攻撃者の視点とシミュレータの分布が一致する場合も、効率的に識別できない場合もある。

この問題を解決するために、ゴールドライヒ、ミカリ、ウィグダーソン（Oded Goldreich, Silvio Micali, Avi Wigderson: GMW 1987）らによって確立され、のちにラン・カネッティ（Ran Canetti）の Universal Composability (UC) フレームワークへと結晶化したのが、<strong>「理想世界／現実世界のシミュレーション・パラダイム（Ideal/Real Simulation Paradigm）」</strong>である。

```mermaid
flowchart TD
    subgraph IdealWorld["理想世界 (Ideal World): 絶対に安全な基準"]
        direction TB
        PA1["パーティ P1 (秘密入力 x1)"] -->|"安全な通信路で x1 を送信"| TTP["信頼できる神 / 金庫 (Ideal Functionality F)"]
        PA2["パーティ P2 (秘密入力 x2)"] -->|"安全な通信路で x2 を送信"| TTP
        PAn["パーティ Pn (秘密入力 xn)"] -->|"安全な通信路で xn を送信"| TTP
        TTP -->|"出力 y = f(x1,...,xn) のみを返却"| Out1["全員が y だけを知る (途中経過の漏洩は定義上ゼロ)"]
        Out1 --> Sim["シミュレータ S (不正パーティの入力と出力 y だけから偽の通信ログを生成)"]
    end

    subgraph RealWorld["現実世界 (Real World): 実際の暗号プロトコル Π"]
        direction TB
        RB1["パーティ P1 (秘密入力 x1)"] <-->|"暗号文・乱数シェアの相互通信"| RB2["パーティ P2 (秘密入力 x2)"]
        RB2 <-->|"暗号文・乱数シェアの相互通信"| RBn["パーティ Pn (秘密入力 xn)"]
        RB1 <-->|"暗号文・乱数シェアの相互通信"| RBn
        RB2 --> View["攻撃者 A が観測する通信ログ全体 View_A(x1,...,xn)"]
    end

    Sim <-->|"確率分布として識別不可能 (View_A ≈ Sim)"| View
```

### 2.1 理想世界（Ideal World）と現実世界（Real World）

$n$ 人のパーティ $P_1, P_2, \dots, P_n$ がそれぞれ秘密の入力 $x_1, x_2, \dots, x_n$ を持ち、共同で関数 $f(x_1, \dots, x_n) = (y_1, \dots, y_n)$ を計算したいとする。ここで一部のパーティ集合 $I \subset \{1, \dots, n\}$ が攻撃者 $\mathcal{A}$ に乗っ取られ（あるいは互いに結託し）、正直なパーティたちの秘密を暴こうとしている状況を考える。

1. <strong>理想世界（Ideal World）</strong>：
   この世界には、絶対に買収されず、決して情報を漏らさない全知全能の「神（理想機能 $\mathcal{F}$：Ideal Functionality）」が存在すると仮定する。各パーティ $P_i$ は自分の秘密入力 $x_i$ を誰にも見られない専用パイプで神 $\mathcal{F}$ に渡す。神 $\mathcal{F}$ は一人で黙って $f(x_1, \dots, x_n)$ を計算し、各パーティ $P_i$ にその人の出力 $y_i$ だけを返す。
   この理想世界では、パーティ間のやり取りが一切存在しないため、結託した不正パーティ集合 $I$ が知り得る情報は、定義上<strong>「自分たちの入力 $\{x_i\}_{i \in I}$ と、神から返された自分たちの出力 $\{y_i\}_{i \in I}$」だけ</strong>である。これ以上安全な状態は原理的に存在しない。
2. <strong>現実世界（Real World）</strong>：
   神 $\mathcal{F}$ は存在しない。代わりに各パーティは暗号プロトコル $\Pi$ に従って、何ラウンドにもわたりメッセージ（乱数シェアや暗号文）を送受信し、最終的に出力 $y_i$ を得る。このとき、結託した不正パーティ集合 $I$ の手元には、自分たちの入力・内部乱数・そして正直なパーティから送られてきたすべての受信メッセージの履歴——これを<strong>攻撃者の視点 $\text{View}_I^\Pi(x_1, \dots, x_n)$</strong> と呼ぶ——が残る。

### 2.2 シミュレータ $\mathcal{S}$ による安全性の厳密な定義

では、現実世界のプロトコル $\Pi$ が「理想世界の神 $\mathcal{F}$ と同じくらい安全である」とはどういうことか？
それは、<strong>「理想世界に棲むアルゴリズム（シミュレータ $\mathcal{S}$）が、不正パーティ自身の入力 $\{x_i\}_{i \in I}$ と最終出力 $\{y_i\}_{i \in I}$ だけを与えられた状態で、正直なパーティの本当の入力 $\{x_j\}_{j \notin I}$ を一切見ることなく、現実世界で攻撃者が目にするはずの通信ログ $\text{View}_I^\Pi(x_1, \dots, x_n)$ とまったく見分けがつかない『模造の通信ログ』を単独で捏造（シミュレート）できること」</strong>として定義される：

$$\left\{ \mathcal{S}\left(I, \{x_i\}_{i \in I}, \{y_i\}_{i \in I}\right) \right\} \stackrel{c}{\approx} \left\{ \text{View}_I^\Pi(x_1, \dots, x_n) \right\}$$

ここで $\stackrel{c}{\approx}$ は計算量的識別不能（Computationally Indistinguishable：いかなる多項式時間アルゴリズムも両者の確率分布を区別できないこと）を表し、もし二つの確率分布が文字通り完全に一致する（$\equiv$）ならば<strong>情報理論的安全性（Information-Theoretic / Perfect Security）</strong>と呼ばれる。

なぜシミュレータ $\mathcal{S}$ の存在が「通信記録は定義済みの入力・出力を超える情報を漏らさない」という保証になるのだろうか？
現実世界の攻撃者の視点と、許可された入力・出力だけから作るシミュレータの視点が、選んだ安全性定義のもとで一致する（または計算量的に識別不能である）なら、効率的な攻撃者は通信記録から追加情報を識別できない。ただし保証は指定した攻撃者モデル・機能・仮定に対するもので、あらゆるプロトコルの情報理論的漏えいがゼロだという意味ではない。

たとえば第1節の「3人の平均年収計算」では、不正なエンジニア $B$ が見る通信ログは $s_1 = (x_A + r) \bmod M$ と最終合計 $S$ である。シミュレータ $\mathcal{S}$ は、$A$ の年収 $x_A$ をまったく知らなくても、単に $\mathbb{Z}_M$ から一様乱数 $\tilde{s}_1 \xleftarrow{\$} \mathbb{Z}_M$ を1つ適当に選んで「これが $A$ から届いたメッセージだ」と差し出すだけでよい。本物の $s_1$ も模造の $\tilde{s}_1$ も $\mathbb{Z}_M$ 上の完全な一様分布に従うため、両者の確率分布は 100% 同一であり、情報理論的な完全安全性が直ちに証明される。

---

### 2.3 攻撃者モデル（Adversary Models）と結託閾値の分類

MPCプロトコルを設計・評価する際には、「敵がどこまで悪質な行動をとるか」と「何人まで裏切るか」という2つの軸を明確に区別する必要がある。

| 分類軸 | モデル名 | 定義と特徴 | 代表的なプロトコル・対策 |
| :--- | :--- | :--- | :--- |
| <strong>行動の悪質さ</strong> | <strong>セミオネスト攻撃者</strong><br>(Semi-Honest / Passive) | 「正直だが好奇心旺盛（Honest-but-Curious）」。プロトコルの手順・計算ルールには100%忠実に従うが、通信ログを後から徹底解析して他人の秘密を暴こうとする。 | 基本形Shamir秘密分散 (BGW)、基本形YaoのGarbled Circuits、GMWプロトコル |
| <strong>行動の悪質さ</strong> | <strong>マリシャス攻撃者</strong><br>(Malicious / Active) | プロトコルを無視して嘘の計算結果を送る、自分の入力を途中で書き換える、都合が悪くなると通信を切断する（Abort）など、あらゆる改ざんを行うビザンチン攻撃者。 | 検証可能秘密分散 (VSS)、SPDZ（情報理論的MAC付きシェア）、Cut-and-Choose法、ゼロ知識証明 (ZKP) |
| <strong>結託の人数</strong> | <strong>正直多数（Honest Majority）</strong><br>受動的なプライバシーでは腐敗数 $c<n/2$。標準的なBGWの能動的安全性では通常 $c<n/3$。 | 情報理論的保証が可能だが、攻撃者の行動、通信仮定、可用性・公平性などの保証は区別する。 | BGW（脅威モデル別）、複製秘密分散方式 |
| <strong>結託の人数</strong> | <strong>不正多数（Dishonest Majority）</strong><br>最大 $n-1$ 人の結託を許す方式もある。一般的な機能の安全性は、設定や関数、求める性質に依存する。 | 多くの方式ではOT等の計算量的仮定を使う。安全な計算でも出力漏えい・中断等が別途残り得る。 | YaoのGarbled Circuits (2PC)、GMW、SPDZ / MASCOT / Overdrive |

---

## 3. 第1の数学的エンジン：シャミアの $(t, n)$ 閾値秘密分散法とラグランジュ補間

ここからは、現代のMPCを支える第1の数学的柱である<strong>「秘密分散（Secret Sharing）ベースの算術回路計算」</strong>に踏み込もう。

第1節で紹介した加法的秘密分散（$s \equiv s_1 + s_2 + \dots + s_n \pmod M$）には1つ弱点がある。それは「$n$ 人全員が揃わなければ秘密を復元できず、たった1人でもサーバーが故障したり通信を拒否したりすると計算が永久に止まってしまう」という点、そして「そのままでは秘密同士の掛け算（乗算）ができない」という点である。

この両方の課題を一挙に解決する美しい代数構造が、RSA暗号の発明者の1人でもある<strong>アディ・シャミア（Adi Shamir）</strong>が1979年のわずか2ページの論文 *"How to share a secret"* で発表した<strong>シャミアの $(t, n)$ 閾値秘密分散法（Shamir's Threshold Secret Sharing）</strong>である。

### 3.1 多項式の自由度を利用した秘密の分割（Share Generation）

シャミアの着想は、中学校や高校で習う代数学の極めてシンプルな定理に基づいている。

* $1$ 次関数（直線） $y = s + a_1 x$ は、平面上の異なる <strong>$2$ 個の点</strong>を指定すればただ1本に決まる（1点しか分からなければ、その点を通る直線はあらゆる傾きで無限に引けるため、切片 $s$ はまったく決まらない）。
* $2$ 次関数（放物線） $y = s + a_1 x + a_2 x^2$ は、異なる <strong>$3$ 個の点</strong>を指定すればただ1つに決まる（2点しか分からなければ、その2点を通る放物線は無限に存在し、切片 $s$ はあらゆる値をとり得る）。
* 一般に、<strong>$t-1$ 次多項式は、異なる $t$ 個の点 $(x_1, y_1), \dots, (x_t, y_t)$ を通るものがただ1つ一意に定まるが、$t-1$ 個以下の点しか与えられなければ、定数項（$y$ 切片）の値はすべての候補が完全に等確率で起こり得る。</strong>

これをそのまま暗号プロトコルに仕立て上げる。ただし、実数 $\mathbb{R}$ 上で計算すると「点の座標の大きさから大体の範囲が推測できてしまう（情報漏洩）」うえに浮動小数点の丸め誤差が生じるため、すべての計算を<strong>大きな素数 $p$（$p > n$）を法とする有限体（ガロア体） $\mathbb{F}_p = \{0, 1, 2, \dots, p-1\}$</strong> の上で行う。

<strong>【シャミアの $(t, n)$ 分散アルゴリズム】</strong>
秘密にしたい数値を $s \in \mathbb{F}_p$ とする。参加者 $n$ 人のうち、任意の $t$ 人以上が集まれば $s$ を復元でき、$t-1$ 人以下が結託しても $s$ について1ビットの情報も得られないようにしたい（これを $(t, n)$-閾値法と呼ぶ）。

1. ディーラー（秘密の持ち主）は、有限体 $\mathbb{F}_p$ から $t-1$ 個の独立な一様乱数 $a_1, a_2, \dots, a_{t-1} \xleftarrow{\$} \mathbb{F}_p$ を選び、定数項に秘密 $s$ を据えた $t-1$ 次多項式 $P(x) \in \mathbb{F}_p[x]$ を構成する：
   $$P(x) = s + a_1 x + a_2 x^2 + \dots + a_{t-1} x^{t-1} \pmod p$$
   ここで明らかに、$x = 0$ を代入したときの値（$y$ 切片）が元の秘密 $P(0) = s$ である。
2. ディーラーは、各パーティ $P_i$（$i = 1, 2, \dots, n$）に対して、それぞれ異なる非ゼロの公開座標 $x_i \in \mathbb{F}_p \setminus \{0\}$（通常はそのまま番号 $x_i = i$ を使う）における多項式の評価値
   $$y_i = P(x_i) \pmod p$$
   を計算し、点 $(x_i, y_i)$ をパーティ $P_i$ の<strong>シェア（断片）</strong>として秘密裏に配布する。

### 3.2 ラグランジュ補間公式（Lagrange Interpolation）による秘密の復元

さて、$n$ 人のうち任意の $t$ 人の集合 $T \subset \{1, \dots, n\}$（$|T| = t$）が自分のシェア $\{(x_i, y_i)\}_{i \in T}$ を持ち寄ったとしよう。彼らはどうやって元の多項式 $P(x)$、とりわけその定数項 $s = P(0)$ を求めるのだろうか？連立一次方程式（ヴァンデルモンド行列の逆行列）を解いてもよいが、数値解析における<strong>ラグランジュの補間公式（Lagrange Polynomial Interpolation）</strong>を使えば、一発で明示的な式として書き下すことができる。

集合 $T$ に属する各インデックス $i \in T$ に対して、<strong>「点 $x = x_i$ でだけ $1$ になり、他のすべての点 $x = x_j$ ($j \in T \setminus \{i\}$) で $0$ になる」</strong>という都合のよい $t-1$ 次多項式——<strong>ラグランジュ基底多項式 $\ell_i(x)$</strong>——を次のように定義する：

$$\ell_i(x) = \prod_{j \in T,\, j \ne i} \frac{x - x_j}{x_i - x_j} \pmod p$$

実際に確かめてみよう。$x = x_i$ を代入すれば、分子と分母がすべて一致して $\frac{x_i - x_j}{x_i - x_j} = 1$ の積となるため $\ell_i(x_i) = 1$ である。一方、$i$ 以外の任意の $k \in T$ ($k \ne i$) に対して $x = x_k$ を代入すると、積の中に必ず分子が $x_k - x_k = 0$ となる因数が1つ現れるため $\ell_i(x_k) = 0$ となる（なお、有限体 $\mathbb{F}_p$ における割り算 $\frac{A}{B}$ は、フェルマーの小定理 $B^{p-2} \bmod p$ または拡張ユークリッド互除法によるモジュラ逆元 $B^{-1} \bmod p$ を掛ける演算 $A \cdot B^{-1} \pmod p$ である）。

すると、各シェアの値 $y_i$ にこの基底多項式 $\ell_i(x)$ を掛けて足し合わせた多項式
$$P(x) = \sum_{i \in T} y_i \cdot \ell_i(x) \pmod p$$
は、高々 $t-1$ 次でありながら、すべての $k \in T$ に対して $P(x_k) = \sum_{i \in T} y_i \delta_{ik} = y_k$ を満たす。異なる $t$ 個の点を通る $t-1$ 次多項式はただ1つしか存在しないため、これこそが元の多項式 $P(x)$ そのものである！

私たちが本当に欲しいのは多項式全体ではなく、<strong>定数項である秘密 $s = P(0)$ だけ</strong>である。したがって、上式に $x = 0$ を代入すれば、次の極めてシンプルかつ美しい復元公式が得られる：

$$s = P(0) = \sum_{i \in T} y_i \cdot \ell_i(0) = \sum_{i \in T} y_i \left( \prod_{j \in T,\, j \ne i} \frac{-x_j}{x_i - x_j} \right) \pmod p$$

ここで、括弧内の定数 $\lambda_i = \ell_i(0) = \prod_{j \in T, j \ne i} \frac{-x_j}{x_i - x_j} \pmod p$ は、誰が参加したか（座標 $\{x_i\}_{i \in T}$）さえ決まれば、シェアの値 $y_i$ とは無関係に事前に計算できる公開の定数（ラグランジュ補間係数）である。つまり、<strong>秘密 $s$ の復元とは、各パーティのシェア $y_i$ に定数 $\lambda_i$ を掛けて足し合わせる単なる線形結合（内積） $\sum_{i \in T} \lambda_i y_i \pmod p$ に過ぎない</strong>のだ！

### 3.3 なぜ $t-1$ 人では1ビットも推測できないのか（情報理論的完全安全性の証明）

ここで、「$t-1$ 個のシェアが集まれば、あと1点足りないだけなのだから、秘密 $s$ の候補がある程度絞り込めてしまうのではないか？」という疑問を抱くかもしれない。答えは<strong>「断じてノー（1ビットたりとも絞り込めない）」</strong>である。

数学的に証明しよう。攻撃者が $t-1$ 個のシェア $(x_1, y_1), \dots, (x_{t-1}, y_{t-1})$ を手に入れたとする。いま、有限体 $\mathbb{F}_p$ の中から任意の仮説上の秘密の値 $s' \in \mathbb{F}_p$ を1つ勝手に選んでみよう。この仮説 $s'$ は点 $(0, s')$ を意味する。
すると、攻撃者が持っている $t-1$ 個の点 $(x_1, y_1), \dots, (x_{t-1}, y_{t-1})$ と、仮説の点 $(0, s')$ を合わせると、<strong>互いに異なる $x$ 座標を持つ合計 $t$ 個の点</strong>が揃うことになる。ラグランジュ補間の定理により、この $t$ 個の点をすべて通る $t-1$ 次多項式 $P_{s'}(x)$ が、<strong>どのような $s' \in \mathbb{F}_p$ を選んでも必ずただ1つずつ一意に存在する</strong>！

ディーラーが最初にランダムな係数 $(a_1, \dots, a_{t-1}) \in \mathbb{F}_p^{t-1}$ を選ぶ確率は、どの組み合わせに対しても完全に等しく $\frac{1}{p^{t-1}}$ である。したがって、観測された $t-1$ 個のシェアと整合する多項式 $P_{s'}(x)$ は、すべての $s' \in \{0, 1, \dots, p-1\}$ に対してちょうど1本ずつ、まったく同じ確率 $\frac{1}{p^{t-1}}$ で存在する。ゆえに、事後確率分布は事前確率分布とまったく変わらず、シャノン・エントロピーの言葉で書けば
$$H(S \mid Y_1 = y_1, \dots, Y_{t-1} = y_{t-1}) = H(S)$$
が厳密に成り立つ。たとえ攻撃者が宇宙の年齢以上の時間をかけて全探索を行える無限の計算能力（量子コンピュータを含む）を持っていたとしても、$t-1$ 個のシェアからは元の秘密 $s$ について1ビットの偏りも見出すことができないのである。

---

### 3.4 BGWプロトコル：シェアのまま「足し算」と「掛け算」を行う方法

シャミアの秘密分散が真に驚異的なのは、秘密をただ金庫のように分割保存できるだけでなく、<strong>「分割されたシェアの状態で、元の秘密を一度も復元することなく足し算や掛け算ができる（準同型性を持つ）」</strong>という点にある。1988年、マイケル・ベン＝オア（Michael Ben-Or）、シャフィ・ゴールドワッサー（Shafi Goldwasser）、アヴィ・ウィグダーソン（Avi Wigderson）の3人は、この性質を使って任意の算術回路を秘密計算する<strong>BGWプロトコル</strong>を発表した。

いま、2つの秘密 $a, b \in \mathbb{F}_p$ がそれぞれ $t-1$ 次多項式 $P(x), Q(x)$（ただし $P(0) = a, Q(0) = b$）によって分散されており、各パーティ $P_i$ がシェア $y_i^{(a)} = P(x_i)$ と $y_i^{(b)} = Q(x_i)$ を持っているとしよう。この状態を $[a], [b]$ と表記する。

#### ① 秘密の加算（$[a] + [b] = [a + b]$）と定数倍（$c \cdot [a] = [c \cdot a]$）：通信コスト完全ゼロ

2つの多項式を足し合わせた新しい多項式 $R(x) = P(x) + Q(x) \pmod p$ を考えてみよう。
多項式の和の性質から、$R(x)$ の次数もやはり高々 $t-1$ 次であり、その定数項は
$$R(0) = P(0) + Q(0) = a + b \pmod p$$
となる！しかも、点 $x_i$ における $R(x)$ の評価値は
$$R(x_i) = P(x_i) + Q(x_i) = y_i^{(a)} + y_i^{(b)} \pmod p$$
に他ならない。
これが何を意味するか分かるだろうか？各パーティ $P_i$ が<strong>誰とも一切通信することなく、自分の手元にある2つのシェア $y_i^{(a)}$ と $y_i^{(b)}$ をただ足し算するだけ</strong>で、その計算結果 $y_i^{(a+b)} = (y_i^{(a)} + y_i^{(b)}) \bmod p$ は、自動的に「和 $a + b$ を定数項に持つ $t-1$ 次多項式 $R(x)$ の正しいシャミア・シェア」になっているのである！公開の定数 $c \in \mathbb{F}_p$ を掛けるスカラー倍 $c \cdot [a] = [c \cdot a]$ もまったく同様に、手元のシェアを $c$ 倍するだけで通信ゼロで完了する。

#### ② 秘密同士の乗算（$[a] \cdot [b] = [a \cdot b]$）：次数の倍増と次数縮約（Degree Reduction）

では、秘密 $a$ と秘密 $b$ の掛け算 $a \cdot b \pmod p$ はどうだろうか？
もし各パーティ $P_i$ が手元で自分のシェア同士を掛け算して
$$z_i = y_i^{(a)} \cdot y_i^{(b)} = P(x_i) \cdot Q(x_i) \pmod p$$
を計算したとすると、この $z_i$ は積多項式 $H(x) = P(x) \cdot Q(x) \pmod p$ の点 $x_i$ における評価値となっている。そして確かに、$H(x)$ の定数項は
$$H(0) = P(0) \cdot Q(0) = a \cdot b \pmod p$$
であり、欲しい積 $a \cdot b$ そのものになっている！

しかし、ここに<strong>2つの重大な壁</strong>が立ちはだかる。
1. <strong>多項式の次数の倍増</strong>：$P(x)$ が $t-1$ 次式、$Q(x)$ も $t-1$ 次式であるため、それらを掛け合わせた $H(x) = P(x)Q(x)$ は<strong>次数が $2(t-1)$ に倍増してしまっている</strong>！もしこのまま次の掛け算をもう一度行えば次数は $4(t-1)$、次は $8(t-1)$ へと指数関数的に膨れ上がり、すぐにパーティ総数 $n$ を超えて補間不可能（復元不可能）になってしまう。
2. <strong>係数のランダム性の崩壊</strong>：$2(t-1)$ 次多項式 $H(x)$ は2つの $t-1$ 次多項式の積として作られているため（因数分解可能な特殊な多項式であるため）、その高次係数は独立な一様乱数ではなく、そのまま公開すると元の多項式 $P(x), Q(x)$ の情報が漏れてしまう。

そこでBGWプロトコルでは、手元でシェアを掛け算した直後に、<strong>次数を $2(t-1)$ から元の $t-1$ に引き戻し、かつ係数を完全にランダム化し直す「次数縮約（Degree Reduction）ステップ」</strong>を1ラウンドの通信で行う。

まず前提として、次数 $2(t-1)$ の多項式 $H(x)$ の定数項 $H(0) = a \cdot b$ をラグランジュ補間で一意に決定するためには、少なくとも $2(t-1) + 1 = 2t - 1$ 個の評価点が必要である。したがって、参加者の総数 $n$ は必ず
$$2t - 1 \le n \iff t \le \left\lfloor \frac{n + 1}{2} \right\rfloor$$
を満たしていなければならない。結託しても秘密が漏れない最大人数は $t - 1$ 人だから、これは<strong>不正パーティの数 $t - 1 < \frac{n}{2}$（すなわち参加者の過半数が正直：Honest Majority）</strong>であることを意味する（たとえば閾値 $t = 2$ なら最低 $n = 2(2) - 1 = 3$ 人のパーティが必要）。

$n \ge 2t - 1$ が満たされているとき、任意の $2t - 1$ 人（簡単のため $i = 1, \dots, 2t-1$ とする）の積シェア $z_i = H(x_i)$ に対して、ラグランジュ補間係数 $\lambda_i = \prod_{j=1, j \ne i}^{2t-1} \frac{-x_j}{x_i - x_j} \pmod p$ を用いれば、
$$a \cdot b = H(0) = \sum_{i=1}^{2t-1} \lambda_i z_i \pmod p$$
という<strong>線形結合</strong>で積 $a \cdot b$ が表せることに注目しよう！
この式はただの足し算と定数倍（線形結合）なのだから、以下の手順で次数を $t-1$ に戻すことができる：

1. <strong>積シェアの再分散（Sub-sharing）</strong>：各パーティ $P_i$ ($i = 1, \dots, 2t-1$) は、自分が計算した中間値 $z_i = y_i^{(a)} y_i^{(b)} \pmod p$ を「新たな秘密」とみなし、新しいランダムな<strong>$t-1$ 次多項式</strong> $R_i(x)$（ただし $R_i(0) = z_i$）を使って全パーティ $P_1, \dots, P_n$ に再分散する（$P_i$ から $P_k$ へ点 $s_{i \to k} = R_i(x_k)$ を送る）。
2. <strong>手元でのラグランジュ線形結合</strong>：各パーティ $P_k$ ($k = 1, \dots, n$) は、$2t-1$ 人から受け取った再分散シェア $s_{1 \to k}, \dots, s_{2t-1 \to k}$ に対して、公開のラグランジュ係数 $\lambda_i$ を掛けて足し合わせる：
   $$y_k^{(a \cdot b)} = \sum_{i=1}^{2t-1} \lambda_i \cdot s_{i \to k} = \sum_{i=1}^{2t-1} \lambda_i R_i(x_k) \pmod p$$
3. <strong>完了</strong>：新しい多項式 $R_{\text{new}}(x) = \sum_{i=1}^{2t-1} \lambda_i R_i(x) \pmod p$ は、<strong>$t-1$ 次多項式の線形結合なので次数は正しく $t-1$ に戻っており</strong>、しかもその定数項は
   $$R_{\text{new}}(0) = \sum_{i=1}^{2t-1} \lambda_i R_i(0) = \sum_{i=1}^{2t-1} \lambda_i z_i = H(0) = a \cdot b \pmod p$$
   となって、完全に独立ランダムな $t-1$ 次多項式による積 $[a \cdot b]$ のシャミア・シェアが得られるのである！

標準的なBGWで $2t-1\le n$ となる補間条件は、基本的な受動攻撃者モデルの説明である。能動的・悪意ある攻撃に耐えるには不正シェアの検知・一貫性検証などが必要で、標準設定では通常 $c<n/3$ の閾値を要する。

---

## 4. オフライン／オンライン分離の革命：ドナルド・ビーバーの乗算トリプルとSPDZプロトコル

BGWプロトコルは理論的に完璧な美しさを持っているが、実用上は2つの制約があった。第1に「掛け算のたびに全パーティ間で多項式の再分散（$O(n^2)$ 個のメッセージ通信）が必要になること」、第2に「$2t - 1 \le n$ という次数条件のせいで、2人だけの秘密計算（$n=2, t=2$）や不正な過半数（Dishonest Majority）では使えないこと」である。

この壁を打ち破り、現代の秘密計算（SPDZ、MASCOT、ABYなど）の標準アーキテクチャを確立したのが、1991年に<strong>ドナルド・ビーバー（Donald Beaver）</strong>が考案した<strong>「ビーバーの乗算トリプル（Beaver's Multiplication Triples）」</strong>である。

### 4.1 ビーバーの乗算トリプル $([u], [v], [w])$ を使うオンライン乗算

ビーバーのアイデアは、計算プロセスを以下の2つのフェーズに完全に切り離すことにある：

* <strong>オフライン（事前準備）フェーズ（Offline / Preprocessing Phase）</strong>：実際に計算したい秘密データ $x, y$ がまだ入力される前（たとえば夜間のアイドル時間中）に、誰にも値が分からないランダムな秘密の3つ組 $([u], [v], [w])$ ——ただし $u, v \xleftarrow{\$} \mathbb{F}_p$ は一様乱数であり、<strong>$w = u \cdot v \pmod p$ という積の関係を満たす</strong>——を大量に事前生成して各パーティにシェアとして蓄えておく。
* <strong>オンラインフェーズ（Online Phase）</strong>：秘密入力 $[x], [y]$ が与えられた後、事前生成した乗算トリプル $([u], [v], [w])$ を1組消費し、プロトコルに応じてマスク差分 $d=x-u$ と $e=y-v$ を開示して積のシェアを計算する。通信遅延や処理性能は方式・実装・ネットワーク条件に依存する。

なぜランダムな積 $w = u \cdot v$ のシェアを持っているだけで、任意の秘密 $x$ と $y$ の積 $[x \cdot y]$ が線形演算だけで計算できてしまうのか？その鮮やかな代数トリックを導出しよう。

<strong>【ビーバーの乗算プロトコル】</strong>
各パーティは秘密入力のシェア $[x], [y]$（これはシャミア秘密分散でも加法的秘密分散でもよい！）と、未使用の乗算トリプル $([u], [v], [w])$（ただし $w = u \cdot v \pmod p$）を持っているとする。

1. <strong>乱数マスク付きの差分シェアの局所計算（通信ゼロ）</strong>：
   各パーティは手元の引き算（線形演算）だけで、以下の2つのシェアを計算する：
   $$[d] = [x] - [u] \pmod p, \qquad [e] = [y] - [v] \pmod p$$
2. <strong>マスクされた差分 $d, e$ の公開（Open）</strong>：
   全員で $[d]$ と $[e]$ のシェアを持ち寄って復元し、平文の数値 $d = (x - u) \bmod p$ と $e = (y - v) \bmod p$ を<strong>全員に公開する</strong>。
   正しく前処理されたトリプルの共有値 $u,v$ が入力と独立で一様に分布し、再利用されない理想化モデルでは、$d,e$ の開示から許可された値を超える情報は得られない。悪意ある参加者への安全性には、トリプルの真正性・整合性検査を含む具体的なプロトコルが必要である。
3. <strong>公開された定数 $d, e$ を用いた線形結合による積の合成（通信ゼロ）</strong>：
   いまや $d = x - u$ と $e = y - v$ は全員が知っている<strong>ただの定数（スカラー）</strong>である。ここで $x = u + d$ および $y = v + e$ を代入して、私たちが求めたい積 $x \cdot y$ を展開してみよう：
   $$\begin{aligned} x \cdot y &= (u + d)(v + e) \\ &= u \cdot v + d \cdot v + e \cdot u + d \cdot e \\ &= w + d \cdot v + e \cdot u + d \cdot e \pmod p \end{aligned}$$
   この最後の式をじっくり眺めてほしい。右辺に登場する未知の秘密は $w, v, u$ の3つだけであり、それらのシェア $[w], [v], [u]$ は全員が最初から手元に持っている。そしてそこに掛かっている $d$ と $e$ は、ステップ2ですでに公開された<strong>既知の定数</strong>である！
   つまり、右辺にはもはや「秘密×秘密」の掛け算が1つも残っておらず、すべて<strong>「シェアの足し算」「定数×シェアのスカラー倍」「定数 $d \cdot e$ の加算」という線形演算のみ</strong>になっているのだ！
   したがって、各パーティは誰とも通信することなく、手元で
   $$[x \cdot y] = [w] + d \cdot [v] + e \cdot [u] + d \cdot e \pmod p$$
   を計算するだけで、瞬時に積 $x \cdot y$ の正しいシェア $[x \cdot y]$ を得ることができる！

Beaverトリプルを使う方式では、オンライン乗算ごとにマスク差分を開示する設計がある。SPDZ系の一部は、認証付きシェア、検証可能な前処理、悪意ある参加者への検査などを備え、計算量的仮定のもとで不正多数派（少なくとも1者は正直）を許容する。Beaverトリプルだけでこの安全性が得られるわけではなく、性能も方式・実装・ネットワークに依存する。

2012年に発表された<strong>SPDZプロトコル</strong>は、BeaverトリプルとMAC付きシェアを組み合わせる悪意ある攻撃者向けの不正多数派MPC方式である。安全性には、正しい前処理、認証鍵の保護、プロトコル固有の検査と暗号学的仮定が必要であり、検出確率はパラメーターにも依存する。これは可用性や公平性を自動的に保証するものではない。

---

**耐障害数は攻撃者モデルに依存する**：古典的BGWは受動的（honest-but-curious）モデルでは $c<n/2$ を許容し、悪意ある参加者に対する情報理論的安全性では、適切な通信仮定のもと通常 $c<n/3$ が必要となる。Beaverトリプル単独では耐障害数は決まらず、能動的安全性も保証しない。

## 5. 第2の数学的エンジン：紛失通信（OT）とヤオのガーブルド・サーキット

ここまで見てきた「有限体 $\mathbb{F}_p$ 上の秘密分散（算術回路）」は、平均・分散・内積・行列積・多項式評価といった<strong>数値計算</strong>には無類の強さを発揮する。
しかし、第1節で登場した「ヤオの億万長者問題（$x > y$ の大小比較）」や、SHA-256・AES のようなビット演算、あるいは `if (x > y) then ...` のような条件分岐を有限体 $\mathbb{F}_p$ の足し算と掛け算だけで表現しようとすると、数値を一度ビット分解する必要があり、回路の深さ（通信ラウンド数）が大きく増えてしまう。

そこで、あらゆる計算を<strong>ブール論理回路（AND ゲート、XOR ゲート、OR ゲート）</strong>として表現する別の潮流として、紛失通信（Oblivious Transfer: OT）を使う<strong>1-out-of-2 OT</strong>と、アンドリュー・ヤオの<strong>ガーブルド・サーキット（Garbled Circuits）</strong>がある。ガーブルド・サーキットの通信ラウンド数はゲート数・回路の深さと独立にできる構成があるが、実際の往復回数や通信量はプロトコルとOTの実装に依存する。

### 5.1 1-out-of-2 紛失通信（$\text{OT}_1^2$）

マイケル・ラビンは1981年に、受信者が確率1/2でメッセージを受け取り、その成否を送信者に知られないOT方式を提案した。これとは異なる「1-out-of-2 OT」はEven、Goldreich、Lempelが1985年に定式化した。以下ではこの1-out-of-2 OTの機能を説明する。実際の構成は暗号学的仮定に依存する計算量的安全性を持つことが多く、文字どおり情報が1ビットも漏れないという意味ではない。

* <strong>$\text{OT}_1^2$ の仕様</strong>：
  * 送信者（Sender）アリスは、2つの秘密メッセージ $m_0, m_1$ を持っている。
  * 受信者（Receiver）ボブは、1ビットの選択値 $b \in \{0, 1\}$ を持っている。
  * プロトコルが終了したとき、以下の2つの条件が同時に満たされる：
    1. <strong>送信者のプライバシー（Sender's Privacy）</strong>：ボブは自分が選んだメッセージ $m_b$ を取得し、選ばなかった $m_{1-b}$ について、採用した安全性定義の範囲で許容されない情報を得ない。
    2. <strong>受信者のプライバシー（Receiver's Privacy）</strong>：アリスの視点から、ボブの選択ビット $b$ が0か1かを安全性定義の範囲で区別できない。

日常の感覚からすると魔法のような通信箱である。「郵便局員（アリス）が2通の手紙を入れて差し出し、受取人（ボブ）は片方だけを取り出して読むが、郵便局員にはどちらの手紙が抜かれたか分からず、受取人ももう片方の手紙を絶対に盗み見ることができない」という仕組みを、物理的な箱を使わずに公開鍵暗号の数式だけでどう実現するのだろうか？

ここでは、Diffie–Hellman と ElGamal 型暗号を使う<strong>Bellare–Micali 方式の教育用スケッチ</strong>を見てみよう。

<strong>【離散対数問題に基づく $\text{OT}_1^2$ プロトコル】</strong>
離散対数問題が困難な素数位数 $q$ の巡回群 $\mathbb{G}$ とその生成元 $g$ を共有しておく。

1. <strong>アリスからのランダムチャレンジ</strong>：
   アリスはランダムな群要素 $C \xleftarrow{\$} \mathbb{G}$ をボブに送る。安全性のため、適切な hash-to-group を使って生成し、アリスもボブも $\log_g C$ を知る trapdoor を持たないようにする必要がある。アリスが既知の指数で $C$ を作る方法は、この要件を満たさない。
2. <strong>ボブによる「片方だけ秘密鍵を知っている2つの公開鍵」の生成</strong>：
   ボブは乱数（秘密鍵） $k \xleftarrow{\$} \mathbb{Z}_q$ を1つ選び、自分の選択ビット $b \in \{0, 1\}$ に応じて、2つの公開鍵 $(PK_0, PK_1)$ を次のようにセットする：
   * もしボブが <strong>$b = 0$</strong> を選びたいなら：
     $$PK_0 = g^k, \qquad PK_1 = \frac{C}{g^k}$$
   * もしボブが <strong>$b = 1$</strong> を選びたいなら：
     $$PK_0 = \frac{C}{g^k}, \qquad PK_1 = g^k$$
   そしてボブは、自分では $PK_0$ だけ（$PK_1$ は常に $C / PK_0$ から自動で決まるため）をアリスに送る。
   ここがこのプロトコルの白眉である！
   * <strong>なぜアリスに選択ビット $b$ がバレないのか？</strong>：$k$ は一様乱数なので、$b=0$ のときの $PK_0 = g^k$ も、$b=1$ のときの $PK_0 = C / g^k$ も、群 $\mathbb{G}$ 上の<strong>完全に一様なランダム要素</strong>である。つまり、アリスから見れば $PK_0$ と $PK_1$ は単に $PK_0 \cdot PK_1 = C$ を満たす無作為なペアにしか見えず、ボブがどちらの離散対数（秘密鍵 $k$）を知っているのかは、情報理論的に<strong>1ビットも区別できない</strong>！
   * <strong>なぜボブが両方のメッセージを得ることは困難なのか？</strong>：両公開鍵の離散対数を知れば、$PK_0 \cdot PK_1=C$ から $\log_g C$ も求められる。安全性はチャレンジ生成法と離散対数・Diffie–Hellman等の計算量的仮定に依存するため、無条件の保証ではない。
3. <strong>アリスによる二重暗号化とボブの復号</strong>：
   アリスは受け取った $PK_0$ と $PK_1 = C / PK_0$ を使い、乱数 $r_0, r_1 \xleftarrow{\$} \mathbb{Z}_q$ と鍵導出ハッシュ $H$ で $E_i = (g^{r_i},\, m_i \oplus H(PK_i^{r_i}))$ を作って送る。これは説明用の hashed-ElGamal 型表記であり、実装では適切なKDFと暗号化方式が必要である。
   ボブは自分が秘密指数 $k$ を知る側の暗号文 $E_b$ を $PK_b^{r_b} = (g^{r_b})^k$ から復号できる。反対側の鍵共有値を効率的に求められないことは、適切な群・ハッシュモデルと計算量的Diffie–Hellman等の仮定に依存する。これは説明用のスケッチで、実用プロトコルの安全性証明や実装指針の代わりにはならない。

1988年、ジョー・キリアン（Joe Kilian）は暗号理論の歴史に残る大定理を証明した。それは<strong>「紛失通信（OT）というブラックボックスが1つあるだけで、他のいかなる暗号学的仮定も一切使わずに、任意の関数に対する安全なマルチパーティ計算（MPC）を構成できる（OT is complete for MPC）」</strong>という事実である。

---

### 5.2 ヤオのガーブルド・サーキット（Yao's Garbled Circuits）の完全解剖

では、この紛失通信（$\text{OT}_1^2$）を部品として使い、アンドリュー・ヤオの<strong>ガーブルド・サーキット（Garbled Circuits）</strong>がどのようにブール回路の秘密計算を実現するかを見ていこう。通信ラウンド数や往復回数は具体的なプロトコル構成に依存する。

```mermaid
flowchart TD
    subgraph Step1["1. アリス (Garbler): 回路の暗号化"]
        W["各ワイヤ w_i に0用と1用のランダム鍵ペア (k_i^0, k_i^1) を生成"] --> G["各ゲート(AND等)の真理値表4行を二重暗号化: Enc(k_a^α, k_b^β, k_c^g(α,β))"]
        G --> P["4つの暗号文の行順序をランダムにシャッフル (Garbled Table)"]
    end

    subgraph Step2["2. 鍵の受け渡し (OT_1^2 の活躍)"]
        P -->|"Garbled Tables と アリスの入力鍵 k_a^x を送信"| Eval["ボブ (Evaluator)"]
        BobIn["ボブの秘密入力ビット y ∈ {0,1}"] --> OT["1-out-of-2 紛失通信 (OT_1^2)"]
        W -->|"候補鍵ペア (k_b^0, k_b^1)"| OT
        OT -->|"アリスに y を秘匿したまま k_b^y のみ取得"| Eval
    end

    subgraph Step3["3. ボブ (Evaluator): 回路の一方向評価"]
        Eval --> Dec["手元の鍵ペア (k_a^x, k_b^y) で4行中1行だけを復号し出力鍵 k_c^z を取得"]
        Dec --> Out["最終出力ワイヤの鍵から計算結果 z = f(x,y) のみを判明させる"]
    end
```

いま、アリス（入力 $x$）とボブ（入力 $y$）がある論理ゲート——たとえば1ビットの <strong>AND ゲート $z = x \land y$</strong>——を計算したいとする（一般の複雑な関数も、このゲートを多数つなぎ合わせた有向非巡回グラフ（DAG）に過ぎない）。

#### ステップ1：各ワイヤへのランダムな暗号鍵ペア（ラベル）の割り当て
回路作成者（Garbler）であるアリスは、回路内のすべての電線（入力ワイヤ $w_a, w_b$ と出力ワイヤ $w_c$）に対して、それぞれ<strong>真理値 `0` を表す128ビットのランダムなAES暗号鍵 $k_i^0$</strong> と、<strong>真理値 `1` を表す128ビットのランダムなAES暗号鍵 $k_i^1$</strong> を生成する：
* 入力ワイヤ $w_a$（アリス用）：$(k_a^0,\, k_a^1) \xleftarrow{\$} \{0, 1\}^{128} \times \{0, 1\}^{128}$
* 入力ワイヤ $w_b$（ボブ用）：$(k_b^0,\, k_b^1) \xleftarrow{\$} \{0, 1\}^{128} \times \{0, 1\}^{128}$
* 出力ワイヤ $w_c$（結果用）：$(k_c^0,\, k_c^1) \xleftarrow{\$} \{0, 1\}^{128} \times \{0, 1\}^{128}$

ここで重要なのは、鍵 $k_i^0$ や $k_i^1$ が一様に生成された鍵ラベルであり、適切なガーブル方式と暗号学的仮定のもとでは、ラベル単体から対応するビットを効率的に判別できないよう設計される点である。

#### ステップ2：真理値表の二重暗号化と行のランダムシャッフル（Garbling）
通常の AND ゲートの真理値表は、$(\alpha, \beta) \in \{(0,0), (0,1), (1,0), (1,1)\}$ に対して出力 $\gamma = \alpha \land \beta \in \{0, 0, 0, 1\}$ を対応させる表である。
アリスはこの真理値表の `0` と `1` をすべて対応する暗号鍵ラベル $k_i^\alpha$ に置き換え、さらに各行の出力鍵 $k_c^{\alpha \land \beta}$ を、その行の2つの入力鍵 $k_a^\alpha$ と $k_b^\beta$ の<strong>両方が揃わなければ復号できないように二重暗号化（Double Encryption）</strong>する：

| 元の入力 $(\alpha, \beta)$ | 元の出力 $\alpha \land \beta$ | 二重暗号化された出力鍵（シャッフル前） |
| :---: | :---: | :--- |
| $(0, 0)$ | $0$ | $c_{0,0} = \text{Enc}_{k_a^0, k_b^0}\left(k_c^0\right)$ |
| $(0, 1)$ | $0$ | $c_{0,1} = \text{Enc}_{k_a^0, k_b^1}\left(k_c^0\right)$ |
| $(1, 0)$ | $0$ | $c_{1,0} = \text{Enc}_{k_a^1, k_b^0}\left(k_c^0\right)$ |
| $(1, 1)$ | $1$ | $c_{1,1} = \text{Enc}_{k_a^1, k_b^1}\left(k_c^1\right)$ |

もしこの4つの暗号文 $(c_{0,0}, c_{0,1}, c_{1,0}, c_{1,1})$ をこの順番のままボブに渡してしまうと、ボブが「3番目の暗号文が復号できた！」と分かった瞬間に、「上から3番目だから入力は $(1, 0)$ だったのだな」とバレてしまう。
そこでアリスは、<strong>この4つの暗号文の行の順番をランダムな置換 $\pi$ でシャッフル（並べ替え）した表（Garbled Table）</strong>を作り、ボブに送信する！

#### ステップ3：入力ワイヤの鍵の受け渡し（ここで $\text{OT}_1^2$ が決定的な役割を果たす！）
ボブがこのゲートを評価するためには、アリスの実際の入力ビット $x \in \{0, 1\}$ に対応する鍵 $k_a^x$ と、ボブ自身の入力ビット $y \in \{0, 1\}$ に対応する鍵 $k_b^y$ の2つ（各ワイヤにつき片方の鍵だけ）を手に入れる必要がある。

1. <strong>アリスの入力鍵 $k_a^x$ の送信</strong>：
   アリスは自分の入力ビット $x$ を知っているので、2つの鍵 $(k_a^0, k_a^1)$ のうち、実際の入力に対応する片方の鍵 $k_a^x$ だけをそのままボブに送る。先ほど述べた通り、$k_a^x$ はただの128ビットの乱数文字列なので、ボブはそれを受け取っても $x=0$ なのか $x=1$ なのかまったく分からない！
2. <strong>ボブの入力鍵 $k_b^y$ の取得（1-out-of-2 紛失通信 $\text{OT}_1^2$）</strong>：
   では、ボブの入力ワイヤの鍵 $k_b^y$ はどうやって渡せばよいだろうか？
   どちらの鍵 $(k_b^0, k_b^1)$ が `0` でどちらが `1` かを知っているのは、鍵を生成したアリスだけである。しかし、ボブがアリスに「私の入力は $y=1$ だから $k_b^1$ をちょうだい」と言ってしまえば、アリスにボブの秘密 $y$ がバレてしまう。かといって、アリスがボブに $k_b^0$ と $k_b^1$ の<strong>両方</strong>を渡してしまえば、ボブは $y=0$ のときと $y=1$ のときの両方の出力を計算できてしまい、そこからアリスの秘密 $x$ を逆算できてしまう！
   まさにこのジレンマを解決するために、第5.1節の<strong>1-out-of-2 紛失通信（$\text{OT}_1^2$）</strong>を使うのである！アリスが2つの鍵 $(m_0 = k_b^0,\, m_1 = k_b^1)$ を送信者としてセットし、ボブが自分の入力ビット $b = y \in \{0, 1\}$ を選択ビットとして $\text{OT}_1^2$ を実行する。すると、<strong>アリスにはボブの入力 $y$ が1ビットも知られることなく、ボブは自分の入力に対応する片方の鍵 $k_b^y$ だけを受け取ることができる</strong>！

#### ステップ4：ボブによるブラインド評価（Garbled Evaluation）
いま、評価者（Evaluator）であるボブの手元には、シャッフルされた4つの暗号文の表（Garbled Table）と、2つの鍵 $(k_a^x,\, k_b^y)$ が揃った。
ボブはこの鍵ペア $(k_a^x, k_b^y)$ を使って、表の4つの暗号文を復号してみる。他の3つの行は異なる鍵で暗号化されているため復号に失敗（あるいは認証タグが不一致）し、<strong>まさに $(x, y)$ に対応するただ1つの行だけが正しく復号されて、出力ワイヤの鍵 $k_c^{x \land y}$ が飛び出してくる</strong>！

複数のゲートが連なる大きな回路（たとえば億万長者問題の64ビット比較回路）であっても、ボブは得られた出力鍵 $k_c^{x \land y}$ をそのまま次のゲートの入力鍵として使い、誰とも通信することなく自分の手元のコンピュータだけで入力層から最終出力層まで一気に復号を連鎖させていくことができる。途中の何千本ものワイヤの鍵が `0` を表していたのか `1` を表していたのかは、ボブにも一切分からない（目隠しをしたまま迷路の鍵を次々と開けて進むような状態である）。
そして最後の出力ワイヤの鍵 $k_{\text{out}}^z$ に到達したときだけ、アリスがあらかじめ添付しておいた「最終出力ワイヤの翻訳表（$H(k_{\text{out}}^0) \to 0,\; H(k_{\text{out}}^1) \to 1$）」と照合することで、最終結果 $z = f(x, y) \in \{0, 1\}$ だけが初めて平文として浮かび上がるのである！

---

### 5.3 ガーブルド・サーキットの効率を高めた3つの最適化

ガーブルド・サーキットには、回路サイズを小さくし計算・通信を減らす最適化が提案されてきた。ここでは代表的なPoint-and-Permute、Free-XOR、Half-Gatesを紹介する。実測性能は回路、プロトコル、実装、ハードウェア、ネットワーク条件によって変わり、単一の処理速度を一般化できない。

1. <strong>Point-and-Permute（Beaver, Micali, Rogaway 1990）：4回の試験復号を1回に削減</strong>
   素朴な構成では、ボブは4行の暗号文のうちどれが自分の鍵に対応する行か分からないため、平均2.5回（最悪4回）復号を試みる必要があり、しかも「どの行が正しく復号できたか」を判定するために平文に冗長なゼロビット列（パディング）を付加する必要があった。
   <strong>Point-and-Permute</strong> では、各ワイヤ $w_i$ の2つの鍵 $k_i^0, k_i^1$ の最下位ビット（これを<strong>選択ビット / カラービット $p_i$</strong> と呼ぶ）に、ランダムなビット $\pi_i \in \{0, 1\}$ とその反転 $\pi_i \oplus 1$ を割り当てる（$\pi_i$ が乱数なので、最下位ビットを見ても本当の真理値が $0$ か $1$ かはまったく分からない）。そしてアリスは、真理値表の4行を「本当の真理値 $(\alpha, \beta)$」ではなく<strong>「2つの鍵の最下位ビットの組 $(p_a, p_b) \in \{0,1\}^2$」の辞書順に並べて配置する</strong>。
   Point-and-Permute方式では、入力ラベルの選択ビットを使って評価する行を選べる。復号・ハッシュの回数や行形式はガーブル方式と最適化に依存し、すべてのゲートで同じ1回の暗号処理になるとは限らない。
2. <strong>Free-XOR（Kolesnikov & Schneider 2008）：XORゲート用の暗号文送信を省く最適化</strong>
    ウラジミール・コレスニコフとトーマス・シュナイダーが提案した <strong>Free-XOR</strong> は、ガーブルド・サーキットの通信量を減らす代表的な最適化である。
   アリスは回路全体でただ1つのグローバルな秘密乱数オフセット $\Delta \xleftarrow{\$} \{0, 1\}^{127} \parallel 1$ を選び、回路内のすべてのワイヤ $w_i$ において、`0` 用の鍵 $k_i^0$ だけをランダムに選んだら、`1` 用の鍵 $k_i^1$ は必ず
   $$k_i^1 = k_i^0 \oplus \Delta$$
   という関係式で定義する（すなわち、任意の真理値 $\alpha \in \{0, 1\}$ に対して $k_i^\alpha = k_i^0 \oplus \alpha \Delta$ と書ける）。
   このとき、入力ワイヤ $w_a, w_b$ から出力ワイヤ $w_c$ への <strong>XOR ゲート（$\gamma = \alpha \oplus \beta$）</strong>を考えよう。アリスが出力ワイヤの `0` 用鍵を $k_c^0 = k_a^0 \oplus k_b^0$ と定義すると、ボブが手元の2つの入力鍵 $k_a^\alpha$ と $k_b^\beta$ のビット排他的論理和（XOR）を計算したとき、なんと次の恒等式が成り立つ：
   $$\begin{aligned} k_a^\alpha \oplus k_b^\beta &= \left(k_a^0 \oplus \alpha \Delta\right) \oplus \left(k_b^0 \oplus \beta \Delta\right) \\ &= \left(k_a^0 \oplus k_b^0\right) \oplus (\alpha \oplus \beta)\Delta \\ &= k_c^0 \oplus (\alpha \oplus \beta)\Delta = k_c^{\alpha \oplus \beta} \end{aligned}$$
   この構成では、ボブは入力ラベルを XOR して正しい出力ラベルを得られる。XORゲート用のガーブル暗号文を送らずに済むが、ラベルのXOR演算自体を含む計算コストがゼロになるわけではない。
3. <strong>Half-Gates（Zahur, Rosulek, Evans 2015）：AND ゲートの暗号文を4個から2個へ半減</strong>
   Free-XOR によって XOR ゲートが無料になったため、残るコストは非線形な AND ゲートだけとなった。サミール・ザフールらは、一般の AND ゲート $\alpha \land \beta$ を、カラービット $r$ を用いて
   $$\alpha \land \beta = (\alpha \land r) \oplus \left(\alpha \land (\beta \oplus r)\right)$$
   という2つの「片方の入力をアリスまたはボブがすでに知っている特殊な AND ゲート（ハーフゲート）」の XOR 結合に分解した。ハーフゲートはそれぞれ暗号文1個だけで表現でき、最後の結合は Free-XOR で無料になるため、<strong>AND ゲート1個あたりの暗号文数は4個からわずか2個（128ビット×2 = 32バイト）</strong>にまで圧縮され、かつこの「2個」が線形ガーブリングにおける数学的な下界（これ以上減らせない限界）であることも同時に証明された。

---

## 6. Pythonによる完全実装：有限体 $\mathbb{F}_p$ 上のシャミア秘密分散・ラグランジュ補間・Beaver乗算トリプル

理論の美しさを実際に手で触って確かめるために、有限体 $\mathbb{F}_p$（ここでは61ビットのメルセンヌ素数 $p = 2^{61} - 1$ を使用）の上で動作する<strong>シャミアの $(t, n)$ 閾値秘密分散法、ラグランジュ補間による秘密復元、BGW方式の通信ゼロ加算、そしてビーバーの乗算トリプルを用いた秘密の乗算と分散（Variance）計算</strong>をフルスクラッチのPythonコードで実装してみよう。

この例では各年収の二乗も新しいBeaverトリプルで秘密計算し、合計と二乗和を復元して平均と母分散を求める。復元した統計量は復元者に開示される。コード全体は1プロセス内の教材用シミュレーションであり、分散したサーバー間の通信を実装していない。

```python
import secrets
from typing import List, Tuple

# 61-bit Mersenne prime p = 2^61 - 1 for our prime finite field F_p
PRIME = (1 << 61) - 1

def mod_inv(a: int, p: int = PRIME) -> int:
    # Modular inverse in F_p via Extended Euclidean Algorithm (Python 3.8+ pow(a, -1, p))
    return pow(a % p, -1, p)

def shamir_share(secret: int, t: int, n: int, p: int = PRIME) -> List[Tuple[int, int]]:
    # Shamir's (t, n) Threshold Secret Sharing:
    # Samples a random degree-(t-1) polynomial P(x) with P(0) = secret and evaluates it at x = 1..n.
    assert 1 <= t <= n < p, "Threshold t and party count n must satisfy 1 <= t <= n < p"
    # P(x) = s + a_1 * x + a_2 * x^2 + ... + a_{t-1} * x^{t-1} (mod p)
    coeffs = [secret % p] + [secrets.randbelow(p) for _ in range(t - 1)]

    shares = []
    for i in range(1, n + 1):
        # Evaluate P(i) using Horner's method
        y = 0
        for c in reversed(coeffs):
            y = (y * i + c) % p
        shares.append((i, y))
    return shares

def lagrange_reconstruct(shares: List[Tuple[int, int]], p: int = PRIME) -> int:
    # Reconstructs P(0) = s from any subset of >= t shares using Lagrange Polynomial Interpolation:
    # s = sum_{i in T} y_i * prod_{j in T, j != i} (-x_j) / (x_i - x_j) (mod p)
    secret = 0
    k = len(shares)
    for i in range(k):
        xi, yi = shares[i]
        num = 1
        den = 1
        for j in range(k):
            if i == j:
                continue
            xj, _ = shares[j]
            num = (num * (-xj)) % p
            den = (den * (xi - xj)) % p
        lambda_i = (num * mod_inv(den, p)) % p
        secret = (secret + yi * lambda_i) % p
    return secret

def mpc_add(shares_a: List[Tuple[int, int]], shares_b: List[Tuple[int, int]], p: int = PRIME) -> List[Tuple[int, int]]:
    # Local homomorphic addition [a] + [b] = [a + b] (Zero communication)
    return [(xa, (ya + yb) % p) for (xa, ya), (xb, yb) in zip(shares_a, shares_b)]

def mpc_sub(shares_a: List[Tuple[int, int]], shares_b: List[Tuple[int, int]], p: int = PRIME) -> List[Tuple[int, int]]:
    # Local homomorphic subtraction [a] - [b] = [a - b] (Zero communication)
    return [(xa, (ya - yb) % p) for (xa, ya), (xb, yb) in zip(shares_a, shares_b)]

def mpc_scalar_mul(scalar: int, shares_a: List[Tuple[int, int]], p: int = PRIME) -> List[Tuple[int, int]]:
    # Local multiplication by a public scalar c * [a] = [c * a] (Zero communication)
    return [(xa, (scalar * ya) % p) for xa, ya in shares_a]

def mpc_add_constant(const: int, shares_a: List[Tuple[int, int]], p: int = PRIME) -> List[Tuple[int, int]]:
    # Adding a public constant [a] + c = [a + c] shifts P(x) by +c at every evaluation point
    return [(xa, (ya + const) % p) for xa, ya in shares_a]

def generate_beaver_triple(t: int, n: int, p: int = PRIME):
    # Offline Preprocessing Phase: Generates a shared random multiplication triple ([u], [v], [w = u * v])
    u = secrets.randbelow(p)
    v = secrets.randbelow(p)
    w = (u * v) % p
    return shamir_share(u, t, n, p), shamir_share(v, t, n, p), shamir_share(w, t, n, p)

def mpc_beaver_mul(
    shares_x: List[Tuple[int, int]],
    shares_y: List[Tuple[int, int]],
    triple: Tuple[List[Tuple[int, int]], List[Tuple[int, int]], List[Tuple[int, int]]],
    t: int,
    p: int = PRIME
) -> List[Tuple[int, int]]:
    # Online Phase: Evaluates [x * y] using a Beaver Multiplication Triple ([u], [v], [w]):
    # 1. Locally compute [d] = [x] - [u] and [e] = [y] - [v]
    # 2. Open masked differences; security depends on fresh, valid, single-use triples and the threat model
    # 3. Locally compute the linear combination [x * y] = [w] + d * [v] + e * [u] + d * e
    shares_u, shares_v, shares_w = triple
    shares_d = mpc_sub(shares_x, shares_u, p)
    shares_e = mpc_sub(shares_y, shares_v, p)

    # Open the masked differences d = x - u and e = y - v using t shares
    d = lagrange_reconstruct(shares_d[:t], p)
    e = lagrange_reconstruct(shares_e[:t], p)

    # Linear combination to obtain degree-(t-1) shares of [x * y]
    term1 = shares_w
    term2 = mpc_scalar_mul(d, shares_v, p)
    term3 = mpc_scalar_mul(e, shares_u, p)
    res = mpc_add(mpc_add(term1, term2, p), term3, p)
    res = mpc_add_constant((d * e) % p, res, p)
    return res

if __name__ == "__main__":
    # 5 MPC servers (n = 5) with reconstruction threshold t = 3 (any 2 servers learn 0 bits)
    t, n = 3, 5
    salaries = [850, 920, 780]  # Example salary units

    # Each engineer splits their secret salary across the 5 servers
    shared_salaries = [shamir_share(s, t, n) for s in salaries]

    # 1. Compute the sum of salaries locally with zero inter-server communication
    sum_shares = shared_salaries[0]
    for s_share in shared_salaries[1:]:
        sum_shares = mpc_add(sum_shares, s_share)

    # Reconstruct the total from any 3 servers (e.g., servers 1, 3, and 5)
    subset_3 = [sum_shares[0], sum_shares[2], sum_shares[4]]
    total_salary = lagrange_reconstruct(subset_3)
    mean_salary = total_salary / len(salaries)
    print(f"Reconstructed total (units): {total_salary:,} (mean: {mean_salary:,.2f})")

    # 2. Compute the sum of squares S_2 = x_A^2 + x_B^2 + x_C^2 using Beaver Multiplication Triples
    sq_sum_shares = shamir_share(0, t, n)
    for s_share in shared_salaries:
        triple = generate_beaver_triple(t, n)
        sq_share = mpc_beaver_mul(s_share, s_share, triple, t)
        sq_sum_shares = mpc_add(sq_sum_shares, sq_share)

    total_sq = lagrange_reconstruct(sq_sum_shares[:t])
    variance = (total_sq / len(salaries)) - (mean_salary ** 2)
    print(f"Reconstructed sum of squares: {total_sq:,} (population variance: {variance:,.2f})")
```

このコードを実行すると、`復元された合計年収: 2550 万円 (平均: 850.0 万円)` および `復元された二乗和: 2177300 -> 年収の分散: 3266.67` が1ビットの誤差もなく出力される。しかも計算の途中、どのサーバーも $850, 920, 780$ という個人の年収はおろか、その二乗値 $850^2 = 722500$ すら一切知ることなく、ランダムな数値の断片だけを処理して最終的な統計量（平均と分散）だけを導き出しているのである。

---

## 7. プライバシー強化技術（PETs）4大アプローチの徹底比較：MPC vs. 完全準同型暗号（FHE） vs. ゼロ知識証明（ZKP） vs. TEE

今日、<strong>プライバシー強化技術（Privacy-Enhancing Technologies: PETs）</strong>という大きな枠組みの中で、秘密計算（MPC）と並んで頻繁に言及される技術に、<strong>完全準同型暗号（Fully Homomorphic Encryption: FHE）</strong>、<strong>ゼロ知識証明（Zero-Knowledge Proofs: ZKP）</strong>、そして<strong>信頼実行環境（Trusted Execution Environment: TEE）</strong>がある。これらはしばしば混同されるが、数学的な目的も、ボトルネックの所在も、信頼の前提もまったく異なる。

| 比較項目 | 秘密計算 (MPC) | 完全準同型暗号 (FHE) | ゼロ知識証明 (ZKP) | ハードウェア安全領域 (TEE) |
| :--- | :--- | :--- | :--- | :--- |
| <strong>解決する核心問題</strong> | <strong>複数の主体が持つ別々の秘密入力 $x_1, \dots, x_n$</strong> から、互いの入力を明かさずに関数 $f(x_1, \dots, x_n)$ を共同計算する。 | <strong>暗号文 $\text{Enc}(x)$ のまま</strong>、秘密鍵を持たない単一のサーバー（クラウド等）が任意の計算を行い $\text{Enc}(f(x))$ を得る。 | <strong>1人の証明者がすでに知っている秘密 $w$</strong> について、$w$ を一切明かさずに「$f(x, w) = 1$ が正しいこと」だけを他者に証明する。 | CPU内部の隔離メモリ空間（Enclave）に暗号化データを送り、<strong>ハードウェアの内部でだけ平文に戻して</strong>高速計算する。 |
| <strong>代表的なアルゴリズム</strong> | Shamir秘密分散 (BGW), SPDZ, Yao's Garbled Circuits, GMW | Gentry (2009), BGV / BFV, CKKS (近似実数), TFHE (論理ゲート) | Groth16, PlonK, Halo2 (zk-SNARKs), zk-STARKs | Intel SGX / TDX, AMD SEV-SNP, ARM TrustZone, AWS Nitro |
| <strong>計算負荷（CPU／メモリ）</strong> | <strong>方式・回路・脅威モデルに依存</strong><br>線形演算は軽い場合があるが、乗算や比較は通信・計算を要する。 | <strong>一般に高負荷になり得る</strong><br>暗号方式、回路、精度、パラメーターで大きく変わる。 | 証明系・命題により異なる。生成と検証のコストは別々に測る。 | 速度・安全メモリーは環境とワークロードに依存。 |
| <strong>通信負荷（ネットワーク）</strong> | <strong>方式により異なる</strong><br>ラウンド数・通信量は演算、前処理、ネットワーク条件で変わる。 | <strong>暗号文は大きくなり得る</strong><br>対話回数と転送量は方式・処理で異なる。 | <strong>証明と公開入力を送信</strong><br>非対話方式でも証明サイズや設定データは方式依存。 | <strong>通常の通信に加えアテステーション等</strong><br>構成とデータ転送量に依存。 |
| <strong>信頼モデルと弱点</strong> | <strong>結託閾値と攻撃者モデル</strong><br>出力自体からの漏えい、可用性、公平性は別途検討する。 | <strong>暗号学的仮定と鍵管理</strong><br>正しい計算の検証や復号結果からの漏えい防止は別途必要。 | <strong>命題・証明方式への依存</strong><br>公開出力の秘匿や複数人の入力統合を単独では解決しない。 | <strong>ハードウェア・実装・運用への信頼</strong><br>サイドチャネル、ファームウェア、アテステーション等のリスクがある。 |

```mermaid
flowchart TD
    Start["守りたい計算・証明の課題は何か？"] --> Q1{"秘密の入力データは誰が持っているか？"}
    Q1 -->|"1人の証明者がすでに秘密 w をすべて持っており、計算の正当性だけを他人に納得させたい"| ZKP["ゼロ知識証明 (ZKP: zk-SNARKs / STARKs)"]
    Q1 -->|"複数の組織・個人が別々の秘密 x1, ..., xn を持っており、誰も全体を見ずに結合計算したい"| Q2{"ハードウェアメーカー(Intel/AMD)と物理耐タンパー性を信頼できるか？"}
    Q2 -->|"はい (サイドチャネル攻撃リスクよりネイティブ速度を最優先)"| TEE["ハードウェア安全領域 (TEE: Intel SGX / TDX, AMD SEV)"]
    Q2 -->|"いいえ (純粋な数学・暗号理論のみで安全性を保証したい)"| Q3{"計算サーバー間の高速ネットワーク通信が可能か？"}
    Q3 -->|"はい (通信条件と方式を評価したうえで、複数参加者間の共同計算を行いたい)"| MPC["秘密計算 (MPC: Shamir秘密分散 / SPDZ / Garbled Circuits)"]
    Q3 -->|"いいえ (クライアントが暗号文を1回投げてクラウド1台に計算させたい)"| FHE["完全準同型暗号 (FHE: CKKS / TFHE)"]
```

### 7.1 なぜ「MPC × FHE × ZKP」は対立するのではなく融合するのか？

現代の暗号システムにおいて、これら4つは決して排他的なライバルではなく、<strong>互いの弱点を補い合う強力な共生関係</strong>にある。

1. <strong>MPC の内部で FHE を使う（SPDZ / Overdrive）</strong>：
   SPDZ系プロトコルの一部は、オンライン計算用のBeaverトリプルを前処理段階で生成する。前処理には準同型暗号やOTなど複数の方式があり、すべてのSPDZ系で同じ構成を使うわけではない。オンライン性能は演算・実装・通信環境によって変わる。
2. <strong>MPC の内部で ZKP を使う（マリシャス安全性の達成）</strong>：
   参加者が嘘をつくマリシャス（Active）モデルにおいて、「自分がプロトコル通りに正しい乱数と入力を使って暗号文を作ったこと」を他のパーティに証明するために、<strong>ゼロ知識証明（ZKP）</strong>が組み込まれる。逆に、ZKP の証明サイズを極限まで小さくする<strong>「MPC-in-the-Head（頭の中の秘密計算：IKOS 2007 / ZKBoo / Picnic）」</strong>という驚くべき手法もある。これは、1人の証明者が自分の頭（メモリ）の中で仮想的な $n$ 人のパーティによるMPCをシミュレートしてコミットし、検証者がランダムに選んだ $n-1$ 人の通信ログ（View）を開示させることで、MPCのプライバシー性質をそのままゼロ知識証明に変換してしまうというエレガントな双対理論である。

---

## 8. 社会を変えたMPCの実世界応用：デンマークのテンサイ市場オークションから医療ゲノム解析・暗号資産ウォレットまで

秘密計算（MPC）は理論研究にとどまらず、オークション、賃金統計、パスワード照合、ゲノム解析、閾値署名などで実験・研究・製品利用されています。以下は方式や成熟度の異なる事例です。実運用の存在は、あらゆる攻撃や出力からの推測を防ぐ保証ではありません。

### 8.1 2008年：デンマークのテンサイ（砂糖大根）生産枠ダブルオークション（初期の大規模実運用例）

MPCが研究室を飛び出して現実の経済活動に使われた歴史的転換点は、2008年1月にデンマークで実施された<strong>テンサイ（Sugar Beet）生産枠の電子ダブルオークション</strong>である。
当時、EUの砂糖市場改革に伴い、デンマークの1,200軒以上のテンサイ農家と、国内唯一の製糖企業である Danisco 社の間で、数万トン規模の生産権（契約枠）を再配分する必要が生じた。経済学的に最も公平かつ効率的な価格決定方法は、各農家が「価格 $p$ なら何トン売りたいか／買いたいか」という<strong>供給・需要曲線（入札リスト）</strong>をすべて提出し、総需要と総供給が一致する<strong>市場清算価格（Market Clearing Price）</strong>を算出するダブルオークションである。

入札価格ごとの数量を含むデータは農場の経営状態や生産コストに関わるため、単一の運営者へ生データを渡すことへの懸念があった。外部の仲介者に委託する案にもコストや信頼上の課題があり、複数の関係者で計算する設計が検討された。

そこでオーフス大学（Aarhus University）の暗号学者ピーター・ボゲトフト（Peter Bogetoft）やアイヴァン・ダムゴードらのチームは、<strong>シャミアの秘密分散と比較回路を組み合わせた3サーバーMPCシステム</strong>を構築した。
1. 報告されたシステムでは、農家が入札データをシャミア秘密分散でシェアに分け、<strong>① Danisco 社、② 農家組合（DKS）、③ オーフス大学</strong>が運用する3サーバーへ送った。機密性はサーバーの分離と想定する結託モデルに依存し、3者が結託しないことを暗号技術が保証するわけではない。
2. 3台のサーバーは、どの農家がいくらで入札したかを1ビットも復元することなく、秘密分散のまま全農家の需要合計と供給合計を比較し、二分探索によって市場清算価格と各農家の落札量だけを計算した。
3. 論文によると、2008年1月14日の計算は約30分かかり、約25,000トンの生産権が移転した。これは大規模で実用的なMPC利用の初期事例として報告されている。参加者が想定した結託モデルや、公開される市場結果から推測できる情報まで消えるわけではない。

### 8.2 ボストン市（BWWC）における企業横断の男女間・人種間賃金格差調査

アメリカの <strong>Boston Women's Workforce Council (BWWC)</strong> とボストン大学の取り組みは、企業間の賃金格差統計にMPCを利用する事例である。BWWCは雇用主からデータを集め、賃金格差を隔年で公表している。
市全体の「男女間および人種間の賃金格差（Gender/Racial Wage Gap）」を正確に把握するには、都市圏の多数の民間企業から、役職・勤続年数・性別・人種ごとの詳細な給与支払データを集めて集計する必要がある。しかし、どの企業も自社の詳細な給与テーブルを競合他社や行政機関に提出することは、営業秘密の漏洩や訴訟リスクの観点から絶対に受け入れられなかった。

同プロジェクトは給与データを保護するためMPCソフトウェアを使い、企業・従業員を横断する集計を行っている。BWWCの公開ページは2023年の報告で103雇用主・約165,000人を記載し、報告を隔年で作成すると説明する。これは各個人の情報や集計結果からの推測リスクが一切ないことを意味しない。入力保護に加え、集計の粒度、参加者数、繰り返しクエリ、公開結果を管理する必要がある。

### 8.3 Google Chrome / Apple iCloud のパスワード漏洩チェック（Private Set Intersection: PSI）

Google Chrome と Apple のパスワード監視機能には、漏えい済み資格情報を照合するためのプライバシー保護暗号技術が使われている。ただし両社の方式・実装は同一ではなく、ブラウザーや機能の更新で変わる。
よく考えてみてほしい。Google や Apple は、どうやってあなたのパスワードが漏洩リストに含まれているかを確認しているのだろうか？もしブラウザがあなたの平文パスワード（あるいは単純なハッシュ値）をそのまま Google のサーバーに送信していたら、Google のサーバー管理者にあなたのパスワードがバレてしまう。逆に、Google が持っている「ダークウェブに流出した数十億件の漏洩パスワード辞書」を丸ごとあなたのPCにダウンロードさせるのも、データ量とセキュリティの観点から不可能である。

GoogleはChromeのPassword Checkupについて、blindingを使うPSI方式でユーザー名・パスワードと漏えい資格情報を照合すると説明している。AppleのPassword Monitoringも暗号学的PSIを使うと説明するが、細部は異なる。こうしたプロトコルは問い合わせ内容やサーバー側データの露出を抑えるよう設計される一方、実装、端末・サーバーの侵害、サイドチャネル、通信メタデータ、照合結果からの推測などのリスクまで自動的に消すものではない。Chromeの実装については、2023年の査読付き研究がマイクロアーキテクチャのサイドチャネルを報告している。具体的な挙動は各社の最新の技術資料を確認する。

### 8.4 医療・創薬における複数病院間の横断ゲノム解析（GWAS）と連合学習

「複数の病院が患者ゲノムを共同解析したいが、法令・契約・倫理審査などの要件に従い、個人データの共有方法を慎重に設計する必要がある」

複数機関のゲノムを共同解析するMPC研究では、主成分分析や関連統計を入力を秘密分散したまま計算する方式が提案されている。2018年のSecure GWAS研究は大規模データへの拡張を実験で評価したが、公開される統計値から推測できる情報は保護対象外であり、実用性・計算量は方式やデータ規模に依存する。法令への適合も暗号方式だけでは決まらない。

連合学習は、学習データを各端末・機関に残したままモデル更新を集約する学習方式で、MPCそのものと同義ではない。Secure Aggregationは個々の更新ではなく、所定数以上の参加者の集約値をサーバーが得るためのMPC系プロトコルである。集約値や繰り返し観測からの推測、参加者の少ないグループ、勾配反転などのリスクをゼロにはしない。必要に応じて差分プライバシーやクエリ制限などを組み合わせる。

### 8.5 MPC閾値署名ウォレット（Threshold Crypto Wallets：Fireblocks / Coinbase / ZenGo）

最後に、現在MPCが商業的に最も巨大な市場を形成しているのが、暗号資産（ブロックチェーン）における<strong>MPC閾値署名ウォレット（Threshold Signatures / Distributed Key Generation）</strong>である。
ビットコインやイーサリアムなどの暗号資産では、楕円曲線デジタル署名アルゴリズム（ECDSA や Schnorr / EdDSA）の<strong>秘密鍵 $sk$</strong> を失うことは資産の全損を意味し、逆に秘密鍵 $sk$ がハッカーに盗まれれば一瞬で全額が流出する。従来のハードウェアウォレットや単一サーバー保管では、「署名を作る瞬間に必ずどこか1つのメモリ上に秘密鍵 $sk$ が復元される」という<strong>単一障害点（Single Point of Failure）</strong>が避けられなかった。

これに対し、ジェナロとゴールドフェダー（Gennaro & Goldfeder 2018 / Lindell 2017）らが実用化した<strong>閾値ECDSA（Threshold ECDSA）プロトコル</strong>は、秘密鍵の生成段階（Distributed Key Generation: DKG）からして、誰一人として完全な秘密鍵 $sk$ を知ることがない。
たとえば、ユーザーのスマートフォンにシェア $sk_1$、クラウドサーバーAにシェア $sk_2$、セキュリティ会社のサーバーBにシェア $sk_3$ が $(2, 3)$ 閾値分散で保持される。送金トランザクションに署名する際には、これらのサーバーがMPCプロトコル（乗算トリプルや加法準同型暗号 Paillier）を実行し、<strong>秘密鍵 $sk$ を一度もどのメモリ上にも復元することなく、最終的なデジタル署名 $(r, s)$ だけを共同計算してブロックチェーンに送信する</strong>！

適切な閾値署名プロトコルでは、署名時に単一の参加者が秘密鍵全体を再構成せずに署名を共同生成できる。ただし、鍵生成・署名・端末・実装・運用の安全性は個別に評価が必要であり、製品ごとの方式や脅威モデルも異なる。プロアクティブ更新は、各期間内に攻撃者が侵害できる参加者数、更新処理の安全性、旧シェアの消去などの前提を置く防御で、複数サーバーの侵害を無条件に無力化するものではない。暗号資産の保全額や製品採用規模は、独立に検証可能な資料がない限り断定しない。

---

## 9. まとめ：信頼の前提を明示して共同計算する

MPCなどのプライバシー強化技術は、生データを各参加者間で共有する必要を減らし、従来難しかった共同計算を可能にする。ただし、プライバシーと有用性のトレードオフが消えるわけではない。公開出力そのものが個人情報を推測させる場合があり、脅威モデル、実装、通信、可用性、運用コストを含む設計が必要である。

本稿で見てきた通り、秘密計算（MPC）は、
1. <strong>シャミアの $(t, n)$ 閾値秘密分散法とラグランジュ補間</strong>によって、定められた閾値未満のシェアから秘密の情報を得られない性質を利用し、
2. <strong>BGWプロトコルとビーバーの乗算トリプル</strong>によって、プロトコルの閾値・前処理・攻撃者モデルの範囲で秘密を再構成せず有限体の演算を行い、
3. <strong>紛失通信（OT）とヤオのガーブルド・サーキット（および Free-XOR / Half-Gates）</strong>によって、プロトコルごとの通信・安全性条件のもとで非線形な大小比較やブール論理回路を評価する、

という精緻な数学的エンジンの結晶である。

MPCは、単一の仲介者へ平文データを集めずに共同計算する選択肢を提供する。しかし、参加者が誰も信用不要になるわけではなく、結託可能性、出力からの漏えい、実装と運用の前提を明示して使う必要がある。医療・金融・行政・機械学習への適用では、暗号学的保証と制度・法令・現場の対策を組み合わせて評価する。

**実装例の範囲**：このPythonコードは有限体上の秘密分散と演算を1つのプロセスで模擬する教育用サンプルです。ネットワーク上で各当事者が自分のシェアだけを保持するMPCシステムではなく、悪意ある参加者への検証、認証・安全な通信、信頼できる前処理、入力範囲・オーバーフロー管理も実装していません。`lagrange_reconstruct`で秘密や出力を復元する箇所では、その値は復元者に開示されます。実データや資産を保護する用途には使わないでください。

## 参考資料

- [Rabin, “How to Exchange Secrets with Oblivious Transfer” (1981)](https://eprint.iacr.org/2005/187.pdf)
- [Even, Goldreich, and Lempel, “A Randomized Protocol for Signing Contracts” (1985)](https://luca-giuzzi.unibs.it/corsi/Support/papers-cryptography/SigningContracts.pdf)

- [Bogetoft et al., “Secure Multiparty Computation Goes Live” (2009)](https://www.acsu.buffalo.edu/~mblanton/cse715/sugar-beet-auction.pdf)
- [BWWC: Wage Gap Studies](https://thebwwc.org/wage-gap-studies)
- [Google: Better password protections in Chrome](https://security.googleblog.com/2019/12/better-password-protections-in-chrome.html)
- [Apple Platform Security: Password Monitoring](https://support.apple.com/guide/security/password-monitoring-sec78e79fc3b/web)
- [Kwong et al., USENIX Security 2023: Chrome password-check side channels](https://www.usenix.org/conference/usenixsecurity23/presentation/kwong)
- [Cho et al., “Secure genome-wide association analysis using multiparty computation” (2018)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5990440/)
- [Bonawitz et al., Google Research: Practical Secure Aggregation](https://research.google/pubs/practical-secure-aggregation-for-federated-learning-on-user-held-data/)
- [Canetti et al., “UC Non-Interactive, Proactive, Threshold ECDSA” (2020)](https://eprint.iacr.org/2020/492)
- [Cao et al., “Understanding Information Disclosure from Secure Computation Output” (2025)](https://doi.org/10.1145/3705004)
- [Kolesnikov and Schneider, “Improved Garbled Circuit: Free XOR Gates and Applications” (2008)](https://encrypto.de/papers/KS08XOR.pdf)
- [Zahur, Rosulek, and Evans, “Two Halves Make a Whole: Reducing Data Transfer in Garbled Circuits using Half Gates” (2015)](https://www.cs.virginia.edu/~evans/pubs/ec2015/halfgates.pdf)

- [Stanford University cryptography notes: Oblivious Transfer](https://crypto.stanford.edu/pbc/notes/crypto/ot.html)

- [A Full Proof of the BGW Protocol for Perfectly Secure MPC](https://doi.org/10.1007/S00145-015-9214-4)

- [Yao, “Protocols for Secure Computations” (FOCS 1982)](https://doi.org/10.1109/SFCS.1982.38)
