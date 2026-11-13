# バッチ035：コルモゴロフ複雑性の原稿調査

2026-11-13。**予備調査のみ。改稿・翻訳承認・公開確認は未完了、加算0。**

## 実際に読んだ範囲

- 日本語原文569行を1–240、241–475、476–末尾の3区分で全文確認。メタデータ、全7章、数式、表、2図の全ラベル・接続、証明用Python風擬似コード2個を含む。
- 英語原稿537行を1–220、221–460、461–末尾で全文確認。同じ範囲を読み、英語だけにある補足・相違も確認。
- 他11言語はファイル名・行数・ハッシュ・見出し等の機械的な棚卸しのみ。いずれも111行・4章で、本文未読。短いという構造的事実だけで省略の意味・誤訳の内容を認定しない。
- 初期ハッシュ、公開日時・言語・パス、機械的構造、画像ハッシュは [初期棚卸し](batch-035-source-audit.json)。画像そのものは未視認。
- 日本語・英語ともまだ変更していない。校閲台帳420件は不変。バッチ034の公開確認待ちと並行した予備調査である。

## 原稿を読んで確認した修正候補

1. 日本語冒頭は「プレーンテキスト100万文字」と「100万bit＝125,000byteのビット詰め」を混同。英語はraw binaryと明記しており、この日本語固有の誤記を転用しない。
2. 公平独立なコインの実現値も、偶然すべて0や交互列になり得る。S3の複雑性・短い規則の不存在は各実現値への保証ではなく、固定機械・欠損定数を指定した高確率の主張へ直す。実際に100万回の物理実験を行った証拠はなく、提示ビット列も模式例として扱う。
3. πの正規性を「強く信じられる」とした後で既知の性質として使用している。有限の経験頻度・固定kについての漸近性・計算可能性・正規性・暗号学的予測不能性を区別する。Shannon理論全体を0次頻度モデルと同一視しない。π用の計算可能な予測器・分布をモデルにできる。
4. prefix complexity K と plain C を分けて導入した後、S1とπのKを一律 log2(n)+O(1) と等号で置いている。自己区切り整数の記述を含め、計算可能な列の長さnの接頭辞には K(prefix)=K(n)+O(1) とするのが適切。単にnの通常の二進桁を付けるだけではprefix条件を満たさない。条件付きK(prefix|n)=O(1)と、K(n)=O(log n)の粗い上界は別に述べる。
5. 無条件K(x)≤|x|+O(1)は一般には成立しない。英語5.1にもこの誤式がある。一方4.1は両版ともplain/条件付きK/無条件prefix Kを既に区別しているので、正しい段落まで一律誤りとはしない。
6. 日本語不変性定理は任意の「万能」機械と任意Aを無条件に混ぜている。加法最適なplain/prefix機械をそれぞれ同じクラスで固定する。英語定理文はadditively optimalを既に明記しており、この点を日本語と同じ誤りとして転用しない。英語の専用機械の定数が必ず100万bit以上という断言は、対象文字列の高複雑性を未証明のまま前提にしており、有限対象の機械依存を消せる定理でもない。
7. 非圧縮性定理のカウント式はc≥0を無制限に許しているが、表示の 2^n−2^(n−c)+1 はc>nで総数2^nより大きくなる。0≤c≤nに制限して式を示し、c>nはC(x)≥n−cが全対象で自明という別ケースにする。
8. C(x)≥n−cは「c bitまで短縮できない」ではなく「c bitを超える短縮ができない」。日本語c=1、10、20と英語c=10、20の説明に境界のずれがある。割合の下界が1になる・全自然界を意味するとの読み方も避ける。
9. 有限長で高複雑性であること、無限列の全接頭辞に同じ定数が使えること、通常の統計検定を一回棄却しないことは別。日本語ML検定の定義は一様c.e.開集合と測度条件を明示する。英語はその定義を既に記載しているが、「計算可能martingaleが成功しない」とML-randomの同値を主張しており、computable randomnessとの区別が必要。
10. 日本語Berryの例はUnicodeコードポイントで25文字なのに24文字と記述。30文字未満であるという例の趣旨は保てる。英語の英語11語という計数は実際に11語で正しく、誤りを転用しない。
11. Berryの探索は長さ順・同じ長さ内辞書順のshortlexと明記する。通常の辞書順は全有限列の実効的な全列挙と同一ではない。ComputeKは背理法の仮定であり実装できないoracleを実装済みプログラムのように示さない。既存コードは関数定義・擬似コードであり、未定義oracleを呼んで失敗させても「Kの実装バグを再現した」とは扱わない。
12. 上からの近似は整数列なので各固定xで実際には有限段階から一定になるが、その到達を全入力について判定する手続きがない。「到達する瞬間が永遠にない」とは異なる。
13. Chaitinの定数は基準機械・理論・表現・健全性の仮定に依存する。表示L=C_F+cと、証明に使ったC_F+log L+c'の関係を整える。任意に20,000/50,000bitをZFCの限界と断定しない。図の「n>Lなら99.9999%以上」も間隔n−Lに依存する。定理を数学の一般的な情報量保存則や公理より長い定理が出せないという主張にしない。
14. Ωは最適prefix機械Uごとに異なる。Kraftだけで非厳密≤1は出るが、0<Ω<1とランダム性には機械の仮定を含む説明が必要。既知N桁の下端aに対し、部分和がaを**超えた**段階で残りの重みが2^−N未満になるという論証へ。日本語は「達した」としているが英語は既にexceeded。すべての数学命題を数千桁で決められるとはせず、同じ機械で一定長以下の停止問題に符号化できる対象に限定する。
15. 平均Kとエントロピーはモデルの与え方・計算可能性・prefix条件付き・加法定数を含む関係で、数値的な完全一致ではない。離散分布の有限／可算、有限エントロピー、0確率の扱い、符号長の丸めを整える。
16. 停止してちょうどxを出すprefix機械による離散普遍半測度m(x)と、出力がxで始まる単調機械のSolomonoff半測度M(x)を区別する。符号化定理をそのまま後者の予測分布に適用しない。一般の尤度P(D|H)を常に2^−K(D|H)と置けるわけではなく、Bayes/MAPと二部MDLの等式を一般定理として断定しない。
17. NIDの理論定義と、連結表現・対表現や加法誤差を含む式、実圧縮器NCDの近似上の制約を分ける。圧縮器の窓・ヘッダ・順序・データ長に依存し、実NCDを厳密な距離や常に同一ファイルでほぼ0となる普遍的な保証にしない。実験報告をすべての系統樹の正解保証にしない。
18. 予測確率と理想符号長の対応には正の確率、再現可能な有限モデル、decoder共有、トークナイザ・系列長・丸め・フレーミングが必要。固定サイズのモデルの訓練NLL最小化と、モデル記述長も含むMDL最小化を同じ最適化と断定しない。圧縮改善だけで世界の因果法則やAGIの獲得が論理的に強制されるという主張は、仮説・解釈と数学的事実を分ける。
19. 英語だけのMermaidラベルにロシア語「десятки」が混入。英語のHutter Prize説明はenwik8とenwik9を同じ100MBと括っており要修正。賞の現行詳細・引用の正確な出典は未確認なので、直接引用・現行額・測定値を新たに断定しない。

## 実際の有限検査

[有限検査](batch-035-original-finite-probe.json) と再現用 [Python](probe_batch_035_original.py)。

- n=0..16、0≤c≤nの153組で幾何和・数え上げの下界が総数内に収まることを確認。
- c>nの4例では旧式の下界が総数を上回る。例n=1,c=2は下界5/2に対し全体2個。
- ASCII/UTF-8の01を50万回＝100万byte、ビット詰めなら125,000byte。メモリ管理オーバーヘッドのベンチマークではない。
- 上記日本語例25コードポイント、英語例11語。
- 固定seed3501の65,536byte列にgzip(mtime=0)を使った有限例。C(x)=65,574byte、C(xx)=131,130byte、NCD(x,x)=3642/3643≈0.9997255。展開の完全一致も検査。これは一つの有限窓の例であり、全圧縮器・理想NIDの反例ではない。
- n=2^mの6値で、指数mのElias gamma符号からnを生成する記述を検討。nの通常二進長そのものが最短prefix記述長に等しいとはいえないことの構成例。真のKを計算していない。
- 物理的100万回コイン、πの正規性の証明、一般の最短プログラムの計算、停止oracle、全入力の定理、完全NCD/LLM実験は実施していない。

## 一次資料の実際の参照範囲

- Alexander Shen, [Uppsala lecture notes (2007)](https://www.lirmm.fr/~ashen/uppsala-notes.pdf)。全31頁。取得PDFのSHA256 e5ee75cfdb1c7221100663973245d21f01732b5ad1d14638883793dc638a4789。返却抽出テキストの定義・最適復号器・非計算可能性／不完全性と、prefix節34–37の返却範囲を読んだ。**印刷26–27頁のみ画像を開いて実際に視認**。他の画像3–5、29頁は生成したが未視認、全巻読了ではない。記号Kがplain、KPがprefixである点に注意。prefix版に一律n+O(1)という上界を適用できないことを確認。
- Cilibrasi/Vitányi, [Clustering by compression](https://arxiv.org/abs/cs/0312044)：著者・版とabstractのみ。normal compressorの仮定と適用例を報告する研究で、未読の本文や図・実験を再現済みとしない。
- Jason Rute, [Computable randomness and betting... v4](https://arxiv.org/html/1203.5535v4)：abstract、導入・節2冒頭までの返却範囲のみ。ML、Schnorr、computable randomnessの区別と、computable bettingの定義を確認。後続定理の全証明は未読。
- Kohtaro Tadaki, [Chaitin Ω numbers and halting problems](https://arxiv.org/abs/0904.1149)：abstractのみ。最適機械と同じ機械の長さN以下の停止問題という対応の範囲を確認。
- Delétangほか, [Language Modeling Is Compression](https://arxiv.org/abs/2309.10668)：著者・版・abstractのみ。予測と圧縮の対応を扱うが、全実験未読・未再現。LLMから世界モデルやAGIが必然という証明として使用しない。
- Baileyの [π資料索引](https://www.davidhbailey.com/pi/) と [normality-digits-pi.pdf](https://www.davidhbailey.com/dhbpapers/normality-digits-pi.pdf)：検索返却の索引・導入抜粋のみ。PDF未取得・全体未読。πの正規性を証明済みという原稿の推論の根拠にはしない。
- Hutter Prizeの公式トップ取得は502。現行の賞・コーパス・引用を確認済みとはしない。
- 最初のShenローカル取得はPythonの証明書チェーンエラー。証明書検証を無効化せず、WindowsのInvoke-WebRequestで取得成功。web screenshotは参照文字列のみ返却され実画像の視認に使えなかったため、ローカルで生成した26–27頁をview_imageで読んだ。一次資料への最終アクセス障害ではない。

## 次に行うこと

日本語原文を全7テーマを保って修正し、擬似コードと実行可能な補助教材を区別する。一次資料の未確認箇所を必要分だけ追加照合し、改稿全文・数式・図・コード・HTMLを再確認してから原文を凍結する。英語の固有の誤り・正しい補足を反映して全文照合し、残り11言語を各本文全体で順次読む。**この時点では校閲記録を追加しない。**


## 追加の原稿読了と一次資料 — 2026-11-13

簡体字・繁体字各111行をメタデータ・全4章・表示式・2図の全ラベルと接続・表・末尾式まで実際に全文読了。改稿・承認はまだしていない。初期棚卸しと上記の「他11未読」は時系列の初期状態として保持し、現在の未読は他9言語。両中国語版はπの「小数点後」と書きながら整数部11で始まる例を置き、Berry例を「最大の正整数」と誤訳している（定義できない整数は無限にあり最大値はない）。14漢字との計数も実文字列で再確認。式のapproxがU+0007 BELに、theta/text/fraction等の一部がエスケープ由来の制御文字／タブや脱落に壊れている箇所を実読した。簡体字に韓国語の마커스 후터が混入。繁体字の隨機種源は情報源の文脈で不適切。BBPの滴定という訳も数学の桁抽出として整理する。点質量でエントロピー0という両版の補足はモデル依存の正しい例なので保持し、原文の誤りを一律に転用しない。具体的な文字数・制御コードはbatch-035-cn-tw-original-reading.json、本文はまだ不変。

一次資料追加：Rute v4の返却範囲で節2定義2.4–2.5と節3.2定義3.3–3.4、式3.1および定理3.6–3.7の記述を確認（後続証明全文は未読）。Cilibrasi/VitányiのHTML版 https://arxiv.org/html/cs/0312044v2 の検索返却箇所、節3.1定義3.2と周辺の対称性・近似論、補題3.5を確認。冪等性・単調性・対称性・分配性は加法O(log n)の仮定を持ち、NIDの理論を無条件で実圧縮器へ転用できないことが明記されている。全実験や全文読了を主張しない。

スペイン語・韓国語の旧稿各111行もメタデータ・4章・全表示式・2図の全ラベル接続・表・末尾を実際に全文読了。π小数部の例が11で始まる、コイン実現値の無条件高複雑性、自己区切り長の扱い、10000bitという未測定の固定余裕・shortlex・健全性、期待値関係やLLM/MDL同値の過剰断定を確認。両版のBEL/form-feed/タブ由来の数式破損を記録。スペイン語Berryの例は「最小」であり中国語の「最大」誤りはないが、14語という主張に対し空白区切り13語。韓国語は「十語ほど」で実際に10語、計数誤りを転用しない。スペイン語のmore than cとat least cの文間不一致、韓国語の이상（以上）と厳密不等号の差も直す対象。両版とも点質量H=0の補足はモデルに依存する正しい例として保持。図は全英語ラベルであり、翻訳時に内容とともにローカライズする。改稿・承認はまだ0。現在原稿読了はJA/EN/CN/TW/ES/KO、未読7言語。根拠batch-035-es-ko-original-reading.json。

ポルトガル語・フランス語旧稿各111行をメタデータ・4章・全式・2図全ラベル接続・表・末尾まで全文読了。共通のコイン実現値の保証、prefix整数長、c境界、未測定10000bit、shortlex、健全性やモデル条件の不足、LLM/最適圧縮/因果モデル必然の断定を確認。制御文字・タブ由来の数式破損は個別計数。PTのBerry例は14語なのに15語、FRは12語なのに14語と記載。両者とも最小整数の趣旨は正しく、中国語の最大整数誤りを転用しない。FRのΩは前n桁から長さn以下の停止問題を解けるという片方向を正しく述べており、他版の同値という誤記を転用しない。PTは単にBBP algorithmといい、他版の滴定などの誤訳はない。元のstationary ergodicの平均複雑性/長さ→エントロピー率の補足は、有限アルファベットの定常エルゴード的過程のBrudno型関係として残せる（原文の条件付き計算可能分布の定数誤差の主張と混同して、ここまで計算可能性必須としない）。現在JA/EN/CN/TW/ES/KO/PT/FRの原稿読了、他5言語未読、改稿・承認0。根拠batch-035-pt-fr-original-reading.json。

ドイツ語・ヒンディー語旧稿各111行を全範囲で読了。メタデータ・4章・式・2図・表・末尾まで確認し、共通のprefix長、コイン実現値への保証、c境界、固定10000bitと図1000bit、理論の健全性、計算可能予測と実圧縮・知能の混同、制御文字の数式破損を個別に記録。独語Berryの例は15語で15語との記載が正しいので他版の計数誤りを転用しない。ヒンディー語は空白区切り16語で14語ではない（依然20語未満で趣旨は保てる）。両者とも最小整数を正しく述べ、中国語の最大誤訳はない。独語Ωの説明は片方向で正しく、後半の一般的な表で「haltingと同値」とした主張とは分けて扱う。独語の固定オーバーヘッドが完全に消えるという表現は、長さで正規化した相対効果との区別が必要。ヒンディー語ではअकलनीय／計算不可能性とअपूर्णता／不完全性、निश्चरताの不変性の訳と正規化・上界・予測を整理する。点質量H=0と定常エルゴード的な率の補足は条件を明示して保持。現在JA/EN/CN/TW/ES/KO/PT/FR/DE/HI原稿読了、ID/RU/AR未読、改稿・承認0。根拠batch-035-de-hi-original-reading.json。

インドネシア語・ロシア語・アラビア語の旧稿各111行をメタデータ・4章・式・2図の全ラベル接続・表・末尾まで全文読了。共通の数式・記述長・コイン・c境界・ML検定・モデル条件と知能必然の断定を確認。各版の制御文字・タブによる破損を個別計数。IDには定義文にタイ語เมื่อが混入。IDのBerry例は空白区切り14語に対して15語、RUは10語に対して12語。ARは11語で11語という計数が正しく、計数誤りを転用しない。RUはΩから停止問題への片方向を正しく述べ、他版の同値という誤記を転用しない。ARのOccam razorをشفرة（コード・暗号）とする語とpigeonholeをبرج الحمام（鳩の塔）とする語を、規則・原理と引き出しの数学用語へ整理する。全英語ラベルの2図も対象言語へ訳す。現在全13版の旧稿本文を実際に読了したが、原文・翻訳の改稿や改稿全文照合はまだで、承認0／台帳420不変。初期未読フラグ・時系列メモは上書きしない。根拠batch-035-id-ru-ar-original-reading.json。

既存eyecatch.jpgを実際に視認。星空風の背景に、左は規則的な金色の幾何／フラクタル線、右は不規則に散った色付きガラス片風の抽象図。読める数式や定理、実際のコイン実験、数学的非圧縮性の測定証拠はない。概念的な挿絵として保持可能、ハッシュ不変。全13原稿と画像の初期ハッシュ一致を再確認した。初期visuallyRead=falseは時点記録として保持。

Hutter Prize公式トップの再取得も502。関連著者ページ https://www.hutter1.net/ai/aixigentle.htm は取得でき、著者・版・abstractを読んだ。AIXIは意思決定と普遍帰納の理想モデルで、計算不可能という制約を明記。70頁本文・最適性の全定理や証明は未読。LLMとAIXIの同一性やAGI獲得の証明として使用しない。賞の現行条件・サイズ・直接引用は未確認のまま。

## Japanese revision and freeze — 2026-11-13

改稿日本語の実ファイル1–280、281–544行を全文読了。最初のドラフトはdocs/drafts/kolm035-ja-initial.mdにSHA b09008615f5e9aaaf6d9b8b1cbd13c4bd8aedae7d26205f275a0fa2eb23e45cbで保存。6種類の最終置換（最適機械の基準の早期明示、カウントの表現、半数の表現、丸めた割合の下界表現、Ωの有限二進小数でない説明、Brudno文献差替え）を別途読了。22箇所の強調を可逆性検査付きで明示strongにし、全て実HTMLに残ることを確認。原文の7テーマ、通常／prefixの定義、同クラスの最適性と証明、計算可能接頭辞K(n)、条件付き長、鳩の巣の全証明とcの範囲、ML検定と一様定数、Berryと健全な理論の非有界下界探索、Ωの同機械停止問題、平均とエントロピー率、離散mと逐次M、尤度とMDL、NIDと実NCD、モデル/メタデータ/トークン化を含む予測符号長を保持して修正。物理実験やπ正規性、世界モデル/AGI獲得を証明したとはしていない。2つの証明コードはtextの擬似コードとして明示し、実行可能なKや停止oracleは存在しないことを説明。掲載実行プログラム0。

重要な訂正：予備調査候補14の「旧JAの部分和が下端aに達したでは不十分」という解釈を取り下げる。a<Ω<a+2^-Nならq_s=aでもΩ-q_s<2^-Nが成立する。旧JAのこの条件は誤りと認定しない。改稿のq_s>aは有効な十分条件を選んだもので、旧等号の数学的失敗を直したとは記録しない。16個の有理数による残量例でも等号で十分なことを確認したが、その例1/3は実際のΩではなく計算可能な教材値。

追加の独立有限検査：Elias gamma整数1..1023の全符号と復号、prefix-freeとKraft和1023/1024、965有理分布のHuffman平均長とentropyの不等式、2445個のSFE区間符号、長さ1..9の二値逐次モデル全1022列で確率和・dyadic区間包含・prefix-free・符号復元を検査。これはKを計算した結果、定理全入力の証明、LLMコーパス実験、完全算術圧縮器や性能実測ではない。先行の153計数・gzip有限例等は不変の証拠を参照し未再実行。

初回JAビルドでは224TeX／38表示式、2図6+5辺、8参照、2擬似コード、224説明断片、22強調とナビゲーションが通り、既存17テストも成功。しかしselected36束プレビューの11言語×home/post RSS＝22XMLがC0制御文字で不正となりHTTPS検査が停止。初回build/check/validationとXML診断を保存。これはselected previewで確認した潜在的なRSS不正であり、本番の全RSSが今壊れているという調査結果ではない。旧全13本文読了と全制御文字の個別文脈確認後、11言語にBEL+pprox、form-feed+rac、TAB+ext/heta/oだけ117箇所のTeX escape復元を行った。元ハッシュと全置換数、復元後ハッシュをbatch-035-escape-repair.jsonに記録。他本文/メタデータは不変で、機械的復元は全文意味校閲ではなく承認0。初期の未変更という検査を無理に成功させず、新R2検査はこの修復manifestの正確なハッシュを検査する。

新規36束R2ビルドで468post原稿＋既存Hindiタグ設定1ファイルの完全一致、2035多言語頁、HTTPS3709HTML41XMLと既存17テスト再実行が全成功。警告は保存し、postだけのpreviewで全サイト/ブラウザ/KaTeX/Mermaid実行検証ではない。原文をSHA c7c4b56ae79a864e3bfa4bf30fa1f73074087c50ccb5e3ec1a751ffcea46d2a6で凍結。まだbatch035翻訳レビューは空、AI420／未確認12,612／人0。次に英語の旧全文を踏まえ改稿し、改稿の全文を照合する。公開は全12翻訳の照合・組立検証後。全記事goal継続。

一次資料追加の実範囲：Petersen lecture PDFのweb返却6.10節と定理6.11の記述を読んだが、ローカル取得はUNC403で失敗し画像視認はしていない。ChazottesのClay講義スライド全53頁を取得、SHA f840e01e3d18a5e7ddcbd66bee80effd18d974d0f32c4824da852572795df117、スライド50のみテキストと画像を実際に読了。有限分割・エルゴード的測度に関するBrudnoの式と仮定を確認し、記事の参照はこちらへ変更。全53頁の読了や証明の再現はしていない。web findの一時timeoutは取得失敗と区別し保存する。

## English full comparison — 2026-11-13

Original English537 lines were fully read in the documented prior ranges, with metadata, all7chapters, equations, both complete graphs, both proof pseudocodes and tables. Actual revised file read1–280,281–557 and three final replacements separately: clarified the first heading, removed an editorial sentence referring to the original comparison, and replaced awkward “shortly describable” wording. Full thematic translation of frozen Japanese, not a summary or semantic approval inferred from structural equality.

Corrected guaranteed incompressibility of every fair-coin realization, model/normality claims, unconditional prefix n+O(1) and endpoint log(n) equalities, universal-versus-optimal class distinctions, c domain and strict compression-saving boundaries, computable-martingale versus ML-random equivalence, uncontrolled numerical Chaitin/ZFC thresholds, discrete m versus sequential M, general Bayesian likelihood versus conditional K, exact concatenation versus encoded-pair NID, real compressor universality, and model/tokenization/precision/metadata costs in prediction codes. Did not assert that compression forces causal models or AGI. Two original Python-looking oracle/proof-enumerator blocks are now explicitly text pseudocode, with shortlex and unbounded numerical theorem-bound search; no executable article program or K/Omega oracle exists.

English-specific scope: original raw-binary storage distinction, theorem statement specifying additive optimality, strict Omega crossing and Berry phrase eleven words were already valid and are not assigned Japanese or other languages’ errors. Original rigged-machine constant >=1million claim corrected without assuming that particular string is incompressible. Preserved eleven-word natural-language example, and retained explicit NID relation with uniquely decoded K(x,y), R=max complexities>0 and O(log(R+2)/R) error as an additional English display. Original Russian десятки in the first diagram removed. Original enwik8/enwik9 both described as100MB was removed without claiming current prize conditions or its inaccessible official page verified. Upper approximation stabilizes for each fixed input but has no general final-value recognition procedure.

Primary addition: actually read returned Cilibrasi/Vitanyi HTML section3, Remark3.1 and equations3.1–3.2 via open/find. Conditional complexity numerator and encoded pair relation have logarithmic precision. Did not read the whole paper, certify all its other statements or reproduce phylogenetic/music experiments. Earlier selected-page/abstract scopes remain. No new whole-paper/standard/browser/KaTeX/Mermaid runtime claim.

Draft-generation first attempt failed before any file write because regex replacement interpreted a JSON Unicode escape; changed to a callable replacement. Old English file remained original at that point; subsequently generated and read actual revised557lines. This is not an article/build failure. First English fresh36-bundle build passes, with no invented retry. Common38 display blocks equal frozen JA apart from the ML annotation, plus one English NID display; all219 TeX expressions and281 prose fragments exact in generated HTML,21strong spans,2graphs6+5edges,8refs,both text pseudocodes,two tables,canonical14hreflang13sidebar,title/date/image/taxonomy. Final English LF SHA256 0819c990de12f88e7ed711c0a589a33cad4e6e4c65b3c9ddaa6fd3060a88f06c. Frozen JA c7c4b56ae79a864e3bfa4bf30fa1f73074087c50ccb5e3ec1a751ffcea46d2a6 unchanged. All11 prior mechanical repair hashes unchanged; they remain semantically unapproved.

Fresh468 exact post snapshots plus1existing Hindi taxonomy frontmatter,2035multilingualpages,HTTPS3709HTML41XML and pre-registration ledger420/12612 pass. Existing17tests and finite auxiliary evidence reference JapaneseR2 success, not rerun for English content-only work. Only English registered as Codex(AI) November13 with allfive notes/date/hashes/limitations, prior420ledger objects unchanged. Current421AI/12,611unreviewed/0human. Other11 full revised semantic comparisons, assembled publication and whole goal pending. Next simplified Chinese rewrite/full reading against frozen source; never approve from mechanical escape restoration alone.
