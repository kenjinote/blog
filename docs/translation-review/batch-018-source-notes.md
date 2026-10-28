# Batch 018: C++ primality testing — source investigation

Started 2026-10-28. Article: `cpp-fast-prime-testing-miller-rabin`.

The complete original Japanese and English metadata and bodies were read in three bounded outputs each. The other eleven translations have not been read or reviewed at this stage. This investigation alone creates no review date. Original normalized hashes and executable reproductions are in `batch-018-source-audit.json`.

## Reproduced problems and distinctions

- The original complete C++ program compiles under WSL GCC 13.3.0/C++17 and prints the six expected sample classifications. This does not establish all-input correctness.
- The separate signed modular-power helper returns `1` for `(2,0,1)` and `-3` for `(-2,3,5)`. Zero modulus produces a UBSan division-by-zero error. Its input contract is missing.
- The trial-division expression `i*i<=n` overflows at odd `i=3037000501`, `n=LLONG_MAX`. Only the isolated expression was exercised, not billions of iterations of the whole trial function. The first `-O1` probe optimized away the multiplication; repeating the same expression at `-O0` exposed the UBSan error. Both outcomes are preserved.
- C++ signed `-1 % 7` evaluates to `-1`. The least nonnegative residue of mathematical −1 is 6; these must not be equated as language expressions.
- A counter added to the copied full Miller–Rabin implementation counts 852 modular multiplications for `18446744073709551557`, already exceeding the article's 448-basic-operation promise. This is instrumentation, not a timing benchmark.
- The seven listed bases are integers, not seven primes. The full program already uses unsigned 128-bit intermediates, which are appropriate for full unsigned 64-bit products; a signed 128-bit intermediate does not cover that entire range.
- Correct fixed-base interval statements are separate from the error bound for independent uniform random bases. Passing a random round is not a primality proof or a posterior probability assertion.
- Carmichael numbers fool Fermat bases coprime to them, not every arbitrary base. `561` fails Fermat with base 3.
- Preserve the useful trial/Fermat/Miller–Rabin progression, the 3/4/7-base optimization, the alternative first twelve primes, and Montgomery's purpose. Correct input domains, strict interval endpoints, classification of 0/1, base-zero comments, complexity units and unsupported universal speed claims.
- A fixed-width 64-bit teaching routine is not an RSA-size prime generator or a cryptographic library audit. No new native-language or production-security certification is implied.

## Primary sources and actual reading scope

- [GCC, 128-bit integers](https://gcc.gnu.org/onlinedocs/gcc/_005f_005fint128.html): complete short documentation, including target-dependent support and signed/unsigned distinction.
- [C++ working draft, multiplicative operators](https://eel.is/c++draft/expr.mul): complete short section; division/remainder, zero-divisor undefined behavior and truncation toward zero. The local compiler reproduces the signed-remainder example.
- [Rabin (1980), original paper](https://math.nyu.edu/~goodman/teaching/Algebra_2_2021/MillerRabinTest.pdf): parsed opening pages through Theorem 1, including randomized error interpretation and warning against treating it as a proof. Did not read the full proof or later implementation sections. Obsolete 1980 general-primality status is not reused.
- [HAC chapter 4](https://cacr.uwaterloo.ca/hac/about/chap4.pdf): parsed §§4.2.1 and 4.2.3, Facts 4.20/4.23/4.25, Algorithm 4.24, and Note 4.47's distinction between conditional error directions. Also inspected the scoped historical notes on Miller/Rabin. Not a whole-chapter or present-day key-generation standard audit.
- [Published SPRP base records](https://miller-rabin.appspot.com/): read the tables for the 3/4/7-base sets, strict thresholds, remarks on reducing bases, and the attribution/date of Sinclair's seven-base result. This is the maintained record of the search results; its full 64-bit database was not independently reproduced. Its zero-base remark is interpreted as passing that round, not immediately declaring the whole integer prime.
- [Sorenson–Webster preprint](https://arxiv.org/html/1509.00864): parsed introduction and Theorem 1.1, giving the first composite passing the first twelve prime bases. [Published journal metadata](https://doi.org/10.1090/mcom/3134) identifies Math. Comp. 86 (2017), 985–1003. Not a full computational proof replication. The generated HTML's displayed 2026 date is not substituted for the preprint's 2015 or journal's 2017 dates.
- Montgomery (1985): publisher PDF/page access failed; UCSD's [scan](https://cseweb.ucsd.edu/classes/fa06/cse246/montgomery.pdf) opened but supplied no parsed text or usable image in these tool results. Only bibliographic/abstract search information was available. Do not claim the full paper or algorithm was read. Obtain a readable primary algorithm source before adding implementation details.
- RSA assumptions and the factorization/primality distinction were investigated in preceding batches 013–017. No fresh full RSA specification review is claimed here.

## Pending

Fix and independently reread Japanese and English; validate all revised code blocks and mathematical/diagram/link structure; then read each remaining language in full. Unread or machine-only checked translations must remain unreviewed. Full-site CI and publication verification follow actual review records.

## Subsequent source revision and actual validation

Readable HAC chapter14 parsed Algorithms14.32/14.36/14.94 and surrounding efficiency/representation/setup conditions. This supports the corrected Montgomery discussion; no original-paper reading claim is added.

Japanese and English were rewritten and independently reread in full. During rereading, the first rewritten diagram lacked a pre-loop exhaustion check for s=1; both were corrected before review recording. Added explicit initializer_list header. All3blocks separately compile; complete11sample outputs pass. Each version passes101275cases under O2 and UBSan (sieve0..50000 for both algorithms, signed/boundary/large numbers, fulluint64 multiplication/power and zero-modulus exceptions). Exact counts and hashes are in batch-018-ja-en-validation.json. All82TeX expressions survive minified HTML. Hugo19bundles, multilingual1185pages and HTTPS2163HTML/41XML pass. Eleven translations remain unread and unreviewed.
