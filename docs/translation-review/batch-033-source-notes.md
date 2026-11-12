# Lossless compression: initial source review

2026-11-12 JST. AI reviewer: Codex. Article directory: `content/post/lossless-data-compression-shannon-entropy-huffman-lz77-arithmetic-coding-ans`.

## Reading and inventory

Read the complete original Japanese `index.ja.md` (434 lines) and English `index.en.md` (388 lines), including metadata, all six numbered sections, every formula, both complete Mermaid diagrams, the BWT table and performance comparison table. There are no executable article programs in these two versions. Other eleven language bodies have **not** been read. Their metadata/structure inventory is mechanical evidence only. Japanese has 33 display-math pairs and English 27; most other versions have four sections and six pairs (Chinese versions have nine pairs), compared with six sections in Japanese and English. This is a reason to investigate omissions, not approval of unread translations.

Baseline hashes, effective publication dates, raw dates, assets and runtime-library presence are in `batch-033-source-audit.json`. The successful 34-bundle baseline build is separately retained. No article rewrite or translation-review record has been made for this batch. Ledger remains 396 AI / 12,636 unreviewed / 0 human.

## Findings from the original article

- The counting bound concerns a **fixed injective encoder**. The Japanese claim that the remaining files cannot be shortened by *any* algorithm changes the quantifiers. English says “fixed” in one passage but calls the remaining strings completely incompressible and repeats an unqualified conclusion. Kolmogorov-complexity statements need a fixed description language and decoder-description costs. For a particular file, a specially chosen swap encoder can map that file to the empty string while expanding the empty string; this is not a universal compressor.
- The illustrative 8,388,608-bit “1 MB” is 1 MiB, not decimal MB. Japanese calls ASCII an eight-bit character code. Both texts overgeneralize ordinary compression percentages, compressed/ciphertext recompression and randomness. Uniform sampling, model assumptions and overhead must be separated from claims about each file or every algorithm.
- The expected-length/Kraft/KL derivation is useful and should be retained with its domains. Zero probabilities, single-symbol conventions and iid assumptions for the block bound need explicit treatment. Japanese omits independence at the block step; English states it. In English prose, normalized Q=2^-ℓ/Z is silently replaced by unnormalized 2^-ℓ while the slack term remains, double-counting it. The display identity using normalized Q is correct.
- Arithmetic coding's ideal payload bound below information plus two bits does not include model transmission, message length/termination, finite precision or headers. It is not a universal two-bit bound for an entire file. Ideal predictive log-loss and an integer serialized bit length are not exactly equal. Reversible tokenization, synchronized probability calculations and shared model costs matter. An optimization relationship does not establish intelligence or understanding, nor the full training objective of every named commercial model.
- The tANS interval `[L, 2L-1)` contains L-1 integer states. Use `[L, 2L)` or the closed integer set from L through 2L-1. A raw rANS bijection does not itself provide a complete framed compressor, zero-overhead representation or a one-cycle CPU guarantee. State zero also needs care in logarithmic size explanations.
- Huffman optimality is conditional on weights and the prefix-code class. Single-symbol conventions and potentially long codewords contradict universal “at least one bit / exactly one table lookup” claims. Historical anecdotes and universal CPU-speed ratios need sources or qualification.
- LZ overlap must follow forward-expanding copy semantics, not a generic overlapping memcpy or snapshot memmove. LZSS flags can expand unmatched data. Fixed-window implementations do not automatically inherit all asymptotic universality statements.
- Zstd literal coding can use raw/RLE or one/four Huffman streams. Sequence FSE states differ from those literal streams. DEFLATE and LZMA2 format properties need their own primary specifications. Speed, RAM, ranking and exact level-independent decompression claims lack reproducible CPU/version/corpus/command conditions; no benchmark has been reproduced.
- BWT's last column preserves symbol count, while the index/sentinel and framing have costs. The banana table is correct in the independent reproduction below. Linear inverse-time statements need alphabet/rank assumptions. The Japanese second diagram contains Chinese “紧凑”. A Transformer should not be described as a recurrent network. “he ” almost always preceded by t/T is an unsupported English-frequency assertion.

## Independent finite mathematical checks

`probe_batch_033_math.py` is the exact script used for `batch-033-original-math-probe.json`; SHA-256 `7a88e0f8feaf08c320a41e96560dd787bf9f7f8757656cb44860a01857edc46a`. The receipt guard preserves the initial result. These are auxiliary experiments on the read formulas, **not execution of article programs**.

- 136 exact counting cases, n=1..16 and c=1..n; 510 separate file-specific swap encoders. They illustrate quantifier distinctions and are not enumeration of all compressors or a Kolmogorov-complexity proof.
- Four interval cardinalities reproduce the tANS off-by-one, including L=1024 giving 1023 states under the original half-open endpoint.
- 1,093 BWT/LF roundtrips over abc strings of length 0..6 with a unique sentinel. `banana$` gives `annb$aa`, primary index 4, and the seven listed sorted rows agree.
- 650 positive frequency profiles, totals M=2/4/8/16 and 1..4 symbols; 308,096 rANS state/symbol roundtrips and 166,400 encoded-state inverse checks. These do not implement renormalization or serialization.
- 511 exact-rational arithmetic interval cases for a fixed binary 1/3,2/3 model and lengths 0..8, checking a contained dyadic interval. Model/length are known; no finite-precision full compressor is claimed.
- English KL counterexample: P=(1/2,1/2), lengths=(2,2), Z=1/2. Correct H=1, normalized KL=0, slack=1, L=2. Using raw Q=(1/4,1/4) and also adding slack gives the incorrect total 3.

## Primary research actually read so far

These reading ranges refer to tool-extracted HTML, not full-paper or figure inspection. No additional PDF pages were viewed for batch033. Paper citations/bibliographies are not automatically sources read.

- [RFC 8878](https://www.rfc-editor.org/rfc/rfc8878.html): introduction and selected returned excerpts, then sequence-code/execution text and tables around lines 541–700. Literal section around 378–478 distinguishes one/four Huffman streams. Sequence decoding around 620–640 maintains separate literal-length, offset and match-length states and reads the bitstream backward. It is an informational RFC, not an Internet Standards Track document. Rest remains unread; table values were not all independently reproduced.
- [Duda 2013, revised 2014](https://arxiv.org/html/1311.2540v2): metadata/abstract, selected excerpts at 78/203, then text/formulas around 123–227, including rANS equations and the closed integer interval `{l,...,2l-1}`. Other sections, detailed table construction, figures, performance and encryption claims remain unreviewed. Some source text has p/q or terminology slips; do not import them mechanically. No modern cryptographic assurance is inferred.
- [Language Modeling Is Compression, 2023/revised 2024](https://arxiv.org/html/2309.10668v2): abstract; selected excerpts at 78–80, 182–210 and conclusion; text around 84–122 and 144–174. It distinguishes raw from model-size-adjusted rates and describes 2048-byte chunks and transformed image/audio data. Its raw headline comparisons exclude model parameter cost. No experiment reproduced; no complete paper/appendix/figure reading. Its casual algorithm-family description is not authoritative for DEFLATE/LZMA2 internals. Use format specifications for those claims. Preserve our independently justified conservative arithmetic bound rather than blindly adopting rounding notation.
- Earlier scoped Shannon/Huffman reading remains in `batch-032-source-notes.md`; this is not a new full reading of those papers.

## Outstanding

Finish relevant primary specifications and research checks; correct the Japanese article without losing its proof, algorithm, BWT and engineering themes; fully compare the revised English and each other translation, restore omitted material, execute appropriate finite checks and generated-HTML validation, then register only actually reviewed versions. Batch032 publication is still separate: run43213662116 attempt1/head f8ca0959a was observed building Hugo at 21:04 JST. Do not restart it or certify live publication early.
