# Batch034: error-correcting codes — original audit

2026-11-13. This is preliminary work, not translation approval. Current ledger: 408 AI reviews, 12,624 unreviewed, zero human reviews. Batch033 is separately closed by matching CI and live442article+3tag evidence.

## Actual reading scope

Read complete original Japanese and English metadata, all eight sections, equations, comparison/output tables, four complete Mermaid diagrams per version, and the complete Python block per version. Japanese was read in lines1–170,171–340,341–500,501–end; English in1–170,171–338,339–500,501–end. Other11 bodies have not been read: their file hashes/structure inventory do not approve them. No revised body exists yet.

Preserved originals are identified by baseline commit and normalized-LF hashes in batch-034-source-audit.json. In particular the original English program is not a literal translation of the Japanese program: Japanese uses GF(257), English constructs GF(2^8) using 0x11D. These differences must be reconciled deliberately, not certified by equal block counts.

## Executed original programs and finite counterexamples

batch-034-original-code-probe.json contains the two actual standalone subprocess results, full stdout/stderr, displayed text outputs and code/source hashes. Both programs exit successfully for their demonstration inputs and reconstruct VOYAGER-1, but both displayed output blocks differ from actual stdout.

At fixed correction radius t=3, additional actual calls with zero, one or two corrupted symbols fail in the original Japanese routine with IndexError and the equivalent English linear-system path with StopIteration. Exactly three errors in the tested patterns recover the message. Four tested errors return a different message without rejecting it. This demonstrates these inputs only; exceeding a code's guaranteed radius cannot in general always be detected, even with verification. A replacement must solve rank-deficient systems appropriately, divide Q by E or otherwise justify reconstruction, validate received distance and clearly state its guarantees.

The Japanese GF(257) evaluation of byte-valued coefficients [255,1] at x=1 is256, so its symbols cannot all be serialized as individual bytes. This educational prime-field code must not be called a QR GF256 implementation. The English field multiplication was checked independently against shift/XOR polynomial reduction for all65,536byte pairs;255nonzero inverse checks passed. This validates those finite arithmetic operations, not the complete decoder or QR/spacecraft interoperability.

batch-034-original-forney-probe.json checks the article's explicit convention:

- S_j=Y X^j, with j starting at1.
- S(z)=S_1+S_2 z+… and Λ(z)=1−Xz for one error.
- Ω(z)=YX and Λ′(z)=−X, so −Ω(X^-1)/Λ′(X^-1)=Y.
- The extra X in the original formula instead returns XY.

Using the original GF256 arithmetic, all65,025nonzeroX/nonzeroY pairs match the formula without extraX;64,770pairs disagree with the article's extraX formula. Witness X=2,Y=3 gives6instead of3. Different first-root/syndrome conventions can legitimately alter an X factor; this finding concerns the explicit convention in this article, not every Forney formula.

The first auxiliary script incorrectly asserted65,535cases instead of255×255=65,025. It failed before writing a receipt and is preserved as probe_batch_034_forney_initial.py. Only the expected count was corrected; arithmetic and64,770mismatches were unchanged. The successful corrected script and receipt are separately preserved. This was an auxiliary counter, not an article-code failure.

## Initial mathematical/editorial concerns, not all yet externally verified

- 10^-16W is100aW, not0.1aW. Current spacecraft distance, radio-link values and historical image/coding claims need primary verification.
- QR restoration percentages concern codewords and conditions, not arbitrary image area/logo coverage or a universal10ms guarantee.
- Discrete memoryless channel capacity can be zero. Continuous AWGN capacity needs input-power/bandwidth/noise assumptions and consistent units. Small asymptotic block error is different from finite zero-error capacity. ln2 is a limiting AWGN bit-energy ratio, not a universal physical constant for every channel.
- An arbitrary correctable radius satisfies t≤floor((d−1)/2); this is not equivalent to equality for every t. Error/erasure guarantees must quantify all patterns. Zero syndrome means membership in the code, not proof that the channel caused no errors.
- The Japanese perfect-code classification and Golay/Voyager paragraph need research; the English omits it. Binary-order and systematic parity-check matrices require different syndrome-to-position interpretation. General complexity and ECC DRAM claims cannot be universalO(1)/everymodule assertions.
- Polynomial root counting over a field needs the factor theorem, not a claim that the algebraically closed-field fundamental theorem applies to finite fields. Evaluation n≤q, cyclic full lengthq−1 and shortening must be distinguished; QR root-index conventions must be checked.
- LDPC sparsity alone does not forbid short cycles. Dimension is n−rank(H), not necessarily n−numberofrows. The Gaussian BPSK LLR needs its amplitude/prior assumptions. Threshold predictions, finite implementation performance and the ultimate wideband bound must not be conflated.
- Polar symmetric capacity under uniform input is not unrestricted capacity for an asymmetric channel. Finite length, SC versus list-dependent SCL costs and actual5G short-control-block exceptions require accurate scope.

## Primary-source reading so far

Only the following returned excerpts/abstracts have been read. No new complete PDF, video, entire paper, standard or hardware experiment has been reviewed.

1. DENSO WAVE, https://www.qrcode.com/en/about/error_correction.html and https://www.qrcode.com/en/about/ . Read returned official search text explaining restoration as a fraction of total8-bitcodewords, redundancy example and damage limitation; opened the canonical pages, whose extracted text is partial (15and64lines). The page opening did not expose every graphic/table. The source does not justify an arbitrary30%surface-area logo guarantee.
2. JPL TDA42-73, https://tda.jpl.nasa.gov/progress_report/42-73/73C.PDF . Read official search-returned introduction excerpt: K7/rate1/2 convolutional plus depth4interleaved(255,223)RS on Voyager, predicted versus practical errors/synchronization losses. No PDF body/figures viewed yet.
3. JPL TDA42-88, https://ipnpr.jpl.nasa.gov/progress_report/42-88/88G.PDF . Read official returned introductory excerpt on concatenation and2e+E≤32. No whole paper read.
4. JPL TDA42-71, https://tda.jpl.nasa.gov/progress_report/42-71/71J.PDF . Read returned intro about planned1986Voyager2firstflight use, code parameters and mission-specific conventions. Historical wording is contemporaneous, not a current status claim.
5. JPL DSN810-005module206RevE, https://deepspace.jpl.nasa.gov/dsndocs/810-005/206/206E.pdf . Read returned selected4.4.1–4.4.3excerpts on uncoded/RS/convolutional tradeoffs, not the complete module.
6. JPL42-54, https://tda.jpl.nasa.gov/progress_report/42-54/54K.PDF . Read returned abstract/intro excerpt on a transform decoder and error/erasure conditions. No timings or decoder implementation reproduced.
7. Arıkan, https://arxiv.org/abs/0807.3917 . Read returned original abstract describing symmetric capacity, uniform input, rate belowI(W), asymptotic error andO(NlogN). Body not yet read.
8. Arıkan–Telatar, https://arxiv.org/abs/0807.3806 . Read returned abstract on sufficiently largeN andβ<1/2; body not yet read.
9. Forney MIT notes, https://ocw.mit.edu/courses/6-451-principles-of-digital-communication-ii-spring-2005/01060b08ba74792ee8d85eb82b9efdb4_chap8.pdf . Read returned selected8.3.1/Theorem8.5evaluation-code excerpt n=q; PDF body not yet read.
10. MIT6.441chapter22, https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/7553afe00a3630164b8e774456d0fdcf_MIT6_441S16_chapter_22.pdf . Read selected search-returned concatenation/RS excerpt; not whole chapter.

Other search results, including unrelated MathWorks optimization pages, secondary QR articles and later polar papers, are not relied on as verification. Next: read necessary primary bodies, independently reproduce remaining mathematical examples, reconcile implementations and correct Japanese before reviewing translations.
