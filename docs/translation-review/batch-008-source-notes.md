# バッチ008：オイラーの等式の原文校閲

2026-10-24。日本語原文を全文読み、下記を訂正した。英語版も全文を読み、原文に対応する証明・幾何学・応用の欠落を補ってから照合した。他の11翻訳は未校閲。

- ファインマンの引用は、I巻22章の一般のオイラーの公式についての言葉であることを確認。特殊値での等式だけに帰した引用を訂正し、出典のない「神が書いた数式」の引用を除去した。
- 重複した `date` は、変更前にHugoの一覧出力で実際の公開日が2026-09-14T13:00:00+09:00であることを確認して一本化。更新日は校閲日とした。
- 0と1の単位元としての役割、自然数の慣習、ユークリッド平面での円周率、指数モデルの適用範囲、虚数単位の向きの約束を説明した。歴史を単一の起源や発明者へ過度に帰す説明を整理した。
- 実数xとラジアンを明示。複素指数関数を絶対収束する級数で定義し、z=0とそれ以外の比の判定を区別。実変数の公式に形式的な代入をするだけの証明から、偶奇項の分離を正当化する説明にした。元の表示数式13組は保持した。
- 虚部は実数値であることを説明。正負の角度、長さの保存、原点の固定を含めて回転を確認した。
- Euler Archiveの1748年刊『Introductio』第1巻の書誌・概要と、ETH図書館の伝記を確認。著作数・記号の発明・コーツの先取権などの断定は、本記事では根拠を確認できた具体的な記述に置き換えた。原典全文を読んだとは扱わない。
- FFTは有限列のDFTを計算するアルゴリズム、通常の非可逆JPEGの基本方式はDCTであると区別。微積分の条件と原始関数、フェーザの線形・時間不変・単一周波数・定常状態の条件を補った。
- 波動関数は確率振幅で、規格化した位置表示の絶対値二乗が確率密度であると訂正。一般の状態が単一指数関数だとはしない。

## 読んだ資料と範囲

- [NIST DLMF §4.2(iii)](https://dlmf.nist.gov/4.2#iii)：複素指数関数の級数と三角関数の関係。
- [MIT 18.100C Lecture 11](https://ocw.mit.edu/courses/18-100c-real-analysis-fall-2012/1058808e5cb57c986118333f8b6fa0d7_MIT18_100CF12_l11sum.pdf)：複素指数級数の無限収束半径・絶対収束。
- [ファインマン I巻22章](https://www.feynmanlectures.caltech.edu/I_22.html)：§22–6末尾の引用と回転の説明。[23章](https://www.feynmanlectures.caltech.edu/I_23.html)の複素振動計算、[25章](https://www.feynmanlectures.caltech.edu/I_25.html)の線形性と定常・過渡の説明も参照。
- [MIT 6.002講義ノート](https://circuits.mit.edu/_static/S23/handouts/lec10b/lecture10b-berggren.pdf)：正弦波定常状態、線形性、インピーダンス法と実部の復元。草稿内のすべての式を認証したという意味ではない。
- [MIT 6.341 Lecture 19](https://ocw.mit.edu/courses/6-341-discrete-time-signal-processing-fall-2005/resources/lec19/)：リンク先講義PDFのDFT定義、FFTの計算量と分解。
- [ファインマン III巻3章](https://www.feynmanlectures.caltech.edu/III_03.html)：複素振幅・絶対値二乗と波動関数の意味。
- [ITU-T T.81](https://www.w3.org/Graphics/JPEG/itu-t81.pdf)：§3.1.58–59、§4.2のDCT方式の定義。規格全体を検証したとは扱わない。
- [Euler Archive書誌](https://scholarlycommons.pacific.edu/euler-works/101/)：刊年、関数・指数関数・記法の位置づけ、収録内容の概要。[ETH図書館](https://library.ethz.ch/sammlungen-und-archive/kurzportraets/leonhard-euler-1707-1783.html)：生没年、出身、失明後の活動。

## 補助検査

`batch-008-validation.json` に原文・翻訳ハッシュ、表示数式、図、リンク、係数25件と指数6件・回転9件の補助計算を保存する。数値検査は全実数での証明の代用ではない。英語は原文の13組に対して8組しかなく、欠落した式・証明・応用を補った。他言語の式数が一致しても、本文未読のまま校閲済みにはしない。
