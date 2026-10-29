# エラトステネスの篩：原文調査

2026-10-29、Codex (AI)。この予備調査だけで翻訳を校閲済みとは数えない。

## 読了と元の挙動

日本語・英語の旧メタデータと本文、各2コードを全文読了。その他11翻訳はこの段階では未読であり、13版のハッシュ・実効公開日・canonical採取は機械検査にすぎない。`batch-020-source-audit.json` に旧版と実行証拠を保存した。

Rust 1.90.0 / x86_64-pc-windows-msvcで、元の日英2コードずつをedition2021、warnings拒否、overflow-checks=yesでコンパイルし実行した。**改変しないn=1000の全4例は、独立したPython整数の試し割りによる全168素数と一致した。**最初は2、最後は997。実際の固定上限でコードが故障したという主張はしない。

別実験として固定のnを0・1・2へ変更した。基本版のn=0、偶数を除く版のn=0・1は添字の範囲外でpanicとなる。これは上限を変更した場合の適用範囲であり、元のn=1000の不具合と混同しない。元コードの掛け算も1000に対しては問題なく、桁の大きい任意入力での検査まで行ったとはしない。

## 訂正すべき説明

- 0からNまで添字を使うにはN+1要素が必要。本文のN要素とコードのn+1要素が不一致。
- p²未満の倍数を省けるのは、より小さい素因数の段階で処理できるため。「小さい数の列挙がすべて終わっている」とは異なる。
- 2自体は素数。合成数なのは2より大きい偶数。
- 平方根以下でよいのは倍数を除く処理の素因数候補。出力する素数全体を平方根以下に制限するのではない。
- false初期化の方が常に高速という断定の根拠や実測はない。候補や書き込み回数の削減と、実測速度を区別する。
- RustというリンクがWebAssembly記事へ向いている。対象を読んだことにせず、適切な一次資料を示す。
- GIFに代替テキストと出典／作者情報がない。

## 一次資料の読了範囲

- [Rust Reference：Boolean type](https://doc.rust-lang.org/reference/types/boolean.html)：短いページを読了。boolのサイズとアラインメントは各1、false/trueの表現。RustのVec<bool>をC++の特殊なビット圧縮vector<bool>と混同しない。
- [Rust標準ライブラリVecのGuarantees](https://doc.rust-lang.org/std/vec/struct.Vec.html#guarantees)：連続したlen個の要素とcapacity、size_ofに関する該当段落を読了。ページ全6780行、unsafe API全体を読んだという主張ではない。取得された現行ドキュメントは1.99.1で、実際のコンパイル環境1.90.0と区別する。
- [Princeton Introduction to Programming：Analysis of Algorithms](https://introcs.cs.princeton.edu/java/41analysis/)：篩についての末尾の設問6と解答を読了。n log log nの成長率とMertensの定理への言及を確認。検索結果の後、web取得は403だったためWindowsの通常TLS検証付きHTTP取得で当該箇所を確認した。章全体・数論の証明全体の読了とはしない。最初に試した14array/Sieve.java.htmlは取得できず、実装原典の読了として数えない。

## GIFの照合

既存ファイルの最初のフレームを目視。2から120までの表とドイツ語Primzahlenの見出しを確認した。全アニメーションの目視確認はしていない。Pillowで445×369、159フレーム、206214バイトと確認。

[Commonsの公開ファイルページ](https://commons.wikimedia.org/wiki/File:Animation_Sieb_des_Eratosthenes.gif)のSummary・Licensing・File historyを読了。作者SKopp、現行ファイルはSuricataの2006年更新版、CC BY-SA 3.0が示されている。ファイル名だけで同一とは判断せず、公開元ファイルを通常TLS検証付きのWindows HTTP取得で読み、既存ファイルとバイト単位で完全一致を確認した。SHA256は `749afb4300f631891b1f76a41e334bbef038bae11a1a2dd574e65724ccb249d9`。

先行Python urllib取得は証明書検証エラーとなり、webの画像取得もcache missとなった。TLS検証を無効にしていない。失敗と成功した後続照合をauditへ併記している。

この時点では記事の修正、翻訳校閲記録、公開後確認は未完了。

## 日英中2版の修正・確認

原文と英訳を修正し、各2Rustコード・8TeX表現と本文全体を独立した出力で読み直した。最初の生成時にJavaScript文字列でTeXのバックスラッシュが失われたため、読み直しで検出して `le` / `log` を正しいコマンドへ訂正した。校閲記録前に検査済み。

その後、簡体字・繁体字も旧版と修正版のメタデータ・本文・全コードを全文読了。簡体字の素数・合数・下标・字节・内存、繁体字の質數・合數・索引・旗標・函式・位元組・記憶體を整理し、境界・倍数を消す範囲と出力範囲・速度とメモリの条件を原文と照合した。他9翻訳は未読・未記録。

中国語版の照合時に、`checked_add` 自体がpanicするように読める説明を発見。公式の [usize::checked_add](https://doc.rust-lang.org/std/primitive.usize.html#method.checked_add) の戻り値・例と [Option::expect](https://doc.rust-lang.org/std/option/enum.Option.html#method.expect) の戻り値・panic条件・例を追加で読んだ。どちらも該当メソッドの範囲であり、usize／Optionの全ページの読了ではない。オーバーフローでNoneを返し、続くexpectがpanicを起こすように4版とも説明を訂正。コードは全く変わらないことを確認したが、現行4版のハッシュと結び付けて実行検査も再実施した。

英訳の初回証拠 `batch-020.json` の該当レビューは変更せず、`batch-020-en-revision.json` で再確認を記録した。台帳の英訳参照を更新し、確認件数を二重計上しない。

日英中2版はそれぞれ、2コード×debugchecked／optimizedcheckedの各モードで2161上限の全素数ベクタを独立したPython整数の試し割りと厳密比較。各実行ファイルの1000に対する168行の完全出力とusizeMAXの明示的な拒否も検査した。後者はcatch_unwindと一時的なpanic hookを用い、大量メモリ確保は試していない。全32TeX表現、8コード全文、GIFの代替テキストと出典、既存URL／公開日を生成HTMLで確認。21記事束ビルド、多言語1283ページ、HTTPS2368HTML／41XMLを通過した。
