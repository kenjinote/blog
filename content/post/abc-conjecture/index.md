---
title: "ABC予想とIUT理論：証明の主張と続く議論"
date: "2026-09-14T13:00:00+09:00"
lastmod: 2026-11-23
slug: "abc-conjecture"
image: "eyecatch.jpg"
categories: ["mathematics", "science"]
tags: ["ABC Conjecture", "Number Theory", "IUT Theory", "Shinichi Mochizuki"]
draft: false
description: "ABC予想の内容、望月新一教授のIUT理論による証明の主張、査読誌掲載と数学界の未解決の議論を、数式と出典を添えて整理します。"
---

## ABC予想とは

互いに素な正の整数 $a,b,c$ が $a+b=c$ を満たすとします。正整数 $n$ の**根基**を、$n$ を割り切る相異なる素数の積

$$\operatorname{rad}(n)=\prod_{p\mid n}p$$

と定義します。たとえば $n=2^3\cdot 3^2$ なら $\operatorname{rad}(n)=2\cdot3=6$ です。根基は素因数の指数を無視するため、整数そのものより小さくなることがあります。

ABC予想は、任意の $\varepsilon>0$ に対して定数 $K_\varepsilon$ が存在し、すべてのそのような組について

$$c\le K_\varepsilon\operatorname{rad}(abc)^{1+\varepsilon}$$

となる、という主張です。1985年にジョゼフ・オステルレとデイヴィッド・マッサーが定式化しました。定数は $\varepsilon$ に依存します。この予想は、和と素因数分解との間に強い制約があることを表しますが、「$a$ と $b$ が小さな素因数を持てば、$c$ に大きな素因数が必ず現れる」という単純な規則ではありません。

## IUT理論による証明の主張

京都大学の望月新一教授は2012年に、ABC予想を含むディオファントス幾何の問題に取り組む新しい枠組みとして、宇宙際タイヒミュラー理論（IUT理論）の論文を公開しました。IUTは数体上の楕円曲線を含む算術的対象を扱い、テイヒミュラー理論、ホッジ・アルケロフ理論、遠アーベル幾何などを組み合わせた非常に技術的な理論です。ホッジ劇場やログ・テータ格子などの概念を用いて、異なる構造の間で算術情報を比較することを目指します。これを「加法と乗法を別々の宇宙に分ける」とだけ説明すると、理論の内容を誤って単純化します。

望月教授はIUTからABC予想が従うと主張しています。論文4編は長い査読を経て、2021年に『Publications of the Research Institute for Mathematical Sciences』（PRIMS）第57巻の特集号に掲載されました。掲載された事実は重要ですが、それだけで数学界全体の合意や、議論の終結を意味するものではありません。

## 何が議論されているのか

ピーター・ショルツとヤコブ・スティックスは2018年の報告で、特にIUT第III論文の定理3.11から系3.12に進む箇所に、ABC予想へつながる議論の欠落があると論じました。望月教授はこの批判は理論の誤解に基づくとして反論しています。2025年の報告でも自らの立場を詳しく述べています。ここで紹介したのは各著者の主張の要約であり、IUTの証明を独立に検証したものではありません。

したがって、慎重な説明では「IUT論文はPRIMSに掲載された」「望月教授はABC予想の証明を主張している」「その証明の核心について数学者間に未解決の見解の相違がある」を区別します。ABC予想を、広く確立した定理として扱うのは適切ではありません。

## フェルマーの最終定理との関係

ABC予想が正しければ、フェルマーの最終定理 $x^n+y^n=z^n$（$n\ge3$ の正整数解はない）も導けます。これは定理がまだ証明されていないという意味ではありません。フェルマーの最終定理はアンドリュー・ワイルズらによってすでに証明されており、ここではABC予想がもたらす**別の含意**を説明します。

理由は簡潔です。もし互いに素な正整数解 $x,y,z$ があれば、任意の正整数 $k$ に対して $(x^{nk},y^{nk},z^{nk})$ も互いに素な和の組になります。一方、$\operatorname{rad}(x^{nk}y^{nk}z^{nk})=\operatorname{rad}(xyz)$ は一定のまま、$z^{nk}$ は際限なく大きくなります。したがって、固定した $\varepsilon>0$ に対するABCの上界を破る組が無限にでき、予想に反します。

## 参考資料

- [ABC予想の標準的な定式化（Jordan S. Ellenberg）](https://arxiv.org/abs/math/9909098)
- [PRIMS 2021年IUT特集号](https://ems.press/journals/prims/issues/1507)
- [ショルツ・スティックス報告（2018年）](https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf)
- [望月教授によるIUT報告（2025年10月）](https://www.kurims.kyoto-u.ac.jp/~motizuki/IUT-report-2025-10.pdf)
- [IUT理論の概説（望月教授、2012年）](https://www.kurims.kyoto-u.ac.jp/~motizuki/Panoramic%20Overview%20of%20Inter-universal%20Teichmuller%20Theory.pdf)

この記事は論争の経緯と基本的な数式を紹介する短い概説であり、IUT論文の証明を再構成・判定するものではありません。
