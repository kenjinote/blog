---
title: "量子糾纏與貝爾不等式：愛因斯坦最後的挫敗與量子資訊革命的曙光"
description: "「幽靈般的超距作用」與 EPR 悖論。證明局域實在論破滅的貝爾不等式與阿斯佩的實驗，以及邁向諾貝爾獎的軌跡。"
slug: "quantum-entanglement-bells-theorem-local-realism"
date: "2026-10-03T05:00:00+09:00"
categories: ["physics", "quantum"]
tags: ["quantum-entanglement", "bells-theorem", "quantum-information", "physics-history"]
image: "eyecatch.jpg"
---

# 量子糾纏與貝爾不等式：愛因斯坦最後的挫敗與量子資訊革命的曙光

現代物理學中最大的謎團，同時也是最強大的工具——「量子糾纏（Quantum Entanglement）」。以及打破人類直覺「局域實在論」的「貝爾不等式」。這些不僅僅是物理學的理論遊戲，更向我們揭示了宇宙的根本性質，甚至成為量子電腦和量子密碼通訊等次世代科技的基石。

本文將從 1935 年愛因斯坦等人的 EPR 論文開始，講述隱變數理論的掙扎、約翰·史都華·貝爾推導出歷史性不等式、CHSH 不等式與量子力學中最大違反（齊雷爾森極限）的數學證明，以及阿斯佩等人進行實驗驗證，直到 2022 年獲得諾貝爾物理學獎的壯麗戲劇。我們將從物理學、量子資訊科學、科學哲學的視角進行極為詳細的解說。此外，還將穿插數學公式，深入探討透過多粒子糾纏的 GHZ 態完全否定局域實在論、量子遙傳的嚴密協定，以及糾纏的定量化手法。

---

## 第1章：1935年，愛因斯坦的反擊

1920年代，當量子力學正由哥本哈根學派（如尼爾斯·波耳與維爾納·海森堡等人）逐步建立公式化體系時，阿爾伯特·愛因斯坦對其機率性與非決定論的詮釋抱持著強烈的不滿。「上帝不擲骰子」這句名言，表達了他對量子力學底層機率性質的拒絕。

1935年，愛因斯坦與鮑里斯·波多爾斯基、納森·羅森共同發表了物理學史上留名的歷史性論文《量子力學對物理實在的描述能被認為是完備的嗎？（Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?）》，即所謂的「EPR論文」。這篇論文的目的是在邏輯上證明量子力學是「不完備」的，也就是說，必定存在著我們尚未知曉的「隱變數」。

### 局域性與實在性的定義

為了理解 EPR 論文的邏輯推演，我們必須準確掌握愛因斯坦等人所作為前提的兩個根本概念。

1. **實在性（Realism）**：
   不論是否被觀測，物理系統都具有確定的物理性質（數值）的觀念。在 EPR 論文中定義為：「如果在不以任何方式干擾系統的情況下，我們能確切地（機率為 1）預測某個物理量的值，那麼就存在一個對應該物理量的物理實在要素。」換句話說，測量前對象就已經確定地保有其屬性，這是古典力學中理所當然的常識。
2. **局域性（Locality）**：
   在空間上分離的兩個區域中，於其中一方進行的操作或測量，不會超越光速瞬間對另一方的物理現實產生影響，這是基於相對論的原則。根據狹義相對論，超越光速的資訊傳遞將導致因果律的崩潰，因此任何物理交互作用都受到光速的限制。

### 「幽靈般的超距作用」（Spooky action at a distance）與 EPR 悖論

在 EPR 論文中，提出了以下的思想實驗。
考慮兩個粒子 A 和 B，它們在強烈交互作用後彼此遠離。在量子力學的框架下，這兩個粒子處於「糾纏（Entangled）」狀態，被描述為整體的波函數。

假設我們測量了粒子 A 的位置 $x_A$。根據動量守恆定律等，當 A 的位置確定時，粒子 B 的位置 $x_B$ 也會瞬間確定。另一方面，如果我們測量粒子 A 的動量 $p_A$，粒子 B 的動量 $p_B$ 就會瞬間確定。
根據量子力學，位置和動量是不對易的物理量（$[x, p] = i\hbar$），無法同時具有確定的值（海森堡的不確定性原理）。然而，對 A 測量的選擇（測量位置還是動量），似乎超越了光速瞬間決定了 B 的狀態（是位置確定的狀態，還是動量確定的狀態）。

如果「局域性」是正確的，那麼對 A 的測量就不可能瞬間影響 B。愛因斯坦將此稱為「幽靈般的超距作用（Spukhafte Fernwirkung / Spooky action at a distance）」，並予以強烈批評。因此，他們得出結論：B 在被測量之前必定已經預先擁有了確定的位置和動量值（隱變數），而未能完全描述位置和動量的量子力學是一個「不完備的理論」。這個悖論成為了後來量子資訊理論中對糾纏本質理解的第一步。

---

## 第2章：隱變數理論的困境與波姆力學

在 EPR 論文發表後，物理學家們開始探索一個假說：「量子力學是正確的，但並不完備，在更深的層次上是否存在著決定論的理論（隱變數理論）？」

### 馮·諾伊曼錯誤的「不可能定理」

對這場爭論澆了一盆冷水的是天才數學家約翰·馮·諾伊曼。他在 1932 年的著作《量子力學的數學基礎》中，提出了一個證明（不可能定理），宣稱要建構一個與量子力學給出相同預測的「隱變數理論」在數學上是不可能的。
馮·諾伊曼的權威極大，在隨後的幾十年裡，「尋找隱變數是毫無意義的」這種風氣主導了物理學界。

然而，後來人們發現，馮·諾伊曼的證明在「隱變數應滿足的條件」中，包含了一個極度受限且非物理的假設（非對易物理量期望值的加法性：$\langle A+B \rangle = \langle A \rangle + \langle B \rangle$ 假設在隱變數層次也成立），實際上並不是一個完美的證明。葛蕾特·赫爾曼很早就注意到了這個缺陷，但在當時並未受到重視。

### 波姆力學：非局域隱變數理論

1952年，大衛·波姆打破了馮·諾伊曼的不可能定理，建構了一個能給出與量子力學完全一致預測的決定論「隱變數理論（波姆力學，或稱德布羅意-波姆理論）」。
在波姆的理論中，粒子始終具有明確的位置（隱變數），並由遍布整個宇宙的「量子位勢」所引導。這個位勢 $Q = -\frac{\hbar^2}{2m}\frac{\nabla^2 R}{R}$ 是透過將薛丁格方程式轉換為極座標表示而得，具有不隨距離衰減的奇異性質。

然而，波姆力學付出了沉重的代價。因為量子位勢會瞬間對整個空間產生影響，這個理論本質上是「非局域的」。愛因斯坦最厭惡的「幽靈般的超距作用」，卻被波姆力學作為理論核心包含在內。
愛因斯坦對波姆的理論也採取了否定的態度，稱之為「廉價的解決方案」，依然堅信「局域」隱變數理論的存在。

---

## 第3章：自旋1/2粒子的單態與量子力學的嚴密預測

在進入貝爾不等式之前，讓我們使用包立矩陣，完整展開量子力學所預測的糾纏相關性的嚴密狄拉克符號（Bra-Ket）計算過程。這將成為後來與局域實在論產生衝突的量子力學核心。

假設產生了一對自旋1/2的粒子，且總自旋為零，處於「單態（Singlet State）」。這個狀態 $|\psi^-\rangle$ 描述如下：

$$ |\psi^-\rangle = \frac{1}{\sqrt{2}} \left( |\uparrow\rangle_A \otimes |\downarrow\rangle_B - |\downarrow\rangle_A \otimes |\uparrow\rangle_B \right) $$

這裡，$|\uparrow\rangle, |\downarrow\rangle$ 分別代表自旋向上（$+1$）、向下（$-1$）的本徵態（$z$基底）。為了簡化，有時寫作 $|\psi^-\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)$。

愛麗絲在方向 $\vec{a}$，鮑伯在方向 $\vec{b}$ 分別測量他們粒子的自旋。方向向量為單位向量，在球座標系中可表示為 $\vec{a} = (\sin\theta_a\cos\phi_a, \sin\theta_a\sin\phi_a, \cos\theta_a)$ 等。
各方向的自旋測量算符，利用包立矩陣 $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ 可表示為 $\sigma_a = \vec{a} \cdot \vec{\sigma}$、$\sigma_b = \vec{b} \cdot \vec{\sigma}$。

我們想知道的是，愛麗絲和鮑伯測量結果乘積的期望值 $\langle \sigma_a \otimes \sigma_b \rangle$。為了計算這個，我們根據期望值的定義展開：

$$ \langle \psi^- | (\vec{a} \cdot \vec{\sigma}) \otimes (\vec{b} \cdot \vec{\sigma}) | \psi^- \rangle $$

首先，作為包立矩陣的性質，我們考慮 $\vec{a} \cdot \vec{\sigma} = a_x \sigma_x + a_y \sigma_y + a_z \sigma_z$。一個簡化計算的巧妙技巧是利用單態 $|\psi^-\rangle$ 是旋轉不變的（在任何基底中都具有相同形式）。但在這裡，我們進行更直接的代數方法完全展開。

算符 $(\vec{a} \cdot \vec{\sigma}) \otimes (\vec{b} \cdot \vec{\sigma})$ 展開如下：
$$ \sum_{i \in \{x,y,z\}} \sum_{j \in \{x,y,z\}} a_i b_j (\sigma_i \otimes \sigma_j) $$

期望值根據線性性質：
$$ \sum_{i,j} a_i b_j \langle \psi^- | \sigma_i \otimes \sigma_j | \psi^- \rangle $$
在此，我們針對每個成分評估 $\langle \psi^- | \sigma_i \otimes \sigma_j | \psi^- \rangle$。

對於 $|\psi^-\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$：
- $\sigma_z \otimes \sigma_z$：
  $\sigma_z \otimes \sigma_z |01\rangle = (+1)(-1)|01\rangle = -|01\rangle$
  $\sigma_z \otimes \sigma_z |10\rangle = (-1)(+1)|10\rangle = -|10\rangle$
  因此 $\sigma_z \otimes \sigma_z |\psi^-\rangle = -|\psi^-\rangle$，期望值為 $-1$。
- $\sigma_x \otimes \sigma_x$：
  $\sigma_x \otimes \sigma_x |01\rangle = |10\rangle$
  $\sigma_x \otimes \sigma_x |10\rangle = |01\rangle$
  因此 $\sigma_x \otimes \sigma_x \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle) = \frac{1}{\sqrt{2}}(|10\rangle - |01\rangle) = -|\psi^-\rangle$，期望值為 $-1$。
- $\sigma_y \otimes \sigma_y$：
  由 $\sigma_y |0\rangle = i|1\rangle, \sigma_y |1\rangle = -i|0\rangle$ 可得：
  $\sigma_y \otimes \sigma_y |01\rangle = (i|1\rangle) \otimes (-i|0\rangle) = |10\rangle$
  $\sigma_y \otimes \sigma_y |10\rangle = (-i|0\rangle) \otimes (i|1\rangle) = |01\rangle$
  因此 $\sigma_y \otimes \sigma_y |\psi^-\rangle = -|\psi^-\rangle$，期望值為 $-1$。

另一方面，不同成分（例如：$\sigma_x \otimes \sigma_y$）的期望值皆為 $0$。
因為 $\sigma_x \otimes \sigma_y |01\rangle = |1\rangle \otimes (-i|0\rangle) = -i|10\rangle$ 等，當與 $\langle \psi^-|$ 取內積時，會因為正交性而消失。

因此，非零的項只有在 $i=j$ 的情況：
$$ \sum_{i} a_i b_i \langle \psi^- | \sigma_i \otimes \sigma_i | \psi^- \rangle = \sum_{i} a_i b_i (-1) = - (a_x b_x + a_y b_y + a_z b_z) = - \vec{a} \cdot \vec{b} $$
這就是嚴密的推導。
若向量 $\vec{a}$ 和 $\vec{b}$ 的夾角為 $\theta$，根據內積的定義 $\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos\theta = \cos\theta$（因為方向向量是單位向量，長度為1）。
因此，量子力學所預測的相關性，成為了以下極為優美且簡單的公式：

$$ E(\vec{a}, \vec{b}) = \langle \sigma_a \otimes \sigma_b \rangle = - \cos\theta $$

這個 $-\cos\theta$ 的強烈相關性，正是古典隱變數理論絕對無法重現的「量子特有行為」之泉源。

---

## 第4章：約翰·史都華·貝爾的衝擊與 CHSH 不等式的嚴密推導

1964年，在 CERN 從事粒子物理學研究的愛爾蘭物理學家約翰·史都華·貝爾，利用空閒時間研究量子力學的基礎問題。他考慮到波姆力學是非局域的，於是產生了以下深遠的疑問：

「究竟，有沒有可能用愛因斯坦所期望的『局域』隱變數理論，來重現量子力學的所有預測呢？」

貝爾將這個原本僅限於哲學爭論的問題，透過嚴密的數學公式化，昇華為可以進行實驗驗證的形式。這就是在科學史上閃耀的「貝爾定理（Bell's Theorem）」與「貝爾不等式」。
接著在1969年，約翰·克勞澤、邁克爾·霍恩、阿伯納·希莫尼、理查·霍爾特四人（CHSH），推導出了能在現實實驗中驗證的擴充版不等式「CHSH不等式」。

### 局域實在論的假設與 CHSH 不等式的積分・代數展開

假設愛麗絲選擇 $a$ 或 $a'$ 作為測量儀器的設定，而鮑伯選擇 $b$ 或 $b'$。
基於局域實在論的「隱變數」設為 $\lambda$，其機率密度函數設為 $\rho(\lambda)$。由於機率已被歸一化：
$$ \int \rho(\lambda) d\lambda = 1 $$

愛麗絲的測量結果 $A$，僅取決於她的測量方向 $a$ 和 $\lambda$，而與鮑伯的測量方向 $b$ 無關（局域性）。
同樣地，鮑伯的測量結果 $B$，僅取決於 $b$ 和 $\lambda$（局域性）。此外，在測量之前結果就已經確定了（實在論）。因為結果是 $+1$ 或 $-1$：
$$ A(a, \lambda) = \pm 1, \quad B(b, \lambda) = \pm 1 $$
$$ A(a', \lambda) = \pm 1, \quad B(b', \lambda) = \pm 1 $$

愛麗絲與鮑伯測量結果的相關函數（期望值），可以透過對隱變數 $\lambda$ 積分來獲得：
$$ E(a, b) = \int A(a, \lambda) B(b, \lambda) \rho(\lambda) d\lambda $$

在此，我們考慮 CHSH 不等式核心的下列變數 $S(\lambda)$：
$$ S(\lambda) = A(a, \lambda)B(b, \lambda) + A(a, \lambda)B(b', \lambda) + A(a', \lambda)B(b, \lambda) - A(a', \lambda)B(b', \lambda) $$

我們針對愛麗絲的測量結果，對這個公式進行因式分解（提出公因式）：
$$ S(\lambda) = A(a, \lambda) \left[ B(b, \lambda) + B(b', \lambda) \right] + A(a', \lambda) \left[ B(b, \lambda) - B(b', \lambda) \right] $$

這裡進入了極其重要的邏輯步驟。$B(b, \lambda)$ 和 $B(b', \lambda)$，兩者的值必定都是 $+1$ 或 $-1$。
因此，若考慮它們的和與差，只存在以下兩種情況：

- 情況1： 當 $B(b, \lambda) = B(b', \lambda)$ 時
  和為 $B(b, \lambda) + B(b', \lambda) = \pm 2$，差為 $B(b, \lambda) - B(b', \lambda) = 0$。
- 情況2： 當 $B(b, \lambda) = -B(b', \lambda)$ 時
  和為 $B(b, \lambda) + B(b', \lambda) = 0$，差為 $B(b, \lambda) - B(b', \lambda) = \pm 2$。

無論在任何情況下，兩個中括號 $\left[ \dots \right]$ 的其中一個必定為 $\pm 2$，另一個必定為 $0$。
然後，乘上那個存活下來的 $\pm 2$ 的 $A(a, \lambda)$ 或 $A(a', \lambda)$ 也同樣是 $\pm 1$。
因此，對於任何隱變數 $\lambda$ 的值，在代數上必定成立以下等式：
$$ S(\lambda) = \pm 2 $$

也就是說，若取絕對值：
$$ |S(\lambda)| = 2 $$

為了求得這個 $S(\lambda)$ 的期望值 $S$，我們乘上機率分布 $\rho(\lambda)$ 在全空間進行積分。
$$ |S| = \left| \int S(\lambda) \rho(\lambda) d\lambda \right| \le \int |S(\lambda)| \rho(\lambda) d\lambda $$
利用 $|S(\lambda)| = 2$ 以及 $\int \rho(\lambda) d\lambda = 1$，得到：
$$ |S| \le \int 2 \rho(\lambda) d\lambda = 2 $$

這個期望值 $S$，可以展開為個別相關函數的和與差：
$$ S = E(a, b) + E(a, b') + E(a', b) - E(a', b') $$

因此，導出了以下的「CHSH 不等式」：
$$ |E(a, b) + E(a, b') + E(a', b) - E(a', b')| \le 2 $$

這就是，如果宇宙遵循著「局域實在論」，**絕對無法超越的極限值**。

### 量子力學最大違反（齊雷爾森極限）

請回想第3章導出的量子力學預測 $E(\vec{a}, \vec{b}) = -\cos\theta$。
假設愛麗絲和鮑伯將測量儀器設定在以下的角度：
- $a = 0$
- $a' = \pi/2$
- $b = \pi/4$
- $b' = -\pi/4$

（※附帶一提，如果使用光子的偏振，係數會與自旋1/2不同，變成 $E = \cos(2\theta)$，但使用上述自旋設定進行計算，本質是一樣的）
各設定間的角度差為：
$|a - b| = \pi/4$
$|a - b'| = \pi/4$
$|a' - b| = \pi/4$
$|a' - b'| = 3\pi/4$

代入量子力學的預測：
$E(a, b) = -\cos(\pi/4) = -1/\sqrt{2}$
$E(a, b') = -\cos(\pi/4) = -1/\sqrt{2}$
$E(a', b) = -\cos(\pi/4) = -1/\sqrt{2}$
$E(a', b') = -\cos(3\pi/4) = +1/\sqrt{2}$

將這些代入 CHSH 不等式的左邊 $S$：
$$ S = \left( -\frac{1}{\sqrt{2}} \right) + \left( -\frac{1}{\sqrt{2}} \right) + \left( -\frac{1}{\sqrt{2}} \right) - \left( +\frac{1}{\sqrt{2}} \right) = -\frac{4}{\sqrt{2}} = -2\sqrt{2} $$
取絕對值得到 $|S| = 2\sqrt{2} \approx 2.828$。

明顯超越了局域實在論極限的 $2$（$2.828 > 2$）。由量子力學所能達成的這個最大值，我們稱為**齊雷爾森極限（Tsirelson Bound）**。透過嚴密的數學證明，顯示出局域實在論與量子力學的預測是絕對無法相容的。

---

## 第5章：多粒子糾纏與局域實在論的「一擊」否定（All-or-Nothing）

貝爾定理是基於統計性相關的「不等式」。然而，1989年，丹尼爾·格林伯格、邁克爾·霍恩和安東·塞林格三人指出，如果考慮三個粒子糾纏的狀態（GHZ態），就不必依賴不等式或統計機率，僅憑一次測量結果的矛盾，就能完全駁倒局域實在論。這被稱為「All-or-Nothing證明」或「GHZ定理」。

### GHZ 態的性質
三個自旋1/2粒子的 GHZ 態定義如下：
$$ |GHZ\rangle = \frac{1}{\sqrt{2}} \left( |\uparrow\uparrow\uparrow\rangle - |\downarrow\downarrow\downarrow\rangle \right) $$

在此，我們作用以下包立算符的乘積：
1. $X_1 Y_2 Y_3 = \sigma_x^{(1)} \otimes \sigma_y^{(2)} \otimes \sigma_y^{(3)}$
2. $Y_1 X_2 Y_3 = \sigma_y^{(1)} \otimes \sigma_x^{(2)} \otimes \sigma_y^{(3)}$
3. $Y_1 Y_2 X_3 = \sigma_y^{(1)} \otimes \sigma_y^{(2)} \otimes \sigma_x^{(3)}$
4. $X_1 X_2 X_3 = \sigma_x^{(1)} \otimes \sigma_x^{(2)} \otimes \sigma_x^{(3)}$

利用：
$\sigma_x |\uparrow\rangle = |\downarrow\rangle, \sigma_x |\downarrow\rangle = |\uparrow\rangle$
$\sigma_y |\uparrow\rangle = i|\downarrow\rangle, \sigma_y |\downarrow\rangle = -i|\uparrow\rangle$
將 $X_1 Y_2 Y_3$ 作用於 $|GHZ\rangle$ 上：
$X_1 Y_2 Y_3 |\uparrow\uparrow\uparrow\rangle = |\downarrow\rangle (i|\downarrow\rangle) (i|\downarrow\rangle) = -|\downarrow\downarrow\downarrow\rangle$
$X_1 Y_2 Y_3 |\downarrow\downarrow\downarrow\rangle = |\uparrow\rangle (-i|\uparrow\rangle) (-i|\uparrow\rangle) = -|\uparrow\uparrow\uparrow\rangle$
因此，
$X_1 Y_2 Y_3 |GHZ\rangle = \frac{1}{\sqrt{2}} (-|\downarrow\downarrow\downarrow\rangle + |\uparrow\uparrow\uparrow\rangle) = |GHZ\rangle$
其本徵值為 $+1$。由對稱性可知，$Y_1 X_2 Y_3$、$Y_1 Y_2 X_3$ 的本徵值同樣也是 $+1$。

另一方面，將 $X_1 X_2 X_3$ 作用於其上：
$X_1 X_2 X_3 |\uparrow\uparrow\uparrow\rangle = |\downarrow\downarrow\downarrow\rangle$
$X_1 X_2 X_3 |\downarrow\downarrow\downarrow\rangle = |\uparrow\uparrow\uparrow\rangle$
因此，
$X_1 X_2 X_3 |GHZ\rangle = \frac{1}{\sqrt{2}} (|\downarrow\downarrow\downarrow\rangle - |\uparrow\uparrow\uparrow\rangle) = -|GHZ\rangle$
其本徵值為 $-1$。量子力學確切地（機率為1）預測了以上的結果。

### 局域實在論破滅的代數證明
在局域實在論中，認為測量結果是由預先決定的隱變數所決定的。
假設粒子1在X方向、Y方向的測量結果分別為 $m_x^1, m_y^1 \in \{+1, -1\}$。粒子2、3也作同樣的定義。
由於必須與量子力學 $+1$ 的預測一致，局域實在論的模型必須滿足以下三個方程式：
1. $m_x^1 m_y^2 m_y^3 = +1$
2. $m_y^1 m_x^2 m_y^3 = +1$
3. $m_y^1 m_y^2 m_x^3 = +1$

將這三個方程式全部乘起來：
$(m_x^1 m_y^2 m_y^3)(m_y^1 m_x^2 m_y^3)(m_y^1 m_y^2 m_x^3) = +1 \times +1 \times +1 = +1$
整理左邊，每個 $m_y^i$ 都被乘了兩次，因此 $(m_y^i)^2 = 1$。
$m_x^1 m_x^2 m_x^3 (m_y^1)^2 (m_y^2)^2 (m_y^3)^2 = m_x^1 m_x^2 m_x^3 = +1$

換句話說，只要遵循局域實在論，$X_1 X_2 X_3$ 的測量結果就必定是 $+1$。
然而，正如我們先前看到的，量子力學嚴密的預測（以及實際的實驗結果）是 $-1$。
$+1$ 和 $-1$。甚至不需要統計上的不等式，在單次測量中，局域實在論與量子力學就產生了決定性的矛盾，證明了量子力學的正確性。

（※順帶一提，在三粒子糾纏中，還存在具有與 GHZ 態不同性質的 W 態 $|W\rangle = \frac{1}{\sqrt{3}}(|100\rangle + |010\rangle + |001\rangle)$，它具有即使失去一個粒子，糾纏也不會完全破壞的堅固性。）

---

## 第6章：在量子資訊科學的應用與量子遙傳的嚴密展開

糾纏從悖論的對象，蛻變成了「資訊資源」。其代表性例子就是「量子遙傳（Quantum Teleportation）」。它於 1993 年由查爾斯·本內特等人提出，並在 1997 年由安東·塞林格（2022年諾貝爾獎得主）的團隊首次以實驗證實。

### 量子遙傳協定的數學公式展開

假設愛麗絲擁有一個未知的量子態 $|\phi\rangle = \alpha|0\rangle + \beta|1\rangle$，她想把這個狀態傳送給遠方的鮑伯。($|\alpha|^2 + |\beta|^2 = 1$)
根據量子不可複製定理（No-cloning theorem），我們無法複製這個狀態發送過去。而且，一旦進行測量就會導致狀態塌縮，無法準確知道未知的 $\alpha, \beta$。

因此，愛麗絲和鮑伯預先共享一對糾纏的粒子（EPR 對），具體來說是以下的貝爾態 $|\Phi^+\rangle$：
$$ |\Phi^+\rangle_{AB} = \frac{1}{\sqrt{2}}(|0\rangle_A |0\rangle_B + |1\rangle_A |1\rangle_B) $$

愛麗絲手邊有想要傳送的粒子（設為粒子 C）以及 EPR 對的其中一個（粒子 A）。鮑伯手邊有 EPR 對的另一個（粒子 B）。整個系統的初始狀態為：
$$ |\psi_{total}\rangle = |\phi\rangle_C \otimes |\Phi^+\rangle_{AB} = (\alpha|0\rangle_C + \beta|1\rangle_C) \otimes \frac{1}{\sqrt{2}}(|0\rangle_A |0\rangle_B + |1\rangle_A |1\rangle_B) $$
展開後為：
$$ \frac{1}{\sqrt{2}} \left( \alpha|000\rangle + \alpha|011\rangle + \beta|100\rangle + \beta|111\rangle \right) $$
（※下標順序為 $C, A, B$）

此時愛麗絲對她手邊的粒子 C 和粒子 A 進行「貝爾測量（Bell measurement）」。這是一種將兩個粒子投影到以下四個貝爾態基底的測量：
$|\Phi^\pm\rangle_{CA} = \frac{1}{\sqrt{2}}(|00\rangle \pm |11\rangle)$
$|\Psi^\pm\rangle_{CA} = \frac{1}{\sqrt{2}}(|01\rangle \pm |10\rangle)$

利用這些逆推 $|00\rangle, |01\rangle, |10\rangle, |11\rangle$，並用貝爾基底 $|\cdot\rangle_{CA}$ 重新整理整個系統的狀態，令人驚訝地，可以變形成如下形式：
$$ |\psi_{total}\rangle = \frac{1}{2} \left[ |\Phi^+\rangle_{CA}(\alpha|0\rangle_B + \beta|1\rangle_B) + |\Phi^-\rangle_{CA}(\alpha|0\rangle_B - \beta|1\rangle_B) + |\Psi^+\rangle_{CA}(\alpha|1\rangle_B + \beta|0\rangle_B) + |\Psi^-\rangle_{CA}(\alpha|1\rangle_B - \beta|0\rangle_B) \right] $$

當愛麗絲進行貝爾測量時，系統會以 1/4 的機率塌縮到這四個項中的任何一個。
1. 如果愛麗絲得到 $|\Phi^+\rangle$，鮑伯的狀態為 $\alpha|0\rangle + \beta|1\rangle = |\phi\rangle$，傳送已經完成（么正算符 $I$）。
2. 如果得到 $|\Phi^-\rangle$，鮑伯的狀態為 $\alpha|0\rangle - \beta|1\rangle$。鮑伯只要施加包立 $Z$ 算符（$\sigma_z$），就能恢復成 $|\phi\rangle$。
3. 如果得到 $|\Psi^+\rangle$，鮑伯的狀態為 $\alpha|1\rangle + \beta|0\rangle$。鮑伯只要施加包立 $X$ 算符（$\sigma_x$），就能恢復成 $|\phi\rangle$。
4. 如果得到 $|\Psi^-\rangle$，鮑伯的狀態為 $\alpha|1\rangle - \beta|0\rangle$。鮑伯先施加 $Z$ 再施加 $X$（即 $XZ$ 或 $i\sigma_y$），就能恢復成 $|\phi\rangle$。

愛麗絲透過一般的通訊（電話或網路），將測量結果（2位元的古典資訊：00, 01, 10, 11）傳達給鮑伯。這種通訊不會超越光速，因此不違反相對論。鮑伯根據接收到的2位元，應用適當的包立算符，完美地還原未知的量子態 $|\phi\rangle$。
這就是量子遙傳的完整協定。

---

## 第7章：糾纏的定量化（Quantification）

糾纏不僅僅是「有」或「沒有」，還可以定量化「糾纏的強度有多強」。在量子資訊理論中，這是一個極其重要的研究主題。

### 1. 馮·諾伊曼糾纏熵（von Neumann Entanglement Entropy）
測量處於純態的雙體系統 $AB$ 糾纏程度的標準尺度，是馮·諾伊曼熵。設整個系統的密度矩陣為 $\rho_{AB} = |\psi\rangle\langle\psi|$，將系統 B 跡除（縮約，trace out）以求得系統 A 的縮約密度矩陣 $\rho_A = \text{Tr}_B(\rho_{AB})$。
此時，糾纏熵 $S$ 定義如下：
$$ S(\rho_A) = -\text{Tr}(\rho_A \log_2 \rho_A) $$
在貝爾態這樣的最大糾纏態中，$\rho_A$ 會成為完全混合態（與單位矩陣成正比），並取得 $S = 1$（最大值）。直觀地說，這表現了糾纏的本質：「我們完全知道整體的狀態，但如果只看部分（系統 A），卻完全沒有任何資訊（看起來是隨機的）」。

### 2. 共生糾纏度（Concurrence）
測量包含混合態的雙量子位元系統糾纏程度的尺度，有威廉·伍特斯等人發明的「共生糾纏度 $C(\rho)$」。
對於密度矩陣 $\rho$，計算自旋反轉態 $\tilde{\rho} = (\sigma_y \otimes \sigma_y) \rho^* (\sigma_y \otimes \sigma_y)$（$\rho^*$ 為複數共軛）。
假設矩陣 $R = \sqrt{\sqrt{\rho} \tilde{\rho} \sqrt{\rho}}$ 的本徵值依大小順序為 $\lambda_1, \lambda_2, \lambda_3, \lambda_4$，則共生糾纏度定義如下：
$$ C(\rho) = \max(0, \lambda_1 - \lambda_2 - \lambda_3 - \lambda_4) $$
$C(\rho)$ 的值介於 $0$（無糾纏）到 $1$（最大糾纏）之間，並且具有強大的數學性質，可以使用這個值直接計算稱為「形成糾纏度（Entanglement of Formation）」的另一種尺度。

### 3. 負值度（Negativity）
基於部分轉置（Partial Transpose）概念的尺度是負值度 $\mathcal{N}(\rho)$。
對於系統 $AB$ 的密度矩陣 $\rho$，只針對系統 B 的基底進行轉置，記為 $\rho^{T_B}$。如果 $\rho$ 是非糾纏的（可分離的）狀態，則 $\rho^{T_B}$ 的本徵值全部為非負（Peres-Horodecki 的 PPT 判斷基準）。
反過來說，如果存在負的本徵值，這就是糾纏的證據。負值度使用 $\rho^{T_B}$ 的跡範數（Trace Norm） $||\cdot||_1$，定義如下：
$$ \mathcal{N}(\rho) = \frac{||\rho^{T_B}||_1 - 1}{2} $$
這等於負本徵值絕對值的總和，因為計算容易，所以成為研究高維度系統或多體系統糾纏時極為有用的指標。

---

## 第8章：實驗驗證與漏洞（Loophole）的徹底封閉

理論已經完成，應用也清晰可見。剩下的就是要在實驗室裡追問大自然，它實際上遵循著哪一種法則。

### 阿蘭·阿斯佩的切換實驗（1982年）
必須排除一種可能性：在愛麗絲和鮑伯決定測量儀器角度之後，該資訊以低於光速的速度傳達到另一方，從而影響了「隱變數」。這被稱為「局域性漏洞（Locality Loophole）」。
法國的阿蘭·阿斯佩等人成功地進行了一項實驗：在光子從光源飛向測量儀器的過程中，使用聲光元件以超高速隨機切換測量儀器的角度設定。藉此創造出即使是光速訊號也無法傳遞資訊的狀況（空間隔離），並出色地觀測到了不等式的違反。愛因斯坦的「幽靈般的超距作用」成為了現實。

### 終極挑戰：完全無漏洞（Loophole-free）實驗（2015年）
在阿斯佩的實驗之後，仍保留了極少數反駁的餘地，例如探測效率過低（聲稱未能測量到的光子帶有方便的隱變數，即「探測漏洞 / Fair-sampling Loophole」）。
然而在 2015 年，荷蘭台夫特理工大學、奧地利維也納大學、美國 NIST 等多個研究團隊，終於成功進行了同時封閉所有主要漏洞的「無漏洞貝爾測試（Loophole-free Bell test）」。在台夫特的實驗中，藉由讓相距 1.3 公里鑽石 NV 中心內的電子自旋產生糾纏，徹底封鎖了局域性漏洞與探測漏洞，為局域實在論的棺材釘上了最後一根釘子。

---

## 代結語：愛因斯坦的挫敗所帶來的光芒

2022 年，為量子力學基礎立下決定性貢獻的阿蘭·阿斯佩、約翰·克勞澤、安東·塞林格三人獲頒了諾貝爾物理學獎。

愛因斯坦厭惡量子力學的機率性質與非局域性，為了批評它而寫下了 EPR 論文。但諷刺的是，他尖銳的批評明確地凸顯了「糾纏」這個概念，並透過貝爾這位天才，為人類真正理解宇宙非局域的連結，並將其作為科技應用，開闢了一條嶄新的道路。

愛因斯坦的「最後挫敗」，絕不是物理學的停滯，而是人類獲得量子資訊這門全新宇宙語言的偉大曙光。

---
*責任編輯：量子資訊科學科技作家*
*本文是涵蓋從量子力學基礎到最尖端量子資訊技術的學術性解說。*
